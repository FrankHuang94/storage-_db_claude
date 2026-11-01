### 第 4 部分 — Everpure

第 4 部分的卡片围绕 Everpure 本身：公司历史、Purity 与 DirectFlash、各产品线、平台以及财务。参加任何内部会议之前，这些内容都应烂熟于心。

| 章节 | 卡片数（L1 / L2） | 卡片编号 |
|---|---|---|
| [第 25 章](../04-everpure/25-company-history-and-strategy.md) | 6 (3 / 3) | Q127–Q132 |
| [第 26 章](../04-everpure/26-purity-and-directflash.md) | 7 (3 / 4) | Q133–Q139 |
| [第 27 章](../04-everpure/27-flasharray-and-flashblade.md) | 6 (3 / 3) | Q140–Q145 |
| [第 28 章](../04-everpure/28-platform-and-software.md) | 6 (3 / 3) | Q146–Q151 |
| [第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md) | 6 (2 / 4) | Q152–Q157 |

*图 59.12 — 第 4 部分 — Everpure：5 章共 31 张卡片（14 张 L1、17 张 L2），编号 Q127–Q157；可按卡片编号分章记录答错的题目。*

<details>
<summary><strong>Q127.</strong> Pure Storage 在 2009 年创立时的核心洞见是什么？</summary>

消费级闪存加上激进的数据缩减，可以让每可用 TB 的成本与磁盘持平。（[第 25 章](../04-everpure/25-company-history-and-strategy.md)）

</details>

<details>
<summary><strong>Q128.</strong> FlashArray 何时正式发布（GA）？Pure Storage 何时 IPO？</summary>

FlashArray 于 2012 年 5 月正式发布（GA）。IPO 随后于 2015 年 10 月完成，发行价每股 $17，募资 $425M，在 NYSE 上市，代码 PSTG。（[第 25 章](../04-everpure/25-company-history-and-strategy.md)）

</details>

<details>
<summary><strong>Q129.</strong> (L2) 为什么说 Everpure 持久的护城河是"一种商业模式，而不是一台设备"？</summary>

Forever Flash（2014 年）和 Evergreen（2015 年）把控制器升级变成了订阅。FY2026 订阅 ARR 为 $1.92B。（[第 25 章](../04-everpure/25-company-history-and-strategy.md)）

</details>

<details>
<summary><strong>Q130.</strong> (L2) 如何概括 Everpure 的并购记录？</summary>

规模小、以获取能力为导向：StorReduce、Compuverde、Portworx 和 1touch 的已披露对价合计约 $0.6B，低于 FY2026 的自由现金流 $616M。StorReduce 的产品后来被悄然下架。（[第 25 章](../04-everpure/25-company-history-and-strategy.md)）

</details>

<details>
<summary><strong>Q131.</strong> (L2) 2026 年 2 月更名为 Everpure 意在主张什么？</summary>

主张数据平台级别的估值（NYSE: P，原 PSTG），而收入目前仍主要来自阵列及其附带订阅：这是一种主张，尚未成为结果。（[第 25 章](../04-everpure/25-company-history-and-strategy.md)）

</details>

<details>
<summary><strong>Q132.</strong> Everpure 的 FY2027 收入指引是多少？</summary>

$5.03–5.07B，增长约 +38%，由 2026 年 2 月最初给出的 $4.3–4.4B 指引上调而来。（[第 25 章](../04-everpure/25-company-history-and-strategy.md)）

</details>

<details>
<summary><strong>Q133.</strong> Purity 是什么类型的操作系统？</summary>

一种日志结构、类数据库的存储操作系统。它以追加代替覆盖写，在线完成数据缩减，并把所有映射关系保存在键值元数据存储中。（[第 26 章](../04-everpure/26-purity-and-directflash.md)）

</details>

<details>
<summary><strong>Q134.</strong> (L2) DirectFlash 去掉了什么？换来了什么？</summary>

去掉了 SSD 自己的"大脑"。Purity 在裸 NAND 模块之上运行一个全局 FTL，因此整台阵列只有一个日志、一个垃圾回收器和一个备用闪存池，而不是每块盘各一套。（[第 26 章](../04-everpure/26-purity-and-directflash.md)）

</details>

<details>
<summary><strong>Q135.</strong> (L2) 为什么 DirectFlash Module 的容量比 SSD 更大？</summary>

没有了每块盘的映射 DRAM 和隐藏的备用空间（标准 SSD 中约为用户容量的 ~15–37%），模块容量可以增长得更快。DFM 已达到 300 TB，而当时出货的最大标准 SSD 为 245.76 TB。（[第 26 章](../04-everpure/26-purity-and-directflash.md)）

</details>

<details>
<summary><strong>Q136.</strong> (L2) 用半导体类比来描述 DirectFlash。</summary>

这相当于一家无晶圆厂（fabless）式的玩家完成了"集成内存控制器"这一步。收益是全局调度；代价是每一代 NAND 都要自己做认证，而 NAND 又是从同时销售成品 SSD 的 IDM 那里采购的。（[第 26 章](../04-everpure/26-purity-and-directflash.md)）

</details>

<details>
<summary><strong>Q137.</strong> (L2) DirectFlash 护城河面临的主要威胁是什么？</summary>

灵活数据放置（Flexible Data Placement，FDP）SSD——它让通用硬盘也能按数据生命周期分开存放——以及超大规模云厂商的自研设计。（[第 26 章](../04-everpure/26-purity-and-directflash.md)）

</details>

<details>
<summary><strong>Q138.</strong> 什么是 RAID-HA？</summary>

Purity 跨 DirectFlash Module 的双校验保护机制。（[第 26 章](../04-everpure/26-purity-and-directflash.md)）

</details>

<details>
<summary><strong>Q139.</strong> 什么是 NAND 认证（NAND qualification）？</summary>

对新一代 NAND 裸片进行特性表征，使固件或软件能够可靠地驱动它；对于 DirectFlash，这项工作由 Everpure 自己完成。（[第 26 章](../04-everpure/26-purity-and-directflash.md)）

</details>

<details>
<summary><strong>Q140.</strong> 将 FlashArray 和 FlashBlade 与各自的操作系统和架构对应起来。</summary>

FlashArray 运行 Purity//FA，采用双控制器纵向扩展（scale-up）设计，以块存储为主。FlashBlade 运行 Purity//FB，基于横向扩展（scale-out）刀片，面向文件和对象存储。（[第 27 章](../04-everpure/27-flasharray-and-flashblade.md)）

</details>

<details>
<summary><strong>Q141.</strong> Everpure 哪些型号属于性能层，哪些属于容量层？</summary>

FlashArray//XL、//X 和 //ST 是 TLC 性能层；//C 和 //E 是 QLC 容量层。FlashBlade//S 为性能型，FlashBlade//E 为容量型。（[第 27 章](../04-everpure/27-flasharray-and-flashblade.md)）

</details>

<details>
<summary><strong>Q142.</strong> (L2) FlashBlade//EXA 如何工作？</summary>

运行在 DFM 刀片上的 Purity//FB 元数据核心，与独立的第三方 Linux/NVMe 数据节点并列部署。客户端通过 pNFS 从核心获取文件布局，然后直接与数据节点之间收发数据。（[第 27 章](../04-everpure/27-flasharray-and-flashblade.md)）

</details>

<details>
<summary><strong>Q143.</strong> (L2) 应如何描述 EXA 的 MLPerf Storage v3.0 成绩？</summary>

应表述为参赛者中的最高成绩：51 台主机上检查点写入 877.5 GiB/s（读取较低，为 588 GiB/s）、KV 缓存读取 1,623.4 GiB/s，这一领先部分来自规模。VAST、WEKA、DDN、Dell、IBM 和 NetApp 均未提交，因此"第一"指的是在参赛系统中排名第一。（[第 27 章](../04-everpure/27-flasharray-and-flashblade.md)）

</details>

<details>
<summary><strong>Q144.</strong> (L2) Everpure 在 NVIDIA 认证上的缺口在哪里？</summary>

FlashBlade//S 已获得 SuperPOD 和 NCP 高性能存储认证。对于 EXA，Everpure 于 2026 年 3 月宣布通过 NVIDIA-Certified Storage 验证，NCP 认证仍待完成。（[第 27 章](../04-everpure/27-flasharray-and-flashblade.md)）

</details>

<details>
<summary><strong>Q145.</strong> 什么是 R 代（R-generation）？</summary>

FlashArray 的控制器换代，如 R4 或 R5，客户可以原地升级。（[第 27 章](../04-everpure/27-flasharray-and-flashblade.md)）

</details>

<details>
<summary><strong>Q146.</strong> (L2) Everpure 的转换成本越来越多地体现在哪里？</summary>

体现在控制平面：Fusion 预设和自动化流程的生命周期比任何一次硬件换代都长。到 Q1 FY27，使用 Fusion 的客户超过 1,200 家，较上一季度翻番，但仍不到客户总数的十分之一。（[第 28 章](../04-everpure/28-platform-and-software.md)）

</details>

<details>
<summary><strong>Q147.</strong> Evergreen//Forever、//Flex 和 //One 分别是什么？</summary>

分别是自有、自有按用量付费、以及即服务（as-a-service）三种订阅层级。（[第 28 章](../04-everpure/28-platform-and-software.md)）

</details>

<details>
<summary><strong>Q148.</strong> 什么是 Fusion 预设（preset）？</summary>

一种覆盖整个设备群的策略模板，自动化流程按名称调用它来配置存储。（[第 28 章](../04-everpure/28-platform-and-software.md)）

</details>

<details>
<summary><strong>Q149.</strong> (L2) 收购 1touch 押注的是什么？</summary>

押注存储元数据加上内容分类能够成为一款治理与 AI 就绪（AI-readiness）产品。这笔 $125.0M 的交易（2026-05-07 完成）使 Everpure 进入了由数据目录和数据安全厂商主导的品类。（[第 28 章](../04-everpure/28-platform-and-software.md)）

</details>

<details>
<summary><strong>Q150.</strong> 什么是 Portworx？</summary>

可在任意基础设施上运行的 Kubernetes 数据服务，于 2020 年以 $352.9M 加留任激励收购，是 Everpure 迄今最大的一笔交易。（[第 28 章](../04-everpure/28-platform-and-software.md)）

</details>

<details>
<summary><strong>Q151.</strong> (L2) 各家相互竞争的"数据平台"说法实际有何不同？</summary>

Dell、NetApp、HPE、VAST 和 Everpure 的说法如出一辙。差别在于：底层是什么（单一操作系统还是产品组合）、能否覆盖厂商自有硬件之外的环境，以及客户是否真的购买上层产品。（[第 28 章](../04-everpure/28-platform-and-software.md)）

</details>

<details>
<summary><strong>Q152.</strong> (L2) Everpure 的"两条收入线、三项业务"指什么？</summary>

NAND 计入 Everpure 账面的阵列业务、按期确认收入的 Evergreen 订阅，以及由客户自购 NAND 的超大规模 DirectFlash 授权业务。三者的利润率结构各不相同。（[第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md)）

</details>

<details>
<summary><strong>Q153.</strong> (L2) 超大规模云厂商模式卖的是什么？</summary>

卖的是闪存管理 IP，而不是设备。Meta 在 FY26 已超过 2 EB（原计划为 1–2 EB），第二家前五大超大规模云厂商于 2026-08-10 签约，收入自 FY28 起确认。（[第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md)）

</details>

<details>
<summary><strong>Q154.</strong> Q2 FY27 的订阅 ARR 和 RPO 分别是多少？</summary>

订阅 ARR 为 $2.13B（+20%），RPO 为 $4.1B（+44%）。（[第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md)）

</details>

<details>
<summary><strong>Q155.</strong> 什么是 NAND 成本传导（NAND pass-through）？</summary>

NAND 成本的变化以多快的速度传导到客户价格上。（[第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md)）

</details>

<details>
<summary><strong>Q156.</strong> (L2) 为什么 Everpure 的产品毛利率在 2026 年下降？</summary>

NAND 价格飙升使非 GAAP 产品毛利率由 Q3 FY26 的 72.9% 降至 Q2 FY27 的 66.2%，而订阅毛利率维持在约 75%。（[第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md)）

</details>

<details>
<summary><strong>Q157.</strong> (L2) 为什么 Q2 FY27 的自由现金流为负？</summary>

原因是战略性采购 NAND 和零部件：自由现金流为 –$238M，经营现金流为 –$136M。（[第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md)）

</details>

### 第 5 部分 — AI 存储

第 5 部分的卡片涵盖各类 AI 工作负载（数据管道、训练、推理、RAG、智能体）及其周边力量：NVIDIA、新兴 GPU 云（neocloud）、超大规模云厂商、基准测试和电力。

| 章节 | 卡片数（L1 / L2） | 卡片编号 |
|---|---|---|
| [第 30 章](../05-ai-storage/30-ai-data-pipeline.md) | 5 (3 / 2) | Q158–Q162 |
| [第 31 章](../05-ai-storage/31-training-storage.md) | 6 (2 / 4) | Q163–Q168 |
| [第 32 章](../05-ai-storage/32-inference-and-kv-cache.md) | 7 (3 / 4) | Q169–Q175 |
| [第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md) | 5 (2 / 3) | Q176–Q180 |
| [第 34 章](../05-ai-storage/34-nvidia-ecosystem.md) | 5 (2 / 3) | Q181–Q185 |
| [第 35 章](../05-ai-storage/35-ai-factories-and-neoclouds.md) | 4 (1 / 3) | Q186–Q189 |
| [第 36 章](../05-ai-storage/36-hyperscaler-ai-storage.md) | 4 (1 / 3) | Q190–Q193 |
| [第 37 章](../05-ai-storage/37-reading-benchmarks.md) | 5 (2 / 3) | Q194–Q198 |
| [第 38 章](../05-ai-storage/38-power-and-density.md) | 5 (1 / 4) | Q199–Q203 |
| [第 39 章](../05-ai-storage/39-agentic-ai-and-data-intelligence.md) | 4 (2 / 2) | Q204–Q207 |

*图 59.13 — 第 5 部分 — AI 存储：10 章共 50 张卡片（19 张 L1、31 张 L2），编号 Q158–Q207；可按卡片编号分章记录答错的题目。*

<details>
<summary><strong>Q158.</strong> "AI 存储"实际涵盖多少种工作负载？</summary>

至少八种。数据摄取以写为主、受成本约束；训练读取受吞吐量约束；检查点保存是写入突发；推理、RAG 和智能体则是受延迟约束的小 I/O。（[第 30 章](../05-ai-storage/30-ai-data-pipeline.md)）

</details>

<details>
<summary><strong>Q159.</strong> (L2) 在 AI 管道中，数据如何"先缩小、再变大"？</summary>

超过 10 PB 的网页抓取数据经过滤后变成数十 TB 的训练文本，最终得到不到 1 TB 的权重。随后，管道又会产生多 TB 级的检查点、KV 缓存、嵌入向量和日志。（[第 30 章](../05-ai-storage/30-ai-data-pipeline.md)）

</details>

<details>
<summary><strong>Q160.</strong> (L2) 在 AI 管道中，容量和性能分别落在哪里？</summary>

容量落在对象存储——这是最便宜、所有工具都支持的持久 TB。性能落在紧邻 GPU 的文件存储和闪存，因为训练和检查点代码需要 POSIX 路径和 RDMA 带宽。（[第 30 章](../05-ai-storage/30-ai-data-pipeline.md)）

</details>

<details>
<summary><strong>Q161.</strong> 什么是数据引力（data gravity）？</summary>

应用和支出被吸引到大规模数据已经所在之处的那股力量。（[第 30 章](../05-ai-storage/30-ai-data-pipeline.md)）

</details>

<details>
<summary><strong>Q162.</strong> 对比数据湖与热层（hot tier）。</summary>

数据湖是低成本、通常基于对象的存储，用于存放原始数据和整理后的数据；热层则是为 GPU 供数的高性能文件或闪存层。（[第 30 章](../05-ai-storage/30-ai-data-pipeline.md)）

</details>

<details>
<summary><strong>Q163.</strong> (L2) 为什么决定存储规格的是检查点，而不是训练数据？</summary>

一个 405B 模型在 16,384 块 GPU 上读取文本 token 的速度约为 ~11 MB/s，但要在 60 秒内写出约 ~6.5 TB 的训练状态，则需要约 ~108 GB/s。（[第 31 章](../05-ai-storage/31-training-storage.md)）

</details>

<details>
<summary><strong>Q164.</strong> (L2) 为什么检查点要按每参数 14–16 字节来估算，而不是 2 字节？</summary>

混合精度 Adam 在 bf16 权重之外，还保留 fp32 主权重和两个 fp32 优化器动量。权重本身只占所保存内容的约七分之一。（[第 31 章](../05-ai-storage/31-training-storage.md)）

</details>

<details>
<summary><strong>Q165.</strong> (L2) 故障如何决定检查点频率？</summary>

Meta 的 Llama 3 训练在 54 天内遭遇 419 次意外中断，约每 3.1 小时一次。在同步保存的情况下，即使采用最优间隔，仍会浪费约 10% 的集群算力。（[第 31 章](../05-ai-storage/31-training-storage.md)）

</details>

<details>
<summary><strong>Q166.</strong> (L2) 异步检查点改变了什么？</summary>

它把峰值带宽问题变成了持续带宽问题：GPU 在数秒内把状态转储到主机 DRAM 或本地 NVMe，再在后台慢慢写出。PyTorch DCP 把一个 7B 模型的检查点停机时间从 148.8 s 缩短到 6.3 s。（[第 31 章](../05-ai-storage/31-training-storage.md)）

</details>

<details>
<summary><strong>Q167.</strong> 什么是恢复风暴（restore storm）？</summary>

故障发生后，所有 GPU 同时读取最新检查点。在大规模场景下，重启时间的代价高于保存时间。（[第 31 章](../05-ai-storage/31-training-storage.md)）

</details>

<details>
<summary><strong>Q168.</strong> 什么是 Young 公式？</summary>

最优检查点间隔：√(2 × 保存开销 × MTBF)。（[第 31 章](../05-ai-storage/31-training-storage.md)）

</details>

