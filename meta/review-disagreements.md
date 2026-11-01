Merged from the `## Unresolved / disagreements` sections of the independent reviews in `meta/reviews/` (Phase 2). Each item is something a reviewer could not resolve from public sources reachable in this environment, or a disagreement with the drafting author.

### From `part0.md`

- **Ch 26 vs Ch 14, FlashArray NVRAM.** Ch 26 (text and Fig 26.1) says "NVRAM mirrored across both controllers". Ch 14 (Part 3a) says it is chassis-resident and dual-homed (//m) or on DFMD modules (//XL). One of them should change. 0.2 now uses neutral wording.
- **Ch 27 Fig 27.1 caption** says both families forked into TLC performance and QLC capacity tiers. Ch 27's own Table 27.1 lists FlashBlade//S on QLC DFMs. The caption should be fixed by the Ch 27 owner.
- **Ch 29 line 59** still reads "Analysts identified the customer as Meta", even though Ch 29's TL;DR (after Part 4) says Meta was named in the FY25 10-K. Note also that one Aug 2026 search summary says "Everpure has not confirmed" Meta. The 10-K naming rests on search summaries of the filing.
- **Ch 59 title and the outline** say 200 flashcards, but the deck has 279.
- **300 TB DFM.** "Released in 2025" still rests only on a search summary of the FY26 10-K. No GA or ship release was found. The Ch 26 VERIFY stands.
- **ARR precision.** Search summaries of the Q2 FY27 release round to "$2.1B". The atlas's $2.13B comes from the chart CSV note.
- **Part 4 open item resolved.** The ticker-change release (Nasdaq/PR Newswire, 2026-04-07) confirms the CUSIP is unchanged, as Ch 25 says.
- **`meta/open-questions.md`** still reports 200 VERIFY markers. There are 177 inline. Rerun `scripts/build_meta.py`.

### From `part1.md`

- **Ch 38 (outside my scope) uses the same TCO media inputs** ($22/TB HDD from Q1 2026; $302/TB QLC from a 122 TB street price). It should carry the same caveat: the implied premium is 13.7×, not the 22.6× headline, and HDD reached ~$40/TB by Q3 2026 on the same index. Check the date of the TechRadar $37,128 price.
- **2026 SSD:HDD premium** still rests on a single hybrid-storage vendor's undisclosed-source index (VDURA), which has switched between QLC and TLC bases. TrendForce or Coughlin corroboration was not found.
- **P/E ranges in Table 2.1** are now derived from DWPD ratings, not from NAND-vendor disclosures (vendors rarely publish them).
- **DFM evacuation claim** (Ch 6, also likely in Ch 26): there is no public hours figure. Ask Everpure engineering for evacuation-versus-rebuild times at 150 TB and 300 TB.
- **300 TB DFM GA** (Ch 2, 4): only the 2023 roadmap ("2026") and B&F 2026-08-11 support it.
- **Right-Size Guarantee duration**: sources conflict (6 months in older material, 12 months in a newer blog). The chapter keeps 12 months with the VERIFY on the footnote.
- **EUC definition**: I state that Evergreen//One's effective used capacity is measured before data reduction. The billing-unit doc confirms EUC but I did not see its formal definition. Worth one check against the current Product Guide.
- **Process note:** I ran one read-only `git status` by mistake (no changes made via git).

### From `part2.md`

- **Ch 7:** Exact GA month of Purity//FA 6.4.2 (NVMe/TCP). Sources conflict between 2022 and 2023.
- **Ch 7:** Crehan Research FC +6% (2025) remains search-summary only.
- **Ch 8 / Ch 11:** FlashBlade//S GDS/NFS-over-RDMA support (Purity//FB 4.3.4, Oct 2023) rests on an iThome search summary. It does not appear in NVIDIA GDS release-note partner tables. Someone with Everpure release-note access should confirm. This also bears on Ch 34's "FlashBlade//S holds the full set."
- **Ch 8 / Ch 11:** FlashBlade//EXA GDS rests on a Portworx doc search summary. NVIDIA certification for EXA is not public. A SPECstorage AI_IMAGE disclosure (Jan 2026, Purity//FB 4.6.4) describes RDMA-enabled pNFS to data nodes. It could be cited in Ch 16/27 if useful.
- **Ch 9:** FlashBlade S3-over-RDMA GA status. Pure promised it "later this year" in 2025; no GA notice found by 2026-11-01. If it is still not GA, Ch 11's "Everpure has announced it" is accurate but should not be upgraded to "ships".
- **Ch 10:** Everpure's Spectrum-X +25% read / +23% write figures were not found in any search. Keep the VERIFY or drop the figures. MetaRoCE (Aug 2026) is still unverified.
- **Ch 11:** The Lambda list price (US$3.99 vs US$2.99) is unresolved. It does not change the conclusions, since the mid-tier is illustrative.
- **Ch 12:** Largest shipping E1.S/E3.S capacities, U.2 power class, the CXL 3.1 release day, and the 2015–2019 Optane dates are still VERIFY. E1.S dimensions (33.75 × 118.75 mm) look like the enclosure dimensions; the PCB is 31.5 × 111.49 mm. I left this unchanged.

### From `part3a.md`

- **Ch 24 (outside my scope) repeats the FlashBlade//S error** at line 16 ("a blade scale-out it calls shared-everything") and in the Table row at line 118 ("Everpure calls it shared-everything"). This should be aligned with the corrected Ch 15: Pure calls Purity//FB "partitioned-writer". Ch 27 should be checked for the same wording.
- **FlashBlade//EXA data-node protection scheme** (Ch 16, 17) is still unverified. No public source documents erasure coding or failure domains across data nodes, and a 2026 third-party scorecard also lists it as unresolved.
- **FlashBlade//S multi-chassis placement and current Purity//FB PUT copy count** (Ch 15, 18) are still unverified.
- **NetApp AFF symmetric active/active in ONTAP 9.19.1** (Ch 14): this rests on a NetApp Community post. Official release-note confirmation is still pending.
- **Facebook 180 TB/day:** if someone can reach arXiv 1309.0186, the extended paper may state a median near 180 TB. The chapter now uses the conservative ">100 TB/day" from the USENIX abstract.
- **AFX supported controller count** (32 in 9.19.1) comes from a WWT summary only. It should be checked against NetApp Hardware Universe.
- **WebFetch blocked** for blog.everpuredata.com and arxiv.org. The new Everpure blog citations come from search summaries and are marked as such in the footnotes.

### From `part3b.md`

- **FlashBlade//EXA data-node protection scheme** (Ch 24 engineer question, Ch 16/17). Still undocumented in public sources. Ch 24 now says so explicitly.
- **Everpure Q2 FY27 product/subscription gross margins (66.2% / 74.9%)**. These come only from Quartr and investing.com summaries; I couldn't fetch the 8-K exhibit from sec.gov. They are probably non-GAAP and are now labelled that way. Confirm against the 8-K gross-margin table.
- **Broadcom FY2025 infrastructure software revenue (~US$27B)**. Plausible, but not confirmed; check the 10-K.
- **Evergreen//One Overdrive** (Ch 23). No source found for its terms or GA.
- **Meta Tectonic flattened into one ZippyDB schema** (Ch 21, Blocks & Files 2026-07-27). The search returned nothing, so the VERIFY stays.
- **Pure1 Manage MCP server GA** (Ch 22). It is described only in an Everpure blog, seen via search summary.
- **Ch 24 heatmap remains atlas judgment.** I would still have Everpure field engineers sanity-check the contentious cells, especially the new pNFS-split quadrant position. The staging ASK/VERIFY is kept.
- **Ch 27 (outside scope).** I grepped for "calls it shared-everything" and similar FlashBlade wording, and found no remaining instances outside Ch 15/16 (where it now appears only in corrective context).
- **Network.** usenix.org and docs.aws.amazon.com don't resolve in this session, and blog.everpuredata.com and sec.gov were not fetched. All checks against those sources rely on search summaries.

### From `part4.md`

- **Ch 26: 300 TB DFM status.** The FY26 10-K "released in 2025" reading comes only from a search summary. A June 2025 StorageReview piece said 300 TB modules were "expected by end-2025". No GA or ship press release was found. The VERIFY marker stays.
- **Ch 27: FlashBlade//EXA NCP and SuperPOD certification** is still pending as of the latest public sources, and DFM-based data nodes are still not confirmed GA. Both are key gates for neocloud deals.
- **Ch 29: hyperscale gross margin.** The analyst estimates (75–85%, >90% for pure royalties) conflict in spirit with management's comment that the newer models bring hyperscale margins closer to the company average. I treat 85% as an upper bound. The real figure is undisclosed.
- **Ch 29: Q4 FY26 product GM "67.3%, up more than 400 bp on mix".** Not confirmed whether this is GAAP or non-GAAP, or whether the comparison is year on year. Left as is.
- **Ch 25: CUSIP.** The text says the CUSIP is unchanged after the rename. That rests on the research note citing the ticker-change release; I did not confirm it independently.
- **Style note.** I renumbered footnotes in all five chapters. Any other agent editing these files should re-read the Sources sections rather than reuse old footnote numbers.

### From `part5a.md`

- **Ch11 (outside my scope)** still carries "[VERIFY: announcement date]" for Dynamo. That date is now confirmed as 2025-03-18 (NVIDIA Newsroom, cited as Ch32 footnote 19), and Ch11 can drop the marker.
- **SuperPOD storage tables** (Ch31 H100, Ch34 B200/B300): only the H100 per-SU read row (15/40/125) has been seen, and only in a snippet. The per-node 40/20 figures, the 62 GB/s write, the B200 standard/enhanced 40/20 and 125/62, and the B300 640/2,000 figures need a direct read of docs.nvidia.com, which is blocked in this session.
- **NVCS Enterprise-level GPU count** (~1,000) is unconfirmed.
- **Kokolis et al. 1.8 h projection at 16K GPUs** comes from secondary summaries. arXiv 2410.21680 should be checked.
- **Llama 3 §3.3 figures** are consistent with my reading of the paper, but arXiv was unreachable in this session.
- **PureKVA:** whether it actually reached GA in October 2026, and the test conditions behind the 20× TTFT claim, are both open.
- **Pinecone sale exploration** (Ch33): two searches found nothing. The VERIFY stays. If no primary report surfaces, consider softening to "faced reported strategic pressure" or deleting the clause.
- **VAST in NVIDIA's Series E** (Ch34): unresolved, VERIFY retained.
- **Common Crawl ">10 PB"** and the **S3 500T objects** figures (Ch30): still search-summary only, VERIFY retained.

### From `part5b.md`

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

### From `part6a.md`

- **IDC 2Q26 vendor shares (Ch40).** Huawei 11.3%, NetApp 9.6%, Everpure 8.1% and HPE 6.8% could not be re-confirmed: idc.com is blocked and the table is an image. Dell 23.8% and the totals are confirmed. Someone with IDC access should check them.
- **VAST fiscal year-end month (Ch40, 41, 42).** The release says only "exited fiscal year 2026".
- **VAST Azure Native ISV Service GA (Ch42, Ch43).** I found no GA confirmation. VAST's own release page appears to contain unfilled placeholders, so treat its "now available" wording as unreliable.
- **CNode-X shipping status and whether Cisco sells it (Ch42 Table 42.1).** Only the Supermicro launch was found.
- **WEKA Series E primary/secondary split (Ch43 text and `data/ch43_funding.csv`).** The CSV still shows US$40M secondary. I did not change the chart because the split is plausible but unconfirmed.
- **WEKApod 3 per-rack 10.2 TB/s / 210M IOPS, and NeuralMesh 6 GA (Ch43).** Neither confirmed.
- **DDN revenue base (Ch41, Ch44).** Forbes gives US$400M/US$500M; B&F gives US$500M (2023) and US$750M est. (2024). These cannot both be right, and Ch41's 12.5× multiple uses the Forbes figure. I disagree mildly with leading on the Forbes figure, but have no proof either way.
- **Blackstone–DDN date.** Ch41 says 2025-01-09 and Ch44 says 2025-01-08. The Business Wire ID suggests January 8 and press coverage says January 9. Immaterial; left as is.
- **VAST write-acknowledgement mechanics (Ch42).** "Mirrored into SCM on two enclosures" matches Ch16, but I could not confirm the exact copy count against VAST documentation in this session.

### From `part6b.md`

- **Ch 41 and Ch 43 still carry the old EXA certification wording (outside my scope; please harmonise).**
  - Ch 41 line 184 reads "NVIDIA-Certified Storage claimed for EXA in March 2026".
  - Ch 43 Table 43.3 reads "STX partner; NVIDIA-Certified Storage (Mar 2026)".
  - Both should read "extension of NVIDIA-Certified Storage validation announced Mar 2026; no completed EXA certification found by 2026-11-01".
- **Ch 44 Table (KV-cache tier, VAST column)** says "CNode-X with NVIDIA context-memory support". In Ch 42 and Ch 45, VAST's KV play is the BlueField-4 CNode plus VUA, while CNode-X is the GPU-in-storage node. The Ch 44 reviewer should check this.
- **Ch 49 Matrix 3, WEKA momentum 0.48 vs Hammerspace 0.58.** This is arguably harsh on WEKA, given that AMG came first, NeuralMesh 6 and WEKApod 3 launched, and the OCI validation exists. I left it because "flat valuation, HPE exit" is a defensible reading. Worth checking with competitive-intelligence staff.
- **Ch 49 KV-cache cells.** Everpure ● and VAST ◐ are borderline under the chapter's own legend. I did not change the cells and suggest the main agent decide whether PureKVA should be ◐ until GA is confirmed.
- **Still open:** VAST Azure GA status, NeuralMesh 6 GA, and the exact HPE storage figure from the 8-K table. All are in staging.

### From `part7.md`

- **Ch51 / Ch52, search-summary-only chart anchors.** These remain VERIFY in the CSV status column and staging: RAMAC $10,000/MB (IBM's own estimate is ~$11.4k/MB), the 3380 list-price range, the SunDisk 1991 point, the Semico/iSuppli 2005 $45/GB figure, the 2008 TrendForce NAND shares and the TrendForce 2026 wafer-spot readings. None of them changes an order of magnitude or a direction, but the 2008 shares drive the HHI comparison.
- **Ch51, Symmetrix 41% vs IBM 35% (1995).** This still rests on one Register interview. Keep the "by one account" framing.
- **Ch53, PureKVA/CMX and trend 1.** The Colgrove 600 TB / 1 PB statements and Meta's 512 TB statement are still unverified. The Gartner agentic-ops forecast (<1% → 20% by 2028) is still search-summary only.
- **Ch53, Fig 53.2 vs text.** "Disaggregation and DPUs" is called "table stakes" in the text but plotted in the "Bet now" quadrant, while the chart's "Table stakes" quadrant means high certainty and low impact. This is a wording clash rather than an error; the author may want to rename the quadrant or the call.
- **Ch54, "four deals in 17 years cost about $594M".** This implies about $20M for StorReduce, which I did not verify. The total is within rounding either way.
- **Ch54, the WEKA ~16× ARR and VAST ~60× committed-ARR marks in Gate 3.** Both are company-stated and sourced via Ch 43. I left them in because they are valuation benchmarks, not targets.

### From `part8.md`

- **Ch 45 and Ch 49 (Part 6, outside my scope; no Part 6 review file exists yet)** still call EXA's MLPerf v3.0 results "audited". Ch 49's TL;DR also says Everpure "is the only array vendor selling that IP into hyperscalers". Ch 34 / Part 5a and Ch 29, 36 / Part 4–5b have already changed these to "public, peer-reviewed" and "only array vendor publicly known to…". Part 8 now uses the corrected wording, so until the Part 6 reviewer aligns those chapters, Part 8 and Part 6 disagree.
- **Ch 59 title vs content.** The outline, `mkdocs.yml`, `docs/index.md` and `README.md` say "200 flashcards" (and "60 one-liners" for Ch 58), but the chapters contain 279 cards and 66 one-liners. I did not change the H1 or the navigation, which are fixed by `meta/outline.md`. The main agent may want to update the index blurbs ("279 flashcards", "66 one-liners").
- **Ch 59 has no cards for Ch 54** (strategic option map), which was completed after the deck. A few Ch 54 cards could be added when the deck is next regenerated.
- **Cards carry the upstream VERIFYs implicitly.** Q135 and Q261 (300 TB DFM "released 2025"), Q181 (NVCS Enterprise ~1,000), Q43 (FC +6%, search-summary only) and Q226 (HPE stopped reselling WEKA) are only as solid as their chapters. If those VERIFYs resolve differently, regenerate the cards.
- **PureKVA GA.** Ch 55, 57, 58 and 59 and the lineup SVG now say "announced for October 2026". If Everpure confirms GA, update all five places together.
- **Ch 55 / Ch 28: customer base for the Fusion attach rate** (~14,500 vs ~15,000) is still VERIFY. The ~8% figure is unchanged either way.
- **Network.** No web searches were used; every fact was checked against the reviewed chapters and the review files.

