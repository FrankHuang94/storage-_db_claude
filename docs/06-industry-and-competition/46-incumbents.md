# 46. Incumbents

> **Depth:** L2 · **Reading time:** ~15 min · **Last verified:** 2026-11-01
> **Prerequisites:** [Market structure](40-market-structure.md) · [Scale-up dual-controller arrays](../03-system-architecture/14-scale-up-dual-controller.md) · [Disaggregated shared-everything](../03-system-architecture/16-disaggregated-shared-everything.md) · [Parallel file systems](../03-system-architecture/17-parallel-file-systems.md) · [The NVIDIA ecosystem](../05-ai-storage/34-nvidia-ecosystem.md)

## TL;DR

- **Six incumbents still hold most of the external storage market.** In IDC's 2Q26 count, Dell (23.8%), Huawei (11.3%), NetApp (9.6%) and HPE (6.8%) together held about 51%, with Everpure fourth at 8.1%[^idc2q26]. IBM and Hitachi Vantara sit just below the top five.
- **Every incumbent is retrofitting an AI story onto an enterprise-era core.** The methods differ. Dell, NetApp and HPE built new disaggregated or parallel systems (Lightning FS, AFX, X10000). HPE and Hitachi lean on partners (VAST, Hammerspace). NetApp bought software (DataPelago, PEAK:AIO). Huawei built a separate, NVIDIA-free stack for markets it can still sell into.
- **Their real weapons are commercial, not architectural.** These are installed base, channel reach, bundling storage with servers and networking, captive financing, and (for Huawei) sovereign and China demand. Dell sells the GPU servers, and HPE now also owns Juniper's networking. Both can bundle storage into an AI-factory purchase order.
- **Their weaknesses are specific.** Dell and HPE carry portfolio sprawl, with five or more operating systems each. NetApp's ONTAP core dates from 1992 and AFX is first-generation. HPE's file story depends on VAST. IBM's AI strength is narrow (Storage Scale) and its storage revenue is not disclosed. Hitachi is block-heavy. Huawei is largely shut out of the US.
- **Against Everpure, the threat ranking is roughly Dell > NetApp > HPE > Huawei (outside the US) > IBM > Hitachi.** This is the atlas's judgment. Dell wins on bundling. NetApp wins on unified file and installed base. The others win in narrower niches.

## Why this matters for Everpure strategy

Most of the AI-storage debate is about VAST, WEKA and DDN ([Chapter 42](42-vast-data.md)–[Chapter 44](44-ddn.md)). Most of Everpure's actual revenue, though, is won from or lost to incumbents. Everpure gained share for a decade by displacing EMC, NetApp, HPE 3PAR and IBM arrays in enterprise block and file. In the quarter to June 2026 it was the fastest grower in IDC's top five, at about +50% year on year[^idc2q26]. The next leg of growth depends on enterprise AI: RAG, inference and "AI factories" bought by the same CIOs who own today's arrays. In those deals the incumbent is usually already in the room, often holding the server and network order as well.

Strategy teams should treat each incumbent as a bundle of three assets. The first is an **installed base**, which sets refresh timing and switching costs. The second is a **route to market**: direct sales, channel, OEM, or a server attach. The third is an **AI architecture**, which decides whether the incumbent can keep the AI workload or must cede it to a specialist. This chapter profiles each of the six against those assets. The same sub-structure is used throughout, so the profiles can be compared line by line.

## Core concepts

### The incumbent playbook and the AI problem

An incumbent's moat is mostly commercial. Large customers standardise on a vendor's management tools, replication and support contracts. Value-added resellers earn margin on the full stack. When the vendor also sells servers, it can price storage as an attachment rather than a standalone purchase. Captive finance arms (Dell Financial Services, HPE Financial Services, IBM Financing) turn capex into monthly payments. That competes directly with Everpure's Evergreen//One subscription ([Chapter 23](../03-system-architecture/23-consumption-models.md)).

The AI problem is architectural. Incumbent flagships were designed in the 1990s–2010s for transactional block I/O and enterprise NAS. They are usually [dual-controller, scale-up arrays](../03-system-architecture/14-scale-up-dual-controller.md) or [shared-nothing scale-out NAS](../03-system-architecture/15-scale-out-shared-nothing.md). AI training and inference need terabytes per second of parallel throughput, metadata at billions of files, GPU-direct data paths and, now, a [KV-cache tier](../05-ai-storage/32-inference-and-kv-cache.md). Incumbents can respond in four ways, and most use more than one:

1. **Build** a new disaggregated or parallel system beside the legacy core.
2. **Partner** with an AI-native specialist and resell or embed its software.
3. **Acquire** a start-up for a capability.
4. **Certify**, using NVIDIA's DGX SuperPOD, NVIDIA-Certified Storage and STX programmes as a credibility shortcut ([Chapter 34](../05-ai-storage/34-nvidia-ecosystem.md)).

Five of the six were named STX co-design partners in March 2026: Dell, Hitachi Vantara, HPE, IBM and NetApp. Huawei was not[^stx].

**Semiconductor bridge.** Incumbents are in the position of integrated device makers when fabless design and foundries took off. Their fabs (installed base, field sales) remain valuable. Their process (architecture) is a generation behind the specialist, so they license IP or partner with a foundry while protecting the margin of the legacy line.

| Incumbent | Architectures shipped (Part 3) | Flagship AI offering, 2025–26 | Business model and scale | Key strength | Key weakness |
|---|---|---|---|---|---|
| **Dell** | Scale-up block, SDS block, shared-nothing NAS, parallel FS, object | AI Data Platform: PowerScale + Lightning FS + ObjectScale | Storage $16.6B in FY26, inside ISG; server attach | Server + storage bundle, #1 share | Five-plus storage OSes; storage flat in FY26 |
| **NetApp** | Scale-up unified (ONTAP), disaggregated (AFX), object, parallel FS via E-Series | AFX + AI Data Engine; DataPelago, PEAK:AIO deals | Pure-play, $6.9B FY26 revenue, cloud services | One OS across on-prem and three hyperscalers | ONTAP core age; AFX first-generation |
| **HPE** | Disaggregated block (B10000), disaggregated object/file (X10000), Lustre (Cray), VAST-based file | X10000 KV-cache offload; Private Cloud AI | Storage ~$1.3B/quarter inside Cloud & AI; GreenLake | Servers + Juniper networking + GreenLake | File depends on VAST; storage growth lags servers |
| **IBM** | Scale-up block (FlashSystem), parallel FS (Storage Scale), SDS object (Ceph) | Storage Scale AI Data Platform, content-aware storage | Storage not disclosed; inside Infrastructure | Storage Scale at HPC/AI scale; mainframe estate | Narrow AI footprint; weak mid-market reach |
| **Hitachi Vantara** | Scale-up block (VSP One), NAS, object | Hitachi iQ with NVIDIA; planned STX support | Not disclosed; storage +45% in Q1 FY26 | High-end block reliability; Japan | Thin scale-out file for AI; partner reliance |
| **Huawei** | Scale-up block (Dorado), scale-out AI (A-series), distributed file/object (Pacific) | OceanStor A800, M900 context memory, UCM | Not disclosed; IDC #2 at 11.3% | China and sovereign markets; vertical stack | US Entity List; no NVIDIA programme |

*Figure 46.1 — Profile summary: every incumbent now ships at least one AI-oriented architecture, but only Dell, NetApp, HPE and Huawei built a new one themselves; sources in the profiles below.*

```mermaid
flowchart LR
    D[Dell] --> D1["Block: PowerStore, PowerMax, PowerFlex"]
    D --> D2["File: PowerScale OneFS, Lightning FS"]
    D --> D3["Object: ObjectScale"]
    D --> D4["AI layer: Dell AI Data Platform"]
    N[NetApp] --> N1["Block: AFF and ASA on ONTAP, E-Series"]
    N --> N2["File: ONTAP AFF, AFX"]
    N --> N3["Object: StorageGRID"]
    N --> N4["AI layer: AI Data Engine, DataPelago"]
    H[HPE] --> H1["Block: Alletra MP B10000"]
    H --> H2["File: GreenLake for File, Cray ClusterStor"]
    H --> H3["Object and file: Alletra MP X10000"]
    H --> H4["AI layer: Private Cloud AI, Data Fabric"]
    classDef partner fill:#E69F00,color:#222222
    class H2 partner
```

*Figure 46.2 — Portfolio map, US incumbents: Dell and NetApp own every layer, while HPE's mainstream file product (orange) runs partner VAST software.*

```mermaid
flowchart LR
    I[IBM] --> I1["Block: FlashSystem, DS8000"]
    I --> I2["File: Storage Scale, Scale System"]
    I --> I3["Object: Storage Ceph"]
    I --> I4["AI layer: Scale AI Data Platform, Fusion"]
    V[Hitachi Vantara] --> V1["Block: VSP One Block, High End"]
    V --> V2["File: VSP One File, Hammerspace"]
    V --> V3["Object: VSP One Object"]
    V --> V4["AI layer: Hitachi iQ"]
    W[Huawei] --> W1["Block: OceanStor Dorado"]
    W --> W2["File: OceanStor A-series, Pacific"]
    W --> W3["Object: OceanStor Pacific"]
    W --> W4["AI layer: M900 context memory, UCM"]
    classDef partner fill:#E69F00,color:#222222
    class V2 partner
```

*Figure 46.3 — Portfolio map, IBM, Hitachi Vantara and Huawei: IBM's AI weight sits on one product, Storage Scale; Hitachi borrows its AI-scale file namespace from a partner.*

### Dell Technologies

**Architecture.** Dell has the broadest portfolio, and most of it came through acquisition (EMC, Isilon, XtremIO, ScaleIO). PowerStore and PowerMax are [scale-up block arrays](../03-system-architecture/14-scale-up-dual-controller.md). PowerFlex is [software-defined block](../03-system-architecture/19-software-defined-and-hci.md). PowerScale (OneFS, ex-Isilon) is a [shared-nothing scale-out NAS](../03-system-architecture/15-scale-out-shared-nothing.md). ObjectScale is [object storage](../03-system-architecture/18-object-storage-architecture.md). The new piece is the **Lightning File System**, previewed as Project Lightning: a [parallel file system](../03-system-architecture/17-parallel-file-systems.md) built on OneFS foundations, with a client that stripes I/O across nodes[^dellltng][^nandres].

**AI strategy.** In 2024 Dell said PowerScale was the first Ethernet storage certified for DGX SuperPOD[^dellspod]. At GTC 2026 it recast the Dell AI Data Platform as three storage engines on common hardware: PowerScale for file, Lightning for parallel "Tier 0" file and ObjectScale for object. Dell claims Lightning delivers 2x the throughput of competing parallel file systems and up to 150 GB/s per rack unit (vendor claim)[^dellaidp]. Exascale Storage for Dell PowerRack is slated for 2H 2026, with a PowerFlex-inclusive version in 1H 2027[^nandres].

**Business model.** Storage is a line inside the Infrastructure Solutions Group (ISG). In FY26 (ended 2026-01-30), storage revenue was $16.63B, up 1%, while ISG grew 40% to $60.8B on AI servers[^dellfy26]. Storage therefore fell to about 27% of ISG, from roughly 38% a year earlier (16.46 ÷ 43.4, worked from the prior year's ISG). In Q2 FY27 (May–July 2026) storage was $4.85B, up 26%, and Dell guided full-year storage up mid-teens. It said Dell-IP products (PowerStore, PowerMax, PowerScale and others) keep rising as a share of the mix[^dellq2].

**Strengths.** Dell has the largest share (23.8% in 2Q26[^idc2q26]), an enormous channel, and AI servers it can attach storage to. Its Future-Proof Program offers controller-upgrade and satisfaction guarantees similar to Evergreen[^dellfpp].

**Weaknesses.** Dell runs five or more storage operating systems with different management, replication and support teams. It still resells partner arrays in some segments. A flat FY26 while the market grew says its storage franchise underperformed until NAND-driven price rises and AI demand arrived. Lightning is new, and its scale and customer base are not yet public.

**Against Everpure.** Dell is the most frequent opponent in enterprise block (PowerStore against FlashArray) and file/AI (PowerScale and Lightning against FlashBlade). In AI-factory deals it can quote GPUs, networking, storage and services on one purchase order. The rivalry has history: Pure Storage settled EMC's patent litigation in 2016[^emc].

### NetApp

**Architecture.** NetApp is a storage pure-play built on one OS, ONTAP. ONTAP grew out of the 1992 WAFL file system and runs as HA pairs ([Chapter 14](../03-system-architecture/14-scale-up-dual-controller.md)) clustered into a scale-out namespace. It serves file and block from the AFF (all-flash) and ASA (SAN-only) lines. StorageGRID is its object store, and E-Series with BeeGFS covers parallel HPC. In October 2025 NetApp launched **AFX**, a disaggregated ONTAP system in which AFX 1K controllers share NVMe enclosures over a fabric, so performance and capacity scale independently. An optional DX50 data-compute node hosts GPU work ([Chapter 16](../03-system-architecture/16-disaggregated-shared-everything.md))[^afx].

**AI strategy.** NetApp has two prongs. The first is the AI Data Engine (AIDE), which adds metadata indexing, vectorisation and data-guardrail services to ONTAP and integrates with NVIDIA's AI Data Platform. Launch coverage expected GA in calendar 1Q26[^aidett]. The second is acquisitions. NetApp bought DataPelago (a GPU-accelerated data-processing engine, price undisclosed) on 2026-07-16[^datapelago], and in September 2026 announced its intent to buy PEAK:AIO, a maker of high-performance AI storage software[^peak]. The AFF A90 was validated for DGX SuperPOD and NVIDIA Cloud Partner designs in March 2025[^ntapnv].

**Business model.** FY26 (ended April 2026) revenue was $6.93B (+5%), with all-flash arrays at $4.2B (+11%) and free cash flow of $1.87B[^ntapfy26]. Q1 FY27 (to 2026-07-31) revenue was $2.03B (+30%), flattered by a 14-week quarter. All-flash was about $1.31B (+47%) and public cloud $206M. Full-year FY27 guidance is $7.975–8.225B[^ntapq1].

**Strengths.** NetApp's unique asset is ONTAP running as a first-party service inside all three hyperscalers, which gives true hybrid file. It also has a huge NAS installed base, the most mature data-management feature set, and a strong channel.

**Weaknesses.** ONTAP's write path and HA-pair design date from a pre-flash era. AFX is a first-generation product with little public field evidence. Two AI acquisitions in three months suggest NetApp is buying capability it did not build. Its hardware leans on commodity SSDs rather than custom flash modules.

**Against Everpure.** NetApp is Everpure's closest like-for-like rival: a storage pure-play selling unified block/file, subscriptions (Keystone against Evergreen//One) and AI data services. AFX against FlashBlade//EXA is the cleanest head-to-head in disaggregated AI storage.

### Hewlett Packard Enterprise (HPE)

**Architecture.** HPE has consolidated onto **Alletra Storage MP**, a common hardware platform with two personalities. The B10000 runs block (3PAR/Primera lineage) and now scales out to six nodes[^b10k]. The X10000 is a disaggregated object store with native NFS, scaling to 16 compute and 16 storage nodes and 23 PB raw[^x10k]. File for enterprise AI came first from **GreenLake for File Storage**, which is VAST Data software on Alletra MP hardware (2023)[^hpevast]. Cray ClusterStor serves Lustre for supercomputing. The Nimble line came by acquisition in 2017[^nimble].

**AI strategy.** HPE describes the X10000 as the first object platform to earn NVIDIA-Certified Storage (Foundation level)[^hpenv]. A sponsored validation of X10000 KV-cache offload on H200 GPUs reported up to 20x faster time-to-first-token than no offload (partner content, not independent)[^hpekv]. HPE closed its ~$14B Juniper acquisition on 2025-07-02, which adds data-centre and AI networking to the bundle[^juniper].

**Business model.** In FY25 (ended October 2025) the Hybrid Cloud segment, which held storage and GreenLake private cloud, had revenue of $5.75B (+4.9%). Its gross profit fell 2.5% as HPE moved to the software-defined Alletra platform[^hpe10k]. From FY26 storage is reported within Cloud & AI: Q3 FY26 storage was about $1.3B (+10.2%) against servers up 35%, with Alletra MP orders up strong double digits[^hpeq3]. HPE was named a Leader in Gartner's 2026 Magic Quadrant for Enterprise Storage Platforms[^hpemq].

**Strengths.** HPE combines compute, networking and storage with GreenLake consumption and financing. It has a credible disaggregated platform, a Cray/HPC heritage, and a sovereign and public-sector presence.

**Weaknesses.** HPE depends on a partner for high-end AI file, and that partner competes with it directly in neoclouds. The X10000's native file mode now overlaps GreenLake for File, and it is unclear which HPE will lead with [VERIFY: whether GreenLake for File (VAST) is still actively sold in 2026]. Storage growth lags HPE's server growth by roughly 25 points, and HPE's share (6.8%) trails Everpure's[^idc2q26].

**Against Everpure.** HPE shows up in mid-range block refreshes, especially where GreenLake or HPE servers are already standard, and in sovereign and HPC AI deals.

### IBM

**Architecture.** IBM's AI weight sits on **Storage Scale** (ex-GPFS), a [shared-disk parallel file system](../03-system-architecture/17-parallel-file-systems.md) sold as software or as Storage Scale System appliances. Beside it are FlashSystem scale-up block arrays, which use IBM's own FlashCore Modules. A 2026 generation added 105 TB modules[^fcm], making these the closest analogue to Everpure's DirectFlash. IBM Storage Ceph provides software-defined object and block, after Red Hat's Ceph team moved to IBM in 2022[^ceph]. IBM Fusion packages storage for OpenShift.

**AI strategy.** The Storage Scale System 6000 was certified for DGX SuperPOD in 2024[^ibmspod]. Storage Scale 6.0.1 and Storage Scale System 7.0.1 (GA June 2026) fold in content-aware storage, which embeds and indexes data inside the file system, as the "Storage Scale AI Data Platform". IBM says it is certified for BasePOD, SuperPOD and NVIDIA Cloud Partner reference architectures[^ibmscale]. IBM added S3 over RDMA in June 2026[^s3rdma] and demonstrated a 100-billion-vector database on content-aware storage[^ibmvec].

**Business model.** IBM does not disclose storage revenue. Storage sits in Distributed Infrastructure within the Infrastructure segment. Infrastructure grew 12% in 2025 on the z17 mainframe cycle, but Distributed Infrastructure was only +3% in Q4[^ibmq4].

**Strengths.** Storage Scale has a long record at exabyte HPC scale. IBM has deep financial-services and mainframe accounts, custom flash modules, and Red Hat/OpenShift integration.

**Weaknesses.** IBM's AI strength is narrow: one parallel file system with an HPC-grade operational burden. It has limited mid-market and channel reach, and storage is a small, opaque line inside a software-and-consulting company.

**Against Everpure.** IBM is a frequent FlashSystem opponent in regulated enterprises, and Storage Scale competes in large training and research clusters. It is rarely a broad-portfolio threat.

### Hitachi Vantara

**Architecture.** Hitachi's core is high-end and mid-range **[scale-up block](../03-system-architecture/14-scale-up-dual-controller.md)** under the VSP One brand, plus VSP One File and VSP One Object. VSP One Block High End launched in late 2025 for mission-critical and AI workloads[^hitvsp].

**AI strategy.** Hitachi's AI offer is **Hitachi iQ**, a full-stack NVIDIA-based AI platform. VSP One earned DGX BasePOD certification in 2024[^hitbase]. In March 2026 Hitachi expanded iQ with agent blueprints and said it will support NVIDIA STX. Scale-out AI file comes partly through **Hammerspace**, which orchestrates data that VSP One holds[^hitiq].

**Business model.** Hitachi Vantara is a subsidiary of Hitachi Ltd. and does not publish storage revenue. It reported revenue up 12% and storage revenue up 45% (block +49%) in Q1 FY2026 (April–June 2026)[^hitq1].

**Strengths.** Hitachi has a reputation for high-end block reliability, mainframe connectivity, a strong Japanese and Asia-Pacific base, and the backing of an industrial conglomerate.

**Weaknesses.** It has no home-grown scale-out file system at AI scale and relies on partners for the AI data layer. Share outside Japan is low, and Hitachi is absent from IDC's top five.

**Against Everpure.** Hitachi meets Everpure mainly in high-end block consolidation and mainframe-adjacent estates. It is rarely in AI-factory file deals.

### Huawei

**Architecture.** Huawei sells a complete, vertically integrated range. OceanStor Dorado is all-flash block/unified scale-up. The OceanStor **A-series** is AI storage: the A800 scales to 512 controllers and more than 1 EB, with a claimed 500 GB/s per controller enclosure[^a800]. OceanStor Pacific is distributed scale-out file and object. A May 2026 recap said the A800 replaced the retiring A600 as the flagship[^idi]. In September 2026 Huawei added the **OceanStor M900** context-memory system, which it says provides up to 64 PB of shared KV cache and 40 TB/s per SuperPod cluster (vendor claims)[^m900].

**AI strategy.** Huawei pairs its storage with its own Ascend accelerators. It released **Unified Cache Manager (UCM)**, KV-cache tiering software intended to reduce dependence on scarce HBM, in August 2025 and said it would open-source it[^ucm]. Huawei is outside NVIDIA's STX programme[^stx].

**Business model.** Huawei is privately held. Revenue in 2025 was CNY 880.9B (+2.2%)[^hwar], with storage inside ICT infrastructure, which reported CNY 375.0B [VERIFY: search-summary only][^hwict]. IDC ranks Huawei #2 in external storage (11.3% in 2Q26)[^idc2q26].

**Strengths.** Huawei has a home market that excludes US vendors from many accounts, plus sovereign-AI buyers in the Middle East, Southeast Asia, Latin America and Africa. Its stack is vertically integrated (NAND controllers, SSDs, arrays, accelerators), its prices are aggressive, and it has state-linked financing.

**Weaknesses.** Huawei has been on the US Entity List since May 2019[^entity]. That restricts its access to US technology and makes it unsellable to many Western regulated buyers. It has no NVIDIA certification path, and its claims are rarely independently benchmarked.

**Against Everpure.** Huawei rarely meets Everpure in the US. It matters in EMEA, APJ and sovereign deals, and as an example of a full-stack AI-storage design built without NVIDIA.

### What the revenue numbers do and don't say

Only four of the companies disclose a storage-relevant line, and each defines it differently. The chart aligns them on the fiscal quarter that ended in July or early August 2026.

![Grouped bar chart of revenue in the fiscal quarter ending July–August 2026 vs a year earlier: Dell ISG storage 4.85B (+26%), NetApp total revenue 2.03B (+30%, 14 weeks), Everpure total revenue 1.19B (+38%), HPE storage 1.29B (+10%), each with its IDC 2Q26 external-storage share.](../assets/charts/ch46-storage-revenue.svg)

*Figure 46.4 — In the quarter to mid-2026 every disclosing vendor grew, but HPE's storage grew at a third of the others' pace; company-reported lines are roughly 1.5–2x what IDC's external-storage shares imply.*
Data: `data/ch46_storage_revenue.csv`

Work the IDC arithmetic to see the definitional gap. IDC sized 2Q26 external storage at $10.3B[^idc2q26]:

- Dell: 23.8% × $10.3B ≈ **$2.45B**, against $4.85B reported for a quarter offset by one month.
- HPE: 6.8% ≈ **$0.70B** against $1.29B.
- Everpure: 8.1% ≈ **$0.83B** against $1.19B. Everpure's total includes about $0.5B of subscription services[^everq2].

Company lines include maintenance, services, software and, for Dell, data-protection appliances. IDC counts external systems. The same method gives Huawei about $1.16B a quarter, or roughly $4.6B annualised (estimate, ×4). In external systems that is larger than NetApp's $0.99B (9.6%), even though Huawei publishes no storage figure. When comparing incumbents, use IDC for share and filings for growth and margin, and never mix the two in one ratio.

### Positioning: breadth versus AI-native depth

```mermaid
quadrantChart
    title Incumbent AI positioning - atlas judgment, Nov 2026
    x-axis Narrow portfolio --> Broad portfolio
    y-axis Retrofitted architecture --> AI-native architecture
    quadrant-1 Broad and AI-deep
    quadrant-2 Focused AI specialist
    quadrant-3 Focused legacy
    quadrant-4 Broad but retrofitted
    Dell: [0.90, 0.60]
    HPE: [0.82, 0.48]
    Huawei: [0.78, 0.66]
    IBM: [0.66, 0.62]
    NetApp: [0.56, 0.54]
    Hitachi: [0.42, 0.30]
    Everpure ref: [0.46, 0.64]
    VAST ref: [0.28, 0.88]
```

*Figure 46.5 — Atlas judgment, not measured data: Dell and Huawei combine the broadest portfolios with credible home-grown AI systems, HPE's breadth outruns its own AI architecture, and no incumbent matches a specialist like VAST on AI-native depth.*

The x-axis scores the range of block, file, object, data-protection, compute and networking products sold under one contract. The y-axis scores how much of the AI data path runs on architecture the vendor owns and designed for AI. That covers parallel or disaggregated data paths, GPU-direct I/O, KV-cache tiers and in-storage data services. Partner-sourced capability is discounted. That is why HPE (VAST for file) and Hitachi (Hammerspace) score lower than their catalogues suggest.

## How Everpure approaches it vs. competitors

Everpure's pitch against incumbents has been consistent since the Pure Storage era. It offers one OS (Purity) across FlashArray and FlashBlade, its own flash modules (DirectFlash), non-disruptive upgrades under Evergreen, and Pure Fusion and Pure1 management ([Chapter 28](../04-everpure/28-platform-and-software.md)). The table shows how that pitch meets each incumbent's best argument.

| Incumbent | Typical deal where it meets Everpure | Incumbent's best argument (steelman) | Everpure's counter | Where Everpure is exposed |
|---|---|---|---|---|
| Dell | Enterprise block refresh; AI factory with Dell servers | One vendor for GPUs, network, storage, services and financing; installed base | One OS vs five-plus; Evergreen upgrades; DirectFlash density and power | Cannot bundle servers; smaller field force |
| NetApp | Unified NAS consolidation; hybrid cloud file | ONTAP everywhere, including native in AWS, Azure and Google Cloud | Simpler operations; FlashBlade//EXA vs first-generation AFX | Cloud-native file presence weaker than ONTAP's |
| HPE | Mid-range block; GreenLake-standardised accounts; sovereign | Compute + Juniper networking + GreenLake, one contract | Mature subscription (Evergreen//One); own AI file system, not a partner's | Sovereign and HPC relationships |
| IBM | Regulated-industry block; research clusters | Storage Scale scale record; mainframe and Red Hat integration | Broader enterprise AI portfolio; simpler operations | Large-scale parallel FS heritage |
| Hitachi Vantara | High-end block consolidation | Reliability guarantees; mainframe; Japan relationships | Density, power and upgrade model | High-end mainframe-attached block |
| Huawei | EMEA, APJ, sovereign tenders | Price, full-stack China supply chain, state financing | Trust, compliance, NVIDIA ecosystem | Price-led and sovereign deals |

*Figure 46.6 — Where each incumbent meets Everpure: incumbents mostly win on the commercial bundle, and Everpure mostly wins on architecture and operating model.*

Two strategic implications follow. First, server-attached bundling (Dell, HPE) is the incumbents' hardest-to-copy weapon. Everpure's options are partnerships with server and network vendors, as in its NVIDIA and Cisco reference designs ([Chapter 34](../05-ai-storage/34-nvidia-ecosystem.md)), or making storage an independent purchase through the consumption model. Second, incumbents' reliance on partners (HPE–VAST, Hitachi–Hammerspace) and on acquisitions (NetApp) shows how much AI-native IP is worth. That is relevant to Everpure's own build/buy/partner map ([Chapter 54](../07-history-and-future/54-strategic-option-map.md)).

## History and trajectory

```mermaid
timeline
    title Incumbent AI-storage moves, 2023-2026
    2023 : HPE launches GreenLake for File on VAST software
    2024 : Dell PowerScale certified for DGX SuperPOD : Huawei launches OceanStor A800 : Hitachi VSP One gets BasePOD : IBM Scale System 6000 gets SuperPOD
    2025 : NVIDIA AI Data Platform names Dell HPE Hitachi IBM NetApp : HPE closes Juniper : Huawei unveils UCM : NetApp launches AFX and AI Data Engine : Dell previews Lightning
    2026 : Dell Lightning FS ships : STX co-design partners exclude Huawei : IBM Storage Scale AI Data Platform : NetApp buys DataPelago and agrees to buy PEAK AIO : Huawei OceanStor M900
```

*Figure 46.7 — Incumbents moved from certifying existing arrays (2024) to shipping new disaggregated and parallel architectures and buying AI software (2025–26).*

The 2025 NVIDIA AI Data Platform launch named Dell, HPE, Hitachi Vantara, IBM and NetApp alongside Pure Storage, VAST and WEKA[^aidp]. Over the following year, three incumbents shipped architectures that did not exist two years earlier: Dell Lightning, NetApp AFX and HPE X10000. Three trends to watch are:

1. **KV-cache tiers.** Huawei's M900 and HPE's X10000 offload work show incumbents now competing in [inference context memory](../05-ai-storage/32-inference-and-kv-cache.md), not only training throughput.
2. **Consolidation.** Expect more incumbent purchases of AI data software, following NetApp's two deals.
3. **The pricing cycle.** The 2026 NAND shortage lifted reported storage revenue across the board. Part of the growth in Figure 46.4 is price, not share ([Chapter 48](48-media-suppliers-and-nand-cycle.md)).

## Numbers that matter

| Metric | Value | Context | Source / date |
|---|---|---|---|
| IDC external storage, 2Q26 | $10.3B, +33.6% YoY | Dell 23.8%, Huawei 11.3%, NetApp 9.6%, Everpure 8.1%, HPE 6.8% | IDC via StorageReview, 2026-09[^idc2q26] |
| Dell storage revenue, FY26 | $16.63B, +1% | ISG $60.8B, +40%, on AI servers | Dell, 2026-02-26[^dellfy26] |
| Dell storage, Q2 FY27 | $4.85B, +26% | Full-year storage guided up mid-teens | Dell, 2026-08[^dellq2] |
| NetApp revenue, FY26 | $6.93B, +5% | All-flash $4.2B, +11% | NetApp, 2026-05-28[^ntapfy26] |
| NetApp revenue, Q1 FY27 | $2.03B, +30% | 14-week quarter; FY27 guide $7.975–8.225B | NetApp, 2026-09-02[^ntapq1] |
| HPE storage, Q3 FY26 | ~$1.3B, +10.2% | Servers +35% in the same quarter | HPE 8-K, 2026-09-02[^hpeq3] |
| Hitachi Vantara storage growth, Q1 FY2026 | +45% | Block +49% | Hitachi Vantara, 2026-08-12[^hitq1] |
| Huawei external-storage revenue, implied | ~$1.16B/quarter | 11.3% × $10.3B; Huawei does not disclose | Worked example from IDC[^idc2q26] |
| HPE X10000 maximum scale | 16 + 16 nodes, 23 PB raw | Disaggregated object with native NFS | Blocks & Files, 2026-05-12[^x10k] |
| Everpure revenue, Q2 FY27 | $1.19B, +38% | FY27 guide $5.03–5.07B | Everpure, 2026-08-26[^everq2] |

## Conversation playbook

**Questions for a PM**

1. *"In AI-factory deals where Dell supplies the GPU servers, what is our win rate, and what changes it?"* A strong answer separates deals by who controls the purchase order: the CIO, the AI team or a neocloud. It names the specific levers, such as NVIDIA reference designs, Evergreen//One pricing, power per petabyte and partner bundles, and says where the company walks away.
2. *"How do we position FlashBlade//EXA against NetApp AFX?"* A strong answer is architectural and evidence-based. It covers metadata/data separation versus shared-media ONTAP, the maturity of each, MLPerf or customer results, and ONTAP's hybrid-cloud advantage, which Everpure should concede rather than deny.
3. *"Where does HPE's dependence on VAST help or hurt us?"* A strong answer recognises that HPE+VAST can be a formidable combination in sovereign and HPC accounts. It also notes that the X10000 and GreenLake for File overlap, which can confuse HPE's own sales motion.

**Questions for an engineer**

1. *"What would it take for Dell Lightning FS to match FlashBlade//EXA's metadata scale?"* A strong answer looks at Lightning's client-side striping and OneFS heritage. It identifies whether metadata is distributed or centralised and the likely small-file limits, and distinguishes vendor-claimed GB/s per rack unit from audited results.
2. *"How does IBM FlashCore compare with DirectFlash?"* A strong answer notes that both put flash management in the array's software rather than in an SSD controller. It then compares where compression and the FTL run (inline in the module for FlashCore, in Purity for DirectFlash) and the module-capacity roadmaps.
3. *"Is a KV-cache tier on X10000 or M900 the same product category as PureKVA?"* A strong answer compares the data path (NIXL/GDS and RDMA), capacity versus latency, and whether the cache is a shared namespace or a separate appliance, citing the sponsored or vendor status of each claim.

**Don't say this:**

- *"Incumbents can't do AI."* All six have AI-certified or AI-specific systems, and Dell, NetApp and HPE shipped new architectures in 2025–26.
- *"Dell's storage business is shrinking."* It was flat in FY26 and grew 26% in Q2 FY27.
- *"HPE sells VAST."* HPE sells GreenLake for File built on VAST software. It also sells its own X10000 with native file.
- *"Huawei isn't a competitor."* It is #2 worldwide by IDC's count. It is simply absent from most US deals.
- Comparing IDC share percentages directly with company-reported storage revenue.

## Going deeper (optional, L3 pointers)

- Dell Lightning FS spec sheet and OneFS 9.x technical overviews (Dell InfoHub) cover client striping and protection levels.
- NetApp's AFX technical report and AIDE architecture documents (docs.netapp.com) cover the disaggregated ONTAP data path.
- Read IBM's GPFS paper (Schmuck and Haskin, FAST 2002) alongside the Storage Scale 6.0.1 release blog.
- The HPE X10000 Release 4 notes describe its log-structured key-value design and NFS front end.
- For the economics behind every row above, see the IDC Worldwide Quarterly Enterprise Storage Systems Tracker methodology notes.

## Key terms

- **ISG (Infrastructure Solutions Group)** — Dell's segment containing servers, networking and storage.
- **Lightning File System** — Dell's parallel file system, formerly Project Lightning.
- **AFX** — NetApp's disaggregated ONTAP all-flash system.
- **AI Data Engine (AIDE)** — NetApp's ONTAP extension for indexing, vectorising and governing data for AI.
- **Alletra Storage MP** — HPE's common hardware platform for B10000 block and X10000 object/file.
- **GreenLake for File Storage** — HPE's file service built on VAST Data software.
- **FlashCore Module** — IBM's custom flash module with in-module compression.
- **Hitachi iQ** — Hitachi Vantara's NVIDIA-based AI infrastructure stack.
- **OceanStor A-series** — Huawei's AI-oriented scale-out storage line.
- **Unified Cache Manager (UCM)** — Huawei's KV-cache tiering software.
- **Server attach** — selling storage as part of a server-led purchase.
- See the [glossary](../glossary.md) for the rest.

## Sources

[^idc2q26]: StorageReview, "IDC External Storage Tracker: $10.3 Billion in Q2 2026 as Server Market Tops $166 Billion on AI Demand," 2026-09. https://www.storagereview.com/news/idc-external-storage-tracker-q2-2026-10-3-billion-as-server-market-tops-166-billion ; Blocks & Files, "IDC's latest enterprise storage tracker shows booming storage market growth," 2026-09-23. https://www.blocksandfiles.com/flash/2026/09/23/idcs-latest-enterprise-storage-tracker-shows-booming-storage-market-growth/5298577 (both retrieved 2026-11-01).
[^stx]: StorageNewsletter, "Nvidia GTC 2026: Nvidia Launches BlueField-4 STX Storage Architecture With Broad Industry Adoption," 2026-03-17. https://www.storagenewsletter.com/2026/03/17/nvidia-gtc-2026-nvidia-launches-bluefield-4-stx-storage-architecture-with-broad-industry-adoption/ (retrieved 2026-11-01).
[^dellltng]: Blocks & Files, "Dell PowerScale gets struck by Lightning and goes parallel," 2025-11-17. https://www.blocksandfiles.com/ai-ml/2025/11/17/dell-powerscale-gets-struck-by-lightning-and-goes-parallel/1711291 (retrieved 2026-11-01).
[^nandres]: NAND Research, "Dell Technologies AI Data Platform and storage portfolio for the agentic enterprise," 2026. https://nand-research.com/dell-technologies-ai-data-platform-and-storage-portfolio-for-the-agentic-enterprise/ (retrieved 2026-11-01).
[^dellspod]: Dell Technologies, "PowerScale: World's First Ethernet Storage Certified on NVIDIA SuperPOD," 2024-03. https://www.dell.com/fr-ca/blog/powerscale-worlds-first-ethernet-storage-certified-on-nvidia-superpod/ (retrieved 2026-11-01).
[^dellaidp]: Dell Technologies, "Dell AI Data Platform with NVIDIA Supercharges Enterprise AI with Breakthrough Data Orchestration and Storage Innovations," 2026-03-16. https://www.dell.com/en-us/dt/corporate/newsroom/announcements/detailpage.press-releases~usa~2026~03~dell-ai-data-platform-with-nvidia-supercharges-enterprise-ai-with-breakthrough-data-orchestration-and-storage-innovations.htm (retrieved 2026-11-01).
[^dellfy26]: Dell Technologies (Business Wire), "Dell Technologies Delivers Fourth Quarter and Full Year Fiscal 2026 Results," 2026-02-26. https://www.businesswire.com/news/home/20260226276981/en/Dell-Technologies-Delivers-Fourth-Quarter-and-Full-Year-Fiscal-2026-Results (retrieved 2026-11-01).
[^dellq2]: StorageNewsletter, "Dell Technologies: Fiscal 2Q27 Financial Results," 2026-09-03. https://www.storagenewsletter.com/2026/09/03/dell-technologies-fiscal-2q27-financial-results/ ; Dell Technologies, "Record Results Reflect Compounding Advantages," 2026-08. https://www.dell.com/en-us/blog/record-results-reflect-compounding-advantages/ (both retrieved 2026-11-01).
[^dellfpp]: Dell Technologies, "Future-Proof Program," n.d. https://www.dell.com/en-uk/dt/products/future-proof-program.htm (retrieved 2026-11-01).
[^emc]: SEC, "Pure Storage, Inc. Form 8-K (settlement with Dell/EMC)," 2016-10. https://www.sec.gov/Archives/edgar/data/1474432/000119312516741316/d275548d8k.htm (retrieved 2026-11-01).
[^afx]: Blocks & Files, "NetApp disaggregates ONTAP storage and provides an AI Data Engine," 2025-10-14. https://blocksandfiles.com/2025/10/14/netapp-disaggregates-ontap-storage-and-provides-an-ai-data-engine/ (retrieved 2026-11-01).
[^aidett]: TechTarget, "NetApp adds AI Data Engine, expands Nvidia partnership," 2025-10. https://www.techtarget.com/searchstorage/news/366632757/NetApp-adds-AI-Data-Engine-expands-Nvidia-partnership (retrieved 2026-11-01).
[^datapelago]: NetApp, "NetApp Acquires DataPelago, Making Data AI-Ready at the Infrastructure Layer," 2026-07-16. https://www.netapp.com/en/newsroom/press-releases/news-rel-20260716-210092/ (retrieved 2026-11-01).
[^peak]: NetApp, "NetApp Announces Intent to Acquire PEAK:AIO to Advance Scalable AI Infrastructure Architecture," 2026-09-25. https://s21.q4cdn.com/371534297/files/doc_news/NetApp-Announces-Intent-to-Acquire-PEAKAIO-to-Advance-Scalable-AI-Infrastructure-Architecture-2026.pdf (retrieved 2026-11-01).
[^ntapnv]: HPCwire/BigDATAwire, "NetApp Validated for NVIDIA DGX SuperPOD, Cloud Partners and Certified Systems," 2025-03-18. https://www.hpcwire.com/bigdatawire/this-just-in/netapp-validated-for-nvidia-dgx-superpod-cloud-partners-and-certified-systems/ (retrieved 2026-11-01).
[^ntapfy26]: NetApp (Business Wire), "NetApp Reports Fourth Quarter and Fiscal Year 2026 Results," 2026-05-28. https://www.businesswire.com/news/home/20260528348500/en/NetApp-Reports-Fourth-Quarter-and-Fiscal-Year-2026-Results (retrieved 2026-11-01).
[^ntapq1]: NetApp, "NetApp Reports First Quarter of Fiscal Year 2027 Results," 2026-09-02. https://netapp.com/newsroom/press-releases/news-rel-20260902-results-607632 ; MarketBeat, "NetApp Q1 earnings call highlights," 2026-09-02. https://www.marketbeat.com/instant-alerts/transcript-netapp-q1-earnings-call-highlights-2026-09-02/ (both retrieved 2026-11-01).
[^b10k]: StorageReview, "HPE Alletra Storage MP B10000 10.6.0 arrives with six-node scale-out and agentic support automation," n.d. https://storagereview.com/news/hpe-alletra-storage-mp-b10000-10-6-0-arrives-with-six-node-scale-out-and-agentic-support-automation (retrieved 2026-11-01).
[^x10k]: Blocks & Files, "HPE updates Alletras X and B10000, Zerto and Data Fabric in GreenLake private cloud update blast," 2026-05-12. https://www.blocksandfiles.com/file/2026/05/12/hpe-updates-alletras-x-and-b10000-zerto-and-data-fabric-in-greenlake-private-cloud-update-blast/5239011 (retrieved 2026-11-01).
[^hpevast]: HPCwire, "HPE taps VAST Data for fast file storage on GreenLake," 2023-04-04. https://www.hpcwire.com/2023/04/04/hpe-taps-vast-data-for-fast-file-storage-on-greenlake/ (retrieved 2026-11-01).
[^nimble]: HPE, "HPE Completes Acquisition of Nimble Storage," 2017-04-17. https://www.hpe.com/us/en/newsroom/press-release/2017/04/hpe-completes-acquisition-of-nimble-storage.html (retrieved 2026-11-01).
[^hpenv]: HPE Newsroom, "HPE accelerates secure, scalable production-ready AI through new innovations with NVIDIA," 2026-03-16. https://www.hpe.com/us/en/newsroom/press-release/2026/03/hpe-accelerates-secure-scalable-production-ready-ai-through-new-innovations-with-nvidia.html (retrieved 2026-11-01).
[^hpekv]: Blocks & Files (Partner Content), "HPE puts storage to work on AI's expensive memory problem," 2026-10-29. https://www.blocksandfiles.com/ai-ml/2026/10/29/partner-content-hpe-puts-storage-to-work-on-ais-expensive-memory-problem/5305788 (retrieved 2026-11-01).
[^juniper]: HPE Newsroom, "Hewlett Packard Enterprise closes acquisition of Juniper Networks to offer industry-leading comprehensive, cloud-native, AI-driven portfolio," 2025-07. https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html (retrieved 2026-11-01).
[^hpe10k]: SEC, "Hewlett Packard Enterprise Co. Form 10-K for fiscal year ended October 31, 2025," 2025-12. https://www.sec.gov/Archives/edgar/data/1645590/000164559025000130/hpe-20251031.htm (retrieved 2026-11-01).
[^hpeq3]: SEC, "Hewlett Packard Enterprise Co. Form 8-K, Exhibit 99.1 (fiscal 2026 third quarter results)," 2026-09-02. https://www.sec.gov/Archives/edgar/data/0001645590/000164559026000078/ex-991x922026x8k.htm ; Constellation Research, "HPE delivers strong Q3, ups fiscal 2026 outlook due to AI demand," 2026-09. https://www.constellationr.com/insights/news/hpe-delivers-strong-q3-ups-fiscal-2026-outlook-due-ai-demand (both retrieved 2026-11-01).
[^hpemq]: HPE Newsroom, "HPE named a Leader in 2026 Gartner Magic Quadrant for Enterprise Storage Platforms," 2026-08. https://www.hpe.com/us/en/newsroom/press-release/2026/08/hpe-named-a-leader-in-2026-gartner-magic-quadrant-for-enterprise-storage-platforms.html (retrieved 2026-11-01).
[^fcm]: TechTarget, "IBM FlashSystem adds 105 TB modules with agentic AI smarts," 2026. https://www.techtarget.com/searchstorage/news/366639135/IBM-FlashSystem-adds-105-TB-modules-with-agentic-AI-smarts (retrieved 2026-11-01).
[^ceph]: Ceph, "Red Hat's Ceph team is moving to IBM," 2022-10. https://ceph.io/en/news/blog/2022/red-hats-ceph-team-is-moving-to-ibm/ (retrieved 2026-11-01).
[^ibmspod]: IBM Community, "IBM Storage Scale System 6000 receives NVIDIA DGX SuperPOD certification," 2024-08-29. https://community.ibm.com/community/user/blogs/mike-kieran/2024/08/29/ibm-storage-scale-system-6000-receives-nvidia-dgx (retrieved 2026-11-01).
[^ibmscale]: IBM Community, "Introducing IBM Storage Scale 6.0.1 and Storage Scale System 7.0.1: An AI-Ready Data Platform," 2026-06-08. https://community.ibm.com/community/user/blogs/mike-kieran/2026/06/08/introducing-ibm-storage-scale-601-and-storage-scal (retrieved 2026-11-01).
[^s3rdma]: IBM Community, "IBM Storage Scale announces support for S3 over RDMA," 2026-06-16. https://community.ibm.com/community/user/blogs/ted-hoover/2026/06/16/ibm-storage-scale-announces-support-for-s3-over-rd (retrieved 2026-11-01).
[^ibmvec]: HPCwire, "IBM Demonstrates Extreme Scale for Content-Aware Storage with 100B Vector Database," 2026. https://www.hpcwire.com/off-the-wire/ibm-demonstrates-extreme-scale-for-content-aware-storage-with-100b-vector-database/ (retrieved 2026-11-01).
[^ibmq4]: IBM Newsroom, "IBM Releases Fourth-Quarter Results," 2026-01-28. https://newsroom.ibm.com/2026-01-28-IBM-RELEASES-FOURTH-QUARTER-RESULTS (retrieved 2026-11-01).
[^hitvsp]: Hitachi Vantara (PR Newswire), "Hitachi Vantara Launches Virtual Storage Platform One Block High End Storage to Power the Next Era of AI and Mission-Critical Workloads," 2025. https://www.prnewswire.com/news-releases/hitachi-vantara-launches-virtual-storage-platform-one-block-high-end-storage-to-power-the-next-era-of-ai-and-mission-critical-workloads-302617559.html (retrieved 2026-11-01).
[^hitbase]: Hitachi, "Hitachi Vantara achieves NVIDIA DGX BasePOD certification," 2024-07-29. https://www.hitachi.com/en/press/articles/2024/07/0729/ (retrieved 2026-11-01).
[^hitiq]: iTWire, "Hitachi Vantara expands Hitachi iQ capabilities to help enterprises advance responsible agentic AI," 2026-03. https://itwire.com/business-it-news/data/hitachi-vantara-expands-hitachi-iq-capabilities-to-help-enterprises-advance-responsible-agentic-ai ; Impress Cloud Watch (Japanese), Hitachi iQ and Hammerspace coverage, 2026. https://cloud.watch.impress.co.jp/docs/news/2094445.html (both retrieved 2026-11-01).
[^hitq1]: Hitachi Vantara, "Hitachi Vantara Achieves Strong Q1 Revenue Growth as VSP One Drives...," 2026-08-12. https://www.hitachivantara.com/en-us/news/gl260812 (retrieved 2026-11-01).
[^a800]: Computer Weekly, "Huawei launches exabyte-scale OceanStor A800 at AI workloads," 2024. https://computerweekly.com/news/366583602/Huawei-launches-exabyte-scale-OceanStor-A800-at-AI-workloads (retrieved 2026-11-01).
[^idi]: StorageNewsletter, "Recap Huawei IDI Forum 2026," 2026-05-27. https://www.storagenewsletter.com/2026/05/27/recap-huawei-idi-forum-2026/ (retrieved 2026-11-01).
[^m900]: Huawei, "Huawei Introduces OceanStor M900 Context Memory Storage to Accelerate AI Inference in Hyperscale Data Centers," 2026-09. https://e.huawei.com/de/news/2026/solutions/storage/hc-context-memory-storage (retrieved 2026-11-01).
[^ucm]: TrendForce, "Huawei Unveils UCM Algorithm to Cut HBM Reliance, Reportedly Goes Open Source in September," 2025-08-13. https://www.trendforce.com/news/2025/08/13/news-huawei-unveils-ucm-algorithm-to-cut-hbm-reliance-reportedly-goes-open-source-in-september/ (retrieved 2026-11-01).
[^hwar]: TelecomTV, "Huawei releases 2025 Annual Report: Performance in line with forecast," 2026-03-31. https://www.telecomtv.com/content/access-evolution/huawei-releases-2025-annual-report-performance-in-line-with-forecast-55222/ (retrieved 2026-11-01).
[^hwict]: TrendForce, "Huawei 2025 revenue: cloud revenue slips," 2026-04-01. https://www.trendforce.com/news/2026/04/01/news-huawei-2025-r-cloud-revenue-slips/ (retrieved 2026-11-01).
[^entity]: US Department of Commerce, Bureau of Industry and Security, "Addition of Entities to the Entity List," Federal Register 84 FR 22961, 2019-05-21. https://www.federalregister.gov/documents/2019/05/21/2019-10616/addition-of-entities-to-the-entity-list (retrieved 2026-11-01).
[^everq2]: Everpure, "Everpure Announces Second Quarter Fiscal 2027 Financial Results," 2026-08-26. https://investor.everpuredata.com/news-and-events/press-releases/press-release-details/2026/Everpure-Announces-Second-Quarter-Fiscal-2027-Financial-Results/default.aspx (retrieved 2026-11-01).
[^aidp]: NVIDIA Newsroom, "NVIDIA and Storage Industry Leaders Unveil New Class of Enterprise Infrastructure for the Age of AI," 2025-03-18. https://nvidianews.nvidia.com/news/nvidia-and-storage-industry-leaders-unveil-new-class-of-enterprise-infrastructure-for-the-age-of-ai (retrieved 2026-11-01).
