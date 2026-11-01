# PROGRESS

> **Resume protocol (after any context compaction):** re-read `CLAUDE.md` and this file, then continue with the next unfinished item under "Next step". Run `python3 scripts/build_meta.py` to refresh the tracker.

## Status
- **Phase:** 1 — batch drafting
- **Next step:** finish Parts 5–6 drafting; Part 3a review running; launch reviews per Part as each completes; Part 4 review must trim to ≤11,000 words

## Phase checklist
- [x] Phase 0.1 — skeleton, CLAUDE.md, style guide, scripts, mkdocs.yml, workflow
- [x] Phase 0.2 — research sweep (`meta/research/*.md`: ~170 searches, 3 notes files, ~20.8k words incl. sources; see D13 for fetch limits)
- [x] Phase 0.3 — outline finalized (`meta/outline.md`, `meta/chapters.yml`, `meta/chapter-scopes.md`)
- [x] Phase 0.4 — Ch 16 written + QA'd (quality bar; PASS, 2,299 words, 9 visuals)
- [ ] Phase 1 — Parts 1 → 8 drafted in batches
- [ ] Phase 2 — independent reviewer pass for every Part
- [ ] Phase 3 — Part 0, glossary ≥300, flashcards, cheat sheets, README, final QA, deploy

## Batch log
| Batch | Chapters | Status | Notes |
|---|---|---|---|

## Chapter tracker
<!-- TRACKER -->
| Part | Ch | Title | Status | Words / budget | Visuals | VERIFY |
|---|---|---|---|---|---|---|
| 0 | 0.1 | How to use this atlas | ⏳ todo | 0 / 1,500 | 0 | 0 |
| 0 | 0.2 | The one-page map | ⏳ todo | 0 / 1,500 | 0 | 0 |
| 1 | 1 | What storage does | ✅ drafted | 2,507 / 2,200 | 7 | 1 |
| 1 | 2 | Media physics for a semis person | ✅ drafted | 3,208 / 2,500 | 10 | 4 |
| 1 | 3 | Inside an SSD | ✅ drafted | 2,868 / 2,400 | 7 | 2 |
| 1 | 4 | Performance and economics metrics | ✅ drafted | 2,873 / 2,400 | 9 | 4 |
| 1 | 5 | Data reduction | ✅ drafted | 2,492 / 2,100 | 9 | 4 |
| 1 | 6 | Data protection and resilience | ✅ drafted | 2,758 / 2,400 | 12 | 6 |
| 2 | 7 | Block protocols | ✅ drafted | 2,493 / 2,100 | 9 | 2 |
| 2 | 8 | File protocols | ✅ drafted | 2,202 / 1,900 | 7 | 3 |
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
| 4 | 26 | Core technology: Purity and DirectFlash | ✅ drafted | 2,435 / 2,200 | 7 | 3 |
| 4 | 27 | Product portfolio: FlashArray and FlashBlade | ✅ drafted | 2,366 / 2,200 | 8 | 5 |
| 4 | 28 | Platform and software | ✅ drafted | 2,168 / 2,000 | 8 | 5 |
| 4 | 29 | Hyperscaler business, ecosystem and financials | ✅ drafted | 1,994 / 1,800 | 7 | 5 |
| 5 | 30 | The AI data pipeline end to end | ✅ drafted | 2,286 / 2,000 | 8 | 2 |
| 5 | 31 | Training storage | ✅ drafted | 2,556 / 2,200 | 10 | 1 |
| 5 | 32 | Inference and KV cache | ✅ drafted | 2,640 / 2,300 | 8 | 0 |
| 5 | 33 | RAG, vector databases and AI-native data formats | ✅ drafted | 2,307 / 2,000 | 9 | 2 |
| 5 | 34 | NVIDIA's ecosystem and certifications | ✅ drafted | 2,366 / 2,000 | 6 | 8 |
| 5 | 35 | AI factories and neoclouds | ✅ drafted | 2,184 / 1,900 | 6 | 6 |
| 5 | 36 | How hyperscalers build AI storage | ✅ drafted | 2,301 / 2,000 | 7 | 1 |
| 5 | 37 | Reading benchmarks critically | ✅ drafted | 2,304 / 2,000 | 8 | 7 |
| 5 | 38 | Power, density and the AI datacenter | ✅ drafted | 2,041 / 1,800 | 7 | 7 |
| 5 | 39 | Agentic AI and data intelligence | ✅ drafted | 2,043 / 1,800 | 6 | 2 |
| 6 | 40 | Market structure and sizing | ✅ drafted | 2,301 / 2,000 | 9 | 7 |
| 6 | 41 | Why AI-native storage vendors gained traction | ✅ drafted | 2,868 / 2,500 | 8 | 2 |
| 6 | 42 | VAST Data deep dive | ✅ drafted | 4,545 / 4,000 | 12 | 13 |
| 6 | 43 | WEKA deep dive | ✅ drafted | 3,994 / 3,500 | 9 | 5 |
| 6 | 44 | DDN deep dive | ✅ drafted | 4,008 / 3,500 | 8 | 5 |
| 6 | 45 | Head-to-head: FlashBlade//EXA vs. VAST vs. WEKA vs. DDN | ✅ drafted | 2,713 / 2,500 | 8 | 4 |
| 6 | 46 | Incumbents | ✅ drafted | 3,396 / 3,000 | 8 | 2 |
| 6 | 47 | Other challengers and software-defined players | ✅ drafted | 2,295 / 2,000 | 5 | 7 |
| 6 | 48 | Media suppliers and the NAND cycle | ✅ drafted | 2,264 / 2,000 | 7 | 9 |
| 6 | 49 | Competitive landscape matrices | ✅ drafted | 1,723 / 1,500 | 7 | 2 |
| 6 | 50 | Technical diligence framework | ✅ drafted | 2,297 / 2,000 | 8 | 1 |
| 7 | 51 | History of storage, 1956–2026 | ✅ drafted | 2,842 / 2,500 | 6 | 2 |
| 7 | 52 | History of flash and NAND economics | ✅ drafted | 2,641 / 2,300 | 8 | 14 |
| 7 | 53 | Future trends, 2026–2032 | ✅ drafted | 3,202 / 3,000 | 6 | 5 |
| 7 | 54 | Strategic option map | ⏳ todo | 0 / 2,200 | 0 | 0 |
| 8 | 55 | Talking with product managers | ✅ drafted | 1,833 / 1,600 | 6 | 1 |
| 8 | 56 | Talking with engineering leaders and the CTO office | ✅ drafted | 2,060 / 1,600 | 6 | 1 |
| 8 | 57 | Question bank: 150 questions | ✅ drafted | 3,539 / 1,800 | 6 | 0 |
| 8 | 58 | Explain it in 30 seconds | ✅ drafted | 2,837 / 1,500 | 6 | 0 |
| 8 | 59 | Self-test: 200 flashcards | ⏳ todo | 0 / 1,500 | 0 | 0 |
| 8 | 60 | Cheat sheets | ⏳ todo | 0 / 1,000 | 0 | 0 |
| | | **Total** | **57/62** | **136,817** | **445** | **200** |
<!-- /TRACKER -->
