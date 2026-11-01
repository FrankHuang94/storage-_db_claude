# Review: Part 3a (Chapters 13–18)

**Reviewer scope:** `docs/03-system-architecture/13-storage-stack.md` through `18-object-storage-architecture.md`, their staging files. Reviewed 2026-11-01.

## Summary

I checked every architecture mechanism the brief named against primary or vendor sources where I could reach them: write-acknowledgement paths, controller roles and failover, placement, metadata location, federation limits, VAST hardware specifics, and the EXA and AFX scale claims. I also re-did every worked example (latency sums, rebuild hours, erasure-coding overheads, tail-latency maths, the LIST rate, geo-EC rebuild days). All of them are arithmetically correct.

WebFetch failed for blog.everpuredata.com and arxiv.org because those hosts are blocked in this session. Anything from those hosts is cited from search-result summaries, and the footnotes say so.

On the five questions the brief asked me to rule on:

1. **Ch 14, FlashArray as a "single-controller envelope": upheld.** Current Everpure material ("Why FlashArray Only Needs Two Storage Controllers") says FlashArray is active/active for connectivity. Only the primary controller processes I/O. The secondary relays I/O from its ports and keeps a DRAM mirror of transactions. Justin Emerson's "Storage Architecture Spectrum" post calls Purity//FA a "single-writer" design. Purity Turbo (XL190 only, January 2026) lets the secondary serve reads, and Everpure's own launch blog confirms this. I removed the VERIFY and replaced the 2014 third-party citation with these Everpure sources.
2. **Ch 16 and Ch 17, FlashBlade//EXA as a metadata/data split with a direct pNFS path, not DASE: upheld.** The tech brief, Blocks & Files and the solution brief all say the same thing: pNFS metadata over NFSv4.1/TCP, data over RDMA direct to data nodes, and commodity data nodes running Purity//DN tooling. Ch 13, 15, 16 and 17 are consistent on this.
3. **Ch 15, FlashBlade//S: material error, fixed.** The chapter said "Pure Storage calls it shared-everything", cited to StorageNewsletter. I found no Pure source that says this. Pure's own blog calls Purity//FB "partitioned-writer" and rejects the binary label. A Pure data sheet calls FlashBlade "shared-nothing". Search summaries of the cited StorageNewsletter piece also describe it as shared-nothing globally. I rewrote the section as "partitioned scale-out (authorities per blade) with pooled, global media management". **Ch 24 has the same error in two places and is outside my scope (see Unresolved).**
4. **Ch 16, VAST specifics: one factual fix.** The chapter said "each DBox has two [DNodes]". The 1U Ceres DBox has four BlueField DPUs, each fronting about a quarter of the SSDs, according to Blocks & Files 2022 (the chapter's own source) and VAST's NCP reference architecture. The original x86 DBox had two. The DF-3060V2 figures (12 TB SCM against 1,352 TB QLC, about 0.9%) are confirmed by the VAST KB. Ch 16 quotes no VAST throughput numbers.
5. **Consistency across chapters:** after the fixes, Ch 13–18 agree on FlashArray, FlashBlade//S and EXA. Ch 13 now uses "mirrored or shared NVRAM" so it no longer contradicts Ch 14's chassis-NVRAM description of FlashArray.

**Verdicts:** Ch 13, minor fixes. Ch 14, minor fixes (one outdated competitor fact). Ch 15, material fix (the FlashBlade//S classification). Ch 16, minor fixes; I kept the exemplar style and changed facts only. Ch 17, minor fixes. Ch 18, solid, with one passage sharpened.

**QA after edits:** all six chapters pass `qa_report.py`, `lint_mermaid.sh` and `check_links.py --allow-planned`. Word counts went up slightly. I renumbered the footnotes of Ch 14–18 so they run in order of first use.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 13 | Fig 13.2 and its text: write ACKed once "mirrored in NVRAM on both controllers", quoting the FlashArray//XL170 latency | Wrong for FlashArray. Its NVRAM sits in chassis modules (on //XL, DFMDs) that both controllers reach. Ch 14 says this correctly, so Ch 13 contradicted it | Reworded to "persist to mirrored or shared NVRAM" in the figure, text and Table 13.1, with a link to Ch 14 | fixed |
| 13 | Gross margins: NVIDIA 71.1% (FY26), Everpure 70.4% (FY26) | Checked against the NVIDIA 10-K/8-K and the Everpure Q4 FY26 8-K | None needed | verified |
| 14 | Table 14.1 and text: FlashArray "single-envelope"; VERIFY on whether Purity//FA still relays secondary-port I/O | Sources were from 2014–2016 and third-party | Added the Everpure "Why FlashArray only needs two controllers" blog and the Emerson "single-writer" blog; added the secondary's DRAM transaction mirror; VERIFY removed | fixed |
| 14 | "Partner CPU that mostly waits on writes" | Undersells the secondary: Everpure says it relays front-end I/O and mirrors transactions | Reworded | fixed |
| 14 | "IBM four I/O groups" (with VERIFY); Table 14.4 "Up to 4 I/O groups" | Outdated. From Storage Virtualize 8.7.1, IBM no longer scales a system by adding control enclosures and points to FlashSystem grid (federation; up to 32 systems for the FS7600, per a reseller datasheet) | Text and table rewritten; IBM support page cited; VERIFY removed | fixed |
| 14 | NetApp AFF symmetric active/active "from 9.19.1" | 9.19.1 exists (about Oct 2026), but I could not confirm the SAN feature on official release notes. The chapter cites a NetApp Community post | Left as is | flagged |
| 15 | "Pure Storage calls [FlashBlade//S] shared-everything" (text and Table 15.3) | Unsupported. Pure says "partitioned-writer"; a Pure data sheet says "shared-nothing" | Rewritten with the Emerson blog, the Metadata Advantage white paper and the M&E data sheet; added a "Don't say this" bullet | fixed |
| 15 | Facebook "median ~180 TB/day" EC recovery traffic (VERIFY) | The reachable primary abstract says "more than a hundred terabytes per day". I could not confirm 180 TB (arXiv blocked) | Changed to ">100 TB/day" in text and Numbers table; VERIFY removed | fixed |
| 16 | "Each DBox has two [DNodes] ... in Ceres they are BlueField DPUs" | Ceres has four BlueField DPUs, each fronting about a quarter of the SSDs | Corrected; failure-table row made generic ("another DNode"). The SVG still shows two DNodes per DBox, which is fine as a conceptual minimum | fixed |
| 16 | EXA "60 data nodes >5 TB/s, ≥83 GB/s per node" | Confirmed by the tech brief, which cites "upwards of 85 GB/s" per node. The ">10 TB/s" launch claim is a separate preliminary-test claim | Added the per-node wording and a note on the 10 TB/s claim with a StorageReview citation | fixed |
| 16 | EXA data nodes "(Purity//DN)" | Purity//DN is data-node management tooling (playbooks, upgrades) running on commodity Linux/NVMe servers, not a Purity data path | Reworded | fixed |
| 16 | NetApp AFX "up to 128 controllers, 52 enclosures" | That is the datasheet design maximum. WWT reports 32 controllers supported in ONTAP 9.19.1. ">1 EB effective" needs roughly 13:1 reduction on 52 × 24 × 60 TB | Added the supported-limit caveat in the table and the Numbers table | fixed |
| 16 | HPE X10000 'Yes ("SEDA")' | Acronym not confirmed. HPE says "disaggregated, shared-everything" | Replaced with HPE's wording | fixed |
| 16 | VAST DF-3060V2 12 TB SCM / 1,352 TB QLC; DASE mechanics; stripe maths | Confirmed (VAST KB) | None | verified |
| 16 | VAST ~US$30B valuation "reported by press" | It is also the company-stated Series F (closed 2026-04-22, per CNBC in the research notes). Labelling is acceptable | None | verified |
| 17 | MLPerf v3.0 EXA 877.5 vs Azure Managed Lustre 642.2 GiB/s (VERIFY "from chart captions") | Stated in StorageReview text and in Azure's own results page (128 clients) | Added the Azure doc citation and the 10-node scaling point; VERIFY removed | fixed |
| 17 | WEKA client "User-space client, DPDK kernel bypass" | Incomplete. WEKA also installs a kernel driver for the POSIX mount, which weakens the chapter's "kernel module" contrast if left out | Corrected | fixed |
| 17 | Timeline "2022: Spectrum Scale renamed IBM Storage Scale" | The rename was in 2023 (Blocks & Files 2023-02-24; IBM docs say from 5.1.8) | Year corrected; footnote added | fixed |
| 18 | FlashBlade write path (VERIFY) | The analyst report is from 2023. Everpure's Metadata Advantage paper says DFM NVRAM and flash are distributed to per-blade authority processes | Added that context; sharpened the VERIFY | flagged |
| 18 | Worked examples (8+4 amplification, hedged reads, geo-EC 9.3 days, LIST 433k keys/s) | Recomputed | None | verified |

## Unresolved / disagreements

- **Ch 24 (outside my scope) repeats the FlashBlade//S error** at line 16 ("a blade scale-out it calls shared-everything") and in the Table row at line 118 ("Everpure calls it shared-everything"). This should be aligned with the corrected Ch 15: Pure calls Purity//FB "partitioned-writer". Ch 27 should be checked for the same wording.
- **FlashBlade//EXA data-node protection scheme** (Ch 16, 17) is still unverified. No public source documents erasure coding or failure domains across data nodes, and a 2026 third-party scorecard also lists it as unresolved.
- **FlashBlade//S multi-chassis placement and current Purity//FB PUT copy count** (Ch 15, 18) are still unverified.
- **NetApp AFF symmetric active/active in ONTAP 9.19.1** (Ch 14): this rests on a NetApp Community post. Official release-note confirmation is still pending.
- **Facebook 180 TB/day:** if someone can reach arXiv 1309.0186, the extended paper may state a median near 180 TB. The chapter now uses the conservative ">100 TB/day" from the USENIX abstract.
- **AFX supported controller count** (32 in 9.19.1) comes from a WWT summary only. It should be checked against NetApp Hardware Universe.
- **WebFetch blocked** for blog.everpuredata.com and arxiv.org. The new Everpure blog citations come from search summaries and are marked as such in the footnotes.
