# Translator task (standard instructions)

You are translating part of the "Everpure Tech Atlas" (repo `/home/user/storage-_db_claude`) into Simplified Chinese.

1. Read `Chinese translation/meta/translation-guide.md` first and follow it exactly (mirrored output paths under `Chinese translation/`, source-reference line after the H1, what to keep verbatim, fixed heading translations, terminology table, Mermaid rules, chunked writing, QA).
2. Translate each assigned English file **completely**: all prose, list items, table cells, Mermaid labels, figure/table captions, image alt text, `<details>` cards. Keep `## Sources` footnote definitions and other bibliographic citations verbatim. Never change numbers, dates, names or link targets.
3. Write each output to its mirrored path (same relative path under `Chinese translation/`), unless your assignment gives a different output path (e.g., a `.partN.md` file for a split file — then translate only the assigned line range and do not add a source-reference line unless told to).
4. Rules: do not run git; do not modify any English file or any file outside your assigned outputs; no web search needed.
5. QA each output: `bash scripts/lint_mermaid.sh "<output file>"` must end OK (if the file has Mermaid); `python3 scripts/check_links.py --allow-planned "<output file>"` should report 0 broken (links into not-yet-translated Chinese files are allowed by that flag); footnote ID set matches the English source.
6. Final reply ≤ 80 words: files written, QA status, any problems.
