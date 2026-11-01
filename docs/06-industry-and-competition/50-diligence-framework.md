# 50. Technical diligence framework for storage/AI-data targets

> **Depth:** L2 · **Reading time:** ~10 min · **Last verified:** 2026-11-01
> **Prerequisites:** [Architecture decision matrix](../03-system-architecture/24-architecture-decision-matrix.md) · [Reading benchmarks](../05-ai-storage/37-reading-benchmarks.md) · [Distributed systems fundamentals](../03-system-architecture/20-distributed-systems-fundamentals.md) · [WEKA deep dive](43-weka.md)

## TL;DR

- **Storage diligence asks one question: will this code keep other people's data safe, fast and supportable at ten times today's scale?** Process mechanics are the same as for any software deal. What differs is that the critical risks are durability bugs, metadata walls and support load, and none of these appears in a data room by default.
- **Treat every performance number as a claim until you reproduce it.** Normalise it per node, per rack unit, per kW and per usable TB. Then run your own proof of concept (PoC) on your own workload shape ([Chapter 37](../05-ai-storage/37-reading-benchmarks.md)).
- **Field data beats models.** Annualised failure rates, rebuild-time distributions, data-loss incident logs and phone-home telemetry tell you more than any "eleven nines" durability figure.
- **Integration fit with Everpure has four seams: control plane, data path, licensing and channel.** The data path is the expensive one. Purity and DirectFlash assume a single operating system managing raw NAND, so a second file system is a second product line, not a feature.
- **Public data can score a target, but only roughly.** In this chapter's WEKA worked example, 38% of the scorecard weight rests on placeholders that only diligence access can resolve. The public-data score is 2.8 out of 5, with a plausible range of 2.1 to 3.7.

## Why this matters for Everpure strategy

The AI storage cycle has produced private companies with large valuations and immature evidence. WEKA was last priced at US$1.6B in May 2024[^1] and VAST at a reported US$30B in April 2026[^2]. Any build/buy/partner discussion at Everpure (NYSE: P, formerly PSTG) about AI data infrastructure ([Chapter 54](../07-history-and-future/54-strategic-option-map.md)) ends in technical questions that a financial model cannot answer. Does the architecture scale past the customer's next cluster? Has it ever lost data? Could it ever run under Fusion and on DirectFlash? Everpure's own record is a range of small and mid-sized software deals: StorReduce, Portworx at US$352.9M plus US$32.2M of retention payments[^3], and 1touch at US$125.0M in 2026[^4]. A frontier-AI target would be a different order of risk.

An ex-semis dealmaker already knows the analogous discipline. You would not buy a chip company on its datasheet. You would ask for characterisation data across process corners, the errata list, the yield and RMA history, the tape-out record against plan, and the third-party IP licences. Storage diligence maps onto each of these. Benchmarks are the datasheet. Data-loss incidents are the errata, except that they destroy customer data. Field failure rates are the RMA history, and open-source dependencies are the third-party IP.

## Core concepts

### The diligence flow

```mermaid
flowchart LR
    S["1 Screen - public signals"] --> T["2 Public-info teardown"]
    T --> G1{"Proceed?"}
    G1 -->|yes, NDA| M["3 Management technical sessions"]
    M --> P["4 Hands-on PoC and benchmark"]
    P --> G2{"Claims hold?"}
    G2 -->|yes| R["5 Reference calls"]
    R --> C["6 Code and architecture review - clean team"]
    C --> G3{"Integrable?"}
    G3 -->|yes| I["7 Integration plan"]
    G1 -->|no| X["Stop or monitor"]
    G2 -->|no| X
    G3 -->|no| X
```

*Figure 50.1 — Technical diligence is a funnel with three kill gates; the cheap public teardown should kill most targets before anyone signs an NDA.*

The order matters because access gets more expensive at each stage. The **public-info teardown** reads documentation, patents, benchmark submissions, GitHub repositories, job postings and partner certification lists. Vendor documentation is usually far more candid about limits than marketing is. **Management technical sessions** under NDA should be run by your own architects, not by the corp-dev team. **The PoC** is where most deals should die if they are going to die. Use the acquirer's hardware where possible, the acquirer's workload shape and the acquirer's engineers at the keyboard. **Reference calls** should include a churned customer and a customer at the largest deployed scale, not just the three the target offers. **Code review** happens late, under a clean-team protocol, because it exposes trade secrets and, if the deal fails, contaminates the acquirer's engineers.

### The dimensions that matter

**Architecture and its walls.** Every architecture class has a known first wall ([Chapter 24](../03-system-architecture/24-architecture-decision-matrix.md)). Shared-nothing clusters hit rebalancing and east-west traffic ([Chapter 15](../03-system-architecture/15-scale-out-shared-nothing.md)). Disaggregated shared-everything designs hit fabric and enclosure failure domains ([Chapter 16](../03-system-architecture/16-disaggregated-shared-everything.md)). Parallel file systems hit the metadata server ([Chapter 17](../03-system-architecture/17-parallel-file-systems.md)). Diligence asks which wall this target hits, at what scale, and whether the largest customer is already near it. A good engineering team will name its own wall in the first session, and evasion is a signal.

**Performance claims.** Normalise before comparing. Suppose a vendor claims 1 TB/s from a 40-node cluster. That is 25 GB/s per node. If each node is 2U with 2×400 GbE (100 GB/s of line rate), the system runs at 25% of wire speed, which is either honest headroom or a sign of a software ceiling. Ask about the client count, file sizes, read/write mix, the data-reduction assumption and whether the run was audited (MLPerf Storage, SPECstorage) or vendor-run. [Chapter 37](../05-ai-storage/37-reading-benchmarks.md) lists the gaming techniques.

**Scalability: capacity, performance and metadata are separate curves.** Capacity scaling is usually easy. Performance scaling is a slope to measure, not assume. Metadata scaling decides small-file and AI-dataset performance ([Chapter 21](../03-system-architecture/21-metadata.md)). Ask for the largest production cluster by node count, by file count and by metadata operations per second. These are three different numbers, and vendors usually quote only the flattering one.

**Metadata design.** The semiconductor bridge is tag RAM. A centralised metadata server is a single tag array that every access must consult, and it saturates. Sharded metadata spreads the load, but operations spanning shards, such as renames and snapshots, become distributed transactions. Ask how the namespace is partitioned, how cross-shard operations are made atomic, and what happens to metadata during a node failure.

**Durability and data integrity.** This is the dimension most likely to destroy deal value, and the one data rooms least often cover. Durability claims in "nines" are model outputs, mean time to data loss (MTTDL) estimates ([Chapter 20](../03-system-architecture/20-distributed-systems-fundamentals.md)), not field facts. Ask for evidence instead:

- **Erasure-coding geometry and rebuild behaviour** under realistic load ([Chapter 6](../01-storage-fundamentals/06-data-protection-and-resilience.md)).
- **End-to-end checksums.** Is data verified from client write to media read, and is there background scrubbing?
- **Field failure data.** As a public baseline, Backblaze reported a 1.36% annualised failure rate (AFR) across about 344,000 hard drives in 2025[^5].
- **The data-loss incident log.** This means every case where customer data was lost or corrupted, the root cause, the blast radius and the time to fix.

Worked example: a target with 500 clusters averaging 200 drives has 100,000 drives in the field. At 1% AFR that is 1,000 drive failures a year, roughly three rebuilds a day somewhere in the fleet. The question is not whether drives fail. It is how many rebuilds overlapped a second fault, and what happened then. Field telemetry is also how the industry learned about silent corruption. A FAST '08 study used NetApp's call-home data from 1.53 million drives over 41 months[^6]. A target without equivalent telemetry cannot answer the question at all.

**Security and ransomware resilience.** Check immutable snapshots that an administrator credential cannot delete (Everpure's equivalent is SafeMode), multi-party authorisation for destructive operations, and encryption-key management. Ask for the vulnerability-response history and whether the code has had external penetration tests. Multi-tenant isolation now matters for neocloud buyers.

**Roadmap credibility.** Treat the roadmap as a tape-out record. List what the target announced over the past three years with dates, and check when each item shipped generally available (GA). A team that slips by quarters is normal. One that re-announces the same feature is not.

**Code base and engineering team.** Map the people as well as the lines of code. Key questions are who wrote the data path and metadata engine, their tenure, whether they hold unvested equity and whether they will stay. Run a software composition analysis for open-source dependencies and licences. Copyleft matters here. Lustre is licensed under GPLv2[^7], so distributing modified Lustre kernel modules carries source-disclosure obligations. MinIO moved its server to AGPLv3 in 2021[^8], a licence whose obligations can be triggered by offering the software over a network. Licence disputes are real deal risks. In March 2023 MinIO publicly said it had revoked WEKA's licences, and WEKA replied that its fork derived only from Apache 2.0 code[^9]. No public resolution was found.

**Support burden and installed-base telemetry.** Get support tickets per installed system per year, the severity mix, the share of tickets the vendor detects first, and engineering's share of escalations. A hardware-agnostic product supporting many servers, NICs, kernels and clouds carries a large qualification matrix. That matrix is a cost centre that never appears in gross margin. Telemetry is itself an asset. HPE bought Nimble in 2017 largely for InfoSight[^10], and Pure1 META has run on phone-home data since 2017[^11].

**Hardware dependencies and supply chain.** An appliance vendor carries NAND exposure directly. Everpure raised prices in February 2026 as NAND costs surged[^12] ([Chapter 48](48-media-suppliers-and-nand-cycle.md)). A software-only vendor pushes that exposure to the customer but depends on partners' qualification and supply. Ask which components are single-sourced, which partners could defect, and whether the software assumes commodity SSDs with their own flash translation layer (FTL).

**Customer concentration.** AI-native storage revenue clusters in a few neoclouds and model builders whose spend follows GPU deliveries and their own financing ([Chapter 35](../05-ai-storage/35-ai-factories-and-neoclouds.md)). Get revenue by customer, contract length, committed versus consumed capacity, and any most-favoured-customer or exclusivity terms.

**Unit economics.** Gross margin depends on what is sold. Illustratively, software at 85% gross margin and pass-through hardware at 20% blend to 0.6 × 85% + 0.4 × 20% = **59%** if hardware is 40% of revenue. A target's margin can therefore move with packaging mix, independent of pricing power. For reference, Everpure's non-GAAP Q2 FY27 gross margin was 66.2% on product and 74.9% on subscription[^13] ([Chapter 29](../04-everpure/29-hyperscaler-ecosystem-financials.md)).

### Integration fit: the four seams

```mermaid
flowchart LR
    subgraph TGT["Target"]
        TC["Control plane and telemetry"]
        TD["Data path and client"]
        TL["Licence and price meter"]
        TS["Channel and OEM partners"]
    end
    subgraph EP["Everpure"]
        F["Fusion and Pure1"]
        PU["Purity on DirectFlash"]
        EG["Evergreen subscriptions"]
        CH["Everpure channel"]
    end
    TC -->|"API federation"| F
    TD -->|"parallel stack or port"| PU
    TL -->|"map meters and SLAs"| EG
    TS -->|"conflict check"| CH
```

*Figure 50.2 — Control-plane federation takes months; data-path convergence takes years, because Purity manages raw NAND that the target's software has never seen.*

**Control plane.** Fusion is the fleet control plane at the core of the Enterprise Data Cloud[^14] ([Chapter 22](../03-system-architecture/22-control-planes.md)). Exposing a target's clusters to Fusion and Pure1 through APIs is the cheapest form of integration. **Data path.** Purity runs the FTL across DirectFlash modules itself ([Chapter 26](../04-everpure/26-purity-and-directflash.md)). A target built for commodity SSDs either runs as a parallel stack on other hardware or is ported, a multi-year job. **Licensing.** Evergreen and Evergreen//One SLAs commit Everpure to performance and durability guarantees ([Chapter 28](../04-everpure/28-platform-and-software.md)). Anything sold under them inherits those obligations, which raises the durability bar. **Channel.** A target's OEM partners may be Everpure's competitors, and those relationships can end at close.

### The scorecard

| Dimension | Weight | 1 = red flag | 3 = acceptable | 5 = best in class |
|---|---|---|---|---|
| Architecture and walls | 10 | Wall within the next customer's scale; team cannot name it | Known wall beyond the current largest deployment | Wall well beyond roadmap scale, with a published mitigation |
| Performance claims | 8 | Vendor-run only; not reproducible | Some audited results; PoC within 20% of claims | Audited results in current rounds; PoC matches claims |
| Scalability (capacity, perf) | 7 | Sub-linear beyond a few dozen nodes | Near-linear to the largest customer | Proven linear at multiples of the largest customer |
| Metadata design | 6 | Single metadata server; small-file collapse | Scale-out metadata with known hot spots | Sharded, with atomic cross-shard operations at scale |
| Durability and integrity | 10 | Unexplained data-loss incidents; no end-to-end checksums | End-to-end checksums; incidents disclosed and fixed | Fleet telemetry, scrubbing, clean multi-year incident log |
| Security and ransomware | 6 | Snapshots deletable by an admin credential | Immutable snapshots; encryption at rest | Multi-party authorisation, tenant isolation, external pen tests |
| Roadmap credibility | 6 | Re-announced features; GA slips over a year | Slips of a quarter or two | Ships on announced dates |
| Code base and team | 10 | Key authors gone; copyleft contamination | Core authors retained; licences clean | Deep bench, low attrition, clean SBOM |
| Support burden | 6 | Huge qualification matrix; vendor rarely detects first | Manageable matrix; partial telemetry | Narrow matrix, call-home on most systems |
| Hardware and supply chain | 6 | Single-sourced critical parts; partner can defect | Multiple qualified sources | Hardware-portable, or sourced at scale |
| Customer concentration | 7 | One customer above 30% of revenue | Top 10 below 50% | Broad base across segments |
| Unit economics | 8 | Gross margin falling with mix; heavy burn | Stable margin; burn funded | Software-like margin; self-funding |
| Integration fit with Everpure | 10 | Full overlap with Purity; channel conflict | Partial overlap; Fusion federation feasible | Complementary layer; clean channel fit |

*Table 50.2 — A reusable 13-dimension scorecard, weighted toward the dimensions where a mistake costs the most after close (architecture, durability, team, integration).*

### Worked example: WEKA, public data only

WEKA is the chosen case because its public record ([Chapter 43](43-weka.md)) is unusually documented for a private company. It is a software-only target, which exercises every dimension. *This is a method illustration, not a recommendation, and it implies nothing about non-public Everpure plans.* Where public data is silent, the dimension gets a **placeholder 3** with low confidence.

| Dimension (weight) | Score | Known from public sources | Unknown without diligence access | Confidence |
|---|---|---|---|---|
| Architecture (10) | 4 | Kernel-bypass data path; proprietary client on every compute node[^21]; EC stripe fixed at cluster formation[^22] | Behaviour at the largest production scale | Medium |
| Performance (8) | 3 | Topped SPECstorage 2020 in 2025[^23]; absent from MLPerf Storage v3.0[^20]; AMG 20x TTFT claim is vendor-run[^24] | PoC on the acquirer's workloads | Medium |
| Scalability (7) | 3 | 16+4 EC implies ~80+ servers[^22] | Largest cluster by nodes, files, metadata ops | Low |
| Metadata (6) | 4 | Metadata hashed into buckets on every node[^26] | Cross-shard operation cost at scale | Medium |
| Durability (10) | 3 | 2 or 4 parity strips per stripe[^22] | Field AFR, rebuild data, incident log | Low |
| Security (6) | 3 | NeuralMesh 6 adds per-tenant keys and isolation[^27] | Immutability, pen tests, CVE history | Low |
| Roadmap (6) | 3 | AMG: unveiled March 2025[^28], available November 2025[^24]; NeuralMesh 6 GA planned 2H 2026[^27] | Whether NeuralMesh 6 hit GA on time | Medium |
| Team and code (10) | 2 | President, CFO, CRO left December 2024[^29]; next CFO left after four months[^30]; MinIO licence dispute[^9] | Key-author retention, SBOM | Medium |
| Support (6) | 2 | Many hardware partners[^31] and four clouds; HPE stopped reselling March 2026[^32] | Tickets per system, telemetry coverage | Medium |
| Hardware (6) | 3 | Software-only, but WEKApod 3 adds direct SSD exposure[^33] | WEKApod revenue share, supply terms | Medium |
| Customers (7) | 2 | References skew to neoclouds, AI labs and OCI[^34] | Revenue by customer | Low |
| Economics (8) | 3 | >US$100M ARR in 2024 *(company-stated)*[^25]; list ~US$339/TB/yr[^35] [VERIFY: single reseller listing] | Gross margin, burn, mix | Low |
| Integration fit (10) | 2 | Overlaps Purity//FB and EXA; proprietary client vs pNFS; OEM partners compete with Everpure | Port effort to DirectFlash | Medium |

*Table 50.3 — Public data is decent on architecture and roadmap but silent on durability, customers and economics, the dimensions a buyer most needs.*

```mermaid
xychart-beta
    title "WEKA public-data scorecard - illustrative worked example"
    x-axis ["Arch", "Perf", "Scale?", "Meta", "Durab?", "Secur?", "Road", "Team", "Support", "HW", "Cust?", "Econ?", "Integ"]
    y-axis "Score 1 to 5" 0 --> 5
    bar [4, 3, 3, 4, 3, 3, 3, 2, 2, 3, 2, 3, 2]
```

*Figure 50.3 — WEKA scores well on engineering and poorly on team stability, support load and Everpure fit; "?" marks low-confidence placeholders.*

**Reading the result.** The weighted score is 283 ÷ 100 = **2.83**. The five low-confidence dimensions carry 38 points of weight. Scoring them all 1 gives 2.14, and scoring them all 5 gives 3.66. Public data therefore cannot tell a mediocre target from a good one. What it *can* do is set the diligence agenda: field durability data, customer concentration and gross-margin mix come first.

**Options a strategy team might evaluate, based on public information.** The score favours lighter-touch options over a full acquisition. These include interoperability (Everpure object storage as a WEKA tier), competing directly with PureKVA against AMG, or monitoring signals such as financing events and MLPerf participation ([Chapter 43](43-weka.md)). The integration score of 2 reflects data-path overlap, the costliest seam. A tech-and-team deal would score differently on that dimension, but much lower on retention risk. The same template applied to VAST ([Chapter 42](42-vast-data.md)) or DDN ([Chapter 44](44-ddn.md)) would raise other questions: valuation and data-reduction IP for VAST, Lustre GPL obligations and appliance margin for DDN.

## How Everpure approaches it vs. competitors

| Acquirer | Deal | What was bought | Integration pattern | Diligence lesson |
|---|---|---|---|---|
| Pure Storage (now Everpure) | StorReduce, 2018, US$20.5M[^15] | Dedupe for cloud object storage | Technology tuck-in | Small deals are bets on code and team |
| Pure Storage | Portworx, 2020, US$352.9M + US$32.2M retention[^3] | Kubernetes data services that run on any storage | Separate brand, hardware-agnostic | Retention structure is part of the price |
| Everpure | 1touch, 2026, US$125.0M[^4] | Data discovery and classification | Relaunched as Everpure Data Intelligence[^16] | Control-plane fit is the cheap seam |
| HPE | Nimble, 2017, US$1.09B[^17] | Arrays plus InfoSight telemetry | Telemetry extended across the portfolio[^10] | Installed-base data can be the asset |
| EMC | XtremIO, 2012, ~US$430M *(reported)*[^18] | Pre-revenue flash architecture | Separate product line | Pure architecture bets need deep code review |
| EMC | Isilon, 2010, ~US$2.25B[^19] | Scale-out NAS | Separate product line | The architecture outlived the acquirer's independence |

*Table 50.1 — Storage acquirers have mostly kept acquired data paths as separate product lines and integrated only the control plane, which is the pattern a diligence plan should price in.*

Everpure's pattern differs from that of portfolio incumbents. Dell and HPE run several data paths side by side. Everpure's moat is one OS, Purity, on one hardware architecture, DirectFlash, sold under one subscription model, Evergreen. That makes the data-path seam costlier for Everpure than for Dell. A second file system weakens the "one platform" story. The steelman for the portfolio approach is speed: Dell can own a market segment the day a deal closes. Everpure's approach, building EXA in-house and buying software around the edges (Portworx, 1touch), keeps the platform coherent at the cost of time to market. Diligence should test which of these the target's value depends on.

## History and trajectory

Storage technical diligence grew out of the flash wave. When EMC bought XtremIO before it had product revenue[^18], the diligence was almost entirely architecture and team. HPE's Nimble deal made installed-base telemetry a diligence object in its own right[^10]. Portworx moved the focus to cloud-native software, Kubernetes ecosystems and engineer retention[^3]. AI targets add three new layers. The first is GPU-path claims such as GPUDirect and KV-cache offload, which are rarely audited. The second is NVIDIA certification status, which partners do not control ([Chapter 34](../05-ai-storage/34-nvidia-ecosystem.md)). The third is neocloud concentration. Valuations have also outrun evidence. The audited benchmark record for KV-cache workloads began only with MLPerf Storage v3.0 in September 2026[^20].

## Numbers that matter

| Metric | Value | Context | Source / date |
|---|---|---|---|
| HDD annualised failure rate, 2025 | 1.36% (about 344,000 drives) | Public baseline for a target's field claims | Backblaze, 2026-02[^5] |
| Silent-corruption field study | 1.53M drives over 41 months | Vendor telemetry is how corruption gets measured | USENIX FAST '08[^6] |
| Portworx consideration | US$352.9M + US$32.2M retention | Everpure's largest software deal precedent | Pure Storage 10-K FY2021[^3] |
| 1touch price | US$125.0M cash | Control-plane-layer acquisition, 2026 | Everpure 10-Q Q1 FY27[^4] |
| Everpure non-GAAP gross margin, Q2 FY27 | Product 66.2%; subscription 74.9% | Benchmark for a target's margin structure | Investing.com, 2026-08[^13] |
| WEKA Series E | US$1.6B post-money, ≈ 16x 2024 ARR | Last priced round found | WEKA, 2024-05-15[^1][^25] |
| Blended margin example | 59% at 40% hardware mix | Mix can move margin without any change in pricing | Worked example |
| WEKA public-data score | 2.83 of 5; range 2.1–3.7 | 38% of weight rests on placeholders | Worked example (below) |

## Conversation playbook

**Questions for a PM**

1. *"If we sold this under Evergreen//One, which SLAs could we sign on day one?"* A strong answer names the metrics (performance per TB, durability, uptime), the telemetry needed to measure them, and the gap.
2. *"Which of the target's top customers are in our pipeline, and who resells it today?"* A strong answer identifies overlap and flags OEM partners that compete with Everpure.
3. *"What does the target ship that our roadmap won't have within 18 months?"* A strong answer names one dated capability and compares build time against deal time.

**Questions for an engineer**

1. *"Where does this architecture hit its first wall, and how close is the largest customer?"* A strong answer names the wall by architecture class and gives the largest deployment's metadata operation rate, not only its capacity.
2. *"Walk me through the worst data-integrity bug they shipped."* A strong answer covers how it was found, how many systems it affected, and whether a fleet-wide scan confirmed the fix.
3. *"What would it take to run their data path on DirectFlash and under Fusion?"* A strong answer separates API federation (months) from FTL assumptions (years) and names the modules to rewrite.

**Don't say this:**

- *"Their benchmark proves it scales."* One hero configuration proves only that configuration.
- *"Software-only means no hardware risk."* The risk moves into the qualification matrix, partner defection and support cost.
- *"Eleven nines is their field record."* Nines come from an MTTDL model; field data is incident logs.
- *"Open source means free."* GPL and AGPL obligations are diligence items, and licence disputes happen.
- *"We'll plug it into Fusion."* That covers the control plane only, the cheapest of the four seams.

## Going deeper (optional, L3 pointers)

- Bairavasundaram et al., FAST '08, the field study of checksum mismatches across a vendor fleet[^6].
- Backblaze Drive Stats datasets, a model for what field-failure data requests should look like[^5].
- [Chapter 56](../08-conversation-toolkit/56-talking-with-engineering-and-cto.md) covers architecture-review questions, and [Chapter 49](49-competitive-matrices.md) has cross-vendor matrices.
- SPDX-format software bills of materials (SBOMs), the standard output of software composition analysis.

## Key terms

- **Technical due diligence** — verifying a target's technology claims, risks and integration cost before a deal ([glossary](../glossary.md#t)).
- **Proof of concept (PoC)** — a hands-on test of the target's system on the buyer's workloads.
- **Clean team** — a ring-fenced group allowed to see competitively sensitive material such as source code.
- **Software composition analysis** — automated scanning of code for open-source components and their licences.
- **Copyleft** — licence terms (GPL, AGPL) requiring derived works to be shared under the same terms.
- **Data-loss incident log** — a vendor's record of every case of lost or corrupted customer data.
- **Key-person risk** — dependence on a few engineers whose departure would stall the product.
- **Integration seam** — one of the four places a target must join Everpure: control plane, data path, licensing, channel.
- **Placeholder score** — a neutral score assigned where public data is silent, flagged for diligence.

## Sources

[^1]: WEKA, "WEKA Nets $140M in Series E Funding at $1.6B Valuation," 2024-05-15. https://www.weka.io/news/weka-nets-140m-in-series-e-funding-at-1-6b-valuation (retrieved 2026-11-01).
[^2]: CNBC, "Nvidia backs AI company Vast Data at $30 billion valuation," 2026-04-22. https://www.cnbc.com/2026/04/22/nvidia-backs-ai-company-vast-data.html (retrieved 2026-11-01).
[^3]: SEC, "Pure Storage, Inc. Form 10-K for fiscal year 2021," 2021-03. https://www.sec.gov/Archives/edgar/data/1474432/000162828021005538/pstg-20210131.htm (retrieved 2026-11-01).
[^4]: SEC, "Everpure, Inc. Form 10-Q for the quarter ended May 3, 2026," 2026-06. https://www.sec.gov/Archives/edgar/data/0001474432/000147443226000061/pstg-20260503.htm (retrieved 2026-11-01).
[^5]: Backblaze, "Backblaze Drive Stats for 2025," 2026-02. https://www.backblaze.com/blog/backblaze-drive-stats-for-2025/ (retrieved 2026-11-01, via search summary); corroborated by StorageReview, "Backblaze 2025 year-end drive stats: annual AFR falls to 1.36% as high-capacity drives dominate fleet," 2026-02. https://www.storagereview.com/news/backblaze-2025-year-end-drive-stats-annual-afr-falls-to-1-36-as-high-capacity-drives-dominate-fleet (retrieved 2026-11-01).
[^6]: L. Bairavasundaram, G. Goodson, B. Schroeder, A. Arpaci-Dusseau, R. Arpaci-Dusseau, "An Analysis of Data Corruption in the Storage Stack," USENIX FAST '08, 2008-02. https://www.usenix.org/conference/fast-08/analysis-data-corruption-storage-stack (retrieved 2026-11-01).
[^7]: Launchpad, "Lustre" project page (licence: GNU GPL v2), n.d. https://launchpad.net/lustre (retrieved 2026-11-01); Wikipedia, "Lustre (file system)," n.d. https://en.wikipedia.org/wiki/Lustre_(file_system) (retrieved 2026-11-01).
[^8]: MinIO, "From Open Source to Free and Open Source, MinIO is now fully licensed under GNU AGPLv3," 2021-05. https://blog.min.io/from-open-source-to-free-and-open-source-minio-is-now-fully-licensed-under-gnu-agplv3 (retrieved 2026-11-01).
[^9]: Blocks & Files, "We object! MinIO says no more open license for you, Weka," 2023-03-26. https://blocksandfiles.com/2023/03/26/we-object-minio-says-no-more-open-license-for-you-weka/ (retrieved 2026-11-01, via search summary); WEKA, "WEKA Responds to Unfounded Allegations Made by MinIO Regarding Open Source Licensing," 2023-03. https://www.weka.io/article/weka-responds-to-unfounded-allegations-made-by-minio-regarding-open-source-licensing (retrieved 2026-11-01, via search summary).
[^10]: HPE, "HPE Completes Acquisition of Nimble Storage," 2017-04-17. https://www.hpe.com/us/en/newsroom/press-release/2017/04/hpe-completes-acquisition-of-nimble-storage.html (retrieved 2026-11-01).
[^11]: Pure Storage, "Pure Storage Delivers Industry-First Performance and Capacity Prediction Capabilities Powered by Machine Learning" (Pure1 META press release), 2017-06. https://www.everpuredata.com/company/news-and-events/press/ps_release_accelerate2017_meta.html (retrieved 2026-11-01).
[^12]: Alpha Spread, "P Q4-2026 Earnings Call," 2026-02-25. https://www.alphaspread.com/security/nyse/p/investor-relations/earnings-call/q4-2026 (retrieved 2026-11-01).
[^13]: Investing.com, "Everpure Q2 FY27 slides: 38% revenue growth, guidance raised sharply," 2026-08. https://www.investing.com/news/company-news/everpure-q2-fy27-slides-38-revenue-growth-guidance-raised-sharply-93CH-4878054 (retrieved 2026-11-01).
[^14]: Blocks & Files, "Pure debuts Enterprise Data Cloud with Fusion updates and new FlashArray systems," 2025-06-18. https://www.blocksandfiles.com/ai-ml/2025/06/18/pure-debuts-enterprise-data-cloud-with-fusion-updates-and-new-flasharray-systems/100996 (retrieved 2026-11-01).
[^15]: SEC, "Pure Storage, Inc. Form 10-K for fiscal year 2020," 2020-03. https://www.sec.gov/Archives/edgar/data/1474432/000162828020004133/pstg-20200202.htm (retrieved 2026-11-01).
[^16]: HPCwire, "Everpure Wants to Improve Data Management for the Coming AI Wave," 2026-06-20. https://www.hpcwire.com/aiwire/2026/06/20/everpure-wants-to-improve-data-management-for-the-coming-ai-wave/ (retrieved 2026-11-01).
[^17]: Fortune (Reuters), "Hewlett Packard Enterprise to buy Nimble Storage," 2017-03-07. https://fortune.com/2017/03/07/hewlett-packard-enterprise-nimble-storage (retrieved 2026-11-01).
[^18]: Globes, "EMC buys XtremIO for $430m," 2012-05. https://en.globes.co.il/en/article-1000747655 (retrieved 2026-11-01). EMC did not disclose terms; price as reported by press.
[^19]: eWeek, "EMC Acquires Scale-Out NAS Maker Isilon for $2.25 Billion," 2010-11-15. https://www.eweek.com/storage/emc-acquires-scale-out-nas-maker-isilon-for-2.25-billion/ (retrieved 2026-11-01).
[^20]: MLCommons via GlobeNewswire, "MLCommons Releases New MLPerf Storage v3.0 Benchmark Results," 2026-09-01. https://www.globenewswire.com/news-release/2026/09/01/3354412/0/en/mlcommons-releases-new-mlperf-storage-v3-0-benchmark-results.html (retrieved 2026-11-01).
[^21]: WEKA documentation, "Networking in WEKA" (v5.0), n.d. https://docs.weka.io/5.0/weka-system-overview/networking-in-wekaio (retrieved 2026-11-01).
[^22]: WEKA documentation, "Cluster capacity and redundancy management," n.d. https://docs.weka.io/weka-system-overview/cluster-capacity-and-redundancy-management (retrieved 2026-11-01); WEKA documentation, "Optimize redundancy in WEKA deployments" (v4.3), n.d. https://docs.weka.io/4.3/weka-system-overview/about/optimize-redundancy-in-weka-deployments (retrieved 2026-11-01).
[^23]: Blocks & Files, "WEKA tops SPECstorage Solution 2020 benchmark," 2025-02-11. https://www.blocksandfiles.com/ai-ml/2025/02/11/weka-tops-specstorage-solution-2020-benchmark/1595764 (retrieved 2026-11-01).
[^24]: WEKA, "WEKA Breaks The AI Memory Barrier With Augmented Memory Grid on NeuralMesh," 2025-11-18. https://www.weka.io/news/weka-breaks-the-ai-memory-barrier-with-augmented-memory-grid (retrieved 2026-11-01).
[^25]: WEKA, "A Strategic Step Forward for WEKA: An Open Letter From Our CEO," 2025-02. https://www.weka.io/article/a-strategic-step-forward-for-weka-an-open-letter-from-our-ceo (retrieved 2026-11-01).
[^26]: WEKA, "WEKA Architecture Key Concepts" (white paper), n.d. https://www.weka.io/wp-content/uploads/files/resources/WEKA-Architecture-Key-Concepts.pdf (retrieved 2026-11-01).
[^27]: HPCwire, "WEKA Launches NeuralMesh 6 and WEKApod as AI Inference Pushes Infrastructure Limits," 2026-07-22. https://www.hpcwire.com/2026/07/22/weka-launches-neuralmesh-6-and-wekapod-as-ai-inference-pushes-infrastructure-limits/ (retrieved 2026-11-01).
[^28]: AIwire/HPCwire, "WEKA Expands NVIDIA Integrations and Certifications, Unveils Augmented Memory Grid," 2025-03-19. https://www.hpcwire.com/aiwire/2025/03/19/weka-expands-nvidia-integrations-and-certifications-unveils-augmented-memory-grid/ (retrieved 2026-11-01).
[^29]: Blocks & Files, "WEKA replaces president, chief financial and revenue officers as it doubles down on late stage, pre-IPO growth," 2024-12-13. https://www.blocksandfiles.com/file/2024/12/13/weka-replaces-president-chief-financial-and-revenue-officers-as-it-doubles-down-on-late-stage-pre-ipo-growth/1596903 (retrieved 2026-11-01).
[^30]: Blocks & Files, "WEKA CFO exits four months into role," 2025-04-30. https://www.blocksandfiles.com/ai-ml/2025/04/30/weka-cfo-exits-four-months-into-role/1601839 (retrieved 2026-11-01).
[^31]: WEKA, "Hardware + System Partners," n.d. https://www.weka.io/partners/system-partners/ (retrieved 2026-11-01).
[^32]: Blocks & Files, "HPE stops selling Qumulo, Scality and WEKA software," 2025-11-07. https://www.blocksandfiles.com/file/2025/11/07/hpe-stops-selling-qumulo-scality-and-weka-software/1721655 (retrieved 2026-11-01).
[^33]: StorageReview, "WEKA's WEKApod 3 breaks the single-rack exabyte barrier as NeuralMesh 6 goes multi-tenant," 2026-07. https://www.storagereview.com/news/wekas-wekapod-3-breaks-the-single-rack-exabyte-barrier-as-neuralmesh-6-goes-multi-tenant (retrieved 2026-11-01).
[^34]: WEKA, "Our Customers," n.d. https://www.weka.io/customers/ (retrieved 2026-11-01); AAP (Cision release), "WEKA and Oracle Cloud Infrastructure Validate 10x Throughput Gains for Long-Context AI Inference," 2026-06-09. https://www.aap.com.au/aapreleases/cision20260609ae77787/ (retrieved 2026-11-01).
[^35]: SHI, "WEKA Extreme Performance and Scale (XPS) Edition" (reseller listing), n.d. https://www.shi.com/product/45872663 (retrieved 2026-11-01).
