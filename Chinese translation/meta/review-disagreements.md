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
