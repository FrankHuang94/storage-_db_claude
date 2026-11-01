# Review: Part 2 (Chapters 7–12, Protocols and Networking)

**Reviewer scope:** `docs/02-protocols-and-networking/07-block-protocols.md` through `12-interfaces-and-emerging-tech.md` and their staging files. Reviewed 2026-11-01.

## Summary

**What I checked:**
- Every sequence diagram, arrow by arrow: SCSI/iSCSI/FCP, NVMe/PCIe doorbells, NVMe-oF read and write over RDMA and TCP (including in-capsule data, R2T and C2HData), the NFSv3 path, pNFS OPEN/LAYOUTGET/GETDEVICEINFO, the S3 PUT/GET with SigV4, multipart upload, ECN/DCQCN/PFC, and the traditional versus GDS GPU paths.
- Standards dates and RFC numbers: NVMe 1.0, NVMe-oF 1.0, TP 8000, FC-NVMe, RFC 1813/3530/5661/8881/7862/8435/8166/8267, PCIe 3.0–8.0, CXL 1.0–4.0, 802.3bs/ck/df/dj, UEC 1.0, ZNS and FDP, and the Optane milestones.
- NVIDIA naming: GDS/cuFile, Magnum IO, NIXL, Dynamo/KVBM, cuObject, Spectrum-X, BlueField-3/4, STX/CMX. These are consistent with Ch 34.
- Everpure and competitor protocol claims.
- All the arithmetic, recomputed: the Little's-law IOPS figures, the S3 small-object tax and LIST times, multipart sizing, the 1,024-GPU fabric example, DRAM traffic per 400G port, PFC headroom, the GPU-idle cost CSV (all 12 rows), tokens/s, KV-cache size, bounce-buffer DRAM load, and PCIe x4/x16 bandwidths.

**Arithmetic:** correct, with one rounding fix (0.97 → 0.96 M tokens/s) and one TL;DR price-range inconsistency. The Ch 11 chart CSV reproduces exactly: stall fraction × 1,024 × 8,760 h × price.

**Sequence diagrams:** no wrong-direction arrow. Reads over RDMA are target RDMA WRITEs into the host buffer, and writes are target RDMA READs. I added precision engineers would expect:
- iSCSI immediate/unsolicited data and FC first burst can skip the R2T.
- The NVMe/TCP success flag on the last C2HData PDU lets the target skip the response capsule.
- The in-capsule data limit is advertised by the target.
- FC-NVMe queues map to connections within an association, not to exchanges.
- Fig 7.5 now says "mirrored or shared NVRAM", consistent with Part 3a's FlashArray fix.

**Network limits:** WebFetch was refused for docs.portworx.com, ithome.com.tw and nvidianews.nvidia.com (and per D13, sec.gov and vendor sites). Facts from those hosts are cited from search results, and the footnotes say so.

**Verdicts:**
- Ch 7: minor fixes (competitor table VERIFYs resolved, caption contradiction).
- Ch 8: minor fixes (FlashBlade//S RDMA/GDS status, VAST pNFS).
- Ch 9: minor fixes (VERIFYs resolved).
- Ch 10: minor fixes (incast wording, history VERIFYs).
- Ch 11: minor fixes (Everpure GDS status sourced, dates resolved).
- Ch 12: material fixes (CXL 4.0 bandwidth error, "only vendor owning its flash module" overclaim, E1.S power).

**QA after edits:** all six chapters PASS `qa_report.py`. `lint_mermaid.sh` is OK (23 blocks). `check_links.py --allow-planned` reports 0 broken links. Word counts are 116–119% of budget. Footnotes in all six chapters are renumbered in order of first use. Before this review several chapters were out of order; definitions and text are unchanged apart from the numbers.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 7 | TL;DR "two layers"; Core says three | Internal inconsistency | TL;DR now says "command set riding a transport (plus fabric services)" | fixed |
| 7 | "RoCE (NVMe over RDMA on Ethernet)" | RoCE is the RDMA transport, not NVMe-over-RDMA | "NVMe over RoCE (RDMA on Ethernet)" | fixed |
| 7 | "many HBAs still serialize" | Outdated: scsi-mq and multi-queue FC/SAS HBAs exist | Reworded to per-LUN queue depth and command-path limits | fixed |
| 7 | Fig 7.1 caption: a write always costs an extra round trip | iSCSI ImmediateData/InitialR2T=No and FCP first burst skip the R2T | Caveat added | fixed |
| 7 | Queue pair maps to an "FC exchange context" | FC-NVMe maps each queue to a connection within an association; an exchange is per I/O | Corrected | fixed |
| 7 | NVMe/TCP read path | Omitted the C2HData SUCCESS flag; "large writes" should be "writes above the in-capsule limit" | Added | fixed |
| 7 | Fig 7.5 "persist mirrored copy" | Contradicted Ch 14's shared chassis NVRAM for FlashArray | "persist to mirrored or shared NVRAM"; caption adds the in-capsule size limit and FC first burst | fixed |
| 7 | NetApp ONTAP NVMe/RoCE [VERIFY] | NetApp KB: ONTAP supports NVMe/FC and NVMe/TCP only | Replaced, with E-Series/EF caveat; NVMe/FC from ONTAP 9.4 cited to NetApp docs | fixed |
| 7 | Dell PowerStore RoCE / NVMe/FC [VERIFY] | No RoCE found (Dell chose NVMe/TCP); NVMe/FC in PowerStoreOS 2.0, April/May 2021 | Replaced and cited | fixed |
| 7 | Purity//FA 6.4.2 NVMe/TCP [VERIFY: GA date] | Sources conflict (one summary says 2022-02-07, probably a typo) | Now "2022" with a narrowed VERIFY | flagged |
| 7 | Fig 7.7 caption "protocol coverage is at parity" | The table shows only Everpure offering RoCE | Caption corrected | fixed |
| 7 | NVMe queues, NVMe 1.0/oF 1.0/TP 8000/vSphere 7U3/RFC 3720/FC-PH/SCSI-1 dates; Little's-law maths | Checked | None | verified |
| 8 | FlashBlade//S "NFS-over-RDMA status [VERIFY]" | iThome reports GDS over NFS/RDMA on FlashBlade//S from Purity//FB 4.3.4 (Oct 2023); //E not supported | Table updated, tagged search-summary only | fixed / flagged |
| 8 | VAST pNFS [VERIFY] | VAST NFS client docs v4.5 (Apr 2026) list NFSv3/v4.1 multipath, not pNFS | VERIFY replaced with a doc citation, still hedged as "no public support found" | fixed |
| 8 | Linux client "whose upstream maintainer is Hammerspace's CTO" | Overstated: Myklebust co-maintains the client | "one of whose upstream maintainers" | fixed |
| 8 | Option "whether EXA's data leg delivers GDS" | Portworx docs (search summary) describe GDS on EXA over RDMA NFS | Rephrased: the open questions are NVIDIA certification and measured numbers | fixed |
| 8 | "NetApp agreed to buy PEAK:AIO" | It is an announced intent to acquire, not closed | Reworded | fixed |
| 8 | NFS RFC numbers and dates, nconnect 16 / Linux 5.3, the 44-connection worked example, pNFS diagram | Checked | None | verified |
| 9 | TL;DR lists MinIO as a cuObject adopter | MinIO shipped its own S3-over-RDMA implementation (Nov 2024) | Separated cuObject adopters from MinIO | fixed |
| 9 | MinIO consistency [VERIFY] | MinIO blog states strict read-after-write and list-after-write | Cited and labelled company-stated | fixed |
| 9 | NVIDIA RDMA for S3 date [VERIFY] | Blog c. 2025-11-13 (coverage dated 2025-11-14); GA promised via CUDA in January 2026 | Resolved in text and footnote | fixed |
| 9 | FlashBlade S3 over RDMA [VERIFY: GA] | Pure said "later this year" (2025), ~250 GB/s on five chassis preliminary; no GA notice found | Table sharpened, VERIFY kept | flagged |
| 9 | Prices, LIST and PUT tax, 1 PB chart, 58 months, multipart 650 MB / 8.5 min, strong consistency 2020-12-01, Express One Zone cuts, S3 Vectors scale | Recomputed or checked | None | verified |
| 9 | Pi Day 2024 "350 T objects, 100 M req/s" | Still search-summary only; secondary sources cite about 500 T objects and 200 M req/s in 2025 | Left as dated 2024 figure | flagged |
| 10 | "many-to-few on writes and few-to-many on reads. That shape, called incast" | Read incast is many storage nodes to one client port, not "few-to-many" | Rewritten; "handful of ports" quantified as 2–3 | fixed |
| 10 | PFC headroom "round-trip plus reaction ≈ 1 µs" | The 100 m RTT alone is 1 µs | Reworded as a floor; the arithmetic stands | fixed |
| 10 | "Quantum-X800 was the first switch on 200G SerDes" | Unsupported superlative | "among the first switches of that generation" | fixed |
| 10 | Mellanox deal [VERIFY]; UEC founding [VERIFY] | 2019-03-11, US$6.9B, closed April 2020; UEC 2023-07-19, LF/JDF project with nine founders | Resolved and cited | fixed |
| 10 | Dell'Oro ">2/3 in 2025, ~20% two years earlier" | The 4Q25 release says this for the quarter and the full year (search summary) | Footnote annotated; staging sharpened | verified (search-summary) |
| 10 | Table 10.3 "fully aligned with NVIDIA" | Cheerleading-adjacent wording | "closely aligned" | fixed |
| 10 | 802.3dj "still in ballot Oct 2026" | Confirmed: SA recirculation closed June 2026; approval expected about Dec 2026 | None | verified |
| 10 | DRAM traffic and 819/102 Tb/s fabric arithmetic; 802.3bs/ck/df dates; BlueField-3/4 specs; UEC 1.0 date | Checked | None | verified |
| 11 | TL;DR "US$2–6 per H100-hour → US$0.57–1.75/s" | $1.75 corresponds to $6.16 | "US$2.00–6.16" | fixed |
| 11 | 0.97 M tokens/s | 1,024 × 989e12 × 0.4 ÷ 4.2e11 = 0.964 M | 0.96 M | fixed |
| 11 | Lambda US$3.99 [VERIFY] | Trackers agree on 3.99; Lambda's own page has shown 2.99 | VERIFY sharpened | flagged |
| 11 | FlashBlade//S "GDS claimed" | Now sourced (iThome, Purity//FB 4.3.4, Oct 2023), but absent from NVIDIA release-note tables | Table updated | fixed / flagged |
| 11 | EXA GDS certification [VERIFY] | Portworx documents GDS on EXA; Ch 34 says NVIDIA validation was in progress in March 2026 | Table cross-links Ch 34 | fixed |
| 11 | GPUDirect RDMA year [VERIFY]; Dynamo date [VERIFY] | Kepler/CUDA 5.0, 2012 (NVIDIA doc); Dynamo 2025-03-18 (NVIDIA IR) | Resolved; Pure GDS history now notes Oct 2023 delivery | fixed |
| 11 | "idle time comes mostly from interruptions" | Overclaim | "a large share" | fixed |
| 11 | GPU-idle CSV (12 rows), checkpoint 1.12 TB / 56 s / 3.1%, US$0.89 M saving, KV 320 KiB / 10.7 GB, bounce-buffer 400 vs 614 GB/s | Recomputed | None | verified |
| 12 | "CXL 4.0 ... up to 768 GB/s per direction on x16" | **Wrong.** x16 at 128 GT/s is 256 GB/s per direction; 768 GB/s comes from bundled ports | Text and Numbers table corrected | fixed |
| 12 | E1.S "up to 25 W (15 mm)" | 25 W is the 25 mm heat-sink variant; 5.9 mm is about 12 W, and 15 mm is cited as 20–25 W | "~12 W (5.9 mm) to ~25 W (25 mm)" | fixed |
| 12 | Table 12.3 "Everpure is the only major vendor that owns the flash module" | **Overclaim.** IBM designs FlashCore Modules (with an in-module controller) | Reworded: the only vendor whose module has no drive-level FTL; IBM FCM also noted under computational storage | fixed |
| 12 | ZNS [VERIFY]; CXL 1.0–3.1 [VERIFY]; Pure DirectMemory/Optane [VERIFY]; Micron exit / Lehi sale | TP4053 June 2020; CXL 1.0 Mar 2019, 2.0 Nov 2020, 3.0 Aug 2022; DirectMemory Cache used Optane SSDs (2019); Micron exit Mar 2021 and Lehi sale to TI US$900M Jun 2021 | Resolved and cited; only the CXL 3.1 day and 2015–2019 Optane dates remain VERIFY | fixed |
| 12 | PCIe bandwidth table and chart (3.9/7.9/15.8/29.5/59/118 GB/s x4; 128/256/512 GB/s x16), flit 236/256, 708 GB/s vs 100 GB/s, WAF 4, PCIe release dates | Recomputed or checked | None | verified |

## Unresolved / disagreements

- **Ch 7:** Exact GA month of Purity//FA 6.4.2 (NVMe/TCP). Sources conflict between 2022 and 2023.
- **Ch 7:** Crehan Research FC +6% (2025) remains search-summary only.
- **Ch 8 / Ch 11:** FlashBlade//S GDS/NFS-over-RDMA support (Purity//FB 4.3.4, Oct 2023) rests on an iThome search summary. It does not appear in NVIDIA GDS release-note partner tables. Someone with Everpure release-note access should confirm. This also bears on Ch 34's "FlashBlade//S holds the full set."
- **Ch 8 / Ch 11:** FlashBlade//EXA GDS rests on a Portworx doc search summary. NVIDIA certification for EXA is not public. A SPECstorage AI_IMAGE disclosure (Jan 2026, Purity//FB 4.6.4) describes RDMA-enabled pNFS to data nodes. It could be cited in Ch 16/27 if useful.
- **Ch 9:** FlashBlade S3-over-RDMA GA status. Pure promised it "later this year" in 2025; no GA notice found by 2026-11-01. If it is still not GA, Ch 11's "Everpure has announced it" is accurate but should not be upgraded to "ships".
- **Ch 10:** Everpure's Spectrum-X +25% read / +23% write figures were not found in any search. Keep the VERIFY or drop the figures. MetaRoCE (Aug 2026) is still unverified.
- **Ch 11:** The Lambda list price (US$3.99 vs US$2.99) is unresolved. It does not change the conclusions, since the mid-tier is illustrative.
- **Ch 12:** Largest shipping E1.S/E3.S capacities, U.2 power class, the CXL 3.1 release day, and the 2015–2019 Optane dates are still VERIFY. E1.S dimensions (33.75 × 118.75 mm) look like the enclosure dimensions; the PCB is 31.5 × 111.49 mm. I left this unchanged.
