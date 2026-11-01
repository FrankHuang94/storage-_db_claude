# AI 存储竞争格局：VAST Data、WEKA、DDN（及相邻厂商）

> 📄 英文原文：[meta/research/vast-weka-ddn.md](../../../meta/research/vast-weka-ddn.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

研究笔记编制于 2026-11-01。检索方法：网页搜索（约 40 次查询）。本研究环境中直接抓取网页被拦截（cnbc.com 和 blocksandfiles.com 无法解析），因此以下大多数事实来自所引页面的搜索结果摘录，而非完整阅读页面。凡仅依赖单条摘录、低质量聚合网站，或未经独立核实的厂商声称的内容，均标注 `[VERIFY: ...]`。

**私营公司经营数据的标签：**
- *公司自述*（company-stated）：公司自己的新闻稿、博客或高管表态
- *媒体报道（媒体名称）*（reported by press (outlet)）：记者或媒体援引消息来源进行的报道
- *估算*（estimated）：第三方追踪机构或分析师的估算

---

## 1. VAST Data

### 1.1 创立与里程碑

- VAST Data 由 Renen Hallak（CEO，曾为 XtremIO 早期工程师及研发负责人）、Shachar Fienblit（曾任职 Kaminario）和 Jeff Denworth（曾任职 CTERA）于 2016 年初创立。美国主要办公室位于纽约，研发在以色列。— 来源：Blocks & Files, "VAST Data's business sitrep", 2019-02-26, https://blocksandfiles.com/2019/02/26/vast-datas-business-sitrep/ (retrieved 2026-11-01)
- Wikipedia 给出的创立时间为 January 2016，并称公司没有单一总部：列出的办公地点包括 New York City、Durham、Campbell 和 Yafo。部分来源还将 Alon Horev 计为联合创始人。— 来源：Wikipedia, "VAST Data", n.d., https://en.wikipedia.org/wiki/VAST_Data (retrieved 2026-11-01) [VERIFY: Alon Horev 的联合创始人身份仅来自一个聚合网站（caproasia.com）]
- 在一条 2026 年的摘录中，Calcalist 称 Jeff Denworth 已不再担任运营职务。而其他 2026 年的资料仍将其描述为负责产品与商业战略的联合创始人，并且他曾在 VAST Forward 2026 上发表演讲。— 来源：Calcalist (CTech), article 68ml6rrio, n.d., https://www.calcalistech.com/ctechnews/article/68ml6rrio (retrieved 2026-11-01) [VERIFY: 两种说法相互矛盾，且文章日期不详]
- 公司于 February 2019 携"Universal Storage"结束隐身模式。— 来源：StorageReview, "VAST Data emerges from stealth with Universal Storage", 2019-02, https://www.storagereview.com/news/vast-data-emerges-from-stealth-with-universal-storage (retrieved 2026-11-01)
- April 2021，VAST 停止销售自有硬件，转向"Gemini"模式下的软件订阅。— 来源：Blocks & Files, "VAST Data exits hardware business, pivots to software subscriptions", 2021-04-06, https://blocksandfiles.com/2021/04/06/vast-data-software-subscriptions-pivot/ (retrieved 2026-11-01)
- 一项战略合作将 VAST 文件软件纳入 HPE GreenLake for File Storage。— 来源：Business Wire, "VAST Data Announces Strategic Partnership with Hewlett Packard Enterprise to Provide Software for HPE GreenLake for File Storage", https://www.businesswire.com/news/home/20211217005009/en (retrieved 2026-11-01) [VERIFY: URL 暗示为 December 2021，但其他报道将 HPE 产品发布时间定为 2023 年]
- May 2025，VAST 将自身重新定位为"VAST AI Operating System"（AI OS，AI 操作系统），以 AgentEngine 为主要新组件。— 来源：Blocks & Files, "VAST Data launches AI operating system", 2025-05-21, https://www.blocksandfiles.com/ai-ml/2025/05/21/vast-data-launches-ai-operating-system/1613219 (retrieved 2026-11-01)
- November 2025，VAST 宣布与 CoreWeave 达成 US$1.17B 的商业协议（详见 1.5），以及与 Google Cloud 和 Microsoft Azure 的集成。— 来源：StorageNewsletter, "Vast Data Secures Commercial Partnership Deal with CoreWeave for $1.17 Billion to Power the Next Generation of AI", 2025-11-07, https://www.storagenewsletter.com/2025/11/07/vast-data-secures-commercial-partnership-deal-with-coreweave-for-1-17-billion-to-power-the-next-generation-of-ai/ (retrieved 2026-11-01)
- February 2026，VAST 发布 CNode-X（配备 GPU 的 CNode）、PolicyEngine 和 TuningEngine。— 来源：HPCwire, "VAST Data Expands AI Data Stack, Keeps Eye on North Star", 2026-02-25, https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/ (retrieved 2026-11-01)
- 公司首届用户大会 VAST Forward 2026 约于 March 2026 在 Salt Lake City 举行。— 来源：search extract of a NYSE-hosted interview listing, "VAST Forward 2026: co-founder Jeff Denworth explains VAST's profitability", 2026-03, (mirror) https://git.handmade.network/vast-forward-2026-co-founder-jeff-denworth-explains-vast-s-profitability.html (retrieved 2026-11-01) [VERIFY: 仅找到一个抓取镜像；需在 vastdata.com 上确认地点和日期]
- Series F 于 2026-04-22 以 US$30B 估值完成交割（详见 1.3）。— 来源：CNBC, "Nvidia backs AI company Vast Data at $30 billion valuation", 2026-04-22, https://www.cnbc.com/2026/04/22/nvidia-backs-ai-company-vast-data.html (retrieved 2026-11-01)

### 1.2 技术

- **DASE（Disaggregated, Shared-Everything，分解式全共享架构）**：无状态计算节点（CNode）与存储机柜（DBox）分离，DBox 中装有存储级内存（SCM）和 QLC 闪存。每个 CNode 都能通过 NVMe-oF 访问每个设备，因此任何 CNode 都能处理任何请求，节点之间无需东西向协调流量。— 来源：VAST Data, "How it works", n.d., https://vastdata.com/how-it-works (retrieved 2026-11-01)
- Cisco 的解决方案简介也描述了在 Cisco UCS 上运行的 VAST 所采用的 CNode/DBox 拆分以及 SCM 加 QLC 的介质设计。— 来源：Cisco, "VAST Data on Cisco UCS (solution overview)", n.d., https://www.cisco.com/c/en/us/solutions/collateral/artificial-intelligence/vast-data-ucs-ds.pdf (retrieved 2026-11-01)
- **Element Store**：VAST 的内部数据结构。SCM 吸收写入并保存元数据，数据随后以大块、对闪存友好的条带写入 QLC。基于相似性的数据缩减属于这一层。— 来源：VAST Data, "How it works", n.d., https://vastdata.com/how-it-works (retrieved 2026-11-01)
- **基于相似性的数据缩减**：VAST 称其为全局、字节粒度的数据缩减。一场 VAST 网络研讨会引用的真实数据集缩减比中位数约为 2:1，而一个第三方百科条目称约为 3:1。— 来源：VAST Data, "Scaling Through Flash Scarcity" (webinar), n.d., https://www.vastdata.com/events/scaling-through-flash-scarcity (retrieved 2026-11-01) [VERIFY: 缩减比为厂商数字，且两个来源说法不一]
- **局部可解码纠删码（LDEC）**：采用宽条带，开销极低。VAST 称低于 3%（部分材料为 2.7%）。重建时只需读取约四分之一的存活数据，而 Reed-Solomon 需要读取所有存活条带。— 来源：VAST Data blog, "Beyond Better Codes (Providing Resilience Efficiently, Part II)", n.d., https://vastdata.com/blog/providing-resilience-efficiently-part-ii (retrieved 2026-11-01)
- **多协议访问**：通过 NFS（含 NFS over RDMA）、SMB 和 S3 访问同一份数据，后来又增加了块存储。AI OS 材料中还出现了兼容 Kafka 的事件流。— 来源：VAST Data, "Supported Platforms / Specifications", n.d., https://www.vastdata.com/specifications (retrieved 2026-11-01) [VERIFY: 需对照当前文档确认块存储和 Kafka 协议清单]
- **VAST DataBase**：平台内置的表格/列式数据库，于 2023 年随"VAST Data Platform"推出。它现在是 DataEngine 和向量搜索功能的基础。— 来源：The Next Platform, "VAST Data: What controls the data is more important than what stores it", 2026-02-27, https://www.nextplatform.com/store/2026/02/27/vast-data-what-controls-the-data-is-more-important-than-what-stores-it/4092860 (retrieved 2026-11-01)
- **DataSpace**：横跨多个站点和云的全局命名空间。November 2025，它被扩展为 Google Cloud 托管服务的混合命名空间。— 来源：SDxCentral, "Google Cloud enlists VAST Data to support AI multi-environment deployments", 2025-11, https://www.sdxcentral.com/news/google-cloud-enlists-vast-data-to-support-ai-multi-environment-deployments/ (retrieved 2026-11-01)
- **DataEngine**：平台内部的无服务器、事件触发执行层（函数、触发器、容器）。— 来源：Futuriom, "VAST Data Declares Itself an AI Operating System", 2025-05, https://www.futuriom.com/articles/news/vast-data-declares-itself-an-ai-operating-system/2025/05 (retrieved 2026-11-01)
- **InsightEngine**：为 AI 使用准备数据，包括实时嵌入向量生成、索引和 RAG。据 HPCwire，它于 October 2024 推出；另一来源称为 March 2025。— 来源：HPCwire, "VAST Data Expands AI Data Stack, Keeps Eye on North Star", 2026-02-25, https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/ (retrieved 2026-11-01) [VERIFY: 不同来源的发布日期相互矛盾]
- **AgentEngine**：用于部署 AI 智能体（agent）的自动扩缩运行时，提供低代码环境并支持兼容 MCP 的工具。它是 May 2025 AI OS 发布的核心组件。— 来源：Blocks & Files, "VAST Data launches AI operating system", 2025-05-21, https://www.blocksandfiles.com/ai-ml/2025/05/21/vast-data-launches-ai-operating-system/1613219 (retrieved 2026-11-01)
- **当前命名（2026）**：总品牌为"VAST AI Operating System"（AI OS）。其组件包括 DataStore、DataBase、DataSpace、DataEngine、InsightEngine、AgentEngine、SyncEngine（August 2025），以及 TuningEngine 和 PolicyEngine（February 2026 发布，预计 2026 年底前推出）。还提到了一个"Polaris"控制平面。— 来源：HPCwire, "VAST Data Expands AI Data Stack, Keeps Eye on North Star", 2026-02-25, https://www.hpcwire.com/2026/02/25/vast-data-expands-ai-data-stack-keeps-eye-on-north-star/ (retrieved 2026-11-01) [VERIFY: Polaris 是否为独立产品名称]
- **CNode-X（February 2026）**：一种配备 NVIDIA GPU 的新型 CNode，在 DataEngine 和 DataBase 内运行 cuVS 等 NVIDIA 库，实现 GPU 加速的向量搜索与分析。它还将支持 NVIDIA 用于 KV 缓存的 Context Memory Storage（CMS）平台，并于 2026 年晚些时候通过 Cisco 和 Supermicro 等 OEM 供货。— 来源：Datacenter Dynamics, "VAST Data integrates AI OS into Nvidia GPU-powered servers", 2026-02-25, https://www.datacenterdynamics.com/en/news/vast-data-integrates-ai-os-into-nvidia-gpu-powered-servers/ (retrieved 2026-11-01)
- **硬件合作伙伴**：VAST 的规格页面列出了 Supermicro、HPE 和 Cisco 平台。Lenovo 出现在 VAST 的合作伙伴列表和 OEM 招聘信息中，但未发现 Lenovo 硬件的发布。Supermicro 也为 February 2026 的 CNode-X 发布单独发布了新闻稿。— 来源：VAST Data, "Supported Platforms", n.d., https://www.vastdata.com/specifications (retrieved 2026-11-01); Supermicro, "Supermicro and VAST Data launch new enterprise AI data platform solution (NVIDIA)", 2026-02-25, https://www.supermicro.com/de/pressreleases/supermicro-and-vast-data-launch-new-enterprise-ai-data-platform-solution-nvidia (retrieved 2026-11-01) [VERIFY: Lenovo 是否为已出货的 OEM]
- Cisco 通过其销售团队和渠道，在部分 UCS 服务器上原生提供 VAST，并与 Nexus HyperFabric AI 一同发布。— 来源：Blocks & Files, "VAST links up with Equinix and Cisco", 2024-10-01, https://www.blocksandfiles.com/ai-ml/2024/10/01/vast-links-up-with-equinix-and-cisco/1589567 (retrieved 2026-11-01)

### 1.3 融资与估值

- **Series C（April 2020）**：以 US$1.2B 估值融资 US$100M，由 Next47 领投（*公司自述*）。— 来源：VAST Data press release, "VAST Data Raises $100 Million in Series C Funding at $1.2 Billion Valuation…", 2020-04, https://vastdata.com/news-post/vast-data-raises-100-million-in-series-c-funding-at-1-2-billion-valuation-to-democratize-flash-for-all-data (retrieved 2026-11-01)
- **Series D（May 2021）**：以 US$3.7B 投后估值融资 US$83M，由 Tiger Global 领投，NVIDIA 参投。累计融资额达到约 US$263M。— 来源：StorageNewsletter, "Vast Data Raised $83 Million, Total Reaching $263 Million", 2021-05-05, https://www.storagenewsletter.com/2021/05/05/vast-data-raised-83-million-total-reaching-263-million/ (retrieved 2026-11-01)
- **Series E（December 2023）**：以 US$9.1B 估值融资 US$118M，由 Fidelity Management & Research 领投，NEA、BOND Capital 和 Drive Capital 参投。公司称，截至 2023 财年第三季度末，其累计软件订单额已超过 US$1B，ARR 超过 US$200M（*公司自述*）。— 来源：Blocks & Files, "VAST Data funding", 2023-12-06, https://blocksandfiles.com/2023/12/06/vast-data-funding/ (retrieved 2026-11-01)
- Crunchbase News 援引 The Information 报道称，部分 Series E 资金将用于回购现有股东的股票。— 来源：Crunchbase News, "Unicorn VAST Data valuation doubles (Fidelity)", 2023-12, https://news.crunchbase.com/ai/unicorn-vast-data-valuation-doubles-fidelity (retrieved 2026-11-01)
- **2025 年洽谈**：Globes 援引 Reuters 报道称，公司正与 Alphabet（Google）和 NVIDIA 进行深入洽谈，拟以最高 US$30B 的估值融资"数十亿美元"（*媒体报道*）。— 来源：Globes, "Storage co Vast Data raising several billion dollars - report", 2025, https://en.globes.co.il/en/article-storage-co-vast-data-raising-several-billion-dollars-report-1001517875 (retrieved 2026-11-01) [VERIFY: 未检索到确切日期]
- **February 2026**：Globes 报道称，公司计划进行一轮以老股转让为主的融资，让早期股东得以套现，估值约 US$25–27B（*媒体报道*）。— 来源：Blocks & Files, "VAST Data plans funding round so early stockholders can get cash", 2026-02-05, https://www.blocksandfiles.com/file/2026/02/05/vast-data-plans-funding-round-so-early-stockholders-can-get-cash/4090372 (retrieved 2026-11-01)
- **Series F（March 2026 宣布，2026-04-22 交割）**：总额约 US$1B，包括一级优先股资本和老股要约收购，估值 US$30B。Drive Capital 领投，Access Industries 联合领投，NVIDIA、Fidelity 和 NEA 参投（*公司自述*，被广泛报道）。— 来源：CNBC, "Nvidia backs AI company Vast Data at $30 billion valuation", 2026-04-22, https://www.cnbc.com/2026/04/22/nvidia-backs-ai-company-vast-data.html (retrieved 2026-11-01); Blocks & Files, "VAST Data raises $1B at $30B valuation as AI storage demand surges", 2026-03-11, https://www.blocksandfiles.com/flash/2026/03/11/vast-data-raises-1b-at-30b-valuation-as-ai-storage-demand-surges/5208106 (retrieved 2026-11-01)
  - [VERIFY: 低质量聚合网站 Silicon Valley Investclub 称领投方为 Alphabet 旗下 CapitalG 和 NVIDIA，这与新闻稿报道中 Drive Capital 和 Access Industries 领投的说法矛盾。CB Insights 和 Tracxn 列出 2026-03-10 一笔 US$500M 的 Series F。一级/二级拆分比例未披露。]
- 各聚合网站给出的累计融资总额不一：Tracxn 为 6 轮约 US$841M，CB Insights 约 US$381M（*估算*）。— 来源：Tracxn, "VAST Data – Funding Rounds & List of Investors", 2026, https://tracxn.com/d/companies/vast-data/__o_iHe4fP-R5GinLNlxxCqWO61A2Tre8oo1oVvlPZIno/funding-and-investors (retrieved 2026-11-01) [VERIFY: 两个总额均不可靠]

### 1.4 营收、ARR、盈利能力、员工人数

- 在 Series F 时，VAST 表示其**累计订单额已超过 US$4B**，FY2026（截至 January 2026 的财年）结束时**承诺 ARR（CARR）超过 US$500M**，营业利润率和自由现金流均为正，其"Rule of X"指标得分为 228%（*公司自述*）。— 来源：Futuriom, "VAST Data Hits $30 Billion Valuation Amid 'AI Revolution'", 2026-04, https://www.futuriom.com/articles/news/vast-data-hits-30-billion-valuation-amid-ai-revolution/2026/04 (retrieved 2026-11-01) [VERIFY: 部分摘录写作"exiting FY2025"，需对照新闻稿核实财年标注]
- VAST 的财年于 January 31 结束。据报道，截至 2025-01-31 的财年营收同比增长 3.6x（未给出美元金额）。— 来源：36Kr (EN), article 3439532843355779, 2025, https://eu.36kr.com/en/p/3439532843355779 (retrieved 2026-11-01) [VERIFY: 单一二手来源]
- Calcalist 报道称，2025 年初 ARR 超过 US$200M，并预计一年内增长至三倍（*媒体报道*）。Sacra 估算 January 2025 的 ARR 为 US$200M（*估算*）。— 来源：Sacra, "VAST Data", 2025, https://sacra.com/c/vast-data/ (retrieved 2026-11-01)
- 部分聚合网站称，到 2025 年底 ARR 年化运行率约为 US$2B（*估算*）。Blocks & Files 只是推测，鉴于 CoreWeave 交易，ARR"could even be topping $2 billion"（甚至可能超过 20 亿美元）。— 来源：Blocks & Files, "VAST Data raises $1B at $30B valuation as AI storage demand surges", 2026-03-11, https://www.blocksandfiles.com/flash/2026/03/11/vast-data-raises-1b-at-30b-valuation-as-ai-storage-demand-surges/5208106 (retrieved 2026-11-01) [VERIFY: 属推测；与公司自述的 US$500M+ CARR 相矛盾]
- **盈利历史**：VAST 多次表示其现金流为正。在 Series E 时，公司称已连续 12 个季度实现正现金流（*公司自述*）。— 来源：Crunchbase News, "Unicorn VAST Data valuation doubles (Fidelity)", 2023-12, https://news.crunchbase.com/ai/unicorn-vast-data-valuation-doubles-fidelity (retrieved 2026-11-01)
- **员工人数**：HPCwire 援引 March 2026 的一篇报道，称员工约 1,200 人，约三分之一在以色列。此前 Globes/Reuters 的报道称约 1,000 人，一半在以色列。TipRanks 列出截至 June 2026 为 1,217 人（*媒体报道/估算*）。— 来源：HPCwire, item p=189419, 2026, https://www.hpcwire.com/?p=189419 (retrieved 2026-11-01) [VERIFY: 均为近似数字]

### 1.5 客户与合作伙伴

- **CoreWeave**：一项 US$1.17B 的商业协议（Reuters 独家报道 2025-11-06，新闻稿 2025-11-07）使 VAST AI OS 成为 CoreWeave 整个 AI 云的主要数据平台。VAST 表示此类合同通常为期 3–5 年，未披露详细条款（总额为*公司自述*）。— 来源：StorageNewsletter, "Vast Data Secures Commercial Partnership Deal with CoreWeave for $1.17 Billion…", 2025-11-07, https://www.storagenewsletter.com/2025/11/07/vast-data-secures-commercial-partnership-deal-with-coreweave-for-1-17-billion-to-power-the-next-generation-of-ai/ (retrieved 2026-11-01)
- **Microsoft Azure（Ignite，November 2025）**：VAST AI OS 通过 Azure Native ISV Service 提供给 Azure 客户，并可从本地突发扩展到 Azure。两家公司还计划围绕 Microsoft 的定制 AI 芯片开展合作。财务条款未披露。— 来源：VAST Data press release, "VAST and Microsoft Azure Unite to Advance Agentic AI", 2025-11-18, https://www.vastdata.com/press-releases/vast-and-microsoft-azure-unite-to-advance-agentic-ai (retrieved 2026-11-01) [VERIFY: 新闻稿称"now available"（已上线），但 NAND Research 称"available soon"（即将上线），需核实 GA 状态]
- **Google Cloud（November 2025）**：通过 Google Cloud Marketplace 部署的全托管 VAST AI OS 服务，提供集成计费、混合 DataSpace 命名空间和 TPU 支持。— 来源：Blocks & Files, "VAST supports Google Cloud TPUs in managed service with Red Stapler's SW", 2025-11-11, https://blocksandfiles.com/2025/11/11/vast-supports-google-cloud-tpus-in-managed-service-with-red-staplers-sw/ (retrieved 2026-11-01)
- **xAI Colossus（Memphis）**：VAST 称自己是 Colossus 背后的数据平台（引用的 GPU 数量从 100,000 到 200,000+ 不等）。DDN 也有类似声称，两家都称自己扮演"主要"（primary）角色。— 来源：Blocks & Files, "DDN supplying storage for xAI's Colossus supercomputer", 2024-11-19, https://www.blocksandfiles.com/ai-ml/2024/11/19/ddn-supplying-storage-for-xais-colossus-supercomputer/1604044 (retrieved 2026-11-01) [VERIFY: 哪家厂商服务于 Colossus 的哪一层尚无定论]
- **新兴 GPU 云（neocloud）**：VAST 为 Lambda、Crusoe、Core42 和 Nebius 供货，并有 Nebius 客户案例。— 来源：VAST Data, "Accelerating Global Enterprise AI Adoption (Nebius customer story)", n.d., https://www.vastdata.com/customers/nebius (retrieved 2026-11-01); Fierce Network, "Here's why Nvidia-backed startup VAST Data is all the rage", n.d., https://www.fierce-network.com/cloud/heres-why-nvidia-backed-startup-vast-data-all-rage (retrieved 2026-11-01)
- **NVIDIA**：自 Series D 起成为投资方。February 2026 双方联合推出"end-to-end fully accelerated AI data stack"（端到端全加速 AI 数据栈，即 CNode-X），此前 VAST 已与 Supermicro 合作推出经 NVIDIA 认证的设计。— 来源：StreetInsider (press release), "VAST Data Introduces End-to-End Fully Accelerated AI Data Stack with NVIDIA", 2026-02-25, https://www.streetinsider.com/Press+Releases/VAST+Data+Introduces+End-to-End+Fully+Accelerated+AI+Data+Stack+with+NVIDIA/26058536.html (retrieved 2026-11-01)

### 1.6 基准测试

- VAST 从未提交过 MLPerf Storage（v1.0、v2.0 或 v3.0）。— 来源：StorageReview, "MLPerf Storage v3.0: 877 GiB/s Checkpoints, a Cloud First, and a Leaderboard Turned Over", 2026-09, https://www.storagereview.com/news/mlperf-storage-v3-0-877-gib-s-checkpoints-a-cloud-first-and-a-leaderboard-turned-over (retrieved 2026-11-01) [VERIFY: 需对照 MLCommons 结果表核实]
- 本研究未发现 VAST 提交 IO500 或 SPECstorage 的记录。

### 1.7 市场进入策略（GTM）

- **Gemini 模式（April 2021）**：客户以成本价从制造合作伙伴（点名为 Avnet）购买经认证的硬件，并向 VAST 支付按容量定价、包含支持服务的软件订阅费。VAST 称订阅可续约最长 10 年且不涨价。每 TB 费率未公开。— 来源：VAST Data, "What is Gemini", n.d., https://vastdata.com/what-is-gemini (retrieved 2026-11-01); The Next Platform, "VAST Data Sheds Hardware Business To Tackle Largest Users", 2021-04-06, https://www.nextplatform.com/2021/04/06/vast-data-sheds-hardware-business-to-tackle-largest-users/ (retrieved 2026-11-01)
- VAST 还通过 OEM（HPE GreenLake for File Storage、Cisco UCS、Supermicro 全栈解决方案）以及云市场（Google Cloud 托管服务、Azure Native ISV Service、AWS）销售。— 来源：Blocks & Files, "VAST supports Google Cloud TPUs in managed service…", 2025-11-11, https://blocksandfiles.com/2025/11/11/vast-supports-google-cloud-tpus-in-managed-service-with-red-staplers-sw/ (retrieved 2026-11-01)

---
