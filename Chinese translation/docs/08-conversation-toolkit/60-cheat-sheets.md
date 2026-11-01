# 60. 速查表

> 📄 英文原文：[docs/08-conversation-toolkit/60-cheat-sheets.md](../../../docs/08-conversation-toolkit/60-cheat-sheets.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

> **深度：** L1 · **阅读时间：** 约 5 分钟 · **最后核实：** 2026-11-01
> **前置阅读：** [块存储协议](../02-protocols-and-networking/07-block-protocols.md) · [文件协议](../02-protocols-and-networking/08-file-protocols.md) · [对象存储与 S3](../02-protocols-and-networking/09-object-storage-and-s3.md) · [架构决策矩阵](../03-system-architecture/24-architecture-decision-matrix.md) · [FlashArray 与 FlashBlade](../04-everpure/27-flasharray-and-flashblade.md) · [平台与软件](../04-everpure/28-platform-and-software.md) · [术语表](../glossary.md)

## 要点速览（TL;DR）

- **四份一页纸参考资料，全部基于本图谱已注明来源的事实**：一份含 104 个条目的缩略语表，以及三张海报（协议、架构、Everpure 产品），每张海报都配有一张便于无障碍阅读的表格。
- **协议按主机看到的对象分类**：一块磁盘、一棵目录树，或一个装满键的桶。传输层决定延迟代价：相对本地 NVMe，NVMe over RDMA 约增加 5–15 µs，NVMe/TCP 约增加 20–35 µs[^1][^2]。
- **六种架构几乎覆盖所有交易，每种都有一堵墙**：控制器、东西向流量、网络架构（fabric）、元数据、小对象，或耦合扩展。
- **除 DASE 外，Everpure 在每一种架构上都有产品。** FlashBlade//S 是分区式横向扩展；FlashBlade//EXA 是 pNFS 元数据/数据分离架构。
- **产品线是一个堆栈**：DirectFlash、Purity、两大阵列产品族、Fusion 与 Pure1、Portworx 与 Everpure Cloud、Data Intelligence，全部包裹在 Evergreen 之中。

## 对 Everpure 战略的意义

与产品经理和 CTO 办公室的会议靠速记式术语推进。把 FlashBlade//S 说成"全共享（shared-everything）"，或把 NVMe/TCP 与 NVMe/RoCE 混为一谈，一句话就会损失信誉（[第 56 章](56-talking-with-engineering-and-cto.md)）。产品名称也变化很快：Cloud Block Store 更名为 Everpure Cloud Dedicated，1touch 更名为 Everpure Data Intelligence[^3][^4]。这里的每个单元格都可追溯到一个注明来源的章节。如果海报与章节不一致，以章节为准。

## 核心概念

### 如何使用这些速查表

在会议开始前两分钟使用。脚注引用原始来源；链接的章节给出推理过程。

### 速查表 1：缩略语，A–Z

两个陷阱：RPO 对工程师而言是*恢复点目标（recovery point objective）*，对 CFO 而言却是*剩余履约义务（remaining performance obligations）*；KV cache 中的"KV"指注意力机制的键（key）和值（value），而不是键值数据库。

| 缩略语 | 英文全称（中文名称） | 一句话释义 | 章节 |
|---|---|---|---|
| **AFR** | Annualized failure rate（年化故障率） | 每年预计发生故障的设备比例 | [第 20 章](../03-system-architecture/20-distributed-systems-fundamentals.md) |
| **AIOps** | AI for IT operations（智能运维） | 基于遥测数据的机器学习，用于预测故障并给出修复建议 | [第 22 章](../03-system-architecture/22-control-planes.md) |
| **ALUA** | Asymmetric Logical Unit Access（非对称逻辑单元访问） | 阵列告知主机哪些路径为优化路径的 SCSI 方法 | [第 14 章](../03-system-architecture/14-scale-up-dual-controller.md) |
| **ANA** | Asymmetric Namespace Access（非对称命名空间访问） | NVMe 中与 ALUA 对应的多路径机制 | [第 7 章](../02-protocols-and-networking/07-block-protocols.md) |
| **ANN** | Approximate nearest neighbour（近似最近邻） | 牺牲少量召回率以换取大幅提速的向量搜索 | [第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md) |
| **ARR** | Annual recurring revenue（年度经常性收入） | 按年化计算的订阅收入运行率；Everpure 披露订阅 ARR | [第 29 章](../04-everpure/29-hyperscaler-ecosystem-financials.md) |
| **CMX** | Context memory storage（上下文内存存储） | NVIDIA 基于 BlueField-4、面向 KV 缓存的以太网闪存层级 | [第 32 章](../05-ai-storage/32-inference-and-kv-cache.md) |
| **COW** | Copy-on-write（写时复制） | 在覆盖旧数据块之前先将其复制到别处的快照方法 | [第 6 章](../01-storage-fundamentals/06-data-protection-and-resilience.md) |
| **CRUSH** | Controlled Replication Under Scalable Hashing（可扩展哈希下的受控复制） | Ceph 通过计算（而非查表）确定数据放置位置 | [第 15 章](../03-system-architecture/15-scale-out-shared-nothing.md) |
| **CSI** | Container Storage Interface（容器存储接口） | Kubernetes 用来申请存储卷的插件标准 | [第 22 章](../03-system-architecture/22-control-planes.md) |
| **CXL** | Compute Express Link（计算快速链路） | 运行在 PCIe 物理层上的一致性内存与 I/O 协议 | [第 12 章](../02-protocols-and-networking/12-interfaces-and-emerging-tech.md) |
| **DAS** | Direct-attached storage（直连存储） | 装在一台服务器内部或通过线缆直连该服务器的硬盘 | [第 13 章](../03-system-architecture/13-storage-stack.md) |
| **DASE** | Disaggregated shared-everything（分解式全共享架构） | 无状态计算节点通过 NVMe-oF 共享全部介质 | [第 16 章](../03-system-architecture/16-disaggregated-shared-everything.md) |
| **DFM** | DirectFlash Module（DirectFlash 模块） | Everpure 的裸 NAND 模块，没有盘级 FTL | [第 26 章](../04-everpure/26-purity-and-directflash.md) |
| **DFMD** | DirectFlash Module with NVRAM（带 NVRAM 的 DirectFlash 模块） | 自带 NVRAM 的 DFM，使写日志容量随模块数量增长 | [第 14 章](../03-system-architecture/14-scale-up-dual-controller.md) |
| **DLIO** | Deep Learning I/O (benchmark)（深度学习 I/O 基准） | MLPerf Storage 用来模拟训练数据加载的仿真工具 | [第 37 章](../05-ai-storage/37-reading-benchmarks.md) |
| **DPDK** | Data Plane Development Kit（数据平面开发套件） | 绕过内核、直接驱动网卡的用户态库 | [第 43 章](../06-industry-and-competition/43-weka.md) |
| **DPU** | Data processing unit（数据处理器） | 自带 CPU 核和加速器的网卡 | [第 10 章](../02-protocols-and-networking/10-datacenter-networking.md) |
| **DRR** | Data-reduction ratio（数据缩减率） | 逻辑数据量 ÷ 去重和压缩后的物理容量 | [第 5 章](../01-storage-fundamentals/05-data-reduction.md) |
| **DSPM** | Data security posture management（数据安全态势管理） | 发现敏感数据及其暴露情况的工具 | [第 39 章](../05-ai-storage/39-agentic-ai-and-data-intelligence.md) |
| **DWPD** | Drive writes per day（每日全盘写入次数） | SSD 耐久度指标：质保期内每天可写满全盘容量的次数 | [第 2 章](../01-storage-fundamentals/02-media-physics.md) |
| **EC** | Erasure coding（纠删码） | k 个数据条带 + m 个校验条带；任意 k 个即可重建 | [第 6 章](../01-storage-fundamentals/06-data-protection-and-resilience.md) |
| **ECN** | Explicit Congestion Notification（显式拥塞通知） | 交换机标记数据包，让发送方在丢包前降速 | [第 10 章](../02-protocols-and-networking/10-datacenter-networking.md) |
| **EDSFF** | Enterprise and Data Center Standard Form Factor（企业与数据中心标准外形规格） | 为密度和散热气流设计的 E1/E3 SSD 外形 | [第 12 章](../02-protocols-and-networking/12-interfaces-and-emerging-tech.md) |
| **FC** | Fibre Channel（光纤通道） | 专用、无损的企业级 SAN 网络 | [第 7 章](../02-protocols-and-networking/07-block-protocols.md) |
| **FC-NVMe** | NVMe over Fibre Channel（基于光纤通道的 NVMe） | 运行在现有 FC HBA 和交换机上的 NVMe-oF | [第 7 章](../02-protocols-and-networking/07-block-protocols.md) |
| **FDP** | Flexible Data Placement（灵活数据放置） | 将生命周期相近的数据归组的 NVMe 提示机制 | [第 12 章](../02-protocols-and-networking/12-interfaces-and-emerging-tech.md) |
| **FTL** | Flash translation layer（闪存转换层） | 将逻辑块映射到 NAND 页；屏蔽"先擦后写" | [第 3 章](../01-storage-fundamentals/03-inside-an-ssd.md) |
| **GC** | Garbage collection（垃圾回收） | 把有效页从块中复制出去，使该块可被擦除 | [第 3 章](../01-storage-fundamentals/03-inside-an-ssd.md) |
| **GDS** | GPUDirect Storage | 存储或网卡与 GPU 内存之间的 DMA，无需经 CPU 中转 | [第 11 章](../02-protocols-and-networking/11-gpu-data-path.md) |
| **GPFS** | General Parallel File System（通用并行文件系统） | IBM 的并行文件系统，现名 IBM Storage Scale | [第 17 章](../03-system-architecture/17-parallel-file-systems.md) |
| **HAMR** | Heat-assisted magnetic recording（热辅助磁记录） | 用激光加热辅助 HDD 写入，以提高面密度 | [第 2 章](../01-storage-fundamentals/02-media-physics.md) |
| **HBA** | Host bus adapter（主机总线适配器） | 连接 FC 或 SAS 存储网络的服务器板卡 | [第 7 章](../02-protocols-and-networking/07-block-protocols.md) |
| **HBM** | High-bandwidth memory（高带宽内存） | 封装在 GPU 上的堆叠 DRAM；内存层级的顶端 | [第 2 章](../01-storage-fundamentals/02-media-physics.md) |
| **HCI** | Hyperconverged infrastructure（超融合基础设施） | 每个节点同时运行虚拟机、存储软件并使用本地硬盘 | [第 19 章](../03-system-architecture/19-software-defined-and-hci.md) |
| **HDD** | Hard disk drive（机械硬盘） | 旋转式磁介质；在线存储中每 TB 成本最低 | [第 2 章](../01-storage-fundamentals/02-media-physics.md) |
| **HNSW** | Hierarchical Navigable Small World（分层可导航小世界图） | 基于图的向量索引，在 DRAM 中速度很快 | [第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md) |
| **IOPS** | I/O operations per second（每秒 I/O 操作数） | 请求速率；不说明 I/O 大小和延迟就毫无意义 | [第 4 章](../01-storage-fundamentals/04-performance-and-economics-metrics.md) |
| **iSCSI** | Internet SCSI（互联网 SCSI） | 在普通以太网上通过 TCP/IP 传输 SCSI 命令 | [第 7 章](../02-protocols-and-networking/07-block-protocols.md) |
| **KV cache** | Key-value cache (attention)（注意力键值缓存） | 存储注意力机制的键和值，从而无需重新计算 token | [第 32 章](../05-ai-storage/32-inference-and-kv-cache.md) |
| **LBA** | Logical block address（逻辑块地址） | 卷中某个固定大小数据块的编号 | [第 1 章](../01-storage-fundamentals/01-what-storage-does.md) |
| **LDPC** | Low-density parity-check (code)（低密度奇偶校验码） | SSD 控制器在 NAND 上使用的纠错码 | [第 3 章](../01-storage-fundamentals/03-inside-an-ssd.md) |
| **LTO** | Linear Tape-Open（线性磁带开放协议） | 占主导地位的开放式磁带标准 | [第 2 章](../01-storage-fundamentals/02-media-physics.md) |
| **LUN** | Logical unit number（逻辑单元号） | 块存储卷的 SCSI 地址 | [第 7 章](../02-protocols-and-networking/07-block-protocols.md) |
| **MCP** | Model Context Protocol（模型上下文协议） | 连接 AI 智能体与工具和数据的开放协议 | [第 22 章](../03-system-architecture/22-control-planes.md) |
| **MDS** | Metadata server（元数据服务器） | 并行文件系统中负责命名空间、布局和锁的服务器 | [第 17 章](../03-system-architecture/17-parallel-file-systems.md) |
| **MDT** | Metadata target（元数据目标） | 存放目录、inode 和布局的 Lustre 卷 | [第 17 章](../03-system-architecture/17-parallel-file-systems.md) |
| **MFU** | Model FLOPs utilization（模型算力利用率） | 训练作业实际用到的 GPU 峰值算力比例 | [第 31 章](../05-ai-storage/31-training-storage.md) |
| **MLC** | Multi-level cell（多层单元） | 每单元存储 2 bit 的 NAND | [第 2 章](../01-storage-fundamentals/02-media-physics.md) |
| **MPIO** | Multipath I/O（多路径 I/O） | 在多条路径间分配 I/O 并支持故障切换的主机软件 | [第 14 章](../03-system-architecture/14-scale-up-dual-controller.md) |
| **MTTDL** | Mean time to data loss（平均数据丢失时间） | 建模得出的、重叠故障导致数据丢失之前的时间 | [第 20 章](../03-system-architecture/20-distributed-systems-fundamentals.md) |
| **NAS** | Network-attached storage（网络附加存储） | 拥有文件系统并提供 NFS/SMB 服务的系统 | [第 13 章](../03-system-architecture/13-storage-stack.md) |
| **NCCL** | NVIDIA Collective Communications Library（NVIDIA 集合通信库） | GPU 之间的集合通信，例如 all-reduce | [第 11 章](../02-protocols-and-networking/11-gpu-data-path.md) |
| **NCP** | NVIDIA Cloud Partner（NVIDIA 云合作伙伴） | NVIDIA 的 GPU 云计划，设有存储认证层级 | [第 35 章](../05-ai-storage/35-ai-factories-and-neoclouds.md) |
| **NDR** | Net dollar retention（净收入留存率） | 去年客户群今年贡献的收入 ÷ 其去年收入 | [第 28 章](../04-everpure/28-platform-and-software.md) |
| **NDU** | Non-disruptive upgrade（不停机升级） | 在 I/O 持续运行时更换控制器、软件或介质 | [第 14 章](../03-system-architecture/14-scale-up-dual-controller.md) |
| **NFS** | Network File System（网络文件系统） | Linux/Unix 文件共享协议 | [第 8 章](../02-protocols-and-networking/08-file-protocols.md) |
| **NIXL** | NVIDIA Inference Xfer Library（NVIDIA 推理传输库） | 在 GPU、主机和存储之间搬运 KV 缓存块 | [第 11 章](../02-protocols-and-networking/11-gpu-data-path.md) |
| **NQN** | NVMe Qualified Name（NVMe 限定名称） | NVMe 主机或子系统的唯一名称 | [第 7 章](../02-protocols-and-networking/07-block-protocols.md) |
| **NVCS** | NVIDIA-Certified Storage（NVIDIA 认证存储） | NVIDIA 的分级存储认证（Foundation、Enterprise、NCP） | [第 34 章](../05-ai-storage/34-nvidia-ecosystem.md) |
| **NVMe** | Non-Volatile Memory Express（非易失性内存高速接口） | 闪存原生命令集，最多支持 65,535 个队列 | [第 7 章](../02-protocols-and-networking/07-block-protocols.md) |
| **NVMe-oF** | NVMe over Fabrics（基于网络架构的 NVMe） | 跨网络运行的 NVMe：FC、RDMA 或 TCP | [第 7 章](../02-protocols-and-networking/07-block-protocols.md) |
| **NVRAM** | Non-volatile RAM（非易失性内存） | 存放阵列写日志的持久性内存 | [第 13 章](../03-system-architecture/13-storage-stack.md) |
| **OP** | Over-provisioning（预留空间） | 用于垃圾回收的隐藏备用闪存 | [第 3 章](../01-storage-fundamentals/03-inside-an-ssd.md) |
| **OSD** | Object storage daemon（对象存储守护进程） | 管理一块硬盘的 Ceph 进程 | [第 15 章](../03-system-architecture/15-scale-out-shared-nothing.md) |
| **OSS** | Object storage server（对象存储服务器） | 提供文件数据服务的 Lustre 服务器 | [第 17 章](../03-system-architecture/17-parallel-file-systems.md) |
| **OST** | Object storage target（对象存储目标） | OSS 背后的 Lustre 数据卷 | [第 17 章](../03-system-architecture/17-parallel-file-systems.md) |
| **PFC** | Priority Flow Control（优先级流量控制） | 暂停某一类以太网流量以避免丢包 | [第 10 章](../02-protocols-and-networking/10-datacenter-networking.md) |
| **PG** | Placement group（放置组） | Ceph 的数据放置与再平衡单元 | [第 15 章](../03-system-architecture/15-scale-out-shared-nothing.md) |
| **PLC** | Penta-level cell（五层单元） | 每单元存储 5 bit 的 NAND | [第 53 章](../07-history-and-future/53-future-trends.md) |
| **PLP** | Power-loss protection（掉电保护） | 让 SSD 在断电时把缓冲写入落盘的电容 | [第 3 章](../01-storage-fundamentals/03-inside-an-ssd.md) |
| **pNFS** | Parallel NFS（并行 NFS） | NFSv4.1+ 的布局机制让客户端直接访问数据服务器 | [第 8 章](../02-protocols-and-networking/08-file-protocols.md) |
| **POSIX** | Portable Operating System Interface（可移植操作系统接口） | 应用所期望的 Unix 文件语义：重命名、锁、可见性 | [第 8 章](../02-protocols-and-networking/08-file-protocols.md) |
| **PUE** | Power usage effectiveness（电源使用效率） | 设施总功耗 ÷ IT 功耗；1.0 为理想值 | [第 4 章](../01-storage-fundamentals/04-performance-and-economics-metrics.md) |
| **QLC** | Quad-level cell（四层单元） | 每单元存储 4 bit 的 NAND；容量型介质 | [第 2 章](../01-storage-fundamentals/02-media-physics.md) |
| **QoS** | Quality of service（服务质量） | 按工作负载设置的性能上限或下限（例如 Fusion 预设） | [第 28 章](../04-everpure/28-platform-and-software.md) |
| **RAG** | Retrieval-augmented generation（检索增强生成） | 检索私有数据，再将其作为上下文输入 LLM | [第 33 章](../05-ai-storage/33-rag-vector-lakehouse.md) |
| **RAID** | Redundant array of inexpensive disks（廉价磁盘冗余阵列） | 跨硬盘的镜像或校验 | [第 6 章](../01-storage-fundamentals/06-data-protection-and-resilience.md) |
| **RDMA** | Remote direct memory access（远程直接内存访问） | 网卡在内存之间直接搬运数据，无需内核拷贝 | [第 10 章](../02-protocols-and-networking/10-datacenter-networking.md) |
| **RoCE** | RDMA over Converged Ethernet（基于融合以太网的 RDMA） | 以太网上的 RDMA；v2 基于 UDP/IP，可路由 | [第 10 章](../02-protocols-and-networking/10-datacenter-networking.md) |
| **RPO** | Recovery point objective（恢复点目标） | 以时间衡量的可容忍数据丢失量。在财务语境中：剩余履约义务（第 29 章） | [第 6 章](../01-storage-fundamentals/06-data-protection-and-resilience.md) |
| **RTO** | Recovery time objective（恢复时间目标） | 服务恢复前可容忍的停机时间 | [第 6 章](../01-storage-fundamentals/06-data-protection-and-resilience.md) |
| **S3** | Simple Storage Service（简单存储服务） | Amazon 的对象 API，事实上的标准 | [第 9 章](../02-protocols-and-networking/09-object-storage-and-s3.md) |
| **SAN** | Storage area network（存储区域网络） | 用于共享块存储的专用网络 | [第 13 章](../03-system-architecture/13-storage-stack.md) |
| **SCM** | Storage-class memory（存储级内存） | 介于 DRAM 和 NAND 之间的持久性介质（Optane、SLC SSD） | [第 12 章](../02-protocols-and-networking/12-interfaces-and-emerging-tech.md) |
| **SCSI** | Small Computer System Interface（小型计算机系统接口） | 1986 年的命令集，至今仍由 FC 和 iSCSI 承载 | [第 7 章](../02-protocols-and-networking/07-block-protocols.md) |
| **SDS** | Software-defined storage（软件定义存储） | 不带硬件机箱单独销售的存储操作系统 | [第 19 章](../03-system-architecture/19-software-defined-and-hci.md) |
| **SLA** | Service-level agreement（服务等级协议） | 合同约定的保证，例如 Evergreen//One 的可用性 | [第 23 章](../03-system-architecture/23-consumption-models.md) |
| **SLC** | Single-level cell（单层单元） | 每单元存储 1 bit 的 NAND：最快、最耐用 | [第 2 章](../01-storage-fundamentals/02-media-physics.md) |
| **SMB** | Server Message Block（服务器消息块） | Windows 文件共享协议；SMB3 增加了 Multichannel | [第 8 章](../02-protocols-and-networking/08-file-protocols.md) |
| **SMR** | Shingled magnetic recording（叠瓦式磁记录） | HDD 磁道相互重叠：容量更大，需顺序写入 | [第 2 章](../01-storage-fundamentals/02-media-physics.md) |
| **SPDK** | Storage Performance Development Kit（存储性能开发套件） | 用户态、轮询式 NVMe 驱动库 | [第 43 章](../06-industry-and-competition/43-weka.md) |
| **SQ/CQ** | Submission / completion queue（提交队列 / 完成队列） | NVMe 成对的命令环与完成环 | [第 7 章](../02-protocols-and-networking/07-block-protocols.md) |
| **SSD** | Solid-state drive（固态硬盘） | 集成 NAND、控制器、FTL 和 DRAM 的单一设备 | [第 3 章](../01-storage-fundamentals/03-inside-an-ssd.md) |
| **STaaS** | Storage as a service（存储即服务） | 厂商拥有部署在客户现场的存储；客户按 SLA 为使用量付费 | [第 23 章](../03-system-architecture/23-consumption-models.md) |
| **TAM** | Total addressable market（潜在市场规模） | 某品类若赢下所有交易可获得的支出总额 | [第 40 章](../06-industry-and-competition/40-market-structure.md) |
| **TCO** | Total cost of ownership（总拥有成本） | 一段时间内的购置、电力、空间、支持和运维成本 | [第 4 章](../01-storage-fundamentals/04-performance-and-economics-metrics.md) |
| **TCV** | Total contract value（合同总价值） | 一份合同在整个期限内的价值 | [第 23 章](../03-system-architecture/23-consumption-models.md) |
| **TLC** | Triple-level cell（三层单元） | 每单元存储 3 bit 的 NAND；性能型介质 | [第 2 章](../01-storage-fundamentals/02-media-physics.md) |
| **TTFT** | Time to first token（首 token 延迟） | LLM 输出第一个 token 之前的延迟 | [第 32 章](../05-ai-storage/32-inference-and-kv-cache.md) |
| **UEC** | Ultra Ethernet Consortium（超以太网联盟） | 推出 2025 年面向 AI/HPC 的以太网传输协议的组织 | [第 10 章](../02-protocols-and-networking/10-datacenter-networking.md) |
| **URE** | Unrecoverable read error（不可恢复读错误） | 硬盘无法读回的扇区；重建时的风险所在 | [第 6 章](../01-storage-fundamentals/06-data-protection-and-resilience.md) |
| **WAF** | Write amplification factor（写放大系数） | NAND 写入量 ÷ 主机写入量 | [第 3 章](../01-storage-fundamentals/03-inside-an-ssd.md) |
| **ZNS** | Zoned Namespaces（分区命名空间） | 按区顺序写入、由主机重置的 NVMe 分区 | [第 12 章](../02-protocols-and-networking/12-interfaces-and-emerging-tech.md) |

*表 60.1 — 104 个缩略语，每个都链接到解释它的章节。*

