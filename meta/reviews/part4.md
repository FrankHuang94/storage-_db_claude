# Phase 2 review — Part 4, Everpure (Ch 25–29)

Reviewer: independent (skeptical storage engineer and buy-side analyst), 2026-11-01. Scope: `docs/04-everpure/25…29`.

## Summary

**What I checked (about 16 web searches; sec.gov, everpuredata.com and most trade hosts can't be fetched, so I relied on search-result summaries):**
- Everpure financials: the FY25 10-K naming Meta, Q3 FY26 margins, Q2 FY27 results, GAAP versus non-GAAP gross margin, guidance history, the FY28 preliminary outlook from the September 2026 Financial Analyst Meeting, and TrendForce's 4Q26 NAND forecast.
- Product facts: DFM capacities, the largest shipping SSDs, FlashBlade//EXA general availability and DFM data nodes, MLPerf Storage v3.0, and the NVIDIA certifications.
- The Meta deal and the second-hyperscaler release.

**Cross-chapter consistency:**
- **FY labels** are consistent: FY26 ended 2026-02-01 and Q2 FY27 ended 2026-08-02.
- **Ticker** is consistent throughout: PSTG → P effective 2026-04-17. It is stated in full only in Ch 25 Era 5, and Ch 25, 26 and 29 use "NYSE: P, formerly PSTG".
- **ARR, RPO, revenue, FCF and guidance** now match across Ch 25, 28 and 29.

**Verdicts:**
- **Ch 25: minor fixes.**
- **Ch 26: minor fixes.**
- **Ch 27: material fixes.** Certification status, EXA GA, the MLPerf absentee list and the checkpoint worked example were wrong or incomplete.
- **Ch 28: minor fixes.** Removed bias and duplication.
- **Ch 29: material fixes.** The Meta disclosure claim was wrong, GAAP and non-GAAP margins were mixed in the worked example, and the hyperscale margin was overstated.

**Word count (scripts/wordcount.py):** Part 4 went from **11,413 to 10,934**.
- Ch 25: 2,066 → 1,971
- Ch 26: 2,508 → 2,435
- Ch 27: 2,490 → 2,366
- Ch 28: 2,298 → 2,168
- Ch 29: 2,051 → 1,994

Every chapter is still ≥ 108% of budget. QA is PASS for all five, Mermaid lint is OK, and check_links reports 0 broken.

**Housekeeping:** I renumbered footnotes in order of first use in all five chapters, dropping unused definitions (Ch 28 [old 21, 22] and Ch 29 [old 12]). I also removed resolved items from the staging files `meta/open-questions-staging/ch25–29.md`.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 29 | TL;DR "widely reported as Meta"; Don't-say "Meta is a disclosed customer in the 10-K. Filings describe an unnamed top hyperscaler"; VERIFY on the first naming date | **Wrong.** The FY2025 10-K names Meta as the December 2024 design win. The CEO also cited Meta at the March 2025 EXA launch. Ch 25 already said so, so Ch 25 and Ch 29 contradicted each other. | Text now says Meta was named in the FY25 10-K, with a new footnote. The Don't-say now warns against claiming the *second* hyperscaler has been named. VERIFY resolved. | fixed |
| 26 | "analysts identified it as Meta" | Same issue. | Now says the FY2025 10-K named Meta. | fixed |
| 29 | Worked example: "Q3 FY26 total GM rose to 72.3% from 70.2%" set against a non-GAAP 69.9% base | The comparison mixed GAAP (72.3%) with a non-GAAP base. It also omitted management's statement that the newer hyperscale models (Everpure supplies components) bring margins closer to the company average. | Now uses non-GAAP product GM 72.9% (from 67.4%) and GAAP 72.3%, both labelled. The text now treats 85% hyperscale GM as an upper case. | fixed |
| 26, 28, 29 | Product GM 66.2% and subscription GM 74.9% with no basis stated | These are non-GAAP: 687×66.2% + 499×74.9% reproduces the 69.9% non-GAAP total. | Labelled non-GAAP everywhere. | fixed |
| 26 | "fewer components per terabyte, so 66.2% product gross margin … even during a NAND price spike" | Causal overclaim (pro-Everpure). Non-GAAP product GM fell from 72.9% in Q3 FY26 to 66.2%. | Reworded: the lower BOM supports margin but does not protect it, with the decline shown. | fixed |
| 29 | FY28 outlook marked [VERIFY] | Resolved. The FAM (2026-09-23) gave preliminary FY28 revenue of $7.0–7.3B (+39–45%) and non-GAAP operating income of $1.7–1.9B. It expects the new vectors (data software, Scale AI, hyperscale) to reach only about 20% of revenue by FY2030. | Added, with a footnote. The 20% figure is also a useful brake on the "platform company" narrative. | fixed |
| 29 | Second hyperscaler | The text left out the release's own caveat that the customer may not order the volumes contemplated. | Caveat added. | fixed |
| 25 | TL;DR: hyperscale wins "arrived as FY2027 revenue guidance rose to $5.03–5.07B" | Implied the licence wins caused the guidance raise. Hyperscale is a small share of FY27 revenue. | Reworded. | fixed |
| 25 | "FY2027 Q2 FCF −$238M because the company prepaid for NAND" | The cause was overstated (the prepaid reading is third-party) and the FY label was inconsistent. | Changed to "Q2 FY2027 … after strategic NAND and component purchases", matching Ch 26 and 29. | fixed |
| 25 | "FY2022 rose 29%… Part of that rise came from Meta" | Unsourced attribution. | Changed to "Meta became the showcase AI customer". | fixed |
| 25 | Guidance "Raised from $4.3–4.4B" | Incomplete: the guide was $4.3–4.4B in Feb 2026, $4.41–4.51B in May and $5.03–5.07B in August. | Now labelled "Initial guide (Feb 2026)". | fixed |
| 25 | VAST "$30B valuation" | A private-company figure without the required label. | Labelled *reported by CNBC*. | fixed |
| 25 | DirectFlash launch date [VERIFY] | Resolved: FlashArray//X, April 2017 (press release and The Register). | Footnote added. | fixed |
| 27 | TL;DR / body: "FlashBlade//S holds DGX SuperPOD certification"; NVIDIA-Certified Storage only | Incomplete. In March 2025 FlashBlade also got NCP high-performance-storage certification (HGX B200/H200), as Ch 29 already said. | Added to the TL;DR and body. Ch 27 and Ch 29 now agree. | fixed |
| 27 | "EXA gained NVIDIA-Certified Storage status in March 2026" | Coverage differs on whether it was granted or planned. | Reworded to "Everpure said NVCS validation extended to EXA". NCP is still pending. | fixed |
| 27 | No EXA GA date | GA was declared at Accelerate in June 2025 (TechRepublic). | Added, with a footnote. | fixed |
| 27 | MLPerf v3.0: "VAST, WEKA and DDN did not submit" | Correct but incomplete. Blocks & Files also lists Dell, Huawei, IBM and NetApp as absent. | Absent list widened, with a footnote. | fixed |
| 27 | Checkpoint worked check: "roughly trillion-parameter model at ~16 bytes/param" | The workload is 1.25T parameters. 16.7 TB ÷ 1.25T ≈ 13 B/param. | Corrected. | fixed |
| 27 | "PureKVA and always-on DeepReduce arrived in October 2026" | They were announced 2026-09-30, and the body said September. | Fixed. | fixed |
| 27 | SPEC data-node model [VERIFY, garbled extract] | Resolved: Supermicro ASG-1115S-NE316R, running Purity//DN 1.0, per the SPEC text disclosure. | Model named; VERIFY removed. | fixed |
| 27 | DFM data nodes | Still unconfirmed as GA. The terms of use still describe third-party servers. | VERIFY sharpened with that evidence. | flagged |
| 27 | "no proprietary client … advantage against WEKA and Lustre" | One-sided. VAST makes the same standard-client argument, and WEKA/Lustre clients give finer client-side control in exchange. | Counterpoint added. | fixed |
| 26 | "245.76 TB for the largest standard drive" | Sandisk announced 256 TB UltraQLC for 1H 2026, but shipment is unconfirmed. | Now reads "largest standard SSD confirmed shipping (Sandisk has announced 256 TB)". | fixed |
| 26 / 29 | TrendForce 4Q26: Ch 26 said +23–28% [VERIFY]; Ch 29 said +15–20% | Both were right but measure different things: overall NAND contract prices +15–20% (TrendForce release, 2026-09-30) and enterprise SSD +23–28% (secondary coverage). | Both chapters now state both, citing the primary release. VERIFY resolved. | fixed |
| 26 | "a position no SSD-buying competitor shares" (NAND exposure) | Misleading. Competitors also face NAND inflation, through SSD prices. | Reframed: Everpure competes for raw-NAND allocation with the IDMs' own SSD businesses. | fixed |
| 26 | FlashBlade 2016 raw NAND [VERIFY] | Resolved: the original blades carried MLC NAND chips, not SSDs (The Register, Computer Weekly). | Footnote added. | fixed |
| 28 | Table 28.2 Everpure steelman: "fastest share gains" | Unsourced cheerleading. | Removed. Added the weak spot "software mostly sold with arrays". | fixed |
| 29 | Table 29.2 caption: "the only array vendor monetising its flash design inside hyperscalers" | Absolute claim. | Now "only array vendor publicly known to…". | fixed |
| 29 | Neocloud bullet: CoreWeave stake | Missing counterpoint. | Added that CoreWeave later signed a far larger deal with VAST. | fixed |
| 28 / 29 | Evergreen//One +73% and TCV $277M repeated in both chapters | Duplication. | Kept in Ch 29 only; Ch 28 now cross-links. | fixed |
| all | Word budget | Part 4 was at 11,413. | Trimmed repeated material: the Portworx price (three mentions), the history paragraphs that restated timelines, extra semiconductor bridges, duplicated certification and cloud lists in Ch 29, and wordy playbook answers. | fixed |

## Unresolved / disagreements

- **Ch 26: 300 TB DFM status.** The FY26 10-K "released in 2025" reading comes only from a search summary. A June 2025 StorageReview piece said 300 TB modules were "expected by end-2025". No GA or ship press release was found. The VERIFY marker stays.
- **Ch 27: FlashBlade//EXA NCP and SuperPOD certification** is still pending as of the latest public sources, and DFM-based data nodes are still not confirmed GA. Both are key gates for neocloud deals.
- **Ch 29: hyperscale gross margin.** The analyst estimates (75–85%, >90% for pure royalties) conflict in spirit with management's comment that the newer models bring hyperscale margins closer to the company average. I treat 85% as an upper bound. The real figure is undisclosed.
- **Ch 29: Q4 FY26 product GM "67.3%, up more than 400 bp on mix".** Not confirmed whether this is GAAP or non-GAAP, or whether the comparison is year on year. Left as is.
- **Ch 25: CUSIP.** The text says the CUSIP is unchanged after the rename. That rests on the research note citing the ticker-change release; I did not confirm it independently.
- **Style note.** I renumbered footnotes in all five chapters. Any other agent editing these files should re-read the Sources sections rather than reuse old footnote numbers.
