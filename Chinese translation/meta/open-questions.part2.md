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
