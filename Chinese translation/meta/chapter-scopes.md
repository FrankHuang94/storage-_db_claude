# 章节范围（摘自委托说明书）

> 📄 英文原文：[meta/chapter-scopes.md](../../meta/chapter-scopes.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

配合 `meta/outline.md`（路径、预算、计划图表）和 `meta/agent-brief.md`（写作方法）使用。

## 第 0 部分——从这里开始
- **0.1 如何使用本图谱。** 学习路径：2 小时速成课程、2 天入门计划、2 周精通计划。深度标签 L1/L2/L3。章节的组织结构。如何使用对话工具包。
- **0.2 一页全景图。** 一张覆盖整个领域的 Mermaid 思维导图，外加一份"10 张图看懂 Everpure"摘要。

## 第 1 部分——存储基础
1. **存储做什么。** 数据生命周期；主存储 vs 二级存储 vs 归档存储；块存储 vs 文件存储 vs 对象存储（每种抽象是什么、谁在使用）。
2. **写给半导体人士的介质物理。** HDD 机械原理；NAND 单元（SLC→TLC→QLC→PLC）；3D NAND 层数扩展；耐久度与数据保持；HDD 与 NAND 的每比特成本曲线。包括 ★ 内存 / 介质层级金字塔（HBM → DRAM → CXL → NVMe → 网络化闪存 → HDD → 磁带），标注每一层的延迟、$/GB 和容量。
3. **SSD 内部结构。** 控制器、FTL、垃圾回收、写放大、预留空间，以及为什么 FTL 是通用 SSD 损失效率的地方（为第 26 章的 DirectFlash 做铺垫）。
4. **性能与经济性指标。** IOPS、吞吐量、延迟、队列深度、尾延迟；原始容量 vs 可用容量 vs 有效容量；$/TB、TB/W、每机架单元 TB 数（TB/rack-unit）；附算例的 TCO。
5. **数据缩减。** 重复数据删除、压缩、精简配置；为什么数据缩减比被激进营销；如何对厂商宣称值做合理性核查。
6. **数据保护与韧性。** RAID、纠删码、快照、克隆、同步 / 异步复制、RPO/RTO、延伸集群（stretched cluster）、勒索软件与不可变性。

## 第 2 部分——协议与网络
7. **块协议。** SCSI → Fibre Channel → iSCSI → NVMe → NVMe-oF（FC-NVMe、RoCE、TCP），每一种都配读 / 写时序图（★ NVMe-oF 读 / 写时序图）。
8. **文件协议。** NFSv3 / v4.1 / pNFS、SMB，以及 HPC 和 AI 为什么看重并行文件访问。
9. **对象存储与 S3。** S3 API、一致性模型、分段上传（multipart upload）、S3 为何正成为 AI 数据的默认接口、S3-over-RDMA。
10. **面向存储的数据中心网络。** Ethernet vs InfiniBand、RDMA、RoCEv2、400/800G、拥塞控制、NVIDIA Spectrum-X、存储路径中的 DPU/SmartNIC（BlueField）。
11. **GPU 数据路径。** GPUDirect Storage、GPUDirect RDMA、Magnum IO、NIXL。为什么"让 GPU 吃饱"是问题的全部，附 GPU 空闲成本算例。★ GPU 直连路径 vs 传统路径。
12. **接口与新兴技术。** PCIe 各代、CXL、EDSFF、分区命名空间（Zoned Namespaces）/ 灵活数据放置（Flexible Data Placement）、计算存储（computational storage）、Optane 的教训。

## 第 3 部分——存储系统架构基础
每个架构章节（第 14–19 章）必须涵盖：(a) 工作原理——组件图 + 端到端追踪一次读和一次写的时序图；(b) 状态和元数据存放在哪里；(c) 如何扩展（容量、性能、元数据）以及在哪里遇到瓶颈；(d) 故障处理：硬盘、节点、控制器、网络链路；(e) 优缺点表；(f) 最适合和最不适合的工作负载；(g) 采用该架构的真实产品；(h) 成本与运维影响。
13. **逐层解析存储栈。** 应用 → 文件系统 → 卷管理器 → 协议 → 网络 → 控制器 → 介质。每种架构把"智能"放在哪一层；DAS → SAN/NAS → 分布式 → 分解式的演进。★ 逐层示意图。
14. **纵向扩展双控制器阵列。** 双活（active/active）vs 主备（active/passive）、ALUA、镜像写缓存 / NVRAM、一次写操作如何得到确认、不停机控制器升级。示例：FlashArray、Dell PowerStore/PowerMax、NetApp AFF/ONTAP HA 对。
15. **横向扩展无共享集群。** 节点设计、数据放置（一致性哈希、CRUSH 式）、再平衡、东西向流量、法定多数（quorum）。示例：PowerScale/Isilon、WEKA、Ceph、ONTAP 集群。
16. **分解式全共享架构（DASE 式）。** 无状态计算节点、共享 NVMe-oF 存储柜、全局命名空间、性能与容量解耦。示例：VAST、FlashBlade//EXA 的元数据 / 数据分离，以及其他产品。
17. **并行与分布式文件系统。** Lustre（MDS/MDT、OSS/OST）、IBM Storage Scale/GPFS、BeeGFS、客户端条带化。HPC 为什么构建了它们；AI 为什么连同其痛点一起继承了它们。
18. **对象存储架构。** 扁平命名空间、元数据数据库、跨节点和跨站点的纠删码、网关、一致性与规模之间的取舍。示例：S3、MinIO、Cloudian、Ceph RGW、FlashBlade 对象存储。
19. **软件定义存储与 HCI。** 运行在通用服务器上的 Ceph、vSAN、Nutanix 和 MinIO；云块存储的内部机制（EBS 式）；纯软件模式 vs 一体机模式的商业模式权衡。
20. **面向存储的分布式系统基础。** 一致性模型、L2 层面的共识（Paxos/Raft）、持久性计算（几个 9、平均数据丢失时间）、故障域、实践中的 CAP、缓存 / 分层设计。
21. **元数据：隐藏的瓶颈。** 命名空间、inode、日志结构设计、小文件问题、元数据扩展策略、AI 工作负载为什么元数据密集。
22. **控制平面与集群（设备群）管理。** 遥测、AIOps、策略驱动的管理、API 与自动化。
23. **消费模式。** 资本支出、租赁、存储即服务（Storage-as-a-Service）与订阅式升级；商业模式如何塑造架构。
24. **架构决策矩阵。** 以一张大型 ★ 热力表呈现每种架构对每类工作负载（数据库、虚拟机、容器、备份、HPC、AI 训练、AI 推理 / KV 缓存、RAG、归档）的适配度，外加一张 ★ 决策树示意图（"给定工作负载 X，应选哪种架构以及为什么"）。

## 第 4 部分——Everpure
25. **公司历史与战略，2009–2026。** ★ Mermaid 时间线：创立、第一款 FlashArray、2015 年 IPO、Evergreen、FlashBlade、Portworx、超大规模云厂商设计导入（design win）、Enterprise Data Cloud、2026 年 2 月更名为 Everpure、1touch；一张精简的并购记录表。每个日期都要核实。
26. **核心技术：Purity 与 DirectFlash。** L2 层面的 Purity 架构；为什么直接管理裸 NAND 胜过通用 SSD（半导体视角）；DFM 容量路线图（核实最新数据）；能效与功耗影响；对 NAND 供应商的依赖。★ Purity 架构；★ DirectFlash vs 通用 SSD 软硬件栈。
27. **产品组合：FlashArray 与 FlashBlade。** 用一张 ★ 谱系图呈现当前产品阵容；按工作负载定位；FlashBlade//EXA 架构与基准测试宣称（例如 MLPerf Storage——核实是哪个版本、哪个日期）。
28. **平台与软件。** Evergreen、Portworx、Pure1/Fusion、Enterprise Data Cloud、云服务。"存储厂商 → 数据管理平台"的转型应如何运作；1touch 数据智能投资逻辑。
29. **从技术视角看超大规模云厂商业务、生态与财务。** 关于 Meta 订单的公开信息；★ 合作伙伴 / 生态系统网络图（NVIDIA、Cisco、新兴 GPU 云、ISV）；收入结构、订阅 /ARR 以及与技术挂钩的毛利率驱动因素，附基于财报的图表。

## 第 5 部分——AI 存储
30. **端到端 AI 数据流水线。** 数据摄取 → 数据整理 → 训练 → 检查点保存 → 微调 → 推理 → RAG → 智能体，并标注每个阶段的 I/O 模式（★）。
31. **训练存储。** 数据集加载、吞吐量计算、检查点大小与频率，以 70B / 405B / 1T+ 模型为算例。
32. **推理与 KV 缓存。** 内存 / 存储层级（HBM → DRAM → CXL → 本地 NVMe → 网络化闪存）；KV 缓存卸载（NVIDIA Dynamo、KVBM、NIXL、LMCache——核实当前名称）；MLPerf Storage KV 缓存测试（核实是否存在）；存储在 token 经济学中的角色。★ KV 缓存分层。
33. **RAG、向量数据库与 AI 原生数据格式。** 嵌入向量、向量索引、Lance/LanceDB、Iceberg/Delta 湖仓；存储厂商与数据库厂商各自的位置。
34. **NVIDIA 生态与认证。** AI Data Platform 参考设计、DGX SuperPOD/BasePOD、NVIDIA-Certified Storage、NCP 认证；存储厂商如何通过 NVIDIA 赢得或失去 AI 工厂订单。
35. **AI 工厂与新兴 GPU 云（neocloud）。** CoreWeave、Lambda、Crusoe、Nebius 等：它们如何采购存储、看重什么。AI 工厂机架布局 SVG。
36. **超大规模云厂商如何构建 AI 存储。** Google Colossus、Meta Tectonic、AWS S3 Express / FSx for Lustre、Azure；自建与采购的决策逻辑。
37. **批判性地解读基准测试。** MLPerf Storage、SPECstorage、IO500：它们如何运作、厂商如何刷分、应该问哪些问题。
38. **电力、密度与 AI 数据中心。** TB/W 与每机架 TB 数的计算；闪存取代 HDD；电力约束作为需求驱动因素。
39. **智能体 AI 与数据智能。** 元数据、语义层、治理、发现 / 分类；存储与数据管理的融合。

## 第 6 部分——行业与竞争
40. **市场结构与规模。** 企业主存储、文件 / 对象存储以及 AI 存储的潜在市场规模（TAM），附带来源的数据、份额趋势和图表。
41. **AI 原生存储厂商为何获得如此强的市场牵引力。** 贯穿全书的核心论点：适配 GPU 并行 I/O 和元数据密集型工作负载的架构；与 NVIDIA 的协同及认证；新兴 GPU 云作为新的买家类别；基于通用硬件的软件定义模式；HPC 传承；产品迭代速度；传统厂商的盲点。以及该论点在哪些地方站不住脚或被过度炒作。
42. **VAST Data 深度剖析（约 4,000）。** *技术：* DASE、Element Store、QLC + 高速持久层、基于相似性的数据缩减、多协议（NFS/SMB/S3/块）、向数据库 / 计算 / AI 数据平台的上移（DataBase、DataEngine、InsightEngine、AgentEngine——核实当前名称），架构示意图 + I/O 全流程走查。*商业：* 创立历史、融资轮次与估值（公司自述 vs 媒体报道）、收入 /ARR 信号、在合作伙伴硬件上运行软件的模式、OEM/合作伙伴渠道、标杆客户（需核实）。*为何在赢、风险、待解问题；* 与 FlashBlade//EXA 的比较。
43. **WEKA 深度剖析（约 3,500）。** *技术：* WekaFS / NeuralMesh（需核实）、运行在通用服务器和云上的并行分布式软件定义架构、内核旁路（kernel-bypass）数据路径、KV 缓存 / 内存扩展（Augmented Memory Grid——需核实）、GPU 直连集成。*商业：* 发展历史、融资与估值、市场进入策略（云市场、OEM、新兴 GPU 云）、客户、竞争地位。*为何在赢、风险、待解问题；* 与 FlashBlade//EXA 和 VAST 的比较。
44. **DDN 深度剖析（约 3,500）。** *技术：* EXAScaler（基于 Lustre）、Infinia（需核实）、HPC 传承、在 NVIDIA 自有 AI 基础设施中的角色（需核实）。*商业：* 创始人主导的私有股权结构、盈利能力宣称、外部投资（核实近期融资轮次）、政府 /HPC/AI 客户、合作关系。*为何在赢、风险、待解问题；* 与其他厂商的比较。
45. **正面对比：FlashBlade//EXA vs VAST vs WEKA vs DDN。** 架构、性能宣称、数据缩减、协议、硬件模式、定价 / 消费模式、市场进入策略、生态、目标客户——多维度矩阵、雷达式图表、"谁赢下哪类订单以及为什么"对比表。★ 四方架构对比。
46. **传统厂商。** Dell、NetApp、HPE、IBM、Hitachi Vantara、Huawei——每家一页概况：架构、AI 战略、商业模式、优势、劣势。
47. **其他挑战者与软件定义厂商。** Hammerspace、Qumulo、MinIO、Cloudian、基于 Ceph 的产品、Nutanix、超大规模云厂商原生存储。
48. **介质供应商与 NAND 周期。** Samsung、SK hynix/Solidigm、Kioxia、Micron、Sandisk、Western Digital、Seagate；价格周期如何影响阵列厂商；HDD vs QLC 的经济性。
49. **竞争格局矩阵。** 覆盖整个领域的 ★ 四象限图（Mermaid `quadrantChart`）和热力表。
50. **存储 / AI 数据类标的的技术尽职调查框架。** 架构、性能宣称、可扩展性、元数据设计、持久性、路线图、团队、与 Purity/Fusion 的整合；可复用的核查清单 + 评分卡模板，并仅使用公开数据，以 VAST/WEKA/DDN 之一作为算例加以应用。

## 第 7 部分——历史与未来
51. **存储历史，1956–2026。** IBM RAMAC → RAID（1988）→ SAN/NAS → 闪存阵列 → 云 → AI；★ 时间线 +"每个时代的启示"。
52. **闪存与 NAND 经济学的历史。** 成本曲线图、拐点、全闪存为何赢下主存储市场。
53. **未来趋势，2026–2032。** 更大容量的闪存模块、PLC、HDD 的未来、CXL、分解式架构、光子互连、KV 缓存作为新的存储层、数据管理融合、主权 / 边缘 AI。每一项都给出：可能性、时间点、赢家 / 输家、对 Everpure 的影响。★ 未来趋势雷达图。
54. **战略选项图（基于公开信息）。** 覆盖整个技术栈的自建 / 收购 / 合作选项，★ 分层技术栈示意图。

## 第 8 部分——对话工具包
55. **与产品经理对话。** 存储产品经理如何思考；按产品线划分的问题集。
56. **与工程负责人及 CTO 办公室对话。** 架构评审问题、高质量回答是什么样子、危险信号。
57. **问题库：150 个问题，** 按主题和受众（PM / Eng / CTO / Sales Eng）打标签。
58. **"30 秒讲清楚"。** 面向 CFO 或董事会受众的 60 条一句话解释。
59. **自测。** 使用 `<details>` 标签的 200 张闪卡，按部分组织。
60. **速查表。** 缩略语速查表、★ 协议对比海报、★ 架构对比海报、★ 产品阵容海报。
