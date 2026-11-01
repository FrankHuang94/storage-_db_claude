#!/usr/bin/env bash
# Render every Mermaid block with mmdc; exit non-zero if any block fails.
# Usage: bash scripts/lint_mermaid.sh [file.md ...]   (default: all docs/**/*.md)
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

CHROME="${PUPPETEER_EXECUTABLE_PATH:-/opt/pw-browsers/chromium}"
if [ -x "$CHROME" ] || [ -e "$CHROME" ]; then
  printf '{"executablePath":"%s","args":["--no-sandbox","--headless"]}\n' "$CHROME" > "$TMP/pc.json"
else
  printf '{"args":["--no-sandbox","--headless"]}\n' > "$TMP/pc.json"
fi

if ! command -v mmdc >/dev/null 2>&1; then
  echo "mmdc not found: npm i -g @mermaid-js/mermaid-cli" >&2
  exit 2
fi

if [ "$#" -gt 0 ]; then
  FILES=("$@")
else
  mapfile -t FILES < <(cd "$ROOT" && find docs -name '*.md' | sort)
fi

fail=0; total=0
for f in "${FILES[@]}"; do
  [ -f "$f" ] || f="$ROOT/$f"
  [ -f "$f" ] || { echo "missing: $f"; fail=1; continue; }
  # extract each mermaid block to its own .mmd so failures are attributable
  base="$(basename "$f" .md)"
  python3 - "$f" "$TMP/$base" <<'PY'
import sys, re, pathlib
src, prefix = sys.argv[1], sys.argv[2]
text = pathlib.Path(src).read_text()
blocks, cur, inside = [], [], False
start = 0
for i, line in enumerate(text.splitlines(), 1):
    s = line.strip()
    if not inside and re.match(r"^```\s*mermaid\s*$", s):
        inside, cur, start = True, [], i
        continue
    if inside and s == "```":
        blocks.append((start, "\n".join(cur)))
        inside = False
        continue
    if inside:
        cur.append(line)
for n, (ln, b) in enumerate(blocks, 1):
    pathlib.Path(f"{prefix}__{n:03d}__L{ln}.mmd").write_text(b + "\n")
PY
  for mmd in "$TMP/$base"__*.mmd; do
    [ -e "$mmd" ] || continue
    total=$((total+1))
    line="${mmd##*__L}"; line="${line%.mmd}"
    if ! out="$(mmdc -q -p "$TMP/pc.json" -i "$mmd" -o "${mmd%.mmd}.svg" 2>&1)"; then
      echo "FAIL  $f:$line"
      echo "$out" | grep -v -E '^\s*$' | head -8 | sed 's/^/      /'
      fail=1
    elif [ ! -s "${mmd%.mmd}.svg" ] || grep -q 'Syntax error' "${mmd%.mmd}.svg"; then
      echo "FAIL  $f:$line  (syntax error rendered)"
      fail=1
    fi
  done
done
echo "Mermaid blocks checked: $total  —  $([ $fail -eq 0 ] && echo OK || echo FAILURES)"
exit $fail
