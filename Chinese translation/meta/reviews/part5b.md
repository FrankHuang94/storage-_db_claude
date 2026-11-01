# 第二阶段审阅 — 第 5b 部分：AI 存储（第 35–39 章）

> 📄 英文原文：[meta/reviews/part5b.md](../../../meta/reviews/part5b.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

审阅人：独立审阅人（持怀疑态度的存储工程师兼买方分析师），2026-11-01。范围：`docs/05-ai-storage/35…39`，及其图表、CSV 和暂存文件。

## 摘要

**核查内容（约 35 次网络检索）。** 本会话无法抓取 cisco.com、docs.nvidia.com 和 files.futurememorystorage.com，因此这些来源依赖检索结果摘要。
- **新兴 GPU 云（neocloud）：**
  - CoreWeave：10-K FY2025 电力数字、Q2 2026 电力、资本开支与积压订单、2025 年资本开支的计量口径，以及存储定价。
  - Nebius：Q2 2026 目标与预付款，以及 2025 年 9 月的可转债。
  - 交易：Microsoft–Nscale、Backblaze–CoreWeave，以及 Lambda–VAST 的合作历史。
  - 参考设计：Cisco NCP 存储设计及 NVIDIA 的 NCP 存储要求。
- **超大规模云厂商系统：** S3 规模、Google Next '26（Rapid Bucket、Managed Lustre）、Azure AMLFS 20、Meta 的 QLC 文章及其 FMS 2025 演示材料。
- **MLPerf Storage：** v0.5 和 v1.0 提交者、v3.0 参与情况与缺席者、EXA 检查点读取与 KV 缓存数字、训练负载领先者、向量数据库测试设计，以及机架单元与功耗披露规则。
- **IO500：** 首份榜单（SC17）以及 Sugon/Aurora 在 ISC26 的得分。
- **第 38 章：** DDN AI400X3 容量、VAST DBox 的硬盘类别，以及 Nadella 播客日期。我重新计算了 100 PB 算例的每一行，以及机架密度和 TB/W 图表的输入数据。
- **第 39 章：** 1touch 价格与交割日期、Digital Omnibus（Regulation 2026/1744）、OSI 成员、Cyera，以及 NetApp AIDE 的 GA 日期。

**重新计算。** 100 PB 算例的算术无误：
- 硬盘数量：3,030 与 543。
- IT 功耗：45.5 与 23.9 kW。
- PUE 1.3 下的设施功耗：59.1 与 31.1 kW。
- 五年能耗：2.59 与 1.36 GWh，即节省 1.23 GWh，价值约 $170K。
- 介质溢价：$8.5–37.3M。
- 隐含碳排放：21.3 对 2.7 kt。

其他算例数字同样无误：第 35 章的毛利率与电力、第 36 章的 3FS 与检查点计算、第 37 章的归一化表与每节点速率、第 39 章的访问决策。**问题出在解读，而非算术：**
- 第 38 章"escape route 1"（出路 1）夸大了 GPU 方面的论据。
- 第 38 章沿用了第 4 章偏于乐观的介质溢价却未加说明。此项应协调人要求补充，与 `part1.md` 中第 4 章的修正保持一致。

**结论。**
- **第 35 章：实质性修正。** NCP"存储需在 GPU 到货前 8 周就绪"的要求表述有误；"存储 ≈ 资本开支的 1%"是由单一合同推而广之；Nebius 可转债规模被当作超额配售选择权已行使来表述；EXA 的 DFM 功率密度优势被套用到仍采用第三方服务器的数据层上。
- **第 36 章：小幅修正。**
- **第 37 章：小幅至实质性修正。** 解决了四处 VERIFY。EXA 的 KV 缓存领先现已附上规模方面的保留说明（以公平对待竞争对手）。检查点读取定为 588 GiB/s。
- **第 38 章：实质性修正。** GPU 槽位论据夸大了闪存的优势；缺少介质溢价的保留说明；DDN 的柱形被当作上限呈现。
- **第 39 章：小幅修正。**

**QA。** 五章均通过 `qa_report.py`；Mermaid lint 为 OK；`check_links --allow-planned` 显示 0 个失效链接。

**修改后字数（预算）：**
| 章 | 字数 | 预算 |
|---|---|---|
| 35 | 2,305 | 1,900 |
| 36 | 2,381 | 2,000 |
| 37 | 2,425 | 2,000 |
| 38 | 2,274 | 1,800 |
| 39 | 2,085 | 1,800 |

第 35、37、38 章的阅读时间已更新。五章的脚注均按首次引用顺序重新编号。

**整理工作。** 运行 `scripts/make_charts.py` 重新生成了全部图表 SVG。只有第 38 章 CSV 的配置说明发生了变化，但 matplotlib 可能会改写我范围之外图表的内部 SVG ID；这些图表的内容未变。

## 审阅发现

| 章 | 论断 / 段落 | 问题 | 已作修改 | 状态 |
|---|---|---|---|---|
| 35 | NCP 要求："storage integrated through the API eight weeks before the GPUs arrive"（存储须在 GPU 到货前八周通过 API 完成集成）（正文、表 35.1、"关键数字"表） | **有误。** NVIDIA 的要求是对*数据迁移系统*设置 T-minus-8 周（交付前 8 周）里程碑。数据迁移存储约在交付前 2 周到位。每 PB 99.5% 的可用时间要求适用于高速文件系统；NFSv4 home 层的目标为 99.99%。 | 正文、表格行和"关键数字"行均已重写。脚注现引用 v2.4 要求（2026-09-01）。 | 已修复 |
| 35 | 要点速览 / "不要这样说"："Storage is roughly 1% of a neocloud's capex"（存储约占新兴 GPU 云资本开支的 1%） | 由单一合同推而广之。CoreWeave 还采购 WEKA、DDN 和 IBM 的席位，自建对象存储层，并向 Backblaze 付费。 | 重新表述为"the largest disclosed storage contract is about 1% a year of its customer's capex"（已披露的最大存储合同约占其客户每年资本开支的 1%）。 | 已修复 |
| 35 | Nebius"issued about US$3.16 billion of convertible notes"（发行了约 US$3.16B 可转换票据） | 定价规模为 US$2.75B；只有在购买方的选择权全额行使时才是 US$3.16B。 | 已更正，并补充 Nebius 定价新闻稿。 | 已修复 |
| 35 | Nebius 5 GW 目标与 50–60% 预付款 [2× VERIFY] | 经 Q2 2026 电话会报道确认。还需补充：签约电力 ≠ 已接入电力（到 2026 年底接入 0.8–1 GW），以及 2026 年超过 US$9B 的预付款。 | VERIFY 已解决，补充背景，并新增 MarketBeat 脚注。 | 已修复 |
| 35 | CoreWeave 电力仅使用 2025 年底数字；第 38 章使用 Q2 2026 数字（1.5 GW / 3.7 GW） | 跨章不一致（日期不同，二者均正确）。 | 正文和"关键数字"表中补充 Q2 2026 数字。 | 已修复 |
| 35 | Microsoft–Nscale"reportedly ~200,000 GB300"（据报道约 200,000 颗 GB300）[VERIFY] | 经 Nscale 2025-10-15 新闻稿确认（未披露金额）。原先列在 11 月事件下。 | 来源改为 Nscale 和 TechCrunch；移至 10 月；VERIFY 已解决。Nscale 的*存储*供应商仍为空缺，并在暂存中保留 VERIFY。 | 已修复 |
| 35 | 表 35.2：Everpure 契合点 ="DirectFlash power density"（DirectFlash 功率密度）；表注"power density and financing as its levers"（以功率密度和融资为抓手） | 偏向 Everpure 的过度表述。EXA 数据节点是第三方 NVMe 服务器（第 37 章、第 4 部分审阅），因此目前 DFM 密度只适用于元数据层。 | 契合点、弱点单元格和表注均已更正。 | 已修复 |
| 35 | Backblaze 一栏"$335M capacity deal"（$335M 容量交易） | 正确，但未说明 Backblaze 提供的是什么。 | 已澄清：为 CoreWeave AI Object Storage 背后的基于 HDD 的存储层，首批订单约 US$335M。 | 已修复 |
| 35 | 历史部分遗漏了 VAST 2023 年的订单 | US$1.17B 交易是对始于 2023 年的合作关系的*扩展*。VAST 先是 CoreWeave 的存储平台，后又成为 Lambda 的（2023 年 10 月）。 | 已补充至历史部分，并将 2025 年 11 月的交易改写为扩展。 | 已修复 |
| 35 | 图 35.3 CoreWeave 2025 年资本开支 US$14.9B"search-summary only"（仅检索摘要） | 为 Q4 电话会上的公司自述，按权责发生制计量；10-K 中现金资本开支为 US$10.3B。 | 已更新 CSV 的 `verified` 列和来源；暂存已更新。Oracle 仍为已标记状态。 | 已修复 / 已标记 |
| 35 | Cisco NCP 1,152 个 GPU 对应 180 GB/s [VERIFY] | 检索确认存在一个基于 Cisco 的 VAST EBox NVL72 设计，拓扑为 1,152 GPU，但未确认该数字。PDF 无法抓取。 | 已在暂存中细化 VERIFY。 | 已标记 |
| 36 | S3"500 trillion objects and ~1 PB/s in 2025"（2025 年 500 万亿个对象、约 1 PB/s）[VERIFY] | 对象数量与"hundreds of exabytes"（数百 EB）已由 re:Invent 2025 报道确认。1 PB/s 的数字经由 Wikipedia 追溯到 2024 年的一场演讲。 | 拆分该论断，新增 B&F 来源；VERIFY 收窄至带宽数字。 | 已修复 / 已标记 |
| 36 | Meta QLC"10 MB/s per TB, which 16–20 TB HDDs used to meet"（每 TB 10 MB/s，过去由 16–20 TB HDD 满足） | Meta 的文章中并没有"16–20 TB"的说法。文章把 QLC 定在约 10 MB/s/TB，TLC 承载 15–20 MB/s/TB 的批处理负载。Meta 的 FMS 演示材料显示 HDD 集群的实际供给为 5–7 MB/s/TB，低于正文计算出的最佳情形 12.5。 | 结合两点重写；新增 FMS 演示材料脚注。 | 已修复 |
| 36 | Everpure："Only array vendor inside a top-five hyperscaler's own storage"（唯一进入前五大超大规模云厂商自有存储的阵列厂商） | 无法证明。 | 改为"only array vendor *publicly known* to…"（*公开所知*唯一……的阵列厂商）。 | 已修复 |
| 36 | Google Managed Lustre"up to 10 TB/s"（最高 10 TB/s） | 已确认（Next '26），但这是 Google 自己的声明（约为其 2025 年数字的 10 倍）。Rapid Bucket 数字也已确认。 | 标注为 Google 自述。 | 已修复 |
| 36 | Azure AMLFS 20 | 已确认（2025-11-18）。正文遗漏了 25 PiB 上 512 GB/s 仅相当于 20 MB/s/TiB，属于偏重容量的存储层。 | 已补充背景。 | 已修复 |
| 37 | EXA 检查点读取 588.3 对 833.0 GiB/s [VERIFY] | 依据 Everpure 新闻稿、B&F 和 Techzine，为 588.28 GiB/s。StorageReview 的 833 与其自身的详细段落相矛盾。读取*低于* 877.5 GiB/s 的写入，以恢复为主的买家应注意这一点。 | 已解决，并附上该保留说明。工程师问题 2 现改为询问读取为何落后于写入。 | 已修复 |
| 37 | EXA KV 缓存"1,623.4 GiB/s on 51 hosts, far ahead of the next entrants"（51 台主机 1,623.4 GiB/s，远超其后参赛者） | 按本章自身的逻辑，这种表述不公平：领先的标准规模提交（UBIX、FarmGPU，约 444 GiB/s）使用的配置更小。 | 改写为：领先部分源于规模，因此应按每主机归一化。 | 已修复 |
| 37 | v3.0 参与情况 | 缺席名单遗漏了 v2.0 提交者 Huawei、Hammerspace 和 Lightbits。Nebius 和 NVIDIA 为首次提交。 | 已补充。 | 已修复 |
| 37 | WEKA MLPerf v1.0"reportedly"（据报道）[VERIFY]；v0.5/IO500 日期 [VERIFY] | WEKA（以及 DDN）提交了 v0.5（2023 年 9 月）和 v1.0。首份 IO500 榜单发布于 SC17（2017-11-15）。 | 表 37.3 已更正；三处 VERIFY 已附来源解决。 | 已修复 |
| 37 | IO500 Sugon 79,110 对 Aurora 32,166 [VERIFY] | 经 Sugon 自己的新闻稿（500 个客户端节点）和 Tom's Hardware 确认。调整原因是缺乏可广泛获得的架构细节。 | 已附来源解决。 | 已修复 |
| 37 | "on-premises submissions disclose power and rack units"（本地部署提交须披露功耗和机架单元） | 规则要求披露机架单元以及上电硬件*清单*；实测功耗为可选项。 | 表述已精确化。 | 已修复 |
| 37 | 向量数据库"DiskANN in every submission"（每个提交都使用 DiskANN） | B&F 描述的是基于 Milvus 的测试（在给定召回率下的 QPS）。DiskANN 只是索引选项之一。 | 已改写；数据集规模和索引仍保留 VERIFY。 | 已修复 / 已标记 |
| 37 | EXA 训练负载提交 [VERIFY] | U-Net 表格（YanRong 543.9、HPE K3000 345.8 GiB/s）中没有 EXA 条目，但没有来源明确这么说。 | 结合该证据细化 VERIFY。 | 已标记 |
| 38 | 出路 1：13 个 GPU 赚取"$3.5M of gross rental… At mid-2025 prices, with exabyte scale… it starts to"（$3.5M 的总租金收入……按 2025 年中价格、在 EB 级规模下……开始能够） | **夸大（偏向闪存）。** (a) 总租金收入忽略了 GPU 资本开支、融资和运营成本。(b) 把 H100 的价格套用到 GB200 级别的电力槽位上。(c) 规模无济于事，因为溢价和释放出的电力都随容量线性增长。按 2025 年中价格，上限也覆盖不到约 $8.5M 溢价的一半。 | 改写为上限，并与第 4 章的每 kW-年 $15K（≈$1.6M）交叉核对，加上"only alongside routes 2 or 3"（仅在与出路 2 或 3 结合时）。要点速览相应调整。 | 已修复 |
| 38 | 介质成本行使用第 4 章的 $302 对 $22/TB（协调人要求） | 隐含溢价为 13.7 倍，而非指数显示的 22.6 倍。按指数约 $504/TB 计算，QLC 介质约为 $67M。到 Q3 2026 HDD 已升至约 $40/TB（HDD 介质约 $5.4M，溢价约 $35M）。 | 补充段落和表格行，与第 4 章当前文本一致；要点速览现写为"on Chapter 4's inputs, and more at index prices"（按第 4 章的输入，按指数价格则更高）。删除 ServNet 的 VERIFY（已有佐证，同第 4 章）。 | 已修复 |
| 38 | 能耗行使用 PUE 1.3；第 4 章使用 1.54 | 跨章不一致且未作说明。 | 已在表中注明：PUE 1.54 下节省约 $200K。 | 已修复 |
| 38 | DDN AI400X3 0.21 TB/W 作为最低的系统柱形 | 取决于配置，作为品类上限并不公平。AI400X3M（2026 年 6 月）每台设备最高提供 2 PB 可用容量。 | 正文和 CSV 配置说明中补充保留说明；单台容量仍保留 VERIFY。 | 已修复 / 已标记 |
| 38 | VAST"today's 61 TB-class DBoxes trail 245 TB-class designs"（当前 61 TB 级的 DBox 落后于 245 TB 级设计） | DBox 的 TB/W 取决于所装硬盘；"today's"（当前）暗示 VAST 没有更大容量的硬盘（未经核实）。 | 范围限定为图 38.2 中数据表所列的 DBox。 | 已修复 |
| 38 | FMS 2025 演示材料 [VERIFY: Meta 隶属关系] | 演讲者 Sumit Gupta 是 Meta 软件工程师（FMS 日程列表）。 | 隶属关系已解决；幻灯片措辞仍为 VERIFY。 | 已修复 / 已标记 |
| 39 | Digital Omnibus（Reg. 2026/1744） | 已确认：2026-07-24 公布，2026-07-27 生效，Annex III / Annex I 日期与正文所述一致。它还把第 50 条（Article 50）透明度义务保留在 2026 年 8 月 2 日，正文遗漏了这一点。 | 已补充，附 Lewis Silkin 来源。 | 已修复 |
| 39 | OSI："Databricks, Informatica, Salesforce, dbt Labs… were in the working group"（Databricks、Informatica、Salesforce、dbt Labs……均在工作组中） | Databricks 直到 2026 年 1 月更新时才加入。所找到的片段中未出现 Informatica。Snowflake 称 v1 只是一个起点。 | 已更正成员名单，并补充"起点"的保留说明。 | 已修复 |
| 39 | 1touch US$125.0M，2026-05-07 交割；Cyera US$12B | 均已确认（10-Q；SecurityWeek/Globes）。补充 Cyera 背景（一年前为 US$6B）。 | — | 已修复 |

## 未解决事项 / 分歧

- **第 35 章 — Cisco NCP 配置（每 GPU 0.16 GB/s）。** 这是"sixfold spread"（六倍差距）的下限，仅有检索摘要支持；需在网络设置中放行 cisco.com 才能核对 PDF。
- **第 35 章 — Oracle FY2026 资本开支 US$55.7B。** 唯一来源是二手的（引用 The Register）。CoreWeave 预计 11 月中旬发布的 Q3 2026 业绩会使 Q2 数字过时。
- **第 35 章 — 示意成本。** "US$1,000 per usable TB over four years"（四年每可用 TB US$1,000）按 2026 年 NAND 价格看偏低：仅介质就约为每原始 TB ~$302，尚未计入系统加价。利用率结论依然成立，但满载销售下 70% 的毛利率美化了新兴 GPU 云。建议做一个 2026 年价格的敏感性分析。
- **第 36 章 — S3 约 1 PB/s 峰值带宽。** 唯一来源是二手的。Meta 2024/2025/2026 年的工程博客文章仅通过检索摘录阅读。
- **第 37 章 — v3.0 规则。** 有三项需要 MLCommons v3.0 结果和规则页面，本会话无法访问：
  - 向量数据库的数据集规模（10M 对 1M）及其索引类型；
  - 功耗和机架空间效率是否为报告指标；
  - EXA 是否参加了任何训练负载。
- **第 37 章 — 模型规模。** 1T 级检查点的模型归属（llama3-1t 对 1.25T）仍留在暂存中。
- **第 38 章 — 单一来源输入。** DBox 与 WD JBOD 的瓦数、FlashBlade//S500 的 1.3 W/TB、DDN 单台设备容量以及 EIA 电价均仅有检索摘要支持。因此若干 TB/W 图表柱形依赖单一来源。
- **第 38 章 — 硬盘功耗口径。** 硬盘级 TB/W 混用了不同口径：QLC 用最大额定值，44 TB HDD 用"operating"（运行）功耗，DFM 用"under 10 W typical"（典型值低于 10 W）。图表表注提示应同口径比较，但要点速览中的"~2×"（约 2 倍）使用了混合口径。我未作修改，因为方向是稳健的。
- **第 39 章 — 待核事项。** 无法核实 Everpure 的 OSI 成员身份；未能成功检索 OSI 成员目录网站。NetApp AI Data Engine 的 GA 日期仍未确认。
- **流程说明。** `scripts/make_charts.py` 会重新生成所有图表，而 matplotlib 的 SVG ID 未加盐（`svg.hashsalt` 未设置）。因此运行它可能改动审阅人范围之外的图表文件。建议在 `scripts/charts/_style.py` 中设置 `svg.hashsalt`。
