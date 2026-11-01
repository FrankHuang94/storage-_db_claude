# 审校报告：第 6b 部分（第 45–50 章）

> 📄 英文原文：[meta/reviews/part6b.md](../../../meta/reviews/part6b.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

**审校范围：** `docs/06-industry-and-competition/45-head-to-head.md` 至 `50-diligence-framework.md`、相应的 staging 文件以及 `data/ch45_radar.csv`。审校范围还允许一项跨章节修正：第 27 章和第 34 章中关于 FlashBlade//EXA 获得 NVIDIA 认证的句子。审校日期 2026-11-01。

## 摘要

**核查内容：**

- **第 45 章矩阵**：我将表 45.1 的每个单元格与第 27 章（EXA）、第 42 章（VAST）、第 43 章（WEKA）和第 44 章（DDN）的现行文本逐一比对，并对照第 32 章核查了 KV 缓存相关单元格，对照第 34 章核查了认证相关单元格。
- **第 45 章算例数字**：我重新计算了全部数字，结果均正确：942 GB/s 与 6.9 s；每个数据节点 31 GB/s；1,743 GB/s ÷ 42 GB ≈ 每秒 41 个上下文；原始容量 51.4 PB 对 62.5 PB，差距约 11 PB；DDN 为 880 GB/s 与 7.4 s。
- **第 46 章**：我重新计算了按 IDC 份额推算的收入：Dell $2.45B、HPE $0.70B、Everpure $0.83B、Huawei $1.16B、NetApp $0.99B。我还核查了 Dell ISG 存储份额（27% 对 38%）以及每一个财年标签（Dell 财年于 1 月下旬结束，NetApp 于 4 月下旬，HPE 于 10 月，Hitachi 于 3 月，Nutanix 于 7 月）。
- **第 48 章**：我重新计算了 NAND 前五大厂商收入：份额合计 87.6%，收入合计 $68.87B，"其他"占 12.4%。复合价格指数为 4.73×，与图表中的 482 一致。我还重新计算了毛利率算例（45% / 54% / $157 / +57%）以及功耗与溢价对比算例（$6.4k 对 $0.8M 和 ≈$7M）。
- **第 49 章与第 50 章**：我将第 49 章象限图的纵轴值与第 46 章图 46.5 进行了比对，并核查了第 49 章 KV 列的计数（16 行中的 10 行）。我重新计算了第 50 章的加权得分（283/100）及其区间（2.14–3.66）。

**网络访问**：约 16 次搜索；WebFetch 无法访问 barchart.com（不在本会话允许的域名之内），因此下文所有内容均基于搜索结果摘要。

**经搜索核实：**

- IDC 2Q26：$10.3B，+33.6%，Dell 23.8%，发布于 2026-09-10。
- Dell Q2 FY27 存储：$4.85B，+26%，指引上调至中双位数（mid-teens）增长。
- HPE Q3 FY26 存储：约 $1.3B，+10.2%。
- Everpure Q2 FY27：经营现金流（OCF）−$136M，自由现金流（FCF）−$238M，产品毛利率 66.2%，订阅毛利率 74.9%，产品收入 +54%。
- TrendForce 2Q26 NAND：每家供应商的数据。
- Lenovo 于约 2026-04-09 完成对 Infinidat 的收购。
- minio/minio 于 2026-04-25 归档；据分叉项目维护者称，README 于 2026-02-12 被标注为 "no longer maintained"（不再维护）。
- Nutanix ARR：US$2.55B，+16%。
- TACC Horizon：400 PB 全闪存（TACC 自述）。
- 仍未解决：NeuralMesh 6 GA（未找到确认）以及 VAST Azure GA（状态不明）。

**FlashBlade//EXA 的 NVIDIA 认证（指派的不一致项）：已解决。** 公开记录是一致的：

- 在 2026-03-16 的 GTC 上，Everpure 宣布将 NVIDIA-Certified Storage（NVCS）验证*扩展*至 EXA。StorageReview 称之为通往 NVCS NCP 级别的 "stepping stone"（垫脚石），NAND Research 则描述为 "stated path toward" NCP（已表明的迈向 NCP 的路径）。
- 只有 Blocks & Files 写道 EXA 已 "Nvidia-certified"（获 NVIDIA 认证），NCP 将于 "later this year"（今年晚些时候）完成。这一措辞与其他来源相矛盾。
- NVIDIA 认证存储系统列表的搜索摘录显示有 FlashBlade//S500，但没有 EXA 条目。
- 3 月之后没有任何来源报道 EXA 已完成认证。

依据最充分的措辞：*2026 年 3 月宣布将 NVCS 验证扩展至 EXA，作为迈向 NCP 级别的一步；截至 2026-11-01 未发现 EXA 已完成认证。* 我将其应用于以下位置：

- 第 27 章：要点速览（TL;DR）和 "Signals"（信号）段落。
- 第 34 章：表 34.2 的单元格和 "Everpure's position"（Everpure 的定位）段落。脚注 31 现在还引用了 Blocks & Files。
- 第 45 章：矩阵单元格、表 45.3、雷达图提示以及 `ch45_radar.csv`。
- 第 49 章：认证深度证据行和"不要这样说"。

第 27 章原先的措辞（"Everpure claimed NVIDIA-Certified Storage"，即"Everpure 声称已获 NVIDIA-Certified Storage"）夸大了实际状态；第 34 章原先的措辞（"in progress"，即"进行中"）是正确的，但语气较弱。

**结论：**

| 章 | 结论 |
|---|---|
| 45 | 轻微至实质性修正：认证措辞；PureKVA "GA" 表述夸大；VAST 的 KV 单元格遗漏了 VUA；WEKA 的最强版本论证（steelman）过度主张；表 45.2 图注把"亚军"数目数错了。除此之外，矩阵与第 27/42/43/44 章一致，且公允 |
| 46 | 扎实；轻微问题（已为一处 VERIFY 加注）。财务数据和财年标签经核查无误 |
| 47 | 扎实；两处 MinIO 的 VERIFY 已解决；Lenovo–Infinidat 交割已确认 |
| 48 | 轻微修正：YMTC "far less"（远低于）表述夸大；要点速览中的溢价区间下限缺乏依据 |
| 49 | 轻微修正：两个纵轴值与第 46 章不一致；KV 和认证证据偏向 Everpure |
| 50 | 轻微修正："placeholders"（占位值）把一个低置信度的 2 分错误标注了。仅使用公开数据 |

**修改后的 QA：** 第 27、34 章及第 45–50 章均通过 `qa_report.py`。`lint_mermaid.sh` 结果为 OK，`check_links.py --allow-planned` 未发现失效链接。字数不变或略有增加，每章仍高于预算。在新增一个来源后，我按首次引用顺序对第 45 章的脚注重新编号。

## 发现的问题

| 章 | 主张 / 段落 | 问题 | 已采取的修正 | 状态 |
|---|---|---|---|---|
| 27/34/45 | EXA 的 NVIDIA 认证：第 27 章 "claimed NVIDIA-Certified Storage"；第 34 章 "validation in progress"；第 45 章 "NVCS validation extended… NCP pending" | 措辞不一致，且第 27 章夸大了状态。一手来源和大多数二手来源描述的是已宣布的验证*扩展*、迈向 NCP 级别。只有 B&F 称其 "certified"，而 NVIDIA 的列表中没有 EXA 条目 | 在第 27、34、45、49 章及雷达图 CSV 中统一采用同一措辞；第 34 章脚注 31 增加 B&F；ch45 staging 中相应行已更新 | 已修复 |
| 45 | "PureKVA on FlashBlade incl. EXA, GA Oct 2026"；"PureKVA itself only became available in October 2026"；表 45.2 "GA only in Oct 2026" | 第 32 章审校人只找到已宣布的 10 月上市，没有 GA 确认 | 现改为 "availability announced for Oct 2026"（已宣布 2026 年 10 月上市）/ "announced 30 September 2026, with availability slated for October"（2026 年 9 月 30 日宣布，计划 10 月上市）；雷达图 CSV 已同步 | 已修复 |
| 45 | VAST KV 缓存单元格：仅写 "BlueField-4 CNode… hardware 2H 2026" | 对 VAST 不公平：第 32 章记载了 2025 年 4 月开源的 VUA | 增加 VUA 并加脚注；雷达图 CSV 的理由说明已更新 | 已修复 |
| 45 | WEKA 的最强版本论证："on sale a year longer than anyone's"（比任何对手都早一年上市销售） | 过度主张：AMG（2025 年 11 月）领先 DDN 集成 Dynamo 的版本（2026 年 6 月）约 7 个月，领先 PureKVA 约 11 个月 | 按实际时间差改写 | 已修复 |
| 45 | 表 45.2 图注：Everpure "credible runner-up in three more"（在另外三类中是可信的亚军） | 表中 Everpure 在两类典型场景（推理、整合）中是亚军，在新兴 GPU 云（neocloud）场景中是挑战者 | 图注已更正 | 已修复 |
| 45 | VAST 规模单元格："TACC Horizon all-flash tier (400 PB system)" | 400 PB 是 TACC 对全闪存存储的数据，而非整个系统的数据。另有一篇报道称原始容量为 200 PB | 现改为 "high-speed tier, 400 PB all-flash (TACC-stated)"（高速层，400 PB 全闪存，TACC 自述） | 已修复 |
| 45 | WEKA 性能单元格：SPECstorage 全部五项工作负载第一（2025-02） | 缺乏背景、已过时：2026 年 EXA 在 AI_IMAGE 上取代了 HPE/WEKA 的成绩（第 27 章、第 43 章） | 增加 "AI_IMAGE since overtaken by EXA"（AI_IMAGE 此后已被 EXA 超越） | 已修复 |
| 45 | "不要这样说"：KV 成熟度 "differs by a year or more"（相差一年或更久） | 鉴于上述日期，属于夸大 | 改为 "by up to a year"（最多相差一年） | 已修复 |
| 45 | 雷达图提示：NCP 认证被描述为 "announced item"（已宣布事项） | 并无任何已宣布达成的事项 | 改为 "pending items: NCP-level certification, which Everpure has said it is working toward"（待定事项：NCP 级别认证，Everpure 表示正在推进） | 已修复 |
| 45 | 表 45.1 的其余部分（架构、元数据、数据路径、保护、规模、MLPerf/SPEC、VAST/WEKA/DDN 的 NVIDIA 认证标识、云、消费模式、GTM） | 与第 27/42/43/44/34 章交叉核对：一致（VAST SuperPOD 2023 / HPS 2024 年 7 月；WEKA HPS 2024 年 9 月；DDN HPS 2024 年 8 月；HPE 转售于 2026-03-03 结束；Eos 达到数据手册的 93%；160 TiB 授权容量） | 无 | 已核实 |
| 45 | VAST Azure GA；NeuralMesh 6 GA | 已搜索：VAST 一份未注明日期的新闻稿称 "now available"（现已上市），而报道称 "soon"（即将）。未找到 NeuralMesh 6 GA 公告 | 保留 VERIFY | 已标记 |
| 46 | IDC 2Q26 份额；Dell FY26 及 Q2 FY27 存储；HPE Q3 FY26；NetApp FY26/Q1 FY27；Everpure FY26 +16% | 经 IDC、Dell、Constellation、B&F 及第 29 章确认。财年标签和期末日期正确。所有算术正确 | 为 HPE 的 staging VERIFY 加注（仅精确的 $1.29B 仍需 8-K 表格确认） | 已核实 |
| 46 | 图 46.4 图注 "company lines ~1.5–2x IDC"（公司口径约为 IDC 的 1.5–2 倍） | Everpure 的比率为 1.43x，因此区间实际约为 1.4–2.0x | 未修改（四舍五入范围内） | 已核实 |
| 47 | MinIO：二进制文件停止发布 "[VERIFY: October 2025]"；README "no longer maintained" "[VERIFY: 12 Feb]"；2026 年 4 月 25 日归档 | 归档日期已确认。2 月 12 日来自分叉项目维护者的陈述（已列为脚注 19）。2025 年 10 月来自一篇二手博客；README 确认仅提供源码分发 | 两处 VERIFY 均替换为有出处的 "reportedly"（据报道）/ "per"（据……）措辞；脚注 17 增加 Pinggy；删除 staging 中两行 | 已修复 |
| 47 | Lenovo–Infinidat 于 2026 年 4 月完成交割 | 已确认：约 2026-04-09 宣布完成；Calcalist 估计 >US$500M | 无 | 已核实 |
| 47 | Nutanix FY26 ARR US$2.55B，+16%，财年截至 2026-07-31 | 已确认（8-K，2026-08-26） | 无 | 已核实 |
| 48 | "YMTC ships as many bits as Kioxia but earns far less"（YMTC 出货比特数与 Kioxia 相当，但收入远低于后者）（要点速览、图 48.1） | 夸大。所有非前五厂商合计仅占 12.4% 的收入，而 Kioxia 为 13.6%，因此在比特份额相等的情况下，YMTC 每比特收入至少低约 9%，而不是 "far less"。Counterpoint 将 YMTC 排在第五，也与 TrendForce 的前五名排名冲突 | 现改为 "less per bit"（每比特收入更低），在图注中给出推导出的下限，并就两种排名加注说明 | 已修复 |
| 48 | 要点速览 "premium widened to ~15–22×"（溢价扩大至约 15–22 倍） | 正文中的指数读数为 18.6× 和 22.6×；没有任何内容支持 15× | 改为 "~19–23×"（保留 VERIFY，单一厂商指数） | 已修复 |
| 48 | TrendForce 2Q26 供应商收入与份额；Everpure Q2 FY27 现金流与毛利率；复合指数；算例 | 已确认并重新计算 | 无 | 已核实 |
| 49 | 矩阵 1 的纵轴值 "reused from Figure 46.5"（沿用图 46.5） | Hitachi 为 0.32，而第 46 章为 0.30；Huawei 为 0.68，而第 46 章为 0.66 | 已与第 46 章对齐 | 已修复 |
| 49 | KV 缓存证据："Everpure PureKVA GA October 2026"（●）对 VAST ◐ | 偏向 Everpure："GA" 未经确认，且按图例的 "new"（新）判定标准，● 处于临界。未提及 VAST 的 VUA | 改写证据行（Pure KVA 自 2025 年起配合 Dynamo；PureKVA 已宣布上市；标注 ● 为临界；为 VAST 引用 VUA）。单元格未改 | 已修复（单元格已标记） |
| 49 | Everpure 的 NVIDIA 认证深度为 ● | 依据的是 FlashBlade//S。EXA 尚未完成认证，而本章没有说明这一点 | 增加限定说明；改写"不要这样说"一行（STX 是参考设计，而非认证） | 已修复 |
| 49 | 定位与第 24 章（架构类别）及第 46 章（x/y、IDC 份额）的一致性 | 其他方面一致 | 无 | 已核实 |
| 50 | "38% of the weight rests on placeholders"（38% 的权重落在占位值上） | 五个低置信度维度中有四个是占位的 3 分，但客户维度评分为 2。算术（2.83；2.14–3.66）正确 | 重新标注为 "low-confidence scores, four of them placeholders"（低置信度评分，其中四个为占位值）；并解释客户维度为何评 2 分 | 已修复 |
| 50 | WEKA 算例仅使用公开数据 | 已确认：每个单元格都有指向公开来源的脚注；SHI 价格标注了 VERIFY；方法示意免责声明齐备 | 路线图单元格注明未找到 NeuralMesh 6 GA | 已核实 |

## 未解决事项 / 分歧

- **第 41 章和第 43 章仍沿用旧的 EXA 认证措辞（超出我的范围；请统一）。**
  - 第 41 章第 184 行写作 "NVIDIA-Certified Storage claimed for EXA in March 2026"。
  - 第 43 章表 43.3 写作 "STX partner; NVIDIA-Certified Storage (Mar 2026)"。
  - 两处都应改为 "extension of NVIDIA-Certified Storage validation announced Mar 2026; no completed EXA certification found by 2026-11-01"（2026 年 3 月宣布扩展 NVIDIA-Certified Storage 验证；截至 2026-11-01 未发现 EXA 已完成认证）。
- **第 44 章表格（KV 缓存层，VAST 列）** 写作 "CNode-X with NVIDIA context-memory support"。在第 42 章和第 45 章中，VAST 的 KV 方案是 BlueField-4 CNode 加 VUA，而 CNode-X 是存储内置 GPU 的节点。第 44 章审校人应核查此处。
- **第 49 章矩阵 3，WEKA 势头 0.48 对 Hammerspace 0.58。** 考虑到 AMG 率先推出、NeuralMesh 6 和 WEKApod 3 已发布，且有 OCI 验证，这一评分对 WEKA 可以说偏严。我未作修改，因为 "flat valuation, HPE exit"（估值持平、HPE 退出）是一种站得住脚的解读。值得向竞争情报人员求证。
- **第 49 章 KV 缓存单元格。** 按本章自身的图例，Everpure 的 ● 和 VAST 的 ◐ 都处于临界。我没有修改单元格，建议由主代理决定在 GA 得到确认之前是否将 PureKVA 改为 ◐。
- **仍待解决：** VAST Azure GA 状态、NeuralMesh 6 GA，以及 8-K 表格中 HPE 存储的精确数字。均已记入 staging。
