# 审阅报告：第 1 部分（第 1–6 章）

> 📄 英文原文：[meta/reviews/part1.md](../../../meta/reviews/part1.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

**审阅范围**：`docs/01-storage-fundamentals/01-what-storage-does.md` 至 `06-data-protection-and-resilience.md`，相关 SVG 与图表素材（`ch02-media-hierarchy.svg`、`ch02-nand-cell.svg`、`ch06-rebuild` 图表及其 CSV、`ch02_hdd_vs_nand_cost.csv`），以及各章的 staging 文件。审阅日期 2026-11-01。

## 摘要

我重新推导了每一个算例：WAF 不动点、DWPD、每 TB 映射表所需 DRAM、Little 定律、M/M/1 尾部、32 颗 die SSD 的拐点、扇出概率、容量瀑布图、完整的五年 TCO 及其敏感性分析、DRR 混合比与每有效 TB 价格表、去重索引大小与碰撞概率、EC 开销、重建小时数、URE 概率、光纤往返时间，以及 5 PB 恢复。大部分算术是正确的。WAF 模型（u = e^-(1-u)(1+OP)）精确复现了 7.8 / 4.1 / 2.1，TCO 表重新计算得到 $4.29M 对 $1.33M。

实质性问题集中在物理机制的表述、一处增长率计算、一个重建模型，以及对部分合同条款的描述上。详见下文。

我进行了约 30 次网络搜索。正如任务说明所预警，厂商网站、SEC 和 blocksandfiles 无法直接抓取；我依据搜索摘要引用它们，脚注中已注明。

**结论**：
- 第 1 章：扎实。解决了一个 VERIFY。
- 第 2 章：实质性修正（金字塔图中的 HBM 延迟、擦除机制、P/E 范围、Backblaze 降价速率、HDD 寻道时间、表 2.1 的表注）。
- 第 3 章：轻微修正（LDPC 重试流程、映射条目宽度、Micron DRAM 问题已解决、FDP 证据加强）。
- 第 4 章：实质性修正（Evergreen//One 计费描述有误、FlashArray "3.9:1" 的误读、TCO 价格输入不匹配现已披露）。
- 第 5 章：轻微至实质性（WEKA 历史有误、DeepReduce 基线问题已解决、保证计划方面的倾向已平衡）。
- 第 6 章：对分布式（declustered）重建模型做了实质性修正；更正 Dell 保证计划的适用范围；不可变性比较更加公允。

**修改后的 QA**：六章全部通过 `qa_report.py`，所有 Mermaid 块 lint OK，失效链接为 0。字数有所增加。脚注已按首次引用顺序重新编号。第 2、5、6 章的阅读时间已更新。ch02 和 ch06 图表已重新生成。

## 发现的问题

| 章 | 原文主张 / 段落 | 问题 | 已采取的修正 | 状态 |
|---|---|---|---|---|
| 2 | 金字塔 SVG：HBM "~100 ns class"（"约 100 ns 级"）；要点速览 "memory 100–300 ns"（"内存 100–300 ns"） | 对 GPU 而言是错误的。在 H100 上，一次缓存未命中的 HBM 加载约需 350 ns（指针追踪测试），比 CPU DRAM 还慢。HBM 是带宽层级 | SVG 改为 "~350 ns from GPU"（"从 GPU 访问约 350 ns"）；补充 desc 与脚注说明；正文新增一句并引用 arXiv；要点速览改为 100–400 ns | 已修复 |
| 2 | 金字塔 SVG：HBM 每 GB 价格 "$10–20" 而正文为 "$8–18"；SSD "$0.10–0.80"；HDD "30–44 TB" | 内部不一致。$0.10/GB 是 2025 年中的 QLC 价格，与本章自身给出的 18–23× 溢价相矛盾 | 改为 $8–18、$0.30–0.80 和 20–44 TB | 已修复 |
| 2 | "Erase pulls charge out by raising the channel or well voltage"（"擦除通过抬高沟道或阱电压把电荷拉出"）（正文与 SVG） | 这是浮栅的图景。电荷俘获型（charge-trap）的擦除主要靠空穴注入来中和被俘获的电子；由于多晶硅沟道没有体接触，3D 串常通过 GIDL 产生空穴 | 重写正文和 SVG；补充 ISPP、TLC/QLC 多遍编程以及约 16 kB 的页；QLC 的 tPROG 改以 ms 计 | 已修复 |
| 2 | "GC … the DRAM-refresh of flash"（"垃圾回收……相当于闪存的 DRAM 刷新"） | 类比不严谨（刷新更接近数据保持方面的巡检擦洗） | 改为 "a background tax, much as refresh is for DRAM"（"一种后台开销，就像刷新之于 DRAM"） | 已修复 |
| 2 | DWPD ≈ P/E ÷ (WAF × 天数) | 遗漏了原始容量/用户容量（OP）项 | 公式已修正。以 Micron 6600 ION 的额定值为锚：128 KB 顺序写为 1.0 DWPD，16 KB 随机写为 0.3，推算当前 QLC 约 2,000 次 P/E | 已修复 |
| 2 | 表 2.1：TLC 约 1,000–3,000、QLC 约 500–1,500 次 P/E | 偏低。扣除 OP 和 WAF 后，与 Micron 7450 MAX（3 DWPD）和 6600 ION（顺序 1.0 DWPD）的额定值不符 | 改为 TLC 3,000–10,000、QLC 1,000–3,000；注明推导过程；VERIFY 更加具体 | 已修复 / 已标记 |
| 2 | 表 2.1 表注 "each added bit gives 33%, 25% then 20%"（"每增加 1 bit 依次带来 33%、25%、20%"） | SLC→PLC 的序列有误（应为 100/50/33/25%） | 已修正 | 已修复 |
| 2 | "Each extra bit halves the voltage margin"（"每多 1 bit，电压裕量减半"） | 间隔数依次为 1→3→7→15，因此只是大致减半（SLC→MLC 是三分之一） | 要点速览和 SVG 中改为 "roughly halves"（"大致减半"） | 已修复 |
| 2 | 数据保持："about three months … at end of life"（"寿命末期……约三个月"） | 准确，但读者容易理解为典型寿命 | 澄清为 JESD218 规定的寿命末期下限；新盘保持时间更长，但不作保证 | 已修复 |
| 2 | HDD："~4–5 ms seek → 8–10 ms → 100–125 IOPS, ~4 IOPS/TB" | 该寻道时间属于 10k/15k rpm 硬盘的范畴。近线硬盘标称约 8 ms，实测更高。这也与第 4 章 QD16 下 170 IOPS 的数字冲突 | 改为约 12 ms、QD1 约 80 IOPS、QD16 约 170、3–6 IOPS/TB；与第 4 章一致 | 已修复 |
| 2 | Backblaze 2009 至 2022 年 11 月 $0.11→$0.014/GB "≈0.5%/month, ~6%/yr"（"约每月 0.5%、每年约 6%"） | 算术错误。正确结果为约每月 1.2%、每年约 14% | 已修正 | 已修复 |
| 2 | 2026 年 Q1 的 22.6× 引用自 PCSP（SEO 页面） | 来源层级低；未说明是 QLC 还是 TLC 口径 | 改为引用 Blocks & Files 和 Tom's Hardware（VDURA 指数，QLC 口径，2025 年 Q2 为 4.9×）。注明该指数曾切换口径，HDD 从 $668 涨至 $1,216；图表 CSV 已更新 | 已修复 / 已标记 |
| 2 | Mozaic 4+ 44 TB（VERIFY，SEO 来源） | 已由 Seagate 投资者关系页面确认，2026-03-03 | 删除 VERIFY | 已修复 |
| 2 | Blackwell Ultra 288 GB（VERIFY） | 已确认（12 层堆叠 HBM3E） | 删除 VERIFY；更新脚注 | 已修复 |
| 2 | 2020 年前里程碑的 VERIFY | RAMAC 在第 1 章中已引用 Computer History Museum | 已解决；只剩 2016–22 年的层数节点作为背景信息 | 已修复 |
| 3 | LDPC："re-reads at shifted voltages, giving soft information"（"以偏移电压重读，得到软信息"） | 混淆了读重试（偏移 Vref，硬判决译码）与软判决译码（多次包夹读取 → LLR） | 纠正升级流程 | 已修复 |
| 3 | 表 3.1 在 245 TB / 16 KB 下 "~4 B/entry"（"每条目约 4 B"） | 150 亿个单元超过 2³²，因此条目至少需要 34 bit | 补充注释；该列标注为 "(floor)"（"下限"） | 已修复 |
| 3 | Micron 6600 ION DRAM（VERIFY，64 GB 还是 16 GB） | TweakTown 和 TechRadar 正文都写 64 GB；只有标题写 16 GB。评测认为 16 KB IU 使其随机写性能约为 64 KB IU 竞品的 3 倍 | VERIFY 已解决 | 已修复 |
| 3 | FDP CacheLib 1.3→1.0（VERIFY） | 已确认。同一份演示文稿显示满利用率时为 3.5→约 1；EuroSys 2025 论文报告在无主机侧 OP 时约为 1 | 证据加强；删除 VERIFY | 已修复 |
| 3 | LightNVM "2017" | 合入 Linux 4.4（2016）；FAST 论文为 2017 | 时间线拆分为 2016 / 2017 | 已修复 |
| 4 | "Evergreen//One metered on effective used capacity, with a floor at the reserve commitment plus 25%"（"Evergreen//One 按有效已用容量计量，下限为预留承诺量加 25%"） | 错误。25% 是 Everpure 保持部署的容量缓冲（最多 1 PiB），不是计费下限。客户支付的是预留承诺量加按需用量，二者都以 EUC 计 | 已重写；新增 Everpure 支持文档 | 已修复 |
| 4 | "FlashArray//XL R5 1.9 PB raw → 7.4 PB effective implies ~3.9:1"（"原始 1.9 PB → 有效 7.4 PB，意味着约 3.9:1"） | 误读。Everpure 的有效容量数字假设平均 DRR 为 5:1；3.8× 是扣除 RAID、元数据和 TiB 换算后的有效/原始之比 | 已修正；新增产品页脚注 | 已修复 |
| 4 | TCO 输入：QLC $302/TB（122 TB 街价）对 HDD $22/TB（2026 年 Q1） | 由此推算的介质溢价 13.7× 远低于同章使用的 22.6× 标题数字；而按同一指数，HDD 到 2026 年 Q3 已涨至约 $40/TB | 在正文中披露；在要点速览和数字表中新增敏感性分析（按 2026 年 Q3 HDD 价格约为 2.7×） | 已修复 / 已标记（第 38 章） |
| 4 | 混合平台 "$40 per raw TB"（"每原始 TB $40"） | 只有当闪存层按 $150/TB 计价时，$0.77M 的总额才成立 | 澄清该行标签 | 已修复 |
| 4 | 瀑布图显示 TiB "loss"（"损失"） | 这是单位换算，不是丢失的字节 | 补充一句说明 | 已修复 |
| 4 | VDURA 22.6× 与 ServNet HDD 价格（2 个 VERIFY） | 已由 B&F 引用的 VDURA 数字佐证（QLC $2,450→$15,121；4.9×→22.6×） | 删除 VERIFY；注明来源及 VDURA 的厂商利益关系 | 已修复 |
| 4 | 其余所有算例（Little 定律、M/M/1 4.6×/6.9×、QD32 下 255K IOPS、63%/64%/99%、瀑布图、TCO 及其 2.0×/1.6×/校验敏感性） | 已重新计算 | 无 | 已核实 |
| 5 | "WEKA adding data reduction in NeuralMesh 6 (2026)"（"WEKA 在 NeuralMesh 6（2026）中加入数据缩减"）；相似性缩减只列了 VAST + Everpure | 历史有误。WEKA 自 WEKA 4.2（2023）起就具备集群范围、后处理、4K 块相似性加差分（delta）缩减 | 修正时间线、历史、要点速览以及在线/后处理相关文字；表 5.3 新增 WEKA 一行 | 已修复 |
| 5 | DeepReduce 基线（VERIFY）；"always-on in October"（"10 月起始终开启"） | 2:1 的中位数是在已压缩数据之上测得的。始终开启是在 9 月下旬宣布、10 月生效 | 删除 VERIFY；日期与第 27 章对齐 | 已修复 |
| 5 | Evergreen//One "reportedly" EUC-billed（"据报道"按 EUC 计费）（VERIFY） | 已由 Everpure 支持文档确认 | 删除 VERIFY | 已修复 |
| 5 | "Everpure inverts … more honest"（"Everpure 反其道而行……更诚实"） | 偏向 Everpure。按工作负载确定的保证依赖厂商自己的容量评估，而 Dell 的 6:1 无需评估或签字 | 两方面均作平衡 | 已修复 |
| 5 | Dell 6:1 Gen 3（PowerStoreOS 5.0）；5:1 Gen 2/PowerMax；NetApp 4:1 SAN / 3:1 虚拟化 NAS / 1.5:1 NAS；Right-Size //X 和 //XL | 已确认（部分 Dell 地区页面仍写 5:1） | 无 | 已核实 |
| 5 | StorReduce US$20.5M | 这是 10-K 中的净额；宣布时约为 $25M | 补充 "net of cash acquired"（"扣除所获现金后"） | 已修复 |
| 5 | 算例（31:1 总效率、调和平均混合、表 5.2、10⁻⁵⁵ 碰撞概率） | 已重新计算 | 无 | 已核实 |
| 6 | 分布式重建："100 drives × 0.5 GB/s → 1.4 h"（"100 块盘 × 0.5 GB/s → 1.4 小时"） | 忽略了该段自己提到的 k 倍读放大。在 16+2 下，50 GB/s 的输出需要 800 GB/s 的读取 | 重新设定为：每盘读 4 GB/s、8+2 条带 → 输出 50 GB/s → 1.4 小时；并给出 16+2 和 146+4 的后果。图表注释和 CSV 已更新（数字未变） | 已修复 |
| 6 | 150 TB 的 DFM 疏散 "tens of minutes"（"数十分钟"）（VERIFY） | 在任何来源中都未找到；这意味着单个模块需约 40+ GB/s。95% 的说法确实存在，但没有公开的基线 | 删去该说法；标注为公司自述；VERIFY 更加具体 | 已标记 |
| 6 | PowerMax 一行中的 Dell Cyber Recovery Guarantee | 它覆盖的是 PowerProtect DD Cyber Recovery 隔离库（生产 US$5M + 隔离库 US$5M），而非 PowerMax | 在表格和数字行中更正适用范围 | 已修复 |
| 6 | 将 "ROW snapshots are nearly free, so SafeMode can default on"（"ROW 快照几乎零成本，因此 SafeMode 可默认开启"）作为 Everpure 的差异化；对 NetApp 描述单薄 | NetApp 的防篡改快照即使是 NetApp 支持团队也无法缩短保留期；它还有 ARP 检测和 MAV | 比较更公允；补充检测类厂商；差异化收窄为替换阵列 SLA | 已修复 |
| 6 | WAFL/ZFS 被称为 "log-structured"（"日志结构"） | 二者属于任意位置写（write-anywhere），自称 "copy-on-write"（"写时复制"） | 措辞已修正；注明这一术语陷阱 | 已修复 |
| 6 | URE 概率 "should hit more than one error"（"应会遇到不止一个错误"） | 规格值是上限；现场实测比率更低 | 补充限定说明 | 已修复 |
| 6 | 同步复制 "four to nine times slower"（"慢四到九倍"） | 1.15/0.15 = 7.7，因此范围应为四到八倍；不带写加速的 FC 需要两次往返 | 已修正并注明 | 已修复 |
| 6 | Evergreen//One 网络安全 SLA（VERIFY）；ActiveCluster 2017（VERIFY）；RAID-5 2007 年文章（VERIFY） | SLA 主要条款已确认（次工作日发货、48 小时计划、8 TiB/h、同样覆盖灾备）；ActiveCluster/Purity 5.0 于 2017 年发布以及 Harris 的文章均已有定论 | 删除 VERIFY；合同细则仍记录在 staging 中 | 已修复 |
| 6 | EC 计算、重建小时数、5 PB 按 8 TiB/h ≈ 24 天、光纤 RTT | 已重新计算 | 无 | 已核实 |
| 1 | VAST 块存储 "VERIFY GA date"（"VERIFY GA 日期"） | NVMe/TCP 块存储于 2025 年初推出（VAST 5.3） | 已依据 Next Platform 和 VAST KB 解决 | 已修复 |
| 1 | S3 23×、LTO 原生 64 EB、131,072 次写入、RAMAC | 已重新计算或核查 | 无 | 已核实 |

## 未解决事项 / 分歧

- **第 38 章（不在我的审阅范围内）使用了相同的 TCO 介质输入**（2026 年 Q1 的 HDD $22/TB；按 122 TB 街价得出的 QLC $302/TB）。它应附上同样的限定说明：推算溢价为 13.7×，而非 22.6× 的标题数字；且按同一指数，HDD 到 2026 年 Q3 已达约 $40/TB。请核查 TechRadar $37,128 报价的日期。
- **2026 年 SSD:HDD 溢价**仍依赖一家混合存储厂商（VDURA）未披露来源的单一指数，且该指数曾在 QLC 与 TLC 口径之间切换。未找到 TrendForce 或 Coughlin 的佐证。
- **表 2.1 中的 P/E 范围**现由 DWPD 额定值推导，而非来自 NAND 厂商披露（厂商很少公布）。
- **DFM 疏散主张**（第 6 章，第 26 章可能也有）：没有公开的小时数。建议向 Everpure 工程团队询问 150 TB 和 300 TB 下疏散与重建的耗时对比。
- **300 TB DFM GA**（第 2、4 章）：仅有 2023 年路线图（"2026"）和 B&F 2026-08-11 的报道支持。
- **Right-Size Guarantee 的期限**：来源互相矛盾（较早资料为 6 个月，较新的博客为 12 个月）。本章保留 12 个月，脚注上的 VERIFY 保留。
- **EUC 定义**：我写的是 Evergreen//One 的有效已用容量在数据缩减之前计量。计费单位文档确认了 EUC，但我没有看到其正式定义。值得对照当前的 Product Guide 核查一次。
- **流程说明**：我误运行了一次只读的 `git status`（未通过 git 做任何更改）。
