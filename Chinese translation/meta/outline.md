# 大纲——字数预算与计划图表

> 📄 英文原文：[meta/outline.md](../../meta/outline.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

正文字数预算（按 `scripts/wordcount.py` 统计）。机器可读版本：`meta/chapters.yml`。总预算约 124,000 词。**★ = 规格书要求的标志性图表（§7）。**

## 第 0 部分——从这里开始（3,000）· `docs/00-start-here/`
| 章 | 文件 | 预算 | 计划图表 |
|---|---|---|---|
| 0.1 | `00a-how-to-use-this-atlas.md` | 1,500 | 学习路径流程图（2 小时 / 2 天 / 2 周）；深度标签表；阅读顺序图 |
| 0.2 | `00b-one-page-map.md` | 1,500 | 领域思维导图；"10 张图看懂 Everpure"（链接 + 10 张精简 Mermaid 图 / 缩略图） |

## 第 1 部分——存储基础（14,000）· `docs/01-storage-fundamentals/`
| 章 | 文件 | 预算 | 计划图表 |
|---|---|---|---|
| 1 | `01-what-storage-does.md` | 2,200 | ★ 块存储 vs 文件存储 vs 对象存储示意图（SVG）；数据生命周期流程图；主存储 / 二级存储 / 归档存储对比表 |
| 2 | `02-media-physics.md` | 2,500 | ★ 内存 / 介质层级金字塔（SVG：从 HBM 到磁带，含延迟、$/GB、容量）；NAND 单元剖面 SVG；SLC→PLC 对比表；HDD vs NAND $/TB 图表；3D NAND 层数图表 |
| 3 | `03-inside-an-ssd.md` | 2,400 | SSD 内部结构 SVG；FTL 映射流程图；垃圾回收 / 写放大算例图表；预留空间（OP）vs WAF 图表 |
| 4 | `04-performance-and-economics-metrics.md` | 2,400 | 延迟 / 队列深度曲线图；原始容量→可用容量→有效容量瀑布图；TCO 算例表；利特尔法则（Little's law）示意图 |
| 5 | `05-data-reduction.md` | 2,100 | 去重流程时序图；压缩流水线；DRR 合理性核查决策树；宣称值与实际值对比表 |
| 6 | `06-data-protection-and-resilience.md` | 2,400 | RAID / EC 布局示意图；快照（写时重定向）示意图；同步 vs 异步时序图；RPO/RTO 图表；勒索软件恢复流程 |

## 第 2 部分——协议与网络（12,000）· `docs/02-protocols-and-networking/`
| 章 | 文件 | 预算 | 计划图表 |
|---|---|---|---|
| 7 | `07-block-protocols.md` | 2,100 | ★ NVMe-oF 读、写时序图；SCSI→NVMe 演进时间线；传输层对比表；队列模型示意图 |
| 8 | `08-file-protocols.md` | 1,900 | NFSv3 vs pNFS 时序图；协议对比表；并行访问示意图 |
| 9 | `09-object-storage-and-s3.md` | 1,900 | S3 PUT/GET 时序图；分段上传（multipart upload）流程；一致性模型表；S3-over-RDMA 路径 |
| 10 | `10-datacenter-networking.md` | 2,100 | RDMA vs TCP 协议栈示意图；Ethernet vs InfiniBand 对比表；拥塞控制流程；DPU 位于数据路径中的示意图 |
| 11 | `11-gpu-data-path.md` | 2,000 | ★ GPU 直连路径 vs 传统路径（Mermaid + SVG）；GPU 空闲成本算例图表；NIXL/Magnum IO 层级栈 |
| 12 | `12-interfaces-and-emerging-tech.md` | 2,000 | PCIe 各代带宽图表；CXL 拓扑示意图；EDSFF 外形规格表；FDP/ZNS 数据放置示意图；Optane 时间线 |

## 第 3 部分——存储系统架构（17,500）· `docs/03-system-architecture/`
每个架构章节需包含：组件图 + 读、写时序图（★）、状态 / 元数据、扩展瓶颈、故障处理、优缺点表、最适合 / 最不适合的工作负载、真实产品、成本 / 运维影响。
| 章 | 文件 | 预算 | 计划图表 |
|---|---|---|---|
| 13 | `13-storage-stack.md` | 1,500 | ★ 逐层存储栈示意图；"智能位于哪一层"对比表；DAS→SAN/NAS→分布式→分解式时间线 |
| 14 | `14-scale-up-dual-controller.md` | 1,700 | 组件图；★ 写确认时序图（镜像 NVRAM）；读时序图；ALUA 路径示意图；不停机升级（NDU）状态图 |
| 15 | `15-scale-out-shared-nothing.md` | 1,700 | 集群示意图；★ 读 / 写时序图；一致性哈希环；数据再平衡流程 |
| 16 | `16-disaggregated-shared-everything.md` | 2,000 | DASE 集群 SVG；★ 读 / 写时序图；扩展图表（性能与容量解耦）；对比表 |
| 17 | `17-parallel-file-systems.md` | 1,600 | Lustre 组件图；★ 读 / 写时序图；条带化示意图；产品对比表 |
| 18 | `18-object-storage-architecture.md` | 1,500 | 对象存储集群示意图；★ PUT/GET 时序图；跨站点纠删码示意图 |
| 19 | `19-software-defined-and-hci.md` | 1,400 | HCI vs SDS vs 一体机示意图；EBS 式块存储服务示意图；商业模式对比表 |
| 20 | `20-distributed-systems-fundamentals.md` | 1,500 | Raft 时序图；持久性（几个 9 vs MTTDL）图表；故障域示意图；一致性对比表 |
| 21 | `21-metadata.md` | 1,300 | inode / 命名空间示意图；小文件 IOPS 图表；元数据扩展策略表 |
| 22 | `22-control-planes.md` | 1,000 | 控制平面 vs 数据平面示意图；遥测 / AIOps 闭环；API 自动化时序图 |
| 23 | `23-consumption-models.md` | 1,100 | 资本支出（capex）vs STaaS 现金流图表；模式对比表；架构与商业模式反馈示意图 |
| 24 | `24-architecture-decision-matrix.md` | 1,200 | ★ 架构 × 工作负载热力表；★ 决策树流程图；四象限图 |

## 第 4 部分——Everpure（10,000）· `docs/04-everpure/`
| 章 | 文件 | 预算 | 计划图表 |
|---|---|---|---|
| 25 | `25-company-history-and-strategy.md` | 1,800 | ★ 公司时间线 2009–2026；并购记录表；战略演进流程图 |
| 26 | `26-purity-and-directflash.md` | 2,200 | ★ Purity 架构示意图；★ DirectFlash vs 通用 SSD 软硬件栈（SVG）；DFM 容量路线图图表 |
| 27 | `27-flasharray-and-flashblade.md` | 2,200 | ★ FlashArray/FlashBlade 产品谱系树；按工作负载定位表；FlashBlade//EXA 架构示意图 |
| 28 | `28-platform-and-software.md` | 2,000 | 平台层级示意图；Evergreen 模式流程；Fusion/Pure1 控制平面示意图；1touch 投资逻辑示意图 |
| 29 | `29-hyperscaler-ecosystem-financials.md` | 1,800 | ★ 生态系统网络图；收入图表；订阅 / ARR 图表；毛利率驱动因素表 |

## 第 5 部分——AI 存储（20,000）· `docs/05-ai-storage/`
| 章 | 文件 | 预算 | 计划图表 |
|---|---|---|---|
| 30 | `30-ai-data-pipeline.md` | 2,000 | ★ 标注各阶段 I/O 模式的 AI 流水线；I/O 模式表；数据量漏斗图 |
| 31 | `31-training-storage.md` | 2,200 | 检查点大小图表（70B/405B/1T）；吞吐量计算表；检查点保存时序图；异步检查点示意图 |
| 32 | `32-inference-and-kv-cache.md` | 2,300 | ★ KV 缓存分层示意图；KV 大小算例图表；Dynamo/KVBM/NIXL 流程；token 经济学对比表 |
| 33 | `33-rag-vector-lakehouse.md` | 2,000 | RAG 时序图；向量索引对比表；湖仓（lakehouse）层级示意图 |
| 34 | `34-nvidia-ecosystem.md` | 2,000 | AI Data Platform 参考架构示意图；认证阶梯；厂商认证对比表 |
| 35 | `35-ai-factories-and-neoclouds.md` | 1,900 | AI 工厂机架布局 SVG；新兴 GPU 云（neocloud）采购标准表；neocloud 与厂商关系图 |
| 36 | `36-hyperscaler-ai-storage.md` | 2,000 | Colossus / Tectonic 示意图；AWS AI 存储栈；自建 vs 采购矩阵 |
| 37 | `37-reading-benchmarks.md` | 2,000 | MLPerf Storage 方法示意图；基准测试对比表；"刷分"核查清单流程图 |
| 38 | `38-power-and-density.md` | 1,800 | TB/W 图表；机架密度对比；电力约束流程 |
| 39 | `39-agentic-ai-and-data-intelligence.md` | 1,800 | 智能体（agentic）数据访问时序图；数据智能层级栈；厂商趋同四象限图 |

## 第 6 部分——行业与竞争（28,500）· `docs/06-industry-and-competition/`
| 章 | 文件 | 预算 | 计划图表 |
|---|---|---|---|
| 40 | `40-market-structure.md` | 2,000 | 市场规模图表；厂商份额图表；细分市场图 |
| 41 | `41-why-ai-native-vendors-won.md` | 2,500 | 市场牵引力驱动因素因果图；论点强度表；传统厂商盲点流程 |
| 42 | `42-vast-data.md` | 4,000 | ★ VAST 架构示意图；I/O 全流程时序图；★ 融资 / 估值时间线 + 图表；产品栈示意图 |
| 43 | `43-weka.md` | 3,500 | ★ WEKA 架构示意图；数据路径时序图；★ 融资时间线 + 图表；AMG 分层示意图 |
| 44 | `44-ddn.md` | 3,500 | ★ DDN 架构（EXAScaler + Infinia）；★ 里程碑时间线；产品对比表 |
| 45 | `45-head-to-head.md` | 2,500 | ★ 四方架构对比；多维度矩阵；雷达式图表；"谁赢下哪类订单"对比表 |
| 46 | `46-incumbents.md` | 3,000 | 概况表 ×6；传统厂商 AI 战略四象限图；产品组合图 |
| 47 | `47-other-challengers.md` | 2,000 | 挑战者分布图；对比表；Hammerspace 全局命名空间示意图 |
| 48 | `48-media-suppliers-and-nand-cycle.md` | 2,000 | NAND 供应商份额图表；NAND 价格周期图表；周期 → 阵列厂商毛利率传导流程 |
| 49 | `49-competitive-matrices.md` | 1,500 | ★ 四象限图 ×3；热力表 |
| 50 | `50-diligence-framework.md` | 2,000 | 尽职调查流程；核查清单表；评分卡模板 + 算例 |

## 第 7 部分——历史与未来（10,000）· `docs/07-history-and-future/`
| 章 | 文件 | 预算 | 计划图表 |
|---|---|---|---|
| 51 | `51-history-of-storage.md` | 2,500 | ★ 历史时间线 1956–2026；各时代经验教训表；$/GB 长期走势图 |
| 52 | `52-history-of-flash.md` | 2,300 | 闪存成本曲线图；拐点时间线；HDD/SSD 交叉点图表 |
| 53 | `53-future-trends.md` | 3,000 | ★ 未来趋势雷达图（SVG）；趋势评分卡表；时间节点时间线 |
| 54 | `54-strategic-option-map.md` | 2,200 | ★ 分层技术栈战略图；自建 / 收购 / 合作矩阵；选项评估流程 |

## 第 8 部分——对话工具包（9,000）· `docs/08-conversation-toolkit/`
| 章 | 文件 | 预算 | 计划图表 |
|---|---|---|---|
| 55 | `55-talking-with-pms.md` | 1,600 | 产品经理思维模型示意图；按产品线划分的问题集表；会前准备流程 |
| 56 | `56-talking-with-engineering-and-cto.md` | 1,600 | 架构评审流程；高质量回答 / 危险信号对比表；可信度阶梯 |
| 57 | `57-question-bank.md` | 1,800 | 主题 × 受众覆盖表；标签图例；150 个问题 |
| 58 | `58-explain-in-30-seconds.md` | 1,500 | 主题图；按主题划分的 66 条一句话解释 |
| 59 | `59-self-test-flashcards.md` | 1,500 | 闪卡分布图表 / 表格；200 张 `<details>` 闪卡 |
| 60 | `60-cheat-sheets.md` | 1,000 | 缩略语速查表；★ 协议海报；★ 架构海报；★ 产品阵容海报 |
