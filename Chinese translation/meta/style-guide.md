# 风格指南——Everpure Tech Atlas

> 📄 英文原文：[meta/style-guide.md](../../meta/style-guide.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

## 1. 读者与语气
- 读者：战略 / 企业发展岗位高管，曾从事半导体并购，具备 CFA/MBA/法律背景。聪明、时间紧张，了解芯片和 NAND 基础知识，但对存储系统还比较陌生。
- 语气：一位犀利的资深分析师向这位高管做简报。语言平实，段落简短。使用具体例子和 **算例**（"一个 405B 参数模型的检查点，连同 Adam 优化器状态，大约为 405e9 × 16 bytes ≈ 6.5 TB……"）。
- 不要营销腔，没有数字支撑就不用最高级形容词，不为任何厂商摇旗呐喊—— **包括 Everpure**。对竞争对手要给出其最强版本论证（steelman）。
- 默认深度为 **L2**（机制 + 权衡）。L3 内容只放在"深入阅读"部分。
- 使用 **半导体类比**（"FTL 之于 SSD，相当于内存控制器的地址映射 + 磨损均衡之于 DRAM/NAND……"，"元数据服务器就是文件系统的 tag RAM"）。
- 股票代码：Everpure 自 2026-04-17 起以 **NYSE: P** 交易（此前为 PSTG）。在需要提及股票代码的章节中，首次出现时写作"NYSE: P (formerly PSTG)"。
- 2026 年 2 月及以后的公司称"Everpure"，描述此前历史时称"Pure Storage"（例如"Pure Storage（现 Everpure）于 2015 年上市"）。产品名称沿用官方名称（FlashArray、FlashBlade、Purity、DirectFlash、Evergreen、Portworx、Pure1、Fusion），除非有来源表明已更名。
- 战略内容 = *"基于公开信息、战略团队可能评估的选项"*。绝不臆测未公开的计划。

## 2. 章节模板（强制，标题须与下文完全一致）

```markdown
# <Chapter #>. <Title>
> **Depth:** L2 · **Reading time:** ~X min · **Last verified:** YYYY-MM-DD
> **Prerequisites:** [links]

## TL;DR
- 5 bullets a strategy person must remember.

## Why this matters for Everpure strategy
1–2 paragraphs: the business "so what".

## Core concepts
L2 explanation with analogies, worked numbers, visuals interleaved (not dumped at the end).
Use ### sub-headings freely.

## How Everpure approaches it vs. competitors
Comparison table + trade-off discussion. Steelman the alternatives.

## History and trajectory
How we got here; where it's going (dated, sourced signals).

## Numbers that matter
| Metric | Value | Context | Source / date |

## Conversation playbook
- **3 questions for a PM** + what a strong answer sounds like
- **3 questions for an engineer** + what a strong answer sounds like
- **Don't say this:** misconceptions that would undermine credibility

## Going deeper (optional, L3 pointers)

## Key terms

## Sources
[^1]: Publisher, "Title," publication date. URL (retrieved YYYY-MM-DD).
```

（译注：上方模板代码块保持英文原样，因为 QA 脚本按英文标题检查。各段说明大意：TL;DR——战略人员必须记住的 5 个要点；Why this matters for Everpure strategy——1–2 段，说明商业上的"so what"；Core concepts——L2 讲解，配类比、算例，图表穿插于正文中（不要堆在末尾），可自由使用 ### 子标题；How Everpure approaches it vs. competitors——对比表 + 权衡讨论，给出替代方案的最强版本论证；History and trajectory——如何走到今天、未来走向（附日期和来源的信号）；Numbers that matter——指标 / 数值 / 背景 / 来源与日期表；Conversation playbook——向产品经理提的 3 个问题及高质量回答的样子、向工程师提的 3 个问题及高质量回答的样子，以及"不要这样说"——会损害可信度的误解。中文译本中的模板标题统一译法见 `Chinese translation/meta/translation-guide.md` 第 4 节。）

公司深度剖析章节（第 42–44 章）须在 **"Core concepts"之后、"How Everpure approaches it vs. competitors"之前** 增加：
`## Business model & financials`、`## Customers & go-to-market`、`## Why it gained traction`、`## Risks & open questions`、`## Strategic relevance to Everpure`。

阅读时间 = 正文词数 / 230，四舍五入。

## 3. 来源与脚注
- 每个数字、日期、规格、产品名称相关的说法、客户、融资轮次、估值或市场数据 → 脚注 `[^n]`。
- 脚注定义放在 `## Sources` 下，按首次引用顺序编号，格式如下：
  `[^3]: Everpure, "Form 10-K for fiscal year ended February 1, 2026," 2026-04-01. https://… (retrieved 2026-11-01).`
- 无法核实 → 正文内标注 `[VERIFY: what needs checking]`，并在该章节的暂存清单中加一行（见 §6）。
- 私营公司数据：正文中始终标注 *(company-stated)*、*(reported by Bloomberg)*、*(estimated)*。
- 引语：少于 15 个词，每个来源最多一条，加引号并附脚注。
- 公认的通用工程事实（例如"RAID 5 可容忍一块硬盘故障"）无需脚注。任何有时效性的内容都需要脚注。

## 4. 图表规范
- 目标：每 700 个正文词至少 1 个图表，每章至少 3 个，其中至少 2 个不是表格。
- **优先使用 Mermaid**（` ```mermaid `）。允许的类型：`flowchart`、`sequenceDiagram`、`timeline`、`mindmap`、`quadrantChart`、`block-beta`、`xychart-beta`、`stateDiagram-v2`、`classDiagram`。标签保持简短；含标点的标签加引号：`A["NVMe-oF (TCP)"]`。timeline/mindmap 中避免使用 `<br>`。避免未加引号的括号 / 冒号。每个代码块都必须通过 `bash scripts/lint_mermaid.sh <file>`。
- 每个图表之后（或之前）都要有一句斜体图注，点明要点：`*Figure 16.2 — Stateless compute nodes mean any CNode can serve any request; scaling performance is just adding CNodes.*`
- **图片**（SVG/PNG）：`![Alt text describing the image](../assets/diagrams/ch16-dase-cluster.svg)` + 图注行。替代文本（alt text）必填。
- **SVG 示意图**（手工绘制，`docs/assets/diagrams/chNN-<slug>.svg`）：基于 viewBox，宽度 ≤ 1000，字体 `Inter, Helvetica, Arial, sans-serif`，白色背景矩形，使用下方调色板，所有文字 ≥ 12px。仅限原创绘图。
- **数据图表**：`scripts/charts/chNN_<slug>.py`，对外提供 `build(out_dir: pathlib.Path)`；读取 `data/chNN_<slug>.csv`（必须包含 `source` 和 `as_of` 列）；输出 `docs/assets/charts/chNN-<slug>.svg`（优先 SVG）；使用 `scripts/charts/_style.py`（`apply()`、`PALETTE`、`VENDOR_COLORS`、`save(fig, out_dir, name)`）。在图注下方添加一行数据说明，CSV 路径用行内代码表示（不要用链接，因为 `data/` 位于 MkDocs 的 docs 目录之外）：``Data: `data/chNN_slug.csv` ``。
- **表格**：属于结构化对比（≥ 3 行 × 3 列）时计为图表。

### 调色板（Okabe–Ito，色盲友好）
| 角色 | 色值 |
|---|---|
| 主色 / Everpure | `#0072B2`（蓝） |
| 竞争对手 A | `#E69F00`（橙） |
| 竞争对手 B | `#009E73`（绿） |
| 竞争对手 C | `#CC79A7`（紫粉） |
| 强调 / 高亮 | `#D55E00`（朱红） |
| 次级浅色 | `#56B4E9`（天蓝） |
| 警示 / 注意 | `#F0E442`（黄） |
| 文字 / 中性色 | `#222222`，网格线 `#DDDDDD` |

对比图表中的厂商配色：Everpure `#0072B2`、VAST `#E69F00`、WEKA `#009E73`、DDN `#CC79A7`、Dell `#56B4E9`、NetApp `#D55E00`、HPE `#999999`、其他 `#F0E442`。

## 5. 链接
- 使用相对路径交叉链接：从 `docs/03-system-architecture/16-...md` 链接到 `../01-storage-fundamentals/03-inside-an-ssd.md`。
- 术语表：`../glossary.md`（在 `docs/` 下则为 `glossary.md`）。指向术语表的锚点链接使用字母分节：`../glossary.md#d`。
- 避免使用指向其他章节的锚点链接，模板中的 `##` 标题除外（例如 `#conversation-playbook`）。
- 文件名和路径以 `meta/outline.md` 为准；可以随意链接尚未完成的章节。

## 6. 术语暂存
每章写入 `meta/glossary-staging/chNN.md`，每行一个术语，格式严格如下：
```
- **Term** — one-sentence L1 definition. | NN
```
（NN = 章号。）`scripts/build_glossary.py` 负责合并、去重（以首个定义为准，章节列表合并）并写入 `docs/glossary.md`。

## 7. 待解问题 / VERIFY 暂存
每章把 VERIFY 条目以及值得向 Everpure 人员提出的好问题追加到 `meta/open-questions-staging/chNN.md`：
```
- VERIFY | NN | what needs checking | why it matters
- ASK | NN | audience (PM/Eng/CTO) | question
```

## 8. 字数统计
`scripts/wordcount.py` 只统计正文：不计入围栏代码块 / Mermaid、表格、HTML 标签、图片行、脚注定义以及 `## Sources` 部分。`meta/outline.md` 中的预算均为该统计器口径下的正文词数。目标为预算的 +5–15%。
