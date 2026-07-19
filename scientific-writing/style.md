# Style: voice, sentences, layout

Sentence-scale rules encoding the user's voice. Apply from the first draft, not as a cleanup pass. SKILL.md's reader model and structure rules are assumed.

## Voice

- **Describe, do not convince.** Report what we did and observed; state the finding, then its cause. No persuasive framing: "What sets X apart is...", "the key is...", "Importantly,", "Notably,", rhetorical questions, setup-then-payoff contrasts ("not just X, but Y").
- **First person "We".** "We find", "we attribute", "we use". Not "This follows", "Here we have", "It can be seen that".
- **Formal, not bloggy.** No conversational connectives, no hype adjectives ("powerful", "remarkable", "seamless"), no buzzword repetition across nearby sentences.
- **Cut emphasis filler, do not soften it.** Delete outright: "genuine(ly)", "truly", "actual(ly)", "really", "very", "highly", "key", "crucial", "critical", "essential", "fundamental", "significant(ly)", "clearly", "simply". "genuinely novel territory" -> "novel territory". Keep one only when it draws a load-bearing contrast the sentence loses without it, once per passage. On three nearby nouns it is overused whatever the meaning.
- **NSF/scientific register, not product voice.** Prose reports methods, measurements, releases, and contingencies. It does not pitch a platform, tour users through a map, or read like release notes, an SRE runbook, or a startup roadmap. Prefer positive facts over slogan contrasts. Banned shapes and their replacements:
  - **Product verbs**: "ships/shipped/shipping", "turns X into action", "puts X on the map", "unlocks", "empowers" -> "released as", "implements", what the thing does ("the agent pathfinds and decodes").
  - **Product packaging**: "tool suite", "software suite", "toolkit", "platform", "software ecosystem", "computing stack" as branding. Name the artifact once, then "software" / "tools" / the specific component. List tools by role ("We use X for Y"), not as an ecosystem.
  - **SE/ops jargon**: "backend", "frontend", "API costs", "production pipeline", "downstream component", "degrade gracefully", "critical path", "FTE", "feature engineering", "unit-test coverage" as a success headline. Keep genuine technical nouns (embedding, adapter, backbone, protocol names, Snakemake pipelines in a data-management plan).
  - **Architecture dialect in education/contingency prose**: "base layer", "stretch layer", "demotes to", "re-gate", "suggestion arm is dropped", "building end" / "navigating end", "needs no Git knowledge". State the contingency plainly ("if validation fails, classroom mode shows the descriptive map only").
  - **Marketing metaphor**: "travelers on the map" tours, "navigation layer to counteract convergence", "countermeasure to...", "technology-transfer path to industry", "channels that temper adoption risk", "feasible now", "scarce step", "humans in control" as slogan. State the concrete fact ("the human keeps final selection", "the pilot assesses maps against industrial search needs").
  - **Soft app KPIs**: "users reporting enhanced understanding", "redesign the interface" -> "course participants report...", "revise materials or interaction design".
  - **Capability padding**: sentence-opening "This geometry enables...", "ensuring robust integration", "designed to", "aims X at", "all served by the same underlying method" as platform restatement. State the mechanism or measurement.
  - **Tagline stacks**: one load-bearing contrast (e.g. movement records rather than paper text) may appear once per document as the definition. Do not restate the same "instead of retrieved documents" pivot across summary, merit, impacts, and body; one strongest sentence per claim per section.
  - **Empty adverbs**: "already", "actually", "directly", "in particular" usually delete with no loss. Keep only when they carry a real time or scope contrast.

## Attention budget

Every added fact, qualifier, or contrast splits reader attention at the cost of its neighbors.

- **Prioritize, don't append.** Explain load-bearing parts in depth; mention the rest in a clause.
- **Mentioning X and Y both is not free.** A paragraph explaining two coequal points leaves less of each; cut the secondary point or demote it to a subordinate clause.
- **Preliminary numbers are often not load-bearing.** Keep a number only when the reader needs it to judge the claim; else state the qualitative result.
- **Trim before adding.** Shorten or remove an existing point before writing a new one.

## Sentences

- **Old before new.** Open with material linking to the previous sentence; end on the new information (stress position).
- **No colons or semicolons** in prose. Break into separate sentences.
- **Split comma-coordinator chains; allow one when splitting fragments.** Default: avoid "..., but its ..." by ending the sentence and starting a new one. When two facts are tightly linked and splitting produces two short sentences the reader must reconnect, a single ", and" / ", but" is the better choice. Never chain three clauses.
- **Never a causal "..., so ...".** End the sentence and carry the cause with "Therefore," or recast cause-first with "because". "weight barely predicts content, so the channel loses proportionality" -> "weight barely predicts content. The channel therefore loses proportionality." The so-ban overrides the coordinator leniency.
- **Split nested clauses by default.** Break "which ..." / "that does Y" into separate declaratives, or merge with a compound predicate or appositive. Keep a single light relative clause only when compound predicates and appositives genuinely fail — at most once or twice per paragraph, never as a flow default.
- **Avoid "X, not Y" / "rather than" constructions.** They read as a rhetorical tic. Default to the one fact that matters, or two plain sentences. Reserve for a genuine load-bearing contrast, at most once per section. "is not incremental accuracy but mechanism" -> "is mechanism." Vary the rare genuine case with "instead (of)" or a separate sentence.
- **No em-dash flourishes** ("---not just X---but Y"). Parentheticals and plain commas.
- **Flow first, coordinators last.** Do not overcorrect into staccato fragments. Reach first for varied sentence length, sentence-initial transitions ("therefore", "instead", "by contrast"), prepositional phrases, and compound predicates (one subject, two verbs, no comma: "A token embedding only summarizes a document and cannot generate from it" — always encouraged). Aim for medium sentences.
- **The reader-stop test.** Short is fine; disconnected is not. Before adding a coordinator, try: demote a short sentence into an appositive or participial phrase on its neighbor ("...the relevant information, hidden from cosine similarity"); bridge a turn with a sentence-initial connector or purpose phrase ("Even so,", "To surface it, we train...").
- **Return from an aside.** When a sentence resumes a thread an aside interrupted, insert a short bridge naming the shared term. "Combining two adapters blends their generative processes. [aside] Prior work merges fine-tuned weights..." stalls; fix with "Adapters are weights. Prior work already merges fine-tuned weights...".

## Source layout

- **One sentence per line.** Line break after each sentence-ending period; no hard-wrapping a sentence across lines, no two sentences on one line. Blank line between paragraphs. Keeps diffs, line-based editing, and the critique.md skim extraction mechanical. Source layout only; rendering unchanged.

## Reference and precision

- **Anchor every demonstrative.** Never open with bare "This"/"That"/"These"; name the referent ("This smooth structure"). Applies mid-sentence after semicolons or dashes, and to reports and summaries to the user, not only paper prose.
- **Parenthetical evidence.** Cite numbers and sections inline: "(pairwise cosine similarity is 0.96 versus 0.44 ...)", "(\secref{semantics})". "suggesting that ..." is an acceptable hedge for an inference from a measurement.
- **Cut redundancy within a passage.** Each sentence adds a fact, not a restatement. Distinct from the deliberate cross-scale repetition of the core claim at entry points, which is structure.
- **Few apostrophes.** Recast possessives with "of" or an attributive noun: "the surface wording of the source passages", "one adapter per document". A stray possessive is fine; do not stack them.
- **Direct English.** Say plainly what a method does. No back-pointing devices ("supply that model", "this is where X shines"); write "train such a decoder a posteriori".
- **Prefer Latinate precision where the user uses it**: "a posteriori" over "after the fact".

## Self-check list

Before showing prose, check every touched sentence: colons/semicolons (never), causal "..., so ..." (never), comma-coordinators beyond the earned one, nested clauses (one or two per paragraph max), bare demonstratives, "X, not Y"/"rather than"/"instead of" count (near zero per section; one load-bearing definition per document), emphasis filler (delete, do not soften), product/SE voice (ships, suite, backend, layer dialect, marketing metaphor, enables-openers — rewrite to mechanism or measurement), apostrophe density, repeated buzzwords and taglines, one sentence per line, and the reader-stop test.

## Quick contrast

Blog-like (avoid):
> What sets doc2lora apart is its smooth geometry: embeddings interpolate, and averaging papers moves toward the shared concept, so specific ideas sit around it. ICAE decodes points, but its embeddings fall in a narrow cone.

In style (use):
> Doc2LoRA embeddings form a smooth semantic space. Averaging a set of papers moves the embedding toward the concept those papers share. ICAE decodes constructed points. Its embeddings occupy a narrow cone. Averages over them remain as specific as a single paper.

Product voice (avoid):
> The tool suite ships as an MCP server. An AI agent turns the landscape into action, putting travelers on the map and ensuring robust integration with educational workflows. The base layer ships regardless; on failure the deployment demotes and the suggestion arm is dropped.

NSF descriptive voice (use):
> CoAtlasTool is released as open-source software and exposes pathfinding and decoding through an MCP server. The agent traces a path from the researcher's recent papers toward a knowledge hole, decodes waypoints into guiding questions, and leaves final selection to the human. If the Year-1 curricular validation fails, classroom mode shows the descriptive map only and withholds ordered next-concept suggestions.

Buried point, loses the skimmer (avoid):
> Prior efforts to map science have relied on citation networks, which take years to accumulate. Recent work has explored text embeddings as an alternative. Building on both lines, our preliminary analysis suggests that mobility patterns alone recover the field structure of science.

Point first (use):
> Mobility patterns alone recover the field structure of science. Citation networks recover the same structure but take years to accumulate, and our preliminary analysis shows the mobility map matches them at a fraction of the delay.
