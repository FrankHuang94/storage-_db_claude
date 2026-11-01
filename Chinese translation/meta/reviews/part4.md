# 第二阶段审阅 — 第 4 部分：Everpure（第 25–29 章）

> 📄 英文原文：[meta/reviews/part4.md](../../../meta/reviews/part4.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

审阅人：独立审阅人（持怀疑态度的存储工程师兼买方分析师），2026-11-01。范围：`docs/04-everpure/25…29`。

## 摘要

**核查内容（约 16 次网络检索；sec.gov、everpuredata.com 及多数行业媒体网站无法抓取，因此依赖检索结果摘要）：**
- Everpure 财务：点名 Meta 的 FY25 10-K、Q3 FY26 毛利率、Q2 FY27 业绩、GAAP 与非 GAAP 毛利率、业绩指引沿革、2026 年 9 月 Financial Analyst Meeting（FAM，金融分析师大会）给出的 FY28 初步展望，以及 TrendForce 对 4Q26 NAND 价格的预测。
- 产品事实：DFM 容量、出货中的最大容量 SSD、FlashBlade//EXA 正式上市（GA）及 DFM 数据节点、MLPerf Storage v3.0，以及 NVIDIA 认证。
- Meta 交易及第二家超大规模云厂商的新闻稿。

**跨章一致性：**
- **财年标签**一致：FY26 截至 2026-02-01，Q2 FY27 截至 2026-08-02。
- **股票代码**全书一致：自 2026-04-17 起由 PSTG 改为 P。完整说明仅出现在第 25 章"第 5 阶段"（Era 5）中；第 25、26、29 章使用"NYSE: P, formerly PSTG"（纽交所代码 P，原 PSTG）。
- **ARR、RPO、收入、自由现金流（FCF）和指引**现已在第 25、28、29 章之间保持一致。

**结论：**
- **第 25 章：小幅修正。**
- **第 26 章：小幅修正。**
- **第 27 章：实质性修正。** 认证状态、EXA GA、MLPerf 缺席名单以及检查点算例存在错误或不完整。
- **第 28 章：小幅修正。** 删除了偏向性表述和重复内容。
- **第 29 章：实质性修正。** 关于 Meta 披露的说法有误；算例中混用了 GAAP 与非 GAAP 毛利率；超大规模业务毛利率被高估。

**字数（scripts/wordcount.py）：** 第 4 部分由 **11,413 降至 10,934**。
- 第 25 章：2,066 → 1,971
- 第 26 章：2,508 → 2,435
- 第 27 章：2,490 → 2,366
- 第 28 章：2,298 → 2,168
- 第 29 章：2,051 → 1,994

各章仍不低于字数预算的 108%。五章 QA 均为 PASS，Mermaid lint 为 OK，check_links 报告 0 个失效链接。

**整理工作：** 五章的脚注均按首次引用顺序重新编号，并删除了未使用的定义（第 28 章 [原 21、22] 和第 29 章 [原 12]）。同时从暂存文件 `meta/open-questions-staging/ch25–29.md` 中删除了已解决的条目。

## 审阅发现

| 章 | 论断 / 段落 | 问题 | 已作修改 | 状态 |
|---|---|---|---|---|
| 29 | 要点速览中"widely reported as Meta"（普遍报道为 Meta）；"不要这样说"中"Meta is a disclosed customer in the 10-K. Filings describe an unnamed top hyperscaler"（Meta 是 10-K 中披露的客户。文件描述的是一家未具名的头部超大规模云厂商）；首次点名日期上的 VERIFY | **有误。** FY2025 10-K 已点名 Meta 为 2024 年 12 月的设计导入（design win）。CEO 在 2025 年 3 月 EXA 发布会上也提到了 Meta。第 25 章已如此表述，因此第 25 章与第 29 章互相矛盾。 | 正文现改为 Meta 已在 FY25 10-K 中被点名，并新增脚注。"不要这样说"现改为提醒不要声称*第二家*超大规模云厂商已被点名。VERIFY 已解决。 | 已修复 |
| 26 | "analysts identified it as Meta"（分析师认定其为 Meta） | 同一问题。 | 现改为 FY2025 10-K 已点名 Meta。 | 已修复 |
| 29 | 算例："Q3 FY26 total GM rose to 72.3% from 70.2%"（Q3 FY26 总毛利率由 70.2% 升至 72.3%），并与非 GAAP 69.9% 的基数对比 | 该比较把 GAAP（72.3%）与非 GAAP 基数混在一起。还遗漏了管理层的表态：较新的超大规模模式（Everpure 供应组件）会使毛利率更接近公司平均水平。 | 现改用非 GAAP 产品毛利率 72.9%（由 67.4%）和 GAAP 72.3%，并分别标注口径。正文现把 85% 的超大规模毛利率视为上限情形。 | 已修复 |
| 26、28、29 | 产品毛利率 66.2% 与订阅毛利率 74.9% 未说明口径 | 二者均为非 GAAP：687×66.2% + 499×74.9% 可复算出非 GAAP 总毛利率 69.9%。 | 各处均标注为非 GAAP。 | 已修复 |
| 26 | "fewer components per terabyte, so 66.2% product gross margin … even during a NAND price spike"（每 TB 组件更少，因此即便 NAND 价格飙升，产品毛利率仍有 66.2%） | 因果关系夸大（偏向 Everpure）。非 GAAP 产品毛利率已由 Q3 FY26 的 72.9% 降至 66.2%。 | 改写为：较低的物料成本（BOM）对毛利率有支撑作用但无法使其免受冲击，并列明下降幅度。 | 已修复 |
| 29 | FY28 展望标注 [VERIFY] | 已解决。FAM（2026-09-23）给出 FY28 初步收入 $7.0–7.3B（+39–45%）和非 GAAP 营业利润 $1.7–1.9B。公司预计新增长方向（数据软件、Scale AI、超大规模）到 FY2030 仅占收入约 20%。 | 已补充并加脚注。20% 这一数字也是对"平台型公司"叙事的有益制约。 | 已修复 |
| 29 | 第二家超大规模云厂商 | 正文遗漏了新闻稿本身的保留说明：该客户可能不会按设想的量下单。 | 已补充该保留说明。 | 已修复 |
| 25 | 要点速览：超大规模订单"arrived as FY2027 revenue guidance rose to $5.03–5.07B"（在 FY2027 收入指引上调至 $5.03–5.07B 之际到来） | 暗示授权类订单导致了指引上调。超大规模业务在 FY27 收入中占比很小。 | 已改写。 | 已修复 |
| 25 | "FY2027 Q2 FCF −$238M because the company prepaid for NAND"（因公司预付 NAND 款项，FY2027 Q2 自由现金流为 −$238M） | 原因被夸大（"预付"是第三方解读），且财年标签不一致。 | 改为"Q2 FY2027 … after strategic NAND and component purchases"（Q2 FY2027……在进行战略性 NAND 及组件采购之后），与第 26、29 章一致。 | 已修复 |
| 25 | "FY2022 rose 29%… Part of that rise came from Meta"（FY2022 增长 29%……部分增长来自 Meta） | 归因无来源。 | 改为"Meta became the showcase AI customer"（Meta 成为标杆 AI 客户）。 | 已修复 |
| 25 | 指引"Raised from $4.3–4.4B"（由 $4.3–4.4B 上调） | 不完整：指引在 2026 年 2 月为 $4.3–4.4B，5 月为 $4.41–4.51B，8 月为 $5.03–5.07B。 | 现标注为"Initial guide (Feb 2026)"（初始指引，2026 年 2 月）。 | 已修复 |
| 25 | VAST"$30B valuation"（$30B 估值） | 私营公司数字，缺少规定的来源标签。 | 标注为*据 CNBC 报道*。 | 已修复 |
| 25 | DirectFlash 发布日期 [VERIFY] | 已解决：FlashArray//X，2017 年 4 月（新闻稿及 The Register）。 | 已加脚注。 | 已修复 |
| 27 | 要点速览 / 正文："FlashBlade//S holds DGX SuperPOD certification"（FlashBlade//S 拥有 DGX SuperPOD 认证）；仅列 NVIDIA-Certified Storage | 不完整。2025 年 3 月 FlashBlade 还获得了 NCP 高性能存储认证（HGX B200/H200），第 29 章已有此表述。 | 已补充至要点速览和正文。第 27 章与第 29 章现已一致。 | 已修复 |
| 27 | "EXA gained NVIDIA-Certified Storage status in March 2026"（EXA 于 2026 年 3 月获得 NVIDIA-Certified Storage 资格） | 各方报道对其是已授予还是计划中说法不一。 | 改写为"Everpure said NVCS validation extended to EXA"（Everpure 表示 NVCS 验证已扩展至 EXA）。NCP 仍待定。 | 已修复 |
| 27 | 无 EXA GA 日期 | GA 于 2025 年 6 月 Accelerate 大会上宣布（TechRepublic）。 | 已补充并加脚注。 | 已修复 |
| 27 | MLPerf v3.0："VAST, WEKA and DDN did not submit"（VAST、WEKA 和 DDN 未提交） | 正确但不完整。Blocks & Files 还列出 Dell、Huawei、IBM 和 NetApp 缺席。 | 扩大缺席名单并加脚注。 | 已修复 |
| 27 | 检查点核算："roughly trillion-parameter model at ~16 bytes/param"（约万亿参数模型，约 16 字节/参数） | 该负载为 1.25T 参数。16.7 TB ÷ 1.25T ≈ 13 B/param。 | 已更正。 | 已修复 |
| 27 | "PureKVA and always-on DeepReduce arrived in October 2026"（PureKVA 和常开的 DeepReduce 于 2026 年 10 月推出） | 二者于 2026-09-30 发布，且正文写的是 9 月。 | 已修正。 | 已修复 |
| 27 | SPEC 数据节点型号 [VERIFY，提取文本乱码] | 已解决：Supermicro ASG-1115S-NE316R，运行 Purity//DN 1.0，依据 SPEC 文本披露。 | 已写明型号；删除 VERIFY。 | 已修复 |
| 27 | DFM 数据节点 | 仍未确认 GA。使用条款仍描述为第三方服务器。 | 结合该证据细化了 VERIFY。 | 已标记 |
| 27 | "no proprietary client … advantage against WEKA and Lustre"（无专有客户端……相对 WEKA 和 Lustre 的优势） | 片面。VAST 也提出同样的标准客户端论点，而 WEKA/Lustre 客户端以此为代价换取更精细的客户端侧控制。 | 已补充反方观点。 | 已修复 |
| 26 | "245.76 TB for the largest standard drive"（最大标准硬盘为 245.76 TB） | Sandisk 已宣布 1H 2026 推出 256 TB UltraQLC，但出货未经确认。 | 现改为"largest standard SSD confirmed shipping (Sandisk has announced 256 TB)"（已确认出货的最大标准 SSD（Sandisk 已宣布 256 TB））。 | 已修复 |
| 26 / 29 | TrendForce 4Q26：第 26 章写 +23–28% [VERIFY]；第 29 章写 +15–20% | 二者都对，但衡量对象不同：整体 NAND 合约价 +15–20%（TrendForce 新闻稿，2026-09-30），企业级 SSD +23–28%（二手报道）。 | 两章现均列出两个数字，并引用一手新闻稿。VERIFY 已解决。 | 已修复 |
| 26 | "a position no SSD-buying competitor shares"（采购 SSD 的竞争对手都不具备的处境）（指 NAND 敞口） | 具有误导性。竞争对手同样通过 SSD 价格承受 NAND 涨价压力。 | 重新表述：Everpure 需与 IDM 自有的 SSD 业务争夺原始 NAND 配额。 | 已修复 |
| 26 | FlashBlade 2016 年使用原始 NAND [VERIFY] | 已解决：最初的刀片搭载的是 MLC NAND 芯片，而非 SSD（The Register、Computer Weekly）。 | 已加脚注。 | 已修复 |
| 28 | 表 28.2 Everpure 最强版本论证（steelman）："fastest share gains"（份额增长最快） | 无来源的吹捧。 | 已删除。新增弱点"software mostly sold with arrays"（软件主要随阵列捆绑销售）。 | 已修复 |
| 29 | 表 29.2 表注："the only array vendor monetising its flash design inside hyperscalers"（唯一在超大规模云厂商内部将其闪存设计变现的阵列厂商） | 绝对化表述。 | 现改为"only array vendor publicly known to…"（公开所知唯一……的阵列厂商）。 | 已修复 |
| 29 | 新兴 GPU 云（neocloud）要点：CoreWeave 持股 | 缺少反方观点。 | 补充 CoreWeave 后来与 VAST 签订了规模大得多的交易。 | 已修复 |
| 28 / 29 | Evergreen//One +73% 与 TCV $277M 在两章中重复 | 内容重复。 | 仅保留在第 29 章；第 28 章改为交叉链接。 | 已修复 |
| 全部 | 字数预算 | 第 4 部分原为 11,413 字。 | 精简重复内容：Portworx 价格（三处提及）、复述时间线的历史段落、多余的半导体类比、第 29 章中重复的认证和云列表，以及冗长的对话手册回答。 | 已修复 |

## 未解决事项 / 分歧

- **第 26 章：300 TB DFM 状态。** FY26 10-K 中"released in 2025"（2025 年发布）的说法仅来自检索摘要。2025 年 6 月 StorageReview 的一篇文章称 300 TB 模块"expected by end-2025"（预计 2025 年底推出）。未找到 GA 或出货新闻稿。VERIFY 标记保留。
- **第 27 章：FlashBlade//EXA 的 NCP 和 SuperPOD 认证**，按最新公开资料仍待定；基于 DFM 的数据节点也仍未确认 GA。二者都是新兴 GPU 云交易的关键门槛。
- **第 29 章：超大规模业务毛利率。** 分析师估算（75–85%，纯授权费 >90%）在精神上与管理层"较新模式使超大规模毛利率更接近公司平均水平"的表态相冲突。我把 85% 视为上限。真实数字未披露。
- **第 29 章：Q4 FY26 产品毛利率"67.3%, up more than 400 bp on mix"（67.3%，因产品结构提升 400 多个基点）。** 尚未确认是 GAAP 还是非 GAAP，也未确认是否为同比比较。保持原样。
- **第 25 章：CUSIP。** 正文称更名后 CUSIP 不变。这依据的是引用代码变更新闻稿的研究笔记；我未独立核实。
- **体例说明。** 我对五章的脚注都重新编号了。其他编辑这些文件的代理应重新阅读"资料来源"部分，而不要沿用旧的脚注编号。
