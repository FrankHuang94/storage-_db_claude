# 审校报告：第 8 部分（第 55–60 章，对话工具包）

> 📄 英文原文：[meta/reviews/part8.md](../../../meta/reviews/part8.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

**审校范围：** `docs/08-conversation-toolkit/55-talking-with-pms.md` 至 `60-cheat-sheets.md`、第 60 章的三张 SVG 海报（`ch60-protocol-poster.svg`、`ch60-architecture-poster.svg`、`ch60-product-lineup.svg`）以及 `meta/open-questions-staging/ch60.md`。审校日期 2026-11-01。

## 摘要

第 8 部分是综合性内容。这些章节是根据当时的章节草稿写成的，而这些草稿此后已被第 2 阶段审校人修正，因此本次审校主要是一次一致性检查。无需新的网络研究。

**方法：**
- 我阅读了第 2 阶段的每一份审校文件（`part1`、`part2`、`part3a`、`part3b`、`part4`、`part5a`、`part5b`；当时尚无 `part6a`/`part6b`/`part7` 文件），列出每一项被修改的事实，并在第 8 部分中用 grep 检索。
- 我完整阅读了全部六章：全部 **279 张闪卡**、全部 **66 条一句话要点**、全部 **150 个问题和 41 条 "Listen for"（注意倾听）提示**、含 104 个条目的缩略语表，以及三张 SVG 的全部文字。
- 对每张卡片，我把答案与其所链接章节的要点速览或关键数字表中的修正后措辞进行比对。另有一个脚本将全部 279 张卡片答案和全部 66 条一句话要点中的每个数字标记与所链接章节的文本比对，每个标记都能在章节中找到。因此问题不在于数字偏移，而在于审校人此后已加以限定的措辞。
- 我用无头 Chromium 渲染了我编辑过的两张 SVG，确认没有文字溢出。

**结论：**

| 章 | 结论 | 主要原因 |
|---|---|---|
| 55 | 轻微修正 | 把 PureKVA "GA" 当作事实陈述；EXA 认证状态过时；针对竞争对手产品经理的反问需要加上"仅限公开信息"的约束 |
| 56 | 轻微修正 | FlashArray 写路径被描述为 "mirrored NVRAM"（镜像 NVRAM）；MLPerf 被称为 "audited"（经审计）（三次）；300 TB DFM 的发布被陈述时未附搜索摘要的限定说明；"probe in person"（当面探询）一栏 |
| 57 | 轻微修正 | 一条 Listen-for 提示中的 NVRAM 措辞；Q107 询问了未公开的认证日期；要点速览中的计数（40 对 41） |
| 58 | 轻微修正 | 新兴 GPU 云 "storage ~1% of capex"（存储约占资本开支 1%）；$/s 区间；"NAND stockpiling"（NAND 囤货）；指引 "raised from"（自……上调）；MLPerf 一行缺少读取数字 |
| 59 | 轻微至实质性修正 | 16 张卡片或段落仍沿用审校前的措辞：HBM/内存延迟、"halves"（减半）裕量、GPU 槽位的出路、"~1% of capex"、未经确认的 NVCS Enterprise 约 1,000 计数、"audited"、"only array vendor"（唯一的阵列厂商）、KV 缓存规模限定说明等 |
| 60 | 轻微修正 | Purity//DN 被描述为 Purity 数据路径操作系统的一部分；双控制器海报只显示了镜像 NVRAM；//S 认证信息不完整；缺少 //XL 有效容量的计算口径 |

**本次审校之前即已一致的内容：** FlashBlade//S 为 partitioned-writer（分区写入者），EXA 为元数据/数据分离而非 DASE（第 59 章 Q88–Q92、Q142、Q231；第 60 章要点速览、表格和海报）。以下内容同样一致：FY25 10-K 中点名 Meta、66.2% / 74.9% 标注为非 GAAP、Evergreen//One 的 25% 缓冲、DFM 被描述为 "no drive-level FTL"（没有盘级 FTL）（而非 "the only vendor-owned module"，即"唯一的厂商自有模块"）、NYSE: P（原 PSTG）、第 59 章中 EXA 的 NCP 待定状态（Q144）、产品阵容 SVG 中 PureKVA 标为 "announced"（已宣布），以及 Q143 中 MLPerf 缺席厂商名单。CXL 4.0 带宽、第 31 章的恢复算术以及第 35 章 NCP 八周规则在第 8 部分中均未出现。

**修改后的 QA：** 第 55–60 章均通过 `qa_report.py`。`lint_mermaid.sh` 结果为 OK（13 个代码块）。`check_links.py --allow-planned` 报告 0 个失效链接。字数不变或略有增加；每章均达到或高于预算。第 59 章的阅读时间由约 53 分钟增至约 54 分钟。两张编辑过的 SVG 均可作为 XML 解析，渲染时无溢出。

## 发现的问题

| 章 | 主张 / 段落 | 问题 | 已采取的修正 | 状态 |
|---|---|---|---|---|
| 59 | Q7：内存–存储墙 "DRAM-class memory (~100–300 ns)"（DRAM 级内存，约 100–300 ns） | 第 1 部分已将第 2 章更正为 100–400 ns；HBM 距 GPU 约 350 ns | 现改为 "memory tiers (~100–400 ns; HBM is ~350 ns from the GPU, a bandwidth tier…)"（内存层级（约 100–400 ns；HBM 距 GPU 约 350 ns，属于带宽层……）） | 已修复 |
| 59 | Q9："Each extra bit per cell halves the voltage margin"（每单元每多一个比特，电压裕量减半） | 第 2 章现写作 "roughly halves"（大致减半）（间隔数为 1→3→7→15） | 改为 "roughly halves" | 已修复 |
| 59 | Q24：TCO "~3.2× hybrid disk"（约为混合磁盘的 3.2 倍） | 第 4 章要点速览现补充：计入 2026 年磁盘涨价后约为 2.7× | 增加敏感性说明 | 已修复 |
| 59 | Q33：分散式重建 "over 100 drives cuts that to ~1.4 hours"（分布在 100 块盘上可缩短至约 1.4 小时） | 第 1 部分重新设定了模型（k× 读放大）：每块盘约 4 GB/s 读取，8+2 → 约 50 GB/s 输出 | 在卡片中写明假设 | 已修复 |
| 59 | Q38：块协议 "two layers"（两层） | 第 2 部分已将第 7 章改为 "command set riding a transport (plus fabric services)"（命令集承载于传输层之上（外加 fabric 服务）） | 增加 fabric 服务 | 已修复 |
| 59 / 58 | Q64 与一句话要点 30："US$2–6 per H100-hour → US$0.57–1.75 a second"（每 H100 小时 US$2–6 → 每秒 US$0.57–1.75） | $1.75/s 对应 $6.16/h（第 2 部分修正） | Q64 改为 "US$2.00–6.16"；一句话要点 30 在 $2–6 下改为 "~$0.6–1.7 a second"（每秒约 $0.6–1.7） | 已修复 |
| 59 | Q181：NVCS "Enterprise (about 1,000)"（Enterprise 级（约 1,000）） | 第 5a 部分：约 1,000 的数字未经确认（第 34 章中为 VERIFY） | 改为 "a figure not yet confirmed"（该数字尚未确认） | 已修复 |
| 59 / 58 | Q188、一句话要点 40："Storage is roughly 1% of a neocloud's capex"（存储约占新兴 GPU 云资本开支的 1%） | 第 5b 部分：这是把单一合同泛化；第 35 章现写作 "the largest disclosed storage contract is about 1% a year of its customer's capex"（已披露的最大存储合同每年约占其客户资本开支的 1%） | 两处均改为第 35 章的措辞 | 已修复 |
| 59 | Q198："VAST, WEKA and DDN skipped the September 2026 round"（VAST、WEKA 和 DDN 未参加 2026 年 9 月一轮） | 正确但不完整。第 5a 部分：DDN 和 WEKA 参加过更早的轮次；只有 VAST 从未参加 | 增加相应分句 | 已修复 |
| 59 | Q201 与 Q274："flash wins when freed watts become GPUs"（当节省下来的功耗变成 GPU 时，闪存胜出） | **偏向闪存的夸大表述**，第 5b 部分已从第 38 章删除：节省的功耗有帮助，但很少能单独弥合溢价。$8–37M 的溢价基于第 4 章的输入，按指数价格计算还会更大 | 两张卡片均改为遵循第 38 章要点速览：每 TB 带宽或超大规模云厂商的 NAND 成本；功耗换 GPU "rarely closes the gap on its own"（很少能单独弥合差距） | 已修复 |
| 59 | Q143：EXA 的 MLPerf 结果 | 缺少检查点读取数字（588 GiB/s，低于 877.5 的写入；第 5b 部分）以及 KV 缓存规模限定说明（51 台主机；第 5a 和 5b 部分） | 两者均已补充 | 已修复 |
| 59 | Q232 与对话手册 Q2："EXA: audited throughput"（EXA：经审计的吞吐量） | MLPerf 结果由厂商提交并经同行评审，而非经审计（第 5a 部分，第 34 章修正） | 改为 "published, peer-reviewed benchmark throughput"（已发布、经同行评审的基准测试吞吐量） | 已修复 |
| 59 | Q246："the only array vendor selling that IP into hyperscalers"（唯一向超大规模云厂商销售该 IP 的阵列厂商） | 第 4 部分 / 第 5b 部分已在第 29 章和第 36 章中把同一说法弱化为 "publicly known"（公开已知的） | 改为 "only array vendor publicly known to sell…"（公开已知唯一销售……的阵列厂商） | 已修复 |
| 59 | 工程师对话手册 Q1："passes through NVRAM acknowledgement"（经过 NVRAM 确认） | 一致但含糊；FlashArray 将数据持久化到机箱共享 NVRAM（第 3a 部分） | 改为 "acknowledgement in shared chassis NVRAM"（在机箱共享 NVRAM 中确认） | 已修复 |
| 59 | 关键数字表："Ch 54 pending"（第 54 章待定） | 第 54 章现已存在 | 改写为：第 54 章尚无卡片 | 已修复 |
| 59 | 全部 279 张卡片 | 每个答案中的每个数字标记都出现在其链接章节中（脚本检查）。我对照审校文件人工检查了全部卡片，并对照章节文本对约 70 张做了上下文检查（Q1–Q37、Q64–Q74、Q79、Q88–Q92、Q128–Q157、Q163–Q207、Q221–Q246、Q251、Q256–Q279） | 除上述各行外无 | 已核实 |
| 55 | "PureKVA's GA and its 'up to 20×'… date from September–October 2026"（PureKVA 的 GA 及其"最高 20 倍"……可追溯至 2026 年 9–10 月） | 第 4 部分和第 5a 部分：PureKVA 于 2026-09-30 宣布、计划 10 月上市，GA 未经确认 | 改写为 "announced… for October availability; GA not confirmed publicly"（已宣布……10 月上市；GA 未经公开确认） | 已修复 |
| 55 | "FlashBlade//EXA's certification was not on the public record"（FlashBlade//EXA 的认证不在公开记录中） | 已过时。Everpure 称已将 NVCS 验证扩展至 EXA（2026 年 3 月）；NCP 待定。FlashBlade 自 2025 年 3 月起还持有 NCP 高性能存储认证（第 4 部分） | 按第 27 章和第 34 章重写 | 已修复 |
| 55 | 历史部分："EXA's … checkpoint result, 877.52 GiB/s"（EXA 的……检查点结果，877.52 GiB/s） | 缺少口径 | 改为 "checkpoint write… (vendor-submitted, peer-reviewed, in a round VAST, WEKA and DDN did not enter)"（检查点写入……（厂商提交、经同行评审，VAST、WEKA 和 DDN 未参加该轮）） | 已修复 |
| 55 | 表 55.3 针对竞争对手产品经理的反问 "including a target's PMs during diligence"（包括尽职调查期间目标公司的产品经理） | 可能被理解为建议去询问竞争对手的员工 | 增加：仅与同事、在公开场合或在尽职调查协议框架下使用，绝不用于从竞争对手员工处获取未公开信息 | 已修复 |
| 56 | "In a dual-controller array, a write is acknowledged once it sits in mirrored NVRAM"（在双控制器阵列中，写入进入镜像 NVRAM 后即被确认）；白板提示 1 "active controller → mirrored NVRAM"（活动控制器 → 镜像 NVRAM） | 与第 3a 部分修正后的第 13 章和第 14 章矛盾（FlashArray 使用两个控制器都能访问的机箱 NVRAM；由一个主控制器处理 I/O） | 改为 "mirrored or shared NVRAM"（镜像或共享 NVRAM），并附 FlashArray 说明；改为 "primary controller"（主控制器） | 已修复 |
| 56 | "That is an audited result"（这是经审计的结果）；"audited MLPerf v3.0 submissions"（经审计的 MLPerf v3.0 提交）；"Does audited benchmarking stay a differentiator"（经审计的基准测试能否保持差异化优势） | MLPerf 由厂商提交并经同行评审（第 5a 部分） | 改为 "vendor-submitted, peer-reviewed"（厂商提交、经同行评审）；并补充 DDN 和 WEKA 参加过更早的轮次 | 已修复 |
| 56 | "DFMs reached 300 TB in 2025"（DFM 在 2025 年达到 300 TB）；关键数字行 "Released 2025"（2025 年发布） | 第 26 章保留了 VERIFY：10-K 中 "released in 2025" 的解读仅来自搜索摘要（第 4 部分未解决事项） | 在正文和表格中增加限定说明 | 已修复 |
| 56 | 表 56.3 中 "What to probe in person"（当面探询什么）一栏（VAST、WEKA、DDN 各行） | 暗示直接询问竞争对手 | 更名为 "What to test (from public evidence or in formal diligence)"（检验什么（依据公开证据或在正式尽职调查中）） | 已修复 |
| 57 | 要点速览 "Forty 'Listen for' notes"（40 条 "Listen for" 提示） | 题库和关键数字表中均为 41 条 | 改为 "Forty-one"（41 条） | 已修复 |
| 57 | Q34 Listen-for "NVRAM mirror point"（NVRAM 镜像点） | 同一 FlashArray NVRAM 问题 | 改为 "NVRAM persistence point (mirrored or shared)"（NVRAM 持久化点（镜像或共享）） | 已修复 |
| 57 | Q107 "When, and at which level, will EXA be NVIDIA-certified?"（EXA 何时、在哪个级别获得 NVIDIA 认证？） | 询问未公开的日期（第 55 章自己的"不要这样说"警示过这一点）；NVCS 状态也已变化 | 改为 "Beyond NVCS validation, what gates EXA's NCP and SuperPOD certification?"（在 NVCS 验证之外，EXA 获得 NCP 和 SuperPOD 认证的关键门槛是什么？） | 已修复 |
| 57 | 其余 148 个问题和 40 条 Listen-for 提示 | 已对照修正后的章节核查（EXA 分离架构、partitioned-writer、Q81 读低于写、Q87 PureKVA 基线、Q130 VAST/MLPerf） | 无 | 已核实 |
| 58 | 一句话要点 8："A rack of the largest SSDs holds ~5× a disk rack"（一机架最大容量 SSD 的容量约为一机架磁盘的 5 倍） | 遗漏了第 38 章中的取舍 | 改为 "~5× the petabytes … at 2–3× the power"（约 5 倍的 PB 容量……功耗为 2–3 倍） | 已修复 |
| 58 | 一句话要点 41："EXA led v3.0 checkpointing at 877.5 GiB/s … skipped it"（EXA 以 877.5 GiB/s 领跑 v3.0 检查点……未参加） | 读取（588 GiB/s）落后于写入 | 增加读取数字；改为 "skipped the round"（未参加该轮） | 已修复 |
| 58 | 一句话要点 52："NAND stockpiling made free cash flow −$238M"（NAND 囤货使自由现金流为 −$238M） | 第 4 部分：原因的表述是 "strategic NAND and component purchases"（战略性 NAND 及元器件采购） | 已改写 | 已修复 |
| 58 | 关键数字表：指引 "Raised from $4.3–4.4B"（自 $4.3–4.4B 上调） | 第 4 部分：那是初始指引（2026 年 2 月），5 月还有一次中间上调 | 改为 "Initial guide $4.3–4.4B (Feb 2026), raised in May and August"（初始指引 $4.3–4.4B（2026 年 2 月），5 月和 8 月两次上调） | 已修复 |
| 58 | 其余一句话要点（Meta / FY25 10-K 历史、非 GAAP 毛利率、EXA 第三方数据节点、300 TB 对 245.76 TB、IDC 份额、$9–25B TAM） | 与修正后的章节一致；脚本数字检查通过 | 无 | 已核实 |
| 60 | 表 60.4："Purity//FA, //FB, //DN — one log-structured OS family for FlashArray, FlashBlade and EXA data nodes"（Purity//FA、//FB、//DN——覆盖 FlashArray、FlashBlade 和 EXA 数据节点的同一日志结构操作系统家族） | 第 3a 部分和第 3b 部分：Purity//DN 是运行在第三方 Linux 服务器上的数据节点软件，并非 Purity 数据路径；"one OS family"（同一操作系统家族）已收窄为 FlashArray 和 FlashBlade（包括 EXA 的元数据核心） | 重写该行 | 已修复 |
| 60 | 产品阵容 SVG 的 Purity 色带：同一说法，外加 "global FTL … across every module"（跨所有模块的全局 FTL） | 同一问题 | 色带现写作 "Purity//FB (FlashBlade and EXA metadata core), Purity//DN (EXA data-node stack)"（Purity//FB（FlashBlade 与 EXA 元数据核心）、Purity//DN（EXA 数据节点软件栈））；FTL 一行限定为 DFM 上的 Purity//FA 和 //FB；desc 已更新；已渲染，无溢出 | 已修复 |
| 60 | 架构 SVG："NVRAM mirror / failover"（NVRAM 镜像 / 故障切换）及 desc "mirrored NVRAM"（镜像 NVRAM） | 同一 FlashArray NVRAM 问题 | 改为 "mirrored or shared NVRAM; failover"（镜像或共享 NVRAM；故障切换） | 已修复 |
| 60 | //S 行与产品阵容 SVG："S500 DGX SuperPOD-certified"（S500 获 DGX SuperPOD 认证） | 不完整。FlashBlade 还持有 NCP 高性能存储认证（第 4 部分） | 已加入表格和 SVG | 已修复 |
| 60 | //XL "up to 7.4 PB effective"（有效容量最高 7.4 PB） | 第 1 部分：该有效容量数字假设平均 DRR 为 5:1 | 在表格中加入计算口径 | 已修复 |
| 60 | 表 60.5："Five of six rows, one OS family"（六行中有五行属于同一操作系统家族） | Portworx 和 EXA 数据节点不是 Purity | 改为 "one OS family across the arrays"（各阵列共用同一操作系统家族） | 已修复 |
| 60 | 协议 SVG 与表 60.2（NVMe/TCP Purity 6.4.2+，GA 待核实；S3 over RDMA 于 2025 年 3 月宣布，GA 待核实；NVMe/FC Purity 6.1；RoCE Purity 5.2） | 与第 2 部分审校后的第 7 至第 9 章一致 | 为 staging 中的 VERIFY 加注 2022/2023 来源冲突 | 已核实 |
| 60 | 缩略语表（104 个条目） | 抽查；DFM "no drive-level FTL" 与第 2 部分对 IBM FlashCore 的修正一致 | 无 | 已核实 |
| 全部 | 对 Everpure 未公开计划的推测 | 未发现。战略内容均表述为基于公开信息的选项（第 60 章引用第 54 章）；路线图问题询问的是取舍而非日期（Q107 修正后） | — | 已核实 |

## 未解决事项 / 分歧

- **第 45 章和第 49 章（第 6 部分，超出我的范围；当时尚无第 6 部分审校文件）** 仍把 EXA 的 MLPerf v3.0 结果称为 "audited"（经审计）。第 49 章的要点速览还写道 Everpure "is the only array vendor selling that IP into hyperscalers"（是唯一向超大规模云厂商销售该 IP 的阵列厂商）。第 34 章 / 第 5a 部分以及第 29、36 章 / 第 4–5b 部分已将这些措辞分别改为 "public, peer-reviewed"（公开、经同行评审）和 "only array vendor publicly known to…"（公开已知唯一……的阵列厂商）。第 8 部分现已使用修正后的措辞，因此在第 6 部分审校人统一这些章节之前，第 8 部分与第 6 部分存在不一致。
- **第 59 章标题与内容。** 大纲、`mkdocs.yml`、`docs/index.md` 和 `README.md` 写的是 "200 flashcards"（200 张闪卡）（第 58 章为 "60 one-liners"，即 60 条一句话要点），但章节实际包含 279 张卡片和 66 条一句话要点。我没有修改 H1 或导航，它们由 `meta/outline.md` 固定。主代理可考虑更新索引简介（"279 flashcards"、"66 one-liners"）。
- **第 59 章没有针对第 54 章**（战略选项地图）的卡片，因为第 54 章是在卡片集完成之后才完成的。下次重新生成卡片集时，可补充几张第 54 章的卡片。
- **卡片隐含地承载了上游的 VERIFY。** Q135 和 Q261（300 TB DFM "released 2025"）、Q181（NVCS Enterprise 约 1,000）、Q43（FC +6%，仅有搜索摘要）以及 Q226（HPE 停止转售 WEKA）的可靠程度取决于其所在章节。如果这些 VERIFY 的结论有变，请重新生成卡片。
- **PureKVA GA。** 第 55、57、58、59 章和产品阵容 SVG 现均写作 "announced for October 2026"（已宣布 2026 年 10 月上市）。如果 Everpure 确认 GA，请同时更新这五处。
- **第 55 章 / 第 28 章：Fusion 附加率所依据的客户基数**（约 14,500 对约 15,000）仍为 VERIFY。无论取哪个数，约 8% 的数字都不变。
- **网络。** 未进行网络搜索；所有事实均对照已审校的章节和审校文件核查。
