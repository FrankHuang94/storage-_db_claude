# Review: Part 7 (Chapters 51–54)

**Reviewer scope:** `docs/07-history-and-future/51`–`54`, the Ch51/Ch52 chart CSVs and scripts, the Ch53 radar and Ch54 strategy-map SVGs, and staging files ch51–ch54. Reviewed 2026-11-01.

## Summary

**What I checked.**

- **History dates and firsts.** I checked each of these against primary sources or reputable press:
  - RAMAC (1956, ~3.75 MB) and the IBM 3380 (1980, 2.52 GB)
  - the RAID paper (SIGMOD 1988) and EMC Symmetrix (1990)
  - NetApp (founded 1992, first filers 1993) and Isilon (2001; EMC bought it in 2010 for $2.25B)
  - S3 (2006-03-14) and NVMe 1.0 (March 2011)
  - Fusion-io (ioDrive 2007; sold to SanDisk in 2014)
  - Pure Storage (incorporated October 2009; FA-300 announced August 2011; GA May 2012)
  - XtremIO, Violin, Nimble, Dell–EMC and Portworx
  - NOR (IEDM 1984) and NAND (IEDM 1987)
  - Samsung V-NAND (2013-08-06) and Micron–Elpida (2013-07-31, $615M for the equity)
  - the IMFT unwind (2018–19, plus the Lehi sale to TI)
  - Intel NAND → SK hynix/Solidigm (2021 and 2025 closings), the Kioxia IPO and the Sandisk spin-off (February 2025)
- **Charts.** I re-derived the Ch51 decline rates: disk ≈26%/yr and flash ≈35%/yr, which agree. I also checked the Ch52 rates: ≈35%/yr, and a 13–15× surge from the 2023 trough. Every CSV row carries a source, an `as_of` date, a basis and a status. The scripts mark search-summary points as hollow, label the bases differently, use dotted guide lines and state "mixed bases". No decimals are implied beyond the source.
- **Ch53 radar.** I computed each radar dot's radius against the ring radii. All 12 dots sit in the ring and colour that Table 53.2 gives them.
- **Ch54 precedents and Rule 5.** I checked every Ch54 precedent and reviewed the chapter against Rule 5.
- **Searches.** About 22 web searches. WebFetch was not used: the key hosts (sec.gov, vendor sites, Blocks & Files) refuse it. Several resolutions therefore rest on search-result summaries, and the footnotes say so.

**Verdicts**

| Ch | Verdict |
|---|---|
| 51 | Solid; minor fixes |
| 52 | Minor-to-material fixes: the HHI was computed on the wrong basis, a wrong product name, and six VERIFYs resolved |
| 53 | Minor fixes: one forecast mischaracterised, a missing conflict-of-interest fact, the quadrant caption miscounted, and timing calls needed sharpening |
| 54 | Material fixes for Rule 5 (named private companies sat in the "Buy option" column); precedent values corrected or confirmed; all VERIFYs resolved |

**QA after edits:** all four chapters PASS `qa_report.py` (51: 2,851/2,500; 52: 2,730/2,300; 53: 3,335/3,000; 54: 2,599/2,200). `lint_mermaid.sh` is OK (8 blocks) and `check_links.py --allow-planned` finds 0 broken links. I did not change any SVGs or CSVs; they were already consistent.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 51 | "Everpure was #4 at 8.1% share and the fastest-growing vendor" | IDC 2Q26 says fastest *among the top five* (+50.0% YoY). This also aligns with Ch54. | Reworded with the +50.0% figure | fixed |
| 51 | "Micron bought bankrupt Elpida for US$615M" | Per the 10-K, $615M bought Elpida's *equity*; creditor recoveries were separate. Saying "bought for $615M" overstates how cheap the deal was. | "paid US$615M for bankrupt Elpida's equity" | fixed |
| 51 | Timeline and era dates (RAMAC, 3380, RAID 1988, Symmetrix 1990, NetApp 1992/93, FC-PH 1994, S3 2006, Fusion-io 2007, Pure 2009/2012, XtremIO 2012, Violin 2016, Nimble 2017, Dell–EMC 2016) | All consistent with sources | none | verified |
| 51 | Fig 51.2, $/GB chart | Points are sourced and the bases are labelled. Hollow markers flag search-summary points. The text says "read for direction and orders of magnitude, not decimals". The ~1981 "small drives" point ($500k/GB) sits above the 1980 3380 point; it is a different drive class, and it is labelled. | none | verified (acceptable) |
| 52 | NAND invention: "Kioxia 1987 vs SHMJ 1988 … the company's date, not an undisputed one" | The NAND cell was published at IEDM in December 1987 (Masuoka, Momodomi, Iwata, Shirota, Tech. Digest pp. 552–555). 1987 is the defensible date; SHMJ's 1988 appears to be a later announcement. Ch 2 already uses 1987, so the atlas is now consistent. | Rewrote the paragraph and the "Don't say this" bullet; added the IEDM citation to fn 4 | fixed |
| 52 | NAND HHI "about 2,260 for 2Q26 (33.5² + 20.7² + …)" | Wrong basis. Those shares are shares of the *top-five total* (they sum to 100), while the 2008 shares are market shares. TrendForce's 2Q26 market shares are 29.3/18.2/15.1/13.6/11.4 (top five = 87.6%), which gives an HHI of about 1,730. The "less concentrated" conclusion is stronger, not weaker. | Rewrote with market shares, the 87.6% figure and a directional caveat; updated the Numbers row | fixed |
| 52 | "ServeTheHome called Seagate's 15K.6 the likely final 15K series" | Wrong product. The Cheetah 15K.6 dates from about 2007; the article (c. 2017) is about the last Enterprise Performance 15K drives. | Corrected and dated; VERIFY removed | fixed |
| 52 | Playbook: "is PLC worth it at a 20% bit gain?" | PLC adds 25% bits per cell; 20% is the ideal cost-per-bit cut (Table 52.1 is correct) | Reworded | fixed |
| 52 | SLC→MLC row `[VERIFY]` | Resolved: Toshiba/SanDisk 1 Gb MLC NAND, Comdex, November 2001, the first MLC *NAND* (MLC had already shipped in NOR) | Row filled; source added to fn 20 | fixed |
| 52 | "~$1.9B net" for SK hynix's final Intel payment `[VERIFY]` | Intel 8-K of 2025-03-27: about $1.9B, net of adjustments | Added to fn 51; VERIFY removed | fixed |
| 52 | Elpida completion date `[VERIFY]` | Micron FY2013 10-K: 2013-07-31 | Text and fn 30 updated | fixed |
| 52 | "Almost no wafer capacity in 2026 [VERIFY: secondary]" | TrendForce's 2Q26 NAND release says suppliers prioritise DRAM/HBM capex over new NAND capacity | Added TrendForce support; VERIFY removed | fixed |
| 52 | Table 52.2 dates and values (WD–SanDisk, Toshiba Memory, IMFT, Kioxia IPO, Sandisk spin) | Consistent | none | verified |
| 52 | Table 52.3 Pure FA-300 at "$5–10 per usable GB" (2011–12) | Matches 2011 press. The 2012 HA model was quoted at $4–8. | none | verified |
| 53 | Trend 8: Gartner's "80% by 2029" used as independent evidence for storage + catalog + governance + vector convergence; "date has already moved out a year" | Mischaracterised. Gartner forecasts *file-and-object platform consolidation*, which is a narrower claim. Its 2023 version (70% by 2028, from 35%) was *raised* to 80% by 2029, not delayed. | Rewrote: the forecast now supports only the platform half of the trend; VERIFY resolved | fixed |
| 53 | Trend 11: Cerabyte "counts Western Digital as an investor" | Omits that Pure Storage made a strategic investment in Cerabyte (July 2024), with John Colgrove on its board. That is a conflict-of-interest fact the reader needs. | Added to the text and to Table 53.2 (row 11); sources added to fn 18 | fixed |
| 53 | Trend 1 call: "1 PB-class by 2029–30" | The only source is an undated co-founder webinar. The timing is the author's extrapolation, not a roadmap. | Added explicit note: extrapolation of the 75→150→300 TB pace; no dated 600 TB or 1 PB roadmap is public | fixed (calibration) |
| 53 | TL;DR "HAMR takes nearline drives … toward 100 TB by about 2029" | A vendor roadmap stated as fact | "Vendor HAMR roadmaps take…" | fixed |
| 53 | "Roadmaps a vendor controls end to end fare better: Pure … met it" | One flattering data point generalised into a rule; Pure also depends on NAND suppliers | Softened; "one data point, not a rule" | fixed |
| 53 | Trend 6: CPO "in production" `[VERIFY]` | NVIDIA said "in production" on 2026-05-31; TrendForce reported shipments to some partners by July 2026; broad availability is unconfirmed | Text sharpened; fn 29 annotated; VERIFY removed | fixed |
| 53 | Fig 53.2 caption "Four trends sit in 'bet now'" | Five points sit in quadrant 1 (object over RDMA at y = 0.56) | Caption corrected; noted the positions are author judgment | fixed |
| 53 | Table 53.2 caption "well placed on … convergence"; "No competitor ships a proprietary module at 300 TB" | Mild pro-Everpure tilt. Ch54 rates Data Intelligence "early". No steelman against the module lead. | "early but unproven on convergence"; named IBM FCM as the nearest analogue; added the FDP / 512 TB steelman | fixed (bias) |
| 53 | Radar SVG vs scorecard | All 12 dots match ring and colour (checked by computing radii) | none | verified |
| 54 | Table 54.1 Buy column: "Cyera is a category leader at a reported $12B mark", "WEKA (last mark $1.6B) and Hammerspace (>$500M) are category examples" | **Rule 5.** Named private companies in a "Buy option" column read as implied targets, which breaks the chapter's own "never a named private company as a target" rule. The table was also inconsistent with Fig 54.1, which lists only completed precedents. | Replaced with completed or announced precedents (Veeam–Securiti, Everpure–1touch; NetApp–PEAK:AIO). Valuation marks moved, unnamed, into the trade-offs column as price benchmarks. | fixed |
| 54 | "That makes them likelier partners, or rival bidders, than targets" | Implies that Veeam and Salesforce were being weighed as targets, and that Everpure is a bidder | Reworded as a price-level observation | fixed |
| 54 | TL;DR / Fig 54.1: "entered the top three layers only in 2026" | Wrong layers. The 2026 entries are layers 5, 7 and 8; layer 6 (Pure1/Portworx) dates from 2020 or earlier. | Corrected in both places | fixed |
| 54 | IBM–Confluent ~$11B EV, 2026 close `[VERIFY]` | Announced 2025-12-08 at $31/share (~$11B EV); closed 2026-03-17. The 10-Q shows ~$11.6B total consideration on an accounting basis. | Year → "2025 → 2026"; sources added to fn 39; VERIFY removed | fixed |
| 54 | Palo Alto–Chronosphere "$3.35B (*reported*) [VERIFY]" | The price is company-announced (2025-11-19; cash plus replacement equity awards) | Relabelled; year → "2025 → 2026"; fn 38 updated | fixed |
| 54 | Cohesity–Veritas "Combined company >$7B (*company-stated*)" | Not in the closing release. The ~$7B is the combined-company valuation reported at announcement, not a price, and the price was undisclosed. | Relabelled "Price not disclosed; combined company ~$7B (*reported*)" | fixed |
| 54 | HPE–Juniper Gate 5 example `[VERIFY in staging]` | Confirmed: DOJ suit (January 2025); settlement of 2025-06-28 (Instant On divestiture, Mist AI source-code licence auction); close July 2025 | Remedies added; HPE settlement release added to fn 27 | fixed |
| 54 | Lenovo–Infinidat ">$500M (*estimated*)" | Announced January 2025, closed 2026; price undisclosed, with Globes estimating above $500M | Globes added to fn 40 | verified |
| 54 | NetApp–DataPelago (2026-07-16, undisclosed); AMD–MEXT (2026-06-15, undisclosed) | Confirmed | none | verified |
| 54 | SK hynix–Intel "$9B" | The headline figure; actual proceeds were $7B plus ~$1.9B net | Clarified in Table 54.2 | fixed |
| 54 | "NetApp's buying spree" | Loaded wording for two small deals | "NetApp's two 2026 deals" | fixed (bias) |

## Unresolved / disagreements

- **Ch51 / Ch52, search-summary-only chart anchors.** These remain VERIFY in the CSV status column and staging: RAMAC $10,000/MB (IBM's own estimate is ~$11.4k/MB), the 3380 list-price range, the SunDisk 1991 point, the Semico/iSuppli 2005 $45/GB figure, the 2008 TrendForce NAND shares and the TrendForce 2026 wafer-spot readings. None of them changes an order of magnitude or a direction, but the 2008 shares drive the HHI comparison.
- **Ch51, Symmetrix 41% vs IBM 35% (1995).** This still rests on one Register interview. Keep the "by one account" framing.
- **Ch53, PureKVA/CMX and trend 1.** The Colgrove 600 TB / 1 PB statements and Meta's 512 TB statement are still unverified. The Gartner agentic-ops forecast (<1% → 20% by 2028) is still search-summary only.
- **Ch53, Fig 53.2 vs text.** "Disaggregation and DPUs" is called "table stakes" in the text but plotted in the "Bet now" quadrant, while the chart's "Table stakes" quadrant means high certainty and low impact. This is a wording clash rather than an error; the author may want to rename the quadrant or the call.
- **Ch54, "four deals in 17 years cost about $594M".** This implies about $20M for StorReduce, which I did not verify. The total is within rounding either way.
- **Ch54, the WEKA ~16× ARR and VAST ~60× committed-ARR marks in Gate 3.** Both are company-stated and sourced via Ch 43. I left them in because they are valuation benchmarks, not targets.
