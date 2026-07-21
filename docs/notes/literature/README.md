# Literature: AI-assisted writing

Annotated bibliography for the *writing-quality* side of this repo — the evidence
base for optimizing toward clarity, ownership, diversity, and source fidelity
rather than detector outcomes. (The detector red-team empirics live separately in
`docs/notes/pangram-audit/`.)

- PDFs are gitignored (`pdfs/`); this file + `refs.bib` are the tracked index.
- Access checked **2026-07-21**.
- BibTeX keys match `refs.bib`.

**Status legend:** ✅ downloaded (OA) · 🚫 OA but bot-blocked, fetch in browser ·
🔒 paywalled, use institutional access · 📰 press → primary · 🔎 link to locate.

---

## Framing / co-writing

- ✅ **Hellström (2024)**, *AI and its consequences for the written word.*
  `hellstrom-2024` — Sets the terms for what "writing" means when a model is in the
  loop; useful framing for the charter's authorship stance.
  <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10794589/>
- ✅ **HaLLMark (CHI 2024)**, provenance/transparency in LLM writing. *(authors to verify)*
  `hallmark-2024` — Directly supports the "transparent revision" and provenance
  goals; a design precedent for showing where text came from.
  <https://arxiv.org/pdf/2311.13057>

## Homogenization / loss of diversity

- ✅ **Padmakumar & He (ICLR 2024)**, *Does Writing with Language Models Reduce
  Content Diversity?* `padmakumar-he-2024` — Core empirical anchor: co-writing
  compresses content diversity. Backbone of the anti-homogenization argument.
  <https://arxiv.org/abs/2309.05196>
- ✅ **Doshi & Hauser (Science Advances 2024)**, *Generative AI enhances individual
  creativity but reduces collective diversity.* `doshi-hauser-2024` — The
  individual-vs-collective split is the sharpest framing of the diversity cost.
  <https://www.science.org/doi/10.1126/sciadv.adn5290>
- ✅ **Moon, Green & Kushlev (2025)**, *Homogenizing effect of LLMs on creative
  diversity* (diversity growth-rate metric). `homogenizing-growthrate` — Offers a
  *metric* (diversity growth rate) for diversity loss worth borrowing. (Resolves the
  "Moon, Green & Kushlev" loose end below.)
  <https://www.sciencedirect.com/science/article/pii/S294988212500091X>
- ✅ **Wan & Kalman (2026)**, *Diverse AI personas can mitigate the homogenization
  effect in human-AI collaborative ideation.* `diverse-personas-2026` — The mitigation
  side: persona diversity as a lever.
  <https://www.sciencedirect.com/science/article/pii/S294988212600040X>
- 📰 **Google/university coalition study — press (NBC, 2026)**, "AI is changing the
  style and substance of human writing." `nbc-coalition-2026` — Press pointer;
  locate and cite the underlying study rather than the article.
  <https://www.nbcnews.com/tech/tech-news/ai-changing-style-substance-human-writing-study-finds-rcna263789>

## Population-scale lexical shift

- ✅ **Kobak, González-Márquez, Horvát & Lause**, *Delving into LLM-assisted writing in
  biomedical publications through excess vocabulary.* The "delve/underscore" fingerprint
  at population scale — primary evidence that LLM style leaks into the human corpus.
  **NB: `kobak-academic-2024` and `kobak-biomed-2025` are the *same paper*** — arXiv
  preprint (`kobak-academic-2024`, <https://arxiv.org/abs/2406.07016>) and its published
  Science Advances version (`kobak-biomed-2025`, <https://www.science.org/doi/10.1126/sciadv.adt3813>),
  not two separate studies. (My earlier "academic vs biomedical" split was an error carried
  from the source list.)
- ✅ **Bao, Zhao, Mao & Zhang (Scientometrics 2025)**, *Examining linguistic shifts in
  academic writing before and after the launch of ChatGPT: a study on preprint papers.*
  `arxiv-shifts-2025` — Same phenomenon on a preprint corpus; independent of Kobak.
  <https://link.springer.com/article/10.1007/s11192-025-05341-y>
- ✅ **Yakura et al. (2024)**, *LLM's Influence on Human Spoken Communication* (podcasts).
  `yakura-podcasts-2024` — Extends lexical drift from text to *speech* — the effect
  escapes the page. Strong "why this matters" citation.
  <https://arxiv.org/html/2409.01754>
- ✅ **PubMed medical-writing vocabulary study.** `pubmed-medical-vocab` — Another
  domain corpus confirming the shift; corroborating evidence for Kobak.
  <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12679996/>

## Latent persuasion / opinion effects

- ✅ **Jakesch et al. (CHI 2023)**, *Co-Writing with Opinionated Language Models
  Affects Users' Views.* `jakesch-2023` — Foundational: the assistant shifts the
  *writer's* opinion, not just the prose. Central to the persuasion-risk argument.
  <https://arxiv.org/pdf/2302.00560>
- ✅ **Williams-Ceci, Jakesch, Bhat, Kadoma, Zalmanson & Naaman (Science Advances 2026)**,
  *Biased AI writing assistants shift users' attitudes on societal issues.*
  `williams-ceci-2026` — The stronger, newer version of the Jakesch effect: two
  preregistered experiments (N=2582), attitudes shift toward the AI's stance, users
  don't notice, and common safeguards don't prevent it. DOI 10.1126/sciadv.adw5578 (OA).
  <https://www.science.org/doi/10.1126/sciadv.adw5578>

## Cognitive / authorship effects

- ✅ **Kosmyna et al. (MIT, 2025)**, *Your Brain on ChatGPT: Cognitive Debt.*
  `kosmyna-2025` — EEG evidence of reduced engagement/ownership under LLM assistance.
  The "cognitive debt" framing for the ownership goal. (Large PDF, ~37 MB.)
  <https://arxiv.org/abs/2506.08872>
- ✅ **Stanković et al. (2026)**, critique/commentary on the above. `stankovic-2026`
  — Read alongside Kosmyna to avoid over-claiming the cognitive-debt result.
  <https://arxiv.org/pdf/2601.00856>

## Stylometry / AI-vs-human detection

- ✅ **Georgiou (MDPI 2026)**, *What Distinguishes AI-Generated from Human Writing? A
  Rapid Review of the Literature.* `mdpi-prisma-2026` — Survey of stylometric markers;
  useful bridge to the detector tracks. (Key is legacy; it's a rapid review, not a
  formal PRISMA one.)
  <https://www.mdpi.com/2504-2289/10/2/55>
- ✅ **Khera et al. (Stroke)**, *Scientific Writing in the Era of Large Language
  Models: A Computational Analysis of AI- Versus Human-Created Content.* `stroke-stylometry`
  — Domain-specific stylometry.
  <https://www.ahajournals.org/doi/10.1161/STROKEAHA.125.051913>

## Graph-oriented structure & detection

Text-as-graph work. Recurring finding across every graph type mirrors the
homogenization literature: **human structure is more variable (wider spread in graph
metrics), AI structure more regular and concentrated.** Nearly all of it is framed as
*detection* (graph → classifier) rather than intrinsic analysis of how co-writing
reshapes structure — the story-network and discourse-motif papers come closest to the
latter. Open gap: nobody has yet graphed the *homogenization process itself* (an
author-level similarity/diffusion network tracking convergence over time).

- ✅ **Evaluating LLM Story Generation through Large-scale Network Analysis of Social
  Structures (2025).** `story-networks-2025` — Character co-occurrence networks over
  1,200+ human- and LLM-written stories; AI stories cluster in a narrow connectivity
  range, human ones spread out. Homogenization rendered as graph topology; closest to
  an intrinsic-structure analysis.
  <https://arxiv.org/html/2510.18932>
- ✅ **Threads of Subtlety: Detecting Machine-Generated Texts Through Discourse Motifs
  (2024).** `threads-subtlety-2024` — Hierarchical parse trees + recursive hypergraphs;
  human text shows more structural variability, and discourse features help even OOD /
  on paraphrases. Strongest linguistic graph paper here.
  <https://arxiv.org/pdf/2402.10586>
- ✅ **DependencyAI: Detecting AI-Generated Text through Dependency Parsing (2026).**
  `dependencyai-2026` — Interpretable, non-neural baseline using only dependency-relation
  labels; competitive across mono/multilingual, multi-generator settings.
  <https://arxiv.org/pdf/2602.15514>
- ✅ **Muñoz-Ortiz, Gómez-Rodríguez & Vilares (2024)**, dependency/constituent structure
  of human vs. LLM text. `munoz-ortiz-2024` — Fuller treatment: human text has distinct
  dependency/constituent-type use, shorter constituents, more optimized dependency
  distances; LLM text tends to deeper/longer dependency structures.
  <https://arxiv.org/pdf/2308.09067>
- ✅ **Wang et al. (2025)**, *The fluency-based semantic network of LLMs differs from
  humans.* `fluency-semantic-net-2024` — Semantic-association networks compared across
  model generations and vs. humans. (OA; *Computers in Human Behavior: Artificial Humans*.)
  <https://www.sciencedirect.com/science/article/pii/S294988212400063X>
- ✅ **Xiang et al. (CMC 2026)**, *AI-Generated Text Detection: A Comprehensive Review
  of Active and Passive Approaches.* `detection-review-2026` — Best entry point for
  where graph/discourse features sit relative to lexical and probabilistic ones.
  DOI 10.32604/cmc.2025.073347.
  <https://www.techscience.com/cmc/online/detail/10.32604/cmc.2025.073347>

## Bias / equity

- ✅ **Unraveling Downstream Gender Bias from LLMs in Educational Writing.** `gender-bias-2023`
  — Bias propagation through AI-assisted writing; relevant to the equity dimension
  of "do no harm" in revision.
  <https://arxiv.org/pdf/2311.03311>

---

## Referenced but not yet linked (🔎 to locate)

Findable by title on arXiv / ACM DL; not yet fetched (out of the OA-only pass):

- **Juzek & Ward (COLING 2025)**, *Why does ChatGPT "Delve" so much?* — the canonical
  "delve" study; strong companion to Kobak.
- **Lee et al. (CHI 2024)**, design space of human-AI co-writing.
- ~~**Moon, Green & Kushlev**~~ — resolved: this is `homogenizing-growthrate` above
  (their diversity growth-rate paper).
- **Draxler et al.**, the "AI ghostwriter effect" (ownership without attribution).

Say the word and I'll resolve exact URLs and pull the OA ones in a follow-up pass.
