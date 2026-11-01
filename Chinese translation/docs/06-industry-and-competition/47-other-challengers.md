# 47. 其他挑战者与软件定义厂商

> 📄 英文原文：[docs/06-industry-and-competition/47-other-challengers.md](../../../docs/06-industry-and-competition/47-other-challengers.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

> **深度：** L2 · **阅读时间：** 约 10 分钟 · **最后核实：** 2026-11-01
> **前置阅读：** [文件协议](../02-protocols-and-networking/08-file-protocols.md) · [对象存储与 S3](../02-protocols-and-networking/09-object-storage-and-s3.md) · [软件定义存储与 HCI](../03-system-architecture/19-software-defined-and-hci.md) · [传统厂商](46-incumbents.md)

## 要点速览（TL;DR）

- **最大的挑战者是超大规模云厂商自己的存储。** 仅 S3 就存有超过 500 万亿个对象；在云上产生的数据很少会拿出来招标。
- **在规模较小的厂商中，Hammerspace 最具战略意义。** 它的 pNFS 全局命名空间位于所有厂商阵列*之上*，而"Tier 0"把 GPU 服务器中闲置的 NVMe 变成共享存储。如果它胜出，阵列将变得可以相互替代。
- **开源对象存储在 2025–2026 年出现断裂。** MinIO 大幅削减其免费版本，并于 2026 年 4 月将代码仓库归档，迫使用户转向付费的 AIStor、Ceph、分叉版本或其他厂商提供支持的 S3。
- **软件定义厂商和平台厂商凭借控制权和成本取胜，而非峰值速度。** Ceph、Lightbits 和 Nutanix 适合希望自有硬件或迁出 VMware 的买家；Nutanix 同时也是 Everpure 的合作伙伴。
- **Qumulo、Cloudian、VDURA 和归属 Lenovo 的 Infinidat 是细分市场威胁。** 每一家都有可守住的基本盘，并在某一细分市场限制了 Everpure 的份额。

## 对 Everpure 战略的意义

VAST、WEKA 和 DDN（[第 42–45 章](45-head-to-head.md)）以及传统厂商（[第 46 章](46-incumbents.md)）吸引了大部分关注，但 Everpure（NYSE: P，原 PSTG）利润率所承受的压力，很大一部分来自它无法控制的层级。Hammerspace 和超大规模云厂商争夺的是阵列之上的*命名空间和控制平面*。Ceph、MinIO 和 Lightbits 提供的是*运行在通用服务器上的软件*，这压低了买家愿意为集成系统支付的价格上限。Nutanix 争夺的是 VMware 迁出预算所资助的*平台*。每一家都在检验 Everpure 的主张——集成硬件加 Purity 和 Evergreen 胜过自行拼装组件。其中大多数还是私营、规模不足或刚被收购的公司：它们可能成为收购标的、合作伙伴或渠道（[第 54 章](../07-history-and-future/54-strategic-option-map.md)）。

## 核心概念

### 按架构划分的版图

按它们所争夺的*层级*进行归类。

```mermaid
flowchart LR
    EP["Everpure FlashArray 与 FlashBlade"]
    subgraph NS["命名空间与文件层"]
        HS["Hammerspace：pNFS 全局命名空间"]
        QU["Qumulo：横向扩展 NAS、Azure Native"]
        VD["VDURA：PanFS 并行文件系统"]
    end
    subgraph OB["对象存储，软件定义"]
        MI["MinIO AIStor"]
        CL["Cloudian HyperStore"]
        CE["Ceph：IBM、Croit、Clyso、45Drives"]
    end
    subgraph BL["块存储"]
        LB["Lightbits：NVMe/TCP 软件"]
        IN["Infinidat，现属 Lenovo"]
    end
    subgraph PL["平台"]
        NU["Nutanix：AHV、NUS、NKP"]
    end
    subgraph HY["超大规模云原生"]
        AW["AWS：S3、EBS、FSx"]
        AZ["Azure：Blob、ANF、Managed Lustre"]
        GC["Google：GCS、Managed Lustre"]
    end
    HS -. "位于其上" .-> EP
    NU -. "合作伙伴兼对手" .-> EP
    HY == "替代" ==> EP
    OB -- "与 FlashBlade S3 竞争" --> EP
    BL -- "与 FlashArray 竞争" --> EP
    NS -- "与 FlashBlade 文件存储竞争" --> EP
```

*图 47.1 — 按所攻击层级归类的挑战者：Hammerspace 位于阵列之上，软件定义的对象存储和块存储在通用硬件上展开竞争，而超大规模云厂商则替代整个技术栈。*

### Hammerspace：覆盖所有厂商存储的命名空间

Hammerspace 将*文件出现在哪里*与*其字节存放在哪里*分离开来。元数据服务器（Anvil）持有一个全局命名空间。数据服务节点（DSX）以及现有的 NFS、对象或云存储负责存放字节[^1]。客户端运行标准的 Linux NFSv4.2 客户端，使用 pNFS **Flex Files** 布局：先从元数据服务器获取布局，再直接对存储节点执行 I/O（[第 8 章](../02-protocols-and-networking/08-file-protocols.md)）。策略（"objectives"，目标）可在层级和站点之间迁移处于打开状态的文件；改变的只是布局。

**半导体类比。** 这相当于文件的虚拟内存。命名空间是页表；迁移数据就像在应用保持地址不变的情况下，把一个页面从 DRAM 迁移到 CXL 内存。其护城河在于这个"MMU"位于 Linux 内核之中：CTO Trond Myklebust 是上游 Linux NFS 客户端的维护者[^2]。

**Tier 0。** Tier 0 于 2024 年 11 月推出，将 GPU 服务器内部的本地 NVMe 汇聚为同一命名空间中一个共享、受保护的层级[^3]。保护机制是跨可用区的客户端镜像；客户端纠删码仍在路线图上[^4]。5.2 版本新增了"affinitization"（亲和性放置），将客户端的数据写入其自身的本地 Tier 0 卷[^5]。

```mermaid
flowchart TB
    subgraph SITE["AI 集群，站点 A"]
        G1["GPU 服务器 1：本地 NVMe，Tier 0"]
        G2["GPU 服务器 2：本地 NVMe，Tier 0"]
        T1["现有 NAS 或闪存阵列，Tier 1"]
    end
    MD["Anvil 元数据：单一全局命名空间"]
    PO["策略目标：放置、保护、成本"]
    DX["DSX 数据迁移器"]
    OBJ["本地对象存储，Tier 2"]
    CLD["云区域或站点 B"]
    G1 -- "pNFS 布局请求" --> MD
    G1 == "直接数据 I/O" ==> G2
    G2 == "直接数据 I/O" ==> T1
    PO --> MD
    MD --> DX
    DX -- "在线迁移" --> T1
    DX -- "下沉分层" --> OBJ
    DX -- "复制" --> CLD
```

*图 47.2 — Hammerspace 将文件身份保存在单一元数据层中，并在 GPU 本地 NVMe、现有阵列、对象存储和云之间自由迁移字节，因此阵列只是多个层级中的一层。*

**算例（示意）。** 假设有 1,000 台 GPU 服务器，每台配备八块 3.84 TB NVMe 盘，这是常见的 DGX 级配置：1,000 × 8 × 3.84 TB ≈ **30.7 PB 原始容量**，而且已经付过钱，镜像后约为 15 PB。按每块 Gen4 盘约 6 GB/s 计算，本地聚合带宽为 1,000 × 8 × 6 ≈ **48 TB/s**，远超任何共享阵列。问题在于：重启会使盘离线，镜像流量与 GPU 网络共享带宽，而容量随服务器更新周期变动。因此 Tier 0 适合检查点和临时存储，之后再下沉到共享层级（[第 31 章](../05-ai-storage/31-training-storage.md)）。

**它为何有客户。** Meta 是旗舰客户。其两个各含 24,576 块 GPU 的 GenAI 集群，在使用 Tectonic 的同时，还使用了与 Hammerspace 共同开发的并行 NFS[^6]。2025 年 4 月，Hammerspace 完成由 Altimeter 领投的 US$100M B 轮融资，估值超过 US$500M（*媒体报道*），并谈及约两年内 IPO 的可能[^7]。薄弱之处：没有 NVIDIA SuperPOD 或 NVIDIA-Certified Storage 认证[^8]，且性能受制于底层存储。

### Qumulo 与 VDURA：改变了商业模式的文件存储专业厂商

**Qumulo** 销售横向扩展 NAS，具备实时容量与活动分析功能，在媒体、生命科学和科研领域颇受欢迎。在 CEO Doug Gourlay（自 2024 年 7 月起）领导下，它从自有硬件转向面向云、本地和边缘的软件[^9]。其独特资产是 **Azure Native Qumulo**，一项在 Azure 内部销售和计费的文件服务。2026 年 6 月，它新增了将传统 NAS 数据迁入该服务的工具[^10]。其最近一次定价融资是 2020 年 7 月以 US$1.2B 估值完成的 US$125M E 轮（*公司自述*）[^11] [VERIFY: Qumulo 自 2020 年以来的融资情况]。客户购买的是简便性和文件分析能力，而非峰值 GPU 吞吐量。

**VDURA** 即 Panasas，于 2024 年 5 月更名，定位为软件优先的公司[^12]。2025 年，它将 PanFS 重新推出为面向 AI/HPC 的平台，瞄准 VAST、WEKA 和 DDN，推出 V5000 全闪存设备，并自 2026 年 3 月起提供闪存加磁盘的混合选项[^13]。它声称拥有全球最大的国防 GPU 部署之一（*公司自述*）[^14]。在闪存昂贵的时期，它提供经实验室验证的 PanFS 和磁盘的成本优势；其风险在于规模 [VERIFY: VDURA 融资情况]。

### MinIO：自我封闭的开源对象存储

MinIO 是一个快速、免费的单一二进制程序，成为开发者、Kubernetes 和许多新兴 GPU 云的默认 S3 兼容存储。它于 2022 年 1 月以 US$1B 估值融资 US$103M，由 Intel Capital 领投[^15]。随后它分阶段撤回了社区版：

1. **2025 年 6 月：** 移除管理控制台，只保留基本的对象浏览器；管理功能转移到 CLI 或付费的 AIStor[^16]。
2. **2025 年末：** 官方二进制文件和镜像停止更新，据报道始于 2025 年 10 月；README 现称社区版仅以源代码形式发布。2025 年 12 月 3 日，项目进入维护模式，安全修复仅视具体情况提供[^17]。
3. **2026 年：** README 被修改为声明该仓库不再维护（据一位分叉版本维护者的说法，时间为 2 月 12 日[^19]）。GitHub 显示 `minio/minio` **于 2026 年 4 月 25 日归档**。AGPLv3 源代码仍可读取，README 指向 AIStor Free 和 AIStor Enterprise[^18]。

**半导体类比：** 这相当于一家授权方在生态系统已围绕其架构实现标准化之后修改授权条款。被授权方要么付费，要么分叉[^19]，要么迁移——此处是迁往 Ceph RGW 或商业 S3。

AIStor 本身是严肃的产品：它于 2024 年 11 月推出了基于 RDMA 的 S3[^20]，而且 MinIO 是 NVIDIA STX 合作伙伴[^21]。**算例：** 一家新兴 GPU 云以持续 100 GB/s 的速度从社区版 MinIO 迁出 50 PB 数据，需要 50 × 10¹⁵ ÷ 10¹¹ = 500,000 s ≈ **5.8 天**的满负荷复制。加上校验和切换，需要数周时间，因此许多用户会干脆向 MinIO 付费。

### Cloudian 与 Ceph：面向追求控制权用户的对象存储

**Cloudian HyperStore** 是 S3 原生的对象存储，以软件、一体化设备或通过 HPE GreenLake 销售，在受监管的本地部署买家中实力较强。2024 年 6 月，它从 Morgan Stanley Expansion Capital 获得 US$23M 成长融资，并称 ARR 增长 30%、实现盈亏平衡、累计融资约 US$256M（*公司自述*）[^22]。它较早实现了面向对象存储的 GPUDirect（2024 年 11 月声称超过 200 GB/s）[^23]。其 HyperScale AI Data Platform 增加了存储内向量搜索[^24]；HyperStore 8.2.6 于 2026 年 3 月获得 NVIDIA-Certified（Foundation 级）认证[^25]。

**Ceph** 是存储界的 Linux：一个同时提供块（RBD）、文件（CephFS）和对象（RGW）的开源系统，代码免费，但要运行好则代价高昂。Clyso 将一个 68 节点的 NVMe 集群调优至超过 1 TiB/s[^26]，既展示了上限，也展示了所需的技能。它的商业化有三种方式：

- **IBM Storage Ceph**，继承自 Red Hat，于 2026 年 1 月发布 9.0 版本[^27]。
- **软件与支持专业厂商**：Croit（管理软件与支持）[^28]和 Clyso（工程与咨询）[^26]。
- **硬件集成商**，例如 45Drives，其出货的服务器配有用于部署 Ceph 的 Houston 管理界面[^29]。

可以类比 RISC-V：ISA 是免费的；价值归于那些为电信运营商、大学、主权云和新兴 GPU 云把它做得可靠的公司。

### 块存储与平台：Lightbits、Infinidat、Nutanix

**Lightbits** 销售基于 NVMe/TCP 的软件定义块存储，而 NVMe/TCP 正是它参与创立的标准（[第 7 章](../02-protocols-and-networking/07-block-protocols.md)）。Crusoe 的 AI 云块存储服务以数 PB 的规模运行在其上[^30][^31]。最近一次披露的融资为 2022 年的 US$42M（累计 US$105.3M）[^32]。新兴 GPU 云用它来构建类似 EBS 的服务。

**Infinidat** 生产 InfiniBox，这是一款高端块存储阵列，在大型 HDD 或闪存池前端用 DRAM 响应大部分读请求。Lenovo 于 2025 年 1 月宣布收购，并于 2026 年 4 月完成交割；Infinidat 现为 Lenovo 基础设施解决方案集团（Infrastructure Solutions Group）旗下的一个部门[^33]。Calcalist 估计未披露的收购价超过 US$500M（*估算*）[^34]。收益在于 Lenovo 的分销能力。

**Nutanix** 销售的是平台：Nutanix Unified Storage（Files、Objects、Volumes），与 AHV 虚拟化管理程序以及 NKP 一起提供——NKP 是其基于收购 D2iQ（2024 年）构建的 Kubernetes 平台[^35]。Broadcom 对 VMware 许可的调整是顺风因素。Nutanix 报告称在 2026 财年第二季度新增超过 1,000 个新客户，为八年来最佳，其中大部分来自 VMware 迁出 [VERIFY: 仅见于搜索摘要][^36]；2026 财年 ARR 为 US$2.55B，增长 16%[^37]。AHV 如今也支持外部阵列：Dell PowerFlex、通过 NVMe/TCP 接入的 Pure Storage FlashArray（2025 年 5 月），随后是 NetApp ONTAP 和 Dell PowerStore[^38][^39]。NUS 也于 2026 年获得 NVIDIA 认证[^40]。

### 最大的挑战者：超大规模云原生存储

每家超大规模云厂商都提供完整的产品菜单：AWS 的 S3、EBS 和 FSx（Lustre、NetApp ONTAP、OpenZFS、Windows）；Azure 的 Blob、Azure NetApp Files 和 Azure Managed Lustre；Google 的 Cloud Storage 和 Managed Lustre。仅 S3 就存有超过 500 万亿个对象，在数百 EB 的数据上每秒处理超过 2 亿次请求[^41]。S3 Vectors（2025 年 12 月正式发布）表明它们正在向技术栈上层延伸[^42]。

类比是定制芯片：Graviton、Trainium 和 TPU 并没有在所有场景中击败商用芯片，但拿下了已经在云上的工作负载。当租用合作伙伴技术比自建更快时，云厂商也会将其作为第一方服务提供。Google Cloud Managed Lustre 运行在 DDN EXAScaler 上，于 2025 年 7 月正式发布[^43]；NetApp 的第一方及云市场（marketplace）云存储收入在 2026 财年第三季度增长 27%[^44]。它们还在 AI 性能上展开竞争：Azure Managed Lustre 是首个参加 MLPerf Storage 的超大规模云服务，在 v3.0 中检查点写入达到 642.2 GiB/s[^45]。据报道，Google 基于 DAOS 的 Parallelstore 正被逐步淘汰，由 Managed Lustre 取代 [VERIFY: 仅见于合作伙伴来源][^46]。
