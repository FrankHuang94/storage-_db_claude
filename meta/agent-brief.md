# Chapter-writer brief (read this fully before writing)

You are drafting chapter(s) of the **Everpure Tech Atlas**, a strategy-level knowledge base on storage and AI storage, in the repo at `/home/user/storage-_db_claude`. Today is **2026-11-01**. Your training data is stale after mid-2025.

## 1. Read first (in this order)
1. `CLAUDE.md` — reader profile, standing rules (accuracy, sourcing, copyright, voice, visuals).
2. `meta/style-guide.md` — **the mandatory chapter template**, footnote format, visual conventions, palette, staging formats.
3. `meta/outline.md` — every chapter's file path (for cross-links) and planned visuals. Your chapter's row lists its required visuals; ★ = signature visual you must deliver.
4. `meta/research/*.md` — the verified fact base from the research sweep (Everpure, VAST/WEKA/DDN, ecosystem). Reuse its facts **and its sources** (cite the original URL, not the notes file).
5. If it exists, `docs/03-system-architecture/16-disaggregated-shared-everything.md` is the **quality-bar exemplar**: match its depth, density, tone and structure. Skim it.

## 2. Research
- Do your own targeted live research (typically 6–15 WebSearch/WebFetch calls per chapter) for anything time-sensitive or numeric not already in `meta/research/`. Primary sources first (filings, official docs, standards bodies, papers), then reputable trade press. Never cite the notes files; cite the underlying source.
- Never invent numbers, product names, dates, customers, funding, valuations or quotes. If you can't verify: `[VERIFY: …]` inline + a VERIFY line in staging (below).
- Well-established engineering facts and your own worked arithmetic need no footnote (show the arithmetic so it's checkable). Anything vendor-specific, time-sensitive or market-related needs a footnote.

## 3. What to write
- **The chapter file** at the exact path in `meta/outline.md`, following the template headings *exactly* (QA checks them): `# N. Title`, header block (`> **Depth:** L2 · **Reading time:** ~X min · **Last verified:** 2026-11-01` and `> **Prerequisites:** …`), then `## TL;DR`, `## Why this matters for Everpure strategy`, `## Core concepts`, `## How Everpure approaches it vs. competitors`, `## History and trajectory`, `## Numbers that matter`, `## Conversation playbook`, `## Going deeper (optional, L3 pointers)`, `## Key terms`, `## Sources`. (Ch 42–44 add the five deep-dive sections — see style guide.)
- **Word budget:** hit the chapter budget in `meta/chapters.yml` **+5–15%**, as measured by `python3 scripts/wordcount.py <file>` (prose only: code, Mermaid, tables, footnote defs and the Sources section are NOT counted). Most of the words belong in *Core concepts*. Substance only — mechanisms, worked numbers, examples, history, implications. No repetition, no filler.
- **Visuals:** ≥ max(3, words/700) per chapter, ≥ 2 non-table, interleaved with the prose, each with alt text (images) and an italic one-sentence takeaway caption `*Figure N.k — …*`. Deliver every ★ visual listed for your chapter. Prefer Mermaid; use hand-authored SVG (`docs/assets/diagrams/chNN-<slug>.svg`, image link `../assets/diagrams/chNN-<slug>.svg`) for things Mermaid draws badly; data charts via `scripts/charts/chNN_<slug>.py` + `data/chNN_<slug>.csv` (CSV must have `source` and `as_of` columns; chart module exposes `build(out_dir)` and uses `scripts/charts/_style.py`; output `docs/assets/charts/chNN-<slug>.svg`; link `../assets/charts/chNN-<slug>.svg`). Look at any existing `scripts/charts/ch*.py` for the pattern. Only chart **sourced or clearly-labelled illustrative** data (label illustrative/worked-example charts as such in the title).
- **Semiconductor bridges:** the reader is ex-semis M&A. Use analogies to memory hierarchies, HBM/DRAM, NAND physics, controllers, PCIe/SerDes, chiplets, foundry dynamics, GPU utilization economics — where they genuinely clarify.
- **Everpure framing:** honest, not promotional. Steelman competitors. Strategy content = "options a strategy team might evaluate, based on public information". Use "Everpure" for the company from Feb 2026 onward, "Pure Storage" for earlier history.
- **Cross-links:** link related chapters with relative paths from your file (e.g., `../01-storage-fundamentals/03-inside-an-ssd.md`), and the glossary as `../glossary.md`. Linking to not-yet-written chapters is fine.
- **Conversation playbook:** 3 PM questions + strong-answer sketch, 3 engineer questions + strong-answer sketch, and a "**Don't say this:**" list of misconceptions — make these genuinely useful and specific.
- **Numbers that matter:** a table `| Metric | Value | Context | Source / date |` with ≥ 5 rows, every row sourced (footnote) or marked as a worked example.

## 4. Staging files (also required)
- `meta/glossary-staging/chNN.md` — every term introduced (aim 8–20 per chapter), one per line, exactly:
  `- **Term** — one-sentence L1 definition. | NN`
- `meta/open-questions-staging/chNN.md` — lines `- VERIFY | NN | item | why it matters` for every `[VERIFY]`, plus 3–6 lines `- ASK | NN | PM/Eng/CTO | a sharp question worth asking Everpure people`.
(NN = chapter number, two digits not required: use the number as in chapters.yml, e.g. `16`.)

## 5. QA you must run and pass before finishing
```bash
cd /home/user/storage-_db_claude
python3 scripts/wordcount.py docs/<part>/<file>.md
bash scripts/lint_mermaid.sh docs/<part>/<file>.md      # must end "OK"; fix every FAIL
python3 scripts/make_charts.py chNN                     # if you added charts
python3 scripts/qa_report.py --chapter NN               # must say PASS
python3 scripts/check_links.py --allow-planned docs/<part>/<file>.md   # 0 broken
```
Mermaid pitfalls: quote node labels containing punctuation `A["NVMe-oF (TCP)"]`; no unquoted parentheses in flowchart labels; in `timeline` and `mindmap` avoid colons/parentheses inside entries; `quadrantChart` points need x,y in [0,1] and simple names; in `sequenceDiagram` avoid semicolons and `#` in messages; `xychart-beta` category labels with spaces must be quoted. Keep diagrams readable (≤ ~15 nodes).

## 6. Rules of engagement
- **Do NOT** run git (no add/commit/push). The main agent commits.
- **Do NOT** edit files other than your chapter(s), your own SVG/chart/CSV files, and your own staging files. Never edit `docs/glossary.md`, `PROGRESS.md`, `README.md`, `mkdocs.yml`, other chapters, or shared scripts (if a shared script has a bug, work around it and mention it in your reply).
- Copyright: own words only; never paste vendor text or replicate vendor diagrams; quotes < 15 words, ≤ 1 per source.
- **Final reply (≤ 120 words):** for each chapter: path, prose words, visuals (M/I/T), VERIFY count, QA status; plus any judgment calls worth logging in `meta/decisions.md` (one line each). Nothing else — no chapter text in the reply.
