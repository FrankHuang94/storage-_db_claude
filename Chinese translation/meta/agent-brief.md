# 章节撰写者说明（动笔前请完整阅读）

> 📄 英文原文：[meta/agent-brief.md](../../meta/agent-brief.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

你负责起草 **Everpure Tech Atlas** 的一个或多个章节。这是一部战略层面的存储与 AI 存储知识库，仓库位于 `/home/user/storage-_db_claude`。今天是 **2026-11-01**。你的训练数据在 2025 年中之后即已过时。

## 1. 先读（按此顺序）
1. `CLAUDE.md`——读者画像、常设规则（准确性、来源、版权、语气、图表）。
2. `meta/style-guide.md`—— **强制使用的章节模板**、脚注格式、图表规范、调色板、暂存文件格式。
3. `meta/chapter-scopes.md`——你所负责章节的委托范围（列出的内容全部要覆盖），以及相邻章节的范围（避免重复——改用交叉链接）。
4. `meta/outline.md`——每一章的文件路径（用于交叉链接）和计划图表。你所负责章节的那一行列出了必需的图表；★ = 必须交付的标志性图表。
5. `meta/research/*.md`——前期研究汇总形成的已核实事实库（Everpure、VAST/WEKA/DDN、生态）。复用其中的事实 **及其来源**（引用原始 URL，而不是笔记文件）。这些文件很长：用 grep / 略读找出你的章节所需内容。
6. 如果 `docs/03-system-architecture/16-disaggregated-shared-everything.md` 已存在，它就是 **质量标杆范例**：在深度、密度、语气和结构上向它看齐。略读一遍。

## 2. 研究
- 对 `meta/research/` 中尚未涵盖的、任何有时效性或涉及数字的内容，自行开展有针对性的实时研究（通常每章 6–15 次 WebSearch/WebFetch 调用）。一手来源优先（财报文件、官方文档、标准组织、论文），其次是信誉良好的行业媒体。绝不引用笔记文件；引用其背后的原始来源。
- 网络说明：这里有许多主机拒绝 WebFetch（sec.gov、purestorage.com、everpuredata.com、blocksandfiles.com、nextplatform.com、mlcommons.org、cnbc.com……）；WebSearch 可用，能检索到这些站点的 URL 和关键事实。不要反复重试被拒绝的主机而浪费调用次数。改为尝试一手来源或其他信誉良好的媒体。若一个关键数字只出现在搜索结果摘要中（而非已抓取的页面上），则须同时加脚注 **和** `[VERIFY: search-summary only]`，除非有第二个来源佐证。
- 绝不编造数字、产品名称、日期、客户、融资、估值或引语。无法核实时：正文中标注 `[VERIFY: …]`，并在暂存文件中加一行 VERIFY（见下文）。
- 公认的工程事实和你自己的算例无需脚注（要列出计算过程，以便核查）。任何厂商相关、有时效性或与市场相关的内容都需要脚注。

## 3. 写什么
- **章节文件**：放在 `meta/outline.md` 中指定的确切路径，模板标题须 *完全一致*（QA 会检查）：`# N. Title`、页首信息块（`> **Depth:** L2 · **Reading time:** ~X min · **Last verified:** 2026-11-01` 和 `> **Prerequisites:** …`），然后依次是 `## TL;DR`、`## Why this matters for Everpure strategy`、`## Core concepts`、`## How Everpure approaches it vs. competitors`、`## History and trajectory`、`## Numbers that matter`、`## Conversation playbook`、`## Going deeper (optional, L3 pointers)`、`## Key terms`、`## Sources`。（第 42–44 章另加五个深度剖析部分——见风格指南。）
- **字数预算**：达到 `meta/chapters.yml` 中章节预算的 **+5–15%**，以 `python3 scripts/wordcount.py <file>` 的统计结果为准（只计正文：代码、Mermaid、表格、脚注定义和 Sources 部分均不计入）。大部分字数应放在 *Core concepts* 中。只写实质内容——机制、算例、例子、历史、影响。不重复，不注水。
- **图表**：每章 ≥ max(3, 词数/700) 个，其中 ≥ 2 个不是表格，穿插在正文中；每个图表都要有替代文本（图片）和一句斜体要点图注 `*Figure N.k — …*`。交付你的章节所列的每一个 ★ 图表。优先用 Mermaid；Mermaid 画不好的内容用手工绘制的 SVG（`docs/assets/diagrams/chNN-<slug>.svg`，图片链接 `../assets/diagrams/chNN-<slug>.svg`）；数据图表通过 `scripts/charts/chNN_<slug>.py` + `data/chNN_<slug>.csv` 生成（CSV 必须包含 `source` 和 `as_of` 列；图表模块对外提供 `build(out_dir)` 并使用 `scripts/charts/_style.py`；输出 `docs/assets/charts/chNN-<slug>.svg`；链接 `../assets/charts/chNN-<slug>.svg`）。可参考任何现有的 `scripts/charts/ch*.py` 了解写法。只把 **有来源或明确标注为示意** 的数据做成图表（示意性 / 算例图表须在标题中注明）。
- **半导体类比**：读者曾从事半导体并购。在确实有助于理解时，类比内存层级、HBM/DRAM、NAND 物理、控制器、PCIe/SerDes、芯粒（chiplet）、晶圆代工格局、GPU 利用率经济学。
- **Everpure 的定位表述**：坦诚，不做宣传。对竞争对手给出其最强版本论证（steelman）。战略内容 = "基于公开信息、战略团队可能评估的选项"。2026 年 2 月及以后的公司称"Everpure"，此前历史称"Pure Storage"。
- **交叉链接**：从你的文件出发，用相对路径链接相关章节（例如 `../01-storage-fundamentals/03-inside-an-ssd.md`），术语表链接为 `../glossary.md`。链接到尚未写完的章节没有问题。
- **对话手册**：3 个向产品经理提的问题 + 高质量回答要点，3 个向工程师提的问题 + 高质量回答要点，以及一份"**Don't say this:**"误解清单——要切实有用、具体。
- **关键数字**：一张 `| Metric | Value | Context | Source / date |` 表格，≥ 5 行，每一行都有来源（脚注）或标注为算例。

## 4. 暂存文件（同样必需）
- `meta/glossary-staging/chNN.md`——本章引入的每个术语（目标每章 8–20 个），每行一个，格式严格如下：
  `- **Term** — one-sentence L1 definition. | NN`
- `meta/open-questions-staging/chNN.md`——每个 `[VERIFY]` 对应一行 `- VERIFY | NN | item | why it matters`，另加 3–6 行 `- ASK | NN | PM/Eng/CTO | a sharp question worth asking Everpure people`（一个值得向 Everpure 人员提出的犀利问题）。
（NN = 章号，不要求两位数：使用 chapters.yml 中的编号，例如 `16`。）

## 5. 完成前必须运行并通过的 QA
```bash
cd /home/user/storage-_db_claude
python3 scripts/wordcount.py docs/<part>/<file>.md
bash scripts/lint_mermaid.sh docs/<part>/<file>.md      # must end "OK"; fix every FAIL
python3 scripts/make_charts.py chNN                     # if you added charts
python3 scripts/qa_report.py --chapter NN               # must say PASS
python3 scripts/check_links.py --allow-planned docs/<part>/<file>.md   # 0 broken
```
（注释含义：lint 必须以 "OK" 结束，修复每一个 FAIL；make_charts 仅在新增图表时运行；qa_report 必须显示 PASS；check_links 必须 0 个失效链接。）

Mermaid 常见陷阱：含标点的节点标签要加引号 `A["NVMe-oF (TCP)"]`；flowchart 标签中不要出现未加引号的括号；在 `timeline` 和 `mindmap` 的条目中避免冒号 / 括号；`quadrantChart` 的点要求 x、y 位于 [0,1] 区间且名称简单；`sequenceDiagram` 的消息中避免分号和 `#`；`xychart-beta` 中含空格的分类标签必须加引号。保持图表易读（不超过约 15 个节点）。

## 6. 工作规则
- **不要** 运行 git（不要 add/commit/push）。由主代理负责提交。
- **不要** 编辑你的章节、你自己的 SVG / 图表 / CSV 文件以及你自己的暂存文件以外的任何文件。绝不编辑 `docs/glossary.md`、`PROGRESS.md`、`README.md`、`mkdocs.yml`、其他章节或共享脚本（如果共享脚本有 bug，自行绕开并在回复中说明）。
- 版权：只用自己的语言；绝不粘贴厂商文字或复制厂商图表；引语少于 15 个词，每个来源 ≤ 1 条。
- **最终回复（≤ 120 词）**：每章列出：路径、正文词数、图表数（M/I/T）、VERIFY 数量、QA 状态；外加任何值得记入 `meta/decisions.md` 的判断（每条一行）。除此之外不写其他内容——回复中不要包含章节正文。
