## 3. 向 Everpure 人员提出的问题（301）

| 章 | 对象 | 问题 |
|---|---|---|
| 0.1 | PM | 本图谱针对贵产品线的定位表中，哪一行是错的？哪一笔丢单可以证明？ |
| 0.1 | PM | 哪个内部指标最能预测续约或扩容，而公开指标（ARR、NDR、客户数）掩盖了它？ |
| 0.1 | Eng | 这是我对 Purity 写入路径的 L2 模型；对当前版本而言，哪一步是错的？ |
| 0.1 | CTO | 本图谱"不要这样说"中列出的误解，哪一条您最常从存储新人那里听到？ |
| 0.1 | CTO | 关于 Everpure 所在市场的基准测试或分析师数据，您最不信任哪一个？您会改用什么？ |
| 0.2 | PM | "用 10 张图看懂 Everpure"中的十个视角，哪一个在两年内变化最大？什么事件会改变它？ |
| 0.2 | PM | FY27 收入增长中，有多少来自 NAND 价格传导、多少来自出货容量？内部如何跟踪？ |
| 0.2 | Eng | 掌控技术栈第 6 至第 8 层，每一代 NAND 在认证时间和工程人力上要付出多少成本？ |
| 0.2 | CTO | 如果 Hammerspace 这类 pNFS 命名空间层架在所有阵列之上，什么能让阵列继续成为控制点？ |
| 0.2 | CTO | 哪个信号会最先告诉您 FlashBlade//EXA 是否已追平与 VAST 在参考客户和认证上的差距？ |
| 2 | Eng | 在 QLC DirectFlash Module 上，Purity 按工作负载类型在现场实测的写放大是多少？在 150 TB 和 300 TB 下留出多少 DWPD 余量？ |
| 2 | PM | 按 2026 年 SSD:HDD 的 $/TB 溢价，我们推销全闪存替代磁盘时采用的盈亏平衡溢价是多少？短缺是否改变了 HDD 替换项目的赢单率？ |
| 2 | CTO | 在 Purity 中管理裸 NAND，是否让 Everpure 能比商用 SSD 厂商更早采用 PLC 或更高层数的 QLC？PLC 需要满足什么条件才可行？ |
| 2 | Eng | 在以读为主的 AI 训练数据集上，Purity 如何调度读干扰（read-disturb）迁移和数据保持巡检，而不损害尾延迟？ |
| 2 | PM | 2026 年 NAND 合约价上涨中，有多少已传导到 FlashArray/FlashBlade 定价，又有多少由毛利率吸收？ |
| 3 | Eng | 在典型 FlashArray 和 FlashBlade 工作负载上，Purity 实测的端到端 WAF 是多少？比同样数据放在标准 SSD 上低多少？ |
| 3 | CTO | 随着 FDP 在超大规模云厂商中普及，您预期 DirectFlash 的哪部分优势能够保持：WAF、映射表 DRAM、池化备用闪存、延迟控制还是模块密度？ |
| 3 | Eng | DFM 映射状态存放在哪里？模块从 150 TB 走向 300 TB 及以上时，控制器内存每 PB 如何扩展？ |
| 3 | PM | 在与采用 122–245 TB QLC SSD（间接映射单元 16 KB 以上）的阵列竞争时，小块写性能或耐久度有多常成为决定因素？ |
| 3 | Eng | 在老化的 QLC DFM 上，LDPC 读重试和读干扰刷新如何调度以保护尾延迟？ |
| 4 | PM | Pure1 遥测按工作负载类别（数据库、虚拟机、文件共享、AI 语料）显示的缩减比是多少？为 AI 数据湖报有效容量时我们采用哪个比率？ |
| 4 | PM | 按当前 NAND 合约价，在容量层上我们与混合磁盘的 $/有效 TB 交叉点在哪里？哪些项目属性（功率上限、性能下限、可缩减数据）能赢下它？ |
| 4 | Eng | 在 90% 满的系统上、DFM 重建期间、70% 额定负载下，FlashArray 和 FlashBlade 的 p99.9 读延迟是多少？ |
| 4 | CTO | 当实际数据缩减低于假设比率时，Evergreen//One 的利润率表现如何？是否在考虑针对 AI 工作负载按可用 TB 定价？ |
| 4 | Eng | Evergreen//One 的 watts/TiB 保证是在阵列电源处实测还是建模得出？不可压缩数据如何处理？ |
| 5 | PM | 剔除精简配置和快照后，按工作负载划分的设备群数据缩减比中位数和第 25 百分位数是多少？随着 AI 数据增长有何变化？ |
| 5 | PM | Right-Size Guarantee 如何为 AI 数据集和检查点估算容量？该保证历史上以免费容量形式付出了多少成本？ |
| 5 | Eng | FlashArray 去重索引存放在哪里？每 PB 有多大？在什么负载下内联缩减会延后执行？ |
| 5 | CTO | 格式感知压缩（BF16/FP8 张量、token 分片、KV 缓存块）是否是 DeepReduce 的一条路径？相似性缩减是否会扩展到 FlashBlade//EXA 数据节点？ |
| 5 | Eng | 在同一数据集上正面对比，DeepReduce 与 VAST 相似性缩减相比如何？增量编码块的读放大代价是多少？ |
| 6 | PM | Evergreen//One Cyber Recovery and Resilience SLA 的附加率是多少？被触发过多少次？履约成本是多少？ |
| 6 | Eng | 一块 300 TB DFM 彻底失效（无法迁出）时，在 80% 填充和生产负载下恢复到完全冗余需要多久？主机可见的性能影响是什么？ |
| 6 | Eng | 如果仲裁器（mediator）和站点间链路同时失效，ActiveCluster 预选举和 Pure1 Cloud Mediator 的行为如何？ |
| 6 | CTO | PB 级恢复带宽（例如 FlashBlade//EXA 的 AI 数据集）是否应成为合同 SLA 指标？要兑现它，架构需要具备什么？ |
| 6 | PM | 在"最后一道防线"预算上，Everpure 对 Veeam/Rubrik/Cohesity 在哪里赢、在哪里输？策略是合作、集成还是自建？ |
| 7 | PM | 从 Pure1 遥测看，FlashArray 当前的主机接入组合（FC、NVMe/FC、iSCSI、NVMe/TCP、NVMe/RoCE）如何？新装机中 NVMe/TCP 增长多快？ |
| 7 | Eng | 在当前 FlashArray 上，QD1 与饱和状态下，NVMe/TCP 与 NVMe/RoCE 的实测延迟和每 IOPS 主机 CPU 差距是多少？ |
| 7 | PM | 在 Nutanix AHV 及其他 VMware 迁出项目中，NVMe/TCP 的发现与自动化能力（相对于 Dell SFSS 式集中发现）是帮助赢单还是导致丢单？ |
| 7 | CTO | 当主机前端已经是 NVMe-oF 时，DirectFlash 的端到端 NVMe 路径是否还能带来可测量的优势，还是主要体现在效率和密度上？ |
| 7 | Eng | FlashArray 对 NVMe-oF 队列对和每端口主机连接数的上限是多少？面对数千个 Kubernetes 节点时表现如何？ |
| 8 | PM | FlashBlade//EXA pNFS 客户端验证过哪些 Linux 发行版和内核版本？目标新兴 GPU 云（neocloud）设备群中有多少运行较旧内核？ |
| 8 | Eng | 在 EXA 上，数据节点失效时正在进行的写入会怎样？在 1,000+ 客户端规模下，一次布局召回（layout recall）加重新获取需要多久？ |
| 8 | CTO | 鉴于所有 pNFS 厂商都依赖同一套代码，Everpure 是否打算派工程师为上游 Linux pNFS/NFS-RDMA 客户端做贡献？ |
| 8 | PM | 是否计划在 FlashBlade//S 上支持 pNFS，使企业客户和 EXA 客户共享同一套并行访问方案？ |
| 8 | Eng | 在与 VAST 多路径 NFS 客户端的正面测试中，EXA 在启用和不启用 GDS 时每客户端吞吐量分别达到多少？ |
| 9 | PM | S3 over RDMA 目前是否已在 FlashBlade 上正式发布（GA）？支持哪些型号？它与 NVIDIA cuObject 客户端兼容，还是另一套实现？ |
| 9 | Eng | 在十亿键的存储桶上，FlashBlade 能持续多高的 LIST 速率和小对象（4–64 KB）GET 延迟？与原生对象存储竞争对手相比如何？ |
| 9 | Eng | FlashArray 的 S3 实现与 FlashBlade 的有何不同（一致性、分段上传限制、条件写入、性能包络）？ |
| 9 | CTO | Everpure 将 S3 Tables 和 S3 Vectors 的本地部署对应物视为存储平台功能，还是合作伙伴/生态层？ |
| 9 | PM | 在 AI 项目中，新增 FlashBlade 容量有多大比例主要通过 S3 而非 NFS 访问？趋势如何？ |
| 1 | PM | FlashArray 和 FlashBlade 出货容量中，有多少部署为二级/备份存储、多少为主存储？自 //E 推出以来趋势如何？ |
| 1 | PM | 在 AI 项目中，签单的买方是谁：AI 平台团队、中央 IT 还是新兴 GPU 云运营商？Everpure 对不同买方的赢单率有何差异？ |
| 1 | CTO | 当同一数据集必须同时通过 S3 和 NFS 提供时，Everpure 是保留一份具有双重语义的副本，还是两个视图？还剩哪些语义冲突（重命名、部分覆盖写、ACL）？ |
| 1 | Eng | 目前是什么限制了 FlashBlade 上的对象列举和小文件元数据速率？//EXA 如何改变这一点？ |
| 1 | CTO | Everpure 如何看待归档层的走向：超大规模云厂商中的 DirectFlash 只在温数据层替代 HDD，还是也会进入由磁带服务的近归档层？ |
| 10 | PM | FlashBlade//EXA 的 AI 商机中，有多大比例涉及 InfiniBand 计算网络？已有独立以太网存储网络的情况有多常见？ |
| 10 | CTO | 以 STX 实现的方式在 BlueField-4 上运行 Purity 服务（元数据、数据缩减、KV 缓存服务），在技术和商业上是否有吸引力，还是会削弱控制器的差异化？ |
| 10 | Eng | FlashBlade RDMA 部署假设采用何种丢包恢复模式和 PFC/ECN 阈值？在有损或 UEC 风格的网络上表现如何？ |
| 10 | PM | 在网络厂商站队上，Everpure 如何权衡 NVIDIA Spectrum-X 认证深度、基于 UEC/Broadcom 的中立性以及与 Cisco 的合作关系？ |
| 10 | Eng | 面对数百个 GPU 节点同步检查点突发，Everpure 按什么样的 incast 行为和存储侧端口数进行设计？ |
| 11 | Eng | FlashBlade（S 和 EXA）通过 NFS-RDMA 配合 GDS 向一台当前 HGX/DGX 节点提供的单节点读吞吐量是多少？瓶颈在网卡、Linux NFS 客户端的并发能力，还是阵列？ |
| 11 | Eng | 在 FlashBlade//EXA 上，一次 4,000 GPU 检查点的端到端恢复需要多久（包括分片文件上的元数据 open/stat 风暴）？ |
| 11 | PM | Everpure 是否维护或计划为 FlashBlade/PureKVA 提供上游 NIXL 后端？采用哪条插件路径（POSIX、GDS、OBJ/S3-RDMA）？ |
| 11 | CTO | NVIDIA 的 BlueField-4 STX/CMX 上下文内存层发布后，Everpure 预期自己是供应该层、作为 Dynamo 的 G4 位于其后方，还是与之竞争？ |
| 11 | PM | 在近期丢掉的 AI 项目中，专有并行文件系统客户端（WEKA、Lustre、GPFS）凭借每节点吞吐量或检查点恢复时间胜过标准 NFS 客户端的情况有多常见？ |
| 12 | PM | 与最好的标准 E3.L QLC 盘相比，DFM 每代在容量和 TB/W 上领先多少？当标准盘达到 512 TB 时这一领先如何变化？ |
| 12 | Eng | 在混合工作负载上，Purity 实测 WAF 与启用 FDP 的商用 SSD 相比如何？Purity 是否在任何地方使用 FDP（例如 FlashArray//ST 的商用盘）？ |
| 12 | CTO | CXL 挂接内存在 FlashArray/FlashBlade 控制器内部（去重表、元数据缓存）是否有用武之地？或作为与 PureKVA 并列的 KV 缓存层？ |
| 12 | CTO | DirectFlash 和 EXA 技术栈中，目前哪些组件实际上是单一来源（NAND、控制器、DPU、网卡）？第二来源计划是什么？ |
| 12 | PM | 鉴于限制阵列吞吐量的是前端网络而非盘链路，PCIe 6.0 的 DFM 或控制器何时才具备经济合理性？ |
| 13 | CTO | Everpure 预期下一个商品化的技术栈层是哪一层（例如 DPU 承载的存储服务、标准 SSD 上的 FDP）？这如何改变 DirectFlash 授权的投资逻辑？ |
| 13 | Eng | 在 FlashArray 上，通过 NVMe/TCP 与 NVMe/RoCE 进行一次 4 KB 写入时，各层的 p99 延迟预算是多少？负载升高时哪一层最先变化？ |
| 13 | Eng | 与同等商用 QLC SSD 相比，DirectFlash 每个 150 TB 模块省去了多少 FTL DRAM 和预留空间？ |
| 13 | PM | 在超大规模云厂商项目中，价值如何在模块设计、闪存管理软件和支持服务之间分配？是什么阻止客户像 AWS 做 Nitro SSD 那样自行内化？ |
| 13 | PM | Everpure 在哪些项目中输给纯软件方案？哪些产品（Portworx、Everpure Cloud）被定位来应对？ |
| 14 | PM | 在 XL190 上进行 Evergreen 控制器更换时，一个控制器离线期间会失去哪些 Purity Turbo 读性能增益？单控制器窗口通常持续多久？ |
| 14 | Eng | 在 Purity Turbo 下，次控制器的读缓存如何与主控制器负责的写入保持一致？在互连带宽上代价多大？ |
| 14 | Eng | FlashArray 下一个性能天花板是 CPU、内存带宽、PCIe 通道还是 DFMD NVRAM 带宽？ |
| 14 | CTO | 把双活（active/active）从读扩展到更多操作，是否与"故障切换无性能损失"的承诺相冲突？会如何定价或附加说明？ |
| 14 | PM | 对于超出单台 //XL 的块存储客户，目前推荐的路径是什么：在集群管理下部署多台阵列、ActiveCluster，还是转向 FlashBlade？ |
| 15 | PM | 在与 PowerScale 的哪些正面竞争中，重建时间和捆绑扩展成本真正决定了结果？我们使用哪些证据？ |
| 15 | Eng | FlashBlade//S 刀片或 DFM 失效时，Purity//FB 如何放置和重建数据？每恢复 1 字节有多少字节穿过机箱网络？ |
| 15 | PM | 采用 FlashArray 作为外部存储的 Nutanix AHV 客户带来的商机管道有多大？是哪些容量与计算比在驱动它？ |
| 15 | CTO | 随着盘容量达到 100+ TB，Everpure 认为无共享竞争对手的节点丢失重建时间是持久的架构切入点，还是更宽的编码能够解决的问题？ |
| 15 | Eng | 客户将 FlashBlade 与自运维 Ceph 比较时，我们的 TCO 模型采用什么样的空闲空间预留、人员配置和重建窗口假设？ |
| 16 | PM | 在哪些项目画像（吞吐量、GPU 数量、命名空间规模）下，FlashBlade//EXA 的直连数据路径胜过共享介质的 DASE 设计？目前我们在哪里会输？ |
| 16 | Eng | 一次 EXA 写入在确认之前要穿越多少次后端网络？数据落在哪些故障域中？ |
| 16 | Eng | 在检查点进行中、80% 满时一个 EXA 数据节点失效，客户端吞吐量和数据可用性会怎样？恢复需要多久？ |
| 16 | CTO | 为基于 DirectFlash 的数据节点提供共享介质（DASE 式）模式是否在路线图讨论之中，还是元数据/数据分离是有意为之的长期押注？ |
| 16 | PM | 在一份大型 EXA 物料清单中，后端网络占多大比例？客户能否复用现有 GPU 网络？ |
| 17 | PM | 当 Lustre 或 GPFS 用户评估 FlashBlade//EXA 时，最常见的技术异议是什么？共享文件写一致性成为否决因素的情况有多常见？ |
| 17 | Eng | EXA 元数据核心每个刀片能持续多高的 create 和 open 速率？单个热点目录能否跨刀片扩展？ |
| 17 | Eng | 当客户端在 EXA 上写入中途挂起（布局召回、租约过期）时，会看到什么？其他客户端要等多久才能继续？ |
| 17 | CTO | 鉴于 EXA 相对 Lustre 的优势取决于 Linux pNFS 客户端的质量，向该客户端上游贡献是否是战略优先事项？ |
| 17 | PM | 对于 GPU 部署在公有云中的买方，EXA 如何与 Google、Azure 和 AWS 的托管 Lustre 竞争？ |
| 18 | Eng | 按对象数量计，生产环境中最大的 FlashBlade 存储桶有多大？在使用典型（非手工调优）客户端时能持续多高的 LIST 速率？ |
| 18 | Eng | Purity//FB 如何存储一个 4 KB 的 S3 对象：内联存于元数据、暂存于 NVRAM，还是立即纠删编码？在闪存上的放大是多少？ |
| 18 | PM | 在哪些对象存储项目中我们输给了基于 HDD 的 MinIO、Ceph 或 Cloudian？配备 DeepReduce 的 FlashBlade//E 能否改变 $/TB 的结果？ |
| 18 | CTO | 在 FlashBlade 对象存储项目中，客户是否要求跨站点的地理分散纠删码，还是异步复制已足够？ |
| 18 | PM | FlashBlade 的容量和 I/O 中，现在有多大比例是 S3 而非 NFS/SMB？是哪些 AI 工作负载在驱动？ |
| 19 | PM | 在 VMware 续约中，FlashArray 商机中有多大比例现在涉及非 VMware 虚拟化平台（Nutanix AHV、OpenShift Virtualization、Hyper-V）？自 2024 年以来变化如何？ |
| 19 | CTO | 若要以软件形式运行在客户自选的服务器上，Purity 需要放弃什么？DirectFlash 授权是否是实现同一目标的更好路径？ |
| 19 | Eng | 与 Nutanix 本地存储路径相比，NVMe/TCP 连接 FlashArray 为 Nutanix AHV 工作负载增加多少延迟和 CPU 开销？ |
| 19 | PM | 对于迁移到 KubeVirt/OpenShift Virtualization 的虚拟机，Portworx 如何相对 VMware 定位？它与 FlashArray 的附加率是多少？ |
| 19 | CTO | 可复制的 DirectFlash IP 授权业务（不止首家超大规模云厂商）是否与保护每笔交易的一体机毛利相兼容？ |
| 20 | Eng | FlashBlade 和 FlashBlade//EXA 的哪些服务运行共识协议（Raft/Paxos 或其他）？有多少投票成员？失去多数派时什么会停顿？ |
| 20 | CTO | Everpure 是否公布或在内部跟踪建模的持久性数字（几个 9/MTTDL）？如何对固件批次等相关性故障建模？ |
| 20 | Eng | 当前最大的 DirectFlash Module 在 80% 满、生产负载下的实测重建时间是多少？重建是否在整个阵列上分簇（declustered）进行？ |
| 20 | PM | 当前"六个 9"可用性数字是如何定义的（停机定义、是否包含升级、测量窗口、设备群覆盖范围）？ |
| 20 | PM | ActiveCluster 部署中，使用本地仲裁器与云仲裁器的比例各是多少？是什么驱动这一选择？ |
| 21 | Eng | 单个 FlashBlade//EXA 元数据机箱在单一共享目录与大量私有目录下分别能持续多高的 create/s 和 stat/s？什么最先饱和？ |
| 21 | PM | 在 EXA 项目中，客户数据集已经分片（WebDataset/TFRecord）的情况有多常见？剩下的哪些工作负载（检查点、数据整理、KV 缓存）真正决定元数据规模？ |
| 21 | CTO | Purity//FB 元数据数据库是否已（或计划公开）作为可查询索引开放给数据智能使用？靠什么隔离防止查询影响前台 I/O？ |
| 21 | Eng | PyTorch DCP 式检查点的 create 突发（每个 rank 一个文件、10k+ rank、同一目录）如何处理：目录哈希、锁粒度、p99 create 延迟？ |
| 22 | PM | Sev-1 支持工单中，有多大比例在客户察觉之前由 Pure1 开出？每台受支持阵列的成本趋势如何？ |
| 22 | Eng | Fusion 如何根据预设（preset）为新工作负载选择阵列？它权衡哪些输入（预测填充率、延迟等级、故障域）？ |
| 22 | CTO | 哪些护栏约束那些能（通过 MCP）在客户设备群上执行写操作的 AI 智能体？ |
| 22 | PM | 哪些 Evergreen//One SLA 在暗站点（dark site）无法执行？有多少订阅客户以暗站点方式运行？ |
| 23 | PM | Evergreen//One 按合同年度的毛利率如何？定价假设已部署余量的利用率是多少？ |
| 23 | PM | 哪些客户群选择 Evergreen//Forever 而非 Evergreen//One？会计处理方式（租赁还是服务）是否是主要驱动因素？ |
| 23 | Eng | 哪些代际边界约束曾让控制器或介质升级变得不简单？向后兼容如何测试？ |
| 23 | CTO | 订阅模式如何改变路线图优先级，例如密度和每 TB 瓦数相对峰值性能的权重？ |
| 24 | PM | 在哪些架构 × 工作负载单元格上，Everpure 是因架构而非价格而输？针对每一项的计划是什么（合作、路线图、放弃）？ |
| 24 | Eng | 对于 KV 缓存大小的随机读，FlashBlade//EXA 相对 FlashBlade//S 的实测 p99 延迟代价（如有）是多少？ |
| 24 | CTO | Everpure 所说的"统一"是指各产品行共用一个操作系统（Purity 系列），还是一个系统服务所有协议？为何做此选择而非 VAST 的单一系统路线？ |
| 24 | PM | 企业"AI 存储"商机最终变成容量/治理类（FlashBlade//E、对象存储）而非吞吐量类（EXA）项目的情况有多常见？ |
| 25 | CTO | Purity 代码库中哪些部分源自收购（Compuverde、StorReduce、Portworx）？发布前重写了多少？ |
| 25 | PM | Everpure 将用什么指标展示 Data Intelligence（原 1touch）的牵引力？何时可能单独披露？ |
| 25 | PM | Meta 和第二家超大规模云厂商的授权交易如何改变 FY2027–FY2028 的 Evergreen 与产品毛利率结构？ |
| 25 | Eng | 为适配客户自建硬件和客户自采 NAND，超大规模云厂商项目要求 Purity/DirectFlash 做了哪些改动？ |
| 25 | CTO | 回顾 2023 年"2028 年后不再有新 HDD"的判断，Everpure 现在预期 DirectFlash 将替代超大规模云厂商近线容量的多大比例？何时实现？ |
| 26 | Eng | 目前为 DirectFlash 认证一款新 NAND die 需要多久？同时有多少家供应商的多少款 die 在认证中？ |
| 26 | CTO | 如果 FDP 在标准 QLC SSD 上普及，DirectFlash 的哪些优势在系统层面仍可测量（W/TB、TB/RU、省去的 DRAM、WAF）？幅度多大？ |
| 26 | PM | 从 300 TB 到 600 TB DFM 的有日期的路径是什么？限制因素是什么：NAND die 密度、封装、功耗包络，还是重建/迁出时间？ |
| 26 | CTO | 获得授权的超大规模云厂商最终能否将全局 FTL 内化？授权中的哪些内容（软件更新、NAND 认证支持）让它保持依赖？ |
| 26 | PM | Q2 FY27 的 NAND 采购规模是如何确定的？它如何对冲固定价格的 Evergreen//One 承诺以应对 NAND 进一步涨价？ |
| 27 | PM | FlashBlade//EXA 商机管道中，有多大比例卡在 DFM 数据节点上、多少卡在 NCP/SuperPOD 认证上？各自何时解除？ |
| 27 | Eng | 在 30 节点的 MLPerf v3.0 检查点测试中，是什么限制了每节点吞吐量（网卡、SSD、元数据）？换成 DFM 数据节点后会有何变化？ |
| 27 | Eng | EXA 数据节点目前如何保护（HA 还是纠删码）？检查点进行中丢失一个数据节点时，客户端看到的是什么？ |
| 27 | PM | FlashArray//ST 在哪些项目中能赢下配备 Purity Turbo 的 //XL190 会输掉的单子？这一市场是否大到足以支撑一个独立 SKU？ |
| 27 | CTO | 如果 VAST、WEKA 和 DDN 参加下一轮 MLPerf Storage，Everpure 是否也会提交？针对哪些工作负载？ |
| 28 | PM | Data Intelligence 订单中，有多大比例覆盖的数据不存放在 Everpure 阵列上？它是否与存储分开定价和报告？ |
| 28 | PM | 在 1,200+ 家 Fusion 客户中，有多少通过 API 或 Terraform 在生产中运行预设？他们续约或扩容是否更快？ |
| 28 | CTO | Everpure 打算让 Data Intelligence 与 Unity Catalog、Purview 等数据目录集成还是竞争？为何不加入 Open Semantic Interchange？ |
| 28 | Eng | 如何从 Purity 写入路径或快照触发内容分类而不影响延迟？哪些在阵列上运行、哪些在 SaaS 中运行？ |
| 28 | PM | Evergreen//One 的 25% 缓冲在整个设备群上让 Everpure 付出多少已部署容量？FY27 的 NAND 涨价如何改变了定价？ |
| 29 | PM | 超大规模业务收入如何定价：按部署 TB、按模块，还是按授权档位？DFM 容量翻倍时会如何变化？ |
| 29 | CTO | DirectFlash 要在超大规模云厂商内部替代 HDD 层（而不只是 SSD 层）需要什么条件？功耗/密度阈值在哪里？ |
| 29 | PM | Evergreen//One 毛利率的改善中，有多少来自 DFM 密度、多少来自数据缩减、多少来自定价？ |
| 29 | Eng | 超大规模部署与 FlashArray/FlashBlade 之间共享多少 Purity 代码？谁负责与超大规模云厂商设备群软件的集成？ |
| 29 | PM | 哪些新兴 GPU 云项目是因 NCP 认证而非价格赢下或丢掉的？面向 EXA 的 Evergreen//One 是否改变了新兴 GPU 云的融资方式？ |
| 30 | PM | 目前 Everpure 归属于 AI 的订单中，各流水线阶段（数据湖、训练/检查点、推理 KV、RAG/智能体）各占多少？哪一项增长最快？ |
| 30 | PM | 当客户的 AI 数据湖已在超大规模云厂商的对象存储中时，Everpure 赢下本地热数据层的打法是什么？是否曾把数据湖本身拉回本地？ |
| 30 | Eng | 在 FlashBlade//EXA 上，16K GPU 规模下一个约 6 TB 检查点造成的 GPU 阻塞时间是多少？其中有多少被主机 DRAM 或本地 NVMe 暂存吸收？ |
| 30 | CTO | Everpure 是否把智能体记忆/状态视为一种独立的存储工作负载（KV 缓存之外）？Data Intelligence 是否意在成为其元数据层？ |
| 30 | Eng | 鉴于 MLPerf Storage v3.0 新增了 S3 访问层，在训练数据加载方面，FlashBlade 的 S3 路径与 NFS-over-RDMA 路径相比如何？ |
| 31 | PM | 在近期训练项目中，客户是以突发写入 GB/s、持续排空速率还是恢复训练时间来规定检查点性能的？他们运行的是哪些框架（同步还是异步、本地检查点）？ |
| 31 | Eng | 在 FlashBlade//EXA 上，一次冷启动的 16K rank 检查点恢复是什么样子（每秒文件打开数、读 GB/s、最慢客户端的尾部）？为什么 v3.0 检查点读（588 GiB/s）低于写（877 GiB/s）？ |
| 31 | Eng | 在多 TB 检查点排空途中一个 EXA 数据节点失效时，表现如何：降级后的写带宽以及恢复全速所需时间？ |
| 31 | CTO | 随着异步、本地 NVMe 和内存内检查点消除了突发需求，Everpure 预期训练存储的差异化将落在哪里：恢复速度、留存经济性，还是把检查点作为资产进行数据管理？ |
| 31 | PM | 是否有参考规划工具，能把模型规模、GPU 数量、故障率和检查点间隔换算成 EXA 节点数？一线团队是否在用？ |
| 32 | PM | 典型 PureKVA 客户在生产中看到的每 GPU 恢复带宽和命中率是多少？TTFT 与本地 NVMe 上的 LMCache 相比如何？ |
| 32 | CTO | Everpure 将 FlashBlade//EXA 定位为 NVIDIA STX/CMX 机柜内的软件层、位于其后的 G4 层，还是它们的替代方案？ |
| 32 | Eng | 是否有（或将有）面向 FlashBlade 的上游 NIXL 后端和 LMCache/llm-d 连接器？采用哪种传输（NFS over RDMA、S3 over RDMA、GDS）？ |
| 32 | PM | KV 层应如何定价（按 TB、按 GB·小时、按服务的 token）？DeepReduce 对 fp16/fp8 KV 张量能否带来任何可测量的缩减？ |
| 32 | Eng | 当客户更新模型权重或更换 tokenizer/推理引擎时，PureKVA 如何为缓存的 KV 设置键、版本并使其失效？ |
| 33 | PM | 当 FlashBlade 客户用 Data Stream 运行 RAG 时，向量索引放在哪里（DRAM、本地 SSD、FlashBlade）？哪些合作伙伴引擎已通过验证？ |
| 33 | Eng | FlashBlade 对小型 S3 GET 的单请求延迟和 LIST 速率是多少？以 FlashBlade 作为 SSD 层时，一个 10 亿向量的 DiskANN 或 SPANN 索引表现如何？ |
| 33 | PM | 哪些湖仓引擎（Spark、Trino/Starburst、Dremio、Snowflake、Databricks）在生产中于 FlashBlade 上读写 Iceberg？托管压缩合并（compaction）是否在路线图讨论之中？ |
| 33 | CTO | 长期押注是通过 Data Intelligence 掌控元数据/目录层，还是作为 Unity Catalog 和 Polaris 之下的中立底座？ |
| 33 | Eng | Everpure 是否计划发布 MLPerf Storage v3.0 向量数据库工作负载的结果？ |
| 34 | PM | FlashBlade//EXA NVIDIA 认证的目标季度和级别（Enterprise 还是 NCP）是什么？目前有哪些项目提到其缺失？ |
| 34 | CTO | Purity 的数据服务能否在 BlueField-4 STX 控制器上运行？CMX 对 FlashBlade 是机会还是蚕食威胁？ |
| 34 | PM | FlashBlade AI 商机管道中，经由 NVIDIA 主导、Cisco/OEM 主导和直接新兴 GPU 云渠道的各占多少？ |
| 34 | Eng | 在 B300/Rubin 上，FlashBlade//S 和 //EXA 每个 SU 相对 SuperPOD 增强层有多少余量？什么最先成为瓶颈？ |
| 34 | CTO | 每一代 NVIDIA GPU 的重新认证投入多少工程能力？从 GPU 发布起需要多久？ |
| 35 | PM | 在新兴 GPU 云的比拼测试中，哪些多租户功能（每租户密钥、VRF 隔离、QoS 下限、计量导出、Terraform provider）仍在阻碍 FlashBlade//EXA？何时发布？ |
| 35 | PM | 在 50% 售出率下，计入数据缩减和 Evergreen//One 条款，新兴 GPU 云在 EXA 与 VAST 上的存储毛利率分别如何？ |
| 35 | Eng | EXA 数据节点软件能否运行在新兴 GPU 云自己认证的服务器 SKU 上？认证和支持需要什么？ |
| 35 | CTO | 除认证之外，Everpure 是否力求成为 NVIDIA 面向 GB300 和 Vera Rubin 的 NCP 参考设计中被点名的存储设计？STX 带来什么变化？ |
| 35 | CTO | 与 CoreWeave 的股权关系如何转化为部署容量？哪些 CoreWeave 层级或区域是与 VAST 并存的现实目标？ |
| 36 | CTO | 除 Meta 的 Tectonic 外，还有哪些超大规模云厂商内部文件系统面临类似的 HDD 每 TB 带宽瓶颈，使 DirectFlash 授权可以嵌入其 chunk/数据服务器之下？ |
| 36 | PM | 在超大规模场景下，以机架密度、功耗和写放大衡量，DirectFlash 授权相对 NVMe FDP 加标准 QLC SSD 的可辩护差异化是什么？ |
| 36 | Eng | 超大规模云厂商集成中，有多少是在其自研主机上运行的 DirectFlash 软件，又有多少是 Everpure 提供的非 NAND 模块硬件？ |
| 36 | PM | 对于缺少自研 Tectonic 级文件系统的新兴 GPU 云和二线云，是否有相对授权模式而言的产品路径（例如 FlashBlade//EXA）？ |
| 36 | CTO | Rapid Bucket 和 S3 Express One Zone 等按可用区、紧邻 GPU 的云存储层，是否改变了企业对本地 AI 存储 API（S3 over RDMA、gRPC 流式传输）的期望？ |
| 37 | PM | 是什么决定了 EXA 参加 MLPerf Storage v3.0 的哪些工作负载？v4.0 是否计划提交训练工作负载或 DFM 数据节点的结果？ |
| 37 | Eng | 在 30 节点检查点测试中，是什么限制了每数据节点的吞吐量（网卡、SSD、元数据）？基于 DFM 的数据节点会如何改变它？ |
| 37 | CTO | Everpure 是否（在内部或向客户）发布在标准带宽/容量比下按 RU、kW 和美元归一化的结果？是否会倡导 MLCommons 按这些指标排名？ |
| 37 | PM | 在由 POC 决定结果的新兴 GPU 云项目中，一线团队如何回应"VAST、WEKA 和 DDN 不需要 MLPerf"？ |
| 38 | Eng | FlashBlade//EXA 或 FlashArray//E 系统在空闲、以读为主负载和重建时，实测墙插功耗如何分解（NAND、控制器、DRAM、风扇、网卡）？ |
| 38 | PM | 在功率受限的 AI 项目中，客户要求的是 TB/W、每 kW 的 GB/s，还是都不要？在该指标上我们最常输给哪种竞争配置？ |
| 38 | CTO | HDD 容量到哪个点（例如 60 TB、100 TB HAMR）时，DirectFlash 相对磁盘的功耗与密度论点在冷数据层不再成立？届时如何应对？ |
| 38 | PM | 在不可缩减的 AI 数据集上，Evergreen//One 的每 TiB 瓦数保证表现如何？是否已扩展到 FlashBlade//EXA？ |
| 38 | CTO | Everpure 是否会对照 NVIDIA 参考架构规格，发布经审计的系统级 TB/W 和每 kW GB/s？目前是什么阻止了它？ |
| 39 | PM | Data Intelligence 订单中，有多大比例覆盖的数据不存放在 Everpure 上？是否单独定价和报告？ |
| 39 | Eng | Data Intelligence MCP 服务器如何处理用户身份（令牌交换还是服务账号）？权限撤销多快能传播生效？ |
| 39 | CTO | Everpure 打算与 OSI、Unity Catalog、Polaris 或 Purview 互操作，还是成为权威数据目录（catalog of record）？ |
| 39 | Eng | 分类是在写入路径上、由 SafeMode 快照还是由定期扫描触发？消耗多少控制器资源？ |
| 39 | PM | Data Intelligence 的买方是谁（存储管理员、CDO、CISO）？在覆盖非 Everpure 存储的项目中，阵列销售人员如何获得激励？ |
| 40 | PM | Everpure 如何调和其"修正后"的 IDC 份额与 IDC 公布的份额？内部规划使用哪一个？ |
| 40 | CTO | 在一份典型 AI 工厂物料清单中，共享存储目前占多大比例？未来两年推理/KV 缓存层将如何改变这一比例？ |
| 40 | PM | FY27 产品增长中，有多少来自每 TB 价格、多少来自出货容量？如果 NAND 合约价下跌 30%，增长会怎样？ |
| 40 | CTO | 超大规模云厂商的哪些存储功能在现实中可以授权（而非自建）？每部署 1 EB 的可触达支出是多少？ |
| 40 | PM | 战略团队对 AI 存储采用哪种 TAM 定义？是否包括超大规模云厂商自建部分？ |
| 41 | PM | 过去四个季度的 AI 存储丢单中，有多少输给了 VAST、WEKA 或 DDN？分别在哪个买方群体（新兴 GPU 云、AI 实验室、企业）？ |
| 41 | CTO | 我们把挑战者的哪些优势视为可复制（架构、认证），哪些视为结构性（NVIDIA 股权、新兴 GPU 云锚定客户）？这如何影响自建/合作/收购的选择？ |
| 41 | PM | 自 1Q26 以来，我们的 NAND 预付款头寸如何改变了相对纯软件厂商的赢单率或交付承诺？ |
| 41 | Eng | 要让 FlashBlade//EXA 获得 NCP 级别的 NVIDIA 认证需要什么？关键的门槛测试是什么？ |
| 41 | CTO | 如果 NVIDIA 的 STX/CMX 将 KV 缓存层标准化，存储厂商的差异化会转移到哪里？ |
| 42 | PM | 过去四个季度 EXA 对 VAST 的项目中，我们赢了多大比例？决定因素是架构、参考客户、认证，还是上层功能？ |
| 42 | Eng | 在比拼测试中，我们在客户 AI 数据集（检查点、token 化分片、图像）上测得的缩减比，与 VAST 相似性缩减在同一数据上的结果相比如何？ |
| 42 | CTO | 我们预期到 2028 年买方会要求存储提供 VAST AI OS 的哪些层（DataBase、DataEngine 触发器、AgentEngine）？哪些属于合作伙伴？ |
| 42 | PM | Everpure 的 NAND 供应地位如何转化为按成本价采购硬件的纯软件厂商无法匹敌的交付时间或价格承诺？ |
| 42 | CTO | BlueField-4 STX 让每家厂商都有了驻留在 DPU 上的控制器，在 GPU 服务器边缘的 KV 缓存上，Purity 还剩下什么差异化？ |
