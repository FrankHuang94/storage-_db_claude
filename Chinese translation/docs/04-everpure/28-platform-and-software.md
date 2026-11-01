# 28. 平台与软件

> 📄 英文原文：[docs/04-everpure/28-platform-and-software.md](../../../docs/04-everpure/28-platform-and-software.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

> **深度：** L2 · **阅读时间：** 约 10 分钟 · **最后核实：** 2026-11-01
> **前置阅读：** [控制平面与集群管理](../03-system-architecture/22-control-planes.md) · [消费模式](../03-system-architecture/23-consumption-models.md) · [Purity 与 DirectFlash](26-purity-and-directflash.md) · [FlashArray 与 FlashBlade](27-flasharray-and-flashblade.md)

## 要点速览（TL;DR）

- **一套软件栈，多种硬件。** Purity 运行在每一台阵列上；Fusion 和 Pure1 管理设备群；Portworx 和 Everpure Cloud 将其延伸到 Kubernetes 和公有云；Data Intelligence（原 1touch）则识别数据*是什么*。统称品牌：Enterprise Data Cloud（2025）、"Data Primacy"（2026）。
- **Evergreen 是让平台成立的商业模式。** 客户订阅的是一种架构；控制器和介质原地更新，无需迁移数据。Q2 FY27 订阅 ARR 达到 $2.13B（+20%）[^1]。
- **转换成本如今存在于控制平面。** Fusion 预设（preset）和自动化比任何一次硬件换代都更持久。截至 Q1 FY27，使用 Fusion 的客户超过 1,200 家，较上一季度翻倍[^2]，但仍不到客户总数的十分之一。
- **1touch（$125.0M，2026-05-07 完成交割）[^3] 押注的是：存储元数据加内容分类将成为一款治理与 AI 就绪（AI-readiness）产品。** 与 Portworx（约 $353M，2020）[^4] 相比规模较小，但它进入的是由数据目录和数据安全厂商主导的品类。
- **每家传统厂商都在讲同一个故事。** Dell、NetApp、HPE 和 VAST 都在销售"数据平台"；区别在于底层是什么（一套操作系统还是一个产品组合）、能否覆盖自家硬件之外，以及客户是否购买上层软件。

## 对 Everpure 战略的意义

硬件利润率随 NAND 周期起伏；随着零部件成本飙升，Everpure 于 2026 年 2 月提价（[第 29 章](29-hyperscaler-ecosystem-financials.md)）。Q2 FY27 订阅毛利率为 74.9%，产品毛利率为 66.2%（均为非 GAAP）[^5]。平台的目标是通过附加销售（attach）和扩展让收入实现复利增长。FY26 订阅净美元留存率为 113%[^6]，即某个客户群第一年支付 $100，第二年支付 $113。

风险在于：如果 Fusion、Portworx 和 Data Intelligence 主要是随阵列交易一起出货，而不是赢得独立预算，那么"数据管理公司"只不过是在存储业务损益表上换了块招牌。基于公开信息，战略团队可能评估的选项都取决于这一区别。

## 核心概念

### 逐层拆解软件栈

```mermaid
flowchart TB
    DI["数据智能：Everpure Data Intelligence、Data Stream"]
    PX["Portworx：Kubernetes 数据服务"]
    CL["Everpure Cloud：Dedicated、Azure Native"]
    CP["控制平面：Fusion 策略 + Pure1 遥测与 AIOps"]
    AR["阵列：FlashArray、FlashBlade、FlashBlade EXA"]
    OS["Purity 操作系统"]
    MD["介质：基于裸 NAND 的 DirectFlash 模块"]
    EV["Evergreen 订阅覆盖每一层"]
    DI --> CP
    PX --> CP
    CL --> CP
    CP --> AR
    AR --> OS
    OS --> MD
    EV -.-> CP
    EV -.-> AR
```

*图 28.1 — 每台阵列一套操作系统，所有阵列之上一个控制平面；最新的几层（Portworx、云、数据智能）接入的是这个控制平面，而不是单台设备。*

底部三层分别见[第 26 章](26-purity-and-directflash.md)、[第 27 章](27-flasharray-and-flashblade.md)和[第 22 章](../03-system-architecture/22-control-planes.md)。上面各层不需要 Everpure 硬件：**Portworx** 可在任何环境中服务 Kubernetes，**Everpure Cloud** 在 AWS 和 Azure 中运行 Purity，**Data Intelligence** 则对任何位置的数据进行分类。

**半导体类比：** 这就像 Synopsys 和 Cadence 从单点工具走向完整流程（flow）。仿真器很容易替换；而一套积累了多年脚本和已验证配方的签核（sign-off）流程则不然。Fusion 预设和自动化就是 Everpure 的"流程"，阵列则是工具。

命名几经变化，表述务必准确。**Enterprise Data Cloud**（2025 年 6 月）是一个以 Fusion 为核心、统一本地与云端的控制平面[^7]；CEO 将 2026 年 2 月启用的 Everpure 新名称与它及 Evergreen 联系在一起[^8]。法律顾问文件和监管申报现在使用"Everpure Platform"[^9]。在 Accelerate 2026 上，定位变成了 **Data Primacy**——以可信数据而非应用为中心[^10]，支柱包括数据管理、统一数据平面和智能控制平面[^11]。"Pure Storage Cloud"现已更名为 **Everpure Cloud**[^12]。

### Evergreen：订阅一种架构

Evergreen 始于 2015 年；在 2022 年的重组中，Evergreen Gold 更名为 Evergreen//Forever[^13]，并形成了如今的三个层级[^14]。

| 层级 | 硬件归属 | 付费内容 | 更新机制 | 主要保障（公司自述） |
|---|---|---|---|---|
| Evergreen//Forever | 客户 | 购买阵列加经常性订阅 | 控制器更新与三年续约挂钩，受计划条款约束[^15][^16] | 不停机升级；已拥有的容量无需重复购买 |
| Evergreen//Flex | 客户 | 实际使用的容量，可在设备群层面汇集 | 与 //Forever 相同；容量可在设备群内调配 | 在自有阵列上按用量付费[^15] |
| Evergreen//One | Everpure | 按已用容量单位计价的性能层级，设有最低承诺量 | 由 Everpure 负责，客户无感知 | 最多十项 SLA，包括 99.9999% 可用性、25% 容量缓冲、能效、零计划停机和零数据丢失[^17][^18] |

*表 28.1 — 三个 Evergreen 层级逐步把风险从客户（拥有并规划）转移到 Everpure（拥有、规划并提供保障）。*

其前提是架构层面的。在 Purity 双控制器阵列中，持久状态（数据、元数据、写日志）位于机箱内的闪存模块和 NVRAM 上，而不在控制器中（[第 14 章](../03-system-architecture/14-scale-up-dual-controller.md)）。因此控制器可以逐个更换，期间由另一台控制器继续服务 I/O；介质的更换则通过加入新模块并迁出旧模块完成。

```mermaid
flowchart LR
    S["签订订阅：Forever、Flex 或 One"] --> T["Pure1 遥测：容量、负载、健康状况"]
    T --> F["预测：容量填满日期、性能余量"]
    F --> D{"触发条件"}
    D -->|"续约或 SLA 违约风险"| C["发运新控制器"]
    D -->|"容量或密度需求"| M["发运新 DirectFlash 模块"]
    C --> N["逐个更换控制器，I/O 不中断"]
    M --> E["加入新模块，迁出并退役旧模块"]
    N --> R["同一阵列、同一数据、更新的硬件"]
    E --> R
    R --> T
```

*图 28.2 — Evergreen 循环：遥测告诉 Everpure 何时发运硬件，架构则让这些硬件无需数据迁移即可上线——这正是订阅得以续约的原因。*

截至 2021 年 7 月，Pure Storage 称自 2015 年以来已为超过 2,700 家客户完成超过 7,000 次不停机控制器升级（公司自述）[^19]。Evergreen//One 的 SLA 之所以能够承保，完全是因为 Pure1 监控着每一台阵列；缓冲容量依据 Pure1 工作负载规划器（workload planner）中的历史增长确定[^17]。**Overdrive** 宣布于 2026 年第三季度（Q3 2026）推出，允许突发用量最多超出订阅水平 25%[^20] [VERIFY: Overdrive 条款仅见于二手摘要]。

**算例（示意）。** 某客户在 Evergreen//One 下使用 800 TiB。按 25% 缓冲，Everpure 需在客户现场、在其自有硬件上保持至少 1,000 TiB 有效容量；如果数据缩减效果不及预期，Everpure 自费追加闪存。厂商承担了原本由资本支出型买家承担的利用率和数据缩减风险，这些风险已计入每 TiB 价格，且只有在遥测保证预测准确时才能盈利。现金流方面见[第 23 章](../03-system-architecture/23-consumption-models.md)。

Evergreen//One 订单（bookings）增长情况见[第 29 章](29-hyperscaler-ecosystem-financials.md)。

### Fusion 与 Pure1：控制平面即产品

```mermaid
flowchart TB
    U["管理员、Terraform、Ansible、通过 MCP 接入的 AI 智能体"] --> API["Fusion API 与 Pure1 Manage MCP"]
    API --> PS["预设：QoS、保护、标签、合规"]
    PS --> PL["放置引擎选择有余量的阵列"]
    PL --> A1["FlashArray 设备群"]
    PL --> A2["FlashBlade 设备群"]
    PL --> A3["Everpure Cloud Dedicated"]
    A1 --> P1["Pure1 遥测与 AIOps"]
    A2 --> P1
    A3 --> P1
    P1 -->|"预测、漂移告警、问题分诊"| PL
```

*图 28.3 — 用户和智能体通过同一个 API 提出期望结果；预设编码策略，Pure1 遥测为放置决策提供依据，其后的阵列则成为可互换的容量。*

自 2024 年起，Fusion 已内嵌于 Purity，无需单独部署[^21]。其核心对象是**预设（preset）**——一个覆盖整个设备群的模板，包含性能上限、快照与复制策略以及标签[^22]，与 Kubernetes 的存储类（storage class）十分相似。Pure1 提供预测、工作负载规划和预测性支持。2026 年，两者都可以被智能体调用：Everpure 提供 **Pure1 Manage MCP 服务器**和 **Fusion MCP 服务器**，使 AI 工具能够查询设备群状态并执行受监督的操作[^23]。Fusion Compliance 与 Agentic Triage（配置漂移检测，并给出 AI 根因建议），以及 Workload Rebalance and Mobility，原定于 2026 年第四季度（Q4 2026）推出[^24] [VERIFY: GA 状态]。

关注采用率：超过 1,200 家 Fusion 客户，相对约 14,500–15,000 家客户总数 [VERIFY: 存在两个不同的客户总数数据]，约为 8%；控制平面锁定效应只对这部分客户真正成立。

### Portworx：先服务 Kubernetes，再服务虚拟机

Portworx（2020 年 10 月收购[^4]）把 Kubernetes 集群下的任何磁盘或云卷汇集成池，为容器提供持久卷、复制、快照、备份和灾备（DR），可运行在任何硬件或云上，也可直接运行在 FlashArray 上。Everpure 将 Portworx 的定期许可（term licence）计入产品收入，其他产品计入订阅服务收入[^3]，因此没有公开的 Portworx 独立收入数据。

Portworx 的"第二幕"源自 Broadcom：其 2023 年后的 VMware 许可变更推高了许多续约账单[^25]，促使企业评估 **KubeVirt**——它把虚拟机作为 Kubernetes 对象运行（通常通过 OpenShift Virtualization）。Portworx Enterprise 3.6（2026 年 3 月）新增了经过验证的 KubeVirt 框架和一个虚拟机就绪评估工具；客户在其上运行的虚拟机卷超过 100,000 个（公司自述）[^26]。Everpure 自身的 IT 部门已将超过 5,000 台虚拟机迁移到运行于 Portworx 之上的 KubeVirt（公司自述）[^27]。随后在 Red Hat Summit 2026 上又推出了 OpenShift 插件和 Edge SKU[^28]。

Everpure 对 VMware 迁出采取两头下注：面向 Kubernetes 的 Portworx，以及 2025 年 5 月与 Nutanix 的合作（FlashArray 作为 AHV 的外部存储）以覆盖另一种虚拟化平台[^29]。无论哪种方式，阵列都可以继续是 Everpure 的。

### Everpure Cloud

**Everpure Cloud Dedicated**（原 Cloud Block Store）是在客户自己的 AWS 或 Azure 账户中由客户管理的 Purity，其复制和快照功能与本地阵列一致[^12]。**Everpure Cloud Azure Native** 与 Microsoft 联合开发，于 2025 年 9 月推出[^30]，是一项完全托管的 Azure Native ISV 服务，首先面向 Azure VMware Solution[^31]，自 2026 年 6 月起支持 Azure VM 并已 GA[^20] [VERIFY: Azure VM 的 GA 日期]。其作用主要是防御性的：迁往云端的工作负载可以继续留在 Fusion 和 Evergreen 式计费之下，而不是转用原生的 EBS 或 Azure Disk。与 NetApp 在三大超大规模云厂商中均提供的第一方 ONTAP 服务相比，Everpure 的覆盖面更窄（[第 46 章](../06-industry-and-competition/46-incumbents.md)）。

### 1touch 与数据智能论点

```mermaid
flowchart LR
    SM["存储元数据：卷、文件、对象、所有者、快照、访问记录"] --> KG["数据知识图谱"]
    CC["内容分类：实体、PII、PHI、业务含义"] --> KG
    EX["其他数据资产：数据库、SaaS、公有云、第三方存储"] --> CC
    KG --> GV["治理：数据驻留、基于属性的访问控制、血缘"]
    KG --> CY["网络安全：哪些数据被暴露，优先恢复关键数据"]
    KG --> AI["AI 就绪：Data Stream 经 MCP 摄取、索引、向量化"]
```

*图 28.4 — 核心论点：存储层已经知道每个字节在哪里、谁访问过它；再加上对这些字节含义的理解，就能从同一张图谱出发销售治理、网络恢复和 AI 就绪数据。*

1touch 于 2026-05-07 完成交割，$125.0M 对价可能因调整和托管（escrow）安排而变化[^3]。作为 **Everpure Data Intelligence**（2026 年 6 月 GA）[^10]，它发现结构化和非结构化数据，在实体级别对其分类（标记 PII 和 PHI）并纳入语义知识图谱，追踪数据血缘，并执行基于属性的访问控制和数据驻留策略[^32]。分析师还称它可覆盖数据库、SaaS 和第三方存储，而不仅限于 Everpure 阵列[^11]。原生 MCP 支持（2026 年 9 月）使智能体可以查询它[^33]。**Data Stream** 运行在配备 NVIDIA GPU 的 FlashBlade 上，基于 NVIDIA 的 AI Data Platform 参考设计，对这些数据进行摄取、索引和向量化，用于 RAG 和推理[^34]（[第 39 章](../05-ai-storage/39-agentic-ai-and-data-intelligence.md)、[第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md)）。

为什么是存储公司来做？阵列已经掌握了**清单**（每一个卷、文件、对象、快照和访问记录），并且位于**写路径**上，因此可以在数据落盘时触发分类，而不必像存储之上的数据目录那样依赖每周一次的爬取。**半导体类比：** 片上遥测能看到每一笔事务，而外部测试设备只能抽样。

### "存储厂商 → 数据平台"在商业上应如何运作

该模式有三个杠杆：

1. **附加销售（attach）。** 每一层都可以卖给约 15,000 家已经信任该厂商并在使用 Pure1 的客户。*示意：* 若 15,000 家客户中有 5% 按假设的 $150k ARR 附加购买 Data Intelligence，即 750 × $150k ≈ $113M ARR，约为 $2.13B 基数之上再增加 5%。这大致相当于用一年的收入收回 $125M 的收购价。
2. **ARR 质量。** 软件可以提升订阅占比、利润率和净留存率，而不仅仅依赖容量增长。
3. **转换成本。** 转换成本从设备本身（Evergreen 让其易于更新）转移到策略、自动化和知识图谱上，而这些在别处重建的成本很高。

**可能行不通的地方。** 第一，赛道拥挤：数据目录和湖仓（lakehouse）治理（Databricks Unity Catalog、Snowflake 的治理功能、Microsoft Purview）主导着分析场景中"这是什么数据"的问题，而数据安全厂商（BigID、Varonis、Cyera）则把数据发现卖给 CISO——这是另一类买家。第二，中立性尚未得到证明。一位分析师表示，在 Everpure 硬件之外的应用场景"是个更大的问号"（a bigger question mark），并指出 Everpure 未参与 Open Semantic Interchange 元数据计划[^11] [VERIFY: 仅见于搜索摘要]。第三，存储销售人员按阵列拿提成；覆盖竞争对手存储的软件需要单独的激励机制。Futurum 提出的待解问题是：客户会以多快的速度跟进[^32]。

## Everpure 的做法与竞争对手对比

| 厂商 | 平台定位（2025–26） | 底层是什么 | 数据智能 / AI 层 | 消费模式 | 最强版本论证（steelman） | 薄弱环节 |
|---|---|---|---|---|---|---|
| Everpure | Enterprise Data Cloud → Data Primacy[^7][^10] | 一套操作系统（Purity）覆盖所有阵列和云 | Data Intelligence（原 1touch）、Data Stream[^34] | Evergreen //Forever、//Flex、//One | 最简单的单一操作系统软件栈；成熟的不停机更新 | 云覆盖面窄；DI 在非 Everpure 设备上尚未得到验证；软件主要随阵列销售 |
| Dell | 与 NVIDIA 合作的 AI Data Platform[^35] | 多套操作系统：PowerScale、Lightning FS、ObjectScale、PowerStore、PowerMax | AI Data Platform 内的数据编排 | APEX[^36] | 一张采购订单即可购买服务器、网络和存储 | 产品组合庞杂；控制平面统一程度较低 |
| NetApp | 智能数据基础设施；AFX + AI Data Engine[^37] | ONTAP 本地部署，并在三大超大规模云厂商中作为第一方服务提供 | AI Data Engine（基于 NVIDIA AI Data Platform 的 ONTAP 扩展） | Keystone[^36] | 混合云覆盖最深；长期的数据管理积淀 | AFX/AIDE 较新；ONTAP 复杂 |
| HPE | 搭载 GreenLake Intelligence 的 GreenLake 云[^38] | Alletra MP（块、文件、对象）、Zerto、Data Fabric[^39] | X10000 上的内联元数据增强；智能体式运维 | GreenLake[^36] | 在一个云控制台下提供全栈（计算、经由 Juniper 的网络） | 存储只占 HPE 的一小部分；产品众多 |
| VAST | AI Operating System[^40] | 运行在合作伙伴硬件上的一套软件栈（DASE） | 平台内置 DataBase、DataEngine、InsightEngine、AgentEngine、PolicyEngine | 软件订阅 | 集成度最高：数据库和计算都位于存储层 | 要求客户连分析工具也一并替换；作为私营公司信息披露有限 |

*表 28.2 — 五家厂商都自称数据平台；Everpure 的独特主张是一套操作系统加不停机订阅，而 VAST 在软件栈上走得最高，NetApp 在跨云方面走得最远。*

Dell 和 HPE 把多套操作系统缝合在一个控制台之下；NetApp 只有一套操作系统，但其更新订阅不够简洁；VAST 把数据库和函数放进存储内部（[第 42 章](../06-industry-and-competition/42-vast-data.md)），而 Everpure 止步于此之前。最强的竞争对手论证来自 NetApp：它在三大超大规模云厂商中均有第一方 ONTAP 服务，而 Everpure 只有一项原生服务加一个由客户管理的虚拟阵列。

## 历史与发展轨迹

```mermaid
timeline
    title 从 Pure Storage 到 Everpure 的平台里程碑
    2012 : FlashArray 与 All Software Included 授权模式
    2015 : 推出 Evergreen Gold 订阅
    2017 : Pure1 META 遥测分析
    2019 : Pure-as-a-Service，后更名为 Evergreen One
    2020 : 收购 Portworx
    2022 : Evergreen Forever、Flex 与 One 产品家族
    2024 : Fusion 内嵌于 Purity，Pure1 AI Copilot
    2025 : Enterprise Data Cloud，Azure Native 云服务
    2026 : 更名 Everpure，完成 1touch 交割，Data Intelligence GA，MCP 服务器
```

*图 28.5 — 每一步都把价值从硬件推向订阅和软件，但 2026 年数据层这一步是第一次覆盖到 Everpure 自有设备之外。*

时间线来源：All Software Included[^41]、Pure1 META[^42]、Evergreen//One[^14]、AI copilot[^43]。Portworx 是第一款不需要 Pure 硬件的产品。未来 12–18 个月的信号：Fusion 采用率能否继续翻倍；Data Intelligence 是否单独定价、单独披露，并赢得非 Everpure 数据资产；以及 Everpure 是否加入元数据互操作计划。
