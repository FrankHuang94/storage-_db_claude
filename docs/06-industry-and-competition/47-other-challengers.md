# 47. Other challengers and software-defined players

> **Depth:** L2 · **Reading time:** ~10 min · **Last verified:** 2026-11-01
> **Prerequisites:** [File protocols](../02-protocols-and-networking/08-file-protocols.md) · [Object storage and S3](../02-protocols-and-networking/09-object-storage-and-s3.md) · [Software-defined storage and HCI](../03-system-architecture/19-software-defined-and-hci.md) · [Incumbents](46-incumbents.md)

## TL;DR

- **The biggest challenger is not a start-up. It is the hyperscalers' own storage.** S3 alone holds more than 500 trillion objects. Every workload that is born in the cloud and stays there is one no array vendor ever bids on.
- **Hammerspace is the most strategically interesting of the smaller players.** It does not sell media. It sells a global namespace on standard pNFS that sits *above* everyone's arrays, plus "Tier 0", which turns the idle NVMe inside GPU servers into shared storage. If it wins, the array underneath becomes interchangeable.
- **The open-source object market broke in 2025–2026.** MinIO stripped its free edition, put it in maintenance mode and archived the repository in April 2026. That pushed users toward the paid AIStor product, Ceph or forks. It is an opening for any vendor with a supported S3 offering.
- **Software-only and platform vendors win on control and cost, not peak performance.** Ceph (IBM, Croit, Clyso, 45Drives), Lightbits and Nutanix appeal to buyers who want to own their hardware or move off VMware. Nutanix is Everpure's partner and its competitor at the same time.
- **Most of these are niche threats one by one but matter together.** Qumulo, Cloudian, VDURA and Lenovo-owned Infinidat each have a defensible base. None is likely to displace Everpure broadly, but each caps its share in a segment.

## Why this matters for Everpure strategy

The VAST–WEKA–DDN fight ([Chapters 42–45](45-head-to-head.md)) and the incumbents ([Chapter 46](46-incumbents.md)) get the attention, but most of the threats to Everpure's (NYSE: P, formerly PSTG) margin come from layers it does not control. Hammerspace and the hyperscalers compete for the *namespace and control plane* above the array. Ceph, MinIO and Lightbits compete on *software running on commodity servers*, which caps what buyers will pay for an integrated system. Nutanix competes for the *platform*, the place where VMware-exit budgets land. Each one pressures Everpure's core claim that an integrated hardware-plus-Purity system with Evergreen economics beats assembling parts.

These players also define the M&A and partnership map. Most are private, sub-scale or newly owned. That makes them potential targets, partners or channels as well as rivals. A strategy team needs to know which ones to compete with, which to partner with, and which could sell for a reasonable price ([Chapter 54](../07-history-and-future/54-strategic-option-map.md)).

## Core concepts

### A map by architecture

The useful way to sort this crowd is by the *layer* each one competes for, not by revenue.

```mermaid
flowchart LR
    EP["Everpure FlashArray and FlashBlade"]
    subgraph NS["Namespace and file layer"]
        HS["Hammerspace: pNFS global namespace"]
        QU["Qumulo: scale-out NAS, Azure Native"]
        VD["VDURA: PanFS parallel file"]
    end
    subgraph OB["Object, software-defined"]
        MI["MinIO AIStor"]
        CL["Cloudian HyperStore"]
        CE["Ceph: IBM, Croit, Clyso, 45Drives"]
    end
    subgraph BL["Block"]
        LB["Lightbits: NVMe/TCP software"]
        IN["Infinidat, now Lenovo"]
    end
    subgraph PL["Platform"]
        NU["Nutanix: AHV, NUS, NKP"]
    end
    subgraph HY["Hyperscaler-native"]
        AW["AWS: S3, EBS, FSx"]
        AZ["Azure: Blob, ANF, Managed Lustre"]
        GC["Google: GCS, Managed Lustre"]
    end
    HS -. "sits above" .-> EP
    NU -. "partner and rival" .-> EP
    HY == "substitutes" ==> EP
    OB -- "competes with FlashBlade S3" --> EP
    BL -- "competes with FlashArray" --> EP
    NS -- "competes with FlashBlade file" --> EP
```

*Figure 47.1 — Challengers grouped by the layer they attack: Hammerspace sits above the array, software-defined object and block compete on commodity hardware, and the hyperscalers substitute for the whole stack.*

### Hammerspace: a namespace over everyone's storage

Hammerspace separates *where a file appears* from *where its bytes live*. Its metadata servers (Anvil) hold one global namespace. Data-services nodes (DSX) and existing NFS, object or cloud storage hold the bytes[^1]. Clients use the stock Linux NFSv4.2 client with the pNFS **Flex Files** layout. A client asks the metadata server where a file is, gets a layout, then reads and writes the storage nodes directly ([Chapter 8](../02-protocols-and-networking/08-file-protocols.md)). Policies ("objectives") move files between tiers and sites while they stay open, because only the layout changes. The file's identity does not.

**Semiconductor bridge.** This is virtual memory for files. The namespace is the page table. Data movement is page migration between DRAM and CXL-attached memory: the application keeps its address while the OS moves the physical page. Hammerspace's moat is the MMU-equivalent: it sits in the Linux kernel. Its CTO, Trond Myklebust, is the upstream Linux NFS client maintainer[^2]. Tuning the client everyone already runs is a hard advantage to copy.

**Tier 0.** Launched in November 2024, Tier 0 pools the local NVMe drives inside GPU servers into a shared, protected tier in the same namespace[^3]. Hammerspace's description treats GPU nodes as storage nodes grouped into volume groups and availability zones, protected by client-side mirroring. Client-side erasure coding is listed as roadmap[^4]. Version 5.2 added "affinitization", which writes a client's data to its own local Tier 0 volume first[^5].

```mermaid
flowchart TB
    subgraph SITE["AI cluster, site A"]
        G1["GPU server 1: local NVMe, Tier 0"]
        G2["GPU server 2: local NVMe, Tier 0"]
        T1["Existing NAS or flash array, Tier 1"]
    end
    MD["Anvil metadata: one global namespace"]
    PO["Policy objectives: placement, protection, cost"]
    DX["DSX data movers"]
    OBJ["On-prem object store, Tier 2"]
    CLD["Cloud region or site B"]
    G1 -- "pNFS layout request" --> MD
    G1 == "direct data I/O" ==> G2
    G2 == "direct data I/O" ==> T1
    PO --> MD
    MD --> DX
    DX -- "live migration" --> T1
    DX -- "tier down" --> OBJ
    DX -- "replicate" --> CLD
```

*Figure 47.2 — Hammerspace keeps file identity in one metadata layer and moves bytes freely across GPU-local NVMe, existing arrays, object and cloud, so the array becomes one tier among several.*

**Worked example (illustrative).** Assume a 1,000-server GPU cluster in which each server ships with eight 3.84 TB NVMe drives, a common configuration in DGX-class systems. That is 1,000 × 8 × 3.84 TB ≈ **30.7 PB raw**, already paid for and mostly idle. With two-way mirroring, roughly 15 PB is usable. If each Gen4 drive streams about 6 GB/s, the aggregate local bandwidth is 1,000 × 8 × 6 ≈ **48 TB/s**, far above any shared array in the cluster. The catches are real. A server reboot takes its drives offline. Mirroring traffic crosses the same network the GPUs use. The capacity is stranded inside servers on the server refresh cycle. In practice Tier 0 suits checkpoints and scratch data, with durable copies drained to a shared tier ([Chapter 31](../05-ai-storage/31-training-storage.md)).

**Why it has customers.** The flagship proof point is Meta. Its two 24,576-GPU GenAI clusters used a parallel NFS deployment co-developed with Hammerspace, alongside Tectonic[^6]. Hammerspace raised a US$100M Series B led by Altimeter in April 2025, at a valuation sources put above US$500M (*reported by press*), and talked about an IPO within about two years[^7]. The weak spots: it holds no NVIDIA SuperPOD or NVIDIA-Certified Storage designation[^8], and its performance depends on whatever storage sits underneath.

### Qumulo and VDURA: file specialists that changed their business model

**Qumulo** built a scale-out NAS with real-time analytics on capacity and activity, popular in media, life sciences and research. Under CEO Doug Gourlay (appointed July 2024) it moved from selling its own hardware to selling software for cloud, on-premises and edge[^9]. Its most distinctive asset is **Azure Native Qumulo**, a file service sold and billed inside Azure. In June 2026 Qumulo expanded the Microsoft relationship with tooling to migrate legacy NAS data into it, pitched at buyers facing hardware shortages[^10]. Its last priced round was a US$125M Series E at a US$1.2B valuation in July 2020 (*company-stated*)[^11]. No later round was found, so the current valuation is unknown [VERIFY: Qumulo funding since 2020]. Customers stay for simplicity and visibility into billions of files, not peak GPU throughput.

**VDURA** is Panasas renamed. It rebranded in May 2024 as a software-first company[^12] and in 2025 relaunched PanFS as an AI/HPC data platform aimed at VAST, WEKA and DDN, with a V5000 all-flash appliance and, from March 2026, hybrid flash-plus-disk configurations[^13]. It claims a major defense GPU installation (*company-stated*)[^14]. The appeal is decades of production parallel-file-system history at national labs, plus hybrid disk economics while flash prices are high. The risk is scale. Funding totals are unclear and no 2025–2026 round was found [VERIFY: VDURA funding].

### MinIO: the open-source object store that closed itself

MinIO became the default S3-compatible store for developers, Kubernetes and many neoclouds because it was a single binary that was fast on NVMe and free. It raised US$103M at a US$1B valuation in January 2022, led by Intel Capital[^15]. Then it pulled the community edition back in stages:

1. **June 2025:** the admin console was removed from the community edition, leaving a basic object browser; administration moved to the CLI or the paid AIStor[^16].
2. **Late 2025:** official binaries and Docker images stopped being updated [VERIFY: exact date, reported as October 2025], and on 3 December 2025 the project entered maintenance mode, with no new features and security fixes only case by case[^17].
3. **2026:** the README was changed to say the repository is no longer maintained (reportedly 12 February [VERIFY: date]), and GitHub shows `minio/minio` **archived on 25 April 2026**. The source stays available under AGPLv3, and the README points users to the AIStor Free and AIStor Enterprise editions[^18].

**Semiconductor bridge.** It resembles a licensor changing terms after an ecosystem has standardized on its architecture. Each licensee has to choose: pay, fork, or port to another architecture. Users had the same three options. Community forks appeared[^19]. The obvious porting targets were Ceph RGW and commercial S3 stores.

AIStor itself is a serious product. It shipped S3 over RDMA in November 2024[^20] and MinIO is an NVIDIA STX storage partner[^21]. **Worked example:** a neocloud with 50 PB on community MinIO that decides to migrate. Even at a sustained 100 GB/s, a full copy takes 50 × 10¹⁵ ÷ 10¹¹ = 500,000 s ≈ **5.8 days** of saturated transfer. Allow for verification, cut-over and production traffic, and it becomes a multi-week project. That friction is why many will pay MinIO instead of leaving.

### Cloudian and Ceph: object for people who want control

**Cloudian HyperStore** is an S3-native object store sold as software or appliances, strong with on-premises S3 buyers in regulated industries and in Japan, and also sold through HPE GreenLake. In June 2024 it raised US$23M of growth financing from Morgan Stanley Expansion Capital, reporting 30% ARR growth and breakeven, with about US$256M raised in total (*company-stated*)[^22]. It was early to GPUDirect-style object, showing S3 over RDMA in November 2024 with a claimed 200+ GB/s[^23]. Its HyperScale AI Data Platform puts vector search inside the storage layer[^24]. HyperStore 8.2.6 earned the Foundation level of NVIDIA-Certified Storage in March 2026[^25].

**Ceph** is the Linux of storage: one open-source system offering block (RBD), file (CephFS) and object (RGW). It is free as code and expensive to run well. Clyso tuned a 68-node all-NVMe cluster past 1 TiB/s and documented the laggy-placement-group problems it hit along the way[^26], which shows both the ceiling and the expertise needed. Commercial packaging splits into three types:

- **IBM Storage Ceph**, inherited from Red Hat, with release 9.0 in January 2026[^27].
- **Software and support specialists**, Croit (management software and support) and Clyso (engineering and consulting).
- **Hardware integrators** such as 45Drives, which ships servers with its Houston management UI for Ceph deployment[^28].

The RISC-V analogy fits. The ISA is free and the value accrues to implementers who make it reliable. Ceph buyers are telcos, universities, sovereign clouds and neoclouds that value no lock-in and have engineers to spare.

### Block and platform: Lightbits, Infinidat, Nutanix

**Lightbits** sells software-defined block storage over NVMe/TCP, the standard it helped create ([Chapter 7](../02-protocols-and-networking/07-block-protocols.md)). Any Ethernet NIC works, and clusters run on commodity servers. Its showcase is Crusoe, whose AI cloud block storage runs on Lightbits and grew to multi-petabyte scale[^29][^30]. Last disclosed funding was US$42M in 2022, for US$105.3M total[^31]. Neoclouds choose it to build an EBS-like service on their own hardware.

**Infinidat** builds InfiniBox, a high-end block array that serves most reads from DRAM over large HDD or flash pools, with aggressive price and performance guarantees. Lenovo announced the purchase in January 2025 and closed it in April 2026. Infinidat now runs inside Lenovo's Infrastructure Solutions Group[^32]. Terms were undisclosed. Calcalist estimated over US$500M (*estimated*)[^33]. The strategic change is distribution. A sub-scale specialist now has a global server vendor's sales force behind it in large enterprise accounts.

**Nutanix** is a platform company whose storage (Nutanix Unified Storage: Files, Objects, Volumes) comes with its AHV hypervisor and its Kubernetes platform, NKP, launched in 2024 from the D2iQ acquisition[^34]. Broadcom's VMware licensing changes are the tailwind. Nutanix reported more than 1,000 new logos in fiscal Q2 2026, the most in eight years, and said most came from VMware customers [VERIFY: search-summary only][^35]. Fiscal 2026 ARR reached US$2.55B, up 16%[^36]. The twist is that Nutanix has opened AHV to external arrays: Dell PowerFlex, then Pure Storage FlashArray over NVMe/TCP (May 2025), then NetApp ONTAP and Dell PowerStore[^37][^38]. Nutanix Unified Storage also earned NVIDIA-Certified status in 2026[^39].

### The biggest challenger: hyperscaler-native storage

The hyperscalers each sell a full storage menu. AWS has S3, EBS and FSx (Lustre, NetApp ONTAP, OpenZFS, Windows). Azure has Blob, Azure NetApp Files and Azure Managed Lustre. Google has Cloud Storage and Managed Lustre. The scale is in a different class. S3 alone holds more than 500 trillion objects and serves more than 200 million requests per second across hundreds of exabytes[^40]. These services are also moving up the stack: S3 Vectors reached general availability in December 2025[^41].

The pattern matches hyperscaler custom silicon. Graviton, Trainium and TPU did not beat merchant chips everywhere. They took the workloads already in the cloud, and merchant vendors priced against them. Two details matter for array vendors. First, hyperscalers will rent a partner's technology as a first-party service when that is quicker than building it. Google Cloud Managed Lustre runs on DDN EXAScaler and went GA in July 2025[^42]. NetApp's first-party and marketplace cloud storage revenue grew 27% year on year in fiscal Q3 2026[^43]. Second, the cloud services now compete on AI performance. Azure Managed Lustre was the first hyperscale cloud service in MLPerf Storage, at 642.2 GiB/s checkpoint write in v3.0[^44]. Google's DAOS-based Parallelstore is reportedly being phased out in favour of Managed Lustre [VERIFY: Parallelstore deprecation, partner source only][^45].

## How Everpure approaches it vs. competitors

| Company | Architecture | Model | Funding / ownership | Notable customers / proof points | Threat to Everpure (judgment) |
|---|---|---|---|---|---|
| Hyperscaler-native (AWS, Azure, Google) | Proprietary object, block, file; partner-built file services | Cloud service | Public parents | S3: 500T+ objects[^40]; Azure Managed Lustre in MLPerf v3.0[^44] | **High.** Substitutes for the whole stack for cloud-born data. Everpure can only partner (Azure Native) or win repatriation. |
| Hammerspace | pNFS Flex Files global namespace; Tier 0 on GPU-local NVMe | Software | Private; US$100M Series B 2025, >US$500M valuation (*reported*)[^7] | Meta GenAI clusters[^6] | **Medium-high.** Sits above arrays and commoditizes them, but can also run on FlashBlade. |
| Nutanix | HCI plus external arrays; NUS file and object | Software platform | Public (NASDAQ: NTNX); ARR US$2.55B[^36] | VMware-exit mid-market | **Medium.** Wins platform budgets, yet also a FlashArray channel. |
| MinIO AIStor | Hash-placed erasure-coded object | Software (commercial) | Private; US$103M at US$1B, 2022 (*company-stated*)[^15] | Developer and neocloud S3 | **Medium-low.** Licensing fallout creates openings for FlashBlade S3. |
| Ceph (IBM, Croit, Clyso, 45Drives) | Open-source unified block, file, object | Open source plus support/hardware | IBM (public); others private | Telcos, academia, sovereign clouds | **Medium** on price. Sets the floor for commodity object. |
| Lenovo Infinidat | DRAM-cached high-end block | Appliance | Lenovo-owned, closed April 2026[^32] | Large enterprises, service providers | **Medium** in high-end block, through Lenovo's reach. |
| Cloudian | S3-native object | Software / appliance | Private; ~US$256M raised (*company-stated*)[^22] | Regulated industries, HPE GreenLake | **Low-medium.** Strong on-premises S3 niche. |
| Qumulo | Scale-out NAS; Azure Native Qumulo | Software / cloud | Private; last round 2020, US$1.2B (*company-stated*)[^11] | Media, life sciences | **Low-medium.** Competes with FlashBlade file in mid-range. |
| Lightbits | NVMe/TCP software block | Software | Private; US$105.3M total by 2022[^31] | Crusoe[^29] | **Low-medium.** Neocloud block, where FlashArray rarely plays. |
| VDURA | PanFS parallel file, hybrid flash/HDD | Appliance / software | Private; funding unclear | HPC labs, defense (*company-stated*)[^14] | **Low.** Sub-scale, but credible in HPC deals. |

*Table 47.1 — The threat ranking follows layer, not size: whoever owns the namespace or the cloud account matters more than another box vendor.*

Everpure's answers differ by layer. Against **hyperscalers** it brings Purity into the cloud: Pure Storage Cloud Azure Native is a jointly developed, Microsoft-billed managed service[^46], and its second top-five hyperscaler DirectFlash design win (August 2026) turns hyperscalers into customers. The steelman is NetApp, whose ONTAP is a first-party service on all three clouds. Everpure has no equivalent on AWS or Google. Against **Hammerspace**, FlashBlade//EXA uses the same pNFS idea with Everpure's metadata engine. The real question is whether Everpure treats Hammerspace as a namespace partner over FlashBlade or as a layer that turns FlashBlade into a commodity. Against **Ceph, MinIO and Lightbits**, Everpure sells operational simplicity and Evergreen economics against "free plus engineers". It wins where staff are scarce and loses where the customer *is* a team of storage engineers. With **Nutanix**, the May 2025 FlashArray integration means Everpure gains when VMware exits go to AHV with external storage, and loses when they go to Nutanix's own storage.

## History and trajectory

```mermaid
timeline
    title Selected challenger funding, M&A and licensing events, 2024-2026
    2024 : May - Panasas rebrands as VDURA : Jun - Cloudian raises USD 23M growth financing : Jul - Qumulo appoints Doug Gourlay CEO : Oct - Lightbits expands Crusoe deal : Nov - Hammerspace launches Tier 0 : Nov - MinIO AIStor and Cloudian ship S3 over RDMA
    2025 : Jan - Lenovo agrees to buy Infinidat : Apr - Hammerspace raises USD 100M Series B : May - Nutanix adds FlashArray for AHV : Jun - MinIO strips community console : Jul - Google Managed Lustre GA on DDN : Dec - MinIO community enters maintenance mode
    2026 : Jan - IBM Storage Ceph 9.0 : Mar - Cloudian earns NVIDIA certification : Apr - Lenovo closes Infinidat : Apr - MinIO repository archived : Jun - Qumulo expands Azure Native work : Aug - Nutanix FY26 ARR reaches USD 2.55B
```

*Figure 47.3 — Funding was small and sporadic. The defining events were a strategic acquisition, a licence retreat and the cloud and platform vendors moving in.*

Every event in Figure 47.3 is sourced in the sections above. Three signals stand out. **First, capital went elsewhere.** Hammerspace's US$100M round is the largest disclosed primary raise here in 2024–2026, while VAST raised about US$1B in 2026 alone ([Chapter 42](42-vast-data.md)). Most of this group are long-lived, venture-funded companies with no fresh priced rounds, a classic setup for consolidation. A CB Insights entry lists a further Hammerspace "Series B-II" in February 2026 with no amount [VERIFY: single aggregator][^47]. **Second, open source is being monetized harder.** MinIO's retreat follows a wider industry pattern of relicensing, and it strengthens Ceph's position as the neutral default. **Third, the platform owners are absorbing storage.** Lenovo bought Infinidat, Nutanix bundles storage with its hypervisor, and the clouds rent Lustre and ONTAP as their own services. The likely next steps, as public signals suggest, are more server-vendor and platform acquisitions of sub-scale storage software, and Hammerspace either reaching an IPO or being bought, as an analyst quoted at its Series B suggested.

## Numbers that matter

| Metric | Value | Context | Source / date |
|---|---|---|---|
| Amazon S3 scale | >500 trillion objects; >200M requests/s | Hundreds of exabytes | AWS, 2026-03-16[^40] |
| Hammerspace Series B | US$100M; valuation >US$500M (*reported*) | Led by Altimeter; IPO talk | TechCrunch, 2025-04-16[^7] |
| GPU-local NVMe in a 1,000-server cluster | ~30.7 PB raw; ~48 TB/s aggregate | 8 × 3.84 TB per server, ~6 GB/s per drive | Worked example |
| MinIO Series B | US$103M at US$1B valuation | Jan 2022, led by Intel Capital | SiliconANGLE, 2022-01-26[^15] |
| Nutanix ARR | US$2.55B, +16% YoY | FY ended 2026-07-31; methodology restated | Nutanix 8-K, 2026-08-26[^36] |
| NetApp first-party and marketplace cloud storage growth | +27% YoY | Fiscal Q3 2026 | NetApp, 2026-02[^43] |
| Cloudian total raised | ~US$256M; ARR +30% | June 2024, breakeven claimed (*company-stated*) | Blocks & Files, 2024-06-25[^22] |
| Azure Managed Lustre MLPerf v3.0 | 642.2 GiB/s checkpoint write | First hyperscale cloud submission | StorageReview, 2026-09[^44] |
| Ceph record cluster | >1 TiB/s on 68 nodes | Clyso tuning project | Ceph.io, 2024-01[^26] |

## Conversation playbook

**Questions for a PM**

1. *"When a customer runs Hammerspace over FlashBlade, who owns the account?"* A strong answer separates the namespace from capacity. It knows whether Everpure has joint references with Hammerspace and what EXA's pNFS offers that Hammerspace's does not, such as metadata performance and Evergreen.
2. *"How many MinIO community users have we converted since December 2025, and through which product?"* Strong: names FlashBlade S3 versus FlashArray S3, the typical size, the competing Ceph or AIStor quote, and the migration tooling.
3. *"What share of Nutanix AHV migrations attach FlashArray versus Nutanix's own storage?"* Strong: gives an attach rate or at least a trend, and knows how Nutanix's sales team is paid on each.

**Questions for an engineer**

1. *"What does Tier 0 lose if a GPU server reboots mid-checkpoint, and how does EXA handle the same failure?"* Strong: discusses mirror placement across failure domains, rebuild traffic on the GPU fabric, and the drain-to-shared-tier pattern.
2. *"Where is our S3 slower than Ceph RGW or AIStor on small objects, and why?"* Strong: gives a measured objects-per-second number and points to metadata path differences ([Chapter 18](../03-system-architecture/18-object-storage-architecture.md)).
3. *"Could Purity run as a first-party-style service on AWS, as ONTAP does with FSx?"* Strong: explains the engineering gap (control plane, multi-tenancy, billing integration) separately from the commercial one.

**Don't say this:**

- "MinIO is dead." The open-source repository is archived. AIStor is actively sold and NVIDIA-partnered.
- "Hammerspace is a storage array competitor." It is a namespace and orchestration layer. It can sit on top of Everpure.
- "Ceph is free." The code is free. Running it at scale costs engineers, and that cost is what Everpure sells against.
- "Nutanix is just a competitor." Since May 2025 it has also been a route to market for FlashArray.
- "The cloud is just another competitor." It is the default location for new data. Everpure partners with the clouds as much as it competes with them.

## Going deeper (optional, L3 pointers)

- IETF RFC 8435 (pNFS Flexible File Layout) and Myklebust's SNIA SDC 2024 talk on pNFS and NFSv4.2 advances[^2].
- Hammerspace's SNIA SDC 2025 slides on Tier 0, covering volume groups, availability zones and client-side mirroring[^4].
- Clyso's "Journey to 1 TiB/s" write-up, for real-world Ceph tuning on NVMe[^26].
- Meta's GenAI infrastructure post, for how a hyperscaler mixes in-house Tectonic with vendor parallel NFS[^6].

## Key terms

- **Global namespace** — one file tree that spans many storage systems and sites.
- **Tier 0** — Hammerspace's shared tier built from GPU servers' local NVMe.
- **pNFS Flex Files** — the NFSv4.2 layout that lets clients do I/O directly against data servers.
- **AIStor** — MinIO's commercial object storage product.
- **Open-core relicensing** — narrowing or restricting a free edition to push users toward paid editions.
- **Ceph RGW / RBD / CephFS** — Ceph's object, block and file interfaces.
- **NVMe/TCP** — NVMe over standard TCP/IP Ethernet.
- **First-party cloud storage service** — a partner's storage sold and billed by the cloud provider as its own service.
- See the [glossary](../glossary.md) for the rest.

## Sources

[^1]: Hammerspace, "Hyperscale NAS," n.d. https://hammerspace.com/hyperscale-nas/ (retrieved 2026-11-01); Futurum, "Hammerspace shows storage acceleration for AI training at AI Field Day," n.d. https://futurumgroup.com/insights/hammerspace-shows-storage-acceleration-for-ai-training-at-ai-field-day (retrieved 2026-11-01).
[^2]: SNIA, Trond Myklebust (Hammerspace), "Advancements in pNFS and NFSv4.2," SDC 2024 (posted 2025-05). https://snia.org/sites/default/files/2025-05/SNIA-SDC2024-Myklebust-Advancements-in-PNFS-NFSv4.2.pdf (retrieved 2026-11-01).
[^3]: Hammerspace via Business Wire, "Hammerspace Transforms GPU Computing Infrastructure as First to Unlock a New Tier of Ultra-Fast Shared Storage," 2024-11-14. https://www.businesswire.com/news/home/20241114167051/en (retrieved 2026-11-01).
[^4]: SNIA, Christofferson (Hammerspace), "Activating Tier 0 Storage," SDC 2025 (posted 2025-10). https://www.snia.org/sites/default/files/2025-10/SNIA-SDC25-Christofferson-Activating-Tier0-Storage.pdf (retrieved 2026-11-01).
[^5]: Hammerspace, "Hammerspace Tier 0 Affinitization," 2026. https://hammerspace.com/hammerspace-tier-0-affinitization/ (retrieved 2026-11-01).
[^6]: Meta Engineering, "Building Meta's GenAI Infrastructure," 2024-03-12. https://engineering.fb.com/2024/03/12/data-center-engineering/building-metas-genai-infrastructure/ (retrieved 2026-11-01).
[^7]: TechCrunch, "Hammerspace, an unstructured data wrangler, raises $100M," 2025-04-16. https://techcrunch.com/2025/04/16/hammerspace-an-unstructured-data-wrangler-100m/ (retrieved 2026-11-01); TechTarget, "Hammerspace vacuums $100 million in Series B to gear for IPO," 2025-04. https://www.techtarget.com/searchstorage/news/366622858/Hammerspace-vacuums-100-million-in-Series-B-to-gear-for-IPO (retrieved 2026-11-01).
[^8]: StorageReview, "Best Storage Arrays 2026: AI Storage Leaders and Audited Results," updated 2026-09-01. https://www.storagereview.com/best/storage-arrays (retrieved 2026-11-01).
[^9]: GeekWire, "Former Arista and Cisco exec Douglas Gourlay named new CEO of data storage company Qumulo," 2024-07. https://www.geekwire.com/2024/former-arista-and-cisco-exec-douglas-gourlay-named-new-ceo-of-data-storage-company-qumulo/ (retrieved 2026-11-01).
[^10]: Qumulo via Business Wire, "Qumulo Announces Expanded Collaboration with Microsoft to Deliver Cloud Native Storage Relief for the Enterprise Hardware Crisis," 2026-06-03. https://secure.businesswire.com/news/home/20260603197198/en/Qumulo-Announces-Expanded-Collaboration-with-Microsoft-to-Deliver-Cloud-Native-Storage-Relief-for-the-Enterprise-Hardware-Crisis (retrieved 2026-11-01).
[^11]: HPCwire/AIwire, "Qumulo Locks Down $125M Financing, $1.2B Valuation," 2020-07-23. https://www.hpcwire.com/aiwire/2020/07/23/qumulo-locks-down-125m-financing-1-2b-valuation/ (retrieved 2026-11-01).
[^12]: VDURA via Business Wire, "Panasas becomes VDURA" (launch of the VDURA brand), 2024-05-07. https://www.businesswire.com/news/home/20240507806456/en (retrieved 2026-11-01).
[^13]: Blocks & Files, "VDURA takes aim at VAST, WEKA, DDN with AI-HPC storage reboot," 2025-06-28. https://www.blocksandfiles.com/ai-ml/2025/06/28/vdura-takes-aim-at-vast-weka-ddn-with-ai-hpc-storage-reboot/1586714 (retrieved 2026-11-01); Blocks & Files, "VDURA pairs V5000 flash with WD Data60 and Data102 disk shelves," 2026-03-11. https://www.blocksandfiles.com/disk/2026/03/11/vdura-pairs-v5000-flash-with-wd-data60-and-data102-disk-shelves/5208754 (retrieved 2026-11-01).
[^14]: VDURA via Business Wire, "VDURA Powers One of the World's Largest Defense GPU Installations," 2025-10-02. https://www.businesswire.com/news/home/20251002832210/en/VDURA-Powers-One-of-the-Worlds-Largest-Defense-GPU-Installations (retrieved 2026-11-01).
[^15]: SiliconANGLE, "MinIO raises $103M to expand multicloud data object store," 2022-01-26. https://siliconangle.com/2022/01/26/minio-raises-103m-expand-multicloud-data-object-store/ (retrieved 2026-11-01).
[^16]: Blocks & Files, "MinIO removes management features from basic community edition object storage code," 2025-06-19. https://blocksandfiles.com/2025/06/19/minio-removes-management-features-from-basic-community-edition-object-storage-code/ (retrieved 2026-11-01).
[^17]: Linuxiac, "MinIO Ends Active Development, Steers Users Toward Paid AIStor," 2025-12. https://linuxiac.com/minio-ends-active-development/ (retrieved 2026-11-01).
[^18]: GitHub, "minio/minio" repository page (archive banner dated 2026-04-25; README notice "no longer maintained"), n.d. https://github.com/minio/minio (retrieved 2026-11-01).
[^19]: Vonng, "MinIO Is Dead, Long Live MinIO" (community fork pgsty/minio), n.d. https://blog.vonng.com/en/db/minio-resurrect/ (retrieved 2026-11-01).
[^20]: Blocks & Files, "MinIO releases AIStor with GPUDirect-like S3 over RDMA," 2024-11-13. https://blocksandfiles.com/2024/11/13/minio-releases-aistor-with-gpudirect-like-s3-over-rdma/ (retrieved 2026-11-01).
[^21]: StorageNewsletter, "Nvidia GTC 2026: Nvidia Launches BlueField-4 STX Storage Architecture With Broad Industry Adoption," 2026-03-17. https://www.storagenewsletter.com/2026/03/17/nvidia-gtc-2026-nvidia-launches-bluefield-4-stx-storage-architecture-with-broad-industry-adoption/ (retrieved 2026-11-01).
[^22]: Blocks & Files, "Cloudian gets more funding as it reaches breakeven, bags HPE GreenLake wins," 2024-06-25. https://blocksandfiles.com/2024/06/25/cloudian-gets-more-funding-as-it-reaches-breakeven-bags-hpe-greenlake-wins/ (retrieved 2026-11-01); StorageNewsletter, "Cloudian Secures $23 Million, Total at $256 Million," 2024-06-25. https://www.storagenewsletter.com/2024/06/25/cloudian-secures-23-million-total-at-256-million/ (retrieved 2026-11-01).
[^23]: IT Brief, "Cloudian enhances AI processing with NVIDIA GPUDirect tie-up," 2024-11. https://itbrief.co.uk/story/cloudian-enhances-ai-processing-with-nvidia-gpudirect-tie-up (retrieved 2026-11-01).
[^24]: Blocks & Files, "Cloudian launches HyperScale AI platform built on Nvidia Blackwell GPUs," 2025-10-01. https://www.blocksandfiles.com/ai-ml/2025/10/01/cloudian-launches-hyperscale-ai-platform-built-on-nvidia-blackwell-gpus/1592771 (retrieved 2026-11-01).
[^25]: Cloudian, "Cloudian HyperStore Achieves NVIDIA-Certified Storage Designation," 2026-03-16. https://cloudian.com/press/cloudian-hyperstore-achieves-nvidia-certified-storage-designation.md (retrieved 2026-11-01).
[^26]: Ceph.io (Mark Nelson, Clyso), "Ceph: A Journey to 1 TiB/s," 2024-01. https://ceph.io/en/news/blog/2024/ceph-a-journey-to-1tibps (retrieved 2026-11-01).
[^27]: StorageNewsletter, "IBM Releases IBM Storage Ceph 9.0," 2026-01-30. https://www.storagenewsletter.com/2026/01/30/ibm-releases-ibm-storage-ceph-9-0/ (retrieved 2026-11-01).
[^28]: AIwire, "45Drives' new user interface helps manage open source storage software infrastructure," 2021-01-07. https://aiwire.net/2021/01/07/45drives-new-user-interface-helps-manage-open-source-storage-software-infrastructure (retrieved 2026-11-01).
[^29]: Lightbits via Business Wire, "Lightbits and Crusoe AI Announce Collaboration to Expand Elastic Block Storage Service for AI Workloads," 2024-10-29. https://www.businesswire.com/news/home/20241029168108/en/Lightbits-and-Crusoe-AI-Announce-Collaboration-to-Expand-Elastic-Block-Storage-Service-for-AI-Workloads (retrieved 2026-11-01).
[^30]: Lightbits via Business Wire, "Lightbits Labs Closes Q1 2025 with Record Breaking Growth," 2025-04-15. https://www.businesswire.com/news/home/20250415197129/en/Lightbits-Labs-Closes-Q1-2025-with-Record-Breaking-Growth (retrieved 2026-11-01).
[^31]: Blocks & Files, "Lightbits Labs funding," 2022-06-28. https://blocksandfiles.com/2022/06/28/lightbits-labs-funding/ (retrieved 2026-11-01).
[^32]: Lenovo, "Lenovo Completes Acquisition of Infinidat, Expanding Enterprise Storage Portfolio, Enhancing AI-Driven Data Infrastructure," 2026-04. https://news.lenovo.com/pressroom/press-releases/lenovo-completes-acquisition-of-infinidat-expanding-enterprise-storage-portfolio-enhancing-ai-driven-data-infrastructure/ (retrieved 2026-11-01); StorageNewsletter, same title, 2026-04-10. https://www.storagenewsletter.com/2026/04/10/lenovo-completes-acquisition-of-infinidat-expanding-enterprise-storage-portfolio-and-enhancing-ai-driven-data-infrastructure/ (retrieved 2026-11-01).
[^33]: Calcalist (CTech), report on the Lenovo–Infinidat deal value, n.d. https://www.calcalistech.com/ctechnews/article/bkjygubh11g (retrieved 2026-11-01).
[^34]: Nutanix, "Nutanix Announces Nutanix Kubernetes Platform," 2024-05. https://www.nutanix.com/blog/nutanix-announces-nutanix-kubernetes-platform (retrieved 2026-11-01).
[^35]: MarketBeat, "Nutanix Q2 Earnings Call Highlights," 2026-02-26. https://www.marketbeat.com/instant-alerts/nutanix-q2-earnings-call-highlights-2026-02-26/ (retrieved 2026-11-01).
[^36]: Nutanix, "Form 8-K, Exhibit 99.1: Fourth quarter and fiscal 2026 results," 2026-08-26. https://www.sec.gov/Archives/edgar/data/0001618732/000117184326005752/exh_991.htm (retrieved 2026-11-01); Earnings Whispers, "Nutanix Reports 16% YoY ARR Growth and Strong Free Cash Flow for Fiscal 2026," 2026-08-26. https://www.earningswhispers.com/article/NTNX/2608266552 (retrieved 2026-11-01).
[^37]: SDxCentral, "Nutanix partners with Pure Storage in latest VMware assault," 2025-05. https://www.sdxcentral.com/news/nutanix-partners-with-pure-storage-in-latest-vmware-assault/ (retrieved 2026-11-01).
[^38]: SDxCentral, "Dell, Nutanix launch their first external storage package," n.d. https://www.sdxcentral.com/news/dell-nutanix-launch-their-first-external-storage-package/ (retrieved 2026-11-01); IT Brief, "Nutanix links AHV with NetApp storage in new tie-up," n.d. https://itbrief.co.uk/story/nutanix-links-ahv-with-netapp-storage-in-new-tie-up (retrieved 2026-11-01); Blocks & Files, "Nutanix gets Dell PowerStore support," 2026-07-28. https://www.blocksandfiles.com/file/2026/07/28/nutanix-gets-dell-powerstore-support/5279629 (retrieved 2026-11-01).
[^39]: HPCwire/BigDATAwire, "Nutanix Unified Storage Achieves NVIDIA Certification as Enterprises Race to Build AI Factories," 2026-06. https://www.hpcwire.com/bigdatawire/this-just-in/nutanix-unified-storage-achieves-nvidia-certification-as-enterprises-race-to-build-ai-factories/ (retrieved 2026-11-01).
[^40]: AWS News Blog, "AWS Weekly Roundup: Amazon S3 turns 20, Amazon Route 53 Global Resolver general availability, and more," 2026-03-16. https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-s3-turns-20-amazon-route-53-global-resolver-general-availability-and-more-march-16-2026 (retrieved 2026-11-01).
[^41]: StorageNewsletter, "AWS re:Invent 2025: Amazon S3 Vectors is Now Generally Available with 40 Times the Scale of Preview," 2025-12-05. https://www.storagenewsletter.com/2025/12/05/aws-reinvent-2025-amazon-s3-vectors-is-now-generally-available-with-40-times-the-scale-of-preview/ (retrieved 2026-11-01).
[^42]: DDN, "DDN and Google Cloud bring high-performance parallel file systems to cloud AI workloads with Managed Lustre powered by DDN EXAScaler," 2025-07. https://www.ddn.com/blog/ddn-and-google-cloud-bring-high-performance-parallel-file-systems-to-cloud-ai-workloads-with-managed-lustre-powered-by-ddn-exascaler/ (retrieved 2026-11-01).
[^43]: NetApp, "Q3 FY26 Earnings Release," 2026-02. https://s21.q4cdn.com/371534297/files/doc_earnings/2026/q3/earnings-result/NetApp-Q3-26-Earnings-Release-final-final.pdf (retrieved 2026-11-01).
[^44]: StorageReview, "MLPerf Storage v3.0: 877 GiB/s checkpoints, a cloud first and a leaderboard turned over," 2026-09. https://storagereview.com/news/mlperf-storage-v3-0-877-gib-s-checkpoints-a-cloud-first-and-a-leaderboard-turned-over (retrieved 2026-11-01).
[^45]: innFactory, "Google Cloud Parallelstore," n.d. https://innfactory.de/en/cloud/gcp/products/parallelstore/ (retrieved 2026-11-01).
[^46]: Microsoft Learn, "Pure Storage Cloud overview," n.d. https://learn.microsoft.com/en-us/azure/partner-solutions/pure-storage/overview (retrieved 2026-11-01).
[^47]: CB Insights, "Hammerspace financials," 2026. https://www.cbinsights.com/company/hammerspace/financials (retrieved 2026-11-01).
