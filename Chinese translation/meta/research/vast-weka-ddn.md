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

## 2. WEKA（原 WekaIO）

### 2.1 创立与里程碑

- WEKA 由 Liran Zvibel（CEO）、Maor Ben-Dayan 和 Omri Palmon 于 2013 年在以色列创立。公司现总部位于加州 Campbell，品牌已由 WekaIO 更名为 WEKA。— 来源：StorageNewsletter, "Start-up profile: Weka.io", 2016-12-26, https://www.storagenewsletter.com/2016/12/26/start-up-profile-weka-io (retrieved 2026-11-01)
- **June 2022**：WEKA 4 新增原生多云支持（AWS、GCP、Azure、OCI）。— 来源：HPCwire, "WEKA Unveils Multicloud Data Platform for AI and Next-Gen Workloads", 2022-06, https://www.hpcwire.com/off-the-wire/weka-unveils-multicloud-data-platform-for-ai-and-next-gen-workloads/ (retrieved 2026-11-01)
- **May 2024**：一轮 US$140M 的 Series E 使 WEKA 以 US$1.6B 估值成为独角兽（见 2.3）。— 来源：WEKA, "WEKA Nets $140M in Series E Funding at $1.6B Valuation", 2024-05-15, https://www.weka.io/news/weka-nets-140m-in-series-e-funding-at-1-6b-valuation (retrieved 2026-11-01)
- **February 2025**：一次市场进入（GTM）重组裁减约 50 个岗位，同时 WEKA 仍计划招聘约 120 人。CEO 公开信称 WEKA 于 2024 年 ARR 突破 US$100M。— 来源：Blocks & Files, "WEKA restructures for the GenAI era", 2025-02-07, https://www.blocksandfiles.com/ai-ml/2025/02/07/weka-restructures-for-the-genai-era/1599204 (retrieved 2026-11-01)
- **March 2025（GTC）**：WEKA 发布 Augmented Memory Grid，并获得 WEKApod Nitro 的 NVIDIA 认证。— 来源：AIwire/HPCwire, "WEKA Expands NVIDIA Integrations and Certifications, Unveils Augmented Memory Grid", 2025-03-19, https://www.hpcwire.com/aiwire/2025/03/19/weka-expands-nvidia-integrations-and-certifications-unveils-augmented-memory-grid/ (retrieved 2026-11-01)
- **June 2025**：NeuralMesh 推出，是对 WEKA Data Platform 的重新架构与品牌重塑。最初为有限发布，计划于 fall 2025 GA。— 来源：Blocks & Files, "WEKA builds NeuralMesh for exascale AI", 2025-06-18, https://blocksandfiles.com/2025/06/18/weka-builds-neuralmesh-for-exascale-ai/ (retrieved 2026-11-01)
- **November 2025（SC25）**：Augmented Memory Grid 在 NeuralMesh 上商用，OCI 作为独家首发合作伙伴，通过 Oracle Cloud Marketplace 提供。— 来源：Oracle Blogs, "Scaling long-context inference on OCI with WEKA's Augmented Memory Grid", 2025-11, https://blogs.oracle.com/ai-and-datascience/scaling-long-context-inference-on-oci-with-wekas-augmented-memory-grid (retrieved 2026-11-01)
- **July 2026**：WEKA 任命 Shanta Kohli 为 CMO，对外信息转向"AI inferencing at scale"（规模化 AI 推理）。— 来源：Blocks & Files, "WEKA changes marketing head as messaging moves to AI inferencing at scale", 2026-07-15, https://www.blocksandfiles.com/file/2026/07/15/weka-changes-marketing-head-as-messaging-moves-to-ai-inferencing-at-scale/5271663 (retrieved 2026-11-01)
- **2026-07-21**：发布 NeuralMesh 6 和 WEKApod 3，于 2H 2026 GA，现有客户可免费升级。— 来源：WEKA, "WEKA Debuts NeuralMesh 6 to Power Enterprise and Agentic AI Workloads at Production Scale", 2026-07-21, https://www.weka.io/news/neuralmesh-6-enterprise-agentic-ai (retrieved 2026-11-01)

### 2.2 技术

- **WekaFS**：WEKA 最初的面向 NVMe 闪存的并行、POSIX 兼容文件系统，可分层到兼容 S3 的对象存储（"object tier"，对象层）。— 来源：WEKA docs, "WEKA networking" (v4.2 overview), n.d., https://docs.weka.io/4.2/overview/networking-in-wekaio (retrieved 2026-11-01) [VERIFY: 分层描述属背景知识，该文档页面并未涵盖]
- **内核旁路数据路径**：后端服务器必须运行带 SR-IOV 的 DPDK，将网卡映射到用户空间并绕过内核网络栈。客户端可使用 DPDK 或内核 UDP。在"performance-optimized"（性能优化）模式下，CPU 核心专供 WEKA 使用。在"CPU-optimized"（CPU 优化）模式（5.0）下，DPDK 使用 RX 中断，不绑定核心。UDP 模式为后备方案，例如在某些模式下的 AWS ENA 上。— 来源：WEKA docs, "Networking in WEKA" (v5.0), n.d., https://docs.weka.io/5.0/weka-system-overview/networking-in-wekaio (retrieved 2026-11-01)
- **NeuralMesh（June 2025）**：一种面向服务的设计，每个节点运行一个或多个微服务（数据访问、元数据、审计、可观测性），构成动态互联的网格。WEKA 称其规模越大越强、越快，并以此与单体式存储形成对比。— 来源：WEKA press release, "WEKA Introduces NeuralMesh", 2025-06-17, https://www.weka.io/company/weka-newsroom/press-releases/weka-introduces-neuralmesh/ (retrieved 2026-11-01)
- **Augmented Memory Grid（AMG）**：在 NeuralMesh 管理的 NVMe 上存储并复用 KV 缓存，以扩展 GPU 内存。厂商声称可实现 1000x 内存扩展、首 token 延迟最多快 20x、并发用户数增加 10x。它与 NVIDIA GPUDirect Storage、Dynamo 和 NIXL 集成，WEKA 还开源了一个 NIXL 插件。— 来源：WEKA, "WEKA Breaks The AI Memory Barrier With Augmented Memory Grid on NeuralMesh", 2025-11-18, https://www.weka.io/news/weka-breaks-the-ai-memory-barrier-with-augmented-memory-grid (retrieved 2026-11-01) [VERIFY: 厂商性能声称，未找到独立测试]
- **NeuralMesh 6（July 2026）**：新增原生多租户、数据缩减、统一的文件与对象访问，以及增强版 AMG。— 来源：HPCwire, "WEKA Launches NeuralMesh 6 and WEKApod as AI Inference Pushes Infrastructure Limits", 2026-07-22, https://www.hpcwire.com/2026/07/22/weka-launches-neuralmesh-6-and-wekapod-as-ai-inference-pushes-infrastructure-limits/ (retrieved 2026-11-01)
- **WEKApod**：WEKA 的一体化交钥匙设备产品线，其 Nitro 和 Prime 型号于 2025 年获得 NVIDIA DGX SuperPOD 认证。WEKApod 3（July 2026）被描述为 WEKA 首款从机箱层面起即为其软件设计的硬件。它针对 Blackwell 优化，并提供液冷 Nitro 配置。每机架声称：有效容量 1.1 EB、10.2 TB/s 和 210M IOPS。— 来源：Unite.AI, "WEKA Launches NeuralMesh 6 and WEKApod 3 as AI Infrastructure Shifts Toward Inference", 2026-07, https://www.unite.ai/weka-launches-neuralmesh-6-and-wekapod-3-as-ai-infrastructure-shifts-toward-inference/ (retrieved 2026-11-01) [VERIFY: 每机架数字为厂商声称；最初的 WEKApod 发布日期未确认（据信为 GTC 2024）]
- **云上可用性**：自 WEKA 4（June 2022）起与 AWS、GCP、Azure 和 OCI 原生集成，并上架 Azure Marketplace 和 AWS Marketplace。AMG 首先在 OCI 上推出。— 来源：HPCwire, "WEKA Unveils Multicloud Data Platform for AI and Next-Gen Workloads", 2022-06, https://www.hpcwire.com/off-the-wire/weka-unveils-multicloud-data-platform-for-ai-and-next-gen-workloads/ (retrieved 2026-11-01)
- **融合模式（Converged mode）**：WEKA 后端进程直接运行在 GPU 服务器或应用服务器上，使用其本地 NVMe。该模式于 2023 年面向 AWS 推出（公开预览，Stability AI 为参考客户），OCI 文档同时描述了融合与非融合两种部署模式。— 来源：Oracle Blogs, cloud-infrastructure post on WEKA deployment patterns, n.d., https://blogs.oracle.com/cloud-infrastructure/?p=10379 (retrieved 2026-11-01)

### 2.3 融资与估值

- **January 2022**：由 Hitachi Ventures 领投 US$73M，累计融资额达到约 US$140M。Calcalist 称之为 Series D；Blocks & Files 则将其视为后期/C 轮扩展融资。— 来源：Blocks & Files, "WekaIO ramps up its funding to $140 million", 2022-01-04, https://www.blocksandfiles.com/file/2022/01/04/wekaio-ramps-up-its-funding-to-140-million/1609553 (retrieved 2026-11-01) [VERIFY: 轮次名称]
- **November 2022**：以约 US$750M 估值完成 US$135M 的 Series D，由 Generation Investment Management 领投，Hitachi Ventures 参投。— 来源：SiliconANGLE, "Distributed file system startup WekaIO closes bumper $135M Series D funding round", 2022-11-15, https://siliconangle.com/2022/11/15/distributed-file-system-startup-wekaio-closes-bumper-135m-series-d-funding-round/ (retrieved 2026-11-01); Calcalist, "Data management platform WEKA raises $135 million at $750 million valuation", 2022-11, https://www.calcalistech.com/ctechnews/article/h1tlqcx8o (retrieved 2026-11-01)
- **May 2024**：以 US$1.6B 投后估值完成 US$140M 的 Series E（US$100M 一级融资，US$40M 为面向老员工的二级转让）。由 Valor Equity Partners 领投，NVIDIA、Atreides、Generation、Qualcomm Ventures 和 Hitachi Ventures 参投。Valor 的 Antonio Gracias 加入董事会（*公司自述*）。— 来源：WEKA, "WEKA Nets $140M in Series E Funding at $1.6B Valuation", 2024-05-15, https://www.weka.io/news/weka-nets-140m-in-series-e-funding-at-1-6b-valuation (retrieved 2026-11-01); Globes, "Weka raises $140m at $1.6b valuation", 2024-05, https://en.globes.co.il/en/article-1001478786 (retrieved 2026-11-01)
- **2025–2026**：未发现新的定价融资轮。Globes 的一篇采访（约 May 2026）仍将"两年前"的 US$1.6B 那一轮称为最近一轮。— 来源：Globes, "Chip industry headache is this Israeli co's opportunity", 2026, https://en.globes.co.il/en/article-1001542294 (retrieved 2026-11-01) [VERIFY: 摘录中未显示发表日期]
- 聚合网站给出的累计总额：约 US$372M（Tracxn）、约 US$412M（Parsers VC）和约 US$415M（PitchBook）（*估算*）。— 来源：PitchBook, "WEKA 2026 Company Profile", 2026, https://pitchbook.com/profiles/company/160815-16 (retrieved 2026-11-01)

### 2.4 营收、ARR、盈利能力、员工人数

- WEKA **于 2024 年 ARR 突破 US$100M**，营收连续第三年增长超过一倍（*公司自述*，February 2025 CEO 公开信）。— 来源：WEKA, "A Strategic Step Forward for WEKA: An Open Letter From Our CEO", 2025-02, https://www.weka.io/article/a-strategic-step-forward-for-weka-an-open-letter-from-our-ceo (retrieved 2026-11-01)
- 在 2025 年接受 Calcalist 采访时，Zvibel 表示预计当年营收将增长至三倍，每月现金消耗约 US$0.5M，即接近盈亏平衡（*媒体报道，Calcalist*）。— 来源：Calcalist, WEKA interview, 2025, https://www.calcalistech.com/ctechnews/article/bkdbx4gmc (retrieved 2026-11-01) [VERIFY: 摘录可能混淆了 2024 年 Series E 文章与 2025 年的采访]
- Globes 援引 AI 市场高管的说法，估计 WEKA 的 ARR 为 US$100–150M，并点名 Oracle 和 Tesla 为客户（*估算，Globes 报道*）。— 来源：Globes, "Chip industry headache is this Israeli co's opportunity", 2026, https://en.globes.co.il/en/article-1001542294 (retrieved 2026-11-01)
- GetLatka 的"US$24.5M revenue"数字属于一家无关的德国出版商 WEKA Media GmbH，不应使用。
- 未找到可靠的 2026 年员工人数数字。

### 2.5 客户与合作伙伴

- WEKA 的客户名录列有 Cohere、Nebius、Yotta（Shakti Cloud）、Midjourney 和 Stability AI 等。WEKA 称 Fortune 50 中有 30% 的企业使用其产品（*公司自述*）。— 来源：WEKA, "Our Customers", n.d., https://www.weka.io/customers/ (retrieved 2026-11-01)
- **Stability AI** 在 AWS 上使用 WEKA 融合模式（Converged Mode）。WEKA 声称其实现了 95% 的存储成本降低和 93% 的 GPU 利用率（*公司自述*）。— 来源：AAP (Cision release), "WEKA and Stability AI Partner to Maximize Cloud Benefits for AI Model Training", 2023-09-14, https://www.aap.com.au/aapreleases/cision20230914ae06706 (retrieved 2026-11-01)
- **Nebius**：June 2025 达成合作，提供基于 WEKA 存储的 GPU 即服务。— 来源：StorageNewsletter, "WEKA and Nebius Partner to Deliver GPU-as-a-Service (GPUaaS) Solution", 2025-06-11, https://www.storagenewsletter.com/2025/06/11/weka-and-nebius-partner-to-delivers-gpu-as-a-service-gpuaas-solution/ (retrieved 2026-11-01)
- **Oracle Cloud Infrastructure**：AMG 的独家首发合作伙伴，在生产环境中运行超大规模推理。— 来源：WEKA blog, "NeuralMesh Delivers 1000x GPU Memory for AI Inference on Oracle Cloud", 2025-11, https://www.weka.io/blog/ai-ml/neuralmesh-delivers-1000x-gpu-memory-for-ai-inference-on-oracle-cloud/ (retrieved 2026-11-01)
- **NVIDIA**：Series E 的投资方，WEKApod 获得 DGX SuperPOD 认证，并与 Dynamo 和 NIXL 集成。— 来源：WEKA, "Faster, Smarter, More Efficient AI Factories with NVIDIA and WEKA", n.d., https://www.weka.io/partners/nvidia/ (retrieved 2026-11-01)
- 本研究未能确认 WEKA 与 CoreWeave 或 WEKA 与 Lambda 之间存在合作关系。[VERIFY: 需核实此类关系是否存在]

### 2.6 基准测试

- **SPECstorage Solution 2020**：运行于 HPE Alletra Storage Server 4110 上的 WEKA 声称在全部五项工作负载中排名第一（结果日期 2025-01-28）。例如，EDA_BLENDED 达到 17,000 个作业集和约 7.65M ops/s。Blocks & Files 指出，AI_IMAGE 工作负载的竞争程度不及 MLPerf。— 来源：Blocks & Files, "WEKA tops SPECstorage Solution 2020 benchmark", 2025-02-11, https://www.blocksandfiles.com/ai-ml/2025/02/11/weka-tops-specstorage-solution-2020-benchmark/1595764 (retrieved 2026-11-01)
- **MLPerf Storage**：据报道，WEKA 提交了 v1.0（September 2024），但未提交 v2.0（August 2025）或 v3.0（September 2026）。— 来源：StorageReview, "Best Storage Arrays 2026: AI Storage Leaders and Audited Results", 2026, https://www.storagereview.com/best/storage-arrays (retrieved 2026-11-01) [VERIFY: v1.0 参赛情况及 WEKA 的数字尚未与 MLCommons 核对确认]
- **IO500**：Memorial Sloan Kettering 基于 WEKA 的一次提交得分 665.49（261 个客户端节点）。WEKA 曾公开质疑 DDN 的 IO500"#1"声称。— 来源：WEKA, "Revolutionizing Research: WEKA's IO500 Benchmark Success…", n.d., https://www.weka.io/?p=39859 (retrieved 2026-11-01) [VERIFY: 需对照 io500.org 榜单核实]

### 2.7 市场进入策略（GTM）

- WEKA 销售运行在合作伙伴硬件上的软件定义订阅（HPE、Supermicro、Dell、Lenovo、Hitachi Vantara，以及更早的 OEM 交易，如 Hitachi Vantara 于 2020 年 OEM 的 WekaFS）。它还销售 WEKApod 设备，并通过 AWS、Azure、GCP 和 OCI 云市场提供云上部署。— 来源：WEKA, "Hardware + System Partners", n.d., https://www.weka.io/partners/system-partners/ (retrieved 2026-11-01); StorageNewsletter, "WekaIO Signs With Hitachi Vantara", 2020-07-27, https://www.storagenewsletter.com/2020/07/27/wekaio-signs-with-hitachi-vantara/ (retrieved 2026-11-01)
- 按每 TB 容量定价。一家经销商列出的 Lenovo 品牌 WEKA XPS Edition 1 年订阅在 1–2.5 PB 档位的 MSRP 为每 TB US$339。大多数交易为定制报价。— 来源：SHI, "WEKA Extreme Performance and Scale (XPS) Edition", n.d., https://www.shi.com/product/45872663 (retrieved 2026-11-01) [VERIFY: 仅一家经销商的列表]

---

## 3. DDN（DataDirect Networks）

### 3.1 创立与里程碑

- DDN 由 Alex Bouzari（董事长兼 CEO）和 Paul Bloch（总裁）于 1998 年创立，总部位于加州 Chatsworth。— 来源：Wikipedia, "DataDirect Networks", n.d., https://en.wikipedia.org/wiki/DataDirect_Networks (retrieved 2026-11-01)
- DDN 的成长基本未依赖外部资本。Forbes 报道称，两位创始人各持有公司约 40% 的股份。— 来源：Forbes Perú (Forbes reprint), "El nuevo cohete de la IA es una empresa de datos de 28 años", 2026-08-07, https://forbes.pe/editors-pick/2026-08-07/el-nuevo-cohete-de-la-ia-es-una-empresa-de-datos-de-28-anos/ (retrieved 2026-11-01)
- **September 2018**：经过六轮竞拍，DDN 以约 US$60M 收购了已破产的 Tintri 的资产（Tintri 于 July 2018 申请 Chapter 11 破产保护）。— 来源：Blocks & Files, "DDN buys Tintri biz remains for $60mn", 2018-09-05, https://blocksandfiles.com/2018/09/05/ddn-buys-tintri-biz-remains-for-60mn/ (retrieved 2026-11-01)
- **September–November 2019**：DDN 收购了 Western Digital 的 IntelliFlash 全闪存阵列业务（原 Tegile）。WD 成为 DDN 的首选 HDD/SSD 供应商，收购价格未披露。— 来源：StorageNewsletter, "DDN Completes Acquisition of Western Digital Intelliflash AFA Business", 2019-11-21, https://www.storagenewsletter.com/2019/11/21/ddn-completes-acquisition-of-western-digital-intelliflash-afa-business/ (retrieved 2026-11-01)
- DDN 此前已于 2018 年收购了 Intel 的 Lustre 团队及资产（Whamcloud）。[VERIFY: 属背景知识，本研究未重新查证来源]
- **January 2025**：Blackstone 投资（见 3.3）。**February 2025**：Infinia 2.0 发布。**June 2025**：AI400X3 和 Infinia 2.1 发布。**November 2025**：DDN CORE 发布。**June 2026**：AI400X3M 发布（见 3.2）。

### 3.2 技术

- **EXAScaler**：DDN 的 Lustre 并行文件系统企业发行版。它运行在 SFA 硬件上，是面向 NVIDIA DGX BasePOD 和 SuperPOD 参考架构的 A³I（Accelerated, Any-scale AI）设备的基础。— 来源：DDN press release, "DDN Boosts AI Storage Leadership with EXAScaler 6…", n.d., https://www.ddn.com/press-releases/ddn-boosts-ai-leadership-with-exascaler-6 (retrieved 2026-11-01)
- **AI400X2 / AI400X2T**：早期的 A³I 设备。NVIDIA 的 Eos 使用 AI400X2 设备。— 来源：DDN press release, "DDN Delivers 4 Terabytes/Second of Accelerated Storage Performance in Groundbreaking NVIDIA Eos AI Supercomputer", 2024-03, https://www.ddn.com/press-releases/ddn-delivers-4-terabytes-second-of-accelerated-storage-performance-in-groundbreaking-nvidia-eos-ai-supercomputer/ (retrieved 2026-11-01)
- **AI400X3（ISC，June 2025）**：第三代 2U 全闪存 EXAScaler 设备。DDN 声称其写吞吐量比上一代最多高 70%，读吞吐量高 55%。与 Infinia 2.1 一同发布。— 来源：DDN blog, "DDN launches AI400X3 and Infinia 2.1 at ISC 2025", 2025-06, https://www.ddn.com/blog/ddn-launches-ai400x3-and-infinia-2.1-at-isc-2025/ (retrieved 2026-11-01)
- **AI400X3M（ISC，June 2026）**：顺序读最高 190 GB/s、写 110 GB/s，随机读 8M IOPS。EXAScaler 和 Infinia 均通过 NVIDIA Dynamo 和 NIXL 新增 KV 缓存支持。— 来源：StorageReview, "DDN launches AI400X3M and Dynamo-integrated KV cache acceleration at ISC 2026", 2026-06, https://www.storagereview.com/news/ddn-launches-ai400x3m-and-dynamo-integrated-kv-cache-acceleration-at-isc-2026 (retrieved 2026-11-01); HPCwire, "DDN Preps for AI Wave with Speedy New Appliance, KV Cache Solution", 2026-06-24, https://www.hpcwire.com/2026/06/24/ddn-preps-for-ai-wave-with-speedy-new-appliance-kv-cache-solution/ (retrieved 2026-11-01) [VERIFY: 各来源的规格不一致，需核对数据表]
- **Infinia（2.0 于 2025-02-20 在"Beyond Artificial"活动上发布）**：一个软件定义、与硬件无关、云原生的数据智能与对象存储平台。DDN 声称其 AI 数据加速和元数据性能最多快 100x（查找时间低于 1 ms，而非超过 10 ms），成本效率提高 10x。这些是对比未具名或不同基线的厂商基准测试。— 来源：Business Wire, "DDN Unveils Infinia 2.0, The AI Data Intelligence Platform…", 2025-02-20, https://www.businesswire.com/news/home/20250220891434/en/DDN-Unveils-Infinia-2.0-The-AI-Data-Intelligence-Platform-to-Maximize-Value-for-Enterprises-AI-Factories-and-Sovereign-AI (retrieved 2026-11-01) [VERIFY: 100x 声称没有公布测试方法]
- **DDN CORE（SC25，November 2025）**：统一 EXAScaler（文件）和 Infinia（对象）的软件层。随之一同推出的还有 Google Cloud Managed Lustre 的 GA 以及 OCI 上的 Infinia。— 来源：Blocks & Files, "DDN goes hard CORE", 2025-11-18, https://www.blocksandfiles.com/ai-ml/2025/11/18/ddn-goes-hard-core/1718766 (retrieved 2026-11-01)
- **Tintri 和 IntelliFlash**：2018–2019 年收购的企业主存储产品线。Tintri 以"Tintri by DDN"名义运营。— 来源：Blocks & Files, "Western Digital exits data centre systems, sells IntelliFlash to DDN…", 2019-09-20, https://www.blocksandfiles.com/block/2019/09/20/western-digital-exits-data-centre-systems-sells-intelliflash-to-ddn-puts-activescale-on-the-block/1596474 (retrieved 2026-11-01)
- **NVIDIA 内部集群**：Selene（DGX A100 SuperPOD）使用了约 7 PB 的 DDN AI400X/A³I 存储。Eos（576 台 DGX H100）使用 48 台 A³I AI400X2 设备，提供约 4 TB/s（*公司自述*）。DDN 还为 Cambridge-1 供货。— 来源：DDN press release, "DDN Delivers 4 Terabytes/Second… NVIDIA Eos", 2024-03, https://www.ddn.com/press-releases/ddn-delivers-4-terabytes-second-of-accelerated-storage-performance-in-groundbreaking-nvidia-eos-ai-supercomputer/ (retrieved 2026-11-01); insideHPC, "HPC at Scale Enabled by DDN A3i and NVIDIA SuperPOD", 2020-04, https://insidehpc.com/2020/04/hpc-at-scale-enabled-by-ddn-a3i-and-nvidia-superpod/ (retrieved 2026-11-01)

### 3.3 融资与估值

- **January 2025**：Blackstone Tactical Opportunities 以 US$5B 估值投资 US$300M，并获得一个董事会席位。这是 DDN 在约 25 年自筹资金且盈利经营之后首次引入外部机构资本（*公司自述*）。— 来源：Blackstone, "Blackstone Invests $300 Million at a $5 Billion Valuation in DDN…", 2025-01-08/09, https://www.blackstone.com/news/press/blackstone-invests-300-million-at-a-5-billion-valuation-in-ddn-ai-and-data-intelligence-solutions-leader-to-fuel-further-rapid-growth/ (retrieved 2026-11-01); Blocks & Files, "Blackstone investing $300 million in DDN", 2025-01-09, https://blocksandfiles.com/2025/01/09/blackstone-investing-300-million-in-ddn/ (retrieved 2026-11-01)
- **June 2026**：CEO Bouzari 向 Bloomberg 表示，DDN 希望在 2026 年底前进行新一轮融资，并引入战略投资者。Bloomberg 的报道点名 Google 和 Salesforce 为客户。未披露融资规模或估值目标（*媒体报道，Bloomberg*）。— 来源：Bloomberg, "AI Data Firm DDN Eyeing a Fresh Funding Round by End of Year", 2026-06-10, https://www.bloomberg.com/news/articles/2026-06-10/ai-data-firm-ddn-eyeing-a-fresh-funding-round-by-end-of-year (retrieved 2026-11-01); Blocks & Files, "DDN wants strategic investors", 2026-06-12, https://www.blocksandfiles.com/ai-ml/2026/06/12/ddn-wants-strategic-investors/5254665 (retrieved 2026-11-01)
- 截至 2026-11-01，未发现 2026 年已完成交割的融资轮。[VERIFY: 需检查 Q4 2026 是否有相关公告]
- DDN 高管在 2025 年表示目前没有 IPO 计划。— 来源：Forbes Perú (Forbes reprint), "El nuevo cohete de la IA es una empresa de datos de 28 años", 2026-08-07, https://forbes.pe/editors-pick/2026-08-07/el-nuevo-cohete-de-la-ia-es-una-empresa-de-datos-de-28-anos/ (retrieved 2026-11-01) [VERIFY: IPO 表态来自聚合网站摘要]

### 3.4 营收、盈利能力、员工人数

- DDN 向 Forbes 表示，在与 xAI 及主权/政府 AI 超级计算机合同的推动下，其 2026 年营收有望大致翻倍至约 **US$1B**（*媒体报道，Forbes*）。— 来源：Forbes Italia, "Chi è Alex Bouzari, il miliardario che rende più veloci i supercomputer dell'IA", 2026-08-10, https://forbes.it/2026/08/10/chi-e-alex-bouzari-il-miliardario-che-rende-piu-veloci-i-supercomputer-dellia/ (retrieved 2026-11-01)
  - [VERIFY: 各摘要给出的基数不一致。一个聚合网站称 2025 年约 US$500M、2024 年 US$400M；Forbes Perú 的文字暗示历史上每年约 US$300M。需获取 Forbes 英文原文。]
- 较早的历史：DDN 称其于 2020 年营收达到 US$400M，盈利能力创历史新高（*公司自述*）。— 来源：Wikipedia, "DataDirect Networks", n.d., https://en.wikipedia.org/wiki/DataDirect_Networks (retrieved 2026-11-01) [VERIFY: 经由 Wikipedia 转述]
- DDN 称其平台在各客户处支持超过 500,000 块 NVIDIA GPU，其中包括 xAI 拥有 100,000 块 GPU 的 Colossus（*公司自述*）。— 来源：Benzinga, "Blackstone invests $300 million in AI data firm that powers Elon Musk's xAI supercomputer", 2025-01, https://www.benzinga.com/news/25/01/42892338/blackstone-invests-300-million-in-ai-data-firm-that-powers-elon-musks-xai-supercomputer (retrieved 2026-11-01)
- 未找到可靠的员工人数数字。[VERIFY: DDN 员工人数]

### 3.5 客户与合作伙伴

- **xAI Colossus**：November 2024 宣布与 NVIDIA 的合作（关于相互竞争的"主要"声称，见 VAST 部分的说明）。— 来源：DDN press release, "DDN's Data Platform Propels xAI's Colossus to World-Class Performance", 2024-11, https://www.ddn.com/press-releases/ddns-data-platform-propels-xais-colossus-to-world-class-performance/ (retrieved 2026-11-01)
- **NVIDIA**：DDN 存储支撑着 Selene、Eos 和 Cambridge-1，并提供 DGX BasePOD/SuperPOD 参考架构。DDN 声称是首家在任意规模上通过 DGX SuperPOD 验证的存储厂商（*公司自述*）。— 来源：HPCwire, "DDN Announces Next-Gen Reference Architectures for NVIDIA DGX BasePOD and DGX SuperPOD", 2022-09, https://www.hpcwire.com/off-the-wire/ddn-announces-next-gen-reference-architectures-for-nvidia-dgx-basepod-and-dgx-superpod/ (retrieved 2026-11-01)
- **Google Cloud**：Google Cloud Managed Lustre 基于 DDN EXAScaler 构建（2025-04-09 在 Cloud Next 上宣布，到 SC25 时 GA）。Google 还与 DDN 在 Infinia 上开展合作。— 来源：Business Wire, "DDN Announces Collaboration with Google Cloud to Advance AI Initiatives with Google Cloud Managed Lustre and Infinia at Google Cloud Next 2025", 2025-04-09, https://www.businesswire.com/news/home/20250409046523/en/DDN-Announces-Collaboration-with-Google-Cloud-to-Advance-AI-Initiatives-with-Google-Cloud-Managed-Lustre-and-Infinia-at-Google-Cloud-Next-2025 (retrieved 2026-11-01)
- **Oracle（OCI）**：Infinia 已在 OCI 上提供。— 来源：Blocks & Files, "DDN goes hard CORE", 2025-11-18, https://www.blocksandfiles.com/ai-ml/2025/11/18/ddn-goes-hard-core/1718766 (retrieved 2026-11-01)
- **SC25 IO500 榜单中出现的 HPC 站点**：SoftBank（CHIE-4）、University of Florida（HiPerGator）和 Hudson River Trading。— 来源：StorageNewsletter, "SC25: The IO500 lists show interesting results as usual", 2025-11-25, https://www.storagenewsletter.com/2025/11/25/sc25-the-io500-lists-show-interesting-results-as-usual/ (retrieved 2026-11-01)

### 3.6 基准测试

- **MLPerf Storage v1.0（September 2024）**：EXAScaler AI400X2T 在 36 个模拟 H100 和 18 个客户端下达到 99,018 MiB/s。— 来源：Blocks & Files, "MLPerf AI benchmark tests how storage systems keep GPUs busy", 2024-09-26, https://www.blocksandfiles.com/ai-ml/2024/09/26/mlperf-ai-benchmark-tests-how-storage-systems-keep-gpus-busy/1605043 (retrieved 2026-11-01)
- **MLPerf Storage v2.0（August 2025）**：AI400X3 在 ResNet-50 上为最多 640 个模拟 H100 供数，持续读取超过 110 GiB/s。一个二手来源报道其在 3D U-Net 上达到 120.68 GB/s，检查点保存读 30.6 GB/s、写 15.3 GB/s。DDN 被描述为在 v2.0 中性能密度领先。— 来源：HPCwire/AIwire, "DDN Showcases AI400X3 Performance in Latest MLPerf Storage Benchmarks", 2025-08-05, https://www.hpcwire.com/aiwire/2025/08/05/ddn-showcases-ai400x3-performance-in-latest-mlperf-storage-benchmarks/ (retrieved 2026-11-01) [VERIFY: U-Net 和检查点数字来自单一二手来源]
- **MLPerf Storage v3.0（2026-09-01）**：DDN 未提交，VAST 和 WEKA 也均未提交。— 来源：StorageReview, "MLPerf Storage v3.0: 877 GiB/s Checkpoints, a Cloud First, and a Leaderboard Turned Over", 2026-09, https://www.storagereview.com/news/mlperf-storage-v3-0-877-gib-s-checkpoints-a-cloud-first-and-a-leaderboard-turned-over (retrieved 2026-11-01)
- **IO500（ISC，June 2025）**：DDN 声称"#1"。在 10 节点生产榜单上，Argonne 的 DAOS 系统占据前两名，Hudson River Trading 的 EXAScaler 位列第三（348.08）。WEKA 对 DDN 的说法提出异议。— 来源：Blocks & Files, "DDN tops IO500 10-node list for HPC storage", 2025-06-20, https://www.blocksandfiles.com/ai-ml/2025/06/20/ddn-tops-io500-10-node-list-for-hpc-storage/1609176 (retrieved 2026-11-01)

### 3.7 市场进入策略（GTM）

- DDN 主要通过直销、渠道以及由 NVIDIA 主导的 SuperPOD 交易销售集成设备（配 EXAScaler 的 SFA 硬件、A³I AI400X 系列、Tintri、IntelliFlash）。Infinia 和 DDN CORE 为软件定义、与硬件无关的产品。云上可用性通过 Google Cloud Managed Lustre（Google 第一方服务）和 OCI 上的 Infinia 实现。— 来源：Blocks & Files, "DDN goes hard CORE", 2025-11-18, https://www.blocksandfiles.com/ai-ml/2025/11/18/ddn-goes-hard-core/1718766 (retrieved 2026-11-01)
- Blackstone 的投资被描述为财务性而非运营性投资。公司仍由创始人经营。— 来源：Computer Weekly, "DDN seeks AI leadership as it bags $300m investment", 2025-01, https://www.computerweekly.com/news/366618008/DDN-seeks-AI-leadership-as-it-bags-300m-investment (retrieved 2026-11-01)

---

## 4. 相邻厂商（简述）

### 4.1 Hammerspace

- 一轮 US$100M 的 Series B（2025-04-16 宣布）由 Altimeter Capital 领投，ARK Invest 再次参投。TechCrunch 的消息来源称估值超过 US$500M；CB Insights 称为 US$700–800M（*媒体报道/估算*）。Hammerspace 表示正在为约两年内可能的 IPO 做准备。— 来源：TechCrunch, "Hammerspace, an unstructured data wrangler, raises $100M", 2025-04-16, https://techcrunch.com/2025/04/16/hammerspace-an-unstructured-data-wrangler-100m/ (retrieved 2026-11-01)
- CB Insights 列出 2026-02-23 的一轮"Series B-II"（TGC Square），未给出金额。— 来源：CB Insights, "Hammerspace financials", 2026, https://www.cbinsights.com/company/hammerspace/financials (retrieved 2026-11-01) [VERIFY: 单一聚合网站]
- Hammerspace 参加了 MLPerf Storage v1.0，声称其 Tier 0 产品在 3D U-Net 上创下纪录。B&F 最初标注这些结果尚未经过验证。它也提交了 v2.0。— 来源：Blocks & Files, "Hammerspace hammers MLPerf Storage benchmark results", 2024-09, https://blocksandfiles.com/?p=68906 (retrieved 2026-11-01)

### 4.2 Qumulo

- Doug Gourlay（曾任职 Arista 和 Cisco）于 July 2024 出任 CEO，接替 Bill Richter。公司已从销售自有硬件转向面向云、本地和边缘的软件。— 来源：GeekWire, "Former Arista and Cisco exec Douglas Gourlay named new CEO of data storage company Qumulo", 2024-07, https://www.geekwire.com/2024/former-arista-and-cisco-exec-douglas-gourlay-named-new-ceo-of-data-storage-company-qumulo/ (retrieved 2026-11-01)
- Qumulo 已知的最近一轮定价融资是 July 2020 以 US$1.2B 估值完成的 US$125M Series E。— 来源：HPCwire/AIwire, "Qumulo Locks Down $125M Financing, $1.2B Valuation", 2020-07-23, https://www.hpcwire.com/aiwire/2020/07/23/qumulo-locks-down-125m-financing-1-2b-valuation/ (retrieved 2026-11-01)
- 未发现 2025–2026 年的融资或重大新闻。[VERIFY: 需查看 Qumulo 新闻中心]

### 4.3 MinIO（许可与分发变化，2025–2026）

- **May–June 2025**：开源 Community Edition 移除了完整的管理控制台，仅保留基础的对象浏览器。管理工作转移到 CLI 或商业产品 AIStor。— 来源：Blocks & Files, "MinIO removes management features from basic community edition object storage code", 2025-06-19, https://blocksandfiles.com/2025/06/19/minio-removes-management-features-from-basic-community-edition-object-storage-code/ (retrieved 2026-11-01)
- **October 2025**：Community Edition 改为仅提供源代码，官方二进制文件和 Docker 镜像不再更新。— 来源：Linuxiac, "MinIO Ends Active Development, Steers Users Toward Paid AIStor", 2025-12, https://linuxiac.com/minio-ends-active-development/ (retrieved 2026-11-01) [VERIFY: October 2025 这一日期在各来源间不一致]
- **2025-12-03**：Community Edition 进入维护模式：不再接受新功能或 PR，安全修复仅视情况处理。用户被引导至付费的 AIStor。— 来源：Linuxiac, "MinIO Ends Active Development, Steers Users Toward Paid AIStor", 2025-12, https://linuxiac.com/minio-ends-active-development/ (retrieved 2026-11-01)
- **February 2026**：GitHub 仓库被标记为不再维护（据报道为 2026-02-12）并归档。出现了 OpenMaxIO 等社区分支。— 来源：youngju.dev, "MinIO archived: Garage, SeaweedFS, Ceph RGW", 2026-07-17, https://www.youngju.dev/blog/2026-07-17-minio-archived-garage-seaweedfs-ceph-rgw.en (retrieved 2026-11-01) [VERIFY: 博客来源；需对照 GitHub 仓库状态确认]
- MinIO 的服务器许可证早在 2021 年已从 Apache 2.0 改为 AGPLv3。[VERIFY: 属背景知识，本研究未重新查证来源]

### 4.4 Cloudian

- HyperScale AI Data Platform（AIDP）基于 NVIDIA 的 AI Data Platform 参考设计，搭载 RTX PRO 6000 Blackwell GPU，并在存储层内提供向量搜索；它于 September/October 2025 发布，November 2025 GA，v1.1 于 June 2026 在 Supermicro 和 Lenovo 服务器上推出。— 来源：Blocks & Files, "Cloudian launches HyperScale AI platform built on Nvidia Blackwell GPUs", 2025-10-01, https://www.blocksandfiles.com/ai-ml/2025/10/01/cloudian-launches-hyperscale-ai-platform-built-on-nvidia-blackwell-gpus/1592771 (retrieved 2026-11-01)
- Cloudian 于 November 2024 新增面向对象存储的 GPUDirect（S3/RDMA），声称在测试配置中超过 200 GB/s。— 来源：IT Brief, "Cloudian enhances AI processing with NVIDIA GPUDirect tie-up", 2024-11, https://itbrief.co.uk/story/cloudian-enhances-ai-processing-with-nvidia-gpudirect-tie-up (retrieved 2026-11-01)
- 未发现 2025–2026 年的融资。已知最近一轮大额融资是 2018 年 US$94M 的 Series E（累计约 US$173M）。— 来源：Converge Digest, "Cloudian raises $94 million…", 2018, https://convergedigest.com/cloudian-raises-94-million-for/ (retrieved 2026-11-01)

### 4.5 VDURA（原 Panasas）

- Panasas 更名为 VDURA，并重新定位为 AI/HPC 平台（基于 PanFS 的 VDURA Data Platform），矛头指向 VAST、WEKA 和 DDN。V5000 全闪存设备于 2025 年推出，搭配 WD Data60/Data102 磁盘柜的混合版本于 March 2026 推出，AMD 参考架构于 September 2025 推出。— 来源：Blocks & Files, "VDURA takes aim at VAST, WEKA, DDN with AI-HPC storage reboot", 2025-06-28, https://www.blocksandfiles.com/ai-ml/2025/06/28/vdura-takes-aim-at-vast-weka-ddn-with-ai-hpc-storage-reboot/1586714 (retrieved 2026-11-01); Blocks & Files, "VDURA pairs V5000 flash with WD Data60 and Data102 disk shelves", 2026-03-11, https://www.blocksandfiles.com/disk/2026/03/11/vdura-pairs-v5000-flash-with-wd-data60-and-data102-disk-shelves/5208754 (retrieved 2026-11-01)
- VDURA 称其支撑着全球最大的国防 GPU 部署之一（*公司自述*，October 2025）。— 来源：Business Wire, "VDURA Powers One of the World's Largest Defense GPU Installations", 2025-10-02, https://www.businesswire.com/news/home/20251002832210/en/VDURA-Powers-One-of-the-Worlds-Largest-Defense-GPU-Installations (retrieved 2026-11-01)
- 累计融资额不明：CB Insights 称含贷款约 US$133M，Caplight 称约 US$75M。[VERIFY: 无权威来源]

### 4.6 2025–2026 年值得关注的 AI 存储并购及其他交易

- **Lenovo 收购 Infinidat**：January 2025 宣布，预计于 2H 2025 交割。Lenovo 新闻稿确认交易已完成，Infinidat 现作为 Lenovo ISG 内的一个业务单元运营。— 来源：Lenovo, "Lenovo Completes Acquisition of Infinidat…", n.d., https://news.lenovo.com/pressroom/press-releases/lenovo-completes-acquisition-of-infinidat-expanding-enterprise-storage-portfolio-enhancing-ai-driven-data-infrastructure/ (retrieved 2026-11-01) [VERIFY: 确切交割日期]
- **NetApp 收购 DataPelago（July 2026）**，以获得存储层的 GPU 加速数据处理能力。— 来源：Yahoo Finance, "NetApp (NTAP) Acquires AI Storage Software Firm To Expand AI Infrastructure", 2026, https://finance.yahoo.com/technology/ai/articles/netapp-ntap-acquires-ai-storage-220629407.html (retrieved 2026-11-01) [VERIFY: 日期和条款]
- **NetApp 同意收购 PEAK:AIO（英国，September 2026）**，补充并行文件系统和元数据能力。据报道，这是 NetApp 约三个月内的第三笔收购。— 来源：SDxCentral, Storage & Memory acquisition news, 2026-09, https://www.sdxcentral.com/news/?tag=acquisition_1&term=storage-memory (retrieved 2026-11-01) [VERIFY: 单一聚合网站摘录]
- **AMD 收购 MEXT（June 2026）**，其软件把闪存当作 DRAM 来用（内存分层）。— 来源：SDxCentral, Storage & Memory acquisition news, 2026-06, https://www.sdxcentral.com/news/?tag=acquisition_1&term=storage-memory (retrieved 2026-11-01) [VERIFY: 单一聚合网站摘录]
- **MLPerf Storage v3.0（2026-09-01）**：19 家提交方（11 家首次参加，包括 Azure、Nebius、NVIDIA 和"Everpure"），共 143 项结果。新增向量数据库和 S3 测试，模拟加速器从 H100 改为 B200。— 来源：MLCommons, "MLCommons Releases New MLPerf Storage v3.0 Benchmark Results", 2026-09-01, https://mlcommons.org/2026/09/mlperf-storage-v3-0-results/ (retrieved 2026-11-01). Everpure 是 Pure Storage 自 February 2026 品牌更名后的名称（据本项目 CLAUDE.md），因此 Everpure 提交了 v3.0，而 VAST、WEKA 和 DDN 均未提交。
- **MLPerf Storage v2.0（2025-08-04）**：来自 26 家机构的 200 多项结果，并新增了检查点测试。— 来源：GlobeNewswire (MLCommons), "New MLPerf Storage v2.0 Benchmark Results Demonstrate the Critical Role of Storage Performance in AI Training Systems", 2025-08-04, https://www.globenewswire.com/news-release/2025/08/04/3126718/0/en/new-mlperf-storage-v2-0-benchmark-results-demonstrate-the-critical-role-of-storage-performance-in-ai-training-systems.html (retrieved 2026-11-01)
- 本研究未发现 HPE、Dell、IBM 或 Pure 在 2025–2026 年收购 AI 存储初创公司。[VERIFY: 需逐家厂商核查]

---

## 5. 融资表（可直接转为 CSV）

标签说明：`company-stated` = 公司新闻稿或表态（公司自述）；`press` = 媒体报道；`estimated` = 聚合网站或分析师估算。

### 5.1 VAST Data

| 公司（company） | 日期（date） | 轮次（round） | 金额（amount_usd_m） | 估值（valuation_usd_b） | 标签（label） | 来源链接（source_url） |
|---|---|---|---|---|---|---|
| VAST Data | 2020-04 | Series C | 100 | 1.2 | company-stated | https://vastdata.com/news-post/vast-data-raises-100-million-in-series-c-funding-at-1-2-billion-valuation-to-democratize-flash-for-all-data |
| VAST Data | 2021-05 | Series D | 83 | 3.7 | company-stated | https://www.storagenewsletter.com/2021/05/05/vast-data-raised-83-million-total-reaching-263-million/ |
| VAST Data | 2023-12-06 | Series E | 118 | 9.1 | company-stated | https://blocksandfiles.com/2023/12/06/vast-data-funding/ |
| VAST Data | 2025（洽谈） | 媒体报道的洽谈（Alphabet/NVIDIA） | 数千（未披露） | 最高 30 | press | https://en.globes.co.il/en/article-storage-co-vast-data-raising-several-billion-dollars-report-1001517875 |
| VAST Data | 2026-02-05 | 计划中的老股转让（媒体报道） | n/a | 25-27 | press | https://www.blocksandfiles.com/file/2026/02/05/vast-data-plans-funding-round-so-early-stockholders-can-get-cash/4090372 |
| VAST Data | 2026-04-22 | Series F（一级 + 二级） | ~1000 | 30 | company-stated | https://www.cnbc.com/2026/04/22/nvidia-backs-ai-company-vast-data.html |

### 5.2 WEKA

| 公司（company） | 日期（date） | 轮次（round） | 金额（amount_usd_m） | 估值（valuation_usd_b） | 标签（label） | 来源链接（source_url） |
|---|---|---|---|---|---|---|
| WEKA | 2022-01-04 | Series C 扩展 / "Series D"（名称有争议） | 73 | n/a | company-stated | https://www.blocksandfiles.com/file/2022/01/04/wekaio-ramps-up-its-funding-to-140-million/1609553 |
| WEKA | 2022-11-15 | Series D | 135 | 0.75 | press (Calcalist) | https://siliconangle.com/2022/11/15/distributed-file-system-startup-wekaio-closes-bumper-135m-series-d-funding-round/ |
| WEKA | 2024-05-15 | Series E（100 一级 + 40 二级） | 140 | 1.6 | company-stated | https://www.weka.io/news/weka-nets-140m-in-series-e-funding-at-1-6b-valuation |

### 5.3 DDN

| 公司（company） | 日期（date） | 轮次（round） | 金额（amount_usd_m） | 估值（valuation_usd_b） | 标签（label） | 来源链接（source_url） |
|---|---|---|---|---|---|---|
| DDN | 2025-01-09 | 战略少数股权投资（Blackstone Tactical Opportunities） | 300 | 5 | company-stated | https://www.blackstone.com/news/press/blackstone-invests-300-million-at-a-5-billion-valuation-in-ddn-ai-and-data-intelligence-solutions-leader-to-fuel-further-rapid-growth/ |
| DDN | 2026-06-10 | 计划于 2026 年底前进行的融资（尚未交割） | n/a | n/a | press (Bloomberg) | https://www.bloomberg.com/news/articles/2026-06-10/ai-data-firm-ddn-eyeing-a-fresh-funding-round-by-end-of-year |

---

## 6. 待解问题与注意事项

- VAST"US$500M+ CARR"数字所对应的财年标注（FY2025 还是 FY2026），以及 Series F 的领投方。
- 支撑"2026 年约 US$1B"预测的 DDN 2025 年实际营收基数（约 US$300M 还是约 US$500M）。
- VAST 和 DDN 谁是 xAI Colossus 的"主要"存储。两家都声称是自己。
- WEKA 是否参加了 MLPerf Storage v1.0 及其成绩，以及最初的 WEKApod 发布日期。
- 无法进行全文核实：本环境中网页抓取被拦截，因此每一项论断都依赖于所引页面的搜索引擎摘录。
