# Style Guide — Everpure Tech Atlas

## 1. Reader and voice
- Reader: strategy / corp-dev executive, ex-semiconductor M&A, CFA/MBA/legal. Smart, time-poor, knows chips and NAND basics, new to storage systems.
- Voice: a sharp senior analyst briefing that executive. Plain English. Short paragraphs. Concrete examples and **worked numbers** ("a 405B-parameter model checkpoint with Adam optimizer state is roughly 405e9 × 16 bytes ≈ 6.5 TB…").
- No marketing fluff, no superlatives without numbers, no cheerleading for any vendor **including Everpure**. Steelman competitors.
- Default depth **L2** (mechanism + trade-offs). L3 only in "Going deeper".
- Use **semiconductor bridges** ("the FTL is to an SSD what a memory controller's address mapping + wear leveling is to DRAM/NAND…", "metadata servers are the tag RAM of a file system").
- Use "Everpure" for the company from Feb 2026 onward and "Pure Storage" when describing earlier history (e.g., "Pure Storage (now Everpure) IPO'd in 2015"). Product names keep their official names (FlashArray, FlashBlade, Purity, DirectFlash, Evergreen, Portworx, Pure1, Fusion) unless sources show they were renamed.
- Strategy content = *"options a strategy team might evaluate, based on public information."* Never speculate about non-public plans.

## 2. Chapter template (mandatory, headings exactly as below)

```markdown
# <Chapter #>. <Title>
> **Depth:** L2 · **Reading time:** ~X min · **Last verified:** YYYY-MM-DD
> **Prerequisites:** [links]

## TL;DR
- 5 bullets a strategy person must remember.

## Why this matters for Everpure strategy
1–2 paragraphs: the business "so what".

## Core concepts
L2 explanation with analogies, worked numbers, visuals interleaved (not dumped at the end).
Use ### sub-headings freely.

## How Everpure approaches it vs. competitors
Comparison table + trade-off discussion. Steelman the alternatives.

## History and trajectory
How we got here; where it's going (dated, sourced signals).

## Numbers that matter
| Metric | Value | Context | Source / date |

## Conversation playbook
- **3 questions for a PM** + what a strong answer sounds like
- **3 questions for an engineer** + what a strong answer sounds like
- **Don't say this:** misconceptions that would undermine credibility

## Going deeper (optional, L3 pointers)

## Key terms

## Sources
[^1]: Publisher, "Title," publication date. URL (retrieved YYYY-MM-DD).
```

Company deep dives (Ch 42–44) add, **after Core concepts and before "How Everpure approaches it vs. competitors"**:
`## Business model & financials`, `## Customers & go-to-market`, `## Why it gained traction`, `## Risks & open questions`, `## Strategic relevance to Everpure`.

Reading time = prose words / 230, rounded.

## 3. Sourcing and footnotes
- Every number, date, spec, product name claim, customer, funding round, valuation or market figure → footnote `[^n]`.
- Footnote definitions live under `## Sources`, numbered in order of first use, format:
  `[^3]: Everpure, "Form 10-K for fiscal year ended February 1, 2026," 2026-04-01. https://… (retrieved 2026-11-01).`
- Unverifiable → `[VERIFY: what needs checking]` inline, and add a line to the chapter's staging list (see §6).
- Private-company figures: always label inline as *(company-stated)*, *(reported by Bloomberg)*, *(estimated)*.
- Quotes: < 15 words, max one per source, in quotation marks with footnote.
- General well-established engineering facts (e.g., "RAID 5 tolerates one drive failure") need no footnote. Anything time-sensitive does.

## 4. Visual conventions
- Target: ≥ 1 visual per 700 prose words, ≥ 3 per chapter, ≥ 2 of them non-table.
- **Mermaid first** (` ```mermaid `). Allowed: `flowchart`, `sequenceDiagram`, `timeline`, `mindmap`, `quadrantChart`, `block-beta`, `xychart-beta`, `stateDiagram-v2`, `classDiagram`. Keep labels short; quote labels containing punctuation: `A["NVMe-oF (TCP)"]`. Avoid `<br>` in timeline/mindmap. Avoid parentheses/colons unquoted. Every block must pass `bash scripts/lint_mermaid.sh <file>`.
- Every visual is followed (or preceded) by a one-sentence italic caption stating the takeaway: `*Figure 16.2 — Stateless compute nodes mean any CNode can serve any request; scaling performance is just adding CNodes.*`
- **Images** (SVG/PNG): `![Alt text describing the image](../assets/diagrams/ch16-dase-cluster.svg)` + caption line. Alt text mandatory.
- **SVG diagrams** (hand-authored, `docs/assets/diagrams/chNN-<slug>.svg`): viewBox-based, width ≤ 1000, font-family `Inter, Helvetica, Arial, sans-serif`, white background rect, palette below, all text ≥ 12px. Original drawings only.
- **Charts**: `scripts/charts/chNN_<slug>.py` exposing `build(out_dir: pathlib.Path)`; reads `data/chNN_<slug>.csv` (must have `source` and `as_of` columns); writes `docs/assets/charts/chNN-<slug>.svg` (SVG preferred) ; uses `scripts/charts/_style.py` (`apply()`, `PALETTE`, `VENDOR_COLORS`, `save(fig, out_dir, name)`). Under the caption add a data line with the CSV path as inline code (not a link, because `data/` is outside the MkDocs docs dir): ``Data: `data/chNN_slug.csv` ``.
- **Tables** count as visuals when they are structured comparisons (≥ 3 rows × 3 cols).

### Palette (Okabe–Ito, colorblind-safe)
| Role | Hex |
|---|---|
| Primary / Everpure | `#0072B2` (blue) |
| Competitor A | `#E69F00` (orange) |
| Competitor B | `#009E73` (green) |
| Competitor C | `#CC79A7` (purple-pink) |
| Accent / highlight | `#D55E00` (vermillion) |
| Secondary light | `#56B4E9` (sky) |
| Warning / caution | `#F0E442` (yellow) |
| Text / neutral | `#222222`, grid `#DDDDDD` |

Vendor color mapping in comparison charts: Everpure `#0072B2`, VAST `#E69F00`, WEKA `#009E73`, DDN `#CC79A7`, Dell `#56B4E9`, NetApp `#D55E00`, HPE `#999999`, others `#F0E442`.

## 5. Links
- Cross-link with relative paths: from `docs/03-system-architecture/16-...md` to `../01-storage-fundamentals/03-inside-an-ssd.md`.
- Glossary: `../glossary.md` (or `glossary.md` from `docs/`). Anchor links into the glossary use the letter section: `../glossary.md#d`.
- Avoid anchor links into other chapters except to `##` headings from the template (e.g., `#conversation-playbook`).
- File names and paths are fixed in `meta/outline.md`; link to future chapters freely.

## 6. Glossary staging
Each chapter writes `meta/glossary-staging/chNN.md`, one term per line, exactly:
```
- **Term** — one-sentence L1 definition. | NN
```
(NN = chapter number). `scripts/build_glossary.py` merges, dedupes (first definition wins, chapter list merged) and writes `docs/glossary.md`.

## 7. Open questions / VERIFY staging
Each chapter appends VERIFY items and good questions-for-Everpure-people to `meta/open-questions-staging/chNN.md`:
```
- VERIFY | NN | what needs checking | why it matters
- ASK | NN | audience (PM/Eng/CTO) | question
```

## 8. Word counting
`scripts/wordcount.py` counts prose only: excludes fenced code/Mermaid, tables, HTML tags, image lines, footnote definitions and the `## Sources` section. Budgets in `meta/outline.md` are prose words by this counter. Aim for budget +5–15%.
