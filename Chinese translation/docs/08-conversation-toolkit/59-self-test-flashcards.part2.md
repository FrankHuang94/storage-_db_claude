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

<details>
<summary><strong>Q169.</strong> 什么是 KV 缓存？它有多大？</summary>

一段对话的工作内存：此前每个 token 的注意力键（key）和值（value）。一个 Llama 3.1 70B 级别的模型每个 token 需要 320 KiB，一个 128K token 的会话约需 43 GB。（[第 32 章](../05-ai-storage/32-inference-and-kv-cache.md)）

</details>

<details>
<summary><strong>Q170.</strong> (L2) 为什么存储只能存放当前不在解码中的 KV？</summary>

预填充（prefill）受计算约束，而解码（decode）受内存约束，每生成一个新 token 都要重读整个缓存，因此活跃的 KV 必须驻留在 HBM 中。（[第 32 章](../05-ai-storage/32-inference-and-kv-cache.md)）

</details>

<details>
<summary><strong>Q171.</strong> (L2) 解释 KV 缓存"重算还是拉取"的权衡。</summary>

重建一个 128K 上下文需要一台 8-GPU 节点约 ~2.6 s 的计算；而通过 8 × 400 Gb/s 网卡拉取只需约 ~0.13 s。当每块 GPU 的带宽超过大约 2–5 GB/s 时，拉取更划算，因此命中率和带宽决定了经济性。（[第 32 章](../05-ai-storage/32-inference-and-kv-cache.md)）

</details>

<details>
<summary><strong>Q172.</strong> KVBM 有哪些层级？</summary>

Dynamo 的 KV Block Manager 定义了从 G1（HBM）到 G4（网络存储）的层级；BlueField-4 STX/CMX 又增加了一个 pod 级的"G3.5"闪存层。（[第 32 章](../05-ai-storage/32-inference-and-kv-cache.md)）

</details>

<details>
<summary><strong>Q173.</strong> 定义 TTFT 和前缀缓存（prefix caching）。</summary>

TTFT 即首 token 延迟。前缀缓存对相同的开头 token 复用已存储的 KV，从而无需重新计算。（[第 32 章](../05-ai-storage/32-inference-and-kv-cache.md)）

</details>

<details>
<summary><strong>Q174.</strong> (L2) 应如何看待"首 token 延迟快 20×"之类的说法？</summary>

要打折扣。Everpure、WEKA、DDN 和 HPE 大多以无缓存为基线进行比较；MLPerf Storage v3.0 才加入了首个中立的 KV 缓存测试。（[第 32 章](../05-ai-storage/32-inference-and-kv-cache.md)）

</details>

<details>
<summary><strong>Q175.</strong> (L2) 为什么 GQA 和 MLA 对存储容量规划很重要？</summary>

它们缩小了每个 token 的 KV：DeepSeek-V3 的 MLA 每个 token 约需 ~69 KiB，而 Llama 3.1 70B 需要 320 KiB。（[第 32 章](../05-ai-storage/32-inference-and-kv-cache.md)）

</details>

<details>
<summary><strong>Q176.</strong> RAG 如何工作？</summary>

文档被切分成块并嵌入为向量。提问时，检索出最接近的块并粘贴到提示词中。（[第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md)）

</details>

<details>
<summary><strong>Q177.</strong> 什么是嵌入向量和 ANN 索引？</summary>

嵌入向量是表示一个文本块语义的定长向量；ANN 索引（IVF、HNSW、DiskANN）无需扫描每个向量即可找到近似最近邻。（[第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md)）

</details>

<details>
<summary><strong>Q178.</strong> (L2) 为什么十亿级向量索引正在转向闪存？</summary>

十亿个 1,024 维 fp32 向量的原始大小约为 ~4.1 TB。全部放在 DRAM 中，介质成本约为 DiskANN 这类驻留 SSD 的设计的 ~16×（每个副本约 ~US$66k 对 ~US$4k）。（[第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md)）

</details>

<details>
<summary><strong>Q179.</strong> (L2) 对比 Parquet、Lance 和 Iceberg。</summary>

Parquet 为扫描而设计；Lance 兼顾扫描和随机行读取；Iceberg 则在对象存储中的普通文件之上增加了事务和目录（catalog）。（[第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md)）

</details>

<details>
<summary><strong>Q180.</strong> (L2) 在 RAG 技术栈中，价值归于何处？</summary>

归于掌握元数据和查询的一方：目录与治理具有黏性，字节则可替换。例外是那些不能离开本地机房的数据。（[第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md)）

</details>

<details>
<summary><strong>Q181.</strong> 说出 NVIDIA-Certified Storage 的三个级别。</summary>

Foundation（最多 128 块模拟 GPU）、Enterprise（约 1,000 块，该数字尚未确认）和 NCP（最多 10,000 块）。（[第 34 章](../05-ai-storage/34-nvidia-ecosystem.md)）

</details>

<details>
<summary><strong>Q182.</strong> 什么是 SuperPOD 可扩展单元（scalable unit）？</summary>

DGX SuperPOD 的 32 节点构建模块，在 B200 设计中为 256 块 GPU。（[第 34 章](../05-ai-storage/34-nvidia-ecosystem.md)）

</details>

<details>
<summary><strong>Q183.</strong> (L2) 为什么 NVIDIA 认证设定的是底线，而不是对厂商排名？</summary>

它证明的是互操作性和最低吞吐量；SuperPOD B200 的"enhanced"级别要求每块 GPU 的读取带宽不到 0.5 GB/s。它对价格、数据缩减、运维或故障行为只字未提。（[第 34 章](../05-ai-storage/34-nvidia-ecosystem.md)）

</details>

<details>
<summary><strong>Q184.</strong> (L2) 为什么说 NVIDIA 是一个存在利益冲突的"造王者"？</summary>

它掌管着认证厂商名单，却同时持有 VAST 和 WEKA 的股权，而它自己的集群运行在 DDN 上。目前没有报道显示 Everpure 与 NVIDIA 存在股权关系。（[第 34 章](../05-ai-storage/34-nvidia-ecosystem.md)）

</details>

<details>
<summary><strong>Q185.</strong> (L2) NVIDIA 如何进入存储设备内部？</summary>

AI Data Platform（2025 年）把 GPU 和检索软件放进了存储内部；BlueField-4 STX 和 CMX（2026 年）在 NVIDIA 芯片上将 KV 缓存层标准化，并有 12 家存储厂商作为联合设计伙伴。（[第 34 章](../05-ai-storage/34-nvidia-ecosystem.md)）

</details>

<details>
<summary><strong>Q186.</strong> 什么是新兴 GPU 云（neocloud）？</summary>

专注 GPU 的云服务商，向 AI 实验室、企业乃至超大规模云厂商出租加速器算力。（[第 35 章](../05-ai-storage/35-ai-factories-and-neoclouds.md)）

</details>

<details>
<summary><strong>Q187.</strong> (L2) neocloud 采购存储的方式与企业有何不同？</summary>

它把存储当作要转售的产品来采购：必须支持多租户、通过 API 配置、按 $/GB-月计量，并且要在自身成本之上留出利润。（[第 35 章](../05-ai-storage/35-ai-factories-and-neoclouds.md)）

</details>

<details>
<summary><strong>Q188.</strong> (L2) 为什么 neocloud 把可靠性看得比价格更重？</summary>

已披露的最大一笔存储合同每年约占其客户资本开支的 1%，存储约占一排 GPU 机柜功耗的 ~4%，但它却可能让 100% 的 GPU 闲置。可靠性、部署速度和与 NVIDIA 的契合度才是决定因素。（[第 35 章](../05-ai-storage/35-ai-factories-and-neoclouds.md)）

</details>

<details>
<summary><strong>Q189.</strong> (L2) Everpure 在 neocloud 市场处于什么位置？</summary>

挑战者：持有 CoreWeave 股权，拿下了一些小规模的 FlashBlade//EXA 订单，消费模式也契合，但缺少大型锚定客户。VAST 凭借与 CoreWeave 的 US$1.17B 协议，是公认的在位者。（[第 35 章](../05-ai-storage/35-ai-factories-and-neoclouds.md)）

</details>

<details>
<summary><strong>Q190.</strong> (L2) Colossus、Tectonic 和 S3 有什么共同点？</summary>

智能客户端库、建立在可扩展数据库上的元数据（Colossus 用 Bigtable，Tectonic 用 ZippyDB），以及简单的数据服务器，数据路径中没有控制器。超大规模云厂商自身的工作负载不采购阵列。（[第 36 章](../05-ai-storage/36-hyperscaler-ai-storage.md)）

</details>

<details>
<summary><strong>Q191.</strong> (L2) 超大规模云厂商从存储厂商那里买什么？</summary>

买组件和 IP，而不是系统。Meta 和第二家前五大超大规模云厂商在自购 NAND 的同时获得了 DirectFlash 授权；云服务则为租户转售合作伙伴产品，例如 Google 上的 DDN Lustre。（[第 36 章](../05-ai-storage/36-hyperscaler-ai-storage.md)）

</details>

<details>
<summary><strong>Q192.</strong> 什么是智能客户端（smart client）？</summary>

自行完成数据放置和编码的客户端库，因此数据路径中不需要控制器。（[第 36 章](../05-ai-storage/36-hyperscaler-ai-storage.md)）

</details>

<details>
<summary><strong>Q193.</strong> (L2) 为什么 AI 推动超大规模云厂商从磁盘转向闪存？</summary>

GPU 集群对每 TB 带宽的需求高得多，而磁盘的每 TB 带宽随容量增长而下降：一块 250 MB/s 的硬盘在 20 TB 时为每 TB 12.5 MB/s，在 30 TB 时只有 8.3。（[第 36 章](../05-ai-storage/36-hyperscaler-ai-storage.md)）

</details>

<details>
<summary><strong>Q194.</strong> (L2) 存储基准测试主要衡量的是什么？</summary>

主要衡量提交了多少硬件。横向扩展系统本来就能扩展，所以应按买方所需容量点，除以机架单元、千瓦或美元来比较。（[第 37 章](../05-ai-storage/37-reading-benchmarks.md)）

</details>

<details>
<summary><strong>Q195.</strong> (L2) MLPerf Storage 在没有真实 GPU 的情况下如何计分？</summary>

模拟加速器通过休眠来"计算"，得分是存储能让多少个模拟加速器保持在利用率阈值之上（v3.0 中 U-Net 为 90%）。因此不同版本之间的结果不可比较。（[第 37 章](../05-ai-storage/37-reading-benchmarks.md)）

</details>

<details>
<summary><strong>Q196.</strong> 什么是"英雄配置"（hero configuration）？</summary>

为赢得头条而配置、而非对应真实采购的系统。（[第 37 章](../05-ai-storage/37-reading-benchmarks.md)）

</details>

<details>
<summary><strong>Q197.</strong> MLPerf Storage 中的加速器利用率（AU）是什么？</summary>

模拟加速器处于计算状态（而非等待数据）的时间占比。（[第 37 章](../05-ai-storage/37-reading-benchmarks.md)）

</details>

<details>
<summary><strong>Q198.</strong> (L2) 为什么说 MLPerf Storage v3.0 中的"缺席"本身就是数据？</summary>

VAST、WEKA 和 DDN 缺席了 2026 年 9 月这一轮（参与机构 19 家，低于此前的 26 家），尽管 DDN 和 WEKA 参加过更早的轮次。Everpure 的第一名成绩是真实的，但取得于最强对手缺席的赛场。（[第 37 章](../05-ai-storage/37-reading-benchmarks.md)）

</details>

<details>
<summary><strong>Q199.</strong> (L2) 为什么在 AI 数据中心中，存储的每一瓦都具有战略意义？</summary>

站点受限于电力而非芯片：电网接入容量决定了 GPU 的上限，因此存储每用掉一瓦，就少一瓦可以驱动 GPU。（[第 38 章](../05-ai-storage/38-power-and-density.md)）

</details>

<details>
<summary><strong>Q200.</strong> (L2) QLC 闪存在功耗上胜过磁盘吗？</summary>

在单盘层面，每瓦容量约为 2×（~8.2 对 ~4.4 TB/W）。在系统层面则取决于盘容量和机箱：一台 VAST DBox（~1.9 TB/W，不含 CNode）仅略胜于一台 102 盘位磁盘 JBOD（~1.7）。（[第 38 章](../05-ai-storage/38-power-and-density.md)）

</details>

<details>
<summary><strong>Q201.</strong> (L2) 节省的电费能抵消闪存溢价吗？</summary>

按电网电价算不能。按第 4 章的输入参数，100 PB 用 QLC 存放五年可节省约 ~1.23 GWh（~$170K），而介质溢价为 $8–37M；按指数价格计算溢价更高。当必须满足每 TB 带宽要求，或能以超大规模云厂商的成本采购 NAND 时，闪存才胜出；把省下的电力转给 GPU 有帮助，但仅凭这一点很少能弥合差距。（[第 38 章](../05-ai-storage/38-power-and-density.md)）

</details>

<details>
<summary><strong>Q202.</strong> (L2) 在物理层面，闪存在哪方面明显拉开与磁盘的差距？</summary>

密度：一个机柜的 245 TB QLC 盘可容纳约 ~177 PB，而 44 TB 磁盘只有约 ~33 PB；但功耗为约 ~32 kW 对 ~11 kW。（[第 38 章](../05-ai-storage/38-power-and-density.md)）

</details>

<details>
<summary><strong>Q203.</strong> 什么是 GB/s per kW？</summary>

每千瓦带宽，AI 时代的存储效率指标。（[第 38 章](../05-ai-storage/38-power-and-density.md)）

</details>

<details>
<summary><strong>Q204.</strong> 什么是 MCP？</summary>

Model Context Protocol（模型上下文协议），于 2024 年 11 月开源，2025 年 12 月移交给 Linux Foundation 旗下的基金，届时已有超过 10,000 个服务器。它规范了智能体调用工具的方式；大批量数据仍通过 S3、NFS 和 SQL 传输。（[第 39 章](../05-ai-storage/39-agentic-ai-and-data-intelligence.md)）

</details>

<details>
<summary><strong>Q205.</strong> (L2) 智能体如何改变存储访问模式？</summary>

一个问题会扇出为数十次工具调用和数百次小读取，每次都需要一次委托授权决策和一行日志；在算例中，5,000 名用户的部署约需每秒 ~280 次决策。（[第 39 章](../05-ai-storage/39-agentic-ai-and-data-intelligence.md)）

</details>

<details>
<summary><strong>Q206.</strong> (L2) 数据智能领域的战略问题是什么？</summary>

中立性。存储厂商能看到每一次写入，但数据与安全厂商能看到所有厂商的存储，并且掌握着买方；存储厂商只有覆盖不在自家阵列上的数据，才能胜出。（[第 39 章](../05-ai-storage/39-agentic-ai-and-data-intelligence.md)）

</details>

<details>
<summary><strong>Q207.</strong> 什么是"困惑的代理人"（confused deputy）？</summary>

一种安全缺陷：拥有特权的服务被诱骗，替一个本不具备该权限的调用者行使权限；当智能体代表用户行事时，这是一项核心风险。（[第 39 章](../05-ai-storage/39-agentic-ai-and-data-intelligence.md)）

</details>

### 第 6 部分 — 行业与竞争

第 6 部分的卡片涵盖市场格局和每一个主要竞争对手。大多数答案都带有*公司自述*或*媒体报道*的限定语；记数字时要连同限定语一起记住。

| 章节 | 卡片数（L1 / L2） | 卡片编号 |
|---|---|---|
| [第 40 章](../06-industry-and-competition/40-market-structure.md) | 5 (3 / 2) | Q208–Q212 |
| [第 41 章](../06-industry-and-competition/41-why-ai-native-vendors-won.md) | 5 (2 / 3) | Q213–Q217 |
| [第 42 章](../06-industry-and-competition/42-vast-data.md) | 5 (2 / 3) | Q218–Q222 |
| [第 43 章](../06-industry-and-competition/43-weka.md) | 4 (1 / 3) | Q223–Q226 |
| [第 44 章](../06-industry-and-competition/44-ddn.md) | 4 (2 / 2) | Q227–Q230 |
| [第 45 章](../06-industry-and-competition/45-head-to-head.md) | 3 (0 / 3) | Q231–Q233 |
| [第 46 章](../06-industry-and-competition/46-incumbents.md) | 3 (1 / 2) | Q234–Q236 |
| [第 47 章](../06-industry-and-competition/47-other-challengers.md) | 3 (1 / 2) | Q237–Q239 |
| [第 48 章](../06-industry-and-competition/48-media-suppliers-and-nand-cycle.md) | 5 (2 / 3) | Q240–Q244 |
| [第 49 章](../06-industry-and-competition/49-competitive-matrices.md) | 2 (1 / 1) | Q245–Q246 |
| [第 50 章](../06-industry-and-competition/50-diligence-framework.md) | 3 (1 / 2) | Q247–Q249 |

*图 59.14 — 第 6 部分 — 行业与竞争：11 章共 42 张卡片（16 张 L1、26 张 L2），编号 Q208–Q249；可按卡片编号分章记录答错的题目。*

<details>
<summary><strong>Q208.</strong> IDC 的外部企业存储跟踪报告衡量的是什么？</summary>

以独立系统形式销售给企业的品牌阵列：2025 日历年为 US$33.0B，2Q26 为 US$10.3B（+33.6%）。超大规模云厂商的大部分存储支出不在其统计范围内。（[第 40 章](../06-industry-and-competition/40-market-structure.md)）

</details>

<details>
<summary><strong>Q209.</strong> (L2) 为什么要审慎看待 2026 年存储收入 30%+ 的增长？</summary>

这主要是价格因素。2026 年上半年 NAND 合约价格涨了一倍多，IDC 表示客户花了更多的钱却买到了更少的容量。（[第 40 章](../06-industry-and-competition/40-market-structure.md)）

</details>

<details>
<summary><strong>Q210.</strong> 2Q26 外部存储市场前五名的份额分别是多少？</summary>

Dell 23.8%、Huawei 11.3%、NetApp 9.6%、Everpure 8.1%、HPE 6.8%，其余厂商合计约 40%。（[第 40 章](../06-industry-and-competition/40-market-structure.md)）

</details>

<details>
<summary><strong>Q211.</strong> (L2) 为什么不存在可信的公开"AI 存储 TAM"？</summary>

那些给出大数字的报告定义宽松，而 IDC 认为存储只占 AI 基础设施支出的 2.4%。一个站得住脚的三角测算给出 2026 年约 ~US$9–25B，独立厂商能分到的部分还要小得多。（[第 40 章](../06-industry-and-competition/40-market-structure.md)）

</details>

<details>
<summary><strong>Q212.</strong> 什么是 ODM 直供（ODM direct）？</summary>

由 ODM 按超大规模云厂商的设计制造并直接销售给它的存储硬件，不计入品牌阵列的跟踪统计。（[第 40 章](../06-industry-and-competition/40-market-structure.md)）

</details>

<details>
<summary><strong>Q213.</strong> (L2) 哪三个相互强化的驱动因素解释了 AI 原生厂商的市场牵引力？</summary>

为并行、元数据密集的 GPU I/O 而构建的架构；通过参考设计、认证和股权与 NVIDIA 的早期绑定；以及 neocloud 这一采购标准恰好契合的新买方群体。（[第 41 章](../06-industry-and-competition/41-why-ai-native-vendors-won.md)）

</details>

<details>
<summary><strong>Q214.</strong> (L2) AI 原生论点最薄弱的地方在哪里？</summary>

约 US$37B 的私募估值建立在约 ~US$1.1B 的收入信号之上。客户集中，NVIDIA 能扶植也能抛弃厂商，三家都缺席了 MLPerf v3.0，而 NAND 短缺对不自行采购闪存的厂商冲击更大。（[第 41 章](../06-industry-and-competition/41-why-ai-native-vendors-won.md)）

</details>

<details>
<summary><strong>Q215.</strong> 什么是"造王者风险"（kingmaker risk）？</summary>

对平台所有者（这里是 NVIDIA）的依赖——它的背书随时可以延伸给竞争对手。（[第 41 章](../06-industry-and-competition/41-why-ai-native-vendors-won.md)）

</details>

<details>
<summary><strong>Q216.</strong> 什么是已承诺 ARR（CARR）？</summary>

已签署的经常性合同的年化价值，包括尚未上线的合同，因此大于 ARR。（[第 41 章](../06-industry-and-competition/41-why-ai-native-vendors-won.md)）

</details>

<details>
<summary><strong>Q217.</strong> (L2) AI 原生厂商的窗口期已经关闭了吗？</summary>

正在收窄，但尚未关闭。FlashBlade//EXA、NetApp AFX、Dell Lightning 和 HPE X10000 消除了架构差距，但没有消除挑战者的装机基础和 NVIDIA 关系。（[第 41 章](../06-industry-and-competition/41-why-ai-native-vendors-won.md)）

</details>

<details>
<summary><strong>Q218.</strong> (L2) 驱动 VAST 经济性的三个机制是什么？</summary>

超宽纠删码（规模化时开销约 3%）、基于相似性的数据缩减，以及廉价的 QLC。三者叠加，使全闪存不仅适用于热层，也能可信地承载整个数据集。（[第 42 章](../06-industry-and-competition/42-vast-data.md)）

</details>

<details>
<summary><strong>Q219.</strong> 什么是 VAST 的 Element Store？</summary>

位于文件、对象、表和块之下的统一元数据与数据结构，VAST AI Operating System 的各个引擎都构建在其之上。（[第 42 章](../06-industry-and-competition/42-vast-data.md)）

</details>

<details>
<summary><strong>Q220.</strong> 什么是 VAST 的 Gemini 模式？</summary>

硬件按成本价销售，再加上按容量定价的软件订阅。（[第 42 章](../06-industry-and-competition/42-vast-data.md)）

</details>

<details>
<summary><strong>Q221.</strong> (L2) 应如何解读 VAST 的财务说法？</summary>

应视为公司自述：已承诺 ARR 超过 US$500M，累计订单超过 US$4B，2026 年 4 月约 US$1B 的 F 轮融资（约一半为老股转让）估值 US$30B。这相当于约 ~60× CARR。（[第 42 章](../06-industry-and-competition/42-vast-data.md)）

</details>

<details>
<summary><strong>Q222.</strong> (L2) VAST 的主要风险是什么？</summary>

估值跑在已披露收入之前；在 NAND 短缺中依赖合作伙伴硬件；客户集中；NVIDIA 把这一架构推广给所有竞争对手；以及向数据库领域扩张，进入 Databricks 和 Snowflake 的地盘。（[第 42 章](../06-industry-and-competition/42-vast-data.md)）

</details>

<details>
<summary><strong>Q223.</strong> WEKA 卖的是什么？</summary>

软件：一款面向 NVMe 闪存的并行、无共享（shared-nothing）文件系统，2025 年 6 月由 WekaFS 更名为 NeuralMesh。它可运行在通用服务器上、GPU 服务器内部，或在 AWS、Azure、Google Cloud 和 OCI 中运行。（[第 43 章](../06-industry-and-competition/43-weka.md)）

</details>

<details>
<summary><strong>Q224.</strong> (L2) WEKA 的技术标志是什么？</summary>

绕过内核（kernel-bypass）的数据路径，元数据分片分布在每个节点上。（[第 43 章](../06-industry-and-competition/43-weka.md)）

</details>

<details>
<summary><strong>Q225.</strong> (L2) 什么是 WEKA 的 Augmented Memory Grid？</summary>

首个作为产品销售的 KV 缓存卸载层，于 2025-11-18 商用，OCI 为首发合作伙伴。其"TTFT 最高快 20×"的说法合理，但未经独立审计。（[第 43 章](../06-industry-and-competition/43-weka.md)）

</details>

<details>
<summary><strong>Q226.</strong> (L2) 为什么说 WEKA"比围绕它的声量要小"？</summary>

2024 年 ARR 超过 US$100M（公司自述），累计融资约 US$415M，最近一次定价融资是 2024 年 5 月的 US$1.6B，此后再无。HPE 于 2026 年 3 月停止转售其软件。（[第 43 章](../06-industry-and-competition/43-weka.md)）

</details>

<details>
<summary><strong>Q227.</strong> DDN 的两大引擎是什么？</summary>

EXAScaler——以一体机形式交付的 Lustre，用于训练和 HPC 带宽；以及 Infinia——一个键值存储平台，用于推理、KV 缓存和多租户对象数据。DDN CORE 是覆盖两者的控制平面。（[第 44 章](../06-industry-and-competition/44-ddn.md)）

</details>

<details>
<summary><strong>Q228.</strong> (L2) 既然 Lustre 是开源的，DDN 的护城河是什么？</summary>

是亲密关系，而不是代码：维护 Lustre 的工程师、NVIDIA 内部的参考设计（它为 Selene 和 Eos 提供了存储），以及盈利、受政府青睐的供应商记录。（[第 44 章](../06-industry-and-competition/44-ddn.md)）

</details>

<details>
<summary><strong>Q229.</strong> (L2) Blackstone 在 2025 年 1 月的投资释放了什么信号？</summary>

以 $5B 估值投入 $300M 获得股份，这是 DDN 约二十年来首次引入机构资本。媒体报道称其 2025 年收入接近 $500M，2026 年目标约 ~$1B，但基数数据相互矛盾。（[第 44 章](../06-industry-and-competition/44-ddn.md)）

</details>

<details>
<summary><strong>Q230.</strong> 什么是 Whamcloud？</summary>

DDN 自 2018 年起拥有的 Lustre 工程部门。（[第 44 章](../06-industry-and-competition/44-ddn.md)）

</details>

<details>
<summary><strong>Q231.</strong> (L2) EXA、VAST、WEKA 和 DDN 各自如何拆分元数据与数据？</summary>

EXA 把元数据放在 Purity 核心上，通过 pNFS 把大块数据发往数据节点；VAST 把全部数据和元数据存放在无状态 CNode 之后的共享 SCM 和 QLC 上；WEKA 把元数据哈希到每个节点上的桶（bucket）中；DDN 把 Lustre 元数据放在 MDS 上、数据放在 OSS 一体机上。（[第 45 章](../06-industry-and-competition/45-head-to-head.md)）

</details>

<details>
<summary><strong>Q232.</strong> (L2) 四家 AI 规模厂商各自在哪类交易中领先？</summary>

VAST：多租户、多协议平台，拥有 10,000+ GPU 级别的参考客户。DDN：Lustre 传承、NVIDIA 自有设计、主权采购。WEKA：跟随 GPU 进入云端或 GPU 服务器的存储。EXA：公开发布且经同行评审的基准测试吞吐量、标准客户端、现有的 Everpure 客户关系。（[第 45 章](../06-industry-and-competition/45-head-to-head.md)）

</details>

<details>
<summary><strong>Q233.</strong> (L2) FlashBlade//EXA 落后在哪里？</summary>

参考客户、认证徽章、云端覆盖和数据节点成熟度：没有公开的 10,000-GPU 参考客户；SuperPOD 和 NCP 认证属于 FlashBlade//S；没有公有云版 EXA；数据节点的缩减和保护功能还处在年轻的发布周期上。（[第 45 章](../06-industry-and-competition/45-head-to-head.md)）

</details>

<details>
<summary><strong>Q234.</strong> (L2) 传统厂商真正的武器是架构吗？</summary>

不是，是商业层面的：装机基础、渠道、与服务器和网络的捆绑、自有融资，以及对 Huawei 而言的主权需求。（[第 46 章](../06-industry-and-competition/46-incumbents.md)）

</details>

<details>
<summary><strong>Q235.</strong> (L2) 本图谱对传统厂商威胁 Everpure 的程度如何排序？</summary>

大致为 Dell > NetApp > HPE > Huawei（美国以外）> IBM > Hitachi。Dell 胜在捆绑，NetApp 胜在统一文件存储和装机基础，其余厂商在细分领域取胜。（[第 46 章](../06-industry-and-competition/46-incumbents.md)）

</details>

<details>
<summary><strong>Q236.</strong> Dell、NetApp 和 HPE 打造了哪些面向 AI 时代的新系统？</summary>

Dell 的 Lightning File System、NetApp 的 AFX（分解式 ONTAP）以及 HPE 的 X10000（支持原生 NFS 的分解式对象存储）。（[第 46 章](../06-industry-and-competition/46-incumbents.md)）

</details>

<details>
<summary><strong>Q237.</strong> 谁是 Everpure 最大的"其他挑战者"？</summary>

超大规模云厂商自己的存储。仅 S3 就保存了超过 500 万亿个对象，而生于云端的数据很少拿出来招标。（[第 47 章](../06-industry-and-competition/47-other-challengers.md)）

</details>

<details>
<summary><strong>Q238.</strong> (L2) 为什么 Hammerspace 具有战略重要性？</summary>

它的 pNFS 全局命名空间位于所有厂商的阵列之上，其 Tier 0 能把 GPU 服务器中闲置的 NVMe 变成共享存储。如果它胜出，阵列将变得可以互相替代。（[第 47 章](../06-industry-and-competition/47-other-challengers.md)）

</details>

<details>
<summary><strong>Q239.</strong> (L2) 2025–26 年开源对象存储发生了什么？</summary>

MinIO 大幅削减了免费版功能，并于 2026 年 4 月将其代码仓库归档，迫使用户转向付费的 AIStor、Ceph、分叉版本或其他厂商的 S3。（[第 47 章](../06-industry-and-competition/47-other-challengers.md)）

</details>

<details>
<summary><strong>Q240.</strong> NAND 供应的集中度有多高？</summary>

五家公司占据约 88% 的 NAND 收入；2Q26 前五名收入达 $68.87B，单季增长 77%。（[第 48 章](../06-industry-and-competition/48-media-suppliers-and-nand-cycle.md)）

</details>

<details>
<summary><strong>Q241.</strong> 对比 NAND 合约价与长期协议（LTA）。</summary>

合约价是大客户按季度或按月谈定的价格，不同于波动剧烈的现货价。LTA 是多年期供货合同，如今常附带预付款以及价格下限和上限。（[第 48 章](../06-industry-and-competition/48-media-suppliers-and-nand-cycle.md)）

</details>

<details>
<summary><strong>Q242.</strong> (L2) 阵列厂商如何感受 NAND 周期？</summary>

表现为滞后：成本按季度重新定价，而价目表和合同的重新定价更慢。产品毛利率先降后升，收入被推高，现金则流入库存和预付款。（[第 48 章](../06-industry-and-competition/48-media-suppliers-and-nand-cycle.md)）

</details>

<details>
<summary><strong>Q243.</strong> (L2) Everpure 的 NAND 风险敞口如何划分？</summary>

阵列业务的 NAND 计入其账面；Evergreen//One 以合同约定的固定价格承担 NAND；超大规模 DirectFlash 业务则不承担，因为 NAND 由客户采购。（[第 48 章](../06-industry-and-competition/48-media-suppliers-and-nand-cycle.md)）

</details>

<details>
<summary><strong>Q244.</strong> (L2) 为什么 HDD 与 QLC 之争现在既关乎价格，也关乎供货配额？</summary>

根据单一厂商的指数，2026 年闪存每 TB 的溢价达到约 ~18.6–22.6×，远高于云买家所需的 ≤~3×；但近线 HDD 的交货周期已超过 52 周。（[第 48 章](../06-industry-and-competition/48-media-suppliers-and-nand-cycle.md)）

</details>

<details>
<summary><strong>Q245.</strong> 有没有哪家厂商在本图谱的三张象限图中都位于右上角？</summary>

没有。VAST 在 AI 深度上领先，但企业数据服务薄弱；Dell 和 NetApp 在广度上领先，AI 能力是后补的；超大规模云厂商服务的主要是已经在其云中的数据。（[第 49 章](../06-industry-and-competition/49-competitive-matrices.md)）

</details>

<details>
<summary><strong>Q246.</strong> (L2) 本图谱的矩阵认为 Everpure 的独特定位和最弱项分别是什么？</summary>

独特定位在介质经济性：垂直整合加 DirectFlash，是唯一公开已知向超大规模云厂商销售这类 IP 的阵列厂商。最弱项是云端可用性、主权市场存在感和数据智能。（[第 49 章](../06-industry-and-competition/49-competitive-matrices.md)）

</details>

<details>
<summary><strong>Q247.</strong> (L2) 存储尽职调查要回答的唯一问题是什么？</summary>

这套代码能否在今天规模的十倍下，依然让别人的数据安全、快速且可支持？持久性缺陷、元数据瓶颈和支持负担默认不会出现在数据室里。（[第 50 章](../06-industry-and-competition/50-diligence-framework.md)）

</details>

<details>
<summary><strong>Q248.</strong> 在尽职调查中，什么比持久性模型更有说服力？</summary>

现场数据：年化故障率、重建时间分布、数据丢失事件日志以及回传（phone-home）遥测。（[第 50 章](../06-industry-and-competition/50-diligence-framework.md)）

</details>

<details>
<summary><strong>Q249.</strong> (L2) 与 Everpure 整合时，哪个接合面代价最高？</summary>

数据路径。Purity 和 DirectFlash 的前提是由单一操作系统管理裸 NAND，因此第二套文件系统意味着第二条产品线，而不是一项功能；其他接合面是控制平面、授权许可和渠道。（[第 50 章](../06-industry-and-competition/50-diligence-framework.md)）

</details>

### 第 7 部分 — 历史与未来

第 7 部分的卡片着眼长期：存储与闪存的经济性如何演变，以及 2026–2032 年的哪些趋势是确定的、哪些只是厂商路线图。

| 章节 | 卡片数（L1 / L2） | 卡片编号 |
|---|---|---|
| [第 51 章](../07-history-and-future/51-history-of-storage.md) | 6 (3 / 3) | Q250–Q255 |
| [第 52 章](../07-history-and-future/52-history-of-flash.md) | 5 (1 / 4) | Q256–Q260 |
| [第 53 章](../07-history-and-future/53-future-trends.md) | 5 (1 / 4) | Q261–Q265 |

*图 59.15 — 第 7 部分 — 历史与未来：3 章共 16 张卡片（5 张 L1、11 张 L2），编号 Q250–Q265；可按卡片编号分章记录答错的题目。*

<details>
<summary><strong>Q250.</strong> 说出存储历史的六个时代。</summary>

专属磁盘、阵列与网络、横向扩展与云、闪存、软件定义，以及 AI。每个时代都围绕当时最昂贵的资源来组织。（[第 51 章](../07-history-and-future/51-history-of-storage.md)）

</details>

<details>
<summary><strong>Q251.</strong> 磁盘成本下降了多少？</summary>

从约 US$10,000/MB（IBM RAMAC，1956 年）降至 US$0.014/GB（2022 年），年均下降约 26%。2026 年，磁盘和闪存的成本曲线都在上行。（[第 51 章](../07-history-and-future/51-history-of-storage.md)）

</details>

<details>
<summary><strong>Q252.</strong> (L2) 为什么 Pure Storage 活了下来，而 Violin 失败了？</summary>

Pure Storage 卖的是数据缩减和一种商业模式，因此由软件获取了闪存的经济收益。Violin 卖的是速度，最终申请了 Chapter 11 破产保护。（[第 51 章](../07-history-and-future/51-history-of-storage.md)）

</details>

<details>
<summary><strong>Q253.</strong> (L2) 存储业的在位者通常如何退场？</summary>

很少是消亡：它们通过收购进入新浪潮，然后自己被收购。EMC 收购了 Isilon 和 XtremIO，之后于 2016 年被 Dell 以约 US$67B 收购。（[第 51 章](../07-history-and-future/51-history-of-storage.md)）

</details>

<details>
<summary><strong>Q254.</strong> (L2) 什么是"架构钟摆"？</summary>

存储在集中式与分布式设计之间来回摆动；每当通用 CPU 和网络追上专有控制器时，软件定义浪潮就会再次出现。AI 时代的分解式架构是最新一次摆动，而不是最后一次。（[第 51 章](../07-history-and-future/51-history-of-storage.md)）

</details>

<details>
<summary><strong>Q255.</strong> 什么是 SLED？</summary>

单一大型昂贵磁盘（single large expensive disk），是 1988 年 RAID 论文的对照对象；该论文认为由廉价 PC 磁盘组成的阵列可以胜过它。（[第 51 章](../07-history-and-future/51-history-of-storage.md)）

</details>

<details>
<summary><strong>Q256.</strong> (L2) 谁为闪存的学习曲线买了单？</summary>

消费者：从 2000 年代中期起，音乐播放器和手机为 NAND 的规模化提供了资金。NAND 价格从 2005 年的 ~$45/GB 降至 2023 年谷底的 ~2¢/GB，年均降幅约 35%。（[第 52 章](../07-history-and-future/52-history-of-flash.md)）

</details>

<details>
<summary><strong>Q257.</strong> (L2) 每单元每增加一个比特，每比特成本下降了多少？</summary>

SLC 到 MLC 下降 50%，MLC 到 TLC 下降 33%，TLC 到 QLC 下降 25%。这种边际收益递减，使降本杠杆在 Samsung 于 2013 年推出 24 层 V-NAND 之后转移到了 3D 层数上。（[第 52 章](../07-history-and-future/52-history-of-flash.md)）

</details>

<details>
<summary><strong>Q258.</strong> (L2) 闪存在 $/TB 上是否曾胜过近线磁盘？</summary>

没有。它在大约 2011 年至 2015 年间，在有效 $/GB 上胜过了性能型磁盘（15K/10K RPM），因为在线数据缩减在闪存上成本低，在磁盘上成本高。（[第 52 章](../07-history-and-future/52-history-of-flash.md)）

</details>

<details>
<summary><strong>Q259.</strong> (L2) 为什么 NAND 的周期比 DRAM 更剧烈？</summary>

DRAM 通过破产整合为三家，占据约 ~88% 的收入。NAND 则通过易主（Solidigm、Kioxia、Sandisk）完成整合，至今仍有五家大型供应商。（[第 52 章](../07-history-and-future/52-history-of-flash.md)）

</details>

<details>
<summary><strong>Q260.</strong> 对比 NOR 闪存与 NAND 闪存。</summary>

NOR 将存储单元并联，以实现快速随机读取；NAND 将存储单元串联，密度更高、每比特成本更低。（[第 52 章](../07-history-and-future/52-history-of-flash.md)）

</details>

<details>
<summary><strong>Q261.</strong> (L2) 最确定的趋势是什么？Everpure 的主要杠杆是什么？</summary>

单设备容量：DFM 达 300 TB，标准 SSD 达 245.76 TB，512 TB 的硬盘已列入 2027 年路线图。稀缺的资源是重建时间、NAND 供应和电力，而不是盘位。（[第 53 章](../07-history-and-future/53-future-trends.md)）

</details>

<details>
<summary><strong>Q262.</strong> (L2) 磁盘会在这十年内消亡吗？</summary>

不会。HAMR 将在约 2029 年前把近线硬盘从 44 TB 推向 100 TB；闪存拿下性能型和受电力约束的 AI 容量，磁盘则保留冷数据大容量存储。（[第 53 章](../07-history-and-future/53-future-trends.md)）

</details>

<details>
<summary><strong>Q263.</strong> 什么是上下文内存（context memory）？</summary>

介于 GPU 内存与共享存储之间、存放推理 KV 缓存的存储层；自 2H 2026 起，借助 NVIDIA 的 KVBM 和 BlueField-4 STX/CMX，它成为一个可采购的品类。（[第 53 章](../07-history-and-future/53-future-trends.md)）

</details>

<details>
<summary><strong>Q264.</strong> (L2) 哪些未来趋势需要校准预期？</summary>

CXL 内存池化（Azure 的研究显示可节省约 ~7% 的 DRAM）、存储中的共封装光学（CPO）以及 PLC 闪存都是真实的，但来得比厂商演示文稿暗示的更晚、规模更小。DNA 和玻璃归档仍处于商业化之前。（[第 53 章](../07-history-and-future/53-future-trends.md)）

</details>

<details>
<summary><strong>Q265.</strong> (L2) 为什么 1 PB 的模块会引出重建问题？</summary>

以 20 GB/s 计，重建需要约 ~13.9 小时，而 300 TB 模块约为 ~4.2 小时，这拉长了暴露于第二次故障的时间窗口。（[第 53 章](../07-history-and-future/53-future-trends.md)）

</details>

### 战略综合题

战略卡片把不同部分的事实结合起来。它们没有唯一正确的标准句；高质量回答应点出机制、给出一个数字，并说明业务后果。把这些放在最后做，并且要大声说出来。

| 所依据的章节 | 引用该章的战略卡片数 | 卡片编号 |
|---|---|---|
| [第 3 章](../01-storage-fundamentals/03-inside-an-ssd.md) | 1 | Q268 |
| [第 4 章](../01-storage-fundamentals/04-performance-and-economics-metrics.md) | 1 | Q274 |
| [第 11 章](../02-protocols-and-networking/11-gpu-data-path.md) | 1 | Q269 |
| [第 12 章](../02-protocols-and-networking/12-interfaces-and-emerging-tech.md) | 1 | Q268 |
| [第 22 章](../03-system-architecture/22-control-planes.md) | 1 | Q276 |
| [第 23 章](../03-system-architecture/23-consumption-models.md) | 1 | Q275 |
| [第 25 章](../04-everpure/25-company-history-and-strategy.md) | 1 | Q278 |
| [第 26 章](../04-everpure/26-purity-and-directflash.md) | 2 | Q267, Q268 |
| [第 27 章](../04-everpure/27-flasharray-and-flashblade.md) | 2 | Q270, Q277 |
| [第 28 章](../04-everpure/28-platform-and-software.md) | 1 | Q279 |
| [第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md) | 4 | Q266, Q267, Q275, Q278 |
| [第 31 章](../05-ai-storage/31-training-storage.md) | 1 | Q269 |
| [第 32 章](../05-ai-storage/32-inference-and-kv-cache.md) | 1 | Q269 |
| [第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md) | 1 | Q272 |
| [第 34 章](../05-ai-storage/34-nvidia-ecosystem.md) | 1 | Q271 |
| [第 35 章](../05-ai-storage/35-ai-factories-and-neoclouds.md) | 1 | Q273 |
| [第 37 章](../05-ai-storage/37-reading-benchmarks.md) | 1 | Q270 |
| [第 38 章](../05-ai-storage/38-power-and-density.md) | 1 | Q274 |
| [第 39 章](../05-ai-storage/39-agentic-ai-and-data-intelligence.md) | 2 | Q272, Q279 |
| [第 40 章](../06-industry-and-competition/40-market-structure.md) | 2 | Q266, Q278 |
| [第 41 章](../06-industry-and-competition/41-why-ai-native-vendors-won.md) | 1 | Q273 |
| [第 43 章](../06-industry-and-competition/43-weka.md) | 1 | Q277 |
| [第 47 章](../06-industry-and-competition/47-other-challengers.md) | 1 | Q276 |
| [第 48 章](../06-industry-and-competition/48-media-suppliers-and-nand-cycle.md) | 1 | Q266 |
| [第 53 章](../07-history-and-future/53-future-trends.md) | 1 | Q272 |

*图 59.16 — 14 张战略卡片引用了 25 个章节；大多数卡片结合了不止一个部分的事实，因此最能检验各个思维模型是否已融会贯通。*

<details>
<summary><strong>Q266.</strong> (L2) 为什么 Everpure 2026 年的收入增长可能被美化，而利润率却被低估？</summary>

NAND 成本传导推高了收入（2Q26 阵列市场增长 33.6%，主要来自价格），而产品毛利率滞后于投入成本（Q2 FY27 非 GAAP 为 66.2%）。应结合成本传导的滞后，把增长和利润率放在一起看。（[第 40 章](../06-industry-and-competition/40-market-structure.md)、[第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md)、[第 48 章](../06-industry-and-competition/48-media-suppliers-and-nand-cycle.md)）

</details>

<details>
<summary><strong>Q267.</strong> (L2) 把 DirectFlash 与 Everpure 的三条收入来源联系起来。</summary>

它让阵列密度更高（产品）；让 Evergreen 能够原地换代（订阅）；它也是授权给 Meta 和第二家超大规模云厂商、不涉及 NAND 的 IP（超大规模业务）。（[第 26 章](../04-everpure/26-purity-and-directflash.md)、[第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md)）

</details>

<details>
<summary><strong>Q268.</strong> (L2) 为什么"谁来运行 FTL"是一个战略问题，而不仅是工程问题？</summary>

掌握 FTL 可以消除重复的垃圾回收、映射 DRAM 和备用闪存，使模块容量更大，IP 也可对外授权。但这也意味着每一代 NAND 都要自己认证；FDP 则是通用闪存的反制手段。（[第 3 章](../01-storage-fundamentals/03-inside-an-ssd.md)、[第 12 章](../02-protocols-and-networking/12-interfaces-and-emerging-tech.md)、[第 26 章](../04-everpure/26-purity-and-directflash.md)）

</details>

<details>
<summary><strong>Q269.</strong> (L2) 在 AI 交易中，哪三个存储时刻比训练数据读取更重要？</summary>

检查点写入、故障后的恢复，以及推理时的 KV 缓存拉取。文本训练读取在整个集群范围内也只有 MB/s 量级。（[第 11 章](../02-protocols-and-networking/11-gpu-data-path.md)、[第 31 章](../05-ai-storage/31-training-storage.md)、[第 32 章](../05-ai-storage/32-inference-and-kv-cache.md)）

</details>

<details>
<summary><strong>Q270.</strong> (L2) 你会如何对任何厂商（包括 Everpure）的"基准测试第一"说法进行压力测试？</summary>

问清提交了多少硬件；按买方所需容量点，以每机架单元、每 kW 或每美元做归一化；再核实谁没有参赛。Everpure 在 MLPerf v3.0 中的领先，取得于 VAST、WEKA 和 DDN 缺席的一轮。（[第 37 章](../05-ai-storage/37-reading-benchmarks.md)、[第 27 章](../04-everpure/27-flasharray-and-flashblade.md)）

</details>

<details>
<summary><strong>Q271.</strong> (L2) 为什么 NVIDIA 认证不能作为 AI 存储评估的终点？</summary>

它只是证明互操作性和最低吞吐量的底线，B200 enhanced 级别要求每块 GPU 不到 0.5 GB/s。它对价格、数据缩减、运维或故障行为只字未提，而且 NVIDIA 持有部分认证厂商的股权。（[第 34 章](../05-ai-storage/34-nvidia-ecosystem.md)）

</details>

<details>
<summary><strong>Q272.</strong> (L2) 随着数据路径商品化，控制点正在向哪里转移？</summary>

向上转移到数据服务（目录、治理、向量搜索、策略控制平面），向下转移到网络结构（DPU、Ultra Ethernet、S3 over RDMA）。（[第 53 章](../07-history-and-future/53-future-trends.md)、[第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md)、[第 39 章](../05-ai-storage/39-agentic-ai-and-data-intelligence.md)）

</details>

<details>
<summary><strong>Q273.</strong> (L2) 为什么 neocloud 交易所看重的优势与企业交易不同？</summary>

neocloud 要加价转售存储，而存储又可能让所有 GPU 闲置，因此多租户、API 配置、可靠性、部署速度和与 NVIDIA 的契合度比价格和企业级功能更重要。正是这种契合，让 AI 原生厂商率先在这里胜出。（[第 35 章](../05-ai-storage/35-ai-factories-and-neoclouds.md)、[第 41 章](../06-industry-and-competition/41-why-ai-native-vendors-won.md)）

</details>

<details>
<summary><strong>Q274.</strong> (L2) 对"闪存比磁盘便宜吗？"的诚实回答是什么？</summary>

2026 年按采购价算并不便宜（企业级 SSD 对近线 HDD，每 TB 约 ~18.6×）。闪存胜在性能、密度和运维；其节电收益很少能抵消溢价，主要只在必须满足每 TB 带宽要求或能以超大规模云厂商成本采购 NAND 的场景下才行。（[第 4 章](../01-storage-fundamentals/04-performance-and-economics-metrics.md)、[第 38 章](../05-ai-storage/38-power-and-density.md)）

</details>

<details>
<summary><strong>Q275.</strong> (L2) 应结合哪些指标来解读 Everpure 公布的增长？</summary>

订阅 ARR（$2.13B）、RPO（$4.1B）和 STaaS TCV——随着按期确认收入的业务占比提升，这些指标会上升，同时压低报告的产品增长；此外还有订阅净美元留存率（FY26 为 113%）和自由现金流。（[第 23 章](../03-system-architecture/23-consumption-models.md)、[第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md)）

</details>

<details>
<summary><strong>Q276.</strong> (L2) 为什么 Hammerspace 的威胁比其体量所显示的更大？</summary>

一个凌驾于所有阵列之上的命名空间，加上 Tier 0 GPU 本地 NVMe，可能让阵列变得可以互相替代，并把控制点从阵列厂商的控制平面上移走。（[第 47 章](../06-industry-and-competition/47-other-challengers.md)、[第 22 章](../03-system-architecture/22-control-planes.md)）

</details>

<details>
<summary><strong>Q277.</strong> (L2) FlashBlade//EXA 与 WEKA 最明显的区别是什么？</summary>

标准 pNFS 客户端和基于 DirectFlash 的元数据核心，对比 WEKA 可运行在任意硬件上的专有客户端；此外还有 WEKA 在 KV 缓存上的先发优势（Augmented Memory Grid）对比 PureKVA。（[第 43 章](../06-industry-and-competition/43-weka.md)、[第 27 章](../04-everpure/27-flasharray-and-flashblade.md)）

</details>

<details>
<summary><strong>Q278.</strong> 哪三个数字最能勾勒 Everpure 在 2026 年末的规模？</summary>

FY2027 收入指引 $5.03–5.07B、2Q26 外部存储份额 8.1%（第 4 名），以及 $2.13B 的订阅 ARR。（[第 25 章](../04-everpure/25-company-history-and-strategy.md)、[第 40 章](../06-industry-and-competition/40-market-structure.md)、[第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md)）

</details>

<details>
<summary><strong>Q279.</strong> (L2) 为什么战略团队可能认为 1touch 交易的价值超出其价格？</summary>

智能体把元数据变成了产品，而对不在 Everpure 阵列上的数据进行分类，是存储厂商通过中立性检验的唯一途径。（[第 39 章](../05-ai-storage/39-agentic-ai-and-data-intelligence.md)、[第 28 章](../04-everpure/28-platform-and-software.md)）

</details>

## Everpure 的做法与竞争对手对比

可把本节当作对比类卡片的答案要点。同一主题通常既有 Everpure 的立场，也有最强的反驳，可信的回答应两者兼顾。

| 主题 | Everpure 立场 | 竞争对手最强反驳 | 卡片 |
|---|---|---|---|
| 闪存管理 | 在裸 NAND DirectFlash Module 上运行一个全局 FTL | FDP SSD 和超大规模云厂商自研设计在通用硬盘上缩小差距 | Q18, Q74, Q134, Q137 |
| AI 规模文件存储 | FlashBlade//EXA：元数据核心加 pNFS 直达数据节点，标准客户端 | VAST DASE 拥有 10,000+ GPU 级参考客户；WEKA 的专有客户端可在任意环境运行；DDN Lustre 部署在 NVIDIA 内部 | Q92, Q142, Q231, Q232 |
| 基准测试 | MLPerf Storage v3.0 检查点和 KV 缓存成绩第一 | 最强的对手没有参加那一轮 | Q143, Q198 |
| 与 NVIDIA 的契合 | FlashBlade//S 已全面认证；EXA 的 NCP 认证待定；STX 合作伙伴 | NVIDIA 持有 VAST 和 WEKA 的股权，并在 DDN 上运行自有集群 | Q144, Q183, Q184 |
| 商业模式 | 自 2015 年起基于无状态控制器的 Evergreen 订阅 | Dell、NetApp 和 HPE 如今已提供同等合同条款 | Q129, Q81, Q123 |
| 数据智能 | 基于 1touch 的 Data Intelligence，自 2026 年起 | 目录和数据安全厂商能看到所有厂商的存储 | Q149, Q206, Q279 |

*图 59.17 — 六个反复出现的主题上 Everpure 的立场与最强版本的反驳（steelman），以及检验各主题的卡片。*

## 历史与发展轨迹

本卡组反映的是本图谱截至 2026-11-01 最后核实时的状态，各张卡片过时的速度不同。物理与协议类卡片（NAND 磨损、Little 定律、pNFS 布局、法定人数计算）可以多年不变。产品类卡片（DFM 容量、EXA 认证状态、WEKA 的命名）随每次发布而变化。财务与市场类卡片（ARR、RPO、IDC 份额、NAND 合约价、私募估值）每个季度都会变，基准测试类卡片则随每一轮 MLPerf 而变。

| 卡片类型 | 示例 | 变化频率 | 更新触发事件 |
|---|---|---|---|
| 物理与协议 | NAND 磨损、Little 定律、pNFS 布局、法定人数 | 几乎不变 | 图谱新版本 |
| 架构瓶颈 | DASE 最小规模、重建窗口、元数据上限 | 随产品换代 | 厂商重大发布 |
| 产品与认证 | DFM 容量、EXA 认证、WEKA 命名 | 每次发布 | 厂商发布或 NVIDIA 计划更新 |
| 财务与份额 | ARR、RPO、毛利率、IDC 份额 | 每个季度 | 财报发布、IDC 跟踪报告 |
| 基准测试与私募估值 | MLPerf 成绩、VAST 和 WEKA 融资轮次 | 每轮测试或每次融资 | MLPerf 新一轮、融资新闻 |

*图 59.18 — 卡片过时的速度各不相同；最后两行需要每个季度重新核对。*

一条实用规则：每次 Everpure 发布财报、IDC 发布季度跟踪报告、MLPerf Storage 完成新一轮测试之后，都要对照更新后的章节重新核实引用这些来源的卡片，并淘汰已被取代的内容。当本图谱新增或重写某一章时，应根据新的要点速览（TL;DR）和"关键数字"表重新生成该部分的卡片，而不是逐张修改。

## 关键数字

| 指标 | 数值 | 背景 | 来源 / 日期 |
|---|---|---|---|
| 闪卡总数 | 279 | Q1–Q279，连续编号 | 本章，2026-11-01 |
| L1（定义）卡片 | 111 (40%) | 题目行中不加标签 | 本章，2026-11-01 |
| L2（机制 / 权衡）卡片 | 168 (60%) | 标注"(L2)" | 本章，2026-11-01 |
| 第 1 部分 — 存储基础 卡片 | 37 | 17 L1 / 20 L2，Q1–Q37 | 本章，2026-11-01 |
| 第 2 部分 — 协议与网络 卡片 | 37 | 17 L1 / 20 L2，Q38–Q74 | 本章，2026-11-01 |
| 第 3 部分 — 系统架构 卡片 | 52 | 22 L1 / 30 L2，Q75–Q126 | 本章，2026-11-01 |
| 第 4 部分 — Everpure 卡片 | 31 | 14 L1 / 17 L2，Q127–Q157 | 本章，2026-11-01 |
| 第 5 部分 — AI 存储 卡片 | 50 | 19 L1 / 31 L2，Q158–Q207 | 本章，2026-11-01 |
| 第 6 部分 — 行业与竞争 卡片 | 42 | 16 L1 / 26 L2，Q208–Q249 | 本章，2026-11-01 |
| 第 7 部分 — 历史与未来 卡片 | 16 | 5 L1 / 11 L2，Q250–Q265 | 本章，2026-11-01 |
| 战略综合题卡片 | 14 | 1 L1 / 13 L2，Q266–Q279 | 本章，2026-11-01 |
| 至少有一张卡片的章节 | 53 | 第 1–7 部分的每一章，唯独第 54 章（战略选项图）除外——该章在卡组完成之后才写成，目前尚无卡片 | 本章，2026-11-01 |

## 对话手册

**借助本卡组，向产品经理提的 3 个问题**

1. *"哪个 Evergreen 层级增长最快？这在 ARR 与报告的产品收入上分别如何体现？"* 高质量回答会区分 //Forever、//Flex 和 //One，解释按期确认收入的 STaaS 占比上升会压低报告增长、同时推高 ARR、RPO 和 TCV，并能主动说出最新数字（Q147、Q122、Q154）。
2. *"FlashBlade//EXA 目前在哪些场景胜出？怎样才能补上参考客户的缺口？"* 高质量回答会提到经同行评审的基准测试吞吐量、标准客户端和现有客户关系，然后坦承仍缺少 10,000-GPU 参考客户、NCP 认证和公有云版 EXA（Q142、Q144、Q232、Q233）。
3. *"Fusion 的采用进展如何？它是否提高了转换成本？"* 高质量回答会给出 >1,200 家客户这一数字，指出它还不到客户总数的十分之一，并解释为什么预设和自动化流程的生命周期比硬件换代更长（Q146）。

**借助本卡组，向工程师提的 3 个问题**

1. *"请带我走一遍 FlashArray 上一次 4 KB 写入从主机到 NAND 的全过程。"* 高质量回答会依次讲到在机箱共享 NVRAM 中完成确认、日志结构写入、在线数据缩减和全局 FTL，且不存在每块盘各自的垃圾回收（Q79、Q133、Q134）。
2. *"一块 300 TB 的 DFM 重建需要多长时间？是什么让二次故障窗口保持在可接受范围内？"* 高质量回答会用容量除以重建带宽来计算，对比单一热备盘重建与分散式（declustered）重建，并提出 1 PB 模块的问题（Q33、Q32、Q265）。
3. *"KV 缓存位于层级结构的哪一层？什么时候拉取比重算更划算？"* 高质量回答会说出 G1–G4 和 G3.5，使用约 ~2–5 GB/s 每 GPU 的盈亏平衡点，并解释为什么只有不在解码中的 KV 才能离开 HBM（Q170、Q171、Q172）。

**不要这样说**：

- "现在闪存比磁盘便宜了。"按 2026 年的采购价并非如此（Q12、Q274）。
- "我们是 MLPerf 第一，没有之一。"应说是参赛者中第一，而且那一轮 VAST、WEKA 和 DDN 都没有参加（Q143、Q198）。
- "NVIDIA 认证证明我们是最快的。"认证只是底线（Q183）。
- "持久性有十一个九，所以不可能丢数据。"持久性的"几个九"是模型推算出来的（Q111）。
- "DirectFlash 不过是一块大 SSD。"它去掉了硬盘自身的 FTL，在 Purity 中运行一个全局 FTL（Q134、Q135）。
- "AI 存储就是给训练喂数据。"决定规格的是检查点、恢复和 KV 缓存（Q163、Q269）。

## 深入阅读（可选，L3 指引）

- 自建卡组：把问答对导出到任意间隔重复应用中；在本章的当前版本内，卡片编号保持稳定。
- 想加大回忆难度，可以先遮住答案，把 L2 回答画成白板草图，再对照章节中的图表核对。
- 本章可与[问题库](57-question-bank.md)（要*提出*的问题）和[速查表](60-cheat-sheets.md)（单页摘要）配合使用；卡片中出现但未定义的术语，请查阅[术语表](../glossary.md)。

## 关键术语

- **间隔重复**（spaced repetition）— 以逐渐拉长的间隔复习材料，时间点恰好安排在即将遗忘之前。
- **莱特纳盒**（Leitner box）— 一种纸质间隔重复系统：答对的卡片移入复习频率更低的盒子，答错的卡片退回 1 号盒。
- **主动回忆**（active recall）— 先凭记忆给出答案再核对，而不是反复重读。
- **交错练习**（interleaving）— 在一次复习中混合多个主题，而不是一次只集中练一个主题。
- **L1 / L2 卡片** — 词汇卡与机制及权衡卡之分，对应本图谱的深度标签。
- 卡片中用到的所有存储术语，请参见[术语表](../glossary.md)。

## 资料来源

所有答案均出自所链接的本图谱各章。本章未引用任何外部来源；每张卡片所链接的章节载有其所用数据的原始脚注。
