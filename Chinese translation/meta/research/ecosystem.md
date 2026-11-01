# 存储与 AI 存储生态：已核实事实库

> 📄 英文原文：[meta/research/ecosystem.md](../../../meta/research/ecosystem.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

- 编制日期：2026-11-01。所有 "retrieved" 日期均为 2026-11-01。
- 方法：在一手来源（NVIDIA、MLCommons、CXL Consortium、PCI-SIG、NVM Express、SNIA、TrendForce、IDC、公司新闻稿/SEC 文件）和行业媒体（Blocks & Files、StorageReview、HPCwire、StorageNewsletter、Tom's Hardware、Reuters 转载）中进行网络检索。
- 局限：本研究环境中无法直接抓取网页（nvidianews.nvidia.com、docs.nvidia.com、mlcommons.org、storagereview.com 和 venturebeat.com 均无法解析）。因此，以下事实来自所引页面的搜索引擎摘要，而非整页阅读。发布前应对照一手页面抽查确切措辞和数字。标注 `[VERIFY: ...]` 的条目属于不确定、相互矛盾，或来自背景知识而非本次会话中检索到的来源。
- 除非另有说明，厂商性能声明（"最高 Nx"）均为厂商自报。
- 命名说明：Pure Storage 于 2026-02-23 更名为 **Everpure**（更名时股票代码仍为 PSTG；根据 `meta/decisions.md` D12，NYSE 股票代码自 2026-04-17 起改为 **P**）。本文件对 2026 年事件使用 "Everpure (formerly Pure Storage)"（Everpure，原 Pure Storage），对更早事件使用 "Pure Storage"。

---

## 1. NVIDIA 存储生态

### 1.1 NVIDIA AI Data Platform（GTC，2025 年 3 月）
- 在 GTC 2025 上，NVIDIA 将 AI Data Platform 定位为一种可定制的参考设计，存储厂商在其基础上构建产品，把加速计算和 AI 智能体（AI-Q / NeMo Retriever）放进存储层。— 来源：NVIDIA Newsroom, "NVIDIA and Storage Industry Leaders Unveil New Class of Enterprise Infrastructure for the Age of AI", 2025-03-18, https://nvidianews.nvidia.com/news/nvidia-and-storage-industry-leaders-unveil-new-class-of-enterprise-infrastructure-for-the-age-of-ai (retrieved 2026-11-01)
- NVIDIA 点名的首发合作方为 DDN、Dell Technologies、HPE、Hitachi Vantara、IBM、NetApp、Nutanix、Pure Storage、VAST Data 和 WEKA。— 来源：same as above.
- 发布时点名的合作伙伴集成：DDN 将 AI Data Platform 能力集成进 Infinia；HPE 集成进 Private Cloud for AI、Alletra 和 GreenLake for File；IBM 集成进 Fusion/Storage Scale 用于 RAG；NetApp 集成进 AIPod；Pure Storage 集成进 FlashBlade；VAST 集成进 InsightEngine。— 来源：IT Brief UK, "NVIDIA unveils AI data platform with leading storage firms", 2025-03, https://itbrief.co.uk/story/nvidia-unveils-ai-data-platform-with-leading-storage-firms (retrieved 2026-11-01) [VERIFY: 确切发布日]
- 据报道，AIC、ASUS、Foxconn 和 Supermicro 正基于该参考设计构建存储和服务器硬件。— 来源：same as above. [VERIFY: 需对照 NVIDIA 新闻稿确认]
- NVIDIA 将 NVIDIA-Certified Storage 认证描述为合作伙伴在 AI Data Platform 上构建智能体 AI 方案的前提条件。— 来源：NVIDIA Blog, "Full Steam Ahead: NVIDIA-Certified Program Expands to Enterprise Storage for Faster AI Factory Deployment", 2025, https://blogs.nvidia.com/blog/nvidia-certified-enterprise-storage (retrieved 2026-11-01) [VERIFY: 发布日期]
- 到 2026 年，NVIDIA 的 AI 存储页面以 **NVIDIA STX**（见 1.6）为主打，目前尚不清楚 STX 是取代 "AI Data Platform" 这一名称，还是与之并存。— 来源：NVIDIA, "NVIDIA STX" product page, n.d., https://www.nvidia.com/en-gb/data-center/ai-storage/stx/ (retrieved 2026-11-01) [VERIFY: AI Data Platform 与 STX 品牌之间的关系]

### 1.2 DGX SuperPOD / BasePOD 存储认证
- NVIDIA 的 SuperPOD 认证按与集群规模挂钩的特定性能档位测试存储。Blocks & Files 于 2024 年 9 月报道了其方法论。— 来源：Blocks & Files, "How Nvidia assesses SuperPOD AI storage performance", 2024-09-03, https://blocksandfiles.com/2024/09/03/nvidia-superpod-storage-certification/ (retrieved 2026-11-01)
- Pure Storage FlashBlade//S500（以太网）于 2024 年 11 月获得 DGX SuperPOD 认证。Blocks & Files 称其为第七家 SuperPOD 存储供应商。— 来源：Blocks & Files, "Pure Storage's FlashBlade//S500 gains Nvidia SuperPOD certification", 2024-11-18, https://www.blocksandfiles.com/ai-ml/2024/11/18/pure-storages-flashblade/s500-gains-nvidia-superpod-certification/1598641 (retrieved 2026-11-01)
- 截至 2025 年公开宣布获得 SuperPOD 认证或验证的厂商：DDN（A³I AI400X2 / AI400X2 QLC，2025 年 3 月与 GB200 一起完成验证）、Dell PowerScale（号称首个获 SuperPOD 认证的基于以太网的存储）、IBM Storage Scale System 6000、NetApp（AFF A90 于 2025 年 3 月通过 SuperPOD 验证；E-Series EF600/BeeGFS 更早）、VAST Data、WEKA 和 Pure Storage。— 来源：Blocks & Files, "Storage vendors rally behind Nvidia at GTC 2025", 2025-03-18, https://www.blocksandfiles.com/ai-ml/2025/03/18/storage-vendors-rally-behind-nvidia-at-gtc-2025/1602277 (retrieved 2026-11-01); NetApp, "NetApp AFF A90 validation NVIDIA DGX SuperPOD", 2025-03-18, https://www.netapp.com/de/product-updates/aff-a90-validation-nvidia-dgx-superpod/ (retrieved 2026-11-01)
- Hitachi Vantara VSP One 持有 DGX BasePOD 认证。据报道其 SuperPOD 认证尚在计划中。— 来源：Dilip Naik (Substack), "Certified Storage for Nvidia DGX SuperPOD", n.d., https://dilipnaik.substack.com/p/certified-storage-for-nvidia-dgx (retrieved 2026-11-01) [VERIFY: 二手来源；需核对 NVIDIA 合作伙伴名单]
- IBM 表示，NVIDIA 已认证 IBM Storage Scale AI Data Platform 适用于 DGX BasePOD、DGX SuperPOD 和 NVIDIA Cloud Partner 参考架构。— 来源：IBM Community blog, "Introducing IBM Storage Scale 6.0.1 and Storage Scale System 7.0.1: An AI-Ready Data Platform", 2026-06-08, https://community.ibm.com/community/user/blogs/mike-kieran/2026/06/08/introducing-ibm-storage-scale-601-and-storage-scal (retrieved 2026-11-01)
- StorageReview 指出，Hammerspace 拥有经审计的 MLPerf Storage 成绩，但不持有 SuperPOD、BasePOD、NCP 或 NVIDIA-Certified Storage 认证。— 来源：StorageReview, "Best Storage Arrays 2026: AI Storage Leaders and Audited Results", updated 2026-09-01, https://www.storagereview.com/best/storage-arrays (retrieved 2026-11-01)
- 未能检索到一份现行、官方的 NVIDIA SuperPOD 认证存储名单。[VERIFY: 查阅 NVIDIA DGX SuperPOD 存储合作伙伴页面，确认 HPE 状态及当前名单]

### 1.3 NVIDIA-Certified Storage 计划（Foundation / Enterprise / NCP）
- NVIDIA 的计划文档描述了三个认证级别——**Foundation、Enterprise 和 NCP**——每一级模拟更大的 GPU 数量（最多 10,000 个 GPU），基准测试难度也更高。Foundation 模拟最多 128 个 GPU 的工作负载。— 来源：NVIDIA Docs, "NVIDIA-Certified Storage", n.d., https://docs.nvidia.com/certification-programs/certified-storage/latest/nvidia-certified-storage.html (retrieved 2026-11-01) [VERIFY: Enterprise 级的 GPU 数量；有一条搜索摘要显示该页面把 NCP 一节误标为 Enterprise]
- 一份 NetApp 文档将该计划描述为只有 Foundation 和 Enterprise 两个级别，可能早于 NCP 级别的设立。— 来源：NetApp, "NVA-1181 NVIDIA-Certified Storage Program", n.d., https://www.netapp.com/it/media/136519-nva-1181-nvidia-certified-storage-program.pdf (retrieved 2026-11-01) [VERIFY: 级别数量随时间的变化]
- 据报道，Pure Storage 同时获得 Foundation 和 Enterprise 两级认证。— 来源：iTWire, "Pure Storage integrates NVIDIA AI Data Platform into FlashBlade to fuel enterprise AI innovation", 2025, https://itwire.com/guest-articles/company-news/pure-storage-integrates-nvidia-ai-data-platform-into-flashblade-to-fuel-enterprise-ai-innovation (retrieved 2026-11-01) [VERIFY: 日期]
- HPE 表示，Alletra Storage MP X10000 是首个获得 NVIDIA-Certified Storage（Foundation 级）的基于对象的平台。— 来源：HPE Newsroom, "HPE accelerates secure, scalable production-ready AI through new innovations with NVIDIA", 2026-03-16, https://www.hpe.com/us/en/newsroom/press-release/2026/03/hpe-accelerates-secure-scalable-production-ready-ai-through-new-innovations-with-nvidia.html (retrieved 2026-11-01)
- Nutanix Unified Storage 宣布获得 Enterprise 级 NVIDIA 认证。— 来源：HPCwire/BigDATAwire, "Nutanix Unified Storage Achieves NVIDIA Certification as Enterprises Race to Build AI Factories", 2026-06 (search extract gave June 1, 2026), https://www.hpcwire.com/bigdatawire/this-just-in/nutanix-unified-storage-achieves-nvidia-certification-as-enterprises-race-to-build-ai-factories/ (retrieved 2026-11-01) [VERIFY: 日期]

### 1.4 NCP（NVIDIA Cloud Partner）存储要求
- NVIDIA 的 "Requirements for AI Clouds" 为高速文件系统设定的门槛大致为：端到端每 PB 可用性 >99.5%、每 PB 年持久性 >99.999%（v2.2 存档版）。当前版本为 v2.4。— 来源：NVIDIA Docs, "NVIDIA Requirements for AI Clouds – Storage requirements", n.d., https://docs.nvidia.com/dsx/ncp/nvidia-requirements-for-ai-clouds/storage-requirements (retrieved 2026-11-01) [VERIFY: v2.4 的数值]
- 主目录（home directory）存储必须是支持 POSIX 访问控制的 NFSv4 共享存储。NCP 必须在 GPU/集群交付前 8 周交付具备 API 集成的高性能存储。— 来源：same as above.
- 对于 GB300 NVL72 推理服务商集群，存储遵循 "NCP Reference Design for Storage"。详细的合作伙伴要求位于 NVIDIA 的 NVOnline 合作伙伴门户（文档 #1124019），不对外公开。— 来源：NVIDIA Docs, "Inference Provider Platform Requirements on GB300 NVL72 for NCPs", n.d., https://docs.nvidia.com/dsx/ncp/inference-provider-requirements/home (retrieved 2026-11-01)
- 厂商 NCP 设计示例：Pure Storage 发布了一份面向 NCP 的参考架构，使用 FlashBlade//S500 搭配 HGX H200、B200 和 B300。— 来源：Pure Storage, "High-Performance Storage for NVIDIA Cloud Partners (RA)", n.d., https://www.purestorage.com/content/dam/pdf/en/reference-architectures/ra-high-performance-storage-for-nvidia-cloud-partners.pdf (retrieved 2026-11-01)
- NetApp AFF A90 于 2025 年 3 月通过 NCP 配置验证。— 来源：HPCwire/BigDATAwire, "NetApp Validated for NVIDIA DGX SuperPOD, Cloud Partners and Certified Systems", 2025-03-18, https://www.hpcwire.com/bigdatawire/this-just-in/netapp-validated-for-nvidia-dgx-superpod-cloud-partners-and-certified-systems/ (retrieved 2026-11-01)

### 1.5 GPUDirect Storage、Magnum IO、面向存储的 Spectrum-X
- Magnum IO GPUDirect Storage（GDS）在存储与 GPU 显存之间建立直接 DMA 通路，绕过 CPU 回弹缓冲区（bounce buffer）。GDS 1.0 于 2021 年定稿，获得 DDN、Dell、Excelero、HPE、IBM、Micron、NetApp、Pavilion、ScaleFlux、VAST 和 WEKA 等厂商支持。— 来源：Blocks & Files, "GPUDirect Storage hitting the streets to VAST acclaim", 2021-06-28, https://www.blocksandfiles.com/file/2021/06/28/gpudirect-storage-hitting-the-streets-to-vast-acclaim/1611092 (retrieved 2026-11-01); TechTarget, "Nvidia finalizes GPUDirect Storage 1.0 to accelerate AI, HPC", 2021, https://www.techtarget.com/searchstorage/news/252503292/Nvidia-finalizes-GPUDirect-Storage-10-to-accelerate-AI-HPC (retrieved 2026-11-01)
- NVIDIA 关于 Magnum IO 存储合作的文章称，该生态覆盖 180 多家厂商，涉及 DDN EXAScaler、WekaFS、VAST NFSoRDMA 和 IBM Spectrum Scale 等文件系统。— 来源：NVIDIA Developer Blog, "Accelerating IO in the Modern Data Center: Magnum IO Storage Partnerships", n.d., https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-magnum-io-storage-partnerships/ (retrieved 2026-11-01) [VERIFY: 日期及 "180" 这一数量]
- NVIDIA 报告称，Spectrum-X 以太网（自适应路由、拥塞控制）可将 AI 存储读取速度提升最高 48%，写入提升 9–41%，测试对象为 DDN、VAST 和 WEKA。— 来源：NVIDIA Developer Blog, "Accelerating AI Storage by up to 48% with NVIDIA Spectrum-X Networking Platform and Partners", 2025, https://developer.nvidia.com/blog/accelerating-ai-storage-by-up-to-48-with-nvidia-spectrum-x-networking-platform-and-partners/ (retrieved 2026-11-01) [VERIFY: 发布日期]
- 在 GTC 2025 上，DDN 推出 "Inferno"，将 Infinia 与 Spectrum-X 结合。— 来源：Blocks & Files, "Storage vendors rally behind Nvidia at GTC 2025", 2025-03-18 (URL above) (retrieved 2026-11-01)

### 1.6 推理上下文内存存储（CES 2026）→ BlueField-4 STX / CMX（GTC 2026）
- **CES 2026（2026-01-05）**：NVIDIA 发布 **Inference Context Memory Storage（ICMS）Platform**（推理上下文内存存储平台），这是一个由 BlueField-4 驱动、"AI 原生"的 KV 缓存存储层，位于每个 pod 内的 GPU 显存与共享存储之间。NVIDIA 声称相比传统存储可实现最高 5 倍 tokens/sec 和 5 倍能效，预计 2026 年下半年（2H 2026）上市。— 来源：NVIDIA Newsroom, "NVIDIA BlueField-4 Powers New Class of AI-Native Storage Infrastructure for the Next Frontier of AI", 2026-01-05, https://nvidianews.nvidia.com/news/nvidia-bluefield-4-powers-new-class-of-ai-native-storage-infrastructure-for-the-next-frontier-of-ai (retrieved 2026-11-01)
- 在 ICMS 设计中，BlueField-4 负责卸载上下文内存的管理、共享和安全。Blocks & Files 将其描述为 NVIDIA 将 GPU 集群的 KV 缓存卸载到 NVMe SSD 这一做法标准化。— 来源：Blocks & Files, "Nvidia standardizes GPU cluster KV cache offload to NVMe SSDs", 2026-01-06, https://blocksandfiles.com/2026/01/06/nvidia-standardizes-gpu-cluster-kv-cache-offload-to-nvme-ssds/ (retrieved 2026-11-01)
- **GTC 2026（2026-03-16）**：NVIDIA 推出 **BlueField-4 STX**，一种基于 Vera Rubin、BlueField-4 和 Spectrum-X 的模块化存储参考架构。其首个机架级实现是 **NVIDIA CMX 上下文内存存储平台**。— 来源：NVIDIA Investor Relations, "NVIDIA Launches BlueField-4 STX Storage Architecture With Broad Industry Adoption", 2026-03-16, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-BlueField-4-STX-Storage-Architecture-With-Broad-Industry-Adoption/default.aspx (retrieved 2026-11-01)
- 点名的 STX 协同设计存储合作伙伴：Cloudian、DDN、Dell Technologies、Everpure、Hitachi Vantara、HPE、IBM、MinIO、NetApp、Nutanix、VAST Data 和 WEKA。制造合作伙伴：AIC、Supermicro 和 QCT。早期采用者：CoreWeave、Crusoe、IREN、Lambda、Mistral AI、Nebius、OCI 和 Vultr。— 来源：StorageNewsletter, "Nvidia GTC 2026: Nvidia Launches BlueField-4 STX Storage Architecture With Broad Industry Adoption", 2026-03-17, https://www.storagenewsletter.com/2026/03/17/nvidia-gtc-2026-nvidia-launches-bluefield-4-stx-storage-architecture-with-broad-industry-adoption/ (retrieved 2026-11-01)
- NAND Research 将 CMX 描述为位于节点本地存储（G3）与共享企业存储（G4）之间的新 "G3.5" 层，沿用 Dynamo KVBM 的分层命名。— 来源：NAND Research, "NVIDIA STX & CMX: Infrastructure for AI Context Storage (GTC 2026)", 2026-03, https://nand-research.com/nvidia-stx-cmx-infrastructure-for-agentic-ai-context-storage/ (retrieved 2026-11-01)
- 有关 STX 的报道还引用了最高 4 倍能效和 2 倍数据摄取速度。这些均为 NVIDIA 的声明，尚无独立基准测试。— 来源：Tom's Hardware, "Nvidia launches BlueField-4 STX storage architecture for agentic AI at GTC 2026", 2026-03-16, https://www.tomshardware.com/tech-industry/nvidia-launches-bluefield-4-stx-storage-architecture-for-agentic-ai (retrieved 2026-11-01) [VERIFY: 需对照 NVIDIA 新闻稿核实 4x/2x 数字]
- Supermicro 展示了 CMX 存储服务器原型，并正与 Micron、Samsung 和 Phison 验证 STX 专属的 SSD 要求。预计 2026 年下半年出货。— 来源：MLQ.ai, "NVIDIA Launches BlueField-4 STX Storage Architecture at GTC 2026, Supermicro Among First to Build CMX Server", 2026-03, https://mlq.ai/news/nvidia-launches-bluefield-4-stx-storage-architecture-at-gtc-2026-supermicro-among-first-to-build-cmx-server/ (retrieved 2026-11-01)
- 命名问题的答案："CMX" 确有其物。它是上下文内存存储平台（STX 的机架级实现），而不是一种独立的互连技术。有一条 Blocks & Files/HPCwire 摘要提到一款基于 "DMX reference architecture" 的 DDN 产品，这很可能是 CMX/STX 的笔误。[VERIFY: DDN 2026 年 6 月相关报道中的 "DMX"]

### 1.7 NVIDIA Dynamo、NIXL 与 KVBM
- Dynamo 是 NVIDIA 的开源（Apache 2.0）分布式推理服务框架，用 Rust 和 Python 编写。它与推理引擎无关（TensorRT-LLM、vLLM、SGLang），NVIDIA 将其定位为 Triton Inference Server 的继任者。— 来源：NVIDIA Developer, "NVIDIA Dynamo", n.d., https://developer.nvidia.com/dynamo (retrieved 2026-11-01)
- Dynamo 于 2025 年 3 月的 GTC 上发布。[VERIFY: GTC 2025 发布日期（据信为 2025-03-18）；本次会话未直接检索]
- **NIXL**（NVIDIA Inference Xfer Library）是一个开源库，用于在 GPU 显存、CPU 内存和存储之间进行点对点数据搬移（KV 缓存）。Dynamo、TensorRT-LLM、vLLM、SGLang 和 Ray 均使用它。— 来源：NVIDIA Developer Blog, NIXL post, n.d., https://developer.nvidia.com/blog/?p=113426 (retrieved 2026-11-01) [VERIFY: 标题/日期]
- **KVBM（KV Block Manager）** 将 KV 块分层存放在 G1（GPU HBM）、G2（主机 DRAM）、G3（本地 SSD）和 G4（远程/对象存储）。磁盘 I/O 通过 NIXL 经 POSIX 进行，条件允许时使用 GDS。G4 被视为通过 NIXL 访问的不透明 blob 存储。NIXL 的默认后端为 UCX 和 POSIX。— 来源：NVIDIA Docs, "KVBM design", Dynamo docs v1.3.0, n.d., https://docs.nvidia.com/dynamo/v1.3.0/design-docs/component-design/kvbm-design.md (retrieved 2026-11-01)
- 在较新的 Dynamo 版本中，磁盘卸载过滤默认开启，以延长 SSD 寿命：只有被访问至少两次的块才会从 CPU 移到磁盘。— 来源：NVIDIA Dynamo docs, "KVBM Guide / KV cache offloading", n.d., https://docs.dynamo.nvidia.com/dynamo/user-guides/kv-cache-offloading (retrieved 2026-11-01) [VERIFY: 因版本而异]
- Dynamo 文档有 v1.0.0、v1.0.1、v1.1.1 和 v1.3.0 等版本，说明 Dynamo 在 2026 年内进入了 1.x。一份第三方 cookbook 在 2026 年 3 月仍安装 v0.9.1。— 来源：NVIDIA Docs (versioned KVBM pages above); Vultr Docs, "NVIDIA Dynamo overview", 2026-03, https://docs.vultr.com/inference-cookbook/cuda/dynamo/dynamo-overview (retrieved 2026-11-01) [VERIFY: Dynamo 1.0 正式发布（GA）日期]

---

## 2. KV 缓存卸载生态

### 2.1 开源
- **LMCache** 是一个开源 KV 缓存层。它把 vLLM 和 SGLang 中的 KV 缓存从 GPU 显存中取出，在不同引擎和查询之间共享，同时支持前缀复用卸载和预填充/解码分离（prefill/decode disaggregation）。该工作在 MLSys 2026 上发表。— 来源：arXiv, "LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference" (2510.09665), 2025-10, https://arxiv.org/pdf/2510.09665 (retrieved 2026-11-01); MLSys 2026 oral listing, https://mlsys.org/virtual/2026/oral/3646 (retrieved 2026-11-01)
- **vLLM** 的文档描述了跨主机内存、存储和远程对等节点的分层 KV 卸载。对等节点的选择交给 llm-d 等编排层。— 来源：vLLM Blog, "Tiered KV Cache Offloading in vLLM", 2026-09-10, https://vllm.ai/blog/2026-09-10-tiered-kv-offloading (retrieved 2026-11-01)
- **llm-d** 以两种方式支持 KV 卸载：一是通过 vLLM 的 OffloadingConnector 原生支持（CPU RAM 加上一个共享文件系统后端 "llm-d FS"），二是通过 LMCache 等第三方连接器。原生路径中的 GPU→CPU→存储分层卸载仍在积极开发中。— 来源：llm-d docs, "KV-Cache Offloading", n.d., https://llm-d.ai/docs/architecture/advanced/kv-management/kv-offloader (retrieved 2026-11-01); llm-d docs, "Offloading Prefix Cache to Shared Storage", n.d., https://llm-d.ai/docs/dev/guides/tiered-prefix-cache/storage (retrieved 2026-11-01)
- llm-d 的治理结构（Red Hat 主导、CNCF 地位）在本次会话中未得到确认。[VERIFY: llm-d 创始成员 / 所属基金会]

### 2.2 厂商 KV 产品
- **WEKA Augmented Memory Grid（AMG）**：在 GTC 2025 上发布，2025-11-18 作为 NeuralMesh 功能并在 Oracle Cloud Marketplace 上商用。它通过 RDMA 和 GPUDirect Storage 在 GPU 显存与 WEKA 的 "token warehouse"（token 仓库）之间流式传输 KV 缓存。WEKA 声称可将 GPU 显存扩展 1000 倍，TTFT 最多降低 20 倍。— 来源：WEKA, "WEKA Breaks The AI Memory Barrier With Augmented Memory Grid on NeuralMesh", 2025-11-18, https://www.weka.io/news/weka-breaks-the-ai-memory-barrier-with-augmented-memory-grid (retrieved 2026-11-01)
- WEKA 于 2026 年 7 月发布 **NeuralMesh 6**（及 WEKApod 3），计划于 2026 年下半年正式发布（GA）。它声称在 OCI H100 系统上实现 10 倍的 token 吞吐量/并发度。NAND Research 指出，该声明没有可复现的方法论。WEKA 还将 NeuralMesh 与 NVIDIA STX 集成。— 来源：NAND Research, "WEKA NeuralMesh 6 and WEKApod 3: density, KV cache and AI economics", 2026-07, https://nand-research.com/weka-neuralmesh-6-and-wekapod-3-density-kv-cache-and-ai-economics/ (retrieved 2026-11-01); StorageReview, "WEKA integrates NeuralMesh with NVIDIA STX to address AI inference memory bottlenecks", 2026, https://www.storagereview.com/news/weka-integrates-neuralmesh-with-nvidia-stx-to-address-ai-inference-memory-bottlenecks (retrieved 2026-11-01) [VERIFY: NeuralMesh 6 的 GA 状态]
- **VAST Data（CES 2026）**：VAST 发布一种推理架构，让其 CNode 存储控制器软件直接运行在 GPU 服务器内的 BlueField-4 DPU 上。每个 CNode 都能访问完整命名空间和集群内全部 NVMe SSD。VAST 声称 KV 缓存操作功耗降低 75%，硬件于 2026 年下半年上市。— 来源：StorageNewsletter, "CES 2026: Vast Data Redesigns AI Inference Architecture for the Agentic Era with Nvidia", 2026-01-07, https://www.storagenewsletter.com/2026/01/07/ces-2026-vast-data-redesigns-ai-inference-architecture-for-the-agentic-era-with-nvidia/ (retrieved 2026-11-01); NAND Research, "VAST's novel approach to NVIDIA's new Inference Context Memory Storage platform", 2026-01, https://nand-research.com/research-note-vasts-novel-approach-to-nvidias-new-inference-context-memory-storage-platform/ (retrieved 2026-11-01)
- 在 VAST Forward（2026 年 2 月）上，VAST 发布 **CNode-X**，一种配备 GPU 的节点类型，首先通过 Supermicro 和 Cisco 销售。— 来源：HPCwire, "VAST adds GPUs into clusters with CNode-X", 2026-02-25, https://www.hpcwire.com/2026/02/25/vast-adds-gpus-into-clusters-with-cnode-x/ (retrieved 2026-11-01)
- **Everpure（Pure）Key Value Accelerator（KVA / PureKVA）**：最初是基于 NFS 和 S3 的持久化 KV 缓存，随后与 NVIDIA Dynamo 和 vLLM 集成。2026 年的更新通过 RDMA 把 KV 张量从 FlashBlade 预先暂存（pre-stage）到 GPU 显存中——Everpure 声称 TTFT 最多加快 20 倍——并使 DeepReduce 压缩始终开启。预计 2026 年 10 月上市。— 来源：Pure Storage Blog, "Pure KVA Now Integrates with NVIDIA Dynamo for Scalable, Low-Latency LLM Inference", 2025, https://blog.purestorage.com/news-events/pure-kva-integrates-nvidia-dynamo-for-scalable-low-latency-llm-inference/ (retrieved 2026-11-01); StorageReview, "Everpure Adds PureKVA to FlashBlade, Claims Up to 20x Faster Time to First Token, and Makes DeepReduce Always-On", 2026, https://www.storagereview.com/news/everpure-purekva-flashblade-20x-time-to-first-token-always-on-deepreduce (retrieved 2026-11-01) [VERIFY: 是否已于 2026 年 10 月正式发布？]
- **DDN**：2025 年 7 月，DDN 声称 Infinia KV 缓存将处理时间缩短 27 倍，输入 token 成本最多降低 75%。2026 年 6 月（ISC 2026），DDN 在 Infinia 和 EXAScaler 上推出与 Dynamo 集成的 KV 缓存加速，声称 KV 缓存加载速度最多提升 55 倍。— 来源：Blocks & Files, "DDN touts Infinia storage as key to faster, cheaper AI inference", 2025-07-19, https://www.blocksandfiles.com/data-management/2025/07/19/ddn-touts-infinia-storage-as-key-to-faster-cheaper-ai-inference/1603774 (retrieved 2026-11-01); Blocks & Files, "DDN launches faster array HW and KV cache SW for AI", 2026-06-24, https://www.blocksandfiles.com/ai-ml/2026/06/24/ddn-launches-faster-array-hw-and-kv-cache-sw-for-ai/5261447 (retrieved 2026-11-01)
- **Hammerspace Tier 0** 将 GPU 服务器内部的本地 NVMe 汇聚成一个共享层，用于训练、检查点保存和推理。v5.2 新增自动 Tier 0 "affinitization"（亲和化），写入会落到客户端本地的 Tier 0 卷。未确认有 KV 缓存专用产品。— 来源：Hammerspace, "Hammerspace Tier 0 Affinitization", 2026, https://hammerspace.com/hammerspace-tier-0-affinitization/ (retrieved 2026-11-01); Data Center Frontier, "Hammerspace Tier 0 Turns GPU Storage Into AI Infrastructure", n.d., https://www.datacenterfrontier.com/ai-data-platforms/article/55380233/hammerspace-tier-0-turns-gpu-storage-into-ai-infrastructure (retrieved 2026-11-01)
- **HPE**：一项经 Kamiwaza 验证的、在 H200 上进行的 X10000 KV 缓存卸载测试显示，与不卸载相比，TTFT 最多加快 20 倍，有效吞吐量提高 17 倍。这是赞助的合作伙伴内容。— 来源：Blocks & Files (Partner Content), "HPE puts storage to work on AI's expensive memory problem", 2026-10-29, https://www.blocksandfiles.com/ai-ml/2026/10/29/partner-content-hpe-puts-storage-to-work-on-ais-expensive-memory-problem/5305788 (retrieved 2026-11-01)
- **CXL 替代方案**：Synopsys 声称，CXL 4.0 内存的 KV 缓存卸载速度比 SSD 快 3.6 倍。— 来源：StorageReview, "Synopsys CXL 4.0 IP hits 128 GT/s, claims 3.6x KV cache offload over SSDs", 2025-12, https://www.storagereview.com/news/synopsys-cxl-4-0-ip-hits-128-gt-s-claims-3-6x-kv-cache-offload-over-ssds (retrieved 2026-11-01) [VERIFY: 日期]
- TrendForce 将 4Q26 企业级 SSD 需求的一部分归因于超大规模云厂商为 KV 缓存工作负载采购 QLC。— 来源：TrendForce, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26, While Consumer-Side Pressure Persists", 2026-09-30, https://www.trendforce.com/presscenter/news/20260930-13258.html (retrieved 2026-11-01)

---

## 3. MLPerf Storage

### 3.1 工作原理
- MLPerf Storage 用软件模拟加速器，以 "sleep"（休眠）时间代替计算，因此无需真实 GPU。得分是存储系统在每个模拟加速器都保持在所需加速器利用率（AU）门槛以上的前提下，能够持续喂饱的最大模拟加速器数量。— 来源：HPCwire, "The New MLPerf Storage Benchmark Runs Without ML Accelerators", 2024-10-03, https://www.hpcwire.com/2024/10/03/the-new-mlperf-storage-benchmark-runs-without-ml-accelerators/ (retrieved 2026-11-01)
- 对于训练类工作负载，只有 AU 达到 90% 或以上，运行才算通过。— 来源：Quobyte Blog, "MLPerf Storage Benchmark 2025 Preliminary Results", 2025, https://www.quobyte.com/blog/mlperf-storage-benchmark-2025-preliminary-results/ (retrieved 2026-11-01) [VERIFY: 需对照 MLCommons 规则核实各工作负载的 AU 门槛（UNet3D 与 ResNet50/CosmoFlow 可能不同，例如 CosmoFlow 为 70%）]
- v3.0 KV 缓存指标：token 的生成速度受限于存储交付其所依赖 KV 缓存的速度。MLCommons 的 David Kanter 将该得分描述为一个系统能够支撑的对话数量。— 来源：MLCommons, "Benchmark MLPerf Storage", n.d., https://mlcommons.org/benchmarks/storage/ (retrieved 2026-11-01); TechArena, "MLPerf Storage v3.0 Expands Into AI Inference", 2026-09, https://techarena.ai/content/mlperf-storage-v3-0-expands-into-ai-inference (retrieved 2026-11-01)

### 3.2 各轮次
- **v1.0（2024-09-25）**：来自 13 家机构的 100 多项成绩。工作负载为 UNet3D、ResNet50 和 CosmoFlow（BERT 被移除），模拟 NVIDIA A100 和 H100。— 来源：MLCommons, "New MLPerf Storage v1.0 Benchmark Results Show Storage Systems Play a Critical Role in AI Model Training Performance", 2024-09-25, https://mlcommons.org/2024/09/mlperf-storage-v1-0-benchmark-results/ (retrieved 2026-11-01); Blocks & Files, "MLPerf Storage V1.0 results show critical role of next gen storage in AI model training", 2024-09-26, https://www.blocksandfiles.com/ai-ml/2024/09/26/mlperf-storage-v10-results-show-critical-role-of-next-gen-storage-in-ai-model-training/1609378 (retrieved 2026-11-01)
- v1.0 数据点（厂商自报）：Huawei OceanStor A800 以 679 GB/s 喂饱 255 个模拟 H100，AU >90%。HPCwire 指出，1,056 个 H100 和 2,100 个 A100 所需吞吐量相近（约 192,000 MiB/s）。— 来源：HPCwire, 2024-10-03 (URL above) (retrieved 2026-11-01)
- **v2.0（2025-08-04）**：来自 7 个国家 26 家机构的 200 多项成绩，MLCommons 称之为创纪录。在 UNet3D、ResNet50 和 CosmoFlow 之外，新增基于 Llama 3（8B、70B、405B、1T）的**检查点保存**测试。各系统支持的加速器数量约为 v1.0 的 2 倍。点名的提交方包括 Alluxio、Argonne National Lab、DDN、Hammerspace、HPE、IBM、Kingston、KIOXIA、Lightbits Labs、Micron、Nutanix、Oracle、Quanta、Samsung、Sandisk、Simplyblock、TTA、UBIX、WDC 和 YanRong。— 来源：StorageNewsletter, "New MLPerf Storage v2.0 Benchmark Results Demonstrate the Critical Role of Storage Performance in AI Training Systems", 2025-08-08, https://www.storagenewsletter.com/2025/08/08/new-mlperf-storage-v2-0-benchmark-results-demonstrate-the-critical-role-of-storage-performance-in-ai-training-systems/ (retrieved 2026-11-01); Blocks & Files, "Storage arrays get faster in 2nd version of MLPerf Storage benchmark", 2025-08-05, https://blocksandfiles.com/2025/08/05/storage-arrays-get-faster-in-2nd-version-of-mlperf-storage-benchmark/ (retrieved 2026-11-01) [VERIFY: 26 家机构的完整名单；v2.0 中 B200 是否为模拟加速器]
- **v3.0（2026-09-01）**：19 家机构（其中 11 家首次参加），StorageReview 统计为 143 项提交。新增 **KV 缓存**工作负载（LLM 推理上下文卸载，基于工作组的仿真实现）和**向量数据库**工作负载，并在 POSIX 之外新增 **S3 对象访问层**（约六分之一的提交使用 S3）。首次提交方为 Azure、Everpure、HolmesAI、Nebius、NewFW、NVIDIA、OpenLake、Suzhou Zishan Longlin、TuringData、XSKY 和 ZettaLane。— 来源：MLCommons via GlobeNewswire, "MLCommons Releases New MLPerf Storage v3.0 Benchmark Results", 2026-09-01, https://www.globenewswire.com/news-release/2026/09/01/3354412/0/en/mlcommons-releases-new-mlperf-storage-v3-0-benchmark-results.html (retrieved 2026-11-01); StorageReview, "MLPerf Storage v3.0: 877 GiB/s Checkpoints, a Cloud First, and a Leaderboard Turned Over", 2026-09, https://www.storagereview.com/news/mlperf-storage-v3-0-877-gib-s-checkpoints-a-cloud-first-and-a-leaderboard-turned-over (retrieved 2026-11-01)
- v3.0 亮点：Everpure FlashBlade//EXA 在 30 个数据节点下实现 877.5 GiB/s 检查点写入，高于 10 个节点时的 327.6 GiB/s。Azure Managed Lustre 是首个参与提交的超大规模云服务，在 4,096 TiB、128 个客户端条件下实现 642.2 GiB/s 检查点写入。— 来源：StorageReview, 2026-09 (URL above) (retrieved 2026-11-01) [VERIFY: 数字取自图表说明]
- v3.0 KV 缓存（Everpure 自报）：FlashBlade//EXA 在 Llama 3.1 8B 纯存储模式下达到 85,736 tokens/s，在 8B 存储加系统内存模式下达到 67,642 tokens/s，在 70B 纯存储模式下达到 33,403 tokens/s。Everpure 声称在其参加的每项检查点和 KV 缓存测试中均排名第一，这是其自身的表述。— 来源：Everpure Blog, "Everpure FlashBlade//EXA Tops MLPerf Storage v3.0 Checkpointing and KV cache Benchmarks", 2026-09, https://blog.everpuredata.com/purely-technical/everpure-flashblade-exa-tops-mlperf-storage-v3-benchmarks/ (retrieved 2026-11-01)

### 3.3 MLPerf Storage 汇总表（可直接转为 CSV）

| 轮次,发布日期,机构数,成绩数,工作负载,本轮新增,模拟加速器说明 |
|---|
| v0.5,2023-09,n/a [VERIFY],n/a,UNet3D;BERT,首轮,A100 [VERIFY] |
| v1.0,2024-09-25,13,>100,UNet3D;ResNet50;CosmoFlow,新增 ResNet50+CosmoFlow；移除 BERT,A100;H100 |
| v2.0,2025-08-04,26,>200,UNet3D;ResNet50;CosmoFlow;检查点保存(Llama3 8B/70B/405B/1T),检查点保存,加速器数量约为 v1.0 的 2 倍 |
| v3.0,2026-09-01,19（其中 11 家首次参加）,143（据 StorageReview）,训练;检查点保存;KV 缓存;向量数据库,KV 缓存;向量数据库;S3 访问,KV 指标 = tokens/s |

---

## 4. 标准与接口技术

- **NVMe 2.3**：NVM Express Base Specification Revision 2.3 的日期为 2025-07-31（批准版 PDF 为 2025-08-01）。据报道，新功能包括快速路径故障恢复、功率上限配置、可配置设备特性（device personality）和可持续性功能。— 来源：NVM Express, "NVM Express Base Specification Revision 2.3", 2025-07-31, https://nvmexpress.org/wp-content/uploads/NVM-Express-Base-Specification-Revision-2.3-2025.08.01-Ratified.pdf (retrieved 2026-11-01) [VERIFY: 功能列表来自二手摘要]
- NVMe 2.0（2021 年 6 月）将规范重构为一份基础规范加若干命令集规范（NVM、ZNS、KV）和传输规范（PCIe、RDMA、TCP）。[VERIFY: 背景知识，本次会话未检索]
- **Flexible Data Placement（FDP，灵活数据放置）** 于 2022 年末以 TP4146 获得批准，由 Meta 和 Google 联合 Samsung 推动，约 6 个月内定稿。其目标是通过主机提供的数据放置提示降低写放大。— 来源：NVM Express, "Overcoming the Write Amplification Problem with NVM Express Flexible Data Placement", n.d., https://nvmexpress.org/nvmeflexible-data-placement-fdp-blog/ (retrieved 2026-11-01); Samsung Semiconductor, "Hyperscalers Embrace Flexible Data Placement (FDP) to Increase Performance and Lower TCO", n.d., https://semiconductor.samsung.com/news-events/tech-blog/hyperscalers-embrace-flexible-data-placement-fdp-to-increase-performance-and-lower-tco/ (retrieved 2026-11-01) [VERIFY: 2025–26 年 FDP 的生产部署情况]
- **ZNS**（Zoned Namespaces，分区命名空间）作为一种 NVMe 命令集存在。本次会话未找到当前的采用数据。[VERIFY: ZNS 部署状态；业界普遍看法是 FDP 已在超大规模场景中取代 ZNS]
- **NVMe-oF/TCP**：未找到 2025–26 年的采用指标。[VERIFY]
- **CXL 4.0** 于 2025-11-18 在 SC25 上发布。它基于 PCIe 7.0 PHY（PAM4、256B FLIT）将链路速率翻倍至 128 GT/s，新增捆绑端口（bundled ports）、原生 x2 链路宽度、最多 4 个重定时器（retimer）以及更强的内存 RAS，延迟保持不变。x16 链路单向带宽为 768 GB/s（合计 1.536 TB/s）。— 来源：CXL Consortium, "CXL 4.0 Specification Release" / "CXL 4.0 White Paper", 2025-11, https://computeexpresslink.org/wp-content/uploads/2025/11/CXL_4.0-White-Paper_FINAL.pdf (retrieved 2026-11-01); Blocks & Files, "CXL 4.0 doubles bandwidth and stretches memory pooling to multi-rack setups", 2025-11-24, https://www.blocksandfiles.com/ai-ml/2025/11/24/cxl-40-doubles-bandwidth-and-stretches-memory-pooling-to-multi-rack-setups/1709444 (retrieved 2026-11-01)
- CXL 3.0（2022 年 8 月，64 GT/s，支持 fabric）和 CXL 3.1（2023 年 11 月）是此前的两代。[VERIFY: 背景知识]
- **PCIe 7.0** 最终规范于 2025-06-11 发布：128 GT/s，x16 双向 512 GB/s。— 来源：Gigazine, "Final PCIe 7.0 specs released to support AI bandwidth demands", 2025-06-13, https://gigazine.net/gsc_news/en/20250613-pcie-7-specification-finalized (retrieved 2026-11-01)
- **PCIe 8.0** 于 2025-08-05 宣布：256 GT/s，x16 双向最高 1 TB/s，可能采用新连接器，最终版本目标为 2028 年发布。v0.3 草案已发给成员。— 来源：The Register, "Confirmed: PCIe 8.0 will double version 7.0's speed and reach 256.0 GT/s", 2025-08-08, https://www.theregister.com/2025/08/08/pcie_8_spec_speed_announced/ (retrieved 2026-11-01)
- **PCIe 6.0 SSD**：Micron 9650 是首款量产的 PCIe 6.0 数据中心 SSD，读取最高 28 GB/s、写入 14 GB/s、5.5M IOPS，容量 7.68–30.72 TB，提供风冷和液冷选项。Samsung 也已开始生产 PCIe 6.0 AI SSD。— 来源：Borecraft (syndicating Tom's Hardware), "First PCIe 6.0 SSD enters mass production with 28GB/s speeds...", 2026-02-14, https://borecraft.com/2026/02/14/first-pcie-6-0-ssd-enters-mass-production-with-28gb-s-speeds-5-5-million-iops-and-liquid-cooling-micron-9650-series-ssds-support-air-and-liquid-cooling/ (retrieved 2026-11-01); Club386, "Samsung begins production of PCIe 6.0 AI data centre SSDs", 2026, https://www.club386.com/?p=135503 (retrieved 2026-11-01) [VERIFY: Micron 量产日期；Samsung 产品型号]
- **EDSFF**：2025 年 7 月，SNIA 的 SFF TA 立项更新 E1.S/E1.L/E3 规范（SFF-TA-1008 功耗/散热），由 Micron 牵头，Dell 和 HPE 担任编辑。SNIA 托管的一份较早的 Trendfocus 预测显示，2026 年 E1.S 约占 SSD 出货量的 51%，E3.S 约占 5.7%。该预测已过时（以 2022 年为基础）。— 来源：SNIA, "EDSFF Taking Center Stage in the Data Center", n.d., https://www.snia.org/sites/default/files/SSSI/EDSFF%20Taking%20Center%20Stage%20in%20the%20Data%20Center.pdf (retrieved 2026-11-01) [VERIFY: 投票结果；当前外形规格构成]
- Meta 的 GenAI 集群存储（2024 年）使用 YV3 Sierra Point 服务器，配备当时可用的最大容量 E1.S SSD。— 来源：Meta Engineering, "Building Meta's GenAI Infrastructure", 2024-03-12, https://engineering.fb.com/2024/03/12/data-center-engineering/building-metas-genai-infrastructure/ (retrieved 2026-11-01)
- **SNIA Storage.AI** 于 2025-08-04 宣布成立，是一个面向 AI 数据服务的开放标准项目。创始成员包括 AMD、Cisco、Dell、IBM、Intel、NetApp 和 Pure Storage，合作组织包括 UEC、NVM Express、OCP、OFA、DMTF 和 SPEC。该工作组在 SDC 2025 上成立，并于 2025 年 11 月选出主席。— 来源：SNIA, "SNIA Announces Storage.AI", 2025-08-04, https://www.snia.org/news_events/newsroom/announces-storageai (retrieved 2026-11-01); SNIA, "2026 Storage.AI SNIA Preview", 2026, https://www.snia.org/sites/default/files/Preview/2026/2026%20StorageAI%20SNIA%20Preview-Final%20v2.pdf (retrieved 2026-11-01) [VERIFY: 成员总数（有一家媒体称为 15 家）]
- **Intel Optane**：Intel 于 2022 年第二季度开始逐步关停 Optane，在 2022-07-28 的财报电话会上宣布，计提 $559M 费用。Gelsinger 将此次退出与 CXL 联系起来。Optane 200 系列 DIMM 计划于 2025 年末停止出货。— 来源：AnandTech, "Intel To Wind Down Optane Memory Business – 3D XPoint Storage Tech Reaches Its End", 2022-07-28, https://www.anandtech.com/show/17515 (retrieved 2026-11-01); ITPro, "Intel kills off Optane Memory business with $559m loss", 2022-07, https://itpro.com/server-storage/solid-state-storage-ssd/368677/intel-kills-off-optane-memory-business-for-559m-loss (retrieved 2026-11-01)

---

## 5. NAND、SSD 与 HDD 介质

### 5.1 3D NAND 层数
- 据 2024-11-21 报道，SK hynix 开始量产 321 层（TLC、1Tb）4D NAND。它声称借助 "Three Plugs" 工艺，生产率比其 238 层一代高 59%。— 来源：Blocks & Files, "SK hynix begins mass production of 321-layer 3D NAND", 2024-11-21, https://www.blocksandfiles.com/ai-ml/2024/11/21/sk-hynix-begins-mass-production-of-321-layer-3d-nand/1605947 (retrieved 2026-11-01)
- SK hynix 表示，2026 年第二季度 321 层 NAND 在其 NAND 产量中占比最大。下一代路线图目标说法不一（2026 年末 375 层 vs 2027 年 500 层）。— 来源：Tom's Hardware, "Inside the future of 3D NAND: The roadmap to 500 layers", 2026, https://www.tomshardware.com/pc-components/storage/inside-the-future-of-3d-nand-the-roadmap-to-500-layers (retrieved 2026-11-01) [VERIFY: 路线图]
- Samsung V10（第 10 代 V-NAND）为 400+ 层，采用混合键合（hybrid bonding），I/O 速率 5.6 GT/s。Samsung 声称其密度比 V9 高约 58%，TLC 约 28 Gb/mm²。— 来源：Tom's Hardware, "Samsung unveils 10th Gen V-NAND: 400+ layers, 5.6 GT/s and hybrid bonding", 2026, https://www.tomshardware.com/pc-components/ssds/samsung-unveils-10th-gen-v-nand-400-layers-5-6-gt-s-and-hybrid-bonding (retrieved 2026-11-01) [VERIFY: 日期和密度数字]
- Kioxia/Sandisk BiCS10 为 332 层，接口速率 4.8 GT/s。据报道其 QLC 面密度约 37 Gb/mm²，高于 Samsung 的 400 层产品。— 来源：Tom's Hardware, "Kioxia and Sandisk sample world's densest 3D NAND — new 332-Layer beats Samsung's 400-Layer NAND", 2026, https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-sample-worlds-densest-3d-nand-new-332-layer-beats-samsungs-400-layer-nand (retrieved 2026-11-01)
- Kioxia/Sandisk 在 VLSI 2026 上发表了 1,000 层 3D NAND 技术研究。— 来源：Kantenna, "1,000-Layer 3D NAND: Kioxia and Sandisk Unveil World-First Tech at VLSI 2026", 2026-06, https://kantenna.com/topic/kioxia-sandisk-1000-layer-3d-nand-vlsi-2026-world-first (retrieved 2026-11-01) [VERIFY: 来源层级较低]
- Micron G9 为 276 层，TLC 约 21.0 Gb/mm²，用于 245TB 的 6600 ION（QLC）。— 来源：Tom's Hardware, roadmap article (URL above); Micron IR, "Industry-Leading 245TB Micron 6600 ION Data Center SSD Now Shipping", 2026-05-05, https://investors.micron.com/news/press-release/2026/Industry-Leading-245TB-Micron-6600-ION-Data-Center-SSD-Now-Shipping/default.aspx (retrieved 2026-11-01)

**各年份 NAND 层数领先者（可直接转为 CSV）**

| 年份,厂商,层数,备注,状态 |
|---|
| 2013,Samsung,24,首款 V-NAND,[VERIFY: 背景知识] |
| 2016,Samsung/业界,48,,[VERIFY: 背景知识] |
| 2017,业界,64,,[VERIFY: 背景知识] |
| 2018,业界,96,,[VERIFY: 背景知识] |
| 2020,Micron,176,首款 176L,[VERIFY: 背景知识] |
| 2022,Micron,232,首款 200+L,[VERIFY: 背景知识] |
| 2022,SK hynix,238,,[VERIFY: 背景知识] |
| 2024,Samsung,~286 (V9),,[VERIFY: 层数未确认] |
| 2024,SK hynix,321,2024 年 11 月量产,有来源 |
| 2025,Micron,276 (G9),,有来源 |
| 2025-26,Kioxia/Sandisk,332 (BiCS10),密度最高,有来源 |
| 2026,Samsung,400+ (V10),混合键合,有来源 |

### 5.2 最大容量 SSD
- **Micron 6600 ION** 于 2026-05-05 开始出货，可用容量 245.76 TB（原始容量 256 TB）。它采用 G9 QLC、PCIe 5.0，提供 E3.L 和 U.2 两种外形规格，Micron 称其为商用容量最大的 SSD。— 来源：Micron IR, 2026-05-05 (URL above) (retrieved 2026-11-01)
- Micron 的对比（厂商口径）：在最大功耗 30 W 下约 8.2 TB/W，而 10 W 的 44 TB HDD 约为 4.4 TB/W。720 块 E3.L 盘的原始容量为 176.9 PB，相同盘位装满 44 TB HDD 则为 31.7 PB。— 来源：StorageReview, "Micron 6600 ION 245TB SSD Review: A Quarter Petabyte Per Drive Bay", 2026, https://www.storagereview.com/review/micron-6600-ion-245tb-ssd-review-a-quarter-petabyte-per-drive-bay (retrieved 2026-11-01) [VERIFY: 720 盘位机架的假设]
- **Sandisk UltraQLC SN670** 于 FMS 2025（2025-08-05）发布，有 128 TB 和 256 TB 两个版本，基于 BiCS8 218 层 NAND，U.2 版本目标为 2026 年上半年。Sandisk 路线图显示 2027 年推出 512 TB。— 来源：Blocks & Files, "Sandisk unveils 256 TB SSD for AI workloads, shipping in 2026", 2025-08-05, https://www.blocksandfiles.com/ai-ml/2025/08/05/sandisk-unveils-256-tb-ssd-for-ai-workloads-shipping-in-2026/1589534 (retrieved 2026-11-01) [VERIFY: 实际出货状态]
- **Solidigm D5-P5336 122.88 TB**（PCIe 4.0、192 层 QLC、U.2/E1.L）自 2025 年初开始出货。Solidigm 表示 245+ TB 的产品将在 2026 年底前推出。— 来源：StorageReview, "Solidigm 122.88TB D5-P5336 Review", 2025, https://www.storagereview.com/review/solidigm-122-88tb-d5-p5336-review-high-capacity-storage-meets-operational-efficiency (retrieved 2026-11-01); TechRadar, "Solidigm confirms 245+ TB SSDs set to launch before end of 2026", 2026, https://www.techradar.com/pro/solidigm-confirms-245-tb-ssds-set-to-launch-before-end-of-2026 (retrieved 2026-11-01) [VERIFY: 2024 年 11 月的发布日期]
- Kioxia LC9（PCIe 5.0 QLC）最高 245.76 TB。据报道 SK hynix PS1101 属于 245 TB 级别。两者的出货状态均未确认。— 来源：DatacenterDisk, "Solidigm D5-P5336 vs Kioxia LC9", n.d., https://datacenterdisk.com/solidigm-d5-p5336-vs-kioxia-lc9 (retrieved 2026-11-01) [VERIFY: 两者均需核实]
- DapuStor R6060 512 TB 已发布/展示，但尚未广泛供货。— 来源：DatacenterDisk, "Largest SSD in the World 2026: 512TB vs 245TB", 2026, https://datacenterdisk.com/largest-ssd (retrieved 2026-11-01) [VERIFY]
- Everpure DirectFlash Module 单模块容量最高 300 TB。— 来源：Blocks & Files, "Second hyperscaler plumps for Everpure's flash technology", 2026-08-11, https://www.blocksandfiles.com/flash/2026/08/11/second-hyperscaler-plumps-for-everpures-flash-technology/5285903 (retrieved 2026-11-01)
- Huawei 在发布 OceanStor A800（2024 年）的同时宣布了一款 128 TB 大容量 SSD。— 来源：DCD, "Huawei unveils its OceanStor A800 AI-specific storage solution, announces 128TB high-capacity SSD", 2024, https://www.datacenterdynamics.com/en/news/huawei-unveils-its-oceanstor-a800-ai-specific-storage-solution-announces-128tb-high-capacity-ssd (retrieved 2026-11-01)

**各年份商用出货的最大容量 SSD（可直接转为 CSV）**

| 年份,容量_TB,产品,接口,状态 |
|---|
| 2018,30.72,Samsung PM1643,SAS,[VERIFY: 背景知识] |
| 2023,61.44,Solidigm D5-P5336,PCIe 4.0,[VERIFY: 背景知识] |
| 2025,122.88,Solidigm D5-P5336,PCIe 4.0,有来源（2025 年初出货） |
| 2026,245.76,Micron 6600 ION,PCIe 5.0,有来源（2026-05-05 出货） |
| 2026（模块）,300,Everpure DFM（专有）,n/a,有来源（非标准 SSD） |
| 2027（路线图）,512,Sandisk UltraQLC,n/a,路线图 |

### 5.3 PLC
- 截至 2026 年初，PLC（每单元 5 bit）NAND 尚未商用出货。SK hynix 于 2025 年 12 月在 IEDM 上展示了一种 "Multi-Site Cell"（多位点单元）分裂单元 PLC 方案，声称读取速度比传统 PLC 快最多 20 倍。这仅处于研究阶段。— 来源：Blocks & Files, "SK hynix developing split-cell 5-bit flash", 2026-01-15, https://www.blocksandfiles.com/flash/2026/01/15/sk-hynix-developing-split-cell-5-bit-flash/4090388 (retrieved 2026-11-01)

### 5.4 HDD
- Seagate Exos M（Mozaic 3+、HAMR）已历经 30 TB（2024 年 1 月发布）、32 TB 和 36 TB 送样。StorageReview 于 2025-07-15 评测了 30 TB 的 Exos M（每盘片 3 TB、10 张盘片）。— 来源：PetaPixel, "Seagate's new 30TB Hard Drive is the Largest Ever", 2024-01-18, https://petapixel.com/2024/01/18/seagates-new-30tb-hard-drive-is-the-largest-ever/ (retrieved 2026-11-01); CRN Asia, "Seagate introduces hard drive capacities of up to 36TB...", 2025, https://www.crnasia.com/india/news-network/news/seagate-introduces-hard-drive-capacities-of-up-to-36tb-extending-its-hamr-based-mozaic-3-technology-platform (retrieved 2026-11-01)
- Seagate Mozaic 4+（每盘片 4 TB、10 张盘片）可达 40 TB。2026 年 3 月，Seagate 报告 Mozaic 4+ 已向两家超大规模云厂商批量出货，容量最高 44 TB。— 来源：TechRadar, "Seagate confirms 40TB hard drives have already been shipped...", 2025, https://www.techradar.com/pro/seagate-confirms-40tb-hard-drives-have-already-been-shipped-but-dont-expect-them-to-go-on-sale-till-2026 (retrieved 2026-11-01); raidzfscalculator.com, "Seagate Mozaic 4+: 40TB and 44TB HDDs Are Official", 2026-03-07, https://raidzfscalculator.com/en/2026/03/07/seagate-mozaic-4-40tb-and-44tb-hdds-are-official/ (retrieved 2026-11-01) [VERIFY: 来源层级较低；需通过 Seagate IR 确认]
- Western Digital（Innovation Day，2026-02-03）：40 TB UltraSMR ePMR 正在两家超大规模云厂商处认证，2026 年下半年量产。HAMR 正在认证，2027 年爬坡。到 2029 年，ePMR 达到 60 TB，HAMR 达到 100 TB。— 来源：Western Digital, "Western Digital Accelerates Storage Innovation for AI Era", 2026-02-03, https://www.westerndigital.com/company/newsroom/press-releases/2026/2026-02-03-western-digital-accelerates-storage-innovation-for-ai-era (retrieved 2026-11-01)
- StorageReview 稍后的一篇文章称，WD 的 40 TB UltraSMR 已开始出货，44 TB HAMR 定于 2027 年上半年推出。— 来源：StorageReview, "WD Bets 8x Bandwidth Beats More Terabytes as 40TB UltraSMR Starts Shipping", 2026, https://www.storagereview.com/news/wd-bets-8x-bandwidth-beats-more-terabytes-as-40tb-ultrasmr-starts-shipping (retrieved 2026-11-01) [VERIFY: 与"仍处于认证阶段"的报道相矛盾]
- Coughlin Associates 估计，数据中心中超过 85% 的数据存放在 HDD 上；AI 驱动的 HDD 需求约占 2026 年出货量的 18%，到 2028 年将升至约 43%。— 来源：Washington Post Creative Group (Solidigm sponsored), "Is 2026 finally the year for data center storage to crossover to SSDs?", 2026, https://www.washingtonpost.com/creativegroup/solidigm/is-2026-finally-the-year-for-data-center-storage-to-crossover-to-ssds (retrieved 2026-11-01) [VERIFY: 引用 Coughlin 的赞助内容]

**各年份 HDD 最大容量（可直接转为 CSV）**

| 年份,容量_TB,厂商/产品,技术,状态 |
|---|
| 2020,20,Seagate/WD,PMR/ePMR,[VERIFY: 背景知识] |
| 2022,22-26,WD (26TB UltraSMR),ePMR/SMR,[VERIFY: 背景知识] |
| 2023,24,WD Gold,CMR,有来源（30TB 之前的纪录） |
| 2024,30-32,Seagate Exos M (Mozaic 3+); WD 32TB UltraSMR,HAMR; ePMR SMR,有来源 |
| 2025,36（送样）,Seagate Exos M,HAMR,有来源 |
| 2026,40-44,Seagate Mozaic 4+; WD 40TB UltraSMR,HAMR; ePMR SMR,有来源/[VERIFY] |
| 2029（路线图）,100,WD HAMR,HAMR,路线图 |

### 5.5 NAND 价格与 2025–26 年短缺（TrendForce）
- TrendForce 2026 年 1 月的预测显示，1Q26 NAND 合约价环比上涨 33–38%（消费级/客户端 SSD 至少上涨 40%），驱动因素是供应商的产能纪律和服务器需求。2026 年 2 月的后续修订显示，1Q26 NAND 上涨 55–60%，企业级 SSD 上涨 53–58%。— 来源：StorageNewsletter (TrendForce), "Memory Makers Prioritize Server Applications, Driving Across-the-Board Price Increases in 1Q26, Says TrendForce", 2026-01-27, https://www.storagenewsletter.com/2026/01/27/memory-makers-prioritize-server-applications-driving-across-the-board-price-increases-in-1q26-says-trendforce/ (retrieved 2026-11-01) [VERIFY: 2 月 2 日修订数字来自二手来源]
- 预测 2Q26 NAND 合约价环比上涨 70–75%，3Q26 上涨 10–15%。— 来源：TrendForce, "Combined Revenue of Top Five NAND Flash Brands Rises 77% QoQ in 2Q26...", 2026-08-18, https://www.trendforce.com/presscenter/news/20260818-13186.html (retrieved 2026-11-01) [VERIFY: 2Q26 70–75% 的数字经二手汇总获得]
- 4Q26：预测 NAND 合约价环比上涨 15–20%，企业级 SSD 上涨 23–28%，是唯一一个涨幅较上季度加速的存储器品类。大部分新增供给已被锁定。— 来源：TrendForce, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26, While Consumer-Side Pressure Persists", 2026-09-30, https://www.trendforce.com/presscenter/news/20260930-13258.html (retrieved 2026-11-01)
- TrendForce 指出，主要 NAND 供应商 2026 年几乎不会新增晶圆产能。据报道，企业级 SSD 在 NAND bit 中的占比 2Q25 为 26%，2Q26 为 48%。— 来源：Capital & Compute, "Why SSDs Are So Expensive in 2026: The NAND Squeeze", 2026, https://capitalandcompute.net/blog/why-are-ssds-so-expensive/ (retrieved 2026-11-01) [VERIFY: bit 占比数字]
- 前五大 NAND 供应商营收在 4Q25 环比增长 23.8%，1Q26 环比增长 83.7%（超过 $38.9B），2Q26 环比增长 77%（达 $68.87B）。— 来源：TrendForce, "AI Server Storage Demand Surges; Top Five NAND Flash Suppliers Post 23.8% QoQ Revenue Growth in 4Q25", 2026-03-03, https://www.trendforce.com/presscenter/news/20260303-12943.html (retrieved 2026-11-01); iConnect007 (TrendForce), "Combined Revenue of Top Five Global NAND Flash Suppliers Rose by 83.7% QoQ for 1Q26", 2026-05, https://iconnect007.com/article/150139/combined-revenue-of-top-five-global-nand-flash-suppliers-rose-by-837-qoq-for-1q26/150136/smt (retrieved 2026-11-01); TrendForce, 2026-08-18 (URL above)
- 2Q26 前五大企业级 SSD 厂商营收约达 $37.59B。— 来源：TrendForce, "Higher Prices and Shipments Drive Top Five Enterprise SSD Vendors' Revenue to Nearly US$37.59 Billion in 2Q26", 2026-09-01, https://www.trendforce.com/presscenter/news/20260901-13210.html (retrieved 2026-11-01)

**TrendForce NAND 合约价环比预测（可直接转为 CSV）**

| 季度,NAND合约价环比,企业级SSD环比,来源说明 |
|---|
| 1Q26,+33-38%（1 月）/ +55-60%（2 月修订）,+53-58%（2 月修订）,[VERIFY 修订数字] |
| 2Q26,+70-75%,n/a,[VERIFY] |
| 3Q26,+10-15%,n/a,TrendForce 2026-08-18 |
| 4Q26,+15-20%,+23-28%,TrendForce 2026-09-30 |

**2Q26 NAND 供应商营收（TrendForce，可直接转为 CSV）**

| 排名,供应商,营收_十亿美元,环比增长,份额说明 |
|---|
| 1,Samsung,23.06,+70.7%,~33%（推算） |
| 2,SK hynix Group（含 Solidigm）,14.27,+89.5%,~21%（推算） |
| 3,Micron,11.85,+99.2%,~17%（推算） |
| 4,Kioxia,10.72,+79.9%,13.6%（TrendForce 公布） |
| 5,Sandisk,8.97,+50.7%,~13%（推算） |
| -,前五合计,68.87,+77%, |
— 来源：TrendForce, "Combined Revenue of Top Five NAND Flash Brands Rises 77% QoQ in 2Q26; Micron Moves Up to Third Place, Says TrendForce", 2026-08-18, https://www.trendforce.com/presscenter/news/20260818-13186.html (retrieved 2026-11-01)。推算份额是相对于前五合计的占比，并非 TrendForce 数字 [VERIFY: 官方份额列]。

### 5.6 HDD 与 SSD 的 $/TB
- Vdura 的指数（经 Forbes 报道）显示，2026 年第一季度 30 TB QLC 企业级 SSD 的 $/TB 是 30 TB HDD 的 22.6 倍。Vdura 稍后的一次读数约为 14.9 倍（2026 年 8 月），2026 年第三季度指数约为 18.6 倍。被引用的 Coughlin 数字为 20 倍以上。TrendForce 给出的企业级 QLC 每 GB 价格约为 HDD 的 15 倍。Vdura 数据显示，30 TB TLC SSD 价格从 2025 年第二季度到 2026 年第一季度上涨 472%，而 HDD 上涨 35%。— 来源：PCSP, "Enterprise SSD Prices 2026: How to Buy Server Storage Now", 2026, https://pcserverandparts.com/news/enterprise-ssd-prices-2026-server-storage-buying-guide/ (retrieved 2026-11-01); DatacenterDisk, "The SSD/HDD Price Divergence Report 2026", 2026, https://datacenterdisk.com/reports/ssd-hdd-price-divergence-2026 (retrieved 2026-11-01) [VERIFY: 大多数数字都可追溯到同一家厂商（Vdura）；需找到 Forbes 原文]
- 历史基线：2020 年企业级 SSD 的 $/TB 约为近线（nearline）HDD 的 10 倍。— 来源：Blocks & Files, "Enterprise SSDs are ten times the price of nearline disk drives", 2020-05-15, https://blocksandfiles.com/2020/05/15/enterprise-ssds-are-ten-x-cost-of-nearline-disk-drives/ (retrieved 2026-11-01)
- 据报道（引用 TrendForce），2026 年近线 HDD 交货周期超过 52 周。— 来源：PCSP, "Hard Drive Shortage 2026: Nearline Is Sold Out", 2026, https://pcserverandparts.com/news/hard-drive-shortage-2026-what-to-do/ (retrieved 2026-11-01) [VERIFY]

### 5.7 公司事件
- Sandisk 完成与 Western Digital 的分拆，于 2025-02-24 以 SNDK 代码在 Nasdaq 上市交易。WDC 保留 HDD 业务。— 来源：Sandisk IR, "Sandisk Celebrates Nasdaq Listing After Completing Separation from Western Digital", 2025-02-24, https://investor.sandisk.com/news-releases/news-release-details/sandisk-celebrates-nasdaq-listing-after-completing-separation (retrieved 2026-11-01)
- Kioxia 的 IPO 定价为 ¥1,455/股（区间 ¥1,390–1,520），对应估值约 ¥784B，募资约 ¥120B（~$800M），出售方为 Bain 和 Toshiba。它于 2024-12-18 在东证 Prime 市场（TSE Prime）上市，开盘价 ¥1,440，首日收于 ¥1,601（市值 ~¥863B）。— 来源：Nippon.com (Jiji), "Kioxia Sets IPO Price at 1,455 Yen", 2024-12-09, https://nippon.com/en/news/yjj2024120900937 (retrieved 2026-11-01); Nippon.com (Jiji), "Chipmaker Kioxia Makes Solid Stock Market Debut", 2024-12-18, https://nippon.com/en/news/yjj2024121800877 (retrieved 2026-11-01)

---

## 6. 市场规模

### 6.1 IDC 外置企业存储
- 3Q25：市场同比增长 2.1%。Dell 占 22.7%，Huawei 以 12.0% 位列第 2，NetApp 以 9.4% 位列第 3。— 来源：IDC, "Worldwide External Enterprise Storage Systems Market Revenue Increased 2.1% During the Third Quarter of 2025", 2025-12, https://my.idc.com/getdoc.jsp?containerId=prUS54034425 (retrieved 2026-11-01)
- 4Q25：$9.7B，同比增长 5.5%，Dell 占 23.7%。— 来源：Remio (citing IDC), "IDC Enterprise Storage Market Surges, but Higher Spending Hides a Cost Squeeze", 2026, https://www.remio.ai/post/idc-enterprise-storage-market-surges-but-higher-spending-hides-a-cost-squeeze (retrieved 2026-11-01) [VERIFY: 需对照 IDC 新闻稿]
- 1Q26：$9.2B，同比增长 22.7%。Dell 占 31.2%，NetApp 以 9.9% 位列第 2。— 来源：IDC via PressReleasePoint, "Worldwide External Enterprise Storage Systems Market Accelerates to 22.7% Growth in the First Quarter of 2026...", 2026-07-09, https://www.pressreleasepoint.com/worldwide-external-enterprise-storage-systems-market-accelerates-227-growth-first-quarter-2026 (retrieved 2026-11-01) [VERIFY: 与相邻季度相比，Dell 31.2% 显得偏高]
- 2Q26：$10.3B，同比增长 33.6%。全闪存阵列 $5.4B（+42.9%，占营收 52.1%）。Dell 以 23.8% 位列第 1（+42.5%），Huawei 以 11.3% 位列第 2（+29.4%），NetApp 占 9.6%（+35.7%），Everpure 以 8.1% 位列第 4（增长最快，约 +50%），HPE 以 6.8% 位列第 5（+31.9%）。— 来源：StorageReview, "IDC External Storage Tracker: $10.3 Billion in Q2 2026 as Server Market Tops $166 Billion on AI Demand", 2026-09, https://www.storagereview.com/news/idc-external-storage-tracker-q2-2026-10-3-billion-as-server-market-tops-166-billion (retrieved 2026-11-01); Blocks & Files, "IDC's latest enterprise storage tracker shows booming storage market growth", 2026-09-23, https://www.blocksandfiles.com/flash/2026/09/23/idcs-latest-enterprise-storage-tracker-shows-booming-storage-market-growth/5298577 (retrieved 2026-11-01) [VERIFY: NetApp 排名第 3 系推断；未检索到 IBM/Hitachi 份额]

**IDC 外置企业存储（可直接转为 CSV）**

| 季度,营收_十亿美元,同比,Dell份额,Huawei份额,NetApp份额,Everpure/Pure份额,HPE份额 |
|---|
| 3Q25,n/a,+2.1%,22.7%,12.0%,9.4%,n/a,n/a |
| 4Q25,9.7,+5.5%,23.7%,n/a,n/a,n/a,n/a |
| 1Q26,9.2,+22.7%,31.2% [VERIFY],n/a,9.9%,n/a,n/a |
| 2Q26,10.3,+33.6%,23.8%,11.3%,9.6%,8.1%,6.8% |

### 6.2 AI 存储潜在市场规模（TAM）
- 由于定义不同，分析机构的估算差异很大。Grand View Research：从 $30.57B（2024 年）增至 $118.38B（2030 年），CAGR 25.9%。Lucintel：2030 年 $73.6B（CAGR 21.8%）。GII：2030 年 $141.7B。Allied：2031 年 $162.5B。— 来源：Grand View Research, "AI-Powered Storage Market Report", n.d., https://www.grandviewresearch.com/industry-analysis/ai-powered-storage-market-report (retrieved 2026-11-01); Lucintel, "AI Powered Storage Market", n.d., https://lucintel.com/ai-powered-storage-market.aspx (retrieved 2026-11-01); Allied Market Research, "AI Powered Storage Market Insights, 2031", n.d., https://alliedmarketresearch.com/ai-powered-storage-market-A09518 (retrieved 2026-11-01) [VERIFY: 未找到 IDC 或 Gartner 的 AI 存储 TAM；这些数字应视为低可信度的市场研究数据]
- Gartner：预测 2026 年数据中心用电量为 565 TWh，较 2025 年的 447 TWh 增长 26%，其中 AI 优化服务器占 31%。— 来源：Gartner, "Gartner Says Data Center Electricity Consumption to Grow 26% in 2026", 2026-06-10, https://www.gartner.com/en/newsroom/press-releases/2026-06-10-gartner-says-data-center-electricity-demand-to-grow-26-percent-in-2026 (retrieved 2026-11-01)
- 文件与对象存储市场规模：未检索到。[VERIFY: IDC/Gartner 的文件与对象存储数据]

---

## 7. 超大规模云厂商的存储系统

- **Google Colossus** 是 GFS 的集群级继任者，元数据由存放在 Bigtable 中的 "curators"（管理器）持有。Google 的 L4 分布式 SSD 缓存采用机器学习驱动的放置策略，决定哪些文件放在 SSD 上、哪些放在 HDD 上，支持读缓存和回写（writeback）两种模式。— 来源：Google Cloud Blog, "How Colossus optimizes data placement for performance", 2025-03, https://cloud.google.com/blog/products/storage-data-transfer/how-colossus-optimizes-data-placement-for-performance (retrieved 2026-11-01); The Register, "Even Google struggles to balance fast-but-pricey flash and cheap-but-slow hard disks", 2025-03-27, https://www.theregister.com/2025/03/27/google_l4_storage_performance_improvements/ (retrieved 2026-11-01)
- Google 的 Rapid Storage（可用区级 Cloud Storage）通过 gRPC 流式传输使用 Colossus 有状态协议。它与 Cloud Storage FUSE 集成，Google 给出的目标为每秒 2,000 万（20M）次请求和 6 TB/s。— 来源：Google Cloud Blog, "How the Colossus stateful protocol benefits Rapid Storage", 2025-04, https://cloud.google.com/blog/products/storage-data-transfer/how-the-colossus-stateful-protocol-benefits-rapid-storage (retrieved 2026-11-01) [VERIFY: 20M/6TB/s 来自一次会议演讲]
- **Meta Tectonic** 是 Meta 的 EB 级多租户分布式文件系统，见论文 "Facebook's Tectonic Filesystem: Efficiency from Exascale"（Pan et al., FAST '21, pp. 217–231）。每个集群服务整个数据中心。— 来源：USENIX, "Facebook's Tectonic Filesystem: Efficiency from Exascale", 2021-02, https://www.usenix.org/conference/fast21/presentation/pan (retrieved 2026-11-01); Meta Engineering, "Tectonic file system: Consolidating Facebook storage infrastructure", 2021-06-21, https://engineering.fb.com/2021/06/21/data-infrastructure/tectonic-file-system/ (retrieved 2026-11-01)
- **Meta GenAI 存储（2024 年）**：两个 24,576-GPU 集群在针对闪存优化的 Tectonic 上使用 FUSE API，另加一套与 Hammerspace 联合开发的并行 NFS，运行在配备 E1.S SSD 的 YV3 Sierra Point 服务器上。— 来源：Meta Engineering, "Building Meta's GenAI Infrastructure", 2024-03-12 (URL above) (retrieved 2026-11-01)
- Meta 的演讲材料描述了每机架超过 10 PB 的 QLC 机架。— 来源：FMS 2025 proceedings, "QLCP-201-1 (Gupta)", 2025-08-06, https://files.futurememorystorage.com/proceedings/2025/20250806_QLCP-201-1_Gupta.pdf (retrieved 2026-11-01) [VERIFY: 演讲者是否隶属 Meta]
- Pure Storage（2024 年末）和 Everpure（2026-08-10）先后赢得前五大超大规模云厂商的 DirectFlash 设计导入（design win）。第一家是 Meta。第二家未披露，结构为一份涵盖软件和非 NAND 部件的主供货协议（master supply agreement），由该超大规模云厂商自行采购 NAND，预计自 FY2028 起贡献营收。— 来源：Everpure, "Everpure Lands New Design Win with Second Top Five Hyperscaler", 2026-08-10, https://www.everpuredata.com/company/newsroom/press-releases/everpure-lands-new-design-win-with-second-top-five-hyperscaler.html (retrieved 2026-11-01)
- **AWS S3 Express One Zone** 于 re:Invent 2023（2023-11-28）发布，引入目录桶（directory bucket）类型。AWS 声称其访问速度比 S3 Standard 快 10 倍，请求成本低 50%。— 来源：AWS What's New, "Announcing the Amazon S3 Express One Zone storage class", 2023-11, https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-s3-express-one-zone-storage-class (retrieved 2026-11-01)
- **S3 Tables**（带托管压实/合并的 Apache Iceberg 表桶）于 re:Invent 2024（2024 年 12 月）发布。re:Invent 2025 新增 Intelligent-Tiering 和跨区域/跨账户复制。— 来源：AWS S3 User Guide, "What's New", n.d., https://docs.aws.amazon.com/AmazonS3/latest/userguide/WhatsNew.md (retrieved 2026-11-01); NAND Research, "AWS S3 AI-focused enhancements", 2025-12, https://nand-research.com/research-note-aws-s3-ai-focused-enhancements (retrieved 2026-11-01)
- **S3 Vectors** 于 2025-07-15 进入预览，并于 re:Invent 2025（2025 年 12 月）正式发布（GA）：每个索引 20 亿（2B）个向量（预览版为 50M），每个桶最多 20 万亿（20T）个向量，覆盖 14 个区域。AWS 声称成本最多降低 90%。— 来源：StorageNewsletter, "AWS re:Invent 2025: Amazon S3 Vectors is Now Generally Available with 40 Times the Scale of Preview", 2025-12-05, https://www.storagenewsletter.com/2025/12/05/aws-reinvent-2025-amazon-s3-vectors-is-now-generally-available-with-40-times-the-scale-of-preview/ (retrieved 2026-11-01)
- **FSx for Lustre**：未检索到 2025–26 年的具体信息。[VERIFY]
- **Azure Managed Lustre**：Microsoft 门户文档显示，通过支持请求最多可达 12.5 PiB，吞吐量档位为每 TiB 40/125/250/500 MB/s（档位信息来自一个合作伙伴页面）。它是首个参加 MLPerf Storage（v3.0）的超大规模云服务。— 来源：Microsoft Learn, "Create an Azure Managed Lustre file system by using the Azure portal", n.d., https://learn.microsoft.com/en-us/azure/azure-managed-lustre/create-file-system-portal (retrieved 2026-11-01) [VERIFY: 当前最大容量]
- **Azure Blob**：Microsoft 表示 Blob 可扩展至 EB 级、数十 Tbps，并向 GPU 提供数百万 IOPS，为 OpenAI 的工作负载提供底层支撑。— 来源：Microsoft Azure Blog (WP JSON feed), post 48707, n.d., https://azure.microsoft.com/en-us/blog/wp-json/wp/v2/posts/48707 (retrieved 2026-11-01) [VERIFY: 标题/日期]

---

## 8. 新兴 GPU 云（neocloud）

- **CoreWeave**：提供 CoreWeave AI Object Storage 及 **LOTA**（Local Object Transport Accelerator，本地对象传输加速器）——部署在每个 GPU 和 CPU 节点上的代理/缓存。CoreWeave 声称每个 GPU 最高可达 7 GB/s，LOTA Cross-Cloud 处于预览阶段。列出的专用存储合作伙伴为 VAST、WEKA（NeuralMesh）、DDN、IBM Storage Scale 和 Pure Storage。— 来源：CoreWeave, "Storage" product page, n.d., https://coreweave.com/products/storage (retrieved 2026-11-01); CoreWeave, "CoreWeave Unveils AI Object Storage...", 2025, https://coreweave.com/news/coreweave-unveils-ai-object-storage-redefining-how-ai-workloads-access-and-scale-data (retrieved 2026-11-01)
- VAST 与 CoreWeave 签署了一份 $1.17B 的商业协议（2025 年 11 月）。The Next Platform 称 CoreWeave 是 VAST 的"头号客户"。— 来源：Blocks & Files, "VAST Data lands $1.17 billion CoreWeave deal", 2025-11-06, https://www.blocksandfiles.com/ai-ml/2025/11/06/vast-data-lands-117-billion-coreweave-deal/1608868 (retrieved 2026-11-01); The Next Platform, "VAST Data's $1.17 Billion Deal With CoreWeave Is A Leading Indicator", 2025-11-07, https://www.nextplatform.com/2025/11/07/vast-datas-1-17-billion-deal-with-coreweave-is-a-leading-indicator/ (retrieved 2026-11-01)
- Backblaze 与 CoreWeave 签署了一份为期 5 年、多 EB 级、价值 $335M 的存储协议。— 来源：Blocks & Files, "Backblaze gets $335 million CoreWeave bonanza", 2026-06-23, https://blocksandfiles.com/public-cloud/2026/06/23/backblaze-gets-335-million-coreweave-bonanza/5260288 (retrieved 2026-11-01)
- **Nebius** 为其 AI Cloud 的高端层选择了 WEKA（2025 年 6 月），为一位客户部署了 2 PB。Nebius 也是 MLPerf Storage v3.0 的首次提交方。— 来源：WEKA, "WEKA and Nebius Partner to Deliver High-Performance AI Data Infrastructure", 2025-06, https://www.weka.io/news/weka-nebius-partner-high-performance-ai-data-infrastructure (retrieved 2026-11-01)
- **Lambda** 使用 VAST（并对外宣传与 WEKA 的合作）作为其云的后端存储。第三方追踪方对这些合作在多大程度上面向客户说法不一。— 来源：Saturn Cloud, "GPU Cloud Comparison: 17 Neoclouds for AI in 2025", 2025, https://saturncloud.io/blog/gpu-cloud-comparison-neoclouds-2025/ (retrieved 2026-11-01) [VERIFY: Lambda/VAST 的一手公告]
- **Crusoe** 提供基于 Lightbits 的块存储和由 VAST 支撑的共享磁盘，另有原生对象存储。— 来源：same as above. [VERIFY: 一手来源]
- **Together AI**：未披露存储厂商。[VERIFY]
- CoreWeave、Crusoe、IREN、Lambda、Mistral AI、Nebius、OCI 和 Vultr 被列为 NVIDIA STX/CMX 上下文内存存储的早期采用者。— 来源：StorageNewsletter, 2026-03-17 (URL in 1.6) (retrieved 2026-11-01)

---

