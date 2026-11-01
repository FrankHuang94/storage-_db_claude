# Everpure（原 Pure Storage）— 已核实事实库

> 📄 英文原文：[meta/research/everpure.md](../../../meta/research/everpure.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

编制日期 2026-11-01。股票代码：NYSE: P（2026 年 4 月前为 PSTG）。财年截止于最接近 2 月 1 日的星期日（FY2026 于 Feb 1, 2026 结束）。

**方法说明**：本次工作中，WebFetch 无法访问 sec.gov、purestorage.com、everpuredata.com、q4cdn.com 或 barchart.com（这些主机在沙箱中无法解析）。因此，以下每一条事实均来自 WebSearch 结果摘要及搜索工具对所引页面的概述；我无法打开并阅读页面本身。所引 URL 是这些搜索结果所指向的一手或行业来源。发布前，应对照 SEC 文件（EDGAR CIK 1474432）抽查相关数字。

---

## 1. 公司沿革

### 创立与早期
- 公司于 October 2009 在特拉华州注册成立，名为 OS76, Inc.，并于 January 2010 更名为 Pure Storage。— 来源：SEC, "Pure Storage, Inc. Form S-1", 2015-08-27, https://www.sec.gov/Archives/edgar/data/0001474432/000119312515287576/d895532ds1.htm (retrieved 2026-11-01)
- 创始人为 John "Coz" Colgrove（曾任职 Veritas，2009 年为 Sutter Hill Ventures 的驻场创业者）和 John Hayes（曾任职 Yahoo 首席技术官办公室）。公司在 Sutter Hill 的办公室内孵化。— 来源：CNBC, "Disruptors in 2014: Pure Storage", 2014-06-17, https://www.cnbc.com/2014/06/17/disruptors-in-2014-pure-storage.html (retrieved 2026-11-01); Wikipedia, "Everpure", accessed 2026, https://en.wikipedia.org/wiki/Everpure (retrieved 2026-11-01)
- Scott Dietzen 于 2010 年出任 CEO，并带领公司完成 IPO。[VERIFY: 2010 年的上任时间仅见于渠道媒体] — 来源：ChannelE2E, "New Pure Storage CEO: Former Cisco Systems CTO Charles Giancarlo", 2017-08, https://channele2e.com/news/new-pure-storage-ceo-former-cisco-systems-cto-charles-giancarlo (retrieved 2026-11-01)
- FlashArray 于 May 2012 推出，同时推出"All Software Included"（软件全包）许可模式。— 来源：SEC, "Pure Storage, Inc. Form S-1", 2015-08-27, https://www.sec.gov/Archives/edgar/data/0001474432/000119312515287576/d895532ds1.htm (retrieved 2026-11-01)
- Evergreen 计划（以订阅方式提供不停机控制器升级）始于 2015 年初。其首个层级为"Evergreen Gold"，2022 年更名为 Evergreen//Forever。— 来源：IDC/Pure Storage, "Evergreen//Forever Subscription Ushers in New FlashBlade//S" (white paper), 2022, https://www.purestorage.com/content/dam/pdf/de-de/white-papers/wp-idc-evergreen-forever-subscription-ushers-in-new-flashblade-s-de-de.pdf (retrieved 2026-11-01)

### IPO
- IPO 于 October 6, 2015 定价：发行 2,500 万股（25 million）A 类股，每股 $17.00，为 $16–18 区间的中值，募资 $425 million。承销商拥有额外 375 万股（3.75 million）的 30 天超额配售选择权。Morgan Stanley 担任主承销商。— 来源：Pure Storage / Business Wire, "Pure Storage Prices Initial Public Offering", 2015-10-06, https://investor.purestorage.com/news-and-events/press-releases/press-release-details/2015/Pure-Storage-Prices-Initial-Public-Offering/default.aspx (retrieved 2026-11-01); Renaissance Capital, "Pure Storage prices IPO at $17, within the range", 2015-10-06, https://www.renaissancecapital.com/IPO-Center/News/35712/Pure-Storage-prices-IPO-at-$17-within-the-range (retrieved 2026-11-01)
- 公司于 October 7, 2015 以 PSTG 代码在 NYSE 开始交易。首日收盘价 $16.01，下跌 5.8%。Renaissance 称其为 2015 年规模最大的风投支持科技公司 IPO。— 来源：eWeek, "Pure Storage Goes Public, Stock Whiffs on First Day", 2015-10-07, https://www.eweek.com/storage/pure-storage-goes-public-stock-whiffs-on-first-day/ (retrieved 2026-11-01)

### FlashBlade
- FlashBlade 于 March 2016 发布，自 July 2016 起直接销售给部分客户。January 2017 宣布正式上市（GA），一篇报道称面向大众市场的发货始于 February 1, 2017。— 来源：GeekFluent, "Pure Storage's FlashBlade is now GA", 2017-01-25, https://geekfluent.com/2017/01/25/pure-storages-flashblade-is-now-ga/ (retrieved 2026-11-01); Impress Cloud Watch, 2017-02-06, https://cloud.watch.impress.co.jp/docs/news/1042656.html (retrieved 2026-11-01)

### CEO 更替
- August 22, 2017，董事会任命 Charles Giancarlo 为 CEO，接替转任董事长的 Scott Dietzen。该变动于 August 24, 2017 公布。Giancarlo 曾任 Cisco 的 CTO 兼首席开发官（1993–2007），以及 Avaya 临时 CEO（2008–09）。— 来源：SEC, "Pure Storage Form 8-K", 2017-08, https://www.sec.gov/Archives/edgar/data/0001474432/000162828017008861/pstg-8kq22017.htm (retrieved 2026-11-01); Pure Storage, "Q2 FY2018 announcement", 2017-08-24, https://purestorage.com/company/news-and-events/press/q2_2018_announcement.html (retrieved 2026-11-01)
- 截至 FY26 10-K（签署于 March 24, 2026）及 Q2 FY27 财报发布（Aug 26, 2026），Giancarlo 担任董事长兼 CEO，Tarek Robbiati 担任 CFO（约自 June 2025 起任职）。未发现 2026 年有 CEO 或 CFO 变动。— 来源：SEC, "Everpure Form 10-K FY2026", 2026-03-24, https://www.sec.gov/Archives/edgar/data/1474432/000147443226000027/pstg-20260201.htm (retrieved 2026-11-01)

### 收购
- **StorReduce**（云原生对象存储去重），于 August 2018 完成收购，扣除所获现金后现金对价 $20.5M。— 来源：SEC, "Pure Storage Form 10-K FY2020", 2020-03, https://www.sec.gov/Archives/edgar/data/1474432/000162828020004133/pstg-20200202.htm (retrieved 2026-11-01)
- **Compuverde**（瑞典文件软件开发商），于 April 2019 收购。交易条款未披露，但文件显示两年内向原股东支付约 $15.9M。— 来源：SEC, "Pure Storage Form 10-K FY2021", 2021-03, https://www.sec.gov/Archives/edgar/data/1474432/000162828021005538/pstg-20210131.htm (retrieved 2026-11-01); SiliconANGLE, 2019-04-03, https://siliconangle.com/?p=473523 (retrieved 2026-11-01)
- **Portworx**（Kubernetes 数据服务），于 October 2020 完成交割。宣布时金额约 $370M，而 10-K 记录的收购对价为 $352.9M，另加三年内支付的 $32.2M 留任款项。这是 Pure 截至当时历史上最大的一笔收购。— 来源：SEC, "Pure Storage Form 10-K FY2021", 2021-03, https://www.sec.gov/Archives/edgar/data/1474432/000162828021005538/pstg-20210131.htm (retrieved 2026-11-01); TechTarget, "Pure Storage acquires Portworx for container management", 2020-09, https://www.techtarget.com/searchstorage/news/252489099/Pure-Storage-acquires-Portworx-for-container-management (retrieved 2026-11-01)
- **1touch（1touch.io）**：于 February 23, 2026 与品牌更名同日宣布；据 Q1 FY27 10-Q，于 May 7, 2026 完成（Cleary Gottlieb 于 May 11, 2026 宣布交割）。价格为现金 $125.0M，可能根据调整及托管安排变动。1touch 提供数据发现、分类和语义上下文（"数据智能与编排"）。其产品重新推出为 **Everpure Data Intelligence**，于 June 2026 的 Accelerate 大会上 GA。— 来源：SEC, "Everpure Form 10-Q (Q1 FY27)", 2026-06, https://www.sec.gov/Archives/edgar/data/0001474432/000147443226000061/pstg-20260503.htm (retrieved 2026-11-01); Cleary Gottlieb, "Everpure Completes Acquisition of 1touch", 2026-05-11, https://www.clearygottlieb.com/news-and-insights/news-listing/everpure-completes-acquisition-of-1touch (retrieved 2026-11-01)
- **对 CoreWeave 的战略投资**（November 2024）：Pure 取得一笔未披露金额的股权，并成为 CoreWeave 专属环境中的首选存储方案之一。— 来源：Pure Storage, "Pure Storage Announces Strategic Investment and Technology Partnership with CoreWeave", 2024-11, https://www.purestorage.com/company/newsroom/press-releases/pure-announces-strategic-investment-and-tech-partnership-with-coreweave.html (retrieved 2026-11-01)

### 超大规模云厂商设计导入（design win）
- 在 Q3 FY25 业绩发布（Dec 3, 2024）中，Pure 宣布与一家未具名的"前四大超大规模云厂商"（top-four hyperscaler）达成 DirectFlash 设计导入。商业模式为技术许可加支持服务，销售中不含 Pure 硬件；该超大规模云厂商自行采购硬件。分析师普遍认为该客户是 Meta。Q3 FY25 营收为 $831.1M，增长 9%。— 来源：SiliconANGLE, "Shares of Pure Storage jump on impressive earnings beat and strong guidance", 2024-12-03, https://siliconangle.com/2024/12/03/shares-pure-storage-jump-impressive-earnings-beat-strong-guidance/ (retrieved 2026-11-01); Blocks & Files, "Pure Q3 2025", 2024-12-04, https://blocksandfiles.com/2024/12/04/pure-q3-2025/ (retrieved 2026-11-01)
- 在 March 2025 的 FlashBlade//EXA 发布会上，CEO 表示 Meta 因占地和功耗节省而选择了 Pure 的 DFM。此后的报道均称该客户为 Meta。[VERIFY: 需确认 Pure 本身首次点名 Meta 的确切日期] — 来源：Futurum, "Pure Storage Announces FlashBlade//EXA for the AI Factory", 2025-03, https://futurumgroup.com/insights/pure-storage-announces-flashblade-exa-for-the-ai-factory (retrieved 2026-11-01)
- 在 Q2 FY26 电话会（Aug 27, 2025）上，Pure 表示 Meta 已开始首次批量部署，首笔收入于 Q2 FY26 确认。CFO 表示，Pure 有信心在 FY26 结束前向 Meta 交付 1–2 EB 的 DirectFlash，甚至可能更多。Aug 28, 2025 股价盘中上涨约 24%（一篇报道称收盘上涨约 32%，创纪录）。— 来源：Blocks & Files, "Pure knocking it out of the park", 2025-08-29, https://blocksandfiles.com/2025/08/29/pure-knocking-it-out-of-the-park/ (retrieved 2026-11-01); Barron's via iTiger, "Pure Storage Stock Rallies 24%. A Meta Deal Has Something to Do With It", 2025-08-28, https://www.itiger.com/news/2562879055 (retrieved 2026-11-01)
- 在 Q4 FY26 电话会上，管理层表示超大规模业务超出 FY26 预期，并预计在 FY27 继续增长，主要集中在 Q3–Q4 FY27。在 Q1 FY27 时，管理层表示超大规模业务收入规模尚小，根据客户订单承诺，预计将在 Q3 和 Q4 显著上升。— 来源：Futurum, "Everpure Q4 FY 2026 Revenue Passes $1 Billion as Platform Strategy Scales", 2026-02, https://futurumgroup.com/insights/everpure-q4-fy-2026-revenue-passes-1-billion-as-platform-strategy-scales (retrieved 2026-11-01); Everpure, "Q1 FY27 Prepared Remarks", 2026-05-27, https://s21.q4cdn.com/687136699/files/doc_financials/2027/q1/Everpure-Q1FY27-Prepared-Remarks.pdf (retrieved 2026-11-01)
- August 10, 2026，Everpure 宣布与**第二家前五大超大规模云厂商**（未具名）达成基于 DirectFlash 的设计导入及供货协议。Everpure 预计自 FY2028 起产生可观收入；对 FY27 的贡献极小。管理层表示，Everpure 不为超大规模业务采购 NAND。— 来源：Everpure, "Everpure Lands New Design Win with Second Top-Five Hyperscaler", 2026-08-10, https://www.everpuredata.com/company/newsroom/press-releases/everpure-lands-new-design-win-with-second-top-five-hyperscaler.html (retrieved 2026-11-01); Motley Fool, "Everpure (P) Q2 2027 Earnings Call Transcript", 2026-08-31, https://www.fool.com/earnings/call-transcripts/2026/08/31/everpure-p-q2-2027-earnings-call-transcript/ (retrieved 2026-11-01)
- Pure 的超大规模云厂商页面称，DFM 相比 HDD 可降低功耗最多 75%，总功耗最多降低 54%（厂商声称）。— 来源：Pure Storage, "Hyperscaler", n.d., https://purestorage.com/pure-advantage/platform/hyperscaler.html (retrieved 2026-11-01)

### Enterprise Data Cloud（June 2025）
- June 18, 2025，在拉斯维加斯举行的 Pure//Accelerate 2025 上，Pure 推出 **Enterprise Data Cloud（EDC）** 架构：一个横跨本地与云端的统一控制平面，以 Pure Fusion 为核心。它将存储呈现为虚拟化、可自我发现的资源池，并配有编排中心、自动化模板（DRaaS、资源配置）以及 Rubrik 和 CrowdStrike 集成。— 来源：Blocks & Files, "Pure debuts Enterprise Data Cloud with Fusion updates and new FlashArray systems", 2025-06-18, https://www.blocksandfiles.com/ai-ml/2025/06/18/pure-debuts-enterprise-data-cloud-with-fusion-updates-and-new-flasharray-systems/100996 (retrieved 2026-11-01)
- Accelerate 2025 还发布了 FlashArray//XL R5（原始容量最高 1.9 PB / 有效容量 7.4 PB；性能提升因来源不同报道为 +50% 或 +70%）、FlashArray//ST（延迟优化、仅支持块存储、不使用 DFM，首发约 102 TB，并计划推出更大容量版本）、FlashArray 上的 S3 对象存储支持，以及 FlashBlade//S R2。[VERIFY: //XL R5 性能数字在不同来源间不一致；//ST 计划容量报道为 300 TB 或 400 TB] — 来源：Techzine, "Pure surprises: FlashArray gets S3 support, FlashArray//ST without DFMs", 2025-06, https://www.techzine.eu/blogs/infrastructure/132388/pure-surprises-flasharray-gets-s3-support-flasharray-st-without-dfms/ (retrieved 2026-11-01); Architecting IT, "Research Note: Pure Storage introduces Enterprise Data Cloud", 2025-06, https://www.architecting.it/blog/pure-edc/ (retrieved 2026-11-01)

### September 2025 发布
- FlashArray//X R5 和 //C R5 换代改用 Intel Emerald Rapids 处理器：//X 较 R4 提升约 +30%，//C 提升约 +40%。3RU 机箱默认可容纳 28 块盘（容量 +40%）。两款产品在发布时即 GA。FlashArray//XL190 计划于 Feb–Apr 2026 推出。Pure 还推出了 **Pure Storage Cloud Azure Native**（与 Microsoft 联合开发），并宣布 KVA 与 NVIDIA Dynamo 集成。— 来源：Blocks & Files, "Pure Enterprise Data Cloud updates", 2025-09-26, https://blocksandfiles.com/2025/09/26/pure-enterprise-data-cloud-updates/ (retrieved 2026-11-01)

### 更名为 Everpure（2026）
- February 23, 2026，Pure Storage 宣布战略性品牌更名为 **Everpure™**，体现其从全闪存存储向 AI 时代数据管理的转型。Giancarlo 表示，新名称"captures the power of our Enterprise Data Cloud architecture and adaptability of Evergreen"。1touch 收购于同日宣布。— 来源：WWT, "Pure Storage Rebrands To Everpure And Announces Intent To Acquire 1touch", 2026-02-23, https://www.wwt.com/news/pure-storage-rebrands-to-everpure-and-announces-intent-to-acquire-1touch (retrieved 2026-11-01); ChannelWeb UK, "Pure Storage CEO on Everpure name change and 1Touch acquisition", 2026-02, https://www.channelweb.co.uk/news-network/2026/pure-storage-ceo-on-everpure (retrieved 2026-11-01)
- 约 March 5, 2026 起以 Everpure 名称在 NYSE 交易，初期代码仍为 PSTG。公司官网迁至 everpuredata.com。[VERIFY: March 5 这一日期仅来自单一二手来源] — 来源：Pulse 2.0, "Pure Storage Rebrands To Everpure And Announces Intent To Acquire 1touch", 2026-02-23, https://pulse2.com/pure-storage-rebrands-to-everpure-and-announces-intent-to-acquire-1touch (retrieved 2026-11-01)
- April 7, 2026，Everpure 宣布将股票代码由 PSTG 改为 **P**，约于 April 17, 2026 生效。CUSIP 不变。— 来源：Finviz/PR Newswire, "Everpure to Change Ticker Symbol to P", 2026-04-07, https://finviz.com/news/342850/everpure-to-change-ticker-symbol-to-p (retrieved 2026-11-01)
- 商标说明："Everpure"同时也是一个历史悠久的净水过滤品牌（Pentair 于 2004 年收购 Everpure Inc.），这会造成搜索和名称上的混淆。— 来源：SDxCentral coverage via search; WWD Mag, "Pentair completes acquisition of Everpure Inc.", n.d., https://wwdmag.com/sludge-management/pentair-completes-acquisition-everpure-inc (retrieved 2026-11-01)

### Pure//Accelerate 2026（June 16–18, 2026，拉斯维加斯）
- Everpure 发布了"**Data Primacy**"（数据至上）架构，将可信数据而非应用置于中心。它宣布 **Everpure Data Intelligence**（原 1touch）GA，并宣布 **Everpure Data Stream** GA（June 17 新闻稿）。Data Stream 基于 NVIDIA AI Data Platform 参考设计：一条 GPU 加速的从数据摄取到推理的流水线，集成向量数据库和 NIM。— 来源：HPCwire/BigDATAwire, "Everpure Announces Data Stream to Expand AI-Ready Data Offerings", 2026-06-17, https://www.hpcwire.com/bigdatawire/this-just-in/everpure-announces-data-stream-to-expand-ai-ready-data-offerings/ (retrieved 2026-11-01); HPCwire, "Everpure Wants to Improve Data Management for the Coming AI Wave", 2026-06-20, https://www.hpcwire.com/aiwire/2026/06/20/everpure-wants-to-improve-data-management-for-the-coming-ai-wave/ (retrieved 2026-11-01)
- 同时发布的还有：搭载 Purity Turbo 的 FlashArray//XL190；面向新兴 GPU 云（neocloud）的 FlashBlade//EXA 多租户与 QoS；**Evergreen//One Overdrive**（可临时突发至订阅水平以上最多 25%，预计 Q3 2026 推出）；Everpure Cloud 的 Azure 原生 VM 支持 GA；以及与 NVIDIA 合作，基于 NVIDIA 的 STX 参考架构为 FlashBlade//EXA 打造 AI 原生存储。[VERIFY: Overdrive 和 Azure 相关条目来自二手摘要] — 来源：Coolspirit, "Pure Accelerate 2026: What the Latest Announcements Mean", 2026-06, https://www.coolspirit.co.uk/blogs/pure-accelerate-2026-what-the-latest-announcements-mean-for-enterprise-storage (retrieved 2026-11-01); Daymark, "Everpure Data Primacy in Practice", 2026, https://www.daymarksi.com/blog/everpure-data-primacy-in-practice (retrieved 2026-11-01)
- September 30, 2026，在 Pure//Accelerate London 上，Everpure 宣布 FlashBlade 上的 **PureKVA**（声称首 token 延迟最多快 20x；未公布测试细节）、**常开的 Purity DeepReduce**（预计在 FlashBlade//E 和 //S200 R2 上实现中位数 2:1 的全局数据缩减），以及 Data Intelligence 中的原生 MCP 支持。上述功能于 October 2026 推出。— 来源：Blocks & Files, "Everpure bulks up AI offer", 2026-09-30, https://blocksandfiles.com/flash/2026/09/30/everpure-bulks-up-ai-offer/5300162 (retrieved 2026-11-01); StorageReview, "Everpure Adds PureKVA to FlashBlade, Claims Up to 20x Faster TTFT, Makes DeepReduce Always-On", 2026-09/10, https://www.storagereview.com/news/everpure-purekva-flashblade-20x-time-to-first-token-always-on-deepreduce (retrieved 2026-11-01)

---

## 2. 产品线（截至 2026 年末）

### FlashArray（块存储，现亦支持文件和 S3；Purity//FA）
- **//XL**：R5 代于 June 2025 推出。**//XL190** 约于 January 2026 GA，搭载 **Purity Turbo**——这是 XL190 独有的功能，允许备用控制器处理读请求。报道的规格约为 18M IOPS 和 200 GB/s。它以"FlashArray//XL190R5"之名列入 ENERGY STAR。[VERIFY: IOPS 和吞吐量数字来自发布期的单一报道] — 来源：Everpure, "Pure Launch Blog: January 2026 Edition", 2026-01, https://blog.everpuredata.com/products/pure-launch-blog-january-2026-edition/ (retrieved 2026-11-01)
- **//X R5 和 //C R5**：自 September 2025 起 GA（见 §1）。//X 为 TLC 性能型，//C 为 QLC 容量型；二者共用控制器。— 来源：Blocks & Files, 2025-09-26 (above)
- **//E**：用于替代磁盘和二级存储的 QLC 容量层，于 2023 年与 75 TB DFM 及 //X、//C R4 一同推出。— 来源：StorageReview, "Pure Storage adds 75TB flash module, FlashArray//E and new FlashArray//X, //C R4 nodes", 2023, https://www.storagereview.com/news/pure-storage-adds-75tb-flash-module-flasharray-e-and-new-flasharray-x-c-r4-nodes (retrieved 2026-11-01)
- **//ST**：延迟优化、仅支持块存储，使用商用 SSD 而非 DFM（June 2025）。报道称在 5RU 内基于 PCIe 5 SSD 可提供最高 400 TB 可用容量。[VERIFY: 各来源的容量数字不一致] — 来源：Techzine, 2025-06 (above)

### FlashBlade（文件和对象存储；Purity//FB）
- **//S R2**（S100、S200 和 S500 系列）。一份合作伙伴产品列表称每个刀片最高 1,200 TB，配备 400GbE。该产品正在推进 NEBS Level 1 合规。[VERIFY: 每刀片容量数字为合作伙伴声称] — 来源：Everpure, "Pure Launch Blog: January 2026 Edition", 2026-01, https://blog.everpuredata.com/products/pure-launch-blog-january-2026-edition/ (retrieved 2026-11-01)
- **//E**：容量优化型文件和对象存储。Purity DeepReduce 约于 January–February 2026 在 //E 上 GA。— 来源：same as above
- **//EXA**：面向 AI 和 HPC 的分解式平台（见 §3）。
- 未发现任何"FlashBlade//ZEN"产品的证据。[VERIFY: 未找到该术语]

### DirectFlash 模块（DFM）
- 75 TB DFM 自 2023 年起出货。2023 年 Pure 制定的路线图为 end-2024 达到 150 TB、end-2025 达到 300 TB，后来调整为 2025 年 150 TB、2026 年 300 TB。— 来源：Gigazine, "Pure Storage sets goal of realizing 300 TB SSD by 2026", 2023-03-08, https://gigazine.net/gsc_news/en/20230308-pure-storage-300-tb-ssd (retrieved 2026-11-01)
- Micron G8 QLC NAND 已通过 150 TB DFM 的认证，Micron G9 QLC 将用于未来的超大规模云厂商 DFM。Kioxia（BiCS8 2 Tb QLC）被描述为长期 NAND 合作伙伴。— 来源：Blocks & Files, "Pure qualifies Micron's 276-layer flash", 2025-01-08, https://blocksandfiles.com/2025/01/08/pure-qualifies-microns-276-layer-flash/ (retrieved 2026-11-01); TechTarget, "Pure Storage, Micron expand QLC NAND partnership", 2025, https://techtarget.com/searchstorage/news/366617703/Pure-Storage-Micron-expand-QLC-NAND-partnership (retrieved 2026-11-01); Blocks & Files, "Kioxia 2 terabit NAND", 2024-07-03, https://blocksandfiles.com/2024/07/03/kioxia-2-terabit-nand/ (retrieved 2026-11-01)
- Blocks & Files（August 2026）称 DFM 容量"now reaches 300 TB per module"（现已达到每模块 300 TB）。[VERIFY: 未找到 300 TB DFM 的官方 GA 或出货日期公告；600 TB 和 1 PB 仅为表述中的目标] — 来源：Blocks & Files, "Second hyperscaler plumps for Everpure's flash technology", 2026-08-11, https://www.blocksandfiles.com/flash/2026/08/11/second-hyperscaler-plumps-for-everpures-flash-technology/5285903 (retrieved 2026-11-01)

### 软件、云与订阅
- **Pure Fusion**：EDC 核心的集群（设备群）控制平面（June 2025）。— 来源：Blocks & Files, 2025-06-18 (above)
- **Pure1**：SaaS 监控与 AIOps。[VERIFY: 未检索到 2026 年的专门来源]
- **Evergreen 系列**（June 2022 正式成形）：Evergreen//Forever（原 Evergreen Gold；自有阵列加不停机升级）、Evergreen//Flex（集群级容量按用量付费，2022 年新推出）以及 Evergreen//One（存储即服务，原名 Pure-as-a-Service，该名称约自 2019 年起使用）。— 来源：Blocks & Files, "Pure Storage Evergreen rework", 2022-06-08, https://blocksandfiles.com/2022/06/08/pure-storage-evergreen-rework/ (retrieved 2026-11-01)
- **云**：Cloud Block Store 已更名为 **Pure Storage Cloud Dedicated**，由客户在 AWS（含 EVS 集成）和 Azure（含 AVS）上自行管理。**Pure Storage Cloud Azure Native** 是联合开发、全托管的 Azure 原生集成（Azure Native Integration）。— 来源：Pure Community, "Pure Cloud Block Store is now Pure Storage Cloud Dedicated", n.d., https://purecommunity.purestorage.com/tag/cloud (retrieved 2026-11-01); Microsoft Learn, "Pure Storage Cloud overview", n.d., https://learn.microsoft.com/en-us/azure/partner-solutions/pure-storage/overview (retrieved 2026-11-01)
- **Portworx by Everpure**：Portworx Enterprise 3.6 和 Backup 2.11（March 2026）新增经验证的 KubeVirt 框架和一个开源 VM 就绪度评估工具。Everpure 称其在 Kubernetes 上管理超过 100,000 个 VM 卷。— 来源：IT Brief NZ, "Everpure adds VM storage tools for Kubernetes estates", 2026-03, https://itbrief.co.nz/story/everpure-adds-vm-storage-tools-for-kubernetes-estates (retrieved 2026-11-01)
- **Key Value Accelerator（KVA）**：FlashBlade 上的持久化分布式 LLM KV 缓存（S3 和 NFS），可接入 vLLM 和 NVIDIA Dynamo，并通过 RDMA 将数据传入 GPU 内存。Pure 声称推理速度最多提升 20x。Dynamo 集成于 September 2025 宣布，预计 Feb–Apr 2026 推出。自 September 2026 起品牌名为"PureKVA"。— 来源：Pure Storage blog, "Breaking Enterprise AI Bottlenecks: 20X Faster Inference with the First KV Cache for S3 and NFS", 2025, https://blog.purestorage.com/purely-technical/20x-faster-inference-first-kv-cache-for-s3-and-nfs/ (retrieved 2026-11-01); Blocks & Files, 2025-09-26 (above)

### NVIDIA 认证
- November 2024：FlashBlade//S500 获得基于以太网的 NVIDIA DGX SuperPOD 认证，Pure 成为第七家 SuperPOD 存储供应商。同时推出了 GenAI Pod。— 来源：Blocks & Files, "Pure FlashBlade SuperPOD certification", 2024-11-18, https://blocksandfiles.com/2024/11/18/pure-flashblade-superpod-certification/ (retrieved 2026-11-01)
- March 2025（GTC）：FlashBlade 获得 Foundation 和 Enterprise 级别的 NVIDIA-Certified Storage 认证，以及面向 NVIDIA Cloud Partner 参考架构（HGX B200/H200）的 HPS 认证。Pure 还将 NVIDIA AI Data Platform 集成到 FlashBlade 中。— 来源：Blocks & Files, "Pure Storage expands AI capabilities with Nvidia certification", 2025-03-19, https://www.blocksandfiles.com/ai-ml/2025/03/19/pure-storage-expands-ai-capabilities-with-nvidia-certification/1595136 (retrieved 2026-11-01)
- 一家经销商称，基于 FlashBlade//S 的平台已获得 GB200 和 GB300 上的 DGX SuperPOD 认证。[VERIFY: 仅有经销商来源] 未发现任何来源显示 **FlashBlade//EXA** 本身获得了 DGX SuperPOD 认证。[VERIFY] — 来源：ASBIS, "ASBIS Delivers End-to-End AI Infrastructure with Pure Storage and NVIDIA DGX SuperPOD", 2025, https://news.asbis.com/news/ai-driven-world/asbis-delivers-ai-infrastructure-with-purestorage-and-nvidia/ (retrieved 2026-11-01)

### MLPerf Storage
- **v2.0（August 2025）**：Pure 为 FlashBlade//EXA 发布了一份"MLPerf Storage v2.0 test results"白皮书，但我无法确认存在任何正式的 MLCommons 提交。v3.0 的相关报道称 Everpure 的 v3.0 参赛是其*首次* MLPerf Storage 提交。[VERIFY] — 来源：Everpure, "FlashBlade//EXA MLPerf Storage v2.0 Test Results" (white paper), n.d., https://www.everpuredata.com/content/dam/pdf/en/white-papers/twp-flashblade-exa-mlperf-storage-v2-0-test-results.pdf (retrieved 2026-11-01)
- **v3.0（结果约于 late August 2026 公布；Everpure 新闻稿 Sept 2, 2026）**：配备 30 个数据节点的 FlashBlade//EXA 实现 **877.5 GiB/s 检查点写入**（本轮第一，领先于 642.2 GiB/s 的 Azure Managed Lustre）和 588.3 GiB/s 读取。在 51 台主机的配置上实现 **1,623.4 GiB/s KV 缓存读取**，以及 85,736 tokens/s（Llama 3.1 8B，仅存储）和 33,403 tokens/s（70B）。配置为 30 个 EXA 刀片（含 120 个用于元数据的 DFM）加 30 个 Linux/NVMe 数据节点。v3.0 模拟的是 B200 加速器（v2.0 模拟 H100），因此不同版本间的结果不可比。— 来源：StorageReview, "MLPerf Storage v3.0: 877 GiB/s checkpoints, a cloud first and a leaderboard turned over", 2026-08/09, https://storagereview.com/news/mlperf-storage-v3-0-877-gib-s-checkpoints-a-cloud-first-and-a-leaderboard-turned-over (retrieved 2026-11-01); HPCwire, "Everpure Leads MLPerf Storage Tests for Large Model Checkpointing and KV Cache", 2026-09-02, https://hpcwire.com/off-the-wire/everpure-leads-mlperf-storage-tests-for-large-model-checkpointing-and-kv-cache (retrieved 2026-11-01)

---

## 3. FlashBlade//EXA 架构
- FlashBlade//EXA 于 March 11, 2025 发布，面向大规模 AI 和 HPC。Pure 称其为"the world's most powerful data storage platform"（全球最强大的数据存储平台）。— 来源：SiliconANGLE, "FlashBlade//EXA: Pure Storage helps enterprises avoid starving data-hungry GPUs", 2025-03-11, https://siliconangle.com/2025/03/11/flashblade-exa-pure-storage-helps-enterprises-avoid-starving-data-hungry-gpus-accelerate-ai-workloads/ (retrieved 2026-11-01)
- 它采用两个可独立扩展的集群。**Metadata Core**（元数据核心）运行在配备 DFM 的 FlashBlade 刀片上（报道的配置为 1–10 个机箱，每机箱 10 个刀片）。发布时，**Data Nodes**（数据节点）是配备 NVMe SSD 的现成第三方 Linux 服务器。元数据节点位于数据路径之外，但会监控数据节点的容量和健康状态。客户端通过 pNFS（基于 TCP 的 NFSv4.1）访问元数据核心，并直接与数据节点之间收发数据。— 来源：Architecting IT, FlashBlade//EXA analysis, 2025-03, https://www.architecting.it/?p=7294 (retrieved 2026-11-01); Pure Storage, "FlashBlade//EXA for AI" (solution brief), 2025, https://www.purestorage.com/content/dam/pdf/en/solution-briefs/sb-flashblade-exa-ai.pdf (retrieved 2026-11-01)
- Pure 计划在后续版本中推出基于 DFM 的数据节点（75 TB 和 150 TB DFM，每台数据服务器最多 24 个 DFM），预计于 2H 2025 推出。[VERIFY: DFM 数据节点的 GA 尚未确认] — 来源：NAND Research, "Pure Storage FlashBlade//EXA", 2025-03, https://nand-research.com/?p=3935 (retrieved 2026-11-01); Le Monde Informatique, 2025-03, https://www.lemondeinformatique.fr/actualites/lire-avec-flashblade-exa-pure-storage-s-attaque-au-traitement-des-metadonnees-pour-l-ia-96311.html (retrieved 2026-11-01)
- Pure 根据初步测试声称"more than 10 TB/s read performance in a single namespace"（单一命名空间内读性能超过 10 TB/s）（厂商声称）。— 来源：StorageReview, "FlashBlade//EXA: Pure Storage's new AI/HPC powerhouse with 10 TB/s performance", 2025-03-11, https://www.storagereview.com/news/flashblade-exa-pure-storages-new-ai-hpc-powerhouse-with-10-tb-s-performance (retrieved 2026-11-01)
- 上市时间指引为"summer 2025"。[VERIFY: 未找到明确的 GA 新闻稿] 首个企业级 EXA 客户于 Q4 FY26（Nov 2025–Jan 2026）签下，另有"dozens more"（数十家）处于深入洽谈阶段。— 来源：Techzine, "Pure's FlashBlade//EXA should solve storage bottlenecks in AI and HPC", 2025-03, https://techzine.eu/blogs/infrastructure/129502/pures-flashblade-exa-should-solve-storage-bottlenecks-in-ai-and-hpc (retrieved 2026-11-01); Futurum, Q4 FY26 analysis, 2026-02 (above)
- 2026 年，EXA 被定位于新兴 GPU 云和 AI 原生服务商，并在 Accelerate 2026 上新增多租户和 QoS。Everpure 还公布了高于 7,200 的 SPEC AI 成绩 [VERIFY: 仅来自 vmblog 摘要]，以及 EXA 上的 KVA 可在 PB 级前缀复用中实现 10+ TB/s 的声称。— 来源：Everpure blog, "Meet FlashBlade//EXA: the AI Data Platform for Scale", 2026-06, https://blog.everpuredata.com/products/meet-flashblade-exa-the-ai-data-platform-for-scale/ (retrieved 2026-11-01); Everpure blog, "Everpure KVA Meets FlashBlade//EXA", 2026, https://blog.everpuredata.com/purely-technical/everpure-kva-meets-flashblade-exa-enterprise-kv-caching-at-neocloud-scale/ (retrieved 2026-11-01)

---

## 4. 财务

### FY2026（于 Feb 1, 2026 结束；于 Feb 25, 2026 公布）
- 总营收为 **$3,662.8M**（+16%）：产品 $1,971.7M（+16%），订阅服务 $1,691.2M（+15%）。产品约占营收的 54%，订阅约占 46%。— 来源：SEC, "Everpure Form 10-K FY2026", 2026-03-24, https://www.sec.gov/Archives/edgar/data/1474432/000147443226000027/pstg-20260201.htm (retrieved 2026-11-01)
- 美国营收为 $2.5B（+12%，上年为 $2.2B），其他地区营收为 $1.2B（+25%，上年为 $960.8M）。— 来源：same 10-K
- 毛利率为 **70.4%（GAAP）和 72.1%（非 GAAP）**。非 GAAP 营业利润率为 **17.3%**。自由现金流为 **$616M**。— 来源：SEC, "Everpure Q4 FY2026 Press Release (Ex. 99.1)", 2026-02-25, https://www.sec.gov/Archives/edgar/data/1474432/000147443226000015/pstg-ex991q4fy2026.htm (retrieved 2026-11-01)
- 订阅 ARR 为 **$1,924.3M**（+16%，上年为 $1,657.8M）。由于 Evergreen 续约期限拉长，增速由 21% 放缓。订阅净美元留存率为 113%（FY25：117%）。— 来源：Everpure 10-K FY2026 (above)
- RPO 为 **$3.7B**（+40%，FY25 为 +14%），由大额交易以及 Evergreen//Forever 和 //One 推动。订阅 RPO 增长 34%。— 来源：Everpure Form ARS FY2026, https://www.sec.gov/Archives/edgar/data/0001474432/000147443226000043/a10kfy2026.htm (retrieved 2026-11-01)
- 客户：FY26 新增客户超过 1,100 家（Q4 为 335 家）。据报道，FY26 Evergreen//One 及存储即服务的合同总价值（TCV）为 $520M（+32%），其中 Q4 为 $179M（+28%）。[VERIFY: TCV 和客户数字来自电话会纪要摘要] FY25 公司客户基数为"13,000+"家，约覆盖 Fortune 500 的 60%。August 2026，公司引用的客户数为 14,500+ 至 15,000 家。[VERIFY: 存在两个不同数字] — 来源：ROIC.ai, "Everpure Q4 FY2026 Earnings Call Transcript", 2026-02-25, https://www.roic.ai/quote/P/transcripts/2026-year/4-quarter (retrieved 2026-11-01); Everpure, "2025 Pure Impact Fact Sheet", 2025, https://www.everpuredata.com/content/dam/pdf/en/misc/sustainability/2025-pure-impact-fact-sheet.pdf (retrieved 2026-11-01)
- 员工人数约为 6,400 名全职员工（FY26）。[VERIFY: 来自 Yahoo Finance 和 Wikipedia，并非直接从 10-K 中读取] — 来源：Yahoo Finance, "Everpure, Inc. (P) Profile", 2026, https://finance.yahoo.com/quote/P/profile/ (retrieved 2026-11-01)
- FY26 末现金、现金等价物及有价证券为 $1.5B。— 来源：Everpure 10-K FY2026 (above)

### Q4 FY2026
- 营收为 **$1.1B（+20%）**，是公司首个营收超过 $1B 的季度：产品 $618M（+25%），订阅服务 $440M（+14%）。毛利率为 69.9%（GAAP）和 71.4%（非 GAAP）。产品毛利率为 67.3%（受产品组合影响提升超过 400 bp）。非 GAAP 营业利润率为 21.3%，自由现金流（FCF）为 $201M。— 来源：Morningstar/PR Newswire, "Everpure Announces Fiscal Fourth Quarter and Full Year 2026 Financial Results", 2026-02-25, https://www.morningstar.com/news/pr-newswire/20260225sf95343/everpure-announces-fiscal-fourth-quarter-and-full-year-2026-financial-results (retrieved 2026-11-01)
- 由于元器件（NAND）成本飙升，Everpure 于 Feb 9, 2026 提价。公司指引 Q1 产品毛利率处于其 65–70% 区间的低端。— 来源：Alpha Spread, "P Q4-2026 Earnings Call", 2026-02-25, https://www.alphaspread.com/security/nyse/p/investor-relations/earnings-call/q4-2026 (retrieved 2026-11-01)
- **初始 FY27 指引**：营收 $4.3–4.4B（+17–20%），非 GAAP 营业利润 $780–820M。Q1 指引为 $990M–$1.01B。— 来源：Futurum, 2026-02 (above)

### Q1 FY2027（于 May 3, 2026 结束；于 May 27, 2026 公布）
- 营收为 **$1,052.9M（+35%）**：产品 $577M（+55%），订阅服务 $476M（+17%，约占营收 45%）。订阅 ARR 为 **$2.036B（+19%）**，RPO 为 $3.8B（+41%）。GAAP 营业利润为 $20M，非 GAAP 营业利润为 $159M。— 来源：Everpure, "Everpure Announces First Quarter Fiscal 2027 Financial Results", 2026-05-27, https://investor.everpuredata.com/news-and-events/press-releases/press-release-details/2026/Everpure-Announces-First-Quarter-Fiscal-2027-Financial-Results/default.aspx (retrieved 2026-11-01); TradingView, "Everpure 1Q 2027 10-Q Summary", 2026-06, https://www.tradingview.com/news/tradingview:335afadce5a54:0-everpure-inc-1q-2027-revenue-1-05b-eps-0-07-10-q-summary/ (retrieved 2026-11-01)
- 毛利率为 68.7%（GAAP）和 70.1%（非 GAAP）；产品毛利率 65.5%，订阅毛利率 75.6%。Evergreen//One 销售额增长 73%。新增客户 275 家。— 来源：Nasdaq, "Everpure Q1 Earnings Call Highlights", 2026-05, https://www.nasdaq.com/articles/everpure-q1-earnings-call-highlights (retrieved 2026-11-01)
- FY27 指引上调至营收 $4.41–4.51B，非 GAAP 营业利润 $820–860M。— 来源：StockTitan, "Everpure Q1 2027 8-K", 2026-05-27, https://www.stocktitan.net/sec-filings/P/8-k-everpure-inc-reports-material-event-89335bfe97b2.html (retrieved 2026-11-01)

### Q2 FY2027（于 Aug 2, 2026 结束；于 Aug 26, 2026 公布）。最近一个已公布季度
- 营收为 **$1.19B（+38%）**：产品 $687M（+54%），订阅服务 $499M（+20%）。订阅 ARR 为 **$2.13B（+20%）**，RPO 为 **$4.1B（+44%）**。— 来源：Everpure, "Everpure Announces Second Quarter Fiscal 2027 Financial Results", 2026-08-26, https://investor.everpuredata.com/news-and-events/press-releases/press-release-details/2026/Everpure-Announces-Second-Quarter-Fiscal-2027-Financial-Results/default.aspx (retrieved 2026-11-01); Investing.com, "Everpure Q2 FY27 slides", 2026-08, https://www.investing.com/news/company-news/everpure-q2-fy27-slides-38-revenue-growth-guidance-raised-sharply-93CH-4878054 (retrieved 2026-11-01)
- 毛利率为 68.4%（GAAP）和 69.9%（非 GAAP）；产品毛利率 66.2%，订阅毛利率 74.9%。GAAP 营业利润率为 5.3%。非 GAAP 营业利润为 $230M（19.4%）。— 来源：Investing.com (above)
- 经营现金流为 **–$136M**，自由现金流为 **–$238M**（资本开支 $101M），原因是战略性采购 NAND 和元器件（预付款占用约 $577M）。管理层预计经营现金流将在两个季度内恢复正常，FY27 自由现金流为 $600–800M。— 来源：Yahoo Finance, "Everpure (P) Grew Revenue 38% but Free Cash Flow Was Negative", 2026-08, https://finance.yahoo.com/markets/stocks/articles/everpure-p-grew-revenue-38-023544268.html (retrieved 2026-11-01)
- 存储即服务 TCV（含 Evergreen//One）为 $277M（+121%）。管理层表示，FY27 Evergreen//One 的 TCV 年化运行率超过 $1B。[VERIFY: 来自电话会摘要] — 来源：Motley Fool transcript, 2026-08-31 (above)
- **当前 FY27 指引**：营收 **$5.03–5.07B**（中值较 $3.66B 增长约 +38%），非 GAAP 营业利润 $940–960M，Q3 FY27 营收 $1.325–1.335B。截至 2026-11-01，Q3 FY27 尚未公布（预计约于 late November 公布）。— 来源：Everpure Q2 FY27 press release (above)

### 年度营收，FY2016–FY2026（百万美元，来自 10-K 文件）
| 财年（截止日） | 营收（$M） | 同比 | 备注 |
|---|---|---|---|
| FY2016 (Jan 31, 2016) | 440.3 | +152% | FY16 10-K |
| FY2017 | 728.0 | +65% | 原始 10-K；重述后为 739.2（ASC 606） |
| FY2018 | 1,023.0 | +41% | 原始 10-K；重述后为 1,024.8 |
| FY2019 | 1,359.8 | +33% | FY20 10-K |
| FY2020 | 1,643.4 | +21% | FY20 10-K |
| FY2021 | 1,684 | +2% | [VERIFY: 来自 Macrotrends，未与 10-K 核对] |
| FY2022 | 2,181 | +29% | [VERIFY: 来自 Macrotrends，未与 10-K 核对] |
| FY2023 | 2,753.4 | +26% | FY24 10-K |
| FY2024 | 2,830.6 | +3% | FY24 10-K |
| FY2025 (Feb 2, 2025) | ~3,170 | +12% | [VERIFY: 精确到千位的数字待核；报道为 $3.17B] |
| FY2026 (Feb 1, 2026) | 3,662.8 | +16% | FY26 10-K |
| FY2027E | 5,030–5,070 | ~+38% | 截至 Aug 26, 2026 的指引 |

来源：SEC 10-Ks FY2016 https://www.sec.gov/Archives/edgar/data/0001474432/000156459016015322/pstg-10k_20160131.htm ; FY2017 https://www.sec.gov/Archives/edgar/data/0001474432/000162828017003034/a10k2017.htm ; FY2018 https://www.sec.gov/Archives/edgar/data/0001474432/000162828018003579/a10k2018.htm ; FY2020 https://www.sec.gov/Archives/edgar/data/1474432/000162828020004133/pstg-20200202.htm ; FY2024 https://www.sec.gov/Archives/edgar/data/1474432/000162828024013860/pstg-20240204.htm ; FY2025 https://www.sec.gov/Archives/edgar/data/1474432/000162828025015044/pstg-20250202.htm ; FY2026 (above); Macrotrends https://new.macrotrends.net/stocks/charts/PSTG/pure-storage/revenue (all retrieved 2026-11-01)

- FY2025 明细：产品 $1.70B（+5%），订阅服务 $1.47B（+22%），ARR $1,657.8M（+21%）。约 48% 的 RPO 将在 12 个月内到期。— 来源：SEC, "Pure Storage Form 10-K FY2025", 2025-04, https://www.sec.gov/Archives/edgar/data/1474432/000162828025015044/pstg-20250202.htm (retrieved 2026-11-01)

---

## 5. 合作伙伴关系
- **NVIDIA**：DGX SuperPOD（FB//S500，Nov 2024）；NVIDIA-Certified Storage 及 NCP HPS（Mar 2025）；AI Data Platform 集成；Dynamo/KVA（Sept 2025）；基于 AI Data Platform 参考设计的 Data Stream（June 2026）；面向 EXA 的 STX 参考架构合作（2026）。— 来源：Sources in §2 and §1
- **Cisco（FlashStack）**：自 2014 年以来的融合基础设施合作 [VERIFY: 起始年份凭记忆]。November 2023 推出了 FlashStack for AI CVD 并获得 NVIDIA BasePOD 验证。late October 2025，一个新的 FlashStack CVD 加入 **Cisco Secure AI Factory with NVIDIA** 中的 AI POD，于 Q1 2026 通过 AHEAD、ePlus、SHI 和 WWT GA。— 来源：StorageNewsletter, "Pure Storage and Cisco Deliver AI Factories for the Enterprise with Nvidia", 2025-11-07, https://www.storagenewsletter.com/2025/11/07/pure-storage-and-cisco-deliver-ai-factories-for-the-enterprise-with-nvidia/ (retrieved 2026-11-01); Blocks & Files, 2023-11-13, https://blocksandfiles.com/2023/11/13/pure-storage-gets-new-cisco-flashstack-for-ai-certification-added-to-nvidia-basepod-validation/ (retrieved 2026-11-01)
- **Microsoft Azure**：Pure Storage Cloud Azure Native，一项联合开发的托管块存储服务（Sept 2025）；Azure 原生 VM 支持 GA（June 2026，[VERIFY]）；AVS 集成。**AWS**：由客户自行管理的 Cloud Dedicated（原 CBS），外加 EVS 集成。— 来源：Sources in §2
- **Meta**：自 December 2024 设计导入以来采用 DirectFlash 许可加供货模式；自 Q2 FY26 起批量部署；FY26 目标为 1–2 EB。**第二家前 5 大超大规模云厂商**（未具名）：August 2026。— 来源：Sources in §1
- **CoreWeave**：战略投资及首选存储供应商（Nov 2024）。Evercore 指出，投资者认为其重要性不及一家一线超大规模云厂商的订单。— 来源：TipRanks/The Fly, "Evercore says CoreWeave deal could yield sizable contributions for Pure Storage", 2024-11, https://www.tipranks.com/news/the-fly/evercore-says-coreweave-deal-could-yield-sizable-contributions-for-pure-storage (retrieved 2026-11-01)
- **Nutanix**：May 2025 宣布合作（FlashArray 通过 NVMe/TCP 作为 AHV 的外部存储，运行于 Cisco、Dell、HPE、Lenovo 和 Supermicro 服务器之上），瞄准 VMware 迁移需求。这是 Nutanix 首个重要的经认证外部存储集成。— 来源：SDxCentral, "Nutanix partners with Pure Storage in latest VMware assault", 2025-05, https://www.sdxcentral.com/news/nutanix-partners-with-pure-storage-in-latest-vmware-assault/ (retrieved 2026-11-01)
- **NAND 供应商**：Micron（G8 QLC 已通过 150 TB DFM 认证，G9 QLC 用于超大规模云厂商 DFM，2025 年扩大合作）和 Kioxia（长期合作；BiCS8 2 Tb QLC）。— 来源：Sources in §2
- **数据保护与安全**：Rubrik 和 CrowdStrike 集成是 EDC/Fusion 发布（June 2025）的一部分。[VERIFY: 本次未研究 Veeam、Commvault 和 Cohesity 的具体情况] — 来源：Blocks & Files, 2025-06-18 (above)
- **Red Hat / OpenShift**：Portworx OpenShift 插件 2.2 和 Portworx for Edge SKU 在 Red Hat Summit 2026 上发布。— 来源：Efficiently Connected, "Portworx at Red Hat Summit 2026", 2026-05, https://www.efficientlyconnected.com/portworx-edge-kubernetes-storage-red-hat-summit-2026/ (retrieved 2026-11-01)

---

## 6. 市场地位
- **Gartner MQ for Enterprise Storage Platforms 2025**（报告日期 Sept 2, 2025）：领导者（Leader），执行能力（Ability to Execute）最高，愿景完整性（Completeness of Vision）最远。Pure 称这是其连续第 12 年成为 Gartner MQ 领导者，此前在 Primary Storage MQ 中有五年愿景位置最远。— 来源：Pure Storage, "Pure Storage Named a Leader in the 2025 Gartner Magic Quadrant for Enterprise Storage Platforms", 2025-09, https://purestorage.com/company/newsroom/press-releases/pure-storage-named-leader-gartner-magic-quadrant-enterprise-storage-platforms.html (retrieved 2026-11-01)
- **Gartner MQ for Enterprise Storage Platforms 2026**（报告日期 Aug 19, 2026；Aug 21 公布）：Everpure 再次在两个维度上均位居最高。其他领导者为 Huawei、HPE、NetApp、IBM 和 Dell。Hitachi Vantara 是唯一的远见者（Visionary），IEIT Systems 是唯一的特定领域者（Niche Player）。[VERIFY: 不同新闻稿中此前领导者入选次数的说法不一（第 11 次或第 13 次）] — 来源：Everpure, "Everpure Named a Leader in the 2026 Gartner Magic Quadrant for Enterprise Storage Platforms", 2026-08-21, https://www.everpuredata.com/company/newsroom/press-releases/everpure-named-leader-2026-gmq-enterprise-storage-platforms.html (retrieved 2026-11-01); StorageReview, "Gartner MQ for Enterprise Storage 2026: Everpure tops both axes again as the six leaders hold", 2026-08, https://www.storagereview.com/news/gartner-magic-quadrant-for-enterprise-storage-2026-everpure-tops-both-axes-again-as-the-six-leaders-hold (retrieved 2026-11-01)
- Pure 还在 2025 Gartner MQ for Infrastructure Platform Consumption Services（Evergreen//One）中被评为领导者。— 来源：Nasdaq/PR Newswire, "Pure Storage Named a Leader in the 2025 Gartner Magic Quadrant for Infrastructure Platform Consumption Services", 2025, https://www.nasdaq.com/press-release/pure-storage-named-leader-2025-gartnerr-magic-quadranttm-infrastructure-platform (retrieved 2026-11-01)
- **IDC Worldwide Enterprise External Storage Systems tracker**（IDC 全球企业外部存储系统追踪报告）：
  - Q4 2025（日历年）：第 4 名，份额 **7.1%**，位列 Dell、Huawei 和 NetApp 之后。
  - Q2 2026：第 4 名，份额 **8.1%**，同比增长 +50.0%，为前五名中增长最快。全闪存系统为 $5.4B，占外部存储营收的 52.1%。
  - Q1 2026：Blocks & Files 列出的前五名为 Dell、NetApp、Everpure、Huawei、HPE。[VERIFY: 不同媒体对 Q1 排名的说法相互矛盾]
  - Everpure 还发布其自行"调整"（modified）的 IDC 份额数字，这些并非 IDC 的数字。
  - 来源：StorageReview, "IDC External Storage Tracker Q2 2026: $10.3 billion as server market tops $166 billion", 2026-09, https://www.storagereview.com/news/idc-external-storage-tracker-q2-2026-10-3-billion-as-server-market-tops-166-billion (retrieved 2026-11-01); IDC, "2Q2026 ESS Tracker" press release, 2026-09-10, https://www.idc.com/resource-center/press-releases/2q2026-ess-tracker/ (retrieved 2026-11-01); Blocks & Files, "IDC ranks Dell, NetApp, Everpure, Huawei and HPE in external storage systems market", 2026-06-16, https://www.blocksandfiles.com/flash/2026/06/16/idc-ranks-dell-netapp-everpure-huawei-and-hpe-in-external-storage-systems-market/5256070 (retrieved 2026-11-01); Blocks & Files, "Everpure says it's outpacing rivals in revenue, capacity growth", 2026-04-02, https://www.blocksandfiles.com/flash/2026/04/02/everpure-says-its-outpacing-rivals-in-revenue-capacity-growth/5213671 (retrieved 2026-11-01)
- 未找到 2025–2026 年全闪存阵列*厂商*份额的 IDC 数据。[VERIFY]
