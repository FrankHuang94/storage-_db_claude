# 审阅报告：第 0 部分（第 0.1 章与第 0.2 章）

> 📄 英文原文：[meta/reviews/part0.md](../../../meta/reviews/part0.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

**审阅范围**：`docs/00-start-here/00a-how-to-use-this-atlas.md` 与 `docs/00-start-here/00b-one-page-map.md`，以及二者的 staging 文件。审阅日期 2026-11-01。

## 摘要

**本次审阅为何重要**。第 0 部分最后撰写，所依据的章节文本此后已被第 1–6 部分的审阅者修正。我对照以下三方面做了核查：
- 第 13、14、15、25–29、34、37、40、42、44、45、49 章及第 57–59 章的当前文本；
- `meta/reviews/` 中的每一个文件；
- 8 次网络搜索，覆盖：股票代码、Q2 FY27 业绩、第二家超大规模云厂商、FY25 10-K 中点名 Meta、300 TB DFM 的状态、IDC AI 基础设施存储份额、18.6× SSD/HDD 指数，以及 STX 合作伙伴名单。

**图片**。四张嵌入图片均存在。每张图的替代文本和图注都与图示内容一致（我核对了 SVG 中的文字）：
- `ch13-storage-stack.svg`
- `ch26-directflash-vs-ssd.svg`
- `ch45-four-way-architecture.svg`
- `ch29-arr.svg`

修正了一处替代文本错误：图表中的 RPO 起点是 FY2024 年末，而非 FY2023。

速成课程中提到的每一张图（2.1、13.1、26.2、30.1、32.3、45.1）均存在。每个章节链接均可解析。

**结论**：
- **0.1：轻微至实质性修正**。图谱统计数据已过时：问题数、一句话要点数、闪卡数、术语表条目数和 VERIFY 数，以及字数和阅读时间。两周计划与其自身的"每周两次演练"相矛盾，且第 10 天安排过满。
- **0.2：实质性修正**。这些问题源于沿用了审阅者已修正过的事实：
  - FlashBlade//S 被标为 TLC。
  - MLPerf 缺席厂商名单不完整。
  - 缺少 EXA 的认证状态、GA 日期和第三方数据层信息。
  - 超大规模云厂商模式被描述为仅授权（licence-only）。
  - 业绩指引的历史不完整。
  - 有三处措辞偏向 Everpure。

**修改后的 QA**：
- 0.1：PASS，1,771 词 / 预算 1,500。
- 0.2：PASS，1,993 / 1,500。阅读时间现为约 9 分钟。本章超出预算，原因是新增内容均为限定说明（caveat）。
- Mermaid OK。0 个失效链接。
- 0.2 的脚注已按首次引用顺序重新编号。新增五个来源：EXA GA、MLPerf 缺席名单、NVCS 状态、FY25 10-K、partitioned-writer 博客，以及 Sandisk 256 TB。

## 发现的问题

| 章 | 原文主张 / 段落 | 问题 | 已采取的修正 | 状态 |
|---|---|---|---|---|
| 0.2 | §5 "Both forked by media: TLC for performance (FlashArray//X and //XL, FlashBlade//S)"（"二者都按介质分叉：性能型用 TLC（FlashArray//X 和 //XL、FlashBlade//S）"）；图 0.2.6 图注 | **错误**。第 27 章表 27.1 列出 FlashBlade//S 使用 QLC DFM。FlashBlade 按配置而非介质划分 | 已修正正文、图示标签和图注。补充说明 FlashBlade//S 属于 "partitioned-writer"（分区写入者）设计，而非全共享架构（见第 15 章 / 第 3a 部分的发现），并附来源 | 已修复 |
| 0.2 | 要点速览、§6、数字表、对话手册：MLPerf v3.0 "a round VAST, WEKA and DDN skipped"（"VAST、WEKA 和 DDN 缺席的一轮"） | 不完整。Dell、IBM 和 NetApp 同样缺席（第 27 章，B&F） | 各处均扩充了缺席名单；新增 B&F 脚注 | 已修复 |
| 0.2 | §6 "NVIDIA's SuperPOD certification belongs to FlashBlade//S"（"NVIDIA 的 SuperPOD 认证属于 FlashBlade//S"） | 不完整。遗漏了 2026 年 3 月将 NVCS 验证扩展至 EXA 一事，而 EXA 尚无已完成的认证或名单条目（采用第 6b 部分的统一措辞） | 用统一措辞和脚注补充一句。新增"不要这样说"条目："EXA is NVIDIA-certified"（"EXA 已获 NVIDIA 认证"） | 已修复 |
| 0.2 | §5 "EXA, announced March 2025, adds off-the-shelf data nodes"（"2025 年 3 月发布的 EXA 增加了现成的数据节点"）；时间线 "EXA announced"（"EXA 发布"） | 缺少 GA 日期（2025 年 6 月） | 补充 GA，附 TechRepublic 脚注。时间线改为 "announced and GA"（"发布并 GA"） | 已修复 |
| 0.2 | §6 "EXA keeps metadata on a Purity core…"（"EXA 将元数据保存在 Purity 核心上……"） | 未说明数据层是第三方 Linux/NVMe 而非 DirectFlash。MLPerf 一行写的是 "30 data nodes"（"30 个数据节点"），没有注明"第三方" | 两处均已明确 | 已修复 |
| 0.2 | 图 0.2.7 图注 "All four split metadata from data"（"四者都将元数据与数据分离"） | 对 WEKA 不准确，WEKA 没有元数据服务器。也遗漏了 VAST 额外的一跳（第 45 章图 45.1） | 图注按第 45 章重写 | 已修复 |
| 0.2 | 要点速览 "AI position is strong on evidence, thin on references"（"AI 地位证据充分、参考客户偏少"） | 偏向 Everpure。所谓"证据"只是多数对手缺席的一轮基准测试 | 改为 "Rests on one benchmark lead, with thin references and no completed EXA certification"（"依托一次基准测试领先，参考客户偏少，EXA 认证尚未完成"） | 已修复 |
| 0.2 | §3 "300 TB DFMs against 245.76 TB for the largest shipping standard SSD"（"300 TB DFM 对比已出货最大标准 SSD 的 245.76 TB"） | 遗漏了状态和比较方面的限定说明（第 26 章）：300 TB 依据的是经搜索摘要看到的 FY26 10-K，且 Sandisk 已发布 256 TB | DFM 状态以 10-K 和 B&F 为来源。注明 Sandisk 256 TB。功耗主张标注为厂商主张。数字行注明 "Everpure-stated"（Everpure 自述） | 已修复 |
| 0.2 | §4 "acknowledged in mirrored NVRAM"（"在镜像 NVRAM 中确认"）；图 0.2.5 "Mirrored NVRAM"（"镜像 NVRAM"） | 第 14 章（第 3a 部分）指出 FlashArray 的 NVRAM 位于机箱内、双归属或位于 DFMD 上，而非按控制器镜像 | 改用中性措辞："NVRAM that survives a controller failure"（"可在控制器故障后保留数据的 NVRAM"） | 已修复（见"未解决事项"：第 26 章仍写作 "mirrored"） |
| 0.2 | §4 "The same key-value metadata engine underpins Purity//FA and Purity//FB"（"同一个键值元数据引擎支撑 Purity//FA 和 Purity//FB"） | 夸大了第 26 章的说法，后者称 Purity//FB "spreads the same ideas"（"沿用了相同的思路"） | 与第 26 章保持一致 | 已修复 |
| 0.2 | §8–9、"不要这样说"：超大规模云厂商 "license the design"（"授权使用该设计"）；Everpure "paid for IP, software and support"（"按 IP、软件和支持收费"） | 不完整。在 2026 年 2 月标准化后的模式下，Everpure 还供应部分非 NAND 部件（第 29 章，第 4 部分） | 在正文、图 0.2.10 和"不要这样说"中补充 "plus parts"（"外加部件"） | 已修复 |
| 0.2 | 数字表：指引 "Raised from US$4.3–4.4B in Feb 2026"（"由 2026 年 2 月的 US$4.3–4.4B 上调"） | 不完整：指引在 5 月（4.41–4.51）和 8 月两次上调（第 4 部分） | 改为 "Initial guide… raised in May and again in August"（"初始指引……5 月上调、8 月再次上调"） | 已修复 |
| 0.2 | 数字表：超大规模 "First customer, Meta"（"首个客户：Meta"） | Meta 在 FY25 10-K 中被点名（第 4 部分）；该行需要这一来源 | 新增 FY25 10-K 脚注；第二个设计导入标注为未具名，收入自 FY28 起（经搜索确认） | 已修复 |
| 0.2 | §8 非 GAAP 利润率 | 已标注非 GAAP。需要加入第 4 部分"cushions, doesn't protect"（"起缓冲作用，但不能提供保护"）的框架 | 补充一个分句 | 已修复 |
| 0.2 | 图 0.2.9 替代文本 "RPO rising from 2.3 billion to 4.1 billion over the same period"（"同期 RPO 从 23 亿升至 41 亿"） | CSV 显示 RPO 起点为 FY2024 年末，而非 FY2023 | 已修正 | 已修复 |
| 0.2 | 图 0.2.9 "ARR has compounded at about 21% a year"（"ARR 年复合增长约 21%"） | 正确（约 3.5 年内 1.10 → 2.13 ≈ 20.8%）。但掩盖了 FY26 放缓至 16%，以及以 ARR 换 RPO 的权衡（第 29 章） | 图注补充 16% / 20% 以及 "partly at the expense of ARR growth"（"部分以牺牲 ARR 增长为代价"） | 已修复 |
| 0.2 | §7 "Switching costs are moving into the control plane: Fusion passed 1,200 customers"（"转换成本正在转移到控制平面：Fusion 客户数突破 1,200"） | 存在倾向性。第 28 章指出这不到客户基数的十分之一 | 改写为 Everpure 的押注，并附采用率方面的限定说明 | 已修复 |
| 0.2 | §9 "Everpure is a co-design partner on its BlueField-4 STX"（"Everpure 是其 BlueField-4 STX 的联合设计伙伴"） | 属实但带有美化。NVIDIA 列出 12 家存储联合设计伙伴，包括 VAST、WEKA、DDN、Dell 和 NetApp（经搜索确认） | 改为 "One of twelve…, alongside…"（"十二家之一……与……并列"） | 已修复 |
| 0.2 | §10 "Everpure is the clearest integrated media moat"（"Everpure 拥有最清晰的一体化介质护城河"） | 以事实口吻表述判断 | 改为 "Sits furthest into the integrated-media corner; other placements are more contestable"（"在一体化介质象限中位置最靠外；其他厂商的定位更具争议"）。象限数值与第 49 章矩阵 2 一致 | 已修复 |
| 0.2 | 表 0.2.1 Dell/NetApp "New retrofits (Lightning, AFX)"（"新的改装产品（Lightning、AFX）"） | 略带贬低。第 46 章说它们构建的是新系统 | 改为 "New first-generation AI systems (Lightning FS, AFX)"（"新的第一代 AI 系统（Lightning FS、AFX）"） | 已修复 |
| 0.2 | 数字表：SSD ÷ HDD 约 18.6× | 这是单一厂商（VDURA）针对 30 TB TLC 的指数，2026 年 8 月；第 2/48 章给出 18.6–22.6×。缺少日期 | 补充背景和日期（2026-08-21） | 已修复 |
| 0.2 | VAST 一行 "Company-stated ARR; the AI-native benchmark"（"公司自述 ARR；AI 原生的标杆"） | 估值属媒体报道（CNBC） | 两种标签均已注明 | 已修复 |
| 0.2 | 股票代码自 2026-04-17 起为 P；Q2 FY27 ARR/RPO/指引；IDC 2.4%；IDC 8.1% / Dell 23.8%；FY26 收入 $3.66B；第二家超大规模云厂商 2026-08-10 | 已对照章节和搜索核查 | 无需修改 | 已核实 |
| 0.1 | 数字表：154 个问题、64 条一句话要点、200 张闪卡、≈790 个术语、>130k 词 / ≈10 小时、≈200 个 VERIFY | 已过时。实际为：150 个问题（第 57 章题库）、66 条一句话要点、279 张卡片（Q1–Q279）、870 个术语、156,308 个正文词（≈11 小时）、177 个行内 VERIFY | 全部更正；重新计算阅读时间 | 已修复 |
| 0.1 | 图 0.1.1 "Day 2: Parts 5 to 8"（"第 2 天：第 5 至第 8 部分"）；"Every chapter in order"（"按顺序读完每一章"） | 速成路线只覆盖第 5–6 部分的核心内容加第 53–57 章。精通计划表也并非严格按顺序（第 51–52 章在第 5 天，第 55 章在第 6 天） | 标签已修正 | 已修复 |
| 0.1 | 精通计划："two whiteboard rehearsals a week"（"每周两次白板演练"，见图示和 README）与表中仅有两次演练 | 内部矛盾 | 将演练 1–4 分别安排在第 3、4、7 和 8 天 | 已修复 |
| 0.1 | 第 10 天：第 46–50、53–54、57、60 章，加上 "full 200-card pass"（"完整过一遍 200 张卡"），再加一场模拟会议 | 不现实。按 1.5× 计约 2.4 小时阅读，加上过一遍 279 张卡，远超 4 小时 | 第 57 章移至第 8 天（其产出在当天使用）。完整过卡改为第 59 章自带的 50 张卡计时测试。补充说明第 9–10 天耗时最长 | 已修复 |
| 0.1 | 两天速成 "About seven hours a day"（"每天约七小时"） | 按页首时间 1.5× 重新计算：第 1 天 ≈ 6 小时，第 2 天 ≈ 4.5–5 小时 | 改为 "About six hours on day 1 and five on day 2"（"第 1 天约六小时，第 2 天约五小时"） | 已修复 |
| 0.1 | 两小时速成课程：35 分钟读 12 篇要点速览，40 分钟看六张图 | 可行（每篇要点速览加"对 Everpure 战略的意义"约 3 分钟；每张图约 7 分钟）。所有目标均存在 | 无 | 已核实 |
| 0.1 | "Signature (★) diagrams"（"标志性（★）图示"） | ★ 只出现在 `meta/outline.md` 中（以及第 14 章的一个标题），读者在章节中找不到 | 注明 ★ 所在位置 | 已修复 |
| 0.1 | "不要这样说"："We're #1 in MLPerf… VAST, WEKA and DDN skipped"（"我们在 MLPerf 排名第一……VAST、WEKA 和 DDN 缺席"） | 名单不完整 | 已扩充；新增第 27 章链接 | 已修复 |
| 0.1 | 标签表示例（ARR $2.13B、VAST >$500M CARR、DDN ~$500M Forbes、IDC 8.1%） | 与第 29、42、44、40 章一致 | 无 | 已核实 |
| 0.1 | 语气 | 中立。表 0.1.5 对 Everpure 采用同样的证据标准 | 无 | 已核实 |

## 需要修改的 README 内容（按任务要求未直接编辑）

1. **"Start here"（从这里开始）表，两天路线**："Parts 1–4 on day 1, Parts 5–6 on day 2"（"第 1 天第 1–4 部分，第 2 天第 5–6 部分"）→ "the core of Parts 1–4 on day 1; the core of Parts 5–6 plus Ch 53–57 on day 2"（"第 1 天第 1–4 部分的核心内容；第 2 天第 5–6 部分的核心内容加第 53–57 章"）。两天都没有覆盖完整的部分：第 1 天跳过第 10、12 章和第 18–22 章，第 2 天跳过第 33、36、38、39、47、48 和 50 章。
2. **"Learning paths at a glance"（学习路径一览），两天那一行**："plus Ch 53–54"（"加第 53–54 章"）→ "plus Ch 53–57"（"加第 53–57 章"）。
3. **两小时速成课程那一行**：README 列出 9 篇要点速览。0.1 列出 12 篇（新增第 3、25 和 29 章），外加六张图和第 56 章的可信度阶梯。应使 README 与 0.1 一致，或写 "see 0.1 for the full list"（"完整清单见 0.1"）。
4. **两周那一行**："every chapter in order"（"按顺序读完每一章"）→ "every chapter"（"读完每一章"）（0.1 将第 51–52 章和第 55–57 章穿插安排）。"Two whiteboard rehearsals per week"（"每周两次白板演练"）现已与 0.1 一致。
5. **从这里开始表与第 8 部分那一行**："200 flashcards"（"200 张闪卡"）→ 279。"60 one-liners"（"60 条一句话要点"）→ 66。150 个问题的计数是正确的。第 59 章自身标题仍写着 "200 flashcards"（见"未解决事项"）。
6. **进度表**（`<!-- README-TABLE -->`）已过时。表中显示第 0 部分 0/2、第 7 部分 3/4、第 8 部分 4/6，总计 136,818。`wordcount.py` 现在给出 156,308 词，且每个部分都已完成初稿。需重新生成。

## 未解决事项 / 分歧

- **第 26 章与第 14 章：FlashArray NVRAM**。第 26 章（正文和图 26.1）写的是 "NVRAM mirrored across both controllers"（"NVRAM 在两个控制器之间镜像"）。第 14 章（第 3a 部分）称其位于机箱内且双归属（//m），或位于 DFMD 模块上（//XL）。二者之一需要修改。0.2 现采用中性措辞。
- **第 27 章图 27.1 图注**称两个产品家族都分叉为 TLC 性能层和 QLC 容量层。第 27 章自身的表 27.1 列出 FlashBlade//S 使用 QLC DFM。该图注应由第 27 章负责人修正。
- **第 29 章第 59 行**仍写着 "Analysts identified the customer as Meta"（"分析师认定该客户为 Meta"），而第 29 章的要点速览（经第 4 部分审阅后）称 Meta 已在 FY25 10-K 中被点名。另请注意，2026 年 8 月的一份搜索摘要称 "Everpure has not confirmed"（"Everpure 尚未确认"）Meta。10-K 点名一事依据的是对该文件的搜索摘要。
- **第 59 章标题和大纲**写的是 200 张闪卡，但卡组实际有 279 张。
- **300 TB DFM**。"Released in 2025"（"2025 年发布"）仍仅依据 FY26 10-K 的一份搜索摘要。未找到 GA 或出货公告。第 26 章的 VERIFY 保留。
- **ARR 精度**。Q2 FY27 新闻稿的搜索摘要四舍五入为 "$2.1B"。图谱中的 $2.13B 来自图表 CSV 的注释。
- **第 4 部分的一个待解事项已解决**。股票代码变更新闻稿（Nasdaq/PR Newswire，2026-04-07）确认 CUSIP 不变，与第 25 章所述一致。
- **`meta/open-questions.md`** 仍报告 200 个 VERIFY 标记。实际行内共有 177 个。需重新运行 `scripts/build_meta.py`。
