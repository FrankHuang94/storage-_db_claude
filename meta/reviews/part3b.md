# Review: Part 3b (Chapters 19–24)

**Reviewer scope:** `docs/03-system-architecture/19-software-defined-and-hci.md` through `24-architecture-decision-matrix.md` and their staging files. Reviewed 2026-11-01.

## Summary

**What I checked.** I fact-checked the mechanisms the brief named:

- Ch 19: EBS chain replication, Physalia cells, SRD and the io2 Block Express figures.
- Ch 20: Raft, the quorum rules, CAP/PACELC and the MTTDL durability model.
- Ch 21: the metadata scaling claims.
- Ch 22: the names of the fleet tools.
- Ch 23: revenue recognition and the Evergreen program terms.

I also checked the business numbers: Nutanix FY26, Everpure FY26 and Q2 FY27, Broadcom/VCF, and Backblaze.

**Worked examples.** I recomputed every one:

- Ch 19: stranded cores and rebuild hours.
- Ch 20: RAID 6, 8+2, 3-way and 16+4 nines; AFR-to-FIT; the correlated-failure penalty.
- Ch 21: small-file throughput, the crossover size and the ls/stat timings.
- Ch 23: the cash-flow NPVs and year-one revenue.

All of them are arithmetically correct. The Ch 20 chart script implements the formula the prose states.

**Network limits.** WebFetch failed for usenix.org and docs.aws.amazon.com because both hosts are outside the session's allowed network domains. Every check in this review therefore used WebSearch summaries, and new footnotes are marked "seen via search summary" where that applies.

**Known issue fixed first (Ch 24).** Ch 24 repeated the old "Everpure calls FlashBlade//S shared-everything" error in its strategy paragraph and in Table 24.5. I rewrote both to match the corrected Ch 15: a partitioned scale-out with per-blade authorities and pooled media management, which Pure's engineers call "partitioned-writer". The Emerson blog is cited.

I also made Ch 24 consistent with how Ch 16 and Ch 17 classify EXA (a pNFS metadata/data split in the parallel-file-system row, not DASE):

- Heatmap row labels now read "Scale-out shared-nothing (incl. partitioned)" and "Parallel file system (incl. pNFS split)".
- A new "Where Everpure's products sit" paragraph places each FlashBlade product in its row and states the caveats, including EXA's undocumented data-node protection.
- The quadrant gains a "pNFS split" point. Its caption no longer implies that pNFS designs are plotted when they were not.
- The DASE cell of Table 24.5 now says EXA splits metadata from data instead.
- A "Don't say this" bullet was added.

**Heatmap vs Ch 14–19 pros/cons.** Most cells match. I found three mismatches and resolved them:

1. Shared-nothing scores ◐ for OLTP, but Ch 15 lists latency-critical block as a worst fit. I kept ◐ and extended the DASE justification bullet to cover shared-nothing (PowerFlex-style block SDS runs production databases).
2. Object scores ◐ for training and checkpointing, but Ch 18 lists both among its best fits. I kept ◐ and the bullet now explains why: synchronous checkpoint writes and small-file random access.
3. The SDS/HCI row scores HPC and AI ○, while Ch 19 lists "large object and file, AI data lakes" as SDS best fits. I added a note to the legend: SDS sold as software for commodity servers (WEKA, Ceph, VAST) is rated in the row of its architecture, and this row covers HCI and container-native SDS only.

**Verdicts:**

| Ch | Verdict | Main reasons |
|---|---|---|
| 19 | Minor fixes | Wrong "first external storage" claim for Nutanix; three VERIFYs resolved |
| 20 | Minor fixes | S3 consistency understated; declustered-durability caveat added; NetApp VERIFY resolved |
| 21 | Minor fixes | EXA "20×" claim mischaracterised |
| 22 | Minor fixes | Stale roadmap item; Dell renaming; naming anachronism |
| 23 | Minor fixes | Evergreen//One revenue-recognition wording |
| 24 | Material fixes | FlashBlade classification and consistency with Ch 15–17 |

**QA after edits:** Ch 19–24 all pass `qa_report.py`, `lint_mermaid.sh` and `check_links.py --allow-planned`. Word counts went up slightly. I updated reading times for Ch 20, 23 and 24, and renumbered the footnotes of Ch 19, 20, 22, 23 and 24 so they run in order of first use.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 24 | "a blade scale-out it calls shared-everything (FlashBlade//S and //E)" | No Everpure source says this. Pure calls Purity//FB "partitioned-writer", and one data sheet says "shared-nothing" | Rewritten as a partitioned blade scale-out, with the Emerson blog cited and links to Ch 15, 16 and 17. Also says why there is no DASE (EXA has no compute tier that reaches all media) | fixed |
| 24 | Table 24.5: "FlashBlade//S (…Everpure calls it shared-everything)" | Same error | Row renamed "Scale-out shared-nothing or partitioned". FlashBlade//S and //E described as per-blade authorities with pooled media. DASE cell says "EXA splits metadata from data instead". PFS cell says "pNFS metadata/data split". Caption now credits Portworx (SDS) separately from the HCI partnership | fixed |
| 24 | Heatmap rows | Readers could not tell where FlashBlade//S and EXA sit | Row labels now include "partitioned" and "pNFS split". New paragraph places each product and gives its caveats; for EXA, data-node protection is undocumented and the metadata-core claims are company-stated | fixed |
| 24 | Quadrant caption: "DASE and pNFS-style designs" sit top-right | pNFS was not plotted. Parallel FS was plotted bottom-right | Added a "pNFS split" point at (0.86, 0.52) with a sentence of rationale (stock client, but customers still run an RDMA fabric and the data nodes); caption reworded | fixed |
| 24 | Shared-nothing OLTP ◐ vs Ch 15 worst fit; object training/checkpoint ◐ vs Ch 18 best fit; SDS row vs Ch 19 SDS best fit | Inconsistent with the earlier chapters' fit sections | Justification bullets extended; legend clarifies what the SDS/HCI row covers | fixed |
| 24 | "PureKVA shipped on FlashBlade in October 2026" | Sources show a September 2026 announcement for October availability. No GA confirmation found | Reworded to "announced… for October availability" | fixed |
| 24 | "HPE markets the X10000 as unifying all three" | The X10000 is object plus NFS. Block is the B10000 | Reworded to the Alletra Storage MP family; staging VERIFY removed | fixed |
| 24 | "one OS family (Purity)… across its rows" | Overclaim: EXA data nodes run Linux, and Portworx is not Purity | Narrowed to FlashArray and FlashBlade, including EXA's metadata core | fixed |
| 24 | NetApp AFX "up to 128 controllers" | This is the design maximum (see Ch 16 / part3a) | Context column now says so | fixed |
| 24 | Gartner Enterprise Storage Platforms MQ merged categories; S3 Vectors 2B per index (Dec 2025); Lustre >60% of Top500; MLPerf v3.0 877.5 GiB/s | Checked | None needed | verified |
| 19 | "Nutanix's FlashArray integration, its first major certified external storage" | Wrong. Dell PowerFlex was the first external storage on NCP (GA May 2025), and PowerStore followed (NCI 7.6, 2026) | Corrected, with a citation | fixed |
| 19 | VCF 1 TiB vSAN per core [VERIFY] | Confirmed by Broadcom KB 313548 | Citation added; VERIFY removed | fixed |
| 19 | Broadcom 87% VCF adoption [VERIFY] | Confirmed: Q2 FY25 call, per The Register 2025-06-06. The ~US$27B FY25 infrastructure software figure is still unconfirmed | 87% cited; VERIFY narrowed to the US$27B | fixed / flagged |
| 19 | EBS >140 trillion ops/day [VERIFY] | Several summaries of the Olson post agree | VERIFY removed; footnote notes it was seen via summary | fixed |
| 19 | Everpure product/subscription GM 66.2% / 74.9% | Found only in earnings summaries (Quartr). Total 69.9% is the non-GAAP figure, so these are likely non-GAAP | Labelled "non-GAAP per earnings summaries" | fixed |
| 19 | "Everpure raised prices on 2026-02-09" | Primary sources say "early February", with a second rise later | Reworded; Blocks & Files 2026-04-23 added | fixed |
| 19 | "VCF 9 deprecated vVols" | Incomplete: removal is planned for 9.1 (Dell KB, Jan 2026) | Added, with a citation | fixed |
| 19 | Physalia seven-node cell per volume; client→primary→replica chain; io2 256K IOPS, 4,000 MB/s, <500 µs at 16 KiB, 99.999%; Nutanix ARR US$2.55B, FY26 non-GAAP GM 88.0% | Checked. The Nutanix 88.0% is the full-year figure (Q4 alone was 87.7%) | None needed | verified |
| 20 | Table 20.1: S3 is "read-after-write: a writer sees its own write; others once committed" | Understates S3. Since Dec 2020 every reader sees an acknowledged write (strong read-after-write per object), which matches Ch 9 | Row renamed and redefined | fixed |
| 20 | "Same code rebuilt declustered in 4 hours reaches 7.8 [nines]" | The model treats each k+m group as independent, which flatters declustered layouts: there, almost any m+1 failed drives share a stripe (about −3 nines for 8+2 and −5 for 16+4 in this example). Priority rebuild of critical stripes recovers much of it | Caveat sentence added. Chart left as is; its docstring already notes the independence assumption | fixed |
| 20 | NetApp Cloud Mediator from ONTAP 9.17.1 [VERIFY] | Confirmed in the ONTAP 9.17.1 release notes | Cited; VERIFY removed; steelman sentence updated | fixed |
| 20 | Raft sequence, 2f+1, W+R>N, PACELC, Azure 11/12/16 nines, Backblaze 1.36% (1.55% in 2024), copysets 99.99%→0.15%, FIT maths, all MTTDL numbers | Recomputed and checked | None needed | verified |
| 21 | EXA "up to 20× metadata vs scale-out" [VERIFY] | Mischaracterised. Pure's claim is ">20× more files per namespace" than "the leading parallel file system", which is about namespace size, not metadata ops/s | Rewritten and cited to iTWire and the Pure AI page; VERIFY removed | fixed |
| 21 | VAST V-tree 7 levels, 512× fan-out [VERIFY] | Repeated consistently by Blocks & Files (2019, 2022) as company-stated | VERIFY removed; labelled company-stated | fixed |
| 21 | MLPerf config "30 EXA blades with 120 DFMs for metadata, 30 data nodes"; ImageNet maths; HDFS 150 B/object; GPFS 10B files in 43 min; DNE releases; metadata strategy table | Checked | None needed | verified |
| 22 | "MCP integration slated Q4 FY26" | Stale roadmap wording. MCP support was announced in 2025, and a Pure1 Manage MCP server is described in a 2026 Everpure blog | Updated | fixed |
| 22 | Dell "APEX AIOps Infrastructure Observability" | Dell support now calls it "Dell AIOps (formerly CloudIQ)" | Renamed, with the history kept | fixed |
| 22 | "In September 2025 Everpure announced…" | Anachronism: the company was Pure Storage until February 2026 | "Pure Storage (now Everpure)" | fixed |
| 22 | Terraform provider for Fusion | The latest release found (v1.0.16) is from 2023 and targets Fusion v1, so "storage as code" for Fusion v2 may be thinner than implied | Caveat added inline | fixed |
| 22 | NetApp DII/Console renames, HPE InfoSight 86%, Nimble ~US$1B, GreenLake Intelligence MCP | Checked | None needed | verified |
| 23 | STaaS revenue "Over time, on consumption above a minimum commitment" | Misleading. The 10-K says revenue is recognized over the term on a consumption basis, and contracts carry a minimum commitment plus fees for excess usage | Reworded | fixed |
| 23 | Evergreen//Flex revenue recognition not described | The 10-K says Flex product revenue is recognized at the start of the subscription and subscription fees ratably | One clause added | fixed |
| 23 | FY26 STaaS TCV US$520M (+32%) [VERIFY] | Confirmed by a Quartr Q4 FY26 summary (Q4 alone: US$179M, +28%) | VERIFY removed; Q4 figure added | fixed |
| 23 | Q2 FY27 TCV US$277M (+121%), ">well above 40%" adjusted growth, 3–4 year contracts, 10,000+ NDUs to >3,000 customers (2022), Evergreen//Forever 3-year (6-year for //E) Ever Modern | Checked | Nasdaq corroboration added | verified |
| 23 | Evergreen//One "Overdrive" (2026) [VERIFY] | No source found | Left as VERIFY | flagged |

## Unresolved / disagreements

- **FlashBlade//EXA data-node protection scheme** (Ch 24 engineer question, Ch 16/17). Still undocumented in public sources. Ch 24 now says so explicitly.
- **Everpure Q2 FY27 product/subscription gross margins (66.2% / 74.9%)**. These come only from Quartr and investing.com summaries; I couldn't fetch the 8-K exhibit from sec.gov. They are probably non-GAAP and are now labelled that way. Confirm against the 8-K gross-margin table.
- **Broadcom FY2025 infrastructure software revenue (~US$27B)**. Plausible, but not confirmed; check the 10-K.
- **Evergreen//One Overdrive** (Ch 23). No source found for its terms or GA.
- **Meta Tectonic flattened into one ZippyDB schema** (Ch 21, Blocks & Files 2026-07-27). The search returned nothing, so the VERIFY stays.
- **Pure1 Manage MCP server GA** (Ch 22). It is described only in an Everpure blog, seen via search summary.
- **Ch 24 heatmap remains atlas judgment.** I would still have Everpure field engineers sanity-check the contentious cells, especially the new pNFS-split quadrant position. The staging ASK/VERIFY is kept.
- **Ch 27 (outside scope).** I grepped for "calls it shared-everything" and similar FlashBlade wording, and found no remaining instances outside Ch 15/16 (where it now appears only in corrective context).
- **Network.** usenix.org and docs.aws.amazon.com don't resolve in this session, and blog.everpuredata.com and sec.gov were not fetched. All checks against those sources rely on search summaries.
