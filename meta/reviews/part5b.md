# Phase 2 review — Part 5b, AI storage (Ch 35–39)

Reviewer: independent (skeptical storage engineer and buy-side analyst), 2026-11-01. Scope: `docs/05-ai-storage/35…39`, their charts and CSVs, and their staging files.

## Summary

**What I checked (about 35 web searches).** cisco.com, docs.nvidia.com and files.futurememorystorage.com could not be fetched from this session, so I relied on search-result summaries for those.
- **Neoclouds:**
  - CoreWeave: 10-K FY2025 power figures, Q2 2026 power, capex and backlog, 2025 capex basis, and storage pricing.
  - Nebius: Q2 2026 targets and prepayments, and the September 2025 convertible.
  - Deals: Microsoft–Nscale, Backblaze–CoreWeave, and the Lambda–VAST history.
  - Reference designs: the Cisco NCP storage design and NVIDIA's NCP storage requirements.
- **Hyperscaler systems:** S3 scale, Google Next '26 (Rapid Bucket, Managed Lustre), Azure AMLFS 20, Meta's QLC post and its FMS 2025 deck.
- **MLPerf Storage:** v0.5 and v1.0 submitters, v3.0 participation and absentees, EXA checkpoint read and KV-cache numbers, training leaders, vector-DB design, and the rack-unit and power disclosure rules.
- **IO500:** first list (SC17) and the Sugon/Aurora ISC26 scores.
- **Ch 38:** DDN AI400X3 capacity, the VAST DBox drive class, and the Nadella podcast date. I recomputed every line of the 100 PB worked example and the rack-density and TB/W chart inputs.
- **Ch 39:** 1touch price and close date, the Digital Omnibus (Regulation 2026/1744), OSI membership, Cyera, and the NetApp AIDE GA date.

**Recomputation.** The 100 PB example's arithmetic checks out:
- Drive counts: 3,030 and 543.
- IT power: 45.5 and 23.9 kW.
- Facility power at PUE 1.3: 59.1 and 31.1 kW.
- Five-year energy: 2.59 and 1.36 GWh, so a saving of 1.23 GWh, worth about $170K.
- Media premium: $8.5–37.3M.
- Embodied carbon: 21.3 vs 2.7 kt.

The other worked numbers also check: Ch 35 margin and power, Ch 36 3FS and checkpoint maths, Ch 37 normalisation table and per-node rates, Ch 39 access decisions. **The problems were in interpretation, not arithmetic:**
- Ch 38 "escape route 1" overstated the GPU case.
- Ch 38 inherited Ch 4's flattering media premium without saying so. This was added at the coordinator's request, matching the Ch 4 fix in `part1.md`.

**Verdicts.**
- **Ch 35: material fixes.** The NCP "storage 8 weeks before GPUs" requirement was mis-stated. "Storage ≈1% of capex" generalised one contract. The Nebius convertible size was stated as if the option had been exercised. EXA's DFM power-density lever was claimed for a data tier that is still third-party servers.
- **Ch 36: minor fixes.**
- **Ch 37: minor-to-material fixes.** Four VERIFYs resolved. The EXA KV-cache lead is now caveated for scale (fairness to rivals). Checkpoint read was settled at 588 GiB/s.
- **Ch 38: material fixes.** The GPU-slot argument overstated flash's case. The media-premium caveat was missing. The DDN bar was presented as a ceiling.
- **Ch 39: minor fixes.**

**QA.** All five chapters PASS `qa_report.py`; Mermaid lint is OK; `check_links --allow-planned` shows 0 broken links.

**Word counts after edits (budget):**
| Ch | Words | Budget |
|---|---|---|
| 35 | 2,305 | 1,900 |
| 36 | 2,381 | 2,000 |
| 37 | 2,425 | 2,000 |
| 38 | 2,274 | 1,800 |
| 39 | 2,085 | 1,800 |

Reading times were updated for Ch 35, 37 and 38. Footnotes were renumbered in order of first use in all five chapters.

**Housekeeping.** Running `scripts/make_charts.py` regenerated all chart SVGs. Only the Ch 38 CSV config note changed, but matplotlib may rewrite internal SVG IDs in charts outside my scope; their content is unchanged.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 35 | NCP requirements: "storage integrated through the API eight weeks before the GPUs arrive" (body, Table 35.1, Numbers table) | **Wrong.** NVIDIA's requirements put a T-minus-8-week milestone on *data-movement systems*. Data-mover storage is due about 2 weeks before delivery. The 99.5%-per-PB uptime applies to the high-speed file system; the NFSv4 home tier has a 99.99% target. | Body, table row and Numbers row rewritten. Footnote now cites the v2.4 requirements (2026-09-01). | fixed |
| 35 | TL;DR / Don't-say: "Storage is roughly 1% of a neocloud's capex" | Generalises from one contract. CoreWeave also buys WEKA, DDN and IBM seats, builds its own object tier, and pays Backblaze. | Reframed as "the largest disclosed storage contract is about 1% a year of its customer's capex". | fixed |
| 35 | Nebius "issued about US$3.16 billion of convertible notes" | Priced at US$2.75B; US$3.16B only if the purchasers' option was exercised in full. | Corrected, with the Nebius pricing release added. | fixed |
| 35 | Nebius 5 GW target and 50–60% prepayments [2× VERIFY] | Confirmed by Q2 2026 call coverage. Also needed: contracted ≠ connected power (0.8–1 GW connected by end-2026), and more than US$9B of 2026 prepayments. | VERIFYs resolved, context added, MarketBeat footnote added. | fixed |
| 35 | CoreWeave power uses end-2025 figures only; Ch 38 uses Q2 2026 (1.5 GW / 3.7 GW) | Cross-chapter inconsistency (different dates, both right). | Q2 2026 figures added to body and Numbers table. | fixed |
| 35 | Microsoft–Nscale "reportedly ~200,000 GB300" [VERIFY] | Confirmed by Nscale's 2025-10-15 release (no value disclosed). It was listed under the November events. | Re-sourced to Nscale and TechCrunch; moved to October; VERIFY resolved. Nscale's *storage* vendor stays dashed and VERIFY in staging. | fixed |
| 35 | Table 35.2: Everpure fit = "DirectFlash power density"; caption "power density and financing as its levers" | Pro-Everpure overreach. EXA data nodes are third-party NVMe servers (Ch 37, Part 4 review), so DFM density applies only to the metadata tier today. | Fit and weak-spot cells and caption corrected. | fixed |
| 35 | Backblaze edge "$335M capacity deal" | Correct, but what Backblaze supplies was unstated. | Clarified: HDD-based tiers behind CoreWeave AI Object Storage, about US$335M over the initial orders. | fixed |
| 35 | History omitted VAST's 2023 wins | The US$1.17B deal *expanded* a relationship that began in 2023. VAST was CoreWeave's storage platform, then Lambda's (October 2023). | Added to the history, and the November 2025 deal reworded as an expansion. | fixed |
| 35 | Chart 35.3 CoreWeave 2025 capex US$14.9B "search-summary only" | Company-stated on the Q4 call, on an accrual basis; 10-K cash capex was US$10.3B. | CSV `verified` column and source updated; staging updated. Oracle stays flagged. | fixed / flagged |
| 35 | Cisco NCP 180 GB/s for 1,152 GPUs [VERIFY] | Search confirms a VAST-on-Cisco EBox NVL72 design with a 1,152-GPU topology, but not the figure. The PDF can't be fetched. | VERIFY sharpened in staging. | flagged |
| 36 | S3 "500 trillion objects and ~1 PB/s in 2025" [VERIFY] | The object count and "hundreds of exabytes" are confirmed from re:Invent 2025 coverage. The 1 PB/s figure traces to a 2024 talk via Wikipedia. | Split the claim, with a new B&F source; VERIFY narrowed to the bandwidth figure. | fixed / flagged |
| 36 | Meta QLC "10 MB/s per TB, which 16–20 TB HDDs used to meet" | The "16–20 TB" attribution is not in Meta's post. The post sets QLC at ~10 MB/s/TB, with TLC holding 15–20 MB/s/TB batch work. Meta's FMS deck puts real HDD-cluster supply at 5–7 MB/s/TB, which is weaker than the best-case 12.5 the text works out. | Rewritten with both points; FMS deck footnote added. | fixed |
| 36 | Everpure: "Only array vendor inside a top-five hyperscaler's own storage" | Not provable. | Changed to "only array vendor *publicly known* to…". | fixed |
| 36 | Google Managed Lustre "up to 10 TB/s" | Confirmed (Next '26), but it is Google's own claim (about 10× its 2025 figure). Rapid Bucket figures were also confirmed. | Labelled as Google-stated. | fixed |
| 36 | Azure AMLFS 20 | Confirmed (2025-11-18). The text missed that 512 GB/s over 25 PiB is only 20 MB/s/TiB, a capacity-heavy tier. | Context added. | fixed |
| 37 | EXA checkpoint read 588.3 vs 833.0 GiB/s [VERIFY] | 588.28 GiB/s per Everpure's release, B&F and Techzine. StorageReview's 833 contradicts its own detail paragraph. The read is *below* the 877.5 GiB/s write, which restore-heavy buyers should note. | Resolved, with that caveat. Engineer question 2 now asks why read trails write. | fixed |
| 37 | EXA KV cache "1,623.4 GiB/s on 51 hosts, far ahead of the next entrants" | Unfair framing by the chapter's own logic: the leading standard-scale entries (UBIX, FarmGPU, ~444 GiB/s) used smaller configurations. | Reworded: the lead is partly scale, so normalise per host. | fixed |
| 37 | v3.0 participation | The absentee list omitted v2.0 submitters Huawei, Hammerspace and Lightbits. Nebius and NVIDIA were first-timers. | Added. | fixed |
| 37 | WEKA MLPerf v1.0 "reportedly" [VERIFY]; v0.5/IO500 dates [VERIFY] | WEKA (and DDN) submitted to v0.5 (Sept 2023) and v1.0. The first IO500 list came at SC17 (2017-11-15). | Table 37.3 corrected; three VERIFYs resolved with sources. | fixed |
| 37 | IO500 Sugon 79,110 vs Aurora 32,166 [VERIFY] | Confirmed by Sugon's own release (500 client nodes) and Tom's Hardware. The move was for lack of widely available architecture details. | Resolved, with a source. | fixed |
| 37 | "on-premises submissions disclose power and rack units" | The rules require rack units and a *list* of powered hardware; measured power is optional. | Sharpened. | fixed |
| 37 | Vector DB "DiskANN in every submission" | B&F describes a Milvus-based test (QPS at recall). DiskANN is one index option. | Reworded; VERIFY kept on dataset size and index. | fixed / flagged |
| 37 | EXA training entry [VERIFY] | U-Net tables (YanRong 543.9, HPE K3000 345.8 GiB/s) show no EXA entry, but no source says so outright. | VERIFY sharpened with that evidence. | flagged |
| 38 | Escape route 1: 13 GPUs earn "$3.5M of gross rental… At mid-2025 prices, with exabyte scale… it starts to" | **Overstated (pro-flash).** (a) Gross rental ignores GPU capex, financing and opex. (b) It applies an H100 price to a GB200-class power slot. (c) Scale cannot help, because premium and freed watts both scale linearly with capacity. At mid-2025 prices the upper bound covers under half of the ~$8.5M premium. | Rewritten as an upper bound, cross-checked against Ch 4's $15K per kW-year (≈$1.6M), with "only alongside routes 2 or 3". TL;DR bullet adjusted. | fixed |
| 38 | Media-cost line uses Ch 4's $302 vs $22/TB (coordinator request) | The implied premium is 13.7×, not the 22.6× index. At the index's ~$504/TB, QLC media would be ~$67M. HDD rose to ~$40/TB by Q3 2026 (HDD media ~$5.4M, premium ~$35M). | Paragraph and table row added, matching the current Ch 4 text; TL;DR now reads "on Chapter 4's inputs, and more at index prices". ServNet VERIFY removed (corroborated, as in Ch 4). | fixed |
| 38 | Energy line uses PUE 1.3; Ch 4 uses 1.54 | Unflagged cross-chapter inconsistency. | Noted in the table: about $200K saving at PUE 1.54. | fixed |
| 38 | DDN AI400X3 0.21 TB/W as the lowest system bar | Configuration-dependent and unfair as a class ceiling. The AI400X3M (June 2026) offers up to 2 PB usable per appliance. | Caveat added in the text and CSV config note; VERIFY kept on per-unit capacity. | fixed / flagged |
| 38 | VAST "today's 61 TB-class DBoxes trail 245 TB-class designs" | The DBox's TB/W tracks the drive fitted; "today's" implies VAST lacks larger drives (not verified). | Scoped to the datasheet DBox in Figure 38.2. | fixed |
| 38 | FMS 2025 deck [VERIFY: Meta affiliation] | Speaker Sumit Gupta is a Meta software engineer (FMS listing). | Affiliation resolved; slide wording still VERIFY. | fixed / flagged |
| 39 | Digital Omnibus (Reg. 2026/1744) | Confirmed: published 2026-07-24, in force 2026-07-27, with Annex III / Annex I dates as stated. It also left Article 50 transparency duties at 2 August 2026, which the text omitted. | Added, with a Lewis Silkin source. | fixed |
| 39 | OSI: "Databricks, Informatica, Salesforce, dbt Labs… were in the working group" | Databricks joined only at the January 2026 update. Informatica is not named in the snippets found. Snowflake calls v1 a starting point. | Member list corrected and the starting-point caveat added. | fixed |
| 39 | 1touch US$125.0M, closed 2026-05-07; Cyera US$12B | Both confirmed (10-Q; SecurityWeek/Globes). Cyera context added (US$6B a year earlier). | — | fixed |

## Unresolved / disagreements

- **Ch 35 — Cisco NCP sizing (0.16 GB/s per GPU).** This is the low end of the "sixfold spread". Only a search summary supports it; cisco.com must be allowed in network settings to check the PDF.
- **Ch 35 — Oracle FY2026 capex US$55.7B.** The only source is secondary (citing The Register). CoreWeave Q3 2026 results, due mid-November, will date the Q2 figures.
- **Ch 35 — illustrative cost.** "US$1,000 per usable TB over four years" looks low at 2026 NAND prices: media alone is ~$302/TB raw before system markup. The utilisation conclusion holds, but the 70% margin at full sell-through flatters the neocloud. Consider a 2026-price sensitivity.
- **Ch 36 — S3 ~1 PB/s peak bandwidth.** The only source is secondary. Meta's 2024/2025/2026 engineering posts were read via search extracts only.
- **Ch 37 — v3.0 rules.** Three items need the MLCommons v3.0 results and rules pages, which were not reachable here:
  - the vector-DB dataset size (10M vs 1M) and its index type;
  - whether power and rack-space efficiency are reported metrics;
  - whether EXA entered any training workload.
- **Ch 37 — model size.** The model attribution for the 1T-class checkpoint (llama3-1t vs 1.25T) stays in staging.
- **Ch 38 — single-source inputs.** The DBox and WD JBOD watts, the FlashBlade//S500 1.3 W/TB, the DDN per-appliance capacity and the EIA price are all search-summary only. Several TB/W chart bars therefore rest on single sources.
- **Ch 38 — drive power basis.** Drive-level TB/W mixes bases: max-rated for QLC, "operating" for the 44 TB HDD, "under 10 W typical" for the DFM. The chart caption says to compare like for like, but the TL;DR's "~2×" uses mixed bases. I left it, because the direction is robust.
- **Ch 39 — open checks.** Everpure's OSI membership could not be checked; the OSI directory site was not searched successfully. The NetApp AI Data Engine GA date is still unconfirmed.
- **Process note.** `scripts/make_charts.py` regenerates every chart, and matplotlib SVG IDs are not salted (`svg.hashsalt` is unset). Running it may therefore churn chart files outside a reviewer's scope. Suggest setting `svg.hashsalt` in `scripts/charts/_style.py`.
