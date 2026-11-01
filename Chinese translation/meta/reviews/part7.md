# 审校报告：第 7 部分（第 51–54 章）

> 📄 英文原文：[meta/reviews/part7.md](../../../meta/reviews/part7.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

**审校范围：** `docs/07-history-and-future/51`–`54`、第 51/52 章的图表 CSV 和脚本、第 53 章雷达图与第 54 章战略地图 SVG，以及 staging 文件 ch51–ch54。审校日期 2026-11-01。

## 摘要

**核查内容**：

- **历史日期与"首次"**：我对照一手来源或信誉良好的媒体逐项核查了以下内容：
  - RAMAC（1956 年，约 3.75 MB）与 IBM 3380（1980 年，2.52 GB）
  - RAID 论文（SIGMOD 1988）与 EMC Symmetrix（1990 年）
  - NetApp（1992 年成立，1993 年推出首批 filer）与 Isilon（2001 年；EMC 于 2010 年以 $2.25B 收购）
  - S3（2006-03-14）与 NVMe 1.0（2011 年 3 月）
  - Fusion-io（2007 年推出 ioDrive；2014 年出售给 SanDisk）
  - Pure Storage（2009 年 10 月注册成立；2011 年 8 月发布 FA-300；2012 年 5 月 GA）
  - XtremIO、Violin、Nimble、Dell–EMC 与 Portworx
  - NOR（IEDM 1984）与 NAND（IEDM 1987）
  - Samsung V-NAND（2013-08-06）与 Micron–Elpida（2013-07-31，股权对价 $615M）
  - IMFT 拆分（2018–19 年，外加 Lehi 工厂出售给 TI）
  - Intel NAND → SK hynix/Solidigm（2021 年与 2025 年两次交割）、Kioxia IPO 以及 Sandisk 分拆（2025 年 2 月）
- **图表**：我重新推导了第 51 章的价格下降速率：磁盘约 26%/年，闪存约 35%/年，结果一致。我还核查了第 52 章的速率：约 35%/年，以及较 2023 年低谷 13–15× 的飙升。每一行 CSV 都带有来源、`as_of` 日期、口径和状态。脚本把仅来自搜索摘要的数据点标为空心，不同口径分别标注，使用点状参考线，并注明 "mixed bases"（混合口径）。没有暗示超出来源精度的小数位。
- **第 53 章雷达图**：我按各环半径计算了每个雷达点的半径。全部 12 个点都落在表 53.2 所给的环内，颜色也一致。
- **第 54 章先例与规则 5**：我核查了第 54 章的每一个先例，并对照规则 5 审阅了本章。
- **搜索**：约 22 次网页搜索。未使用 WebFetch：关键站点（sec.gov、厂商网站、Blocks & Files）均拒绝抓取。因此若干结论基于搜索结果摘要，脚注中已注明。

**结论**

| 章 | 结论 |
|---|---|
| 51 | 扎实；轻微修正 |
| 52 | 轻微至实质性修正：HHI 计算口径错误、一个产品名错误，并解决了六处 VERIFY |
| 53 | 轻微修正：一项预测被曲解、遗漏一项利益冲突事实、象限图注计数错误，以及时间判断需要更精确 |
| 54 | 针对规则 5 的实质性修正（"Buy option"（收购选项）一栏中出现了具名私营公司）；先例金额已更正或确认；所有 VERIFY 已解决 |

**修改后的 QA：** 四章均通过 `qa_report.py`（51：2,851/2,500；52：2,730/2,300；53：3,335/3,000；54：2,599/2,200）。`lint_mermaid.sh` 结果为 OK（8 个代码块），`check_links.py --allow-planned` 未发现失效链接。我没有修改任何 SVG 或 CSV；它们本已一致。

## 发现的问题

| 章 | 主张 / 段落 | 问题 | 已采取的修正 | 状态 |
|---|---|---|---|---|
| 51 | "Everpure was #4 at 8.1% share and the fastest-growing vendor"（Everpure 以 8.1% 份额排名第 4，且是增长最快的厂商） | IDC 2Q26 的说法是在*前五名中*增长最快（同比 +50.0%）。这也与第 54 章一致。 | 改写并加入 +50.0% 数字 | 已修复 |
| 51 | "Micron bought bankrupt Elpida for US$615M"（Micron 以 US$615M 收购破产的 Elpida） | 据 10-K，$615M 购买的是 Elpida 的*股权*；债权人受偿是另行安排的。说"以 $615M 收购"夸大了这笔交易的便宜程度。 | 改为 "paid US$615M for bankrupt Elpida's equity"（为破产的 Elpida 的股权支付 US$615M） | 已修复 |
| 51 | 时间线与各时代日期（RAMAC、3380、RAID 1988、Symmetrix 1990、NetApp 1992/93、FC-PH 1994、S3 2006、Fusion-io 2007、Pure 2009/2012、XtremIO 2012、Violin 2016、Nimble 2017、Dell–EMC 2016） | 均与来源一致 | 无 | 已核实 |
| 51 | 图 51.2，$/GB 图表 | 数据点有出处，口径已标注。空心标记表示来自搜索摘要的数据点。正文写明 "read for direction and orders of magnitude, not decimals"（看方向和数量级，而非小数）。约 1981 年的 "small drives"（小型硬盘）数据点（$500k/GB）高于 1980 年的 3380 数据点；它属于不同的硬盘类别，且已标注。 | 无 | 已核实（可接受） |
| 52 | NAND 的发明："Kioxia 1987 vs SHMJ 1988 … the company's date, not an undisputed one"（Kioxia 1987 对 SHMJ 1988……这是公司给出的日期，并非无争议） | NAND 单元于 1987 年 12 月在 IEDM 上发表（Masuoka、Momodomi、Iwata、Shirota，Tech. Digest pp. 552–555）。1987 年是站得住脚的日期；SHMJ 的 1988 年似乎是之后的一次发布。第 2 章已采用 1987 年，因此图谱现已一致。 | 改写该段及"不要这样说"条目；在脚注 4 中加入 IEDM 引文 | 已修复 |
| 52 | NAND HHI "about 2,260 for 2Q26 (33.5² + 20.7² + …)"（2Q26 约为 2,260） | 口径错误。这些份额是占*前五名合计*的份额（合计为 100），而 2008 年的份额是市场份额。TrendForce 2Q26 的市场份额为 29.3/18.2/15.1/13.6/11.4（前五名 = 87.6%），由此得出的 HHI 约为 1,730。"less concentrated"（集中度更低）的结论因此更强，而非更弱。 | 改用市场份额、87.6% 数字和方向性说明重写；更新关键数字表中的对应行 | 已修复 |
| 52 | "ServeTheHome called Seagate's 15K.6 the likely final 15K series"（ServeTheHome 称 Seagate 的 15K.6 可能是最后一代 15K 系列） | 产品错误。Cheetah 15K.6 约于 2007 年推出；该文（约 2017 年）讲的是最后一批 Enterprise Performance 15K 硬盘。 | 已更正并注明日期；删除 VERIFY | 已修复 |
| 52 | 对话手册："is PLC worth it at a 20% bit gain?"（以 20% 的比特增益，PLC 值得吗？） | PLC 每单元增加 25% 的比特；20% 是理想情况下每比特成本的降幅（表 52.1 是正确的） | 已改写 | 已修复 |
| 52 | SLC→MLC 行 `[VERIFY]` | 已解决：Toshiba/SanDisk 1 Gb MLC NAND，2001 年 11 月 Comdex，首款 MLC *NAND*（MLC 此前已在 NOR 中出货） | 补全该行；在脚注 20 中加入来源 | 已修复 |
| 52 | SK hynix 对 Intel 的最后一笔付款 "~$1.9B net"（净额约 $1.9B）`[VERIFY]` | Intel 2025-03-27 的 8-K：约 $1.9B，为扣除调整后的净额 | 加入脚注 51；删除 VERIFY | 已修复 |
| 52 | Elpida 交割日期 `[VERIFY]` | Micron FY2013 10-K：2013-07-31 | 更新正文和脚注 30 | 已修复 |
| 52 | "Almost no wafer capacity in 2026 [VERIFY: secondary]"（2026 年几乎没有新增晶圆产能） | TrendForce 2Q26 NAND 发布称，供应商优先将资本开支投向 DRAM/HBM，而非新增 NAND 产能 | 加入 TrendForce 作为依据；删除 VERIFY | 已修复 |
| 52 | 表 52.2 的日期与数值（WD–SanDisk、Toshiba Memory、IMFT、Kioxia IPO、Sandisk 分拆） | 一致 | 无 | 已核实 |
| 52 | 表 52.3 Pure FA-300 "$5–10 per usable GB"（每可用 GB $5–10）（2011–12 年） | 与 2011 年的报道一致。2012 年的 HA 型号报价为 $4–8。 | 无 | 已核实 |
| 53 | 趋势 8：把 Gartner 的 "80% by 2029"（2029 年达 80%）当作存储 + 目录 + 治理 + 向量融合的独立证据；"date has already moved out a year"（日期已推迟一年） | 曲解。Gartner 预测的是*文件与对象平台整合*，这是一个更窄的论断。其 2023 年版本（2028 年达 70%，起点 35%）被*上调*为 2029 年达 80%，而不是推迟。 | 改写：该预测现在只支持趋势中平台整合的那一半；VERIFY 已解决 | 已修复 |
| 53 | 趋势 11：Cerabyte "counts Western Digital as an investor"（投资方包括 Western Digital） | 遗漏了 Pure Storage 曾对 Cerabyte 进行战略投资（2024 年 7 月），且 John Colgrove 进入其董事会。这是读者需要知道的利益冲突事实。 | 已加入正文和表 53.2（第 11 行）；在脚注 18 中加入来源 | 已修复 |
| 53 | 趋势 1 的判断："1 PB-class by 2029–30"（2029–30 年达到 1 PB 级） | 唯一来源是一场未注明日期的联合创始人网络研讨会。该时间点是作者的外推，而非路线图。 | 增加明确说明：这是按 75→150→300 TB 节奏的外推；没有公开的、注明日期的 600 TB 或 1 PB 路线图 | 已修复（校准） |
| 53 | 要点速览 "HAMR takes nearline drives … toward 100 TB by about 2029"（HAMR 将在约 2029 年把近线硬盘推向 100 TB） | 把厂商路线图当作事实陈述 | 改为 "Vendor HAMR roadmaps take…"（厂商的 HAMR 路线图将……） | 已修复 |
| 53 | "Roadmaps a vendor controls end to end fare better: Pure … met it"（厂商端到端掌控的路线图表现更好：Pure……兑现了） | 把一个有利的数据点泛化为规律；Pure 同样依赖 NAND 供应商 | 语气弱化；改为 "one data point, not a rule"（一个数据点，而非规律） | 已修复 |
| 53 | 趋势 6：CPO "in production"（已量产）`[VERIFY]` | NVIDIA 于 2026-05-31 称 "in production"；TrendForce 报道截至 2026 年 7 月已向部分合作伙伴出货；全面供货未经确认 | 措辞更精确；为脚注 29 加注；删除 VERIFY | 已修复 |
| 53 | 图 53.2 图注 "Four trends sit in 'bet now'"（四个趋势位于"立即押注"象限） | 第一象限中有五个点（基于 RDMA 的对象存储，y = 0.56） | 图注已更正；注明各点位置为作者判断 | 已修复 |
| 53 | 表 53.2 图注 "well placed on … convergence"（在……融合方面处于有利位置）；"No competitor ships a proprietary module at 300 TB"（没有竞争对手出货 300 TB 的自有模块） | 轻度偏向 Everpure。第 54 章将 Data Intelligence 评为 "early"（早期）。对模块领先没有给出最强版本的反方论证。 | 改为 "early but unproven on convergence"（在融合方面尚处早期、未经验证）；指出 IBM FCM 是最接近的类比；加入 FDP / 512 TB 的最强版本反方论证 | 已修复（偏向性） |
| 53 | 雷达图 SVG 与评分卡 | 全部 12 个点的环和颜色均匹配（通过计算半径核查） | 无 | 已核实 |
| 54 | 表 54.1 收购一栏："Cyera is a category leader at a reported $12B mark"（Cyera 是品类领导者，据报道估值 $12B）、"WEKA (last mark $1.6B) and Hammerspace (>$500M) are category examples"（WEKA（最近估值 $1.6B）和 Hammerspace（>$500M）是品类示例） | **规则 5。** 在"收购选项"一栏中列出具名私营公司，读起来像是暗示的收购目标，违反了本章自己 "never a named private company as a target"（绝不把具名私营公司作为目标）的规则。该表也与只列已完成先例的图 54.1 不一致。 | 替换为已完成或已宣布的先例（Veeam–Securiti、Everpure–1touch；NetApp–PEAK:AIO）。估值数字以不具名方式移到取舍一栏，作为价格基准。 | 已修复 |
| 54 | "That makes them likelier partners, or rival bidders, than targets"（这使它们更可能成为合作伙伴或竞购对手，而非目标） | 暗示正在把 Veeam 和 Salesforce 当作目标来权衡，并暗示 Everpure 是竞购方 | 改写为关于价格水平的观察 | 已修复 |
| 54 | 要点速览 / 图 54.1："entered the top three layers only in 2026"（直到 2026 年才进入最上面三层） | 层级错误。2026 年进入的是第 5、7、8 层；第 6 层（Pure1/Portworx）早在 2020 年或更早即已进入。 | 两处均已更正 | 已修复 |
| 54 | IBM–Confluent 约 $11B EV，2026 年交割 `[VERIFY]` | 2025-12-08 宣布，每股 $31（EV 约 $11B）；2026-03-17 完成交割。10-Q 显示按会计口径的总对价约为 $11.6B。 | 年份改为 "2025 → 2026"；在脚注 39 中加入来源；删除 VERIFY | 已修复 |
| 54 | Palo Alto–Chronosphere "$3.35B (*reported*) [VERIFY]"（*媒体报道*） | 价格为公司公告（2025-11-19；现金加替代股权激励） | 重新标注；年份改为 "2025 → 2026"；更新脚注 38 | 已修复 |
| 54 | Cohesity–Veritas "Combined company >$7B (*company-stated*)"（合并后公司 >$7B，*公司自述*） | 交割新闻稿中没有此数字。约 $7B 是宣布交易时报道的合并后公司估值，而非交易价格，且交易价格未披露。 | 重新标注为 "Price not disclosed; combined company ~$7B (*reported*)"（价格未披露；合并后公司约 $7B，*媒体报道*） | 已修复 |
| 54 | HPE–Juniper 关口 5 示例 `[VERIFY in staging]` | 已确认：DOJ 起诉（2025 年 1 月）；2025-06-28 达成和解（剥离 Instant On，拍卖 Mist AI 源代码许可）；2025 年 7 月完成交割 | 加入补救措施；在脚注 27 中加入 HPE 和解新闻稿 | 已修复 |
| 54 | Lenovo–Infinidat ">$500M (*estimated*)"（*估算*） | 2025 年 1 月宣布，2026 年交割；价格未披露，Globes 估计超过 $500M | 在脚注 40 中加入 Globes | 已核实 |
| 54 | NetApp–DataPelago（2026-07-16，未披露）；AMD–MEXT（2026-06-15，未披露） | 已确认 | 无 | 已核实 |
| 54 | SK hynix–Intel "$9B" | 这是标题数字；实际收款为 $7B 加约 $1.9B 净额 | 在表 54.2 中加以说明 | 已修复 |
| 54 | "NetApp's buying spree"（NetApp 的收购狂潮） | 对两笔小额交易而言措辞带有倾向性 | 改为 "NetApp's two 2026 deals"（NetApp 在 2026 年的两笔交易） | 已修复（偏向性） |

## 未解决事项 / 分歧

- **第 51 / 52 章，仅有搜索摘要支撑的图表锚点。** 以下各项在 CSV 状态列和 staging 中仍为 VERIFY：RAMAC $10,000/MB（IBM 自己的估计约为 $11.4k/MB）、3380 的标价区间、SunDisk 1991 年数据点、Semico/iSuppli 2005 年 $45/GB 数字、2008 年 TrendForce NAND 份额以及 TrendForce 2026 年晶圆现货读数。它们都不会改变数量级或方向，但 2008 年的份额决定了 HHI 对比。
- **第 51 章，Symmetrix 41% 对 IBM 35%（1995 年）。** 仍只依据 The Register 的一篇访谈。保留 "by one account"（据一种说法）的表述。
- **第 53 章，PureKVA/CMX 与趋势 1。** Colgrove 关于 600 TB / 1 PB 的表述以及 Meta 关于 512 TB 的表述仍未经核实。Gartner 关于智能体运维（agentic ops）的预测（2028 年由 <1% 增至 20%）仍只有搜索摘要支撑。
- **第 53 章，图 53.2 与正文。** 正文把 "Disaggregation and DPUs"（解耦与 DPU）称为 "table stakes"（基本门槛），但图中把它放在"立即押注"象限，而图表中的 "Table stakes" 象限含义是高确定性、低影响。这是措辞冲突而非错误；作者可考虑重命名该象限或该判断。
- **第 54 章，"four deals in 17 years cost about $594M"（17 年内四笔交易共花费约 $594M）。** 这意味着 StorReduce 约为 $20M，我未核实。无论如何，总额都在四舍五入范围内。
- **第 54 章，关口 3 中 WEKA 约 16× ARR 与 VAST 约 60× 已承诺 ARR 的估值倍数。** 两者均为公司自述，经由第 43 章引用。我保留了它们，因为它们是估值基准，而非目标。
