# CLAUDE.md — Everpure Tech Atlas（Everpure 技术图谱）

> 📄 英文原文：[CLAUDE.md](../CLAUDE.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

本仓库是 **Everpure Tech Atlas**：一部 ≥100,000 词、以视觉元素为主的存储与 AI 存储知识库。它的读者是一位即将加入 **Everpure**（原 Pure Storage，2026 年 2 月更名；NYSE 股票代码 2026-04-16 之前为 PSTG，自 2026-04-17 起为 **P**——见 `meta/decisions.md` D12）战略与企业发展部门（Strategy & Corporate Development）的企业发展/战略专业人士（CFA、MBA、法律背景、半导体并购经验）。读者了解芯片、NAND 基础知识、数据中心经济学和交易工作，但对存储系统、协议或存储软件并不深入了解。

**目标：** 让读者通过理解*事物如何运作、取舍为何存在、以及它们在战略上意味着什么*，能够与 Everpure 的产品经理、工程负责人以及首席技术官办公室（Office of the CTO）进行可信、高效的对话。

## 深度标签
- **L1 – 词汇：** 能给出定义，并能在句子中正确使用。
- **L2 – 机制：** 能在白板上讲清它如何运作，说出关键取舍，并说明为何某种设计在某类工作负载上优于另一种。**← 默认深度。**
- **L3 – 实现：** 代码路径、盘上格式、内核内部机制。仅出现在简短的"深入阅读"框中。

以半导体类比作为桥梁：存储器层级、HBM/DRAM、NAND 物理、控制器、PCIe、SerDes、互连、芯粒（chiplet）、晶圆代工/供应链、GPU 利用率经济学。

## 执行模式：一次不间断运行
- 在一次运行中构建整部图谱，从空仓库直到满足完成标准（Definition of Done）。不要停下来等待审阅或提问。
- 遇到歧义 → 做出最合理的判断，记录在 `meta/decisions.md` 中，然后继续。
- 无法核实的事实 → 在行内写 `[VERIFY: …]` 并记录到 `meta/open-questions.md`，然后继续。
- 任何上下文压缩之后：重新阅读 `CLAUDE.md` 和 `PROGRESS.md`，然后继续下一个未完成事项。
- 只有在满足完成标准或遇到硬性阻碍时才停止。停止前先把阻碍记录在 `PROGRESS.md` 中。

## 常设规则
1. **准确优先于篇幅。** 绝不编造数字、产品名称、规格、日期、客户、融资轮次、估值或引语。每一项定量或具有时效性的论断都要附行内脚注，注明来源、出版日期和检索日期。若无法核实，写 `[VERIFY: …]` 并记录。
2. **实时研究。** 对于世界的现状（产品、规格、财务、竞争对手、融资、份额、合作、路线图），使用网页搜索/抓取。2025 年中之后的训练数据视为过时。
3. **来源优先级：** (a) 公司一手来源（SEC 文件、财报电话会、投资者演示材料、文档、数据表、白皮书、工程博客）；(b) 标准组织（SNIA、NVM Express、IETF/NFS RFC、CXL Consortium、MLCommons）；(c) NVIDIA 及合作伙伴文档；(d) 学术/行业论文（USENIX FAST/OSDI/SOSP、Hot Chips、FMS）；(e) 信誉良好的行业媒体和分析师。对于私营公司（VAST、WEKA、DDN），数据标注为*公司自述*、*媒体报道*或*估算*。避免 SEO 内容和论坛。
4. **版权。** 只用自己的语言。绝不粘贴厂商文字，也不复制厂商图表；用原创的 Mermaid/SVG 重绘概念。引语少于 15 个词，每个来源最多引用一次。
5. **仅使用公开信息。** 不推测 Everpure 未公开的计划；不涉及任何保密内容。战略部分表述为*"战略团队基于公开信息可能评估的选项"*。
6. **视觉密度：** 约每 700 词 ≥ 1 个视觉元素；每章 ≥ 3 个视觉元素（且其中 ≥ 2 个不是表格）。视觉元素 = Mermaid 图、SVG、生成的图表（PNG/SVG + 数据 CSV），或结构化对比表。
7. **语气：** 犀利的资深分析师向聪明的高管做简报。平实的语言、具体的例子、算例，不要营销腔，不为任何厂商（包括 Everpure）摇旗呐喊。展示取舍；为竞争对手构建最强版本论证（steelman）。
8. **每一章都遵循章节模板**（`meta/style-guide.md`）。没有例外。
9. **一致性：** 使用 `docs/glossary.md` 中的术语；新增术语（通过 `meta/glossary-staging/chNN.md`）；用相对 Markdown 链接交叉引用各章。
10. **持续提交。** 每章一次提交（`docs(ch42): VAST Data deep dive`）；每批完成后推送。每完成一章就更新 `PROGRESS.md`。
11. **重实质，不注水。** 字数预算靠机制、例子、数字、历史和影响来满足——绝不靠重复。
12. **绝不停下来等待审阅。**

## 仓库约定（原因见 `meta/decisions.md`）
- 仓库根目录 = 图谱根目录（仓库名为 `storage-_db_claude`；图谱名为 "everpure-tech-atlas"）。
- 章节：`docs/<NN-part>/<NN>-<slug>.md`。规范清单见 `meta/outline.md`。
- 图片放在 `docs/assets/{diagrams,charts}/` 下，使相对路径在 github.com 和 MkDocs 上都有效。
- 规范术语表：`docs/glossary.md`。根目录的 `glossary.md` 和 `docs/index.md` 由 `scripts/sync_root.py` 生成——不要手工编辑。
- 图表数据：`data/*.csv`（必须包含 `source` 和 `as_of` 列）。每张图表一个模块，位于 `scripts/charts/*.py`；`scripts/make_charts.py` 运行全部模块。
- 脚注：Markdown 脚注 `[^n]`，定义在该章的 `## Sources` 部分。

## QA 命令
```bash
python3 scripts/wordcount.py            # 每章/每部分/总计的字数（仅正文）
bash scripts/lint_mermaid.sh [file...]  # 用 mmdc 渲染每个 Mermaid 代码块
python3 scripts/check_links.py          # 内部链接 + 锚点
python3 scripts/qa_report.py            # 模板、视觉密度、VERIFY 数量
python3 scripts/make_charts.py          # 重新生成图表
python3 scripts/build_glossary.py       # 将术语暂存合并 → docs/glossary.md
python3 scripts/sync_root.py            # 重新生成根目录 glossary.md + docs/index.md
```
