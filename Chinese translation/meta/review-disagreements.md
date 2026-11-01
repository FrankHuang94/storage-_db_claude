> 📄 英文原文：[meta/review-disagreements.md](../../meta/review-disagreements.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

本文件汇总自 `meta/reviews/` 中各份独立审校报告（第 2 阶段）的 `## Unresolved / disagreements`（未解决事项 / 分歧）部分。每一项要么是审校人无法依据本环境可访问的公开来源解决的问题，要么是审校人与起草作者之间的分歧。

### 来自 `part0.md`

- **第 26 章与第 14 章，FlashArray NVRAM。** 第 26 章（正文及图 26.1）写作 "NVRAM mirrored across both controllers"（NVRAM 在两个控制器之间镜像）。第 14 章（第 3a 部分）则称其位于机箱内并双路接入（//m），或位于 DFMD 模块上（//XL）。两者之一应当修改。0.2 现采用中性措辞。
- **第 27 章图 27.1 图注** 称两个产品家族都分化为 TLC 性能层和 QLC 容量层。而第 27 章自己的表 27.1 列出的 FlashBlade//S 使用 QLC DFM。该图注应由第 27 章负责人修正。
- **第 29 章第 59 行** 仍写作 "Analysts identified the customer as Meta"（分析师认定该客户为 Meta），尽管第 29 章的要点速览（第 4 部分之后）称 Meta 已在 FY25 10-K 中被点名。另请注意，2026 年 8 月的一份搜索摘要称 "Everpure has not confirmed"（Everpure 未予确认）Meta。10-K 点名一事仅依据对该文件的搜索摘要。
- **第 59 章标题与大纲** 写的是 200 张闪卡，但卡片集实有 279 张。
- **300 TB DFM。** "Released in 2025"（2025 年发布）仍只依据 FY26 10-K 的一份搜索摘要。未找到 GA 或出货公告。第 26 章的 VERIFY 保留。
- **ARR 精度。** Q2 FY27 新闻稿的搜索摘要四舍五入为 "$2.1B"。图谱中的 $2.13B 来自图表 CSV 的备注。
- **第 4 部分的一项待解问题已解决。** 股票代码变更新闻稿（Nasdaq/PR Newswire，2026-04-07）确认 CUSIP 不变，与第 25 章所述一致。
- **`meta/open-questions.md`** 仍报告 200 个 VERIFY 标记，而行内实有 177 个。请重新运行 `scripts/build_meta.py`。

### 来自 `part1.md`

- **第 38 章（超出我的范围）使用了相同的 TCO 介质输入**（来自 2026 年第一季度的 HDD $22/TB；按 122 TB 街价计算的 QLC $302/TB）。它应附上同样的限定说明：隐含溢价为 13.7×，而非标题中的 22.6×，且按同一指数，HDD 到 2026 年第三季度已达约 $40/TB。请核查 TechRadar $37,128 价格的日期。
- **2026 年 SSD:HDD 溢价** 仍只依据一家混合存储厂商（VDURA）来源未披露的指数，且该指数曾在 QLC 与 TLC 口径之间切换。未找到 TrendForce 或 Coughlin 的佐证。
- **表 2.1 中的 P/E 区间** 现由 DWPD 额定值推导，而非来自 NAND 厂商的披露（厂商很少公布）。
- **DFM 撤离（evacuation）的说法**（第 6 章，第 26 章可能也有）：没有公开的小时数。请向 Everpure 工程团队询问 150 TB 和 300 TB 下撤离与重建的时间对比。
- **300 TB DFM GA**（第 2、4 章）：只有 2023 年路线图（"2026"）和 B&F 2026-08-11 的报道支持。
- **Right-Size Guarantee 期限**：来源相互冲突（较早材料为 6 个月，较新的博客为 12 个月）。本章保留 12 个月，并在脚注上保留 VERIFY。
- **EUC 定义**：我写明 Evergreen//One 的有效已用容量（EUC）是在数据缩减之前计量的。计费单位文档确认了 EUC，但我没有看到其正式定义。值得对照现行 Product Guide 核查一次。
- **流程说明：** 我误运行了一次只读的 `git status`（未通过 git 做任何改动）。

### 来自 `part2.md`

- **第 7 章：** Purity//FA 6.4.2（NVMe/TCP）的确切 GA 月份。来源在 2022 年与 2023 年之间相互冲突。
- **第 7 章：** Crehan Research 的 FC +6%（2025 年）仍只有搜索摘要支撑。
- **第 8 章 / 第 11 章：** FlashBlade//S 对 GDS/NFS-over-RDMA 的支持（Purity//FB 4.3.4，2023 年 10 月）依据的是 iThome 的一份搜索摘要，且未出现在 NVIDIA GDS 发布说明的合作伙伴表中。应由能访问 Everpure 发布说明的人确认。这也关系到第 34 章的 "FlashBlade//S holds the full set"（FlashBlade//S 具备全部认证）。
- **第 8 章 / 第 11 章：** FlashBlade//EXA 的 GDS 依据的是一份 Portworx 文档的搜索摘要。EXA 的 NVIDIA 认证未公开。一份 SPECstorage AI_IMAGE 披露（2026 年 1 月，Purity//FB 4.6.4）描述了通往数据节点的、启用 RDMA 的 pNFS。如有需要，可在第 16/27 章中引用。
- **第 9 章：** FlashBlade S3-over-RDMA 的 GA 状态。Pure 在 2025 年承诺 "later this year"（今年晚些时候）推出；截至 2026-11-01 未找到 GA 公告。如果仍未 GA，第 11 章的 "Everpure has announced it"（Everpure 已宣布）是准确的，但不应升级为 "ships"（已出货）。
- **第 10 章：** Everpure 关于 Spectrum-X 读 +25% / 写 +23% 的数字在任何搜索中都未找到。保留 VERIFY 或删除这些数字。MetaRoCE（2026 年 8 月）仍未经核实。
- **第 11 章：** Lambda 的标价（US$3.99 对 US$2.99）未解决。由于中档数字仅为示意，这不影响结论。
- **第 12 章：** 正在出货的最大 E1.S/E3.S 容量、U.2 功耗等级、CXL 3.1 的发布日期以及 2015–2019 年 Optane 的各个日期仍为 VERIFY。E1.S 的尺寸（33.75 × 118.75 mm）看起来是外壳尺寸；PCB 为 31.5 × 111.49 mm。我未作修改。

### 来自 `part3a.md`

- **第 24 章（超出我的范围）重复了 FlashBlade//S 的错误**，见第 16 行（"a blade scale-out it calls shared-everything"，即"一种它称为全共享的刀片横向扩展架构"）以及第 118 行表格（"Everpure calls it shared-everything"，即"Everpure 称其为全共享"）。这些应与修正后的第 15 章保持一致：Pure 称 Purity//FB 为 "partitioned-writer"（分区写入者）。第 27 章也应检查是否有相同措辞。
- **FlashBlade//EXA 数据节点的保护方案**（第 16、17 章）仍未经核实。没有公开来源记载数据节点之间的纠删码或故障域，一份 2026 年的第三方评分卡也将其列为未解决。
- **FlashBlade//S 的多机箱数据放置以及当前 Purity//FB 的 PUT 副本数**（第 15、18 章）仍未经核实。
- **NetApp AFF 在 ONTAP 9.19.1 中的对称 active/active**（第 14 章）：依据的是一篇 NetApp Community 帖子。官方发布说明的确认仍待落实。
- **Facebook 180 TB/天：** 如果有人能访问 arXiv 1309.0186，其扩展版论文可能给出接近 180 TB 的中位数。本章现采用 USENIX 摘要中较保守的 ">100 TB/day"（每天超过 100 TB）。
- **AFX 支持的控制器数量**（9.19.1 中为 32 个）仅来自 WWT 的一份摘要。应对照 NetApp Hardware Universe 核查。
- **WebFetch 被阻止**访问 blog.everpuredata.com 和 arxiv.org。新增的 Everpure 博客引文来自搜索摘要，并已在脚注中注明。

### 来自 `part3b.md`

- **FlashBlade//EXA 数据节点的保护方案**（第 24 章工程师问题，第 16/17 章）。公开来源中仍无记载。第 24 章现已明确说明这一点。
- **Everpure Q2 FY27 产品/订阅毛利率（66.2% / 74.9%）**。这些数字仅来自 Quartr 和 investing.com 的摘要；我无法从 sec.gov 获取 8-K 附件。它们很可能是非 GAAP 数字，现已如此标注。请对照 8-K 的毛利率表确认。
- **Broadcom FY2025 基础设施软件收入（约 US$27B）**。看似合理，但未经确认；请核查 10-K。
- **Evergreen//One Overdrive**（第 23 章）。未找到其条款或 GA 的来源。
- **Meta Tectonic 扁平化为单一 ZippyDB schema**（第 21 章，Blocks & Files 2026-07-27）。搜索没有返回结果，因此保留 VERIFY。
- **Pure1 Manage MCP 服务器 GA**（第 22 章）。仅在一篇 Everpure 博客中有描述，且是通过搜索摘要看到的。
- **第 24 章热力图仍属本图谱的判断。** 我仍建议请 Everpure 现场工程师对有争议的单元格进行合理性检查，尤其是新的 pNFS 分离象限位置。staging 中的 ASK/VERIFY 保留。
- **第 27 章（超出范围）。** 我用 grep 检索了 "calls it shared-everything" 及类似的 FlashBlade 措辞，在第 15/16 章之外没有发现残留（在这两章中它现在只出现在纠正性的语境里）。
- **网络。** 本会话中 usenix.org 和 docs.aws.amazon.com 无法解析，blog.everpuredata.com 和 sec.gov 也未被抓取。所有对照这些来源的核查都依赖搜索摘要。

### 来自 `part4.md`

- **第 26 章：300 TB DFM 状态。** FY26 10-K 中 "released in 2025" 的解读仅来自一份搜索摘要。2025 年 6 月 StorageReview 的一篇文章称 300 TB 模块 "expected by end-2025"（预计于 2025 年底推出）。未找到 GA 或出货新闻稿。VERIFY 标记保留。
- **第 27 章：FlashBlade//EXA 的 NCP 和 SuperPOD 认证** 按最新公开来源仍处于待定状态，基于 DFM 的数据节点也仍未确认 GA。两者都是新兴 GPU 云（neocloud）交易的关键门槛。
- **第 29 章：超大规模业务毛利率。** 分析师的估计（75–85%，纯授权费业务 >90%）在实质上与管理层的表态相冲突——管理层称较新的模式使超大规模业务毛利率更接近公司平均水平。我将 85% 视为上限。真实数字未披露。
- **第 29 章：Q4 FY26 产品毛利率 "67.3%, up more than 400 bp on mix"（67.3%，因产品组合上升超过 400 个基点）。** 未确认这是 GAAP 还是非 GAAP 口径，也未确认是否为同比比较。保持原样。
- **第 25 章：CUSIP。** 正文称更名后 CUSIP 不变。这依据的是引用股票代码变更新闻稿的研究笔记；我没有独立确认。
- **格式说明。** 我对全部五章的脚注重新编号。其他编辑这些文件的代理应重新阅读 Sources 部分，而不要沿用旧的脚注编号。

### 来自 `part5a.md`

- **第 11 章（超出我的范围）** 仍带有 Dynamo 的 "[VERIFY: announcement date]"（[VERIFY: 发布日期]）。该日期现已确认为 2025-03-18（NVIDIA Newsroom，即第 32 章脚注 19），第 11 章可以删除该标记。
- **SuperPOD 存储表**（第 31 章 H100，第 34 章 B200/B300）：只看到了 H100 每个 SU 的读取行（15/40/125），且仅见于一段摘录。每节点 40/20 的数字、62 GB/s 写入、B200 标准/增强版 40/20 与 125/62，以及 B300 640/2,000 的数字，都需要直接阅读 docs.nvidia.com，而该站点在本会话中被阻止。
- **NVCS Enterprise 级的 GPU 数量**（约 1,000）未经确认。
- **Kokolis 等人对 16K GPU 规模下 1.8 小时的预测** 来自二手摘要。应核查 arXiv 2410.21680。
- **Llama 3 §3.3 中的数字** 与我对论文的理解一致，但本会话中无法访问 arXiv。
- **PureKVA：** 它是否真的在 2026 年 10 月达到 GA，以及 20× TTFT 说法背后的测试条件，两者都仍待解。
- **Pinecone 寻求出售**（第 33 章）：两次搜索都一无所获。VERIFY 保留。如果找不到一手报道，可考虑弱化为 "faced reported strategic pressure"（据报道面临战略压力）或删除该分句。
- **VAST 参与 NVIDIA 的 E 轮**（第 34 章）：未解决，保留 VERIFY。
- **Common Crawl ">10 PB"** 和 **S3 500T 个对象**（第 30 章）：仍只有搜索摘要支撑，保留 VERIFY。

### 来自 `part5b.md`

- **第 35 章——Cisco NCP 容量规划（每 GPU 0.16 GB/s）。** 这是 "sixfold spread"（六倍差距）的下限。仅有一份搜索摘要支持；必须在网络设置中允许 cisco.com 才能核查该 PDF。
- **第 35 章——Oracle FY2026 资本开支 US$55.7B。** 唯一来源是二手来源（引用 The Register）。CoreWeave 将于 11 月中旬发布的 Q3 2026 业绩会使 Q2 的数字过时。
- **第 35 章——示意成本。** 按 2026 年 NAND 价格，"US$1,000 per usable TB over four years"（四年期每可用 TB US$1,000）显得偏低：仅介质成本在系统加价之前就约为每 TB 原始容量 $302。利用率结论成立，但满额售出时 70% 的毛利率美化了新兴 GPU 云的情况。可考虑加入按 2026 年价格的敏感性分析。
- **第 36 章——S3 峰值带宽约 1 PB/s。** 唯一来源是二手来源。Meta 2024/2025/2026 年的工程博文仅通过搜索摘录阅读。
- **第 37 章——v3.0 规则。** 有三项需要 MLCommons v3.0 的结果和规则页面，而这些页面在此无法访问：
  - 向量数据库数据集规模（10M 对 1M）及其索引类型；
  - 功耗和机架空间效率是否为报告指标；
  - EXA 是否参加了任何训练工作负载。
- **第 37 章——模型规模。** 1T 级检查点对应的模型（llama3-1t 对 1.25T）仍留在 staging 中。
- **第 38 章——单一来源输入。** DBox 和 WD JBOD 的功耗、FlashBlade//S500 的 1.3 W/TB、DDN 每台设备的容量以及 EIA 电价，都只有搜索摘要支撑。因此若干 TB/W 图表柱仅依据单一来源。
- **第 38 章——硬盘功耗口径。** 盘级 TB/W 混用了不同口径：QLC 用最大额定值，44 TB HDD 用 "operating"（运行）值，DFM 用 "under 10 W typical"（典型值低于 10 W）。图注提醒要同口径比较，但要点速览中的 "~2×"（约 2 倍）使用的是混合口径。我未作修改，因为方向是稳健的。
- **第 39 章——待核查事项。** 无法核查 Everpure 的 OSI 成员身份；未能成功检索 OSI 名录网站。NetApp AI Data Engine 的 GA 日期仍未确认。
- **流程说明。** `scripts/make_charts.py` 会重新生成所有图表，而 matplotlib 的 SVG ID 未加盐（`svg.hashsalt` 未设置）。因此运行它可能会改动审校人范围之外的图表文件。建议在 `scripts/charts/_style.py` 中设置 `svg.hashsalt`。

### 来自 `part6a.md`

- **IDC 2Q26 厂商份额（第 40 章）。** Huawei 11.3%、NetApp 9.6%、Everpure 8.1% 和 HPE 6.8% 无法再次确认：idc.com 被阻止，且该表格是图片。Dell 23.8% 和总数已确认。应由有 IDC 访问权限的人核查。
- **VAST 财年结束月份（第 40、41、42 章）。** 新闻稿只写了 "exited fiscal year 2026"（结束了 2026 财年）。
- **VAST Azure Native ISV Service GA（第 42、43 章）。** 未找到 GA 确认。VAST 自己的新闻稿页面似乎含有未填写的占位符，因此其 "now available"（现已上市）的措辞应视为不可靠。
- **CNode-X 的出货状态以及 Cisco 是否销售它（第 42 章表 42.1）。** 只找到了 Supermicro 的发布信息。
- **WEKA E 轮的一级/二级（primary/secondary）拆分（第 43 章正文及 `data/ch43_funding.csv`）。** CSV 仍显示 US$40M 为二级部分。我没有修改图表，因为该拆分看似合理但未经确认。
- **WEKApod 3 每机架 10.2 TB/s / 210M IOPS，以及 NeuralMesh 6 GA（第 43 章）。** 均未确认。
- **DDN 收入基数（第 41、44 章）。** Forbes 给出 US$400M/US$500M；B&F 给出 US$500M（2023 年）和 US$750M（2024 年估算）。两者不可能都对，而第 41 章 12.5× 的倍数使用的是 Forbes 的数字。我对以 Forbes 数字为主略有异议，但两方面都没有证据。
- **Blackstone–DDN 日期。** 第 41 章写 2025-01-09，第 44 章写 2025-01-08。Business Wire 的编号显示为 1 月 8 日，媒体报道则为 1 月 9 日。无关紧要；保持原样。
- **VAST 写入确认机制（第 42 章）。** "Mirrored into SCM on two enclosures"（镜像写入两个机柜的 SCM）与第 16 章一致，但本会话中我无法对照 VAST 文档确认确切的副本数。

### 来自 `part6b.md`

- **第 41 章和第 43 章仍沿用旧的 EXA 认证措辞（超出我的范围；请统一）。**
  - 第 41 章第 184 行写作 "NVIDIA-Certified Storage claimed for EXA in March 2026"。
  - 第 43 章表 43.3 写作 "STX partner; NVIDIA-Certified Storage (Mar 2026)"。
  - 两处都应改为 "extension of NVIDIA-Certified Storage validation announced Mar 2026; no completed EXA certification found by 2026-11-01"（2026 年 3 月宣布扩展 NVIDIA-Certified Storage 验证；截至 2026-11-01 未发现 EXA 已完成认证）。
- **第 44 章表格（KV 缓存层，VAST 列）** 写作 "CNode-X with NVIDIA context-memory support"。在第 42 章和第 45 章中，VAST 的 KV 方案是 BlueField-4 CNode 加 VUA，而 CNode-X 是存储内置 GPU 的节点。第 44 章审校人应核查此处。
- **第 49 章矩阵 3，WEKA 势头 0.48 对 Hammerspace 0.58。** 考虑到 AMG 率先推出、NeuralMesh 6 和 WEKApod 3 已发布，且有 OCI 验证，这一评分对 WEKA 可以说偏严。我未作修改，因为 "flat valuation, HPE exit"（估值持平、HPE 退出）是一种站得住脚的解读。值得向竞争情报人员求证。
- **第 49 章 KV 缓存单元格。** 按本章自身的图例，Everpure 的 ● 和 VAST 的 ◐ 都处于临界。我没有修改单元格，建议由主代理决定在 GA 得到确认之前是否将 PureKVA 改为 ◐。
- **仍待解决：** VAST Azure GA 状态、NeuralMesh 6 GA，以及 8-K 表格中 HPE 存储的精确数字。均已记入 staging。

### 来自 `part7.md`

- **第 51 / 52 章，仅有搜索摘要支撑的图表锚点。** 以下各项在 CSV 状态列和 staging 中仍为 VERIFY：RAMAC $10,000/MB（IBM 自己的估计约为 $11.4k/MB）、3380 的标价区间、SunDisk 1991 年数据点、Semico/iSuppli 2005 年 $45/GB 数字、2008 年 TrendForce NAND 份额以及 TrendForce 2026 年晶圆现货读数。它们都不会改变数量级或方向，但 2008 年的份额决定了 HHI 对比。
- **第 51 章，Symmetrix 41% 对 IBM 35%（1995 年）。** 仍只依据 The Register 的一篇访谈。保留 "by one account"（据一种说法）的表述。
- **第 53 章，PureKVA/CMX 与趋势 1。** Colgrove 关于 600 TB / 1 PB 的表述以及 Meta 关于 512 TB 的表述仍未经核实。Gartner 关于智能体运维（agentic ops）的预测（2028 年由 <1% 增至 20%）仍只有搜索摘要支撑。
- **第 53 章，图 53.2 与正文。** 正文把 "Disaggregation and DPUs"（解耦与 DPU）称为 "table stakes"（基本门槛），但图中把它放在"立即押注"象限，而图表中的 "Table stakes" 象限含义是高确定性、低影响。这是措辞冲突而非错误；作者可考虑重命名该象限或该判断。
- **第 54 章，"four deals in 17 years cost about $594M"（17 年内四笔交易共花费约 $594M）。** 这意味着 StorReduce 约为 $20M，我未核实。无论如何，总额都在四舍五入范围内。
- **第 54 章，关口 3 中 WEKA 约 16× ARR 与 VAST 约 60× 已承诺 ARR 的估值倍数。** 两者均为公司自述，经由第 43 章引用。我保留了它们，因为它们是估值基准，而非目标。

### 来自 `part8.md`

- **第 45 章和第 49 章（第 6 部分，超出我的范围；当时尚无第 6 部分审校文件）** 仍把 EXA 的 MLPerf v3.0 结果称为 "audited"（经审计）。第 49 章的要点速览还写道 Everpure "is the only array vendor selling that IP into hyperscalers"（是唯一向超大规模云厂商销售该 IP 的阵列厂商）。第 34 章 / 第 5a 部分以及第 29、36 章 / 第 4–5b 部分已将这些措辞分别改为 "public, peer-reviewed"（公开、经同行评审）和 "only array vendor publicly known to…"（公开已知唯一……的阵列厂商）。第 8 部分现已使用修正后的措辞，因此在第 6 部分审校人统一这些章节之前，第 8 部分与第 6 部分存在不一致。
- **第 59 章标题与内容。** 大纲、`mkdocs.yml`、`docs/index.md` 和 `README.md` 写的是 "200 flashcards"（200 张闪卡）（第 58 章为 "60 one-liners"，即 60 条一句话要点），但章节实际包含 279 张卡片和 66 条一句话要点。我没有修改 H1 或导航，它们由 `meta/outline.md` 固定。主代理可考虑更新索引简介（"279 flashcards"、"66 one-liners"）。
- **第 59 章没有针对第 54 章**（战略选项地图）的卡片，因为第 54 章是在卡片集完成之后才完成的。下次重新生成卡片集时，可补充几张第 54 章的卡片。
- **卡片隐含地承载了上游的 VERIFY。** Q135 和 Q261（300 TB DFM "released 2025"）、Q181（NVCS Enterprise 约 1,000）、Q43（FC +6%，仅有搜索摘要）以及 Q226（HPE 停止转售 WEKA）的可靠程度取决于其所在章节。如果这些 VERIFY 的结论有变，请重新生成卡片。
- **PureKVA GA。** 第 55、57、58、59 章和产品阵容 SVG 现均写作 "announced for October 2026"（已宣布 2026 年 10 月上市）。如果 Everpure 确认 GA，请同时更新这五处。
- **第 55 章 / 第 28 章：Fusion 附加率所依据的客户基数**（约 14,500 对约 15,000）仍为 VERIFY。无论取哪个数，约 8% 的数字都不变。
- **网络。** 未进行网络搜索；所有事实均对照已审校的章节和审校文件核查。
