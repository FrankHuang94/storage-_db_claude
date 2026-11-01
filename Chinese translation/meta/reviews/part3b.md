# 审阅报告：第 3b 部分（第 19–24 章）

> 📄 英文原文：[meta/reviews/part3b.md](../../../meta/reviews/part3b.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

**审阅范围**：`docs/03-system-architecture/19-software-defined-and-hci.md` 至 `24-architecture-decision-matrix.md`，以及各章的 staging 文件。审阅日期 2026-11-01。

## 摘要

**核查内容**。我对任务说明点名的机制做了事实核查：

- 第 19 章：EBS 链式复制、Physalia 单元（cell）、SRD 以及 io2 Block Express 的各项数字。
- 第 20 章：Raft、法定人数（quorum）规则、CAP/PACELC 以及 MTTDL 持久性模型。
- 第 21 章：元数据扩展方面的主张。
- 第 22 章：集群管理工具的名称。
- 第 23 章：收入确认以及 Evergreen 计划条款。

我还核查了业务数字：Nutanix FY26、Everpure FY26 与 Q2 FY27、Broadcom/VCF，以及 Backblaze。

**算例**。我重新计算了每一个算例：

- 第 19 章：闲置（stranded）核心数和重建小时数。
- 第 20 章：RAID 6、8+2、三副本和 16+4 的"几个 9"；AFR 到 FIT 的换算；相关故障惩罚。
- 第 21 章：小文件吞吐量、交叉点文件大小以及 ls/stat 耗时。
- 第 23 章：现金流 NPV 和第一年收入。

全部算术都正确。第 20 章的图表脚本实现的正是正文所述公式。

**网络限制**。由于 usenix.org 和 docs.aws.amazon.com 不在本会话允许的网络域名之内，WebFetch 访问失败。因此本次审阅的所有核查都依据 WebSearch 摘要，新增脚注在适用之处标注了 "seen via search summary"（"经搜索摘要看到"）。

**首先修复的已知问题（第 24 章）**。第 24 章在其战略段落和表 24.5 中重复了旧的"Everpure 称 FlashBlade//S 为全共享架构"这一错误。我将两处都改写为与修正后的第 15 章一致：一种分区式横向扩展，每个刀片负责各自的 authority，介质池化管理，Pure 的工程师称之为 "partitioned-writer"（分区写入者）。引用了 Emerson 的博客。

我还使第 24 章与第 16 章和第 17 章对 EXA 的分类保持一致（属于并行文件系统一行中的 pNFS 元数据/数据分离，而非 DASE）：

- 热力图的行标签现为 "Scale-out shared-nothing (incl. partitioned)"（"横向扩展无共享（含分区式）"）和 "Parallel file system (incl. pNFS split)"（"并行文件系统（含 pNFS 分离）"）。
- 新增 "Where Everpure's products sit"（"Everpure 产品的定位"）一段，将每款 FlashBlade 产品放入其所属行并说明限定条件，包括 EXA 的数据节点保护方案未见公开文档。
- 象限图新增一个 "pNFS split"（"pNFS 分离"）点。其图注不再暗示图中绘有 pNFS 设计（实际并未绘出）。
- 表 24.5 的 DASE 单元格现改为 EXA 采用元数据与数据分离。
- 新增一条"不要这样说"条目。

**热力图与第 14–19 章优缺点的对照**。大多数单元格一致。我发现三处不一致并加以解决：

1. 无共享架构在 OLTP 上评为 ◐，但第 15 章将延迟敏感型块存储列为最不适合的场景。我保留 ◐，并将 DASE 的说明条目扩展到覆盖无共享架构（PowerFlex 式的块 SDS 可运行生产数据库）。
2. 对象存储在训练和检查点保存上评为 ◐，但第 18 章将二者都列为最适合的场景。我保留 ◐，说明条目现解释了原因：同步检查点写入和小文件随机访问。
3. SDS/HCI 一行在 HPC 和 AI 上评为 ○，而第 19 章将 "large object and file, AI data lakes"（"大型对象和文件、AI 数据湖"）列为 SDS 最适合的场景。我在图例中加注：作为软件销售、运行于通用服务器上的 SDS（WEKA、Ceph、VAST）按其架构归入相应行评分，本行仅覆盖 HCI 和容器原生 SDS。

**结论**：

| 章 | 结论 | 主要原因 |
|---|---|---|
| 19 | 轻微修正 | 关于 Nutanix "首个外部存储"的说法有误；解决了三个 VERIFY |
| 20 | 轻微修正 | 低估了 S3 的一致性；补充分布式布局持久性的限定说明；NetApp 的 VERIFY 已解决 |
| 21 | 轻微修正 | 对 EXA "20×" 主张的描述有误 |
| 22 | 轻微修正 | 路线图事项已过时；Dell 产品更名；命名上的时代错置 |
| 23 | 轻微修正 | Evergreen//One 收入确认的措辞 |
| 24 | 实质性修正 | FlashBlade 的分类以及与第 15–17 章的一致性 |

**修改后的 QA**：第 19–24 章全部通过 `qa_report.py`、`lint_mermaid.sh` 和 `check_links.py --allow-planned`。字数略有增加。我更新了第 20、23 和 24 章的阅读时间，并对第 19、20、22、23 和 24 章的脚注按首次引用顺序重新编号。

## 发现的问题

| 章 | 原文主张 / 段落 | 问题 | 已采取的修正 | 状态 |
|---|---|---|---|---|
| 24 | "a blade scale-out it calls shared-everything (FlashBlade//S and //E)"（"一种它称为全共享的刀片横向扩展（FlashBlade//S 和 //E）"） | 没有任何 Everpure 来源这样说。Pure 称 Purity//FB 为 "partitioned-writer"，一份数据表称之为 "shared-nothing" | 改写为分区式刀片横向扩展，引用 Emerson 博客并链接至第 15、16 和 17 章。同时说明为何没有 DASE（EXA 没有能访问全部介质的计算层） | 已修复 |
| 24 | 表 24.5："FlashBlade//S (…Everpure calls it shared-everything)"（"FlashBlade//S（……Everpure 称其为全共享）"） | 同一错误 | 该行更名为 "Scale-out shared-nothing or partitioned"（"横向扩展无共享或分区式"）。FlashBlade//S 和 //E 描述为每刀片 authority 加池化介质。DASE 单元格写 "EXA splits metadata from data instead"（"EXA 改为将元数据与数据分离"）。PFS 单元格写 "pNFS metadata/data split"（"pNFS 元数据/数据分离"）。表注现将 Portworx（SDS）与 HCI 合作分开列出 | 已修复 |
| 24 | 热力图各行 | 读者无法判断 FlashBlade//S 和 EXA 处于哪一行 | 行标签现包含 "partitioned"（"分区式"）和 "pNFS split"（"pNFS 分离"）。新增一段放置每款产品并说明限定条件；对于 EXA，数据节点保护方案未见文档，元数据核心相关主张为公司自述 | 已修复 |
| 24 | 象限图图注："DASE and pNFS-style designs"（"DASE 和 pNFS 式设计"）位于右上 | pNFS 并未绘出。并行文件系统绘在右下 | 在 (0.86, 0.52) 新增 "pNFS split" 点，并附一句理由（使用标准客户端，但客户仍需运行 RDMA 网络和数据节点）；图注已改写 | 已修复 |
| 24 | 无共享 OLTP ◐ 与第 15 章最不适合场景；对象存储训练/检查点 ◐ 与第 18 章最适合场景；SDS 行与第 19 章 SDS 最适合场景 | 与前面各章的适用性章节不一致 | 扩展了说明条目；图例澄清 SDS/HCI 一行的覆盖范围 | 已修复 |
| 24 | "PureKVA shipped on FlashBlade in October 2026"（"PureKVA 于 2026 年 10 月在 FlashBlade 上发布"） | 来源显示是 2026 年 9 月宣布、10 月可用。未找到 GA 确认 | 改为 "announced… for October availability"（"已宣布……10 月可用"） | 已修复 |
| 24 | "HPE markets the X10000 as unifying all three"（"HPE 将 X10000 宣传为统一三者"） | X10000 是对象加 NFS。块存储是 B10000 | 改为 Alletra Storage MP 产品家族；删除 staging 中的 VERIFY | 已修复 |
| 24 | "one OS family (Purity)… across its rows"（"一个操作系统家族（Purity）……贯穿各行"） | 夸大：EXA 数据节点运行 Linux，Portworx 也不是 Purity | 收窄为 FlashArray 和 FlashBlade，包括 EXA 的元数据核心 | 已修复 |
| 24 | NetApp AFX "up to 128 controllers"（"最多 128 个控制器"） | 这是设计上限（见第 16 章 / part3a） | 背景说明列现已注明 | 已修复 |
| 24 | Gartner Enterprise Storage Platforms MQ 合并类别；S3 Vectors 每索引 2B（2025 年 12 月）；Lustre 在 Top500 中占 >60%；MLPerf v3.0 877.5 GiB/s | 已核查 | 无需修改 | 已核实 |
| 19 | "Nutanix's FlashArray integration, its first major certified external storage"（"Nutanix 的 FlashArray 集成，是其首个获认证的主要外部存储"） | 错误。Dell PowerFlex 才是 NCP 上的首个外部存储（2025 年 5 月 GA），PowerStore 随后跟进（NCI 7.6，2026） | 已修正，并附引用 | 已修复 |
| 19 | VCF 每核 1 TiB vSAN [VERIFY] | 已由 Broadcom KB 313548 确认 | 新增引用；删除 VERIFY | 已修复 |
| 19 | Broadcom 87% VCF 采用率 [VERIFY] | 已确认：Q2 FY25 电话会，据 The Register 2025-06-06。约 US$27B 的 FY25 基础设施软件数字仍未确认 | 87% 已引用；VERIFY 收窄为 US$27B | 已修复 / 已标记 |
| 19 | EBS 每天 >140 万亿次操作 [VERIFY] | 对 Olson 文章的多份摘要说法一致 | 删除 VERIFY；脚注注明经摘要看到 | 已修复 |
| 19 | Everpure 产品/订阅毛利率 66.2% / 74.9% | 仅见于财报摘要（Quartr）。总计 69.9% 是非 GAAP 数字，因此这两项很可能也是非 GAAP | 标注为 "non-GAAP per earnings summaries"（"据财报摘要，非 GAAP"） | 已修复 |
| 19 | "Everpure raised prices on 2026-02-09"（"Everpure 于 2026-02-09 提价"） | 一手来源称是 "early February"（"2 月初"），之后还有第二次提价 | 已改写；新增 Blocks & Files 2026-04-23 | 已修复 |
| 19 | "VCF 9 deprecated vVols"（"VCF 9 弃用了 vVols"） | 不完整：计划在 9.1 中移除（Dell KB，2026 年 1 月） | 已补充，并附引用 | 已修复 |
| 19 | 每卷七节点的 Physalia 单元；客户端→主副本→副本链；io2 256K IOPS、4,000 MB/s、16 KiB 下 <500 µs、99.999%；Nutanix ARR US$2.55B、FY26 非 GAAP 毛利率 88.0% | 已核查。Nutanix 的 88.0% 是全年数字（仅 Q4 为 87.7%） | 无需修改 | 已核实 |
| 20 | 表 20.1：S3 为 "read-after-write: a writer sees its own write; others once committed"（"写后读：写入者能看到自己的写入；其他人在提交后可见"） | 低估了 S3。自 2020 年 12 月起，每个读取者都能看到已确认的写入（按对象的强写后读一致性），这与第 9 章一致 | 该行已更名并重新定义 | 已修复 |
| 20 | "Same code rebuilt declustered in 4 hours reaches 7.8 [nines]"（"同样的编码以分布式布局 4 小时重建，可达 7.8 个 9"） | 该模型把每个 k+m 组视为相互独立，这美化了分布式布局：在分布式布局中，几乎任意 m+1 块失效盘都会落在同一条带上（本例中 8+2 约少 3 个 9，16+4 约少 5 个 9）。对关键条带的优先重建能挽回大部分 | 新增一句限定说明。图表保持不变；其 docstring 已注明独立性假设 | 已修复 |
| 20 | NetApp Cloud Mediator 自 ONTAP 9.17.1 起 [VERIFY] | 已在 ONTAP 9.17.1 发行说明中确认 | 已引用；删除 VERIFY；最强版本论证（steelman）句已更新 | 已修复 |
| 20 | Raft 时序、2f+1、W+R>N、PACELC、Azure 11/12/16 个 9、Backblaze 1.36%（2024 年为 1.55%）、copysets 99.99%→0.15%、FIT 计算、全部 MTTDL 数字 | 已重新计算并核查 | 无需修改 | 已核实 |
| 21 | EXA "up to 20× metadata vs scale-out"（"元数据能力最高为横向扩展架构的 20 倍"）[VERIFY] | 描述有误。Pure 的主张是比 "the leading parallel file system"（"领先的并行文件系统"）"more files per namespace"（"每个命名空间容纳更多文件"）多 20 倍以上，这关乎命名空间规模，而非每秒元数据操作数 | 已重写，引用 iTWire 和 Pure AI 页面；删除 VERIFY | 已修复 |
| 21 | VAST V-tree 7 层、512× 扇出 [VERIFY] | Blocks & Files（2019、2022）一直作为公司自述反复引用 | 删除 VERIFY；标注为公司自述 | 已修复 |
| 21 | MLPerf 配置 "30 EXA blades with 120 DFMs for metadata, 30 data nodes"（"30 个 EXA 刀片配 120 个 DFM 用于元数据，30 个数据节点"）；ImageNet 计算；HDFS 每对象 150 B；GPFS 43 分钟处理 100 亿个文件；DNE 各版本；元数据策略表 | 已核查 | 无需修改 | 已核实 |
| 22 | "MCP integration slated Q4 FY26"（"MCP 集成计划于 Q4 FY26 推出"） | 路线图措辞已过时。MCP 支持已于 2025 年宣布，2026 年的一篇 Everpure 博客介绍了 Pure1 Manage MCP 服务器 | 已更新 | 已修复 |
| 22 | Dell "APEX AIOps Infrastructure Observability" | Dell 支持页面现称其为 "Dell AIOps (formerly CloudIQ)"（"Dell AIOps（原 CloudIQ）"） | 已更名，保留历史沿革 | 已修复 |
| 22 | "In September 2025 Everpure announced…"（"2025 年 9 月，Everpure 宣布……"） | 时代错置：该公司在 2026 年 2 月之前名为 Pure Storage | 改为 "Pure Storage (now Everpure)"（"Pure Storage（现 Everpure）"） | 已修复 |
| 22 | Fusion 的 Terraform provider | 找到的最新版本（v1.0.16）出自 2023 年，面向 Fusion v1，因此 Fusion v2 的"存储即代码"可能比所暗示的更单薄 | 行内补充限定说明 | 已修复 |
| 22 | NetApp DII/Console 更名、HPE InfoSight 86%、Nimble 约 US$1B、GreenLake Intelligence MCP | 已核查 | 无需修改 | 已核实 |
| 23 | STaaS 收入 "Over time, on consumption above a minimum commitment"（"在一段时间内，按超出最低承诺的用量确认"） | 有误导性。10-K 称收入在合同期内按消费量确认，合同包含最低承诺额加超额使用费 | 已改写 | 已修复 |
| 23 | 未描述 Evergreen//Flex 的收入确认 | 10-K 称 Flex 的产品收入在订阅开始时确认，订阅费按期平均确认 | 补充一个分句 | 已修复 |
| 23 | FY26 STaaS TCV US$520M（+32%）[VERIFY] | 已由 Quartr 的 Q4 FY26 摘要确认（仅 Q4：US$179M，+28%） | 删除 VERIFY；补充 Q4 数字 | 已修复 |
| 23 | Q2 FY27 TCV US$277M（+121%）、">well above 40%"（"远高于 40%"）的调整后增长、3–4 年合同、10,000+ 次不停机升级（NDU）覆盖 >3,000 家客户（2022）、Evergreen//Forever 3 年（//E 为 6 年）Ever Modern | 已核查 | 新增 Nasdaq 佐证 | 已核实 |
| 23 | Evergreen//One "Overdrive"（2026）[VERIFY] | 未找到来源 | 保留为 VERIFY | 已标记 |

## 未解决事项 / 分歧

- **FlashBlade//EXA 数据节点的保护方案**（第 24 章工程师问题，第 16/17 章）。公开来源中仍无记载。第 24 章现已明确说明这一点。
- **Everpure Q2 FY27 产品/订阅毛利率（66.2% / 74.9%）**。这些数字仅来自 Quartr 和 investing.com 的摘要；我无法从 sec.gov 获取 8-K 附件。它们很可能是非 GAAP，现已如此标注。需对照 8-K 的毛利率表确认。
- **Broadcom FY2025 基础设施软件收入（约 US$27B）**。看似合理，但未经确认；需核查 10-K。
- **Evergreen//One Overdrive**（第 23 章）。未找到其条款或 GA 的来源。
- **Meta Tectonic 扁平化为单一 ZippyDB schema**（第 21 章，Blocks & Files 2026-07-27）。搜索没有结果，因此 VERIFY 保留。
- **Pure1 Manage MCP 服务器 GA**（第 22 章）。仅见于一篇 Everpure 博客，且经搜索摘要看到。
- **第 24 章热力图仍属本图谱的判断**。我仍建议请 Everpure 现场工程师对有争议的单元格做合理性检查，尤其是新增的 pNFS 分离象限位置。staging 中的 ASK/VERIFY 保留。
- **第 27 章（不在审阅范围内）**。我用 grep 搜索了 "calls it shared-everything" 及类似的 FlashBlade 措辞，除第 15/16 章外（那里现在只出现在纠正性的上下文中）未发现其他残留。
- **网络**。usenix.org 和 docs.aws.amazon.com 在本会话中无法解析，blog.everpuredata.com 和 sec.gov 也未能抓取。所有针对这些来源的核查都依赖搜索摘要。
