# Review: Part 1 (Chapters 1–6)

**Reviewer scope:** `docs/01-storage-fundamentals/01-what-storage-does.md` through `06-data-protection-and-resilience.md`, their SVG and chart assets (`ch02-media-hierarchy.svg`, `ch02-nand-cell.svg`, `ch06-rebuild` chart and CSV, `ch02_hdd_vs_nand_cost.csv`) and their staging files. Reviewed 2026-11-01.

## Summary

I re-derived every worked example: the WAF fixed point, DWPD, map DRAM per TB, Little's law, the M/M/1 tails, the 32-die SSD knee, the fan-out probabilities, the capacity waterfall, the full five-year TCO and its sensitivities, the DRR blends and the $/effective-TB table, the dedupe index size and collision odds, the EC overheads, rebuild hours, URE odds, the fibre round trip and the 5 PB restore. Most of the arithmetic is correct. The WAF model (u = e^-(1-u)(1+OP)) reproduces 7.8 / 4.1 / 2.1 exactly, and the TCO table recomputes to $4.29M against $1.33M.

The material problems were in physics framing, in one growth-rate calculation, in one rebuild model and in how some contract terms were described. These are listed below.

I used about 30 web searches. As the brief warned, vendor hosts, SEC and blocksandfiles were not fetched directly; I cite them from search summaries, and the footnotes say so.

**Verdicts:**
- Ch 1: solid. One VERIFY resolved.
- Ch 2: material fixes (HBM latency in the pyramid, erase mechanism, P/E ranges, the Backblaze rate, HDD seek, the Table 2.1 caption).
- Ch 3: minor fixes (LDPC retry sequence, entry width, Micron DRAM resolved, FDP evidence strengthened).
- Ch 4: material fixes (Evergreen//One billing described wrongly, the FlashArray "3.9:1" misread, the TCO price-input mismatch now disclosed).
- Ch 5: minor-to-material (WEKA history wrong, DeepReduce baseline resolved, guarantee bias balanced).
- Ch 6: material fix to the declustered rebuild model; scope of the Dell guarantee corrected; immutability comparison made fairer.

**QA after edits:** all six chapters PASS `qa_report.py`, all Mermaid blocks lint OK, and there are 0 broken links. Word counts went up. Footnotes were renumbered in order of first use. Reading times were updated for Ch 2, 5 and 6. The ch02 and ch06 charts were regenerated.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 2 | Pyramid SVG: HBM "~100 ns class"; TL;DR "memory 100–300 ns" | Wrong for a GPU. A cache-missing load to HBM takes ~350 ns on H100 (pointer chase), slower than CPU DRAM. HBM is a bandwidth tier | SVG reads "~350 ns from GPU"; desc and footnote note added; text sentence with an arXiv cite; TL;DR changed to 100–400 ns | fixed |
| 2 | Pyramid SVG: HBM $/GB "$10–20" vs text "$8–18"; SSD "$0.10–0.80"; HDD "30–44 TB" | Internal inconsistency. $0.10/GB is mid-2025 QLC, which contradicts the chapter's own 18–23× premium | Changed to $8–18, $0.30–0.80 and 20–44 TB | fixed |
| 2 | "Erase pulls charge out by raising the channel or well voltage" (text and SVG) | Floating-gate picture. Charge-trap erase is mainly hole injection that neutralises trapped electrons; 3D strings often generate holes by GIDL because the poly channel has no body contact | Text and SVG rewritten; ISPP, multi-pass TLC/QLC programming and ~16 kB pages added; QLC tPROG put in ms | fixed |
| 2 | "GC … the DRAM-refresh of flash" | Loose analogy (refresh is closer to retention scrubbing) | Reworded as "a background tax, much as refresh is for DRAM" | fixed |
| 2 | DWPD ≈ P/E ÷ (WAF × days) | Omits the raw/user (OP) term | Formula corrected. Anchored with Micron 6600 ION ratings: 1.0 DWPD at 128 KB sequential vs 0.3 at 16 KB random, implying ~2,000 P/E for current QLC | fixed |
| 2 | Table 2.1: TLC ~1,000–3,000, QLC ~500–1,500 P/E | Too low. They are inconsistent with the Micron 7450 MAX (3 DWPD) and 6600 ION (1.0 DWPD sequential) ratings once OP and WAF are backed out | TLC 3,000–10,000 and QLC 1,000–3,000; derivation stated; VERIFY sharpened | fixed / flagged |
| 2 | Table 2.1 caption "each added bit gives 33%, 25% then 20%" | Wrong sequence for SLC→PLC (it is 100/50/33/25%) | Corrected | fixed |
| 2 | "Each extra bit halves the voltage margin" | Gaps go 1→3→7→15, so roughly halves (SLC→MLC is a third) | "roughly halves" in TL;DR and SVG | fixed |
| 2 | Retention: "about three months … at end of life" | Accurate, but readers take it as typical life | Clarified as the JESD218 end-of-life floor; fresh drives retain longer, unguaranteed | fixed |
| 2 | HDD: "~4–5 ms seek → 8–10 ms → 100–125 IOPS, ~4 IOPS/TB" | Seek is 10k/15k-rpm territory. Nearline drives are spec'd ~8 ms and measure higher. It also conflicted with Ch 4's 170 IOPS at QD16 | ~12 ms, ~80 IOPS at QD1, ~170 at QD16, 3–6 IOPS/TB; consistent with Ch 4 | fixed |
| 2 | Backblaze $0.11→$0.014/GB 2009–Nov 2022 "≈0.5%/month, ~6%/yr" | Arithmetic error. Correct is ~1.2%/month, ~14%/yr | Corrected | fixed |
| 2 | 22.6× Q1 2026 cited to PCSP (SEO page) | Low-tier source; QLC vs TLC basis not stated | Re-cited to Blocks & Files and Tom's Hardware (VDURA index, QLC basis, 4.9× in Q2 2025). Noted the index switched bases and HDD rose $668→$1,216; chart CSV updated | fixed / flagged |
| 2 | Mozaic 4+ 44 TB (VERIFY, SEO source) | Confirmed by Seagate IR, 2026-03-03 | VERIFY removed | fixed |
| 2 | Blackwell Ultra 288 GB (VERIFY) | Confirmed (12-high HBM3E) | VERIFY removed; footnote updated | fixed |
| 2 | Pre-2020 milestone VERIFY | RAMAC is cited in Ch 1 to the Computer History Museum | Resolved; only the 2016–22 layer points remain background | fixed |
| 3 | LDPC: "re-reads at shifted voltages, giving soft information" | Conflates read-retry (shifted Vref, hard decode) with soft decoding (multiple bracketing reads → LLRs) | Escalation sequence corrected | fixed |
| 3 | Table 3.1 "~4 B/entry" at 245 TB / 16 KB | 15 billion units exceed 2³², so entries need ≥34 bits | Note added; column marked "(floor)" | fixed |
| 3 | Micron 6600 ION DRAM (VERIFY, 64 GB vs 16 GB) | TweakTown and TechRadar's body text both say 64 GB; only the headline says 16 GB. Reviews credit the 16 KB IU with ~3× the random writes of 64 KB-IU rivals | VERIFY resolved | fixed |
| 3 | FDP CacheLib 1.3→1.0 (VERIFY) | Confirmed. The same deck shows 3.5→~1 at full utilisation; EuroSys 2025 paper reports ~1 with no host OP | Strengthened; VERIFY removed | fixed |
| 3 | LightNVM "2017" | Merged in Linux 4.4 (2016); FAST paper 2017 | Timeline split 2016 / 2017 | fixed |
| 4 | "Evergreen//One metered on effective used capacity, with a floor at the reserve commitment plus 25%" | Wrong. The 25% is a capacity buffer Everpure keeps deployed (up to 1 PiB), not a billing floor. The customer pays the reserve commitment plus on-demand usage, both on EUC | Rewritten; Everpure support doc added | fixed |
| 4 | "FlashArray//XL R5 1.9 PB raw → 7.4 PB effective implies ~3.9:1" | Misread. Everpure's effective figures assume a 5:1 average DRR; 3.8× is effective/raw after RAID, metadata and TiB conversion | Corrected; product-page footnote added | fixed |
| 4 | TCO inputs: QLC $302/TB (122 TB street) vs HDD $22/TB (Q1 2026) | The implied 13.7× media premium sits well below the 22.6× headline used in the same chapter, and HDD rose to ~$40/TB by Q3 2026 (per the same index) | Disclosed in text; added a sensitivity (~2.7× at Q3 2026 HDD prices) to the TL;DR and Numbers table | fixed / flagged (Ch 38) |
| 4 | Hybrid platform "$40 per raw TB" | The $0.77M total only works if the flash tier carries $150/TB | Row label clarified | fixed |
| 4 | Waterfall shows a TiB "loss" | It is a unit change, not lost bytes | One-line clarification | fixed |
| 4 | VDURA 22.6× and ServNet HDD prices (2 VERIFY) | Corroborated by B&F's VDURA figures ($2,450→$15,121 QLC; 4.9×→22.6×) | VERIFYs removed; source and VDURA's vendor interest noted | fixed |
| 4 | All other worked numbers (Little's law, M/M/1 4.6×/6.9×, 255K IOPS at QD32, 63%/64%/99%, waterfall, TCO and its 2.0×/1.6×/parity sensitivities) | Recomputed | None | verified |
| 5 | "WEKA adding data reduction in NeuralMesh 6 (2026)"; similarity listed as VAST + Everpure only | Wrong history. WEKA has had cluster-wide, post-process, 4K-block similarity plus delta reduction since WEKA 4.2 (2023) | Timeline, history, TL;DR and inline/post-process text fixed; WEKA row added to Table 5.3 | fixed |
| 5 | DeepReduce baseline (VERIFY); "always-on in October" | The 2:1 median is measured on top of already-compressed data. Always-on was announced late September for October | VERIFY removed; dating aligned with Ch 27 | fixed |
| 5 | Evergreen//One "reportedly" EUC-billed (VERIFY) | Confirmed by an Everpure support doc | VERIFY removed | fixed |
| 5 | "Everpure inverts … more honest" | Pro-Everpure. A workload-sized guarantee depends on the vendor's own sizing, and Dell's 6:1 needs no assessment or signature | Balanced both ways | fixed |
| 5 | Dell 6:1 Gen 3 (PowerStoreOS 5.0); 5:1 Gen 2/PowerMax; NetApp 4:1 SAN / 3:1 virt NAS / 1.5:1 NAS; Right-Size //X and //XL | Confirmed (some Dell regional pages still say 5:1) | None | verified |
| 5 | StorReduce US$20.5M | It is the net 10-K figure; it was announced as ~$25M | "net of cash acquired" added | fixed |
| 5 | Worked examples (31:1 total-efficiency, harmonic blend, Table 5.2, 10⁻⁵⁵ collisions) | Recomputed | None | verified |
| 6 | Declustered rebuild: "100 drives × 0.5 GB/s → 1.4 h" | Ignored the k× read amplification the paragraph itself mentions. With 16+2, 50 GB/s of output needs 800 GB/s of reads | Re-specified as 4 GB/s read per drive with 8+2 stripes → 50 GB/s output → 1.4 h; 16+2 and 146+4 consequences shown. Chart note and CSV updated (the numbers did not change) | fixed |
| 6 | DFM evacuation "tens of minutes" for 150 TB (VERIFY) | Not found in any source; implies ~40+ GB/s from one module. The 95% claim exists but has no published baseline | Phrase removed; labelled company-stated; VERIFY sharpened | flagged |
| 6 | Dell Cyber Recovery Guarantee in the PowerMax row | It covers PowerProtect DD Cyber Recovery vaults (US$5M production + US$5M vault), not PowerMax | Scope corrected in the table and Numbers row | fixed |
| 6 | "ROW snapshots are nearly free, so SafeMode can default on" as Everpure differentiation; NetApp described thinly | NetApp tamperproof snapshots cannot be shortened even by NetApp support; it also has ARP detection and MAV | Fairer comparison; detection vendors added; differentiation narrowed to the replacement-array SLA | fixed |
| 6 | WAFL/ZFS called "log-structured" | They are write-anywhere and self-describe as "copy-on-write" | Wording fixed; terminology trap noted | fixed |
| 6 | URE odds "should hit more than one error" | Spec is a ceiling; field rates are lower | Caveat added | fixed |
| 6 | Sync replication "four to nine times slower" | 1.15/0.15 = 7.7, so the range is four to eight; FC without write acceleration needs two round trips | Corrected and noted | fixed |
| 6 | Evergreen//One cyber SLA (VERIFY); ActiveCluster 2017 (VERIFY); RAID-5 2007 article (VERIFY) | Headline SLA terms confirmed (next-business-day shipping, 48 h plan, 8 TiB/h, covers DR too); ActiveCluster/Purity 5.0 2017 and the Harris article are well established | VERIFYs removed; contract fine print still logged in staging | fixed |
| 6 | EC math, rebuild hours, 5 PB at 8 TiB/h ≈ 24 days, fibre RTT | Recomputed | None | verified |
| 1 | VAST block "VERIFY GA date" | NVMe/TCP block launched early 2025 (VAST 5.3) | Resolved with Next Platform and VAST KB | fixed |
| 1 | S3 23×, LTO 64 EB native, 131,072 writes, RAMAC | Recomputed or checked | None | verified |

## Unresolved / disagreements

- **Ch 38 (outside my scope) uses the same TCO media inputs** ($22/TB HDD from Q1 2026; $302/TB QLC from a 122 TB street price). It should carry the same caveat: the implied premium is 13.7×, not the 22.6× headline, and HDD reached ~$40/TB by Q3 2026 on the same index. Check the date of the TechRadar $37,128 price.
- **2026 SSD:HDD premium** still rests on a single hybrid-storage vendor's undisclosed-source index (VDURA), which has switched between QLC and TLC bases. TrendForce or Coughlin corroboration was not found.
- **P/E ranges in Table 2.1** are now derived from DWPD ratings, not from NAND-vendor disclosures (vendors rarely publish them).
- **DFM evacuation claim** (Ch 6, also likely in Ch 26): there is no public hours figure. Ask Everpure engineering for evacuation-versus-rebuild times at 150 TB and 300 TB.
- **300 TB DFM GA** (Ch 2, 4): only the 2023 roadmap ("2026") and B&F 2026-08-11 support it.
- **Right-Size Guarantee duration**: sources conflict (6 months in older material, 12 months in a newer blog). The chapter keeps 12 months with the VERIFY on the footnote.
- **EUC definition**: I state that Evergreen//One's effective used capacity is measured before data reduction. The billing-unit doc confirms EUC but I did not see its formal definition. Worth one check against the current Product Guide.
- **Process note:** I ran one read-only `git status` by mistake (no changes made via git).
