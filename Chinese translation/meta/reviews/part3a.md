# 审阅报告：第 3a 部分（第 13–18 章）

> 📄 英文原文：[meta/reviews/part3a.md](../../../meta/reviews/part3a.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

**审阅范围**：`docs/03-system-architecture/13-storage-stack.md` 至 `18-object-storage-architecture.md`，以及各章的 staging 文件。审阅日期 2026-11-01。

## 摘要

我在能够访问的范围内，对照一手来源或厂商来源核查了任务说明点名的每一项架构机制：写确认路径、控制器角色与故障切换、数据放置、元数据位置、联邦（federation）上限、VAST 硬件细节，以及 EXA 和 AFX 的规模主张。我还重做了每一个算例（延迟累加、重建小时数、纠删码开销、尾延迟计算、LIST 速率、跨地域 EC 重建天数）。全部算术都正确。

由于 blog.everpuredata.com 和 arxiv.org 在本会话中被屏蔽，WebFetch 访问失败。来自这些网站的内容均依据搜索结果摘要引用，脚注中已注明。

关于任务说明要求我裁定的五个问题：

1. **第 14 章，FlashArray 作为"单控制器包络（single-controller envelope）"：维持原判**。Everpure 当前资料（"Why FlashArray Only Needs Two Storage Controllers"）称 FlashArray 在连接层面是 active/active（双活）。只有主控制器处理 I/O。从控制器转发来自其端口的 I/O，并在 DRAM 中保留事务镜像。Justin Emerson 的 "Storage Architecture Spectrum" 一文称 Purity//FA 为 "single-writer"（单写入者）设计。Purity Turbo（仅限 XL190，2026 年 1 月）允许从控制器处理读请求，Everpure 自己的发布博客也证实了这一点。我删除了 VERIFY，并用这些 Everpure 来源替换了 2014 年的第三方引用。
2. **第 16 章和第 17 章，FlashBlade//EXA 是带直接 pNFS 路径的元数据/数据分离架构，而非 DASE：维持原判**。技术简报、Blocks & Files 和解决方案简报说法一致：pNFS 元数据走 NFSv4.1/TCP，数据通过 RDMA 直达数据节点，数据节点为运行 Purity//DN 工具的通用服务器。第 13、15、16 和 17 章在这一点上表述一致。
3. **第 15 章，FlashBlade//S：实质性错误，已修复**。该章写道 "Pure Storage calls it shared-everything"（"Pure Storage 称其为全共享架构"），引用的是 StorageNewsletter。我没有找到任何这样表述的 Pure 来源。Pure 自己的博客称 Purity//FB 为 "partitioned-writer"（分区写入者），并拒绝非此即彼的标签。一份 Pure 数据表称 FlashBlade 为 "shared-nothing"（无共享）。对所引用 StorageNewsletter 文章的搜索摘要也将其描述为全局无共享。我将该节改写为"分区式横向扩展（每个刀片负责各自的 authority），并对介质进行池化的全局管理"。**第 24 章有两处相同的错误，但不在我的审阅范围内（见"未解决事项"）**。
4. **第 16 章，VAST 细节：一处事实修正**。该章写道 "each DBox has two [DNodes]"（"每个 DBox 有两个 [DNode]"）。根据 Blocks & Files 2022 年的报道（即本章自己的来源）和 VAST 的 NCP 参考架构，1U 的 Ceres DBox 有四个 BlueField DPU，每个负责约四分之一的 SSD。最初的 x86 DBox 才是两个。DF-3060V2 的数字（12 TB SCM 对 1,352 TB QLC，约 0.9%）已由 VAST KB 确认。第 16 章没有引用 VAST 的吞吐量数字。
5. **跨章一致性**：修正后，第 13–18 章对 FlashArray、FlashBlade//S 和 EXA 的表述一致。第 13 章现使用 "mirrored or shared NVRAM"（"镜像或共享的 NVRAM"），不再与第 14 章对 FlashArray 机箱 NVRAM 的描述相矛盾。

**结论**：第 13 章，轻微修正。第 14 章，轻微修正（一处竞争对手事实已过时）。第 15 章，实质性修正（FlashBlade//S 的分类）。第 16 章，轻微修正；我保留了范例式的写法，只修改了事实。第 17 章，轻微修正。第 18 章，扎实，有一段表述更加精准。

**修改后的 QA**：六章全部通过 `qa_report.py`、`lint_mermaid.sh` 和 `check_links.py --allow-planned`。字数略有增加。我对第 14–18 章的脚注按首次引用顺序重新编号。

## 发现的问题

| 章 | 原文主张 / 段落 | 问题 | 已采取的修正 | 状态 |
|---|---|---|---|---|
| 13 | 图 13.2 及其正文：写入在 "mirrored in NVRAM on both controllers"（"在两个控制器的 NVRAM 中镜像"）后即确认，并引用 FlashArray//XL170 的延迟 | 对 FlashArray 而言是错误的。其 NVRAM 位于两个控制器都能访问的机箱模块中（//XL 上为 DFMD）。第 14 章对此描述正确，因此第 13 章与之矛盾 | 在图示、正文和表 13.1 中改为 "persist to mirrored or shared NVRAM"（"持久化到镜像或共享的 NVRAM"），并链接至第 14 章 | 已修复 |
| 13 | 毛利率：NVIDIA 71.1%（FY26），Everpure 70.4%（FY26） | 已对照 NVIDIA 10-K/8-K 和 Everpure Q4 FY26 8-K 核查 | 无需修改 | 已核实 |
| 14 | 表 14.1 及正文：FlashArray "single-envelope"（"单包络"）；关于 Purity//FA 是否仍转发从控制器端口 I/O 的 VERIFY | 来源为 2014–2016 年的第三方资料 | 新增 Everpure 的 "Why FlashArray only needs two controllers" 博客和 Emerson 的 "single-writer" 博客；补充从控制器的 DRAM 事务镜像；删除 VERIFY | 已修复 |
| 14 | "Partner CPU that mostly waits on writes"（"主要在等待写入的伙伴 CPU"） | 低估了从控制器：Everpure 称它转发前端 I/O 并镜像事务 | 已改写 | 已修复 |
| 14 | "IBM four I/O groups"（"IBM 四个 I/O 组"）（带 VERIFY）；表 14.4 "Up to 4 I/O groups"（"最多 4 个 I/O 组"） | 已过时。自 Storage Virtualize 8.7.1 起，IBM 不再通过增加控制机柜来扩展单个系统，而是转向 FlashSystem grid（联邦；据一份经销商数据表，FS7600 最多 32 个系统） | 正文和表格已重写；引用 IBM 支持页面；删除 VERIFY | 已修复 |
| 14 | NetApp AFF 对称双活 "from 9.19.1"（"自 9.19.1 起"） | 9.19.1 确实存在（约 2026 年 10 月），但我无法在官方发行说明中确认该 SAN 功能。本章引用的是 NetApp Community 的一篇帖子 | 保持原样 | 已标记 |
| 15 | "Pure Storage calls [FlashBlade//S] shared-everything"（"Pure Storage 称 [FlashBlade//S] 为全共享架构"）（正文和表 15.3） | 缺乏依据。Pure 称之为 "partitioned-writer"；一份 Pure 数据表称之为 "shared-nothing" | 依据 Emerson 博客、Metadata Advantage 白皮书和 M&E 数据表改写；新增一条"不要这样说"条目 | 已修复 |
| 15 | Facebook "median ~180 TB/day"（"中位数约 180 TB/天"）EC 恢复流量（VERIFY） | 可访问的原始摘要写的是 "more than a hundred terabytes per day"（"每天超过一百 TB"）。我无法确认 180 TB（arXiv 被屏蔽） | 正文和数字表中改为 ">100 TB/day"（"每天 >100 TB"）；删除 VERIFY | 已修复 |
| 16 | "Each DBox has two [DNodes] ... in Ceres they are BlueField DPUs"（"每个 DBox 有两个 [DNode]……在 Ceres 中它们是 BlueField DPU"） | Ceres 有四个 BlueField DPU，每个负责约四分之一的 SSD | 已修正；故障表中该行改为通用表述（"another DNode"，"另一个 DNode"）。SVG 仍显示每个 DBox 两个 DNode，作为概念上的最小配置没有问题 | 已修复 |
| 16 | EXA "60 data nodes >5 TB/s, ≥83 GB/s per node"（"60 个数据节点 >5 TB/s，每节点 ≥83 GB/s"） | 已由技术简报确认，其中引用每节点 "upwards of 85 GB/s"（"超过 85 GB/s"）。发布时 ">10 TB/s" 的说法是另一项初步测试主张 | 补充每节点的措辞，并就 10 TB/s 的说法加注，引用 StorageReview | 已修复 |
| 16 | EXA 数据节点 "(Purity//DN)" | Purity//DN 是数据节点管理工具（playbook、升级），运行在通用 Linux/NVMe 服务器上，并非 Purity 数据路径 | 已改写 | 已修复 |
| 16 | NetApp AFX "up to 128 controllers, 52 enclosures"（"最多 128 个控制器、52 个机柜"） | 这是数据表上的设计上限。WWT 报道 ONTAP 9.19.1 支持 32 个控制器。">1 EB effective"（"有效容量 >1 EB"）在 52 × 24 × 60 TB 上需要约 13:1 的缩减比 | 在表格和数字表中补充实际支持上限的限定说明 | 已修复 |
| 16 | HPE X10000 'Yes ("SEDA")'（"是（"SEDA"）"） | 该缩写未经确认。HPE 的表述是 "disaggregated, shared-everything"（"分解式、全共享"） | 改用 HPE 的措辞 | 已修复 |
| 16 | VAST DF-3060V2 12 TB SCM / 1,352 TB QLC；DASE 机制；条带计算 | 已确认（VAST KB） | 无 | 已核实 |
| 16 | VAST 约 US$30B 估值 "reported by press"（"媒体报道"） | 这同时也是公司自述的 F 轮（据研究笔记中的 CNBC 报道，2026-04-22 完成）。现有标注可以接受 | 无 | 已核实 |
| 17 | MLPerf v3.0 EXA 877.5 对 Azure Managed Lustre 642.2 GiB/s（VERIFY "from chart captions"，"来自图表说明"） | StorageReview 正文和 Azure 自己的结果页面（128 个客户端）均有说明 | 新增 Azure 文档引用和 10 节点扩展数据点；删除 VERIFY | 已修复 |
| 17 | WEKA 客户端 "User-space client, DPDK kernel bypass"（"用户态客户端，DPDK 内核旁路"） | 不完整。WEKA 还会为 POSIX 挂载安装一个内核驱动；若不提及，会削弱本章"内核模块"的对比 | 已修正 | 已修复 |
| 17 | 时间线 "2022: Spectrum Scale renamed IBM Storage Scale"（"2022：Spectrum Scale 更名为 IBM Storage Scale"） | 更名发生在 2023 年（Blocks & Files 2023-02-24；IBM 文档称自 5.1.8 起） | 年份已修正；新增脚注 | 已修复 |
| 18 | FlashBlade 写路径（VERIFY） | 分析师报告出自 2023 年。Everpure 的 Metadata Advantage 白皮书称 DFM 的 NVRAM 和闪存分配给每个刀片上的 authority 进程 | 补充该背景；VERIFY 更加具体 | 已标记 |
| 18 | 算例（8+4 放大、对冲读（hedged reads）、跨地域 EC 9.3 天、LIST 每秒 433k 个键） | 已重新计算 | 无 | 已核实 |

## 未解决事项 / 分歧

- **第 24 章（不在我的审阅范围内）重复了 FlashBlade//S 的错误**，分别在第 16 行（"a blade scale-out it calls shared-everything"，"一种它称为全共享的刀片横向扩展"）和第 118 行的表格行（"Everpure calls it shared-everything"，"Everpure 称其为全共享"）。应与修正后的第 15 章保持一致：Pure 称 Purity//FB 为 "partitioned-writer"。第 27 章也应检查是否有相同措辞。
- **FlashBlade//EXA 数据节点的保护方案**（第 16、17 章）仍未核实。没有公开来源记载数据节点之间的纠删码或故障域，2026 年的一份第三方评分表也将其列为未解决。
- **FlashBlade//S 的多机箱数据放置以及当前 Purity//FB PUT 的副本数**（第 15、18 章）仍未核实。
- **ONTAP 9.19.1 中 NetApp AFF 的对称双活**（第 14 章）：依据的是 NetApp Community 的一篇帖子。仍待官方发行说明确认。
- **Facebook 180 TB/天**：如果有人能访问 arXiv 1309.0186，扩展版论文中可能给出接近 180 TB 的中位数。本章现采用 USENIX 摘要中较保守的 ">100 TB/day"。
- **AFX 支持的控制器数量**（9.19.1 中为 32）仅来自 WWT 的摘要。应对照 NetApp Hardware Universe 核查。
- **WebFetch 被屏蔽**：blog.everpuredata.com 和 arxiv.org。新增的 Everpure 博客引用均来自搜索摘要，脚注中已注明。
