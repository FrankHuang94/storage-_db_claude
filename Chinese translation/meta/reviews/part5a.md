# 审阅：第 5a 部分（第 30–34 章）

> 📄 英文原文：[meta/reviews/part5a.md](../../../meta/reviews/part5a.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

**审阅范围：** `docs/05-ai-storage/30-ai-data-pipeline.md` 至 `34-nvidia-ecosystem.md`，及其暂存文件和第 30 章图表 CSV。审阅日期 2026-11-01。

## 摘要

**核查内容。** 我重新计算了五章中的每一个算例数字：

- **第 30 章：** token 字节数、检查点大小与写出（drain）时间、Llama 3 70B 每 token 的 KV 字节数、RAG 向量总量，以及 Horowitz 能耗比。
- **第 31 章：** 表 31.1；表 31.2 全部 16 个单元格；表 31.3 中基于 Young 公式的间隔与开销，包括将 MTBF 线性外推至 100K GPU；恢复读取放大；由 41% MFU 推导出的 167 tokens/s/GPU；表 31.4；SuperPOD 扩展；以及 MLPerf 隐含的 16–17 TB 检查点。
- **第 32 章：** Llama 3.1 8B、70B、405B 以及 DeepSeek-V3 MLA 每 token 的 KV 字节数；128K 与 1M 会话大小；每台 DGX B200 的会话数；解码阶段 HBM 读取示例；重算 FLOPs（线性部分加因果注意力）与读取时间的对比；盈亏平衡 GB/s；以及表 32.1 全部内容，包括 $/GB-hour 数字。
- **第 33 章：** 1B × 1,024 维索引大小、HNSW 链接字节数、DRAM/SSD 成本与图表 CSV 的对照、DiskANN 延迟与 IOPS、PQ 压缩，以及 Parquet 读取放大。
- **第 34 章：** SuperPOD 下限下每 GPU 的 GB/s。

几乎所有算术都正确且内部一致。第 31 章的 14–16 字节/参数与第 11 章更正后的示例一致：16 B/param 为完整状态上限，实际保存约 14 B/param，70B 模型为 1.12 TB。

**网络访问。** 对 docs.nvidia.com 和 glennklockwood.com 的 WebFetch 失败，这两个域名不在本会话允许范围内。因此 NVIDIA 文档中的数字依赖检索结果摘要，脚注中已注明。

**结论：**

| 章 | 结论 |
|---|---|
| 30 | 扎实；小幅修正（解决一处 VERIFY，一处 MLPerf 标签） |
| 31 | 小幅修正（恢复算术、MTTF 外推背景、Gemini 归属） |
| 32 | 小幅至实质性修正（一个错误的"does not fit"（放不下）单元格、一份夸大 VAST 的厂商声明列表、把 PureKVA"GA"当作事实陈述、MLPerf KV 数字需要规模背景） |
| 33 | 小幅修正（解决 Snowflake 的 VERIFY、成本表述的清晰度） |
| 34 | 小幅修正（ICMS→CMX 命名、细化 NVCS 的 VERIFY、去除 MLPerf 表述中的偏向） |

**NVIDIA 命名与日期在第 10、11、32、34 章之间一致。** 我逐一核实了以下内容：

- Dynamo 于 2025-03-18 发布，Dynamo 1.0 于 2026-03-16 在 GTC 上进入生产可用。
- KVBM 采用 G1–G4 分层。
- BlueField-4 STX 于 2026-03-16 推出。其首个机架级实现是 CMX，即 CES 2026 上的 ICMS 平台更名而来。合作伙伴称之为"G3.5"层。
- STX 有 12 家存储协同设计合作伙伴（Cloudian、DDN、Dell、Everpure、Hitachi Vantara、HPE、IBM、MinIO、NetApp、Nutanix、VAST、WEKA）、8 家早期采用的云或实验室，以及负责硬件的 AIC、Supermicro 和 QCT。合作伙伴的 STX 平台预计于 2H 2026 推出。
- AI Data Platform 于 2025 年 3 月推出，有 10 家合作伙伴。
- NVIDIA-Certified Storage 分为 Foundation、Enterprise 和 NCP 三级。Foundation 对应 128 个模拟 GPU，阶梯上限为 10,000。

**修改后的 QA：** 五章均通过 `qa_report.py`，`lint_mermaid.sh` 为 OK，`check_links.py --allow-planned` 未发现失效链接。字数不变或略有增加，各章仍高于预算。

## 审阅发现

| 章 | 论断 / 段落 | 问题 | 已作修改 | 状态 |
|---|---|---|---|---|
| 30 | FineWeb"~44 TB on disk"（磁盘占用约 44 TB），带 VERIFY | Hugging Face 官方 FineWeb 文章写明"15-trillion tokens, 44TB disk space"（15 万亿 token，44TB 磁盘空间）。约 50 TB 的数字来自二手来源 | 删除 VERIFY；脚注 13 现引用 HF 博客；CSV 说明与暂存条目已更新 | 已修复 |
| 30 | Gartner 2026 年 565 TWh；MLPerf v3.0 中约 1/6 的提交使用 S3 路径；Llama 3 15.6T token、16M token 批大小 | 已核对：Gartner 2026-06-10 给出 565 TWh，较 447 TWh 增长 26%。MLCommons/Nebius 称约 1/6，即 19 家封闭组提交者中有 3 家使用 S3 | 无 | 已核实 |
| 30 | 表 30.2："877.5 GiB/s ... (company-reported)"（公司报告） | MLPerf 结果由厂商提交并经同行评审，且主要竞争对手未参赛。仅用该标签会夸大结果 | 重新标注为"vendor-submitted"（厂商提交），并指向第 31 章说明哪些厂商未参赛 | 已修复 |
| 30 | 算例数字（62 TB token、64 MB/step、5.7–6.5 TB 检查点、3.3 s / 65 s、320 KiB/token、128K 下 40 GiB、4.1 TB 向量、81 s 权重加载） | 已重新计算 | 无 | 已核实 |
| 31 | 恢复："0.81 TB × 128 + 5.67 TB ≈ 109 TB ... to recover 6.5 TB of unique data"（……以恢复 6.5 TB 唯一数据） | 5.67 TB 已包含 bf16 权重，因此权重被重复计算。6.5 TB 是内存中的状态（16 B/param），而保存的唯一数据约为 5.7 TB（14 B/param） | 更正为 0.81 × 128 + 4.86 TB ≈ 109 TB，以恢复约 5.7 TB；恢复目标现为 47–54 GB/s | 已修复 |
| 31 | "Scaling [7.9 h at 1,024 GPUs] linearly predicts about 30 minutes at 16K"（将 [1,024 GPU 下 7.9 h] 线性外推，预测 16K 下约 30 分钟） | 算术正确，但 Kokolis 等人自己的模型预测 16K GPU 下约 1.8 h（据二手摘要）。缺少这一点，读者看到的只是最悲观的外推 | 在 Llama 3 的 3.1 h 旁补充 1.8 h 的预测 | 已修复 |
| 31 | Llama 3：466/47/419 次中断、约 78% 为硬件、3.1 h；16,384 GPU 上 41% MFU；Tectonic 240 PB / 7,500 台服务器 / 2 TB/s / 7 TB/s；每 GPU 1 MB–4 GB | 与我所知的论文内容一致。240 PB / 7,500 台 SSD 服务器有 Princeton 幻灯片佐证。arXiv 本身无法访问 | 已在暂存 VERIFY 上加注 | 已核实（二手来源） |
| 31 | 表 31.2、表 31.3（19 min / 10.4%、6.3 min / 3.4%、3.5 min / 1.9% / 31 GB/s、7.8 min / 25.6%、1.4 min / 4.7% / 76 GB/s）、重启 2.7% / 16%、167 tok/s、11 MB/s、66 天、30 × 5.67 TB | 重新计算，全部正确。100K GPU 下 30 分钟的 MTBF 已明确标注为假设 | 无 | 已核实 |
| 31 | MLPerf v3.0 EXA：877.52 / 588.28 GiB/s、17.74 s / 28.99 s、30 个数据节点、首次提交；VAST、WEKA 和 DDN 缺席 | 经 Techzine、StorageReview 和 MLCommons 确认（19 家中有 11 家首次提交） | 暂存条目已更新 | 已核实 |
| 31 | SuperPOD H100"best"（最佳）档每节点 40/20 GB/s、每 SU 125/62（VERIFY） | RA 表 6 的检索片段显示每 SU 读取为 15/40/125（good/better/best），与 125 一致。每节点及写入数字仍未确认 | 已在正文和暂存中细化 VERIFY | 已标记 |
| 31 | "AWS's Gemini research system"（AWS 的 Gemini 研究系统） | Gemini 是 Rice University 与 AWS 合作的论文 | 已更正归属 | 已修复 |
| 32 | 要点速览："Everpure, WEKA, DDN, VAST and HPE all claim 20× or more faster TTFT"（Everpure、WEKA、DDN、VAST 和 HPE 均宣称 TTFT 快 20 倍以上） | 未找到 VAST 关于 20× TTFT 的声明。VAST 宣称的是功耗降低 75%，其自己的表格行也是这样写的。这夸大了竞争对手的营销口径 | 改为 Everpure、WEKA、DDN 和 HPE；VAST 和 NVIDIA 宣称的是功耗与吞吐量收益 | 已修复 |
| 32 | 表 32.1，1M token 行："does not fit one node's HBM"（单节点 HBM 放不下） | 错误：343 GB 完全可放入一台 DGX B200 的 1,440 GB（扣除 71 GB fp8 权重后约可容纳 4 个会话）。它超出的是单个 GPU 的 180 GB | 已更正该单元格 | 已修复 |
| 32 | PureKVA"GA October 2026"（2026 年 10 月 GA）（表格与时间线） | 来源称相关能力"will be available this October"（将于今年 10 月可用），这是一个已宣布的日期。截至 2026-11-01 未找到 GA 确认 | 改为"availability announced for October 2026"（已宣布 2026 年 10 月可用）和"PureKVA announced"（PureKVA 已发布）；暂存已更新 | 已修复 |
| 32 | EXA KV 读取 1,623.4 GiB/s，51 台主机，"company-reported"（公司报告）；"benchmark evidence, not a marketing multiplier"（是基准测试证据，而非营销倍数） | 缺少规模背景。标准规模组领先者 UBIX 和 FarmGPU 以小得多的配置取得约 444 GiB/s，且 WEKA、VAST 和 DDN 未参赛。不加说明的话读起来偏向 Everpure | 补充按每主机比较的保留说明及未参赛说明 | 已修复 |
| 32 | CMX"5× tokens/s, 5× power efficiency"（5 倍 tokens/s、5 倍能效），日期为 2026-01 | 该声明是在 CES 上针对 ICMS 提出的，ICMS 后来更名为 CMX | 已在"关键数字"表中补充背景 | 已修复 |
| 32 | 每 token KV 字节（128 / 320 / 504 / 68.6 KiB）；128K 下 43 GB；31 个会话；每 GPU 每步 86 GB ≈ 11 ms；重算 4.1e16 FLOPs ≈ 2.6 s / 21 GPU-s；读取 0.13 s；0.43–0.96 MFLOP/byte → 2–5 GB/s；重算 $0.023 对比 DRAM $0.012/h 和闪存 $0.0006/h；250 万 agent 预填充 token | 重新计算，全部正确。头维度和层数与 Llama 3.1 及 DeepSeek-V3 配置一致 | 无 | 已核实 |
| 32 | Dynamo 2025-03-18，Dynamo 1.0 2026-03-16；KVBM G1–G4；CMX 的"G3.5" | 已确认（DigitalOcean/IgorsLab 关于 GTC 2026 的报道；Solidigm 使用"Tier G3.5"） | 无 | 已核实 |
| 32 | 厂商表（WEKA 1000× / 20×、DDN 55× / 27×、HPE 20× 赞助测试、NVIDIA 5×） | 均标注为厂商声明，表注写明基线为无缓存 | 无 | 已核实 |
| 33 | Snowflake FY2026 产品收入 US$4.47B（VERIFY） | 已确认：产品收入 US$4,472.3M，总收入 US$4,683.9M，依据 10-K 及 Q4 FY26 新闻稿 | 删除 VERIFY；脚注 8 补充新闻稿；删除暂存条目 | 已修复 |
| 33 | "In-memory replica carries ~US$63,000 of DRAM"（内存副本承载约 US$63,000 的 DRAM）与"~US$66k versus ~US$4k"（约 US$66k 对约 US$4k）并列 | 正文未解释两者差距。图表 CSV 中包含约 $3k 的 SSD 上 fp32 副本 | 已澄清 | 已修复 |
| 33 | 网络化阵列查询"~15 ms" | 30 轮 × (0.1 + 0.5 ms) ≈ 18 ms | 现改为"~15–18 ms" | 已修复 |
| 33 | 4.1 TB；每向量 264 B 的 HNSW 链接；DRAM $14.5/GB（$927 / 64 GB）；SSD $0.75/GB；$22k / $4.1k / $4.2k；16×；DiskANN 3 ms 与 1.2M 次读取/s；PQ 64×；Parquet 250×；10 TB 语料 → 20 TB 向量 | 对照 CSV 重新计算，全部正确 | 无 | 已核实 |
| 33 | Databricks 年化收入 >US$7B，估值 US$190B，2026 年 8 月 | 已确认（融资于 2026-08-13 完成，公司自述） | 无 | 已核实 |
| 34 | NVCS Foundation 128 / Enterprise ~1,000 / NCP 10,000（均带 VERIFY） | Foundation 128 和 10,000 上限有 NVIDIA 文档和博客摘要佐证。Enterprise 约 1,000 无佐证 | VERIFY 收窄至 Enterprise 数量 | 已标记 |
| 34 | CES 上的 ICMS 与 GTC 上的"CMX"被当作两样东西 | ICMS 已更名为 CMX | 正文说明 CMX 即 CES 平台更名而来；补充与 G3/G4 及第 32 章"G3.5"的关联 | 已修复 |
| 34 | "Everpure's distinctive move is independent benchmarking ... VAST, WEKA and DDN did not"（Everpure 的独特之处在于独立基准测试……VAST、WEKA 和 DDN 没有） | "Independent"（独立）一词过于宽容，因为 MLPerf 提交由厂商自行运行并经同行评审。该句还暗示竞争对手回避基准测试，但 DDN 和 WEKA 参加过早期轮次；只有 VAST 从未参加 | 改写为"public, peer-reviewed"（公开、经同行评审），补充早期轮次说明，并提示结果不代表市场排名 | 已修复 |
| 34 | 125/256 = 0.49 GB/s/GPU；40/256 = 0.16；4 GB/s ≈ 8× 及每 SU 约 1 TB/s；WEKApod 720 GB/s 对比四 SU 增强目标 500 GB/s | 重新计算，正确 | 无 | 已核实 |
| 34 | 12 家 STX 存储合作伙伴、AIC/Supermicro/QCT、8 家早期采用者、2H 2026 | 对照 NVIDIA 新闻稿报道已确认 | 无 | 已核实 |
| 34 | FlashBlade//EXA 的 NVIDIA 认证 | 仍未找到。2026 年 3 月 StorageReview 文章称 NVCS 验证是通往 NCP 级别的"stepping stone"（垫脚石） | 暂存说明已更新 | 已核实（确认缺失） |

## 未解决事项 / 分歧

- **第 11 章（不在我的范围内）** 仍保留 Dynamo 的"[VERIFY: announcement date]"（[VERIFY: 发布日期]）。该日期现已确认为 2025-03-18（NVIDIA Newsroom，即第 32 章脚注 19），第 11 章可删除该标记。
- **SuperPOD 存储表**（第 31 章 H100、第 34 章 B200/B300）：目前只看到 H100 每 SU 读取行（15/40/125），且仅见于片段。每节点 40/20、62 GB/s 写入、B200 标准/增强 40/20 与 125/62，以及 B300 640/2,000 等数字，需要直接阅读 docs.nvidia.com，而本会话无法访问。
- **NVCS Enterprise 级 GPU 数量**（约 1,000）未经确认。
- **Kokolis 等人对 16K GPU 的 1.8 h 预测**来自二手摘要，应核对 arXiv 2410.21680。
- **Llama 3 §3.3 中的数字**与我对论文的理解一致，但本会话无法访问 arXiv。
- **PureKVA：** 是否真的在 2026 年 10 月达到 GA，以及 20× TTFT 声明背后的测试条件，均未解决。
- **Pinecone 寻求出售**（第 33 章）：两次检索均无结果，VERIFY 保留。若找不到一手报道，可考虑弱化为"faced reported strategic pressure"（据报道面临战略压力），或删除该从句。
- **VAST 参与 NVIDIA 的 Series E**（第 34 章）：未解决，VERIFY 保留。
- **Common Crawl">10 PB"** 与 **S3 500T 对象**数字（第 30 章）：仍仅有检索摘要支持，VERIFY 保留。
