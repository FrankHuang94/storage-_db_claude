# Review: Part 6a (Chapters 40–44)

**Reviewer scope:** `docs/06-industry-and-competition/40-market-structure.md` through `44-ddn.md`, plus their staging files. Reviewed 2026-11-01.

## Summary

**What I checked.** I recomputed every worked number in the five chapters:

- **Ch40:** the 2Q25 base backed out of IDC's 2Q26 growth (US$7.74B total, US$3.78B all-flash, US$1.42B high-end), the derived year-ago vendor shares, the price/volume table, and the TAM triangulation.
- **Ch41:** the valuation and revenue sums and the multiples (60×, 45.5×, 16×, 12.5×).
- **Ch42:** stripe overhead and the 11 PB raw-flash gap, the similarity-reduction example, the Rule of X inference, the SCM share and the embedding bytes.
- **Ch43:** KV bytes and the recompute-versus-fetch comparison, the OCI capacity and throughput ratios, the WEKApod 3 reduction implied by its effective-capacity claim, list-price ARR, and the sum of the funding rounds.
- **Ch44:** Eos scaling, checkpoint time, Qwen3-32B KV bytes, multiples and revenue per employee.

The arithmetic was almost all correct. I spent about 25 searches on funding, customer, product-status and MLPerf claims.

**Web access.** idc.com, docs.weka.io and huggingface.co are outside this session's allowed domains, so WebFetch failed on them. Figures from those hosts rest on search-result summaries.

**Verdicts:**

| Ch | Verdict |
|---|---|
| 40 | Solid; minor fixes (TAM labelling, Gartner VERIFY resolved) |
| 41 | Material fixes (EXA certification misstated, HPE dates, DDN "first institutional money", Everpure prepayment stated as fact, MLPerf history) |
| 42 | Material fixes (data-reduction ratio, SyncEngine/Polaris status, missing VUA, MLPerf history, xAI citation, "audited" tilt) |
| 43 | Material fixes (erasure-coding sizing rule unsupported, HPE detail, funding sum, KV "a year before NVIDIA", Series E split, pro-Everpure lines) |
| 44 | Minor-to-material fixes (VAST Colossus claim mis-cited, unsourced tenancy negative removed, MLPerf v0.5 added, VAST KV row wrong) |

**Cross-chapter consistency is now in place.** All five chapters, Ch16 and Ch29 now agree on the following:

- **VAST:** US$30B Series F (April 2026, ~US$1B, ~half secondary, Drive Capital led with Access Industries as co-lead); more than US$500M CARR on exiting FY2026; more than US$4B of bookings; the US$1.17B CoreWeave deal (~29% of bookings).
- **WEKA:** US$1.6B Series E (May 2024); more than US$100M ARR in 2024; US$100–150M ARR estimated.
- **DDN:** US$5B Blackstone round (January 2025); ~US$0.5B 2025 revenue (reported); ~US$1B 2026 target.
- **Everpure:** subscription ARR of US$2.13B (Q2 FY27).
- **HPE–WEKA:** announced November 2025, quoting ended 31 January, no orders accepted from 3 March 2026. Ch41 and Ch43 now match.
- **xAI:** "both supply Colossus; the split is unknown" in all three deep dives, with VAST's October 2025 expansion noted.
- **MLPerf Storage history:**
  - DDN entered v0.5, v1.0 and v2.0.
  - WEKA entered v0.5 and v1.0.
  - VAST has never submitted.
  - All three skipped v3.0.
- **Language:** "peer-reviewed" replaces "audited" for MLPerf throughout.

**QA after edits:** all five chapters PASS `qa_report.py`, `lint_mermaid.sh` is OK and `check_links.py --allow-planned` finds 0 broken links. Prose words: 40: 2,377, 41: 2,975, 42: 4,720, 43: 4,173, 44: 4,064. All deep dives are ≥ 3,150 and every chapter is above budget. I renumbered footnotes into order of first use wherever I added sources.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 40 | IDC 2Q26 US$10.34B +33.6%, AFA 52.1%, Dell 23.8% / +42.5%; 1Q26 Dell 31.2% | Confirmed via search summaries of IDC, StorageReview and B&F. Huawei, NetApp, Everpure and HPE shares could not be retrieved (table published as an image); derived 2Q25 shares recomputed and consistent | None | verified (partly secondary) |
| 40 | IDC AI infrastructure 1Q26: US$89.7B, storage US$2.2B = 2.4%, 2026 forecast US$497B | Confirmed | None | verified |
| 40 | Top-down "At IDC's own measured storage share" × 2026 forecast | Reads as an IDC number, but it applies a 1Q26 share to a forecast IDC gives no storage share for | Labelled as our extrapolation | fixed |
| 40 | Bottom-up floor sums CARR, a revenue target and an ARR estimate | Mixed metrics; DDN's figure includes HPC and Tintri; "January 2026 fiscal year" is not in VAST's release | Caveat added ("order of magnitude, not a sum"); FY label aligned to "fiscal year 2026"; low and high ends of the range labelled by what anchors them | fixed |
| 40 | VAST "not in reported 2026 placements [VERIFY]" | B&F 2026-08-24: VAST not included, DDN dropped; Gartner covers file and object vendors separately | VERIFY resolved with new footnote; staging line deleted | fixed |
| 41 | "Blackstone … DDN's first institutional money" | Blackstone's wording, but DDN took ~US$12M of VC around 2002 (Ch44) | Attributed to Blackstone, with the 2002 VC noted | fixed |
| 41 | Table 41.3: EXA has "No NVIDIA certification … yet" | Contradicts Ch27: Everpure claimed NVIDIA-Certified Storage for EXA in March 2026, with NCP pending and no SuperPOD certification. This understated Everpure | Corrected to match Ch27 | fixed |
| 41 | "HPE stopped reselling WEKA …"; scorecard "HPE drops WEKA (Nov 2025)" | Announcement (Nov 2025) and effective date (orders end 2026-03-03) were conflated; HPE VARs can still sell WEKA on HPE servers | Both dates given, consistent with Ch43; reseller caveat added; footnote annotated | fixed |
| 41 | "Everpure … used about US$577M of prepayments for strategic NAND" | Ch26 treats US$577M as a third-party reading with a VERIFY. Stating it as fact is a pro-Everpure overclaim | Reworded as an analyst reading, with a link to Ch26 | fixed |
| 41 | "VAST added GPU-equipped CNodes"; "WEKA launched WEKApod 3, its first chassis-up hardware" | CNode-X is announced, not shipping; WEKApod 3 deliveries start fall 2026 | Changed to "announced", with delivery timing | fixed |
| 41 | "MLPerf absences" and scorecard counter-evidence | Everpure's lead was stated without noting that the three rivals were absent; participation history missing | Added "among entrants" and each vendor's history | fixed |
| 41 | Table 41.3: EXA "audited MLPerf v3.0 lead" | MLPerf is peer-reviewed by submitters, not audited | "Peer-reviewed … among entrants" | fixed |
| 41 | NetApp AFX "GA timing [VERIFY]" | AFX ships on ONTAP 9.18.1/9.19.1 and an AFX 2K exists; the exact 1K GA date was not found | Cell sharpened with WWT footnote; staging updated | flagged |
| 41 | NVIDIA in WEKA Series E; VAST Series D with NVIDIA; Eos 48×AI400X2 ~4 TB/s; AMG GA 2025-11-18 | Confirmed | None | verified |
| 42 | "VAST's own median … about 2:1 [VERIFY]" | In January 2026 Denworth gave a 3.4:1 average across ~1,000 customers and a 1.75:1 median (B&F) | Replaced; "Don't say" corrected; VERIFY resolved | fixed |
| 42 | SyncEngine "[VERIFY scope/pricing]" | Announced 2025-08-21; catalogues POSIX, S3 and SaaS sources and syncs them; no charge to customers | Row rewritten with sources; VERIFY resolved | fixed |
| 42 | Polaris "[VERIFY whether separately sold]"; grouped under "not yet GA" | Announced 2026-02-25 at VAST Forward; Kubernetes-based; included at no extra cost; available in VAST cloud deployments | Row and Mermaid subgraph label fixed; timeline updated | fixed |
| 42 | KV-cache section omits VUA | VAST open-sourced VUA in April 2025 (Ch32 lists it). Leaving it out understates VAST's KV history | VUA added to text, timeline and the Ch43/Ch44 comparison tables | fixed |
| 42 | Series E: bookings only | VAST also stated more than US$200M ARR at the end of fiscal Q3 2023 (the basis of Ch41's 45.5× multiple); Sacra's US$200M for Jan 2025 is likely stale | Added, with ARR-versus-CARR caveat | fixed |
| 42 | CARR "fiscal year ending January 2026 [VERIFY]" | The release says "exited fiscal year 2026"; the month is not stated | Reworded; VERIFY narrowed to FY-end month | flagged |
| 42 | Rule of X inference assumes a 2× multiplier | Bessemer frames the multiplier as 2–3×; analysts use up to 3× | Added the 3× case (66–73% growth) | fixed |
| 42 | xAI "Blocks & Files later reported …" cited to the 2024 B&F and VAST blog footnotes | Wrong citation; the October 2025 B&F report also notes DDN's continuing role | Re-cited and reworded | fixed |
| 42 | "Absent from MLPerf Storage v1.0–v3.0"; "audited benchmarks" | VAST has never submitted in any round, v0.5–v3.0 (StorageReview) | Corrected; "peer-reviewed" | fixed |
| 42 | Denworth role open question | Rested on one outlet's speculation, but he was briefing press for VAST in January 2026 | Balanced; VERIFY narrowed | fixed |
| 42 | Table 42.5 caption "EXA leads on … audited results" | Pro-Everpure framing; VAST's reduction lead was omitted | Rebalanced | fixed |
| 42 | Series F investors, US$4B bookings, 228% Rule of X, FCF positive; CoreWeave US$1.17B; Google Cloud and Azure announcements Nov 2025 | Confirmed (VAST release via iTWire; Reuters). Azure GA still unconfirmed | Staging updated | verified / flagged (Azure) |
| 42 | CNode-X "due later in 2026" | Announced 2026-02-25 with Supermicro; no ship date found. The "sold first by … Cisco" claim was not corroborated in my searches | Left as written | flagged |
| 43 | "Stripe width under about a quarter of the cluster, so 16+4 implies 80+ servers" | Not in WEKA docs (per search). Docs require stripe ≤ failure domains plus spare headroom and give a 16+2-on-20-servers example; stripe width is 3–16 data (4.1 docs) or 5–20 total (current); N+2 is the default | Rewritten | fixed |
| 43 | TL;DR "first vendor to make KV-cache offload a product" | "First" is unprovable (VUA, DDN Infinia KV cache, LMCache) | "Among the first … commercial product" | fixed |
| 43 | "It shipped a KV tier a year before NVIDIA standardised one" | Unveiled March 2025, GA November 2025; STX followed in March 2026, so GA came months, not a year, ahead | Corrected | fixed |
| 43 | HPE resale end | Missing quote-end date, the VAR route and WEKA's response | Added | fixed |
| 43 | Series E "US$100M primary and US$40M secondary by employees" | WEKA's release says only "primary and secondary" | Kept with VERIFY and source; staging line added | flagged |
| 43 | History: "raised US$275M in two rounds" for 2020–2024 | Omits the US$73M January 2022 round | "About US$348M in three rounds" | fixed |
| 43 | OCI test: "42 GB per context, ~7,500 vs ~225 contexts" | The test used 100K-token contexts, not 128K | Recomputed (~33 GB, ~9,600 vs ~290); ratio unchanged | fixed |
| 43 | WEKApod 3 1.1 EB ⇒ ~2.5:1 | Correct on raw capacity; coverage cites ~3:1 on usable capacity | Note added (TechRadar) | fixed |
| 43 | MLPerf v0.5 participation (footnote cites an "unofficial" WEKA run) | WEKA was one of five official v0.5 submitters and also ran an unofficial AWS test; v2.0 absence is per StorageReview | v2.0 sourced; v1.0 VERIFY in staging deleted | fixed |
| 43 | "KV-cache losses should shrink now that PureKVA and audited MLPerf KV results exist"; "supports Everpure's integrated thesis"; Table 43.3 PureKVA "Oct 2026"; VAST "Azure listing" | Pro-Everpure tilt; PureKVA is announced, not confirmed GA (per the Part 5a review); VAST Azure GA unconfirmed | Softened, re-dated and rebalanced; "audited" → "peer-reviewed" (5 places) | fixed |
| 43 | NeuralMesh 6 GA / WEKApod 3 shipping | No GA or shipment announcement found by 2026-11-01 | Staging updated | flagged |
| 44 | "VAST Data has also claimed Colossus …[^30]" | Cited DDN's own sources for VAST's claim | New footnote (VAST blog, B&F October 2025) | fixed |
| 44 | "Tenancy is enforced at the access layer, not cryptographically [VERIFY: informal source]" | Unsupported negative about a competitor, with no footnote | Replaced with a neutral diligence question; staging reworded | fixed |
| 44 | Benchmarks section starts at v1.0/v2.0 | DDN was an official v0.5 submitter (2023) | Added with sources; heading and "Don't say" updated | fixed |
| 44 | TL;DR "sat out MLPerf v3.0, where Everpure posted the top checkpoint result" | Everpure plug in a DDN TL;DR; omitted that VAST and WEKA also sat out | Reworded | fixed |
| 44 | Table 44.2 VAST KV tier: "CNode-X with NVIDIA context-memory support" | CNode-X is the GPU node for vector search and SQL; the KV path is the BlueField-4 CNode plus VUA (Ch42) | Corrected; PureKVA re-dated | fixed |
| 44 | Eos "delivery about 93% of datasheets" | 93% uses 4.3 TB/s; the headline is 4.0 TB/s (87%) | "87–93%" | fixed |
| 44 | Blackstone US$300M at US$5B; "first institutional investor"; B&F US$500M (2023) and US$750M est. (2024) | Confirmed by search summaries; still conflicts with Forbes' US$400M/US$500M | Staging annotated | verified (secondary) |
| 44 | Qwen3-32B 64 layers / 8 KV heads / head dim 128 | Matches my recollection of the model card; huggingface.co blocked, so not confirmed | VERIFY kept | flagged |

## Unresolved / disagreements

- **IDC 2Q26 vendor shares (Ch40).** Huawei 11.3%, NetApp 9.6%, Everpure 8.1% and HPE 6.8% could not be re-confirmed: idc.com is blocked and the table is an image. Dell 23.8% and the totals are confirmed. Someone with IDC access should check them.
- **VAST fiscal year-end month (Ch40, 41, 42).** The release says only "exited fiscal year 2026".
- **VAST Azure Native ISV Service GA (Ch42, Ch43).** I found no GA confirmation. VAST's own release page appears to contain unfilled placeholders, so treat its "now available" wording as unreliable.
- **CNode-X shipping status and whether Cisco sells it (Ch42 Table 42.1).** Only the Supermicro launch was found.
- **WEKA Series E primary/secondary split (Ch43 text and `data/ch43_funding.csv`).** The CSV still shows US$40M secondary. I did not change the chart because the split is plausible but unconfirmed.
- **WEKApod 3 per-rack 10.2 TB/s / 210M IOPS, and NeuralMesh 6 GA (Ch43).** Neither confirmed.
- **DDN revenue base (Ch41, Ch44).** Forbes gives US$400M/US$500M; B&F gives US$500M (2023) and US$750M est. (2024). These cannot both be right, and Ch41's 12.5× multiple uses the Forbes figure. I disagree mildly with leading on the Forbes figure, but have no proof either way.
- **Blackstone–DDN date.** Ch41 says 2025-01-09 and Ch44 says 2025-01-08. The Business Wire ID suggests January 8 and press coverage says January 9. Immaterial; left as is.
- **VAST write-acknowledgement mechanics (Ch42).** "Mirrored into SCM on two enclosures" matches Ch16, but I could not confirm the exact copy count against VAST documentation in this session.
