# Review: Part 5a (Chapters 30–34)

**Reviewer scope:** `docs/05-ai-storage/30-ai-data-pipeline.md` through `34-nvidia-ecosystem.md`, their staging files and the Ch30 chart CSV. Reviewed 2026-11-01.

## Summary

**What I checked.** I recomputed every worked number in the five chapters:

- **Ch30:** token bytes, checkpoint size and drain times, Llama 3 70B KV bytes per token, the RAG vector total, and the Horowitz energy ratio.
- **Ch31:** Table 31.1; all 16 cells of Table 31.2; Young's-formula intervals and overheads in Table 31.3, including the linear MTBF scaling to 100K GPUs; the restore-read amplification; the 167 tokens/s/GPU derivation from 41% MFU; Table 31.4; the SuperPOD scale-up; and the MLPerf-implied 16–17 TB checkpoint.
- **Ch32:** KV bytes per token for Llama 3.1 8B, 70B and 405B and for DeepSeek-V3 MLA; the 128K and 1M session sizes; sessions per DGX B200; the decode HBM-read example; recompute FLOPs (linear plus causal attention) against fetch time; the break-even GB/s; and the whole of Table 32.1, including the $/GB-hour figures.
- **Ch33:** the 1B × 1,024-dim index sizes, the HNSW link bytes, the DRAM/SSD costs against the chart CSV, DiskANN latency and IOPS, PQ compression, and Parquet read amplification.
- **Ch34:** GB/s per GPU at the SuperPOD floor.

Almost all of the arithmetic is correct and internally consistent. Ch31's 14–16 bytes per parameter agrees with Ch11's corrected example: 16 B/param as the full-state upper bound, about 14 B/param saved, and 1.12 TB for 70B.

**Web access.** WebFetch failed for docs.nvidia.com and glennklockwood.com, which are outside this session's allowed domains. NVIDIA documentation figures therefore rest on search-result summaries, and the footnotes already say so.

**Verdicts:**

| Ch | Verdict |
|---|---|
| 30 | Solid; minor fixes (one VERIFY resolved, one MLPerf label) |
| 31 | Minor fixes (restore arithmetic, MTTF-projection context, Gemini attribution) |
| 32 | Minor-to-material fixes (a wrong "does not fit" cell, a vendor-claim list that overstated VAST, PureKVA "GA" stated as fact, MLPerf KV figure needing scale context) |
| 33 | Minor fixes (Snowflake VERIFY resolved, cost-line clarity) |
| 34 | Minor fixes (ICMS→CMX naming, NVCS VERIFY sharpened, MLPerf framing de-biased) |

**NVIDIA naming and dates are consistent across Ch10, 11, 32 and 34.** I confirmed each of the following:

- Dynamo was unveiled 2025-03-18, and Dynamo 1.0 entered production at GTC on 2026-03-16.
- KVBM uses G1–G4.
- BlueField-4 STX was launched 2026-03-16. Its first rack-scale implementation is CMX, the CES 2026 ICMS platform under a new name. Partners call it the "G3.5" tier.
- STX has 12 storage co-design partners (Cloudian, DDN, Dell, Everpure, Hitachi Vantara, HPE, IBM, MinIO, NetApp, Nutanix, VAST, WEKA), 8 early-adopter clouds or labs, and AIC, Supermicro and QCT building hardware. Partner STX platforms are due in 2H 2026.
- The AI Data Platform launched in March 2025 with 10 partners.
- NVIDIA-Certified Storage has Foundation, Enterprise and NCP levels. Foundation means 128 simulated GPUs and the ladder tops out at 10,000.

**QA after edits:** all five chapters PASS `qa_report.py`, `lint_mermaid.sh` is OK and `check_links.py --allow-planned` finds 0 broken links. Word counts are unchanged or slightly higher, and every chapter is still above budget.

## Findings

| Ch | Claim / passage | Issue | Fix applied | Status |
|---|---|---|---|---|
| 30 | FineWeb "~44 TB on disk" with VERIFY | Hugging Face's official FineWeb post states "15-trillion tokens, 44TB disk space". The ~50 TB figures come from secondary sources | VERIFY removed; footnote 13 now cites the HF blog; CSV note and staging line updated | fixed |
| 30 | Gartner 565 TWh 2026; MLPerf v3.0 S3 path used by ~1/6 of submissions; Llama 3 15.6T tokens, 16M-token batch | Checked: Gartner 2026-06-10 gives 565 TWh, +26% from 447 TWh. MLCommons/Nebius say ~1/6, with 3 of 19 closed submitters using S3 | None | verified |
| 30 | Table 30.2: "877.5 GiB/s ... (company-reported)" | MLPerf results are vendor-submitted and peer-reviewed, and the major rivals did not enter. The label alone overstates the result | Relabelled "vendor-submitted", with a pointer to Ch31 for who did not enter | fixed |
| 30 | Worked numbers (62 TB of tokens, 64 MB/step, 5.7–6.5 TB checkpoint, 3.3 s / 65 s, 320 KiB/token, 40 GiB at 128K, 4.1 TB of vectors, 81 s weight load) | Recomputed | None | verified |
| 31 | Restore: "0.81 TB × 128 + 5.67 TB ≈ 109 TB ... to recover 6.5 TB of unique data" | 5.67 TB already includes the bf16 weights, so they were counted twice. 6.5 TB is the in-memory state (16 B/param), but the saved unique data is about 5.7 TB (14 B/param) | Corrected to 0.81 × 128 + 4.86 TB ≈ 109 TB to recover ~5.7 TB; restore target now 47–54 GB/s | fixed |
| 31 | "Scaling [7.9 h at 1,024 GPUs] linearly predicts about 30 minutes at 16K" | The arithmetic is right, but Kokolis et al.'s own model projects about 1.8 h at 16K GPUs (secondary summaries). Without that, the reader sees only the most pessimistic extrapolation | Added the 1.8 h projection next to Llama 3's 3.1 h | fixed |
| 31 | Llama 3: 466/47/419 interruptions, ~78% hardware, 3.1 h; 41% MFU on 16,384 GPUs; Tectonic 240 PB / 7,500 servers / 2 TB/s / 7 TB/s; 1 MB–4 GB per GPU | Consistent with the paper as I know it. 240 PB / 7,500 SSD servers is corroborated by Princeton slides. arXiv itself was unreachable | Staging VERIFY annotated | verified (secondary) |
| 31 | Table 31.2, Table 31.3 (19 min / 10.4%, 6.3 min / 3.4%, 3.5 min / 1.9% / 31 GB/s, 7.8 min / 25.6%, 1.4 min / 4.7% / 76 GB/s), restart 2.7% / 16%, 167 tok/s, 11 MB/s, 66 days, 30 × 5.67 TB | Recomputed, all correct. The 100K-GPU MTBF of 30 min is clearly labelled as an assumption | None | verified |
| 31 | MLPerf v3.0 EXA: 877.52 / 588.28 GiB/s, 17.74 s / 28.99 s, 30 data nodes, first-time submitter; VAST, WEKA and DDN absent | Confirmed by Techzine, StorageReview and MLCommons (11 first-time submitters out of 19) | Staging line updated | verified |
| 31 | SuperPOD H100 "best" 40/20 GB/s per node, 125/62 per SU (VERIFY) | A search snippet of RA Table 6 shows per-SU read of 15/40/125 (good/better/best), consistent with 125. The per-node and write figures are still unconfirmed | VERIFY sharpened in text and staging | flagged |
| 31 | "AWS's Gemini research system" | Gemini is a Rice University and AWS paper | Reattributed | fixed |
| 32 | TL;DR: "Everpure, WEKA, DDN, VAST and HPE all claim 20× or more faster TTFT" | No VAST 20× TTFT claim found. VAST claims 75% lower power, and its own table row says so. This overstated a competitor's marketing | Changed to Everpure, WEKA, DDN and HPE; VAST and NVIDIA claim power and throughput gains | fixed |
| 32 | Table 32.1, 1M-token row: "does not fit one node's HBM" | Wrong: 343 GB fits easily in a DGX B200's 1,440 GB (about 4 sessions after 71 GB of fp8 weights). It exceeds one GPU's 180 GB | Cell corrected | fixed |
| 32 | PureKVA "GA October 2026" (table and timeline) | Sources say the capabilities "will be available this October", an announced date. I found no GA confirmation as of 2026-11-01 | Changed to "availability announced for October 2026" and "PureKVA announced"; staging updated | fixed |
| 32 | EXA KV read 1,623.4 GiB/s on 51 hosts, "company-reported"; "benchmark evidence, not a marketing multiplier" | Scale context was missing. Standard-scale leaders UBIX and FarmGPU posted ~444 GiB/s on much smaller configurations, and WEKA, VAST and DDN did not enter. Uncaveated, this reads as pro-Everpure | Added per-host comparison caveat and non-entrant note | fixed |
| 32 | CMX "5× tokens/s, 5× power efficiency" dated 2026-01 | The claim was made at CES for ICMS, which was later renamed CMX | Context added in the Numbers table | fixed |
| 32 | KV bytes/token (128 / 320 / 504 / 68.6 KiB); 43 GB at 128K; 31 sessions; 86 GB per GPU per step ≈ 11 ms; recompute 4.1e16 FLOPs ≈ 2.6 s / 21 GPU-s; fetch 0.13 s; 0.43–0.96 MFLOP/byte → 2–5 GB/s; $0.023 recompute vs DRAM $0.012/h and flash $0.0006/h; 2.5M agent prefill tokens | Recomputed, all correct. Head dims and layer counts match the Llama 3.1 and DeepSeek-V3 configs | None | verified |
| 32 | Dynamo 2025-03-18, Dynamo 1.0 2026-03-16; KVBM G1–G4; "G3.5" for CMX | Confirmed (DigitalOcean/IgorsLab on GTC 2026; Solidigm uses "Tier G3.5") | None | verified |
| 32 | Vendor table (WEKA 1000× / 20×, DDN 55× / 27×, HPE 20× sponsored, NVIDIA 5×) | All labelled as vendor claims, and the caption says no-cache baselines | None | verified |
| 33 | Snowflake FY2026 product revenue US$4.47B (VERIFY) | Confirmed: US$4,472.3M product revenue and US$4,683.9M total, per the 10-K and the Q4 FY26 release | VERIFY removed; footnote 8 adds the release; staging line deleted | fixed |
| 33 | "In-memory replica carries ~US$63,000 of DRAM" next to "~US$66k versus ~US$4k" | The text did not explain the gap. The chart CSV includes ~$3k for an fp32 copy on SSD | Clarified | fixed |
| 33 | Networked array query "~15 ms" | 30 rounds × (0.1 + 0.5 ms) ≈ 18 ms | Now "~15–18 ms" | fixed |
| 33 | 4.1 TB; 264 B/vector of HNSW links; $14.5/GB DRAM ($927 / 64 GB); $0.75/GB SSD; $22k / $4.1k / $4.2k; 16×; DiskANN 3 ms and 1.2M reads/s; PQ 64×; Parquet 250×; 10 TB corpus → 20 TB of vectors | Recomputed against the CSV, all correct | None | verified |
| 33 | Databricks >US$7B run-rate at a US$190B valuation, August 2026 | Confirmed (round closed 2026-08-13, company-stated) | None | verified |
| 34 | NVCS Foundation 128 / Enterprise ~1,000 / NCP 10,000 (VERIFY on both) | Foundation 128 and the 10,000 ceiling are corroborated by the NVIDIA docs and blog summaries. The ~1,000 Enterprise figure is not | VERIFY narrowed to the Enterprise count | flagged |
| 34 | ICMS at CES, then "CMX" at GTC, presented as two things | ICMS was renamed CMX | Text states that CMX is the CES platform under a new name; tie to G3/G4 and Ch32 "G3.5" added | fixed |
| 34 | "Everpure's distinctive move is independent benchmarking ... VAST, WEKA and DDN did not" | "Independent" is generous, because MLPerf entries are vendor-run and peer-reviewed. The sentence also implied that rivals avoid benchmarks, but DDN and WEKA entered earlier rounds; only VAST has never entered | Reworded to "public, peer-reviewed", with an earlier-rounds note and a caveat that results are not a market ranking | fixed |
| 34 | 125/256 = 0.49 GB/s per GPU; 40/256 = 0.16; 4 GB/s ≈ 8× and ~1 TB/s per SU; WEKApod 720 GB/s against the 500 GB/s four-SU enhanced target | Recomputed, correct | None | verified |
| 34 | 12 STX storage partners, AIC/Supermicro/QCT, 8 early adopters, 2H 2026 | Confirmed against NVIDIA release coverage | None | verified |
| 34 | FlashBlade//EXA NVIDIA certification | Still none found. The March 2026 StorageReview piece describes NVCS validation as a "stepping stone" to the NCP level | Staging note updated | verified (absence) |

## Unresolved / disagreements

- **Ch11 (outside my scope)** still carries "[VERIFY: announcement date]" for Dynamo. That date is now confirmed as 2025-03-18 (NVIDIA Newsroom, cited as Ch32 footnote 19), and Ch11 can drop the marker.
- **SuperPOD storage tables** (Ch31 H100, Ch34 B200/B300): only the H100 per-SU read row (15/40/125) has been seen, and only in a snippet. The per-node 40/20 figures, the 62 GB/s write, the B200 standard/enhanced 40/20 and 125/62, and the B300 640/2,000 figures need a direct read of docs.nvidia.com, which is blocked in this session.
- **NVCS Enterprise-level GPU count** (~1,000) is unconfirmed.
- **Kokolis et al. 1.8 h projection at 16K GPUs** comes from secondary summaries. arXiv 2410.21680 should be checked.
- **Llama 3 §3.3 figures** are consistent with my reading of the paper, but arXiv was unreachable in this session.
- **PureKVA:** whether it actually reached GA in October 2026, and the test conditions behind the 20× TTFT claim, are both open.
- **Pinecone sale exploration** (Ch33): two searches found nothing. The VERIFY stays. If no primary report surfaces, consider softening to "faced reported strategic pressure" or deleting the clause.
- **VAST in NVIDIA's Series E** (Ch34): unresolved, VERIFY retained.
- **Common Crawl ">10 PB"** and the **S3 500T objects** figures (Ch30): still search-summary only, VERIFY retained.
