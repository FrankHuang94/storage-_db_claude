# 翻译指南（Translation guide for the Simplified Chinese reference edition）

> 本文件是简体中文参考译本的翻译规范，供所有译者遵循。This file is the shared brief for everyone translating the atlas into Simplified Chinese.

## 1. 目标与定位 / Goal
- 产出一份**总体准确、通顺专业**的简体中文**参考译本**，覆盖英文原版的全部内容。译文仅供参考；如有出入，以英文原文为准。无需逐句校对式的"精度核查"，但**事实、数字、名称、日期一律不得改动**。
- 读者：企业发展/战略岗位的专业人士（CFA、MBA、法律背景、半导体并购经验）。语气：资深分析师向高管做简报——简洁、具体、专业，类似券商研报或咨询报告，不要口语化或营销腔。

## 2. 文件与结构 / Files and structure
- 译本根目录为仓库中的 `Chinese translation/`，**目录结构与英文原版完全镜像**：英文 `docs/03-system-architecture/16-disaggregated-shared-everything.md` → 中文 `Chinese translation/docs/03-system-architecture/16-disaggregated-shared-everything.md`（文件名保持英文不变，以便相对链接继续有效）。
- 图片已复制到 `Chinese translation/docs/assets/`，所以章节中的图片链接（如 `../assets/diagrams/ch16-dase-cluster.svg`）**保持不变**。图片本身（SVG/图表）仍为英文，不翻译；只翻译替代文本（alt text）和图注。
- **每个译文文件都必须注明英文原文出处**：在 H1 标题之后空一行，插入一行引用块（相对路径链接回英文原文件）：
  - 章节（`Chinese translation/docs/<part>/<file>.md`）：
    `> 📄 英文原文：[docs/<part>/<file>.md](../../../docs/<part>/<file>.md) · 本文为简体中文参考译本，如有出入以英文原文为准。`
  - `Chinese translation/docs/glossary.md`：链接 `../../docs/glossary.md`
  - `Chinese translation/README.md` 等根目录文件：链接 `../README.md`（依此类推）
  - `Chinese translation/meta/<file>.md`：链接 `../../meta/<file>.md`；`meta/research/`、`meta/reviews/` 下的文件：`../../../meta/research/<file>.md` 等。
  - 若原文没有 H1，则把引用块放在文件第一行。

## 3. 必须原样保留的内容 / Keep exactly as-is
- **所有数字、单位、日期、百分比、金额、版本号**（例如 877.5 GiB/s、US$1.17B、2026-04-17、FY27、Q2 FY27）。不要换算单位，不要把 "US$1.17B" 改成"11.7 亿美元"——可以写成"11.7 亿美元（US$1.17B）"，但原始写法必须保留。最稳妥做法：直接保留原写法。
- **公司名、产品名、人名、标准与协议名**保留英文：Everpure、Pure Storage、FlashArray、FlashBlade//EXA、Purity//FA、DirectFlash、Evergreen//One、Portworx、Fusion、Pure1、VAST Data、WEKA、NeuralMesh、DDN、EXAScaler、Infinia、NVIDIA、BlueField-4、Dynamo、NIXL、GPUDirect Storage、NVMe-oF、RoCEv2、pNFS、S3、MLPerf Storage、Lustre 等。
- **缩略语**保留英文（SSD、FTL、WAF、RAID、EC、RPO/RTO、TCO、DRR、KV cache、HBM、CXL、PCIe、EDSFF、QLC、TLC、DASE、HCI、SDS、ARR、RPO、GAAP 等）；首次出现时可在中文后加括号，如"写放大（WAF）"。
- **Markdown 结构**：标题层级、列表、表格的行列数、代码块、`<details>`/`<summary>` 结构、空行（`<details>` 内部的空行必须保留）。
- **脚注**：脚注编号 `[^12]` 与正文中的位置保持不变。`## Sources` 下的脚注定义（出版方、标题、日期、URL、retrieved 日期）是书目数据，**原样保留英文**，不翻译。
- **链接目标**（括号里的 URL/相对路径）不变；只翻译链接文字（如 "Chapter 27" → "第 27 章"，"Ch 26" → "第 26 章"）。
- **`[VERIFY: …]` 标记**：保留 `[VERIFY:` 关键字和方括号，把说明文字译成中文，例如 `[VERIFY: 仅见于搜索摘要]`。
- 代码块（bash 命令等）原样保留，只可翻译 `#` 注释。

## 4. 章节模板标题的统一译法 / Fixed translations for template headings
| English | 中文 |
|---|---|
| TL;DR | 要点速览（TL;DR） |
| Why this matters for Everpure strategy | 对 Everpure 战略的意义 |
| Core concepts | 核心概念 |
| How Everpure approaches it vs. competitors | Everpure 的做法与竞争对手对比 |
| History and trajectory | 历史与发展轨迹 |
| Numbers that matter | 关键数字 |
| Conversation playbook | 对话手册 |
| Going deeper (optional, L3 pointers) | 深入阅读（可选，L3 指引） |
| Key terms | 关键术语 |
| Sources | 资料来源 |
| Business model & financials | 商业模式与财务 |
| Customers & go-to-market | 客户与市场进入策略 |
| Why it gained traction | 为何获得市场牵引力 |
| Risks & open questions | 风险与待解问题 |
| Strategic relevance to Everpure | 对 Everpure 的战略意义 |

页首信息块：`> **深度：** L2 · **阅读时间：** 约 10 分钟 · **最后核实：** 2026-11-01` 与 `> **前置阅读：** …`。
图注/表注：`*图 16.1 — …*`、`*表 16.2 — …*`；`Data: \`data/…csv\`` → `数据：\`data/…csv\``。
对话手册内：`3 questions for a PM` → "向产品经理提的 3 个问题"；`strong answer` → "高质量回答"；`Don't say this` → "**不要这样说：**"。
标签：company-stated → 公司自述；reported by press → 媒体报道；estimated → 估算；illustrative → 示意；worked example → 算例；atlas's judgment → 本图谱的判断。
深度标签 L1/L2/L3 保留：L1 词汇、L2 机制、L3 实现。

## 5. 常用术语对照 / Terminology
| English | 中文 |
|---|---|
| storage array / array | 存储阵列 / 阵列 |
| block / file / object storage | 块存储 / 文件存储 / 对象存储 |
| primary / secondary / archive storage | 主存储 / 二级存储 / 归档存储 |
| controller | 控制器 |
| dual-controller, scale-up | 双控制器、纵向扩展（scale-up） |
| scale-out, shared-nothing | 横向扩展（scale-out）、无共享（shared-nothing） |
| disaggregated shared-everything (DASE) | 分解式全共享架构（DASE） |
| parallel file system | 并行文件系统 |
| metadata / namespace / inode | 元数据 / 命名空间 / inode |
| flash, NAND, SSD | 闪存、NAND、固态硬盘（SSD） |
| flash translation layer (FTL) | 闪存转换层（FTL） |
| garbage collection | 垃圾回收 |
| write amplification | 写放大 |
| over-provisioning | 预留空间（OP） |
| endurance / retention | 耐久度 / 数据保持 |
| raw / usable / effective capacity | 原始容量 / 可用容量 / 有效容量 |
| data reduction, dedupe, compression | 数据缩减、重复数据删除（去重）、压缩 |
| thin provisioning | 精简配置 |
| erasure coding | 纠删码 |
| snapshot / clone / replication | 快照 / 克隆 / 复制 |
| synchronous / asynchronous replication | 同步复制 / 异步复制 |
| ransomware / immutability | 勒索软件 / 不可变性 |
| latency / throughput / IOPS / tail latency | 延迟 / 吞吐量 / IOPS / 尾延迟 |
| queue depth | 队列深度 |
| failure domain / blast radius | 故障域 / 爆炸半径（影响范围） |
| durability / availability | 持久性 / 可用性 |
| consensus | 共识 |
| control plane / data plane | 控制平面 / 数据平面 |
| fleet management | 集群（设备群）管理 |
| consumption model, STaaS, subscription | 消费模式、存储即服务（STaaS）、订阅 |
| non-disruptive upgrade | 不停机升级 |
| checkpoint / checkpointing | 检查点 / 检查点保存 |
| training / inference | 训练 / 推理 |
| KV cache, prefill, decode | KV 缓存、预填充（prefill）、解码（decode） |
| time to first token (TTFT) | 首 token 延迟（TTFT） |
| context window / context memory | 上下文窗口 / 上下文内存 |
| RAG, vector database, embedding | 检索增强生成（RAG）、向量数据库、嵌入向量 |
| lakehouse | 湖仓（lakehouse） |
| AI factory | AI 工厂 |
| neocloud | 新兴 GPU 云（neocloud） |
| hyperscaler | 超大规模云厂商 |
| design win | 设计导入（design win） |
| incumbent / challenger | 传统厂商（在位者） / 挑战者 |
| go-to-market (GTM) | 市场进入策略（GTM） |
| total addressable market (TAM) | 潜在市场规模（TAM） |
| gross margin, non-GAAP | 毛利率、非 GAAP |
| annual recurring revenue (ARR) | 年度经常性收入（ARR） |
| remaining performance obligations (RPO) | 剩余履约义务（RPO） |
| free cash flow | 自由现金流 |
| steelman | 最强版本论证（steelman） |
| benchmark | 基准测试 |
| peer-reviewed | 经同行评审 |
| reference architecture | 参考架构 |
| certification | 认证 |
| due diligence | 尽职调查 |
| build / buy / partner | 自建 / 收购 / 合作 |
| semiconductor bridge | 半导体类比 |

译者若遇到表中没有的术语：首次出现用"中文（English）"，之后用中文。

## 6. Mermaid 图表 / Mermaid diagrams
- **翻译节点标签、连线文字、标题、图例**；不得改动图类型关键字（`flowchart`、`sequenceDiagram`、`timeline`、`mindmap`、`quadrantChart`、`xychart-beta` 等）、节点 ID、`participant` 别名、箭头语法、坐标数值。
- 含中文或标点的标签请用英文双引号包裹：`A["无状态计算节点（CNode）"]`。中文全角括号（）、全角冒号：可以出现在引号内的标签中。`timeline` 与 `mindmap` 中避免使用半角冒号 `:`（`timeline` 的分隔符除外）和半角括号。
- `sequenceDiagram` 消息文字中避免使用分号 `;` 和 `#`。
- `quadrantChart` 的点名称如出现解析错误，可保留英文。`xychart-beta` 的分类标签用双引号。
- 每个文件完成后必须运行：`bash scripts/lint_mermaid.sh "Chinese translation/docs/<part>/<file>.md"`，并修复所有 FAIL。

## 7. 中文写作规范 / Chinese style
- 简体中文；中文语句使用全角标点（，。；：？！""），英文、数字、代码内部用半角。
- 中文与英文单词/数字之间加一个半角空格（如"使用 NVMe-oF 协议"、"约 6.5 TB"）。
- 不要逐词硬译；在不改变事实的前提下，可调整语序使之符合中文表达习惯。保留原文的论证结构、例子和数字。
- 不添加原文没有的事实或观点，不删减内容（包括表格行、列表项、闪卡、问题）。

## 8. 质量检查 / QA for each file
```bash
cd /home/user/storage-_db_claude
bash scripts/lint_mermaid.sh "Chinese translation/docs/<part>/<file>.md"     # 必须以 OK 结束
python3 scripts/check_links.py --allow-planned "Chinese translation/docs/<part>/<file>.md"   # 0 broken（指向尚未翻译完成的中文章节的链接可忽略）
```
还需自查：脚注编号集合与英文原文一致（`grep -o "\[\^[0-9]*\]" | sort -u`）；表格行数一致；`<details>` 数量一致（如适用）。

## 9. 大文件写入方法 / Writing long files
单次写入不宜过长。先用 Write 工具写入第一段（约 120–200 行），再用 Bash 追加后续段落，注意路径含空格须加引号，heredoc 定界符须加单引号以避免 `$` 等被展开：
```bash
cat >> "/home/user/storage-_db_claude/Chinese translation/docs/03-system-architecture/16-disaggregated-shared-everything.md" <<'ZHEOF'
……译文……
ZHEOF
```
