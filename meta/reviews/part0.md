# Review: Part 0 (Ch 0.1 and Ch 0.2)

**Reviewer scope:** `docs/00-start-here/00a-how-to-use-this-atlas.md` and `docs/00-start-here/00b-one-page-map.md`, and their staging files. Reviewed 2026-11-01.

## Summary

**Why this review mattered.** Part 0 was written last, from chapter text that the Part 1–6 reviewers have since corrected. I checked it against three things:
- the current text of Ch 13, 14, 15, 25–29, 34, 37, 40, 42, 44, 45, 49 and 57–59;
- every file in `meta/reviews/`;
- 8 web searches covering the ticker, Q2 FY27 results, the second hyperscaler, the FY25 10-K naming of Meta, 300 TB DFM status, the IDC AI-infrastructure storage share, the 18.6× SSD/HDD index, and the STX partner list.

**Images.** All four embedded images exist. Each one's alt text and caption match the diagram (I checked the SVG text):
- `ch13-storage-stack.svg`
- `ch26-directflash-vs-ssd.svg`
- `ch45-four-way-architecture.svg`
- `ch29-arr.svg`

One alt-text error is fixed: RPO in the chart starts at FY2024 end, not FY2023.

Every figure that the crash course names (2.1, 13.1, 26.2, 30.1, 32.3, 45.1) exists. Every chapter link resolves.

**Verdicts:**
- **0.1: minor-to-material fixes.** The atlas statistics were stale: question, one-liner, flashcard, glossary and VERIFY counts, plus word count and reading time. The 2-week plan contradicted its own "two rehearsals a week", and day 10 was overloaded.
- **0.2: material fixes.** These came from carrying over facts the reviewers had corrected:
  - FlashBlade//S was shown as TLC.
  - The MLPerf absentee list was incomplete.
  - EXA's certification status, GA date and third-party data tier were missing.
  - The hyperscale model was described as licence-only.
  - The guidance history was incomplete.
  - Three phrasings tilted pro-Everpure.

**QA after edits:**
- 0.1: PASS, 1,771 words / 1,500 budget.
- 0.2: PASS, 1,993 / 1,500. The reading time is now ~9 min. The chapter is over budget because the additions are caveats.
- Mermaid OK. 0 broken links.
- 0.2 footnotes renumbered in order of first use. Five sources added: EXA GA, the MLPerf absentee list, NVCS status, FY25 10-K, the partitioned-writer blog and Sandisk 256 TB.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 0.2 | §5 "Both forked by media: TLC for performance (FlashArray//X and //XL, FlashBlade//S)"; Fig 0.2.6 caption | **Wrong.** Ch 27 Table 27.1 gives FlashBlade//S as QLC DFMs. FlashBlade splits by configuration, not media | Prose, diagram labels and caption corrected. Added that FlashBlade//S is "partitioned-writer", not shared-everything (Ch 15 / Part 3a finding), with a source | fixed |
| 0.2 | TL;DR, §6, numbers table, playbook: MLPerf v3.0 "a round VAST, WEKA and DDN skipped" | Incomplete. Dell, IBM and NetApp were also absent (Ch 27, B&F) | Absentee list widened everywhere; B&F footnote added | fixed |
| 0.2 | §6 "NVIDIA's SuperPOD certification belongs to FlashBlade//S" | Incomplete. It omitted the March 2026 NVCS validation extension to EXA, which has no completed certification or list entry (Part 6b's harmonised wording) | Sentence added using the harmonised wording and footnote. New Don't-say line: "EXA is NVIDIA-certified" | fixed |
| 0.2 | §5 "EXA, announced March 2025, adds off-the-shelf data nodes"; timeline "EXA announced" | GA (June 2025) was missing | GA added, with the TechRepublic footnote. Timeline reads "announced and GA" | fixed |
| 0.2 | §6 "EXA keeps metadata on a Purity core…" | Didn't say the data tier is third-party Linux/NVMe, not DirectFlash. The MLPerf row said "30 data nodes" without "third-party" | Both made explicit | fixed |
| 0.2 | Fig 0.2.7 caption "All four split metadata from data" | Inaccurate for WEKA, which has no metadata server. It also left out VAST's extra hop (Ch 45 Fig 45.1) | Caption rewritten to match Ch 45 | fixed |
| 0.2 | TL;DR "AI position is strong on evidence, thin on references" | Pro-Everpure tilt. The "evidence" is one benchmark round that most rivals skipped | "Rests on one benchmark lead, with thin references and no completed EXA certification" | fixed |
| 0.2 | §3 "300 TB DFMs against 245.76 TB for the largest shipping standard SSD" | Status and comparison caveats were dropped (Ch 26): 300 TB rests on the FY26 10-K via search summary, and Sandisk has announced 256 TB | DFM status is sourced to the 10-K and B&F. Sandisk 256 TB is noted. Power claims are flagged as vendor claims. Numbers row says "Everpure-stated" | fixed |
| 0.2 | §4 "acknowledged in mirrored NVRAM"; Fig 0.2.5 "Mirrored NVRAM" | Ch 14 (Part 3a) says FlashArray NVRAM is in the chassis, dual-homed or on DFMDs, not mirrored per controller | Neutral wording: "NVRAM that survives a controller failure" | fixed (see Unresolved: Ch 26 still says "mirrored") |
| 0.2 | §4 "The same key-value metadata engine underpins Purity//FA and Purity//FB" | Overstates Ch 26, which says Purity//FB "spreads the same ideas" | Matched to Ch 26 | fixed |
| 0.2 | §8–9, Don't-say: hyperscalers "license the design"; Everpure "paid for IP, software and support" | Incomplete. Under the standardised Feb 2026 model, Everpure also supplies some non-NAND parts (Ch 29, Part 4) | "plus parts" added in prose, Fig 0.2.10 and Don't-say | fixed |
| 0.2 | Numbers: guidance "Raised from US$4.3–4.4B in Feb 2026" | Incomplete: guidance was raised in May (4.41–4.51) and again in August (Part 4) | "Initial guide… raised in May and again in August" | fixed |
| 0.2 | Numbers: hyperscale "First customer, Meta" | Meta was named in the FY25 10-K (Part 4); the row needed that source | FY25 10-K footnote added; second win marked unnamed, with revenue from FY28 (confirmed by search) | fixed |
| 0.2 | §8 non-GAAP margins | Already labelled non-GAAP. Needed the Part 4 "cushions, doesn't protect" framing | Clause added | fixed |
| 0.2 | Fig 0.2.9 alt text "RPO rising from 2.3 billion to 4.1 billion over the same period" | The CSV shows RPO from FY2024 end, not FY2023 | Corrected | fixed |
| 0.2 | Fig 0.2.9 "ARR has compounded at about 21% a year" | Correct (1.10 → 2.13 over ~3.5 years ≈ 20.8%). But it hid the FY26 slowdown to 16% and the RPO-for-ARR trade-off (Ch 29) | Caption adds 16% / 20% and "partly at the expense of ARR growth" | fixed |
| 0.2 | §7 "Switching costs are moving into the control plane: Fusion passed 1,200 customers" | Tilt. Ch 28 notes this is under a tenth of the base | Reframed as Everpure's bet, with the adoption caveat | fixed |
| 0.2 | §9 "Everpure is a co-design partner on its BlueField-4 STX" | True but flattering. NVIDIA lists 12 storage co-design partners, including VAST, WEKA, DDN, Dell and NetApp (confirmed by search) | "One of twelve…, alongside…" | fixed |
| 0.2 | §10 "Everpure is the clearest integrated media moat" | Judgment phrased as fact | "Sits furthest into the integrated-media corner; other placements are more contestable". Quadrant values match Ch 49 Matrix 2 | fixed |
| 0.2 | Table 0.2.1 Dell/NetApp "New retrofits (Lightning, AFX)" | Mildly dismissive. Ch 46 says they built new systems | "New first-generation AI systems (Lightning FS, AFX)" | fixed |
| 0.2 | Numbers: SSD ÷ HDD ~18.6× | Single-vendor (VDURA) index for 30 TB TLC, Aug 2026; Ch 2/48 show 18.6–22.6×. Date was missing | Context and date (2026-08-21) added | fixed |
| 0.2 | VAST row "Company-stated ARR; the AI-native benchmark" | The valuation is press-reported (CNBC) | Both labels stated | fixed |
| 0.2 | Ticker P from 2026-04-17; Q2 FY27 ARR/RPO/guidance; IDC 2.4%; IDC 8.1% / Dell 23.8%; FY26 revenue $3.66B; second hyperscaler 2026-08-10 | Checked against chapters and search | None needed | verified |
| 0.1 | Numbers table: 154 questions, 64 one-liners, 200 flashcards, ≈790 glossary terms, >130k words / ≈10 h, ≈200 VERIFY | Stale. Actual: 150 questions (Ch 57 bank), 66 one-liners, 279 cards (Q1–Q279), 870 terms, 156,308 prose words (≈11 h), 177 inline VERIFY | All corrected; reading time recomputed | fixed |
| 0.1 | Fig 0.1.1 "Day 2: Parts 5 to 8"; "Every chapter in order" | The ramp covers only the core of Parts 5–6 plus Ch 53–57. The mastery table is not strictly in order (Ch 51–52 on day 5, 55 on day 6) | Labels corrected | fixed |
| 0.1 | Mastery plan: "two whiteboard rehearsals a week" (figure, README) vs only two rehearsals in the table | Internal contradiction | Rehearsals 1–4 placed on days 3, 4, 7 and 8 | fixed |
| 0.1 | Day 10: Ch 46–50, 53–54, 57, 60 plus a "full 200-card pass" plus a mock meeting | Unrealistic. About 2.4 h of reading at 1.5×, plus a 279-card pass, is well over 4 h | Ch 57 moved to day 8 (where its output is used). Full pass replaced by Ch 59's own 50-card timed test. Note added that days 9–10 run longest | fixed |
| 0.1 | 2-day ramp "About seven hours a day" | Recomputed at 1.5× header times: day 1 ≈ 6 h, day 2 ≈ 4.5–5 h | "About six hours on day 1 and five on day 2" | fixed |
| 0.1 | 2-hour crash course: 12 TL;DRs in 35 min, six figures in 40 min | Realistic (~3 min per TL;DR plus "Why this matters"; ~7 min per figure). All targets exist | None | verified |
| 0.1 | "Signature (★) diagrams" | ★ appears only in `meta/outline.md` (and one Ch 14 heading), so readers can't find it in the chapters | Says where ★ lives | fixed |
| 0.1 | Don't-say "We're #1 in MLPerf… VAST, WEKA and DDN skipped" | Incomplete list | Widened; Ch 27 link added | fixed |
| 0.1 | Label table examples (ARR $2.13B, VAST >$500M CARR, DDN ~$500M Forbes, IDC 8.1%) | Consistent with Ch 29, 42, 44, 40 | None | verified |
| 0.1 | Tone | Neutral. Table 0.1.5 applies the same evidence standard to Everpure | None | verified |

## README changes needed (not edited, per brief)

1. **"Start here" table, 2 days:** "Parts 1–4 on day 1, Parts 5–6 on day 2" → "the core of Parts 1–4 on day 1; the core of Parts 5–6 plus Ch 53–57 on day 2". Neither day covers whole Parts: Ch 10, 12 and 18–22 are skipped on day 1, and Ch 33, 36, 38, 39, 47, 48 and 50 on day 2.
2. **"Learning paths at a glance", 2-day line:** "plus Ch 53–54" → "plus Ch 53–57".
3. **2-hour crash course line:** README lists 9 TL;DRs. 0.1 lists 12 (it adds Ch 3, 25 and 29), plus six figures and the Ch 56 credibility ladder. Align the README with 0.1, or say "see 0.1 for the full list".
4. **2-week line:** "every chapter in order" → "every chapter" (0.1 interleaves Ch 51–52 and 55–57). "Two whiteboard rehearsals per week" now matches 0.1.
5. **Start-here table and Part 8 row:** "200 flashcards" → 279. "60 one-liners" → 66. The 150-question count is correct. Ch 59's own title still says "200 flashcards" (see Unresolved).
6. **Progress table** (`<!-- README-TABLE -->`) is stale. It shows Part 0 0/2, Part 7 3/4, Part 8 4/6 and a total of 136,818. `wordcount.py` now gives 156,308 words, with every Part drafted. Regenerate it.

## Unresolved / disagreements

- **Ch 26 vs Ch 14, FlashArray NVRAM.** Ch 26 (text and Fig 26.1) says "NVRAM mirrored across both controllers". Ch 14 (Part 3a) says it is chassis-resident and dual-homed (//m) or on DFMD modules (//XL). One of them should change. 0.2 now uses neutral wording.
- **Ch 27 Fig 27.1 caption** says both families forked into TLC performance and QLC capacity tiers. Ch 27's own Table 27.1 lists FlashBlade//S on QLC DFMs. The caption should be fixed by the Ch 27 owner.
- **Ch 29 line 59** still reads "Analysts identified the customer as Meta", even though Ch 29's TL;DR (after Part 4) says Meta was named in the FY25 10-K. Note also that one Aug 2026 search summary says "Everpure has not confirmed" Meta. The 10-K naming rests on search summaries of the filing.
- **Ch 59 title and the outline** say 200 flashcards, but the deck has 279.
- **300 TB DFM.** "Released in 2025" still rests only on a search summary of the FY26 10-K. No GA or ship release was found. The Ch 26 VERIFY stands.
- **ARR precision.** Search summaries of the Q2 FY27 release round to "$2.1B". The atlas's $2.13B comes from the chart CSV note.
- **Part 4 open item resolved.** The ticker-change release (Nasdaq/PR Newswire, 2026-04-07) confirms the CUSIP is unchanged, as Ch 25 says.
- **`meta/open-questions.md`** still reports 200 VERIFY markers. There are 177 inline. Rerun `scripts/build_meta.py`.
