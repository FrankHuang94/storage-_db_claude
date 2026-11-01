# PROGRESS

> **Resume protocol (after any context compaction):** re-read `CLAUDE.md` and this file, then continue with the next unfinished item under "Next step". Run `python3 scripts/build_meta.py` to refresh the tracker.

## ✅ Completion summary (2026-11-01)

**Status: Definition of Done met.** All 62 chapters (Part 0 + Ch 1–60) are drafted, independently reviewed and passing QA.

| Definition-of-Done item | Target | Result |
|---|---|---|
| Substantive prose | ≥ 100,000 words | **156,675** prose words (144,275 excluding the Ch 59 flashcard deck) — counted by `scripts/wordcount.py` (excludes code, Mermaid, tables, footnotes, Sources) |
| Part 3 | ≥ 15,000 | **20,742** |
| Part 4 | ~10,000 ±10% | **10,999** (trimmed from 11,413 during review) |
| Part 6 | ≥ 25,000; VAST/WEKA/DDN ≥ 3,000 each | **33,140**; VAST 4,720 · WEKA 4,173 · DDN 4,064 |
| Visuals | ≥ 150; every chapter ≥ 3; Mermaid renders | **501** (189 Mermaid, 75 images = 31 hand-authored SVG diagrams + 40 generated charts + reused embeds, 237 comparison tables); minimum per chapter 5; full `lint_mermaid.sh` pass |
| Template incl. Conversation Playbook | every chapter | `qa_report.py`: 62/62 PASS |
| Sourcing | every number sourced/dated; private figures labelled; VERIFY listed | 1,271 unique sources in `meta/sources.md`; 175 inline `[VERIFY]` markers listed in `meta/open-questions.md` |
| Glossary / question bank / flashcards | ≥ 300 / ≥ 150 / ≥ 200 | **870** terms / **150** questions / **279** flashcards (+66 one-liners in Ch 58) |
| Independent review | all Parts | 12 reviewer passes (`meta/reviews/part0…part8.md`), ~390 fixes applied |
| github.com + MkDocs | both | GitHub renders Markdown/Mermaid natively; `mkdocs build` completes with zero warnings; `deploy.yml` publishes to `gh-pages` |
| Learning paths | README 2-hour / 2-day / 2-week | README + Ch 0.1 |

### Remaining `[VERIFY]` items (175) — where they cluster
- **Fetch-blocked primary sources (decision D13).** sec.gov, everpuredata.com/purestorage.com, vendor sites, MLCommons, Blocks & Files, The Next Platform and others refused page fetches in this environment, so many figures rest on search-engine summaries of those primary URLs and carry `[VERIFY: search-summary only]`. Allowing those hosts and re-checking is the single highest-value follow-up.
- **Everpure product status:** 300 TB DFM ship/GA status; DFM-based EXA data nodes GA; EXA NVIDIA-Certified Storage / NCP listing; PureKVA GA (announced for Oct 2026); FlashBlade S3-over-RDMA GA.
- **Private-company financials:** VAST ARR fiscal basis and Series F lead; DDN 2025 revenue base (press figures conflict); WEKA ARR (company-stated vs estimated).
- **Contested facts presented as contested:** xAI Colossus storage (VAST vs DDN claims).
- Full list with chapter numbers: `meta/open-questions.md` §1–2; reviewer disagreements: §4.

### Decisions-log highlights (`meta/decisions.md`)
- **D1–D4** Repo root = atlas root; assets under `docs/assets/` so paths work on GitHub and MkDocs; generated root `glossary.md`/`docs/index.md`; `meta/chapters.yml` drives scripts and nav.
- **D12** Everpure's NYSE ticker changed from PSTG to **P** on 2026-04-17 (the brief said PSTG); the atlas says "NYSE: P (formerly PSTG)".
- **D13** Many primary hosts were unreachable for page fetches; search-summary-only figures are tagged.
- **D15/D22** FlashBlade//EXA = metadata/data split with direct pNFS data path (not DASE); FlashBlade//S = "partitioned-writer" scale-out (not shared-everything).
- **D17/D20** Illustrative charts are formula-driven with stated assumptions; all quadrant/heatmap/radar placements are labelled as the atlas's judgment.
- **D21** Part 8 exceeds its budget because Q&A text counts as prose (Ch 59 alone ≈12.4k words); totals reported with and without it.
- **D23** Everpure margins quoted as non-GAAP unless stated.

### Follow-ups for the owner
1. **GitHub Pages:** the workflow pushes the built site to the `gh-pages` branch. If the site isn't live, set *Settings → Pages → Source: Deploy from a branch → `gh-pages` / root* once.
2. **Network access:** allow sec.gov, everpuredata.com, vastdata.com, weka.io, ddn.com, mlcommons.org, blocksandfiles.com, nextplatform.com, idc.com, trendforce.com in the environment's network settings, then re-run a verification pass over `meta/open-questions.md`.
3. **Keep current:** quarterly — update Ch 29 (financials), Ch 40 (IDC shares), Ch 42–44 (private-company news), Ch 48 (NAND prices); re-run `python3 scripts/make_charts.py && python3 scripts/build_meta.py`.

## Status
- **Phase:** 3 — complete
- **Next step:** none required; see follow-ups above.

## Phase checklist
- [x] Phase 0.1 — skeleton, CLAUDE.md, style guide, scripts, mkdocs.yml, workflow
- [x] Phase 0.2 — research sweep (`meta/research/*.md`: ~170 searches, 3 notes files, ~20.8k words incl. sources; see D13 for fetch limits)
- [x] Phase 0.3 — outline finalized (`meta/outline.md`, `meta/chapters.yml`, `meta/chapter-scopes.md`)
- [x] Phase 0.4 — Ch 16 written + QA'd (quality bar; PASS, 2,299 words, 9 visuals)
- [x] Phase 1 — Parts 1 → 8 drafted in parallel batches (one subagent per chapter or chapter pair; per-chapter commits)
- [x] Phase 2 — independent reviewer pass for every Part (12 reviews in `meta/reviews/`)
- [x] Phase 3 — Part 0, glossary (870), flashcards (279), cheat sheets, README, final QA, deploy workflow

## Batch log
| Batch | Chapters | Status | Notes |
|---|---|---|---|
| Research | — | done | 3 parallel research agents → `meta/research/` |
| Exemplar | 16 | done | Quality bar; SVG + chart patterns established |
| A | 1–12 | done | 12 parallel agents; Ch 3 re-run after a stalled first attempt |
| B | 13–15, 17–24 | done | Rolling launches as slots freed |
| C | 25–29 | done | Everpure; Part 4 trimmed in review |
| D | 30–39 | done | AI storage |
| E | 40–50 | done | Industry & competition; deep dives 42–44 |
| F | 51–54 | done | History & future |
| G | 55–60, 0.1, 0.2 | done | Synthesis chapters, built last |
| Reviews | 0–8 | done | part0, 1, 2, 3a, 3b, 4, 5a, 5b, 6a, 6b, 7, 8 |

## Chapter tracker
<!-- TRACKER -->
| Part | Ch | Title | Status | Words / budget | Visuals | VERIFY |
|---|---|---|---|---|---|---|
| 0 | 0.1 | How to use this atlas | ✅ drafted | 1,771 / 1,500 | 8 | 0 |
| 0 | 0.2 | The one-page map | ✅ drafted | 1,993 / 1,500 | 13 | 0 |
| 1 | 1 | What storage does | ✅ drafted | 2,507 / 2,200 | 7 | 0 |
| 1 | 2 | Media physics for a semis person | ✅ drafted | 3,230 / 2,500 | 10 | 3 |
| 1 | 3 | Inside an SSD | ✅ drafted | 2,868 / 2,400 | 7 | 2 |
| 1 | 4 | Performance and economics metrics | ✅ drafted | 2,873 / 2,400 | 9 | 4 |
| 1 | 5 | Data reduction | ✅ drafted | 2,494 / 2,100 | 9 | 4 |
| 1 | 6 | Data protection and resilience | ✅ drafted | 3,046 / 2,400 | 12 | 2 |
| 2 | 7 | Block protocols | ✅ drafted | 2,493 / 2,100 | 9 | 2 |
| 2 | 8 | File protocols | ✅ drafted | 2,207 / 1,900 | 7 | 3 |
| 2 | 9 | Object storage and S3 | ✅ drafted | 2,166 / 1,900 | 9 | 2 |
| 2 | 10 | Datacenter networking for storage | ✅ drafted | 2,476 / 2,100 | 10 | 3 |
| 2 | 11 | The GPU data path | ✅ drafted | 2,332 / 2,000 | 7 | 6 |
| 2 | 12 | Interfaces and emerging tech | ✅ drafted | 2,380 / 2,000 | 8 | 8 |
| 3 | 13 | The storage stack, layer by layer | ✅ drafted | 1,695 / 1,500 | 6 | 1 |
| 3 | 14 | Scale-up dual-controller arrays | ✅ drafted | 2,012 / 1,700 | 11 | 2 |
| 3 | 15 | Scale-out shared-nothing clusters | ✅ drafted | 2,024 / 1,700 | 11 | 2 |
| 3 | 16 | Disaggregated shared-everything architectures | ✅ drafted | 2,338 / 2,000 | 9 | 1 |
| 3 | 17 | Parallel and distributed file systems | ✅ drafted | 1,851 / 1,600 | 9 | 3 |
| 3 | 18 | Object storage architecture | ✅ drafted | 1,747 / 1,500 | 11 | 3 |
| 3 | 19 | Software-defined storage and HCI | ✅ drafted | 1,638 / 1,400 | 9 | 1 |
| 3 | 20 | Distributed-systems fundamentals for storage | ✅ drafted | 1,778 / 1,500 | 8 | 0 |
| 3 | 21 | Metadata: the hidden bottleneck | ✅ drafted | 1,490 / 1,300 | 7 | 1 |
| 3 | 22 | Control planes and fleet management | ✅ drafted | 1,163 / 1,000 | 5 | 1 |
| 3 | 23 | Consumption models | ✅ drafted | 1,268 / 1,100 | 5 | 1 |
| 3 | 24 | Architecture decision matrix | ✅ drafted | 1,738 / 1,200 | 6 | 1 |
| 4 | 25 | Company history and strategy, 2009–2026 | ✅ drafted | 1,971 / 1,800 | 6 | 4 |
| 4 | 26 | Core technology: Purity and DirectFlash | ✅ drafted | 2,449 / 2,200 | 7 | 3 |
| 4 | 27 | Product portfolio: FlashArray and FlashBlade | ✅ drafted | 2,416 / 2,200 | 8 | 5 |
| 4 | 28 | Platform and software | ✅ drafted | 2,168 / 2,000 | 8 | 5 |
| 4 | 29 | Hyperscaler business, ecosystem and financials | ✅ drafted | 1,995 / 1,800 | 7 | 5 |
| 5 | 30 | The AI data pipeline end to end | ✅ drafted | 2,286 / 2,000 | 8 | 2 |
| 5 | 31 | Training storage | ✅ drafted | 2,556 / 2,200 | 10 | 1 |
| 5 | 32 | Inference and KV cache | ✅ drafted | 2,640 / 2,300 | 8 | 0 |
| 5 | 33 | RAG, vector databases and AI-native data formats | ✅ drafted | 2,307 / 2,000 | 9 | 2 |
| 5 | 34 | NVIDIA's ecosystem and certifications | ✅ drafted | 2,389 / 2,000 | 6 | 8 |
| 5 | 35 | AI factories and neoclouds | ✅ drafted | 2,305 / 1,900 | 6 | 3 |
| 5 | 36 | How hyperscalers build AI storage | ✅ drafted | 2,381 / 2,000 | 7 | 1 |
| 5 | 37 | Reading benchmarks critically | ✅ drafted | 2,425 / 2,000 | 8 | 3 |
| 5 | 38 | Power, density and the AI datacenter | ✅ drafted | 2,274 / 1,800 | 7 | 6 |
| 5 | 39 | Agentic AI and data intelligence | ✅ drafted | 2,085 / 1,800 | 6 | 2 |
| 6 | 40 | Market structure and sizing | ✅ drafted | 2,377 / 2,000 | 9 | 6 |
| 6 | 41 | Why AI-native storage vendors gained traction | ✅ drafted | 2,975 / 2,500 | 8 | 2 |
| 6 | 42 | VAST Data deep dive | ✅ drafted | 4,720 / 4,000 | 12 | 10 |
| 6 | 43 | WEKA deep dive | ✅ drafted | 4,173 / 3,500 | 9 | 6 |
| 6 | 44 | DDN deep dive | ✅ drafted | 4,064 / 3,500 | 8 | 5 |
| 6 | 45 | Head-to-head: FlashBlade//EXA vs. VAST vs. WEKA vs. DDN | ✅ drafted | 2,751 / 2,500 | 8 | 3 |
| 6 | 46 | Incumbents | ✅ drafted | 3,396 / 3,000 | 8 | 2 |
| 6 | 47 | Other challengers and software-defined players | ✅ drafted | 2,308 / 2,000 | 5 | 5 |
| 6 | 48 | Media suppliers and the NAND cycle | ✅ drafted | 2,300 / 2,000 | 7 | 9 |
| 6 | 49 | Competitive landscape matrices | ✅ drafted | 1,739 / 1,500 | 7 | 2 |
| 6 | 50 | Technical diligence framework | ✅ drafted | 2,337 / 2,000 | 8 | 1 |
| 7 | 51 | History of storage, 1956–2026 | ✅ drafted | 2,851 / 2,500 | 6 | 2 |
| 7 | 52 | History of flash and NAND economics | ✅ drafted | 2,730 / 2,300 | 8 | 9 |
| 7 | 53 | Future trends, 2026–2032 | ✅ drafted | 3,335 / 3,000 | 6 | 3 |
| 7 | 54 | Strategic option map | ✅ drafted | 2,599 / 2,200 | 7 | 0 |
| 8 | 55 | Talking with product managers | ✅ drafted | 1,912 / 1,600 | 6 | 1 |
| 8 | 56 | Talking with engineering leaders and the CTO office | ✅ drafted | 1,870 / 1,600 | 6 | 1 |
| 8 | 57 | Question bank: 150 questions | ✅ drafted | 2,579 / 1,800 | 6 | 0 |
| 8 | 58 | Explain it in 30 seconds | ✅ drafted | 1,870 / 1,500 | 6 | 0 |
| 8 | 59 | Self-test: 279 flashcards | ✅ drafted | 12,400 / 1,500 | 19 | 0 |
| 8 | 60 | Cheat sheets | ✅ drafted | 1,164 / 1,000 | 9 | 2 |
| | | **Total** | **62/62** | **156,675** | **501** | **175** |
<!-- /TRACKER -->
