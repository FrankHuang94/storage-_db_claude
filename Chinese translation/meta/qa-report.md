# 质量检查报告（QA report）

> 📄 英文原文：[meta/qa-report.md](../../meta/qa-report.md) · 本文为简体中文参考译本，如有出入以英文原文为准。表中章节标题保留英文，与 `meta/chapters.yml` 一致。

| 章 | 标题 | 字数 / 预算 | 图表（Mermaid/图片/表格）/ 要求 | VERIFY | 脚注 | 状态 |
|---|---|---|---|---|---|---|
| 0.1 | How to use this atlas | 1,771 / 1,500 | 8 (2/0/6) / 3 | 0 | 5 | 通过 |
| 0.2 | The one-page map | 1,993 / 1,500 | 13 (7/4/2) / 3 | 0 | 37 | 通过 |
| 1 | What storage does | 2,507 / 2,200 | 7 (2/1/4) / 4 | 0 | 22 | 通过 |
| 2 | Media physics for a semis person | 3,230 / 2,500 | 10 (2/4/4) / 5 | 3 | 40 | 通过 |
| 3 | Inside an SSD | 2,868 / 2,400 | 7 (2/2/3) / 5 | 2 | 21 | 通过 |
| 4 | Performance and economics metrics | 2,873 / 2,400 | 9 (3/2/4) / 5 | 4 | 30 | 通过 |
| 5 | Data reduction | 2,494 / 2,100 | 9 (5/0/4) / 4 | 4 | 34 | 通过 |
| 6 | Data protection and resilience | 3,046 / 2,400 | 12 (4/4/4) / 5 | 2 | 36 | 通过 |
| 7 | Block protocols | 2,493 / 2,100 | 9 (6/0/3) / 4 | 2 | 29 | 通过 |
| 8 | File protocols | 2,207 / 1,900 | 7 (3/1/3) / 4 | 3 | 29 | 通过 |
| 9 | Object storage and S3 | 2,166 / 1,900 | 9 (4/2/3) / 4 | 2 | 39 | 通过 |
| 10 | Datacenter networking for storage | 2,476 / 2,100 | 10 (4/2/4) / 4 | 3 | 37 | 通过 |
| 11 | The GPU data path | 2,332 / 2,000 | 7 (3/2/2) / 4 | 6 | 30 | 通过 |
| 12 | Interfaces and emerging tech | 2,380 / 2,000 | 8 (3/1/4) / 4 | 8 | 43 | 通过 |
| 13 | The storage stack, layer by layer | 1,695 / 1,500 | 6 (2/1/3) / 3 | 1 | 33 | 通过 |
| 14 | Scale-up dual-controller arrays | 2,012 / 1,700 | 11 (5/1/5) / 3 | 2 | 35 | 通过 |
| 15 | Scale-out shared-nothing clusters | 2,024 / 1,700 | 11 (4/3/4) / 3 | 2 | 26 | 通过 |
| 16 | Disaggregated shared-everything architectures | 2,338 / 2,000 | 9 (3/2/4) / 4 | 1 | 27 | 通过 |
| 17 | Parallel and distributed file systems | 1,851 / 1,600 | 9 (4/1/4) / 3 | 3 | 29 | 通过 |
| 18 | Object storage architecture | 1,747 / 1,500 | 11 (4/1/6) / 3 | 3 | 27 | 通过 |
| 19 | Software-defined storage and HCI | 1,638 / 1,400 | 9 (4/1/4) / 3 | 1 | 31 | 通过 |
| 20 | Distributed-systems fundamentals for storage | 1,778 / 1,500 | 8 (3/1/4) / 3 | 0 | 21 | 通过 |
| 21 | Metadata: the hidden bottleneck | 1,490 / 1,300 | 7 (3/1/3) / 3 | 1 | 27 | 通过 |
| 22 | Control planes and fleet management | 1,163 / 1,000 | 5 (3/0/2) / 3 | 1 | 25 | 通过 |
| 23 | Consumption models | 1,268 / 1,100 | 5 (2/1/2) / 3 | 1 | 20 | 通过 |
| 24 | Architecture decision matrix | 1,738 / 1,200 | 6 (2/0/4) / 3 | 1 | 20 | 通过 |
| 25 | Company history and strategy, 2009–2026 | 1,971 / 1,800 | 6 (2/1/3) / 3 | 4 | 46 | 通过 |
| 26 | Core technology: Purity and DirectFlash | 2,449 / 2,200 | 7 (3/2/2) / 4 | 3 | 45 | 通过 |
| 27 | Product portfolio: FlashArray and FlashBlade | 2,424 / 2,200 | 8 (3/1/4) / 4 | 5 | 43 | 通过 |
| 28 | Platform and software | 2,168 / 2,000 | 8 (5/0/3) / 4 | 5 | 43 | 通过 |
| 29 | Hyperscaler business, ecosystem and financials | 2,005 / 1,800 | 7 (2/2/3) / 3 | 5 | 47 | 通过 |
| 30 | The AI data pipeline end to end | 2,286 / 2,000 | 8 (3/2/3) / 4 | 2 | 30 | 通过 |
| 31 | Training storage | 2,556 / 2,200 | 10 (3/1/6) / 4 | 1 | 20 | 通过 |
| 32 | Inference and KV cache | 2,640 / 2,300 | 8 (3/2/3) / 4 | 0 | 38 | 通过 |
| 33 | RAG, vector databases and AI-native data formats | 2,307 / 2,000 | 9 (5/1/3) / 4 | 2 | 37 | 通过 |
| 34 | NVIDIA's ecosystem and certifications | 2,389 / 2,000 | 6 (4/0/2) / 4 | 8 | 46 | 通过 |
| 35 | AI factories and neoclouds | 2,305 / 1,900 | 6 (1/2/3) / 4 | 3 | 41 | 通过 |
| 36 | How hyperscalers build AI storage | 2,381 / 2,000 | 7 (4/0/3) / 4 | 1 | 32 | 通过 |
| 37 | Reading benchmarks critically | 2,425 / 2,000 | 8 (3/1/4) / 4 | 3 | 38 | 通过 |
| 38 | Power, density and the AI datacenter | 2,274 / 1,800 | 7 (1/1/5) / 4 | 6 | 37 | 通过 |
| 39 | Agentic AI and data intelligence | 2,085 / 1,800 | 6 (4/0/2) / 3 | 2 | 26 | 通过 |
| 40 | Market structure and sizing | 2,377 / 2,000 | 9 (3/2/4) / 4 | 6 | 33 | 通过 |
| 41 | Why AI-native storage vendors gained traction | 2,975 / 2,500 | 8 (3/1/4) / 5 | 2 | 45 | 通过 |
| 42 | VAST Data deep dive | 4,720 / 4,000 | 12 (4/2/6) / 7 | 10 | 80 | 通过 |
| 43 | WEKA deep dive | 4,173 / 3,500 | 9 (3/2/4) / 6 | 6 | 57 | 通过 |
| 44 | DDN deep dive | 4,064 / 3,500 | 8 (3/2/3) / 6 | 5 | 58 | 通过 |
| 45 | Head-to-head: FlashBlade//EXA vs. VAST vs. WEKA vs. DDN | 2,751 / 2,500 | 8 (2/2/4) / 4 | 3 | 59 | 通过 |
| 46 | Incumbents | 3,396 / 3,000 | 8 (4/1/3) / 5 | 2 | 49 | 通过 |
| 47 | Other challengers and software-defined players | 2,308 / 2,000 | 5 (3/0/2) / 4 | 5 | 49 | 通过 |
| 48 | Media suppliers and the NAND cycle | 2,300 / 2,000 | 7 (2/2/3) / 4 | 9 | 49 | 通过 |
| 49 | Competitive landscape matrices | 1,739 / 1,500 | 7 (3/0/4) / 3 | 2 | 47 | 通过 |
| 50 | Technical diligence framework | 2,337 / 2,000 | 8 (3/0/5) / 4 | 1 | 37 | 通过 |
| 51 | History of storage, 1956–2026 | 2,851 / 2,500 | 6 (2/1/3) / 5 | 2 | 47 | 通过 |
| 52 | History of flash and NAND economics | 2,730 / 2,300 | 8 (2/1/5) / 4 | 9 | 69 | 通过 |
| 53 | Future trends, 2026–2032 | 3,335 / 3,000 | 6 (2/1/3) / 5 | 3 | 53 | 通过 |
| 54 | Strategic option map | 2,599 / 2,200 | 7 (2/1/4) / 4 | 0 | 45 | 通过 |
| 55 | Talking with product managers | 1,912 / 1,600 | 6 (2/0/4) / 3 | 1 | 20 | 通过 |
| 56 | Talking with engineering leaders and the CTO office | 1,870 / 1,600 | 6 (2/0/4) / 3 | 1 | 18 | 通过 |
| 57 | Question bank: 150 questions | 2,579 / 1,800 | 6 (2/0/4) / 4 | 0 | 7 | 通过 |
| 58 | Explain it in 30 seconds | 1,870 / 1,500 | 6 (2/0/4) / 3 | 0 | 39 | 通过 |
| 59 | Self-test: 279 flashcards | 12,400 / 1,500 | 19 (5/0/14) / 18 | 0 | 0 | 通过 |
| 60 | Cheat sheets | 1,164 / 1,000 | 9 (0/3/6) / 3 | 2 | 34 | 通过 |

**合计（已撰写章节）：** 156,693 词 · 501 个图表 · 175 个 VERIFY 标记 · 0 个未通过章节
