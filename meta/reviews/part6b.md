# Review: Part 6b (Chapters 45–50)

**Reviewer scope:** `docs/06-industry-and-competition/45-head-to-head.md` through `50-diligence-framework.md`, their staging files and `data/ch45_radar.csv`. The scope also allowed one cross-chapter fix: the FlashBlade//EXA NVIDIA-certification sentences in Ch 27 and Ch 34. Reviewed 2026-11-01.

## Summary

**What I checked:**

- **Ch 45 matrix.** I checked every cell of Table 45.1 against the current text of Ch 27 (EXA), Ch 42 (VAST), Ch 43 (WEKA) and Ch 44 (DDN). I also checked Ch 32 for the KV-cache cells and Ch 34 for the certification cells.
- **Ch 45 worked numbers.** I recomputed all of them, and they are all correct: 942 GB/s and 6.9 s; 31 GB/s per data node; 1,743 GB/s ÷ 42 GB ≈ 41 contexts/s; 51.4 PB vs 62.5 PB raw, an ≈11 PB gap; and 880 GB/s and 7.4 s for DDN.
- **Ch 46.** I recomputed the IDC-implied revenues: Dell $2.45B, HPE $0.70B, Everpure $0.83B, Huawei $1.16B and NetApp $0.99B. I also checked the Dell ISG storage share (27% vs 38%) and every FY label (Dell FY ends late January, NetApp late April, HPE October, Hitachi March, Nutanix July).
- **Ch 48.** I recomputed the top-five NAND revenue: shares sum to 87.6%, revenue to $68.87B, and "others" to 12.4%. The compounded price index is 4.73×, which matches the chart's 482. I also recomputed the GM worked example (45% / 54% / $157 / +57%) and the power-versus-premium example ($6.4k against $0.8M and ≈$7M).
- **Ch 49 and Ch 50.** I checked the Ch 49 quadrant y-values against Ch 46 Figure 46.5, and the Ch 49 KV column count (10 of 16 rows). I recomputed Ch 50's weighted score (283/100) and its range (2.14–3.66).

**Web access.** About 16 searches; WebFetch failed on barchart.com, which is outside this session's allowed domains, so everything below rests on search-result summaries.

**Verified by search:**

- IDC 2Q26: $10.3B, +33.6%, Dell 23.8%, released 2026-09-10.
- Dell Q2 FY27 storage: $4.85B, +26%, guided up mid-teens.
- HPE Q3 FY26 storage: ~$1.3B, +10.2%.
- Everpure Q2 FY27: OCF −$136M, FCF −$238M, product GM 66.2%, subscription GM 74.9%, product revenue +54%.
- TrendForce 2Q26 NAND: every supplier figure.
- Lenovo closed Infinidat on about 2026-04-09.
- minio/minio archived on 2026-04-25; README marked "no longer maintained" on 2026-02-12, per the fork maintainer.
- Nutanix ARR: US$2.55B, +16%.
- TACC Horizon: 400 PB all-flash (TACC-stated).
- Still unresolved: NeuralMesh 6 GA (no confirmation found) and VAST Azure GA (unclear).

**FlashBlade//EXA NVIDIA certification (assigned inconsistency): resolved.** The public record is consistent:

- At GTC on 2026-03-16, Everpure announced it was *extending* NVIDIA-Certified Storage (NVCS) validation to EXA. StorageReview called this a "stepping stone" to the NVCS NCP level, and NAND Research described a "stated path toward" NCP.
- Blocks & Files alone wrote that EXA was "Nvidia-certified" with NCP "later this year". That wording conflicts with the other sources.
- Search extracts of NVIDIA's certified-storage systems list show FlashBlade//S500 but no EXA entry.
- No source after March reports a completed EXA certification.

Best-supported wording: *extension of NVCS validation announced in March 2026, as a step toward the NCP level; no completed EXA certification found by 2026-11-01.* I applied it to the following:

- Ch 27: TL;DR and the "Signals" paragraph.
- Ch 34: the Table 34.2 cell and the "Everpure's position" paragraph. Footnote 31 now also cites Blocks & Files.
- Ch 45: matrix cell, Table 45.3, the radar caution and `ch45_radar.csv`.
- Ch 49: the cert-depth evidence row and "Don't say this".

Ch 27's earlier wording ("Everpure claimed NVIDIA-Certified Storage") overstated the status, and Ch 34's ("in progress") was correct but softer.

**Verdicts:**

| Ch | Verdict |
|---|---|
| 45 | Minor-to-material fixes: certification wording; PureKVA "GA" overstated; VAST KV cell omitted VUA; WEKA steelman overclaimed; Table 45.2 caption miscounted runner-ups. The matrix otherwise agrees with Ch 27/42/43/44 and is fair |
| 46 | Solid; minor (a VERIFY annotated). Financials and FY labels check out |
| 47 | Solid; two MinIO VERIFYs resolved; Lenovo–Infinidat close confirmed |
| 48 | Minor fixes: YMTC "far less" overstated; TL;DR premium range unsupported at its low end |
| 49 | Minor fixes: two y-values inconsistent with Ch 46; KV and cert evidence leaned pro-Everpure |
| 50 | Minor fix: "placeholders" mislabelled a low-confidence 2. Uses public data only |

**QA after edits:** Chapters 27, 34 and 45–50 all PASS `qa_report.py`. `lint_mermaid.sh` is OK and `check_links.py --allow-planned` finds 0 broken links. Word counts are unchanged or slightly higher, and every chapter is still above budget. I renumbered Ch 45's footnotes in order of first use after adding a source.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 27/34/45 | EXA NVIDIA certification: Ch 27 "claimed NVIDIA-Certified Storage"; Ch 34 "validation in progress"; Ch 45 "NVCS validation extended… NCP pending" | Inconsistent wording, and Ch 27 overstated the status. Primary and most secondary sources describe an announced *extension* of validation toward the NCP level. Only B&F says "certified", and NVIDIA's list shows no EXA entry | One wording applied across Ch 27, 34, 45, 49 and the radar CSV; Ch 34 fn 31 adds B&F; ch45 staging line updated | fixed |
| 45 | "PureKVA on FlashBlade incl. EXA, GA Oct 2026"; "PureKVA itself only became available in October 2026"; Table 45.2 "GA only in Oct 2026" | Ch 32's reviewer found only an announced October availability, with no GA confirmation | Now "availability announced for Oct 2026" / "announced 30 September 2026, with availability slated for October"; radar CSV aligned | fixed |
| 45 | VAST KV-cache cell: "BlueField-4 CNode… hardware 2H 2026" only | Unfair to VAST: Ch 32 records VUA, open-sourced in April 2025 | VUA added with footnote; radar CSV rationale updated | fixed |
| 45 | Steelman WEKA: "on sale a year longer than anyone's" | Overclaim: AMG (Nov 2025) leads DDN's Dynamo-integrated release (Jun 2026) by about 7 months and PureKVA by about 11 | Reworded with the actual gaps | fixed |
| 45 | Table 45.2 caption: Everpure "credible runner-up in three more" | The table shows Everpure as runner-up in two archetypes (inference, consolidation) and as a challenger in neocloud | Caption corrected | fixed |
| 45 | VAST scale cell: "TACC Horizon all-flash tier (400 PB system)" | The 400 PB is TACC's figure for the all-flash storage, not the system. One report says 200 PB raw | Now "high-speed tier, 400 PB all-flash (TACC-stated)" | fixed |
| 45 | WEKA perf cell: SPECstorage #1 on all five workloads (2025-02) | Stale without context: EXA displaced the HPE/WEKA result on AI_IMAGE in 2026 (Ch 27, Ch 43) | Added "AI_IMAGE since overtaken by EXA" | fixed |
| 45 | "Don't say": KV maturity "differs by a year or more" | Overstated given the dates above | "by up to a year" | fixed |
| 45 | Radar caution: NCP certification described as an "announced item" | Nothing has been announced as achieved | "pending items: NCP-level certification, which Everpure has said it is working toward" | fixed |
| 45 | Rest of Table 45.1 (architecture, metadata, data path, protection, scale, MLPerf/SPEC, NVIDIA badges for VAST/WEKA/DDN, cloud, consumption, GTM) | Cross-checked against Ch 27/42/43/44/34: consistent (VAST SuperPOD 2023 / HPS Jul 2024; WEKA HPS Sep 2024; DDN HPS Aug 2024; HPE resale end 2026-03-03; Eos 93% of datasheet; 160 TiB entitlement) | None | verified |
| 45 | VAST Azure GA; NeuralMesh 6 GA | Searched: VAST's undated release says "now available", while coverage said "soon". No NeuralMesh 6 GA announcement found | VERIFY kept | flagged |
| 46 | IDC 2Q26 shares; Dell FY26 and Q2 FY27 storage; HPE Q3 FY26; NetApp FY26/Q1 FY27; Everpure FY26 +16% | Confirmed by IDC, Dell, Constellation, B&F and Ch 29. FY labels and period ends correct. All arithmetic correct | HPE staging VERIFY annotated (only the exact $1.29B still needs the 8-K table) | verified |
| 46 | Fig. 46.4 caption "company lines ~1.5–2x IDC" | Everpure's ratio is 1.43x, so the range is really ~1.4–2.0x | Not changed (rounding) | verified |
| 47 | MinIO: binaries stopped "[VERIFY: October 2025]"; README "no longer maintained" "[VERIFY: 12 Feb]"; archived 25 Apr 2026 | Archive date confirmed. Feb 12 comes from the fork maintainer's account (already fn 19). October 2025 comes from a secondary blog; the README confirms source-only distribution | Both VERIFYs replaced with sourced "reportedly"/"per" wording; Pinggy added to fn 17; two staging lines deleted | fixed |
| 47 | Lenovo–Infinidat closed April 2026 | Confirmed: completion announced about 2026-04-09; Calcalist estimates >US$500M | None | verified |
| 47 | Nutanix FY26 ARR US$2.55B, +16%, FY ended 2026-07-31 | Confirmed (8-K, 2026-08-26) | None | verified |
| 48 | "YMTC ships as many bits as Kioxia but earns far less" (TL;DR, Fig. 48.1) | Overstated. All non-top-five makers together had 12.4% of revenue against Kioxia's 13.6%, so at equal bit share YMTC earns at least about 9% less per bit, not "far less". Counterpoint ranking YMTC fifth also conflicts with TrendForce's top five | Now "less per bit", with the derived bound in the caption and a note on the two rankings | fixed |
| 48 | TL;DR "premium widened to ~15–22×" | The body's index readings are 18.6× and 22.6×; nothing supports 15× | "~19–23×" (VERIFY kept, single-vendor index) | fixed |
| 48 | TrendForce 2Q26 supplier revenue and shares; Everpure Q2 FY27 cash flow and margins; compounded index; worked examples | Confirmed and recomputed | None | verified |
| 49 | Matrix 1 y-values "reused from Figure 46.5" | Hitachi 0.32 vs 0.30 in Ch 46; Huawei 0.68 vs 0.66 | Aligned to Ch 46 | fixed |
| 49 | KV-cache evidence: "Everpure PureKVA GA October 2026" (●) vs VAST ◐ | Pro-Everpure: "GA" is unconfirmed, and by the legend's "new" test ● is borderline. VAST's VUA was not mentioned | Evidence row reworded (Pure KVA with Dynamo since 2025; PureKVA availability announced; ● flagged as borderline; VUA cited for VAST). Cells unchanged | fixed (cell flagged) |
| 49 | NVIDIA cert depth ● for Everpure | Rests on FlashBlade//S. EXA has no completed certification, which the chapter didn't say | Caveat added; "Don't say" line reworded (STX is a reference design, not a certification) | fixed |
| 49 | Placements vs Ch 24 (architecture classes) and Ch 46 (x/y, IDC shares) | Otherwise consistent | None | verified |
| 50 | "38% of the weight rests on placeholders" | Four of the five low-confidence dimensions are placeholder 3s, but customers is scored 2. Arithmetic (2.83; 2.14–3.66) is correct | Relabelled "low-confidence scores, four of them placeholders"; the customer score of 2 is explained | fixed |
| 50 | WEKA worked example uses public data only | Confirmed: every cell is footnoted to public sources; the SHI price is labelled VERIFY; the method-illustration disclaimer is present | Roadmap cell notes that no NeuralMesh 6 GA was found | verified |

## Unresolved / disagreements

- **Ch 41 and Ch 43 still carry the old EXA certification wording (outside my scope; please harmonise).**
  - Ch 41 line 184 reads "NVIDIA-Certified Storage claimed for EXA in March 2026".
  - Ch 43 Table 43.3 reads "STX partner; NVIDIA-Certified Storage (Mar 2026)".
  - Both should read "extension of NVIDIA-Certified Storage validation announced Mar 2026; no completed EXA certification found by 2026-11-01".
- **Ch 44 Table (KV-cache tier, VAST column)** says "CNode-X with NVIDIA context-memory support". In Ch 42 and Ch 45, VAST's KV play is the BlueField-4 CNode plus VUA, while CNode-X is the GPU-in-storage node. The Ch 44 reviewer should check this.
- **Ch 49 Matrix 3, WEKA momentum 0.48 vs Hammerspace 0.58.** This is arguably harsh on WEKA, given that AMG came first, NeuralMesh 6 and WEKApod 3 launched, and the OCI validation exists. I left it because "flat valuation, HPE exit" is a defensible reading. Worth checking with competitive-intelligence staff.
- **Ch 49 KV-cache cells.** Everpure ● and VAST ◐ are borderline under the chapter's own legend. I did not change the cells and suggest the main agent decide whether PureKVA should be ◐ until GA is confirmed.
- **Still open:** VAST Azure GA status, NeuralMesh 6 GA, and the exact HPE storage figure from the 8-K table. All are in staging.
