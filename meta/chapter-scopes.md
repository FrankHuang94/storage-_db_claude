# Chapter scopes (from the commissioning brief)

Use with `meta/outline.md` (paths, budgets, planned visuals) and `meta/agent-brief.md` (how to write).

## Part 0 — Start Here
- **0.1 How to use this atlas.** Learning paths: a 2-hour crash course, a 2-day ramp, a 2-week mastery plan. Depth labels L1/L2/L3. How chapters are structured. How to use the conversation toolkit.
- **0.2 The one-page map.** A Mermaid mindmap of the whole domain, plus an "Everpure in 10 diagrams" summary.

## Part 1 — Storage Fundamentals
1. **What storage does.** Data lifecycle; primary vs secondary vs archive; block vs file vs object (what each abstraction is and who uses it).
2. **Media physics for a semis person.** HDD mechanics; NAND cells (SLC→TLC→QLC→PLC); 3D NAND layer scaling; endurance and retention; cost-per-bit curves HDD vs NAND. Includes the ★ memory/media hierarchy pyramid (HBM → DRAM → CXL → NVMe → networked flash → HDD → tape) with latency, $/GB and capacity per tier.
3. **Inside an SSD.** Controller, FTL, garbage collection, write amplification, over-provisioning, and why the FTL is where commodity SSDs lose efficiency (sets up DirectFlash in Ch 26).
4. **Performance and economics metrics.** IOPS, throughput, latency, queue depth, tail latency; raw vs usable vs effective capacity; $/TB, TB/W, TB/rack-unit; TCO with a worked example.
5. **Data reduction.** Deduplication, compression, thin provisioning; why data-reduction ratios are marketed aggressively; how to sanity-check a vendor claim.
6. **Data protection and resilience.** RAID, erasure coding, snapshots, clones, sync/async replication, RPO/RTO, stretched clusters, ransomware and immutability.

## Part 2 — Protocols and Networking
7. **Block protocols.** SCSI → Fibre Channel → iSCSI → NVMe → NVMe-oF (FC-NVMe, RoCE, TCP), with read/write sequence diagrams for each (★ NVMe-oF read/write sequences).
8. **File protocols.** NFSv3 / v4.1 / pNFS, SMB, and why HPC and AI care about parallel file access.
9. **Object storage and S3.** The S3 API, consistency models, multipart upload, why S3 is becoming the default AI data interface, S3-over-RDMA.
10. **Datacenter networking for storage.** Ethernet vs InfiniBand, RDMA, RoCEv2, 400/800G, congestion control, NVIDIA Spectrum-X, DPUs/SmartNICs (BlueField) in the storage path.
11. **The GPU data path.** GPUDirect Storage, GPUDirect RDMA, Magnum IO, NIXL. Why "keep the GPU fed" is the whole game, with a worked GPU-idle-cost example. ★ GPU-direct path vs traditional path.
12. **Interfaces and emerging tech.** PCIe generations, CXL, EDSFF, Zoned Namespaces / Flexible Data Placement, computational storage, lessons from Optane.

## Part 3 — Storage System Architecture Fundamentals
Each architecture chapter (14–19) must cover: (a) how it works — component diagram + sequence diagram tracing one read and one write end to end; (b) where state and metadata live; (c) how it scales (capacity, performance, metadata) and where it hits a wall; (d) failure handling: drive, node, controller, network link; (e) pros/cons table; (f) best-fit and worst-fit workloads; (g) real products that use it; (h) cost and operational implications.
13. **The storage stack, layer by layer.** Application → file system → volume manager → protocol → network → controller → media. Where each architecture puts the "intelligence"; evolution DAS → SAN/NAS → distributed → disaggregated. ★ layer-by-layer diagram.
14. **Scale-up dual-controller arrays.** Active/active vs active/passive, ALUA, mirrored write cache/NVRAM, how a write gets acknowledged, non-disruptive controller upgrades. Examples: FlashArray, Dell PowerStore/PowerMax, NetApp AFF/ONTAP HA pairs.
15. **Scale-out shared-nothing clusters.** Node design, data placement (consistent hashing, CRUSH-style), rebalancing, east-west traffic, quorum. Examples: PowerScale/Isilon, WEKA, Ceph, ONTAP clusters.
16. **Disaggregated shared-everything (DASE-style).** Stateless compute nodes, shared NVMe-oF enclosures, global namespace, decoupling performance from capacity. Examples: VAST, FlashBlade//EXA's metadata/data split, others.
17. **Parallel and distributed file systems.** Lustre (MDS/MDT, OSS/OST), IBM Storage Scale/GPFS, BeeGFS, client-side striping. Why HPC built them; why AI inherited them along with their pain points.
18. **Object storage architecture.** Flat namespace, metadata databases, erasure coding across nodes and sites, gateways, consistency vs scale. Examples: S3, MinIO, Cloudian, Ceph RGW, FlashBlade object.
19. **Software-defined storage and HCI.** Ceph, vSAN, Nutanix and MinIO on commodity servers; cloud block storage internals (EBS-style); the software-only vs appliance business-model trade-off.
20. **Distributed-systems fundamentals for storage.** Consistency models, consensus (Paxos/Raft) at L2, durability math (nines, mean time to data loss), failure domains, CAP in practice, caching/tiering design.
21. **Metadata: the hidden bottleneck.** Namespaces, inodes, log-structured designs, small-file problems, metadata scaling strategies, why AI workloads are metadata-heavy.
22. **Control planes and fleet management.** Telemetry, AIOps, policy-driven management, APIs and automation.
23. **Consumption models.** Capex, leasing, Storage-as-a-Service and subscription upgrades; how the business model shapes the architecture.
24. **Architecture decision matrix.** Every architecture against every workload (databases, VMs, containers, backup, HPC, AI training, AI inference/KV cache, RAG, archive) as a large ★ heatmap table, plus a ★ decision-tree diagram ("given workload X, which architecture and why").

## Part 4 — Everpure
25. **Company history and strategy, 2009–2026.** ★ Mermaid timeline: founding, first FlashArray, 2015 IPO, Evergreen, FlashBlade, Portworx, hyperscaler design win, Enterprise Data Cloud, Feb 2026 rebrand to Everpure, 1touch; compact M&A track-record table. Verify every date.
26. **Core technology: Purity and DirectFlash.** Purity architecture at L2; why managing raw NAND beats commodity SSDs (the semis angle); DFM capacity roadmap (verify current figures); efficiency and power implications; NAND-supplier exposure. ★ Purity architecture; ★ DirectFlash vs commodity SSD stack.
27. **Product portfolio: FlashArray and FlashBlade.** Current lineup in one ★ lineage diagram; positioning by workload; FlashBlade//EXA architecture and benchmark claims (e.g., MLPerf Storage — verify which version and date).
28. **Platform and software.** Evergreen, Portworx, Pure1/Fusion, Enterprise Data Cloud, cloud offerings. How "storage vendor → data management platform" is meant to work; the 1touch data-intelligence thesis.
29. **Hyperscaler business, ecosystem and financials through a tech lens.** What's public about the Meta win; ★ partnership/ecosystem network map (NVIDIA, Cisco, neoclouds, ISVs); revenue mix, subscription/ARR and gross-margin drivers tied to technology, with charts from filings.

## Part 5 — AI Storage
30. **The AI data pipeline end to end.** Ingest → curation → training → checkpointing → fine-tuning → inference → RAG → agents, with I/O patterns per stage (★).
31. **Training storage.** Dataset loading, throughput math, checkpoint size and frequency, worked examples for 70B / 405B / 1T+ models.
32. **Inference and KV cache.** Memory/storage hierarchy (HBM → DRAM → CXL → local NVMe → networked flash); KV-cache offload (NVIDIA Dynamo, KVBM, NIXL, LMCache — verify current names); MLPerf Storage KV-cache tests (verify existence); storage's role in token economics. ★ KV-cache tiering.
33. **RAG, vector databases and AI-native data formats.** Embeddings, vector indexes, Lance/LanceDB, Iceberg/Delta lakehouses; where storage vendors fit vs database vendors.
34. **NVIDIA's ecosystem and certifications.** AI Data Platform reference design, DGX SuperPOD/BasePOD, NVIDIA-Certified Storage, NCP certifications; how storage vendors win or lose AI-factory deals through NVIDIA.
35. **AI factories and neoclouds.** CoreWeave, Lambda, Crusoe, Nebius and others: how they buy storage and what they value. AI-factory rack layout SVG.
36. **How hyperscalers build AI storage.** Google Colossus, Meta Tectonic, AWS S3 Express / FSx for Lustre, Azure; build-vs-buy logic.
37. **Reading benchmarks critically.** MLPerf Storage, SPECstorage, IO500: how they work, how vendors game them, questions to ask.
38. **Power, density and the AI datacenter.** TB/W and TB/rack math; flash displacing HDD; power constraints as a demand driver.
39. **Agentic AI and data intelligence.** Metadata, semantic layers, governance, discovery/classification; storage converging with data management.

## Part 6 — Industry and Competition
40. **Market structure and sizing.** Enterprise primary storage, file/object and AI storage TAM with sourced figures, share trends and charts.
41. **Why AI-native storage vendors gained so much traction.** Cross-cutting thesis: architecture fit for parallel GPU I/O and metadata-heavy workloads; NVIDIA alignment and certification; neoclouds as a new buyer class; software-defined models on commodity hardware; HPC heritage; speed of product iteration; incumbents' blind spots. Where the thesis is weak or overhyped.
42. **VAST Data deep dive (~4,000).** *Technology:* DASE, Element Store, QLC + fast persistent tier, similarity-based data reduction, multiprotocol (NFS/SMB/S3/block), the move up the stack into database/compute/AI data platform (DataBase, DataEngine, InsightEngine, AgentEngine — verify current names), architecture diagrams + I/O walkthrough. *Business:* founding history, funding rounds and valuations (company-stated vs reported), revenue/ARR signals, software-on-partner-hardware model, OEM/partner channels, marquee customers (verify). *Why it's winning, risks, open questions;* comparison with FlashBlade//EXA.
43. **WEKA deep dive (~3,500).** *Technology:* WekaFS / NeuralMesh (verify), parallel distributed software-defined architecture on commodity servers and cloud, kernel-bypass data path, KV-cache/memory-extension (Augmented Memory Grid — verify), GPU-direct integration. *Business:* history, funding and valuation, GTM (cloud marketplaces, OEMs, neoclouds), customers, competitive position. *Why it's winning, risks, open questions;* comparison with FlashBlade//EXA and VAST.
44. **DDN deep dive (~3,500).** *Technology:* EXAScaler (Lustre-based), Infinia (verify), HPC heritage, role in NVIDIA's own AI infrastructure (verify). *Business:* founder-led private ownership, profitability claims, outside investment (verify recent rounds), government/HPC/AI customers, partnerships. *Why it's winning, risks, open questions;* comparison with the others.
45. **Head-to-head: FlashBlade//EXA vs VAST vs WEKA vs DDN.** Architecture, performance claims, data reduction, protocols, hardware model, pricing/consumption, GTM, ecosystem, target customers — multi-dimension matrix, radar-style chart, "who wins which deal and why" table. ★ four-way architecture comparison.
46. **Incumbents.** Dell, NetApp, HPE, IBM, Hitachi Vantara, Huawei — one-page profile each: architecture, AI strategy, business model, strengths, weaknesses.
47. **Other challengers and software-defined players.** Hammerspace, Qumulo, MinIO, Cloudian, Ceph-based offerings, Nutanix, hyperscaler-native storage.
48. **Media suppliers and the NAND cycle.** Samsung, SK hynix/Solidigm, Kioxia, Micron, Sandisk, Western Digital, Seagate; how pricing cycles affect array vendors; HDD vs QLC economics.
49. **Competitive landscape matrices.** ★ Quadrant charts (Mermaid `quadrantChart`) and heatmap tables across the whole field.
50. **Technical diligence framework for storage/AI-data targets.** Architecture, performance claims, scalability, metadata design, durability, roadmap, team, integration with Purity/Fusion; reusable checklist + scorecard template, applied as a worked example to one of VAST/WEKA/DDN using only public data.

## Part 7 — History and Future
51. **History of storage, 1956–2026.** IBM RAMAC → RAID (1988) → SAN/NAS → flash arrays → cloud → AI; ★ timeline + "what each era teaches".
52. **History of flash and NAND economics.** Cost-curve charts, inflection points, why all-flash won primary storage.
53. **Future trends, 2026–2032.** Larger flash modules, PLC, HDD's future, CXL, disaggregation, photonic interconnects, KV cache as a new tier, data-management convergence, sovereign/edge AI. For each: likelihood, timing, winners/losers, implications for Everpure. ★ future-trends radar.
54. **Strategic option map (public-info based).** Build / buy / partner options across the stack, ★ layered stack diagram.

## Part 8 — Conversation Toolkit
55. **Talking with product managers.** How storage PMs think; question sets by product line.
56. **Talking with engineering leaders and the CTO office.** Architecture-review questions, what good answers sound like, red flags.
57. **Question bank: 150 questions,** tagged by topic and audience (PM / Eng / CTO / Sales Eng).
58. **"Explain it in 30 seconds."** 60 one-liners for a CFO or board audience.
59. **Self-test.** 200 flashcards using `<details>` tags, organized by Part.
60. **Cheat sheets.** Acronym sheet, ★ protocol comparison poster, ★ architecture comparison poster, ★ product-lineup poster.
