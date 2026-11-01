# Outline — word budgets and planned visuals

Prose word budgets (as counted by `scripts/wordcount.py`). Machine-readable version: `meta/chapters.yml`. Total budget ≈ 124,000 words. **★ = signature visual required by the spec (§7).**

## Part 0 — Start Here (3,000) · `docs/00-start-here/`
| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 0.1 | `00a-how-to-use-this-atlas.md` | 1,500 | Learning-path flowchart (2h/2d/2w); depth-label table; reading-order map |
| 0.2 | `00b-one-page-map.md` | 1,500 | Domain mindmap; "Everpure in 10 diagrams" (links + 10 compact Mermaid/thumbnails) |

## Part 1 — Storage Fundamentals (14,000) · `docs/01-storage-fundamentals/`
| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 1 | `01-what-storage-does.md` | 2,200 | ★ Block vs file vs object diagram (SVG); data-lifecycle flowchart; primary/secondary/archive table |
| 2 | `02-media-physics.md` | 2,500 | ★ Memory/media hierarchy pyramid (SVG: HBM→tape with latency, $/GB, capacity); NAND cell cross-section SVG; SLC→PLC table; HDD vs NAND $/TB chart; 3D NAND layer chart |
| 3 | `03-inside-an-ssd.md` | 2,400 | Inside-an-SSD SVG; FTL mapping flowchart; GC/write-amplification worked example chart; OP vs WAF chart |
| 4 | `04-performance-and-economics-metrics.md` | 2,400 | Latency/queue-depth curve chart; raw→usable→effective waterfall; TCO worked-example table; Little's-law diagram |
| 5 | `05-data-reduction.md` | 2,100 | Dedup flow sequence; compression pipeline; DRR sanity-check decision tree; claim-vs-reality table |
| 6 | `06-data-protection-and-resilience.md` | 2,400 | RAID/EC layouts diagram; snapshot (redirect-on-write) diagram; sync vs async sequence; RPO/RTO chart; ransomware recovery flow |

## Part 2 — Protocols and Networking (12,000) · `docs/02-protocols-and-networking/`
| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 7 | `07-block-protocols.md` | 2,100 | ★ NVMe-oF read & write sequence diagrams; SCSI→NVMe lineage timeline; transport comparison table; queue model diagram |
| 8 | `08-file-protocols.md` | 1,900 | NFSv3 vs pNFS sequence; protocol comparison table; parallel-access diagram |
| 9 | `09-object-storage-and-s3.md` | 1,900 | S3 PUT/GET sequence; multipart upload flow; consistency-model table; S3-over-RDMA path |
| 10 | `10-datacenter-networking.md` | 2,100 | RDMA vs TCP stack diagram; Ethernet vs InfiniBand table; congestion-control flow; DPU-in-path diagram |
| 11 | `11-gpu-data-path.md` | 2,000 | ★ GPU-direct path vs traditional path (Mermaid + SVG); GPU-idle cost worked-example chart; NIXL/Magnum IO layer stack |
| 12 | `12-interfaces-and-emerging-tech.md` | 2,000 | PCIe generation bandwidth chart; CXL topology diagram; EDSFF form-factor table; FDP/ZNS placement diagram; Optane timeline |

## Part 3 — Storage System Architecture (17,500) · `docs/03-system-architecture/`
Each architecture chapter: component diagram + read & write sequence (★), state/metadata, scaling walls, failure handling, pros/cons table, best/worst-fit workloads, real products, cost/ops implications.
| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 13 | `13-storage-stack.md` | 1,500 | ★ Layer-by-layer stack diagram; "where the intelligence lives" table; DAS→SAN/NAS→distributed→disaggregated timeline |
| 14 | `14-scale-up-dual-controller.md` | 1,700 | Component diagram; ★ write-ack sequence (mirrored NVRAM); read sequence; ALUA path diagram; NDU state diagram |
| 15 | `15-scale-out-shared-nothing.md` | 1,700 | Cluster diagram; ★ read/write sequences; consistent-hashing ring; rebalancing flow |
| 16 | `16-disaggregated-shared-everything.md` | 2,000 | DASE cluster SVG; ★ read/write sequences; scaling chart (perf vs capacity decoupling); comparison table |
| 17 | `17-parallel-file-systems.md` | 1,600 | Lustre component diagram; ★ read/write sequences; striping diagram; product table |
| 18 | `18-object-storage-architecture.md` | 1,500 | Object cluster diagram; ★ PUT/GET sequences; EC-across-sites diagram |
| 19 | `19-software-defined-and-hci.md` | 1,400 | HCI vs SDS vs appliance diagram; EBS-style block service diagram; business-model table |
| 20 | `20-distributed-systems-fundamentals.md` | 1,500 | Raft sequence; durability (nines vs MTTDL) chart; failure-domain diagram; consistency table |
| 21 | `21-metadata.md` | 1,300 | Inode/namespace diagram; small-file IOPS chart; metadata scaling strategies table |
| 22 | `22-control-planes.md` | 1,000 | Control vs data plane diagram; telemetry/AIOps loop; API automation sequence |
| 23 | `23-consumption-models.md` | 1,100 | Capex vs STaaS cash-flow chart; model comparison table; architecture-business feedback diagram |
| 24 | `24-architecture-decision-matrix.md` | 1,200 | ★ Architecture × workload heatmap table; ★ decision-tree flowchart; quadrant |

## Part 4 — Everpure (10,000) · `docs/04-everpure/`
| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 25 | `25-company-history-and-strategy.md` | 1,800 | ★ Company timeline 2009–2026; M&A track-record table; strategy-evolution flowchart |
| 26 | `26-purity-and-directflash.md` | 2,200 | ★ Purity architecture diagram; ★ DirectFlash vs commodity SSD stack (SVG); DFM capacity roadmap chart |
| 27 | `27-flasharray-and-flashblade.md` | 2,200 | ★ FlashArray/FlashBlade lineage tree; positioning-by-workload table; FlashBlade//EXA architecture diagram |
| 28 | `28-platform-and-software.md` | 2,000 | Platform layer diagram; Evergreen model flow; Fusion/Pure1 control-plane diagram; 1touch thesis diagram |
| 29 | `29-hyperscaler-ecosystem-financials.md` | 1,800 | ★ Ecosystem network map; revenue chart; subscription/ARR chart; GM drivers table |

## Part 5 — AI Storage (20,000) · `docs/05-ai-storage/`
| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 30 | `30-ai-data-pipeline.md` | 2,000 | ★ AI pipeline with I/O patterns per stage; I/O pattern table; data-volume funnel |
| 31 | `31-training-storage.md` | 2,200 | Checkpoint size chart (70B/405B/1T); throughput math table; checkpoint sequence; async checkpoint diagram |
| 32 | `32-inference-and-kv-cache.md` | 2,300 | ★ KV-cache tiering diagram; KV size worked-example chart; Dynamo/KVBM/NIXL flow; token economics table |
| 33 | `33-rag-vector-lakehouse.md` | 2,000 | RAG sequence; vector-index comparison table; lakehouse layer diagram |
| 34 | `34-nvidia-ecosystem.md` | 2,000 | AI Data Platform reference diagram; certification ladder; vendor-certification table |
| 35 | `35-ai-factories-and-neoclouds.md` | 1,900 | AI-factory rack layout SVG; neocloud buying-criteria table; neocloud–vendor map |
| 36 | `36-hyperscaler-ai-storage.md` | 2,000 | Colossus / Tectonic diagrams; AWS AI storage stack; build-vs-buy matrix |
| 37 | `37-reading-benchmarks.md` | 2,000 | MLPerf Storage method diagram; benchmark comparison table; "gaming" checklist flowchart |
| 38 | `38-power-and-density.md` | 1,800 | TB/W chart; rack-density comparison; power-constraint flow |
| 39 | `39-agentic-ai-and-data-intelligence.md` | 1,800 | Agentic data-access sequence; data-intelligence layer stack; vendor convergence quadrant |

## Part 6 — Industry and Competition (28,500) · `docs/06-industry-and-competition/`
| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 40 | `40-market-structure.md` | 2,000 | Market size chart; vendor share chart; segment map |
| 41 | `41-why-ai-native-vendors-won.md` | 2,500 | Traction-driver causal diagram; thesis-strength table; incumbent blind-spot flow |
| 42 | `42-vast-data.md` | 4,000 | ★ VAST architecture diagram; I/O walkthrough sequence; ★ funding/valuation timeline + chart; product-stack diagram |
| 43 | `43-weka.md` | 3,500 | ★ WEKA architecture diagram; data-path sequence; ★ funding timeline + chart; AMG tiering diagram |
| 44 | `44-ddn.md` | 3,500 | ★ DDN architecture (EXAScaler + Infinia); ★ milestone timeline; product table |
| 45 | `45-head-to-head.md` | 2,500 | ★ Four-way architecture comparison; multi-dimension matrix; radar-style chart; who-wins-which-deal table |
| 46 | `46-incumbents.md` | 3,000 | Profile tables ×6; incumbent AI-strategy quadrant; portfolio map |
| 47 | `47-other-challengers.md` | 2,000 | Challenger map; comparison table; Hammerspace global-namespace diagram |
| 48 | `48-media-suppliers-and-nand-cycle.md` | 2,000 | NAND supplier share chart; NAND price-cycle chart; cycle → array-vendor margin flow |
| 49 | `49-competitive-matrices.md` | 1,500 | ★ Quadrant charts ×3; heatmap tables |
| 50 | `50-diligence-framework.md` | 2,000 | Diligence flow; checklist table; scorecard template + worked example |

## Part 7 — History and Future (10,000) · `docs/07-history-and-future/`
| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 51 | `51-history-of-storage.md` | 2,500 | ★ History timeline 1956–2026; era-lessons table; $/GB long-run chart |
| 52 | `52-history-of-flash.md` | 2,300 | Flash cost-curve chart; inflection timeline; HDD/SSD crossover chart |
| 53 | `53-future-trends.md` | 3,000 | ★ Future-trends radar (SVG); trend scorecard table; timing timeline |
| 54 | `54-strategic-option-map.md` | 2,200 | ★ Layered stack strategy map; build/buy/partner matrix; option-evaluation flow |

## Part 8 — Conversation Toolkit (9,000) · `docs/08-conversation-toolkit/`
| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 55 | `55-talking-with-pms.md` | 1,600 | PM mental-model diagram; question sets by product line table; meeting-prep flow |
| 56 | `56-talking-with-engineering-and-cto.md` | 1,600 | Architecture-review flow; good-answer/red-flag table; credibility ladder |
| 57 | `57-question-bank.md` | 1,800 | Topic×audience coverage table; tag legend; 150 questions |
| 58 | `58-explain-in-30-seconds.md` | 1,500 | Topic map; 60 one-liners in tables by theme |
| 59 | `59-self-test-flashcards.md` | 1,500 | Card-distribution chart/table; 200 `<details>` flashcards |
| 60 | `60-cheat-sheets.md` | 1,000 | Acronym sheet; ★ protocol poster; ★ architecture poster; ★ product-lineup poster |
