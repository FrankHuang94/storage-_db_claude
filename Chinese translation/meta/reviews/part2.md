# 审阅报告：第 2 部分（第 7–12 章，协议与网络）

> 📄 英文原文：[meta/reviews/part2.md](../../../meta/reviews/part2.md) · 本文为简体中文参考译本，如有出入以英文原文为准。

**审阅范围**：`docs/02-protocols-and-networking/07-block-protocols.md` 至 `12-interfaces-and-emerging-tech.md`，以及各章的 staging 文件。审阅日期 2026-11-01。

## 摘要

**核查内容**：
- 每一张时序图，逐个箭头核对：SCSI/iSCSI/FCP、NVMe/PCIe doorbell（门铃寄存器）、基于 RDMA 和 TCP 的 NVMe-oF 读写（包括 in-capsule data（胶囊内数据）、R2T 和 C2HData）、NFSv3 路径、pNFS 的 OPEN/LAYOUTGET/GETDEVICEINFO、带 SigV4 的 S3 PUT/GET、分段上传（multipart upload）、ECN/DCQCN/PFC，以及传统路径与 GDS 的 GPU 数据路径。
- 标准日期与 RFC 编号：NVMe 1.0、NVMe-oF 1.0、TP 8000、FC-NVMe、RFC 1813/3530/5661/8881/7862/8435/8166/8267、PCIe 3.0–8.0、CXL 1.0–4.0、802.3bs/ck/df/dj、UEC 1.0、ZNS 与 FDP，以及 Optane 的各个里程碑。
- NVIDIA 命名：GDS/cuFile、Magnum IO、NIXL、Dynamo/KVBM、cuObject、Spectrum-X、BlueField-3/4、STX/CMX。这些与第 34 章一致。
- Everpure 与竞争对手的协议相关主张。
- 全部算术均重新计算：Little 定律下的 IOPS、S3 小对象开销与 LIST 耗时、分段大小、1,024 GPU 网络算例、每个 400G 端口的 DRAM 流量、PFC 缓冲余量（headroom）、GPU 空闲成本 CSV（全部 12 行）、tokens/s、KV 缓存大小、回弹缓冲区（bounce buffer）的 DRAM 负载，以及 PCIe x4/x16 带宽。

**算术**：正确，仅有一处舍入修正（0.97 → 0.96 M tokens/s）和一处要点速览中价格区间的不一致。第 11 章图表 CSV 可精确复现：停顿比例 × 1,024 × 8,760 小时 × 价格。

**时序图**：没有方向错误的箭头。基于 RDMA 的读取是目标端向主机缓冲区执行 RDMA WRITE，写入则是目标端执行 RDMA READ。我补充了工程师会期待的精确细节：
- iSCSI 的 immediate/unsolicited data（立即/非请求数据）和 FC 的 first burst（首次突发）可以跳过 R2T。
- NVMe/TCP 最后一个 C2HData PDU 上的成功标志使目标端可以省去响应胶囊。
- 胶囊内数据的上限由目标端通告。
- FC-NVMe 的队列映射到关联（association）内的连接，而不是交换（exchange）。
- 图 7.5 现写为 "mirrored or shared NVRAM"（"镜像或共享的 NVRAM"），与第 3a 部分对 FlashArray 的修正一致。

**网络限制**：WebFetch 被拒绝访问 docs.portworx.com、ithome.com.tw 和 nvidianews.nvidia.com（按 D13，sec.gov 和厂商网站也是如此）。来自这些网站的事实均依据搜索结果引用，脚注中已注明。

**结论**：
- 第 7 章：轻微修正（竞争对手表格中的 VERIFY 已解决，图注矛盾）。
- 第 8 章：轻微修正（FlashBlade//S 的 RDMA/GDS 状态，VAST pNFS）。
- 第 9 章：轻微修正（VERIFY 已解决）。
- 第 10 章：轻微修正（incast 的措辞，历史方面的 VERIFY）。
- 第 11 章：轻微修正（Everpure GDS 状态补充来源，日期已解决）。
- 第 12 章：实质性修正（CXL 4.0 带宽错误、"唯一拥有自有闪存模块的厂商"的夸大说法、E1.S 功耗）。

**修改后的 QA**：六章全部通过 `qa_report.py`。`lint_mermaid.sh` OK（23 个代码块）。`check_links.py --allow-planned` 报告 0 个失效链接。字数为预算的 116–119%。六章的脚注都已按首次引用顺序重新编号。审阅之前有几章的脚注顺序是乱的；除编号外，定义和正文均未改动。

## 发现的问题

| 章 | 原文主张 / 段落 | 问题 | 已采取的修正 | 状态 |
|---|---|---|---|---|
| 7 | 要点速览说 "two layers"（"两层"）；核心概念说三层 | 内部不一致 | 要点速览改为 "command set riding a transport (plus fabric services)"（"命令集运行在传输层之上（外加网络结构服务）"） | 已修复 |
| 7 | "RoCE (NVMe over RDMA on Ethernet)"（"RoCE（以太网上的 NVMe over RDMA）"） | RoCE 是 RDMA 传输，不是 NVMe-over-RDMA | 改为 "NVMe over RoCE (RDMA on Ethernet)"（"NVMe over RoCE（以太网上的 RDMA）"） | 已修复 |
| 7 | "many HBAs still serialize"（"许多 HBA 仍然串行处理"） | 已过时：scsi-mq 和多队列 FC/SAS HBA 已经存在 | 改写为每 LUN 队列深度和命令路径的限制 | 已修复 |
| 7 | 图 7.1 图注：写入总要多一次往返 | iSCSI 的 ImmediateData/InitialR2T=No 和 FCP 的 first burst 可以跳过 R2T | 补充限定说明 | 已修复 |
| 7 | 队列对映射到 "FC exchange context"（"FC 交换上下文"） | FC-NVMe 将每个队列映射到关联内的一条连接；exchange 是按每次 I/O 划分的 | 已修正 | 已修复 |
| 7 | NVMe/TCP 读路径 | 遗漏了 C2HData 的 SUCCESS 标志；"large writes"（"大块写入"）应为 "writes above the in-capsule limit"（"超过胶囊内数据上限的写入"） | 已补充 | 已修复 |
| 7 | 图 7.5 "persist mirrored copy"（"持久化镜像副本"） | 与第 14 章所述 FlashArray 共享机箱 NVRAM 相矛盾 | 改为 "persist to mirrored or shared NVRAM"（"持久化到镜像或共享的 NVRAM"）；图注补充胶囊内数据大小上限和 FC first burst | 已修复 |
| 7 | NetApp ONTAP NVMe/RoCE [VERIFY] | NetApp KB：ONTAP 只支持 NVMe/FC 和 NVMe/TCP | 已替换，并附 E-Series/EF 的限定说明；ONTAP 9.4 起支持 NVMe/FC，引用 NetApp 文档 | 已修复 |
| 7 | Dell PowerStore RoCE / NVMe/FC [VERIFY] | 未找到 RoCE 支持（Dell 选择了 NVMe/TCP）；NVMe/FC 于 PowerStoreOS 2.0 引入，2021 年 4/5 月 | 已替换并附引用 | 已修复 |
| 7 | Purity//FA 6.4.2 NVMe/TCP [VERIFY: GA date] | 来源互相矛盾（一份摘要写 2022-02-07，可能是笔误） | 现写为 "2022"，VERIFY 范围收窄 | 已标记 |
| 7 | 图 7.7 图注 "protocol coverage is at parity"（"协议覆盖面持平"） | 表中显示只有 Everpure 提供 RoCE | 图注已修正 | 已修复 |
| 7 | NVMe 队列、NVMe 1.0/oF 1.0/TP 8000/vSphere 7U3/RFC 3720/FC-PH/SCSI-1 的日期；Little 定律计算 | 已核查 | 无 | 已核实 |
| 8 | FlashBlade//S "NFS-over-RDMA status [VERIFY]"（"NFS-over-RDMA 状态 [VERIFY]"） | iThome 报道 FlashBlade//S 自 Purity//FB 4.3.4（2023 年 10 月）起支持基于 NFS/RDMA 的 GDS；//E 不支持 | 表格已更新，标注为仅见于搜索摘要 | 已修复 / 已标记 |
| 8 | VAST pNFS [VERIFY] | VAST NFS 客户端文档 v4.5（2026 年 4 月）列出的是 NFSv3/v4.1 多路径，而非 pNFS | 用文档引用替换 VERIFY，仍保留 "no public support found"（"未找到公开支持"）的审慎表述 | 已修复 |
| 8 | Linux 客户端 "whose upstream maintainer is Hammerspace's CTO"（"其上游维护者是 Hammerspace 的 CTO"） | 夸大：Myklebust 是该客户端的共同维护者之一 | 改为 "one of whose upstream maintainers"（"其上游维护者之一"） | 已修复 |
| 8 | 选项 "whether EXA's data leg delivers GDS"（"EXA 的数据通路能否提供 GDS"） | Portworx 文档（搜索摘要）描述了 EXA 上基于 RDMA NFS 的 GDS | 改写为：待解问题是 NVIDIA 认证和实测数据 | 已修复 |
| 8 | "NetApp agreed to buy PEAK:AIO"（"NetApp 同意收购 PEAK:AIO"） | 这只是宣布的收购意向，尚未完成 | 已改写 | 已修复 |
| 8 | NFS RFC 编号与日期、nconnect 16 / Linux 5.3、44 条连接算例、pNFS 图 | 已核查 | 无 | 已核实 |
| 9 | 要点速览将 MinIO 列为 cuObject 采用者 | MinIO 发布的是自己的 S3-over-RDMA 实现（2024 年 11 月） | 将 cuObject 采用者与 MinIO 分开 | 已修复 |
| 9 | MinIO 一致性 [VERIFY] | MinIO 博客声明了严格的写后读和写后列举一致性 | 已引用并标注为公司自述 | 已修复 |
| 9 | NVIDIA RDMA for S3 日期 [VERIFY] | 博客约 2025-11-13（报道日期为 2025-11-14）；承诺于 2026 年 1 月通过 CUDA 正式发布 | 正文和脚注中均已解决 | 已修复 |
| 9 | FlashBlade S3 over RDMA [VERIFY: GA] | Pure 曾表示 "later this year"（"今年晚些时候"，指 2025 年），五个机箱约 250 GB/s 为初步数据；未找到 GA 公告 | 表格表述更具体，保留 VERIFY | 已标记 |
| 9 | 价格、LIST 与 PUT 开销、1 PB 图表、58 个月、分段 650 MB / 8.5 分钟、强一致性 2020-12-01、Express One Zone 降价、S3 Vectors 规模 | 已重新计算或核查 | 无 | 已核实 |
| 9 | 2024 年 Pi Day "350 T objects, 100 M req/s"（"350 万亿个对象，每秒 1 亿次请求"） | 仍仅见于搜索摘要；二手来源引用的 2025 年数字约为 500 万亿个对象和每秒 2 亿次请求 | 保留为注明日期的 2024 年数字 | 已标记 |
| 10 | "many-to-few on writes and few-to-many on reads. That shape, called incast"（"写入时多对少、读取时少对多，这种形态称为 incast"） | 读 incast 是多个存储节点对一个客户端端口，而非"少对多" | 已重写；"handful of ports"（"少数几个端口"）量化为 2–3 个 | 已修复 |
| 10 | PFC 缓冲余量 "round-trip plus reaction ≈ 1 µs"（"往返加反应时间 ≈ 1 µs"） | 仅 100 m 的 RTT 就已是 1 µs | 改写为下限；算术结果不变 | 已修复 |
| 10 | "Quantum-X800 was the first switch on 200G SerDes"（"Quantum-X800 是首款采用 200G SerDes 的交换机"） | 缺乏依据的最高级表述 | 改为 "among the first switches of that generation"（"该代最早的交换机之一"） | 已修复 |
| 10 | Mellanox 交易 [VERIFY]；UEC 成立 [VERIFY] | 2019-03-11，US$6.9B，2020 年 4 月完成；UEC 成立于 2023-07-19，为 LF/JDF 项目，九家创始成员 | 已解决并引用 | 已修复 |
| 10 | Dell'Oro ">2/3 in 2025, ~20% two years earlier"（"2025 年超过 2/3，两年前约 20%"） | 4Q25 新闻稿就该季度和全年都给出了这一说法（搜索摘要） | 脚注已加注；staging 表述更具体 | 已核实（搜索摘要） |
| 10 | 表 10.3 "fully aligned with NVIDIA"（"与 NVIDIA 完全对齐"） | 措辞接近摇旗呐喊 | 改为 "closely aligned"（"紧密对齐"） | 已修复 |
| 10 | 802.3dj "still in ballot Oct 2026"（"2026 年 10 月仍在投票阶段"） | 已确认：SA 再循环投票于 2026 年 6 月结束；预计约 2026 年 12 月批准 | 无 | 已核实 |
| 10 | DRAM 流量和 819/102 Tb/s 网络算术；802.3bs/ck/df 日期；BlueField-3/4 规格；UEC 1.0 日期 | 已核查 | 无 | 已核实 |
| 11 | 要点速览 "US$2–6 per H100-hour → US$0.57–1.75/s" | $1.75 对应的是 $6.16 | 改为 "US$2.00–6.16" | 已修复 |
| 11 | 0.97 M tokens/s | 1,024 × 989e12 × 0.4 ÷ 4.2e11 = 0.964 M | 改为 0.96 M | 已修复 |
| 11 | Lambda US$3.99 [VERIFY] | 价格追踪网站一致为 3.99；Lambda 自己的页面曾显示 2.99 | VERIFY 更加具体 | 已标记 |
| 11 | FlashBlade//S "GDS claimed"（"宣称支持 GDS"） | 现已有来源（iThome，Purity//FB 4.3.4，2023 年 10 月），但未出现在 NVIDIA 发行说明表中 | 表格已更新 | 已修复 / 已标记 |
| 11 | EXA GDS 认证 [VERIFY] | Portworx 文档记载了 EXA 上的 GDS；第 34 章称 2026 年 3 月 NVIDIA 验证仍在进行中 | 表格交叉链接至第 34 章 | 已修复 |
| 11 | GPUDirect RDMA 年份 [VERIFY]；Dynamo 日期 [VERIFY] | Kepler/CUDA 5.0，2012 年（NVIDIA 文档）；Dynamo 2025-03-18（NVIDIA 投资者关系） | 已解决；Pure GDS 历史现注明 2023 年 10 月交付 | 已修复 |
| 11 | "idle time comes mostly from interruptions"（"空闲时间主要来自中断"） | 夸大 | 改为 "a large share"（"很大一部分"） | 已修复 |
| 11 | GPU 空闲 CSV（12 行）、检查点 1.12 TB / 56 s / 3.1%、US$0.89 M 节省、KV 320 KiB / 10.7 GB、回弹缓冲区 400 vs 614 GB/s | 已重新计算 | 无 | 已核实 |
| 12 | "CXL 4.0 ... up to 768 GB/s per direction on x16"（"CXL 4.0……x16 每方向最高 768 GB/s"） | **错误**。128 GT/s 下 x16 每方向为 256 GB/s；768 GB/s 来自捆绑端口 | 正文和数字表已修正 | 已修复 |
| 12 | E1.S "up to 25 W (15 mm)"（"最高 25 W（15 mm）"） | 25 W 是 25 mm 散热片版本；5.9 mm 约 12 W，15 mm 引用值为 20–25 W | 改为 "~12 W (5.9 mm) to ~25 W (25 mm)"（"约 12 W（5.9 mm）至约 25 W（25 mm）"） | 已修复 |
| 12 | 表 12.3 "Everpure is the only major vendor that owns the flash module"（"Everpure 是唯一拥有自有闪存模块的主要厂商"） | **夸大**。IBM 自行设计 FlashCore Module（带模块内控制器） | 改写为：唯一一家其模块没有盘级 FTL 的厂商；同时在计算存储部分注明 IBM FCM | 已修复 |
| 12 | ZNS [VERIFY]；CXL 1.0–3.1 [VERIFY]；Pure DirectMemory/Optane [VERIFY]；Micron 退出 / Lehi 工厂出售 | TP4053 2020 年 6 月；CXL 1.0 2019 年 3 月、2.0 2020 年 11 月、3.0 2022 年 8 月；DirectMemory Cache 使用 Optane SSD（2019）；Micron 于 2021 年 3 月退出，2021 年 6 月以 US$900M 将 Lehi 工厂出售给 TI | 已解决并引用；仅 CXL 3.1 的具体日期和 2015–2019 年 Optane 日期仍为 VERIFY | 已修复 |
| 12 | PCIe 带宽表和图表（x4：3.9/7.9/15.8/29.5/59/118 GB/s；x16：128/256/512 GB/s）、flit 236/256、708 GB/s 对 100 GB/s、WAF 4、PCIe 发布日期 | 已重新计算或核查 | 无 | 已核实 |

## 未解决事项 / 分歧

- **第 7 章**：Purity//FA 6.4.2（NVMe/TCP）的确切 GA 月份。来源在 2022 年和 2023 年之间互相矛盾。
- **第 7 章**：Crehan Research 的 FC +6%（2025）仍仅见于搜索摘要。
- **第 8 章 / 第 11 章**：FlashBlade//S 对 GDS/NFS-over-RDMA 的支持（Purity//FB 4.3.4，2023 年 10 月）依据的是 iThome 的一份搜索摘要。它未出现在 NVIDIA GDS 发行说明的合作伙伴表中。应由能访问 Everpure 发行说明的人确认。这也关系到第 34 章 "FlashBlade//S holds the full set"（"FlashBlade//S 具备全套能力"）的说法。
- **第 8 章 / 第 11 章**：FlashBlade//EXA 的 GDS 依据的是 Portworx 文档的一份搜索摘要。EXA 的 NVIDIA 认证尚未公开。一份 SPECstorage AI_IMAGE 披露（2026 年 1 月，Purity//FB 4.6.4）描述了到数据节点的支持 RDMA 的 pNFS。如有需要，可在第 16/27 章中引用。
- **第 9 章**：FlashBlade S3-over-RDMA 的 GA 状态。Pure 在 2025 年承诺 "later this year"（"今年晚些时候"）；截至 2026-11-01 未找到 GA 公告。若仍未 GA，第 11 章 "Everpure has announced it"（"Everpure 已宣布"）的表述是准确的，但不应升级为 "ships"（"已出货"）。
- **第 10 章**：Everpure 的 Spectrum-X 读 +25% / 写 +23% 数字在所有搜索中都未找到。保留 VERIFY 或删除这些数字。MetaRoCE（2026 年 8 月）仍未核实。
- **第 11 章**：Lambda 标价（US$3.99 还是 US$2.99）仍未解决。由于中档价格仅为示意，这不影响结论。
- **第 12 章**：最大已出货 E1.S/E3.S 容量、U.2 功耗等级、CXL 3.1 的发布日期，以及 2015–2019 年 Optane 日期仍为 VERIFY。E1.S 尺寸（33.75 × 118.75 mm）看起来是外壳尺寸；PCB 为 31.5 × 111.49 mm。我未作改动。
