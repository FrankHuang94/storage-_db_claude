#!/usr/bin/env bash
# Commit one chapter with its assets: bash scripts/commit_chapter.sh <num> "<summary>"
# Stages the chapter file, docs/assets/*/chNN-*, scripts/charts/chNN_*.py, data/chNN_*.csv and staging files.
set -euo pipefail
cd "$(dirname "$0")/.."
num="$1"; msg="$2"
file=$(python3 -c "
import sys; sys.path.insert(0,'scripts')
from atlas_lib import all_chapters
print([str(c['path']) for c in all_chapters() if c['num']=='$num'][0])")
pad=$(printf "%02d" "${num%%.*}" 2>/dev/null || echo "$num")
[ -f "$file" ] || { echo "missing $file"; exit 1; }
git add "$file"
for pat in "docs/assets/diagrams/ch${pad}-*" "docs/assets/charts/ch${pad}-*" "scripts/charts/ch${pad}_*.py" "data/ch${pad}_*.csv" \
           "docs/assets/diagrams/ch${num}-*" "docs/assets/charts/ch${num}-*" "scripts/charts/ch${num}_*.py" "data/ch${num}_*.csv" \
           "meta/glossary-staging/ch${num}.md" "meta/glossary-staging/ch${pad}.md" \
           "meta/open-questions-staging/ch${num}.md" "meta/open-questions-staging/ch${pad}.md"; do
  for f in $pat; do [ -e "$f" ] && git add "$f"; done
done
tag="ch${pad}"
git commit -q --allow-empty -m "docs(${tag}): ${msg}

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015j6Et5cc16wRkKSRtDPPUF" && echo "committed ${tag}"
