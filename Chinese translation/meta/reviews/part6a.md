# 审阅：第 6a 部分（第 40–44 章）

> 📄 英文原文：[meta/reviews/part6a.md](../../../meta/reviews/part6a.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

**审阅范围：** `docs/06-industry-and-competition/40-market-structure.md` 至 `44-ddn.md`，及其暂存文件。审阅日期 2026-11-01。

## 摘要

**核查内容。** 我重新计算了五章中的每一个算例数字：

- **第 40 章：** 由 IDC 2Q26 增长率倒推出的 2Q25 基数（总计 US$7.74B、全闪存 US$3.78B、高端 US$1.42B）、推导出的上年同期厂商份额、价格/数量表，以及 TAM 三角校验。
- **第 41 章：** 估值与收入加总，以及各倍数（60×、45.5×、16×、12.5×）。
- **第 42 章：** 条带开销与 11 PB 原始闪存缺口、相似性缩减示例、Rule of X 推断、SCM 占比以及嵌入向量字节数。
- **第 43 章：** KV 字节数及重算与读取的对比、OCI 容量与吞吐量比、由 WEKApod 3 有效容量声明隐含的缩减比、按目录价计算的 ARR，以及各融资轮次的加总。
- **第 44 章：** Eos 扩展、检查点时间、Qwen3-32B KV 字节数、倍数以及人均收入。

算术几乎全部正确。我在融资、客户、产品状态和 MLPerf 相关论断上做了约 25 次检索。

**网络访问。** idc.com、docs.weka.io 和 huggingface.co 不在本会话允许的域名范围内，因此对它们的 WebFetch 失败。来自这些网站的数字依赖检索结果摘要。

**结论：**

| 章 | 结论 |
|---|---|
| 40 | 扎实；小幅修正（TAM 标注、解决 Gartner 的 VERIFY） |
| 41 | 实质性修正（EXA 认证表述有误、HPE 日期、DDN"first institutional money"（首笔机构资金）、把 Everpure 预付款当作事实陈述、MLPerf 历史） |
| 42 | 实质性修正（数据缩减比、SyncEngine/Polaris 状态、遗漏 VUA、MLPerf 历史、xAI 引用、"audited"（经审计）的倾向性） |
| 43 | 实质性修正（纠删码配置规则无依据、HPE 细节、融资加总、KV"a year before NVIDIA"（比 NVIDIA 早一年）、Series E 拆分、偏向 Everpure 的句子） |
| 44 | 小幅至实质性修正（VAST Colossus 声明引用错误、删除无来源的租户隔离负面说法、补充 MLPerf v0.5、VAST KV 行有误） |

**跨章一致性现已到位。** 五章及第 16、29 章现在在以下方面一致：

- **VAST：** US$30B Series F（2026 年 4 月，约 US$1B，约一半为老股转让，Drive Capital 领投，Access Industries 联合领投）；FY2026 年末 CARR 超过 US$500M；预订额超过 US$4B；US$1.17B 的 CoreWeave 交易（约占预订额的 29%）。
- **WEKA：** US$1.6B Series E（2024 年 5 月）；2024 年 ARR 超过 US$100M；ARR 估算为 US$100–150M。
- **DDN：** US$5B Blackstone 融资（2025 年 1 月）；2025 年收入约 US$0.5B（媒体报道）；2026 年目标约 US$1B。
- **Everpure：** 订阅 ARR 为 US$2.13B（Q2 FY27）。
- **HPE–WEKA：** 2025 年 11 月宣布，1 月 31 日停止报价，自 2026 年 3 月 3 日起不再接受订单。第 41 章与第 43 章现已一致。
- **xAI：** 三篇深度剖析中均写为"both supply Colossus; the split is unknown"（两家都为 Colossus 供货；份额划分未知），并注明 VAST 2025 年 10 月的扩展。
- **MLPerf Storage 历史：**
  - DDN 参加了 v0.5、v1.0 和 v2.0。
  - WEKA 参加了 v0.5 和 v1.0。
  - VAST 从未提交。
  - 三家都缺席了 v3.0。
- **用语：** 全书对 MLPerf 一律以"peer-reviewed"（经同行评审）取代"audited"（经审计）。

**修改后的 QA：** 五章均通过 `qa_report.py`，`lint_mermaid.sh` 为 OK，`check_links.py --allow-planned` 未发现失效链接。正文字数：40：2,377，41：2,975，42：4,720，43：4,173，44：4,064。所有深度剖析章节均 ≥ 3,150，且每章都高于预算。凡新增来源之处，我都按首次引用顺序重新编号了脚注。

## 审阅发现

| 章 | 论断 / 段落 | 问题 | 已作修改 | 状态 |
|---|---|---|---|---|
| 40 | IDC 2Q26 US$10.34B +33.6%，全闪存阵列（AFA）52.1%，Dell 23.8% / +42.5%；1Q26 Dell 31.2% | 经 IDC、StorageReview 和 B&F 的检索摘要确认。Huawei、NetApp、Everpure 和 HPE 的份额无法获取（表格以图片形式发布）；推导出的 2Q25 份额已重新计算且一致 | 无 | 已核实（部分为二手来源） |
| 40 | IDC AI 基础设施 1Q26：US$89.7B，存储 US$2.2B = 2.4%，2026 年预测 US$497B | 已确认 | 无 | 已核实 |
| 40 | 自上而下法"At IDC's own measured storage share"（按 IDC 自己测得的存储份额）× 2026 年预测 | 读起来像 IDC 的数字，但实际是把 1Q26 的份额套用到 IDC 并未给出存储份额的预测上 | 标注为本图谱的外推 | 已修复 |
| 40 | 自下而上的下限加总了 CARR、一个收入目标和一个 ARR 估算 | 指标混用；DDN 的数字包含 HPC 和 Tintri；VAST 的新闻稿中没有"January 2026 fiscal year"（截至 2026 年 1 月的财年） | 补充保留说明（"order of magnitude, not a sum"（数量级，而非加总））；财年标签统一为"fiscal year 2026"；区间的上下限分别注明其锚定依据 | 已修复 |
| 40 | VAST"not in reported 2026 placements [VERIFY]"（未出现在已报道的 2026 年排名中） | B&F 2026-08-24：VAST 未入选，DDN 被移出；Gartner 对文件与对象存储厂商分别评估 | VERIFY 已解决并新增脚注；删除暂存条目 | 已修复 |
| 41 | "Blackstone … DDN's first institutional money"（Blackstone……DDN 的首笔机构资金） | 这是 Blackstone 的说法，但 DDN 在 2002 年前后曾获得约 US$12M 的风险投资（第 44 章） | 归属于 Blackstone 的说法，并注明 2002 年的风险投资 | 已修复 |
| 41 | 表 41.3：EXA"No NVIDIA certification … yet"（尚无 NVIDIA 认证） | 与第 27 章矛盾：Everpure 于 2026 年 3 月宣称 EXA 获得 NVIDIA-Certified Storage，NCP 待定，无 SuperPOD 认证。这低估了 Everpure | 已按第 27 章更正 | 已修复 |
| 41 | "HPE stopped reselling WEKA …"（HPE 停止转售 WEKA……）；记分卡"HPE drops WEKA (Nov 2025)"（HPE 放弃 WEKA（2025 年 11 月）） | 混淆了宣布日期（2025 年 11 月）与生效日期（2026-03-03 停止接单）；HPE 的增值经销商（VAR）仍可在 HPE 服务器上销售 WEKA | 两个日期均列出，与第 43 章一致；补充经销商保留说明；脚注加注 | 已修复 |
| 41 | "Everpure … used about US$577M of prepayments for strategic NAND"（Everpure……将约 US$577M 预付款用于战略性 NAND 采购） | 第 26 章把 US$577M 视为第三方解读并标注 VERIFY。当作事实陈述属于偏向 Everpure 的过度表述 | 改写为分析师解读，并链接至第 26 章 | 已修复 |
| 41 | "VAST added GPU-equipped CNodes"（VAST 增加了配备 GPU 的 CNode）；"WEKA launched WEKApod 3, its first chassis-up hardware"（WEKA 推出 WEKApod 3，其首款从机箱做起的硬件） | CNode-X 只是已发布，尚未出货；WEKApod 3 于 2026 年秋季开始交付 | 改为"announced"（已发布），并注明交付时间 | 已修复 |
| 41 | "MLPerf absences"（MLPerf 缺席）及记分卡反证 | 陈述 Everpure 领先时未注明三家竞争对手缺席；缺少参与历史 | 补充"among entrants"（在参赛者中）及各厂商的历史 | 已修复 |
| 41 | 表 41.3：EXA"audited MLPerf v3.0 lead"（经审计的 MLPerf v3.0 领先） | MLPerf 由提交者之间同行评审，而非审计 | 改为"Peer-reviewed … among entrants"（经同行评审……在参赛者中） | 已修复 |
| 41 | NetApp AFX"GA timing [VERIFY]"（GA 时间） | AFX 基于 ONTAP 9.18.1/9.19.1 发货，且已有 AFX 2K；未找到 1K 的确切 GA 日期 | 单元格已细化并加 WWT 脚注；暂存已更新 | 已标记 |
| 41 | NVIDIA 参与 WEKA Series E；VAST Series D 有 NVIDIA 参与；Eos 48×AI400X2 约 4 TB/s；AMG 于 2025-11-18 GA | 已确认 | 无 | 已核实 |
| 42 | "VAST's own median … about 2:1 [VERIFY]"（VAST 自己的中位数……约 2:1） | 2026 年 1 月 Denworth 给出约 1,000 家客户的平均值 3.4:1、中位数 1.75:1（B&F） | 已替换；"不要这样说"已更正；VERIFY 已解决 | 已修复 |
| 42 | SyncEngine"[VERIFY scope/pricing]"（[VERIFY 范围/定价]） | 2025-08-21 发布；对 POSIX、S3 和 SaaS 数据源进行编目并同步；不向客户收费 | 该行已附来源重写；VERIFY 已解决 | 已修复 |
| 42 | Polaris"[VERIFY whether separately sold]"（[VERIFY 是否单独销售]）；被归入"not yet GA"（尚未 GA） | 2026-02-25 在 VAST Forward 上发布；基于 Kubernetes；不额外收费；可在 VAST 云部署中使用 | 该行及 Mermaid 子图标签已修正；时间线已更新 | 已修复 |
| 42 | KV 缓存一节遗漏 VUA | VAST 于 2025 年 4 月开源 VUA（第 32 章已列出）。遗漏它会低估 VAST 在 KV 方面的历史 | 已将 VUA 补充至正文、时间线以及第 43/44 章的对比表 | 已修复 |
| 42 | Series E：只写了预订额 | VAST 还宣称 2023 财年第三季度末 ARR 超过 US$200M（第 41 章 45.5× 倍数的依据）；Sacra 给出的 2025 年 1 月 US$200M 可能已过时 | 已补充，并附 ARR 与 CARR 区别的保留说明 | 已修复 |
| 42 | CARR"fiscal year ending January 2026 [VERIFY]"（截至 2026 年 1 月的财年） | 新闻稿写的是"exited fiscal year 2026"（FY2026 年末）；未说明月份 | 已改写；VERIFY 收窄至财年截止月份 | 已标记 |
| 42 | Rule of X 推断假定乘数为 2× | Bessemer 将乘数设定为 2–3×；分析师最高使用 3× | 补充 3× 情形（增长 66–73%） | 已修复 |
| 42 | xAI"Blocks & Files later reported …"（Blocks & Files 后来报道……）引用的是 2024 年 B&F 和 VAST 博客的脚注 | 引用错误；2025 年 10 月的 B&F 报道还提到 DDN 仍在供货 | 已重新引用并改写 | 已修复 |
| 42 | "Absent from MLPerf Storage v1.0–v3.0"（缺席 MLPerf Storage v1.0–v3.0）；"audited benchmarks"（经审计的基准测试） | VAST 从未在任何一轮（v0.5–v3.0）中提交（StorageReview） | 已更正；改为"peer-reviewed" | 已修复 |
| 42 | 关于 Denworth 角色的待解问题 | 依据的是单一媒体的推测，但他在 2026 年 1 月仍代表 VAST 向媒体做简报 | 表述已平衡；VERIFY 收窄 | 已修复 |
| 42 | 表 42.5 表注"EXA leads on … audited results"（EXA 在……经审计结果上领先） | 偏向 Everpure 的表述；遗漏了 VAST 在数据缩减上的领先 | 已重新平衡 | 已修复 |
| 42 | Series F 投资方、US$4B 预订额、228% Rule of X、自由现金流为正；CoreWeave US$1.17B；2025 年 11 月 Google Cloud 和 Azure 公告 | 已确认（VAST 新闻稿经 iTWire 转载；Reuters）。Azure GA 仍未确认 | 暂存已更新 | 已核实 / 已标记（Azure） |
| 42 | CNode-X"due later in 2026"（2026 年稍后推出） | 2026-02-25 与 Supermicro 联合发布；未找到出货日期。"sold first by … Cisco"（先由……Cisco 销售）的说法在我的检索中未得到佐证 | 保持原文 | 已标记 |
| 43 | "Stripe width under about a quarter of the cluster, so 16+4 implies 80+ servers"（条带宽度低于集群约四分之一，因此 16+4 意味着 80 台以上服务器） | WEKA 文档中没有这一规则（据检索）。文档要求条带 ≤ 故障域数量并保留备用余量，并给出 20 台服务器上 16+2 的示例；条带宽度为 3–16 个数据块（4.1 版文档）或总计 5–20（当前版本）；默认为 N+2 | 已重写 | 已修复 |
| 43 | 要点速览"first vendor to make KV-cache offload a product"（首家把 KV 缓存卸载做成产品的厂商） | "First"（首家）无法证明（VUA、DDN Infinia KV 缓存、LMCache） | 改为"Among the first … commercial product"（最早……的商业产品之一） | 已修复 |
| 43 | "It shipped a KV tier a year before NVIDIA standardised one"（它比 NVIDIA 将 KV 层标准化早一年交付了 KV 层） | 2025 年 3 月发布，2025 年 11 月 GA；STX 于 2026 年 3 月跟进，因此 GA 只领先了几个月，而非一年 | 已更正 | 已修复 |
| 43 | HPE 停止转售 | 缺少停止报价日期、VAR 渠道以及 WEKA 的回应 | 已补充 | 已修复 |
| 43 | Series E"US$100M primary and US$40M secondary by employees"（US$100M 新股，US$40M 员工老股转让） | WEKA 新闻稿只写了"primary and secondary"（新股和老股） | 保留，加 VERIFY 和来源；新增暂存条目 | 已标记 |
| 43 | 历史部分："raised US$275M in two rounds"（两轮融资共 US$275M），时间为 2020–2024 | 遗漏了 2022 年 1 月 US$73M 的一轮 | 改为"About US$348M in three rounds"（三轮共约 US$348M） | 已修复 |
| 43 | OCI 测试："42 GB per context, ~7,500 vs ~225 contexts"（每个上下文 42 GB，约 7,500 对约 225 个上下文） | 该测试使用的是 100K token 上下文，而非 128K | 已重新计算（约 33 GB，约 9,600 对约 290）；比值不变 | 已修复 |
| 43 | WEKApod 3 1.1 EB ⇒ 约 2.5:1 | 按原始容量计算正确；有报道按可用容量引用约 3:1 | 已加注（TechRadar） | 已修复 |
| 43 | MLPerf v0.5 参与情况（脚注引用的是一次"unofficial"（非官方）WEKA 运行） | WEKA 是 v0.5 五家官方提交者之一，另外还做了一次非官方的 AWS 测试；v2.0 缺席依据 StorageReview | v2.0 已附来源；删除暂存中 v1.0 的 VERIFY | 已修复 |
| 43 | "KV-cache losses should shrink now that PureKVA and audited MLPerf KV results exist"（既然已有 PureKVA 和经审计的 MLPerf KV 结果，KV 缓存方面的失单应会减少）；"supports Everpure's integrated thesis"（支持 Everpure 的一体化论点）；表 43.3 PureKVA"Oct 2026"；VAST"Azure listing"（Azure 上架） | 偏向 Everpure；PureKVA 只是已发布，未确认 GA（依据第 5a 部分审阅）；VAST Azure GA 未确认 | 已弱化、重新标注日期并重新平衡；"audited"→"peer-reviewed"（5 处） | 已修复 |
| 43 | NeuralMesh 6 GA / WEKApod 3 出货 | 截至 2026-11-01 未找到 GA 或出货公告 | 暂存已更新 | 已标记 |
| 44 | "VAST Data has also claimed Colossus …[^30]"（VAST Data 也宣称为 Colossus 供货……） | 用 DDN 自己的来源来引证 VAST 的声明 | 新增脚注（VAST 博客、B&F 2025 年 10 月） | 已修复 |
| 44 | "Tenancy is enforced at the access layer, not cryptographically [VERIFY: informal source]"（租户隔离在访问层实施，而非通过加密实现 [VERIFY: 非正式来源]） | 对竞争对手无依据的负面说法，且无脚注 | 替换为中性的尽职调查问题；暂存措辞已修改 | 已修复 |
| 44 | 基准测试一节从 v1.0/v2.0 开始 | DDN 是 v0.5 的官方提交者（2023 年） | 已附来源补充；标题和"不要这样说"已更新 | 已修复 |
| 44 | 要点速览"sat out MLPerf v3.0, where Everpure posted the top checkpoint result"（缺席 MLPerf v3.0，而 Everpure 在该轮取得了最高检查点成绩） | 在 DDN 的要点速览里为 Everpure 做宣传；且遗漏了 VAST 和 WEKA 同样缺席 | 已改写 | 已修复 |
| 44 | 表 44.2 VAST KV 层："CNode-X with NVIDIA context-memory support"（支持 NVIDIA 上下文内存的 CNode-X） | CNode-X 是用于向量搜索和 SQL 的 GPU 节点；KV 路径是 BlueField-4 CNode 加 VUA（第 42 章） | 已更正；PureKVA 重新标注日期 | 已修复 |
| 44 | Eos"delivery about 93% of datasheets"（实际交付约为数据表的 93%） | 93% 使用的是 4.3 TB/s；标称值为 4.0 TB/s（87%） | 改为"87–93%" | 已修复 |
| 44 | Blackstone 以 US$5B 估值投资 US$300M；"first institutional investor"（首家机构投资者）；B&F US$500M（2023）和 US$750M 估算（2024） | 经检索摘要确认；仍与 Forbes 的 US$400M/US$500M 相冲突 | 已在暂存中加注 | 已核实（二手来源） |
| 44 | Qwen3-32B 64 层 / 8 个 KV 头 / 头维度 128 | 与我记忆中的模型卡一致；huggingface.co 被屏蔽，因此未确认 | 保留 VERIFY | 已标记 |

## 未解决事项 / 分歧

- **IDC 2Q26 厂商份额（第 40 章）。** Huawei 11.3%、NetApp 9.6%、Everpure 8.1% 和 HPE 6.8% 无法再次确认：idc.com 被屏蔽，且表格为图片。Dell 23.8% 及总数已确认。应由有 IDC 访问权限的人核对。
- **VAST 财年截止月份（第 40、41、42 章）。** 新闻稿只写了"exited fiscal year 2026"（FY2026 年末）。
- **VAST Azure Native ISV Service GA（第 42、43 章）。** 未找到 GA 确认。VAST 自己的新闻稿页面似乎包含未填写的占位符，因此其"now available"（现已可用）措辞不可靠。
- **CNode-X 出货状态及 Cisco 是否销售（第 42 章表 42.1）。** 只找到了 Supermicro 的发布信息。
- **WEKA Series E 新股/老股拆分（第 43 章正文及 `data/ch43_funding.csv`）。** CSV 仍显示 US$40M 老股转让。我未修改图表，因为该拆分看似合理但未经确认。
- **WEKApod 3 每机架 10.2 TB/s / 210M IOPS，以及 NeuralMesh 6 GA（第 43 章）。** 均未确认。
- **DDN 收入基数（第 41、44 章）。** Forbes 给出 US$400M/US$500M；B&F 给出 US$500M（2023）和 US$750M 估算（2024）。二者不可能同时正确，而第 41 章的 12.5× 倍数使用的是 Forbes 的数字。我对以 Forbes 数字为主略有异议，但两方面都没有证据。
- **Blackstone–DDN 日期。** 第 41 章写 2025-01-09，第 44 章写 2025-01-08。Business Wire 的 ID 显示为 1 月 8 日，媒体报道则为 1 月 9 日。无关紧要；保持原样。
- **VAST 写入确认机制（第 42 章）。** "Mirrored into SCM on two enclosures"（镜像写入两个机箱的 SCM）与第 16 章一致，但本会话中我无法对照 VAST 文档确认确切的副本数量。
