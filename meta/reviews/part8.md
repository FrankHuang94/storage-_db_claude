# Review: Part 8 (Chapters 55–60, Conversation Toolkit)

**Reviewer scope:** `docs/08-conversation-toolkit/55-talking-with-pms.md` through `60-cheat-sheets.md`, the three Ch 60 SVG posters (`ch60-protocol-poster.svg`, `ch60-architecture-poster.svg`, `ch60-product-lineup.svg`) and `meta/open-questions-staging/ch60.md`. Reviewed 2026-11-01.

## Summary

Part 8 is synthesis. Its chapters were written from chapter drafts that have since been corrected by the Phase 2 reviewers, so this review was mainly a consistency pass. No new web research was needed.

**Method:**
- I read every Phase 2 review file (`part1`, `part2`, `part3a`, `part3b`, `part4`, `part5a`, `part5b`; no `part6a`/`part6b`/`part7` file existed yet), listed each changed fact, and grepped Part 8 for it.
- I read all six chapters in full: all **279 flashcards**, all **66 one-liners**, all **150 questions and 41 "Listen for" notes**, the 104-entry acronym sheet, and the text of all three SVGs.
- For each card I compared the answer with the corrected wording in its linked chapter's TL;DR or Numbers table. A script also checked every numeric token in all 279 card answers and all 66 one-liners against the text of the linked chapter, and every token was found there. Numeric drift was therefore not the problem; the problems were wording that the reviewers had since qualified.
- I rendered the two SVGs I edited (headless Chromium) to check that no text overflows.

**Verdicts:**

| Ch | Verdict | Main reasons |
|---|---|---|
| 55 | Minor fixes | PureKVA "GA" stated as fact; EXA certification status out of date; competitor counter-questions needed a public-information guard |
| 56 | Minor fixes | FlashArray write path described as "mirrored NVRAM"; MLPerf called "audited" (three times); 300 TB DFM release stated without its search-summary caveat; "probe in person" column |
| 57 | Minor fixes | NVRAM wording in a Listen-for note; Q107 asked for a non-public certification date; TL;DR count (40 vs 41) |
| 58 | Minor fixes | Neocloud "storage ~1% of capex"; $/s range; "NAND stockpiling"; guidance "raised from"; MLPerf line missing the read figure |
| 59 | Minor-to-material fixes | 16 cards or passages still carried pre-review wording: HBM/memory latency, "halves" the margin, the GPU-slot escape route, "~1% of capex", the unconfirmed NVCS Enterprise ~1,000 count, "audited", "only array vendor", the KV-cache scale caveat and others |
| 60 | Minor fixes | Purity//DN described as part of the Purity data-path OS; dual-controller poster showed only a mirrored NVRAM; //S certification incomplete; the //XL effective-capacity basis was missing |

**Already consistent before this review:** FlashBlade//S as partitioned-writer, and EXA as a metadata/data split rather than DASE (Ch 59 Q88–Q92, Q142, Q231; Ch 60 TL;DR, table and posters). Also consistent were Meta named in the FY25 10-K, non-GAAP labels on 66.2% / 74.9%, the Evergreen//One 25% buffer, the DFM described as having "no drive-level FTL" (not "the only vendor-owned module"), NYSE: P (formerly PSTG), the EXA NCP-pending status in Ch 59 (Q144), PureKVA "announced" in the lineup SVG, and the MLPerf absentee list in Q143. CXL 4.0 bandwidth, the Ch 31 restore arithmetic and the Ch 35 NCP eight-week rule do not appear anywhere in Part 8.

**QA after edits:** Ch 55–60 all PASS `qa_report.py`. `lint_mermaid.sh` is OK (13 blocks). `check_links.py --allow-planned` reports 0 broken links. Word counts are unchanged or slightly higher; every chapter is at or above budget. Ch 59's reading time went from ~53 to ~54 min. Both edited SVGs parse as XML and render without overflow.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 59 | Q7: memory–storage wall "DRAM-class memory (~100–300 ns)" | Part 1 corrected Ch 2 to 100–400 ns; HBM is ~350 ns from the GPU | Now "memory tiers (~100–400 ns; HBM is ~350 ns from the GPU, a bandwidth tier…)" | fixed |
| 59 | Q9: "Each extra bit per cell halves the voltage margin" | Ch 2 now says "roughly halves" (gaps go 1→3→7→15) | "roughly halves" | fixed |
| 59 | Q24: TCO "~3.2× hybrid disk" | Ch 4 TL;DR now adds ~2.7× once disk's 2026 price rise is included | Sensitivity added | fixed |
| 59 | Q33: declustered rebuild "over 100 drives cuts that to ~1.4 hours" | Part 1 re-specified the model (k× read amplification): ~4 GB/s read per drive with 8+2 → ~50 GB/s output | Assumption stated in the card | fixed |
| 59 | Q38: block protocol "two layers" | Part 2 changed Ch 7 to "command set riding a transport (plus fabric services)" | Fabric services added | fixed |
| 59 / 58 | Q64 and one-liner 30: "US$2–6 per H100-hour → US$0.57–1.75 a second" | $1.75/s corresponds to $6.16/h (Part 2 fix) | Q64: "US$2.00–6.16"; one-liner 30: "~$0.6–1.7 a second" for $2–6 | fixed |
| 59 | Q181: NVCS "Enterprise (about 1,000)" | Part 5a: the ~1,000 figure is unconfirmed (VERIFY in Ch 34) | "a figure not yet confirmed" | fixed |
| 59 / 58 | Q188, one-liner 40: "Storage is roughly 1% of a neocloud's capex" | Part 5b: this generalises one contract; Ch 35 now says "the largest disclosed storage contract is about 1% a year of its customer's capex" | Both reworded to the Ch 35 wording | fixed |
| 59 | Q198: "VAST, WEKA and DDN skipped the September 2026 round" | Correct but incomplete. Part 5a: DDN and WEKA entered earlier rounds; only VAST has never entered | Clause added | fixed |
| 59 | Q201 and Q274: "flash wins when freed watts become GPUs" | **Pro-flash overstatement** that Part 5b removed from Ch 38: freed watts help but rarely close the premium alone. The $8–37M premium is on Ch 4's inputs and is larger at index prices | Both cards now follow the Ch 38 TL;DR: bandwidth per TB or hyperscaler NAND cost; watts-to-GPUs "rarely closes the gap on its own" | fixed |
| 59 | Q143: EXA MLPerf results | Missing the checkpoint-read figure (588 GiB/s, below the 877.5 write; Part 5b) and the KV-cache scale caveat (51 hosts; Parts 5a and 5b) | Both added | fixed |
| 59 | Q232 and playbook Q2: "EXA: audited throughput" | MLPerf entries are vendor-submitted and peer-reviewed, not audited (Part 5a, Ch 34 fix) | "published, peer-reviewed benchmark throughput" | fixed |
| 59 | Q246: "the only array vendor selling that IP into hyperscalers" | Part 4 / Part 5b softened the same claim to "publicly known" in Ch 29 and Ch 36 | "only array vendor publicly known to sell…" | fixed |
| 59 | Engineer playbook Q1: "passes through NVRAM acknowledgement" | Consistent but vague; FlashArray persists to shared chassis NVRAM (Part 3a) | "acknowledgement in shared chassis NVRAM" | fixed |
| 59 | Numbers table: "Ch 54 pending" | Ch 54 now exists | Reworded: Ch 54 has no cards yet | fixed |
| 59 | All 279 cards | Every numeric token in each answer is present in its linked chapter (scripted check). I hand-checked all cards against the review files and context-checked about 70 against chapter text (Q1–Q37, Q64–Q74, Q79, Q88–Q92, Q128–Q157, Q163–Q207, Q221–Q246, Q251, Q256–Q279) | None beyond the rows above | verified |
| 55 | "PureKVA's GA and its 'up to 20×'… date from September–October 2026" | Part 4 and Part 5a: PureKVA was announced 2026-09-30 for October availability, and GA is not confirmed | Reworded to "announced… for October availability; GA not confirmed publicly" | fixed |
| 55 | "FlashBlade//EXA's certification was not on the public record" | Out of date. Everpure said NVCS validation extended to EXA (March 2026); NCP is pending. FlashBlade has also held NCP high-performance-storage certification since March 2025 (Part 4) | Rewritten to match Ch 27 and Ch 34 | fixed |
| 55 | History: "EXA's … checkpoint result, 877.52 GiB/s" | Lacked the basis | "checkpoint write… (vendor-submitted, peer-reviewed, in a round VAST, WEKA and DDN did not enter)" | fixed |
| 55 | Table 55.3 counter-questions for rivals' PMs "including a target's PMs during diligence" | Could read as advice to question competitors' staff | Added: use with colleagues, in public forums or under a diligence agreement, never to draw non-public information from a competitor's staff | fixed |
| 56 | "In a dual-controller array, a write is acknowledged once it sits in mirrored NVRAM"; whiteboard prompt 1 "active controller → mirrored NVRAM" | Contradicts Ch 13 and Ch 14 after the Part 3a fix (FlashArray uses chassis NVRAM both controllers reach; one primary controller processes I/O) | "mirrored or shared NVRAM", with the FlashArray note; "primary controller" | fixed |
| 56 | "That is an audited result"; "audited MLPerf v3.0 submissions"; "Does audited benchmarking stay a differentiator" | MLPerf is vendor-submitted and peer-reviewed (Part 5a) | "vendor-submitted, peer-reviewed"; added that DDN and WEKA entered earlier rounds | fixed |
| 56 | "DFMs reached 300 TB in 2025"; Numbers row "Released 2025" | Ch 26 keeps a VERIFY: the 10-K "released in 2025" reading is search-summary only (Part 4 unresolved) | Caveat added in text and table | fixed |
| 56 | Table 56.3 column "What to probe in person" (VAST, WEKA, DDN rows) | Implies questioning competitors directly | Renamed "What to test (from public evidence or in formal diligence)" | fixed |
| 57 | TL;DR "Forty 'Listen for' notes" | 41 in the bank and in the Numbers table | "Forty-one" | fixed |
| 57 | Q34 Listen-for "NVRAM mirror point" | Same FlashArray NVRAM issue | "NVRAM persistence point (mirrored or shared)" | fixed |
| 57 | Q107 "When, and at which level, will EXA be NVIDIA-certified?" | Asks for a non-public date (Ch 55's own Don't-say warns against this); NVCS status has also moved | "Beyond NVCS validation, what gates EXA's NCP and SuperPOD certification?" | fixed |
| 57 | Remaining 148 questions and 40 Listen-for notes | Checked against the corrected chapters (EXA split, partitioned-writer, Q81 read-below-write, Q87 PureKVA baseline, Q130 VAST/MLPerf) | None | verified |
| 58 | One-liner 8: "A rack of the largest SSDs holds ~5× a disk rack" | Dropped Ch 38's trade-off | "~5× the petabytes … at 2–3× the power" | fixed |
| 58 | One-liner 41: "EXA led v3.0 checkpointing at 877.5 GiB/s … skipped it" | Read (588 GiB/s) trails write | Read figure added; "skipped the round" | fixed |
| 58 | One-liner 52: "NAND stockpiling made free cash flow −$238M" | Part 4: the cause is stated as "strategic NAND and component purchases" | Reworded | fixed |
| 58 | Numbers table: guidance "Raised from $4.3–4.4B" | Part 4: that was the initial guide (Feb 2026), with an intermediate raise in May | "Initial guide $4.3–4.4B (Feb 2026), raised in May and August" | fixed |
| 58 | Remaining one-liners (Meta / FY25 10-K history, non-GAAP margins, EXA third-party data nodes, 300 TB vs 245.76 TB, IDC shares, $9–25B TAM) | Consistent with the corrected chapters; scripted number check passed | None | verified |
| 60 | Table 60.4: "Purity//FA, //FB, //DN — one log-structured OS family for FlashArray, FlashBlade and EXA data nodes" | Part 3a and Part 3b: Purity//DN is data-node software on third-party Linux servers, not the Purity data path; "one OS family" was narrowed to FlashArray and FlashBlade, including EXA's metadata core | Row rewritten | fixed |
| 60 | Product-lineup SVG Purity band: same claim, plus "global FTL … across every module" | Same issue | Band now reads "Purity//FB (FlashBlade and EXA metadata core), Purity//DN (EXA data-node stack)"; FTL line scoped to Purity//FA and //FB on DFMs; desc updated; rendered, no overflow | fixed |
| 60 | Architecture SVG: "NVRAM mirror / failover" and desc "mirrored NVRAM" | Same FlashArray NVRAM issue | "mirrored or shared NVRAM; failover" | fixed |
| 60 | //S row and lineup SVG: "S500 DGX SuperPOD-certified" | Incomplete. FlashBlade also holds NCP high-performance-storage certification (Part 4) | Added to table and SVG | fixed |
| 60 | //XL "up to 7.4 PB effective" | Part 1: the effective figure assumes a 5:1 average DRR | Basis added to the table | fixed |
| 60 | Table 60.5: "Five of six rows, one OS family" | Portworx and EXA data nodes are not Purity | "one OS family across the arrays" | fixed |
| 60 | Protocol SVG and Table 60.2 (NVMe/TCP Purity 6.4.2+, GA to verify; S3 over RDMA announced March 2025, GA to verify; NVMe/FC Purity 6.1; RoCE Purity 5.2) | Consistent with Ch 7 to Ch 9 after the Part 2 review | Staging VERIFY annotated with the 2022/2023 source conflict | verified |
| 60 | Acronym sheet (104 entries) | Spot-checked; DFM "no drive-level FTL" matches the Part 2 IBM FlashCore correction | None | verified |
| all | Speculation about non-public Everpure plans | None found. Strategy content is framed as public-information options (Ch 60 cites Ch 54); roadmap questions ask about trade-offs, not dates (after the Q107 fix) | — | verified |

## Unresolved / disagreements

- **Ch 45 and Ch 49 (Part 6, outside my scope; no Part 6 review file exists yet)** still call EXA's MLPerf v3.0 results "audited". Ch 49's TL;DR also says Everpure "is the only array vendor selling that IP into hyperscalers". Ch 34 / Part 5a and Ch 29, 36 / Part 4–5b have already changed these to "public, peer-reviewed" and "only array vendor publicly known to…". Part 8 now uses the corrected wording, so until the Part 6 reviewer aligns those chapters, Part 8 and Part 6 disagree.
- **Ch 59 title vs content.** The outline, `mkdocs.yml`, `docs/index.md` and `README.md` say "200 flashcards" (and "60 one-liners" for Ch 58), but the chapters contain 279 cards and 66 one-liners. I did not change the H1 or the navigation, which are fixed by `meta/outline.md`. The main agent may want to update the index blurbs ("279 flashcards", "66 one-liners").
- **Ch 59 has no cards for Ch 54** (strategic option map), which was completed after the deck. A few Ch 54 cards could be added when the deck is next regenerated.
- **Cards carry the upstream VERIFYs implicitly.** Q135 and Q261 (300 TB DFM "released 2025"), Q181 (NVCS Enterprise ~1,000), Q43 (FC +6%, search-summary only) and Q226 (HPE stopped reselling WEKA) are only as solid as their chapters. If those VERIFYs resolve differently, regenerate the cards.
- **PureKVA GA.** Ch 55, 57, 58 and 59 and the lineup SVG now say "announced for October 2026". If Everpure confirms GA, update all five places together.
- **Ch 55 / Ch 28: customer base for the Fusion attach rate** (~14,500 vs ~15,000) is still VERIFY. The ~8% figure is unchanged either way.
- **Network.** No web searches were used; every fact was checked against the reviewed chapters and the review files.
