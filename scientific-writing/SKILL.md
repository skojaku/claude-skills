---
name: scientific-writing
description: Draft and revise multi-page scientific documents (papers, grant proposals) in the user's style. Structures documents for busy readers who skim, using a skeleton-first drafting loop with skim-reader review passes. Also enforces the user's sentence-level voice (terse first-person description over persuasive, blog-like phrasing).
---

# Scientific Writing for Busy Readers

Write multi-page documents (papers, proposals) for a reader who will not read them in depth, and revise them through the drafting–review loop below. The document-scale rules follow from the reader model. The sentence-scale rules encode the user's voice. Apply both from the first draft.

## The reader model

Every rule in this skill derives from how a busy expert actually processes a long document. Hold this model while drafting and while reviewing.

1. **Readers skim before, or instead of, reading.** A reviewer with a stack of proposals scans headings, first sentences, figures, and bold text to orient, and only descends into full paragraphs where the skim raised interest or doubt (Rogers & Lasky-Fink, *Writing for Busy Readers*).
2. **Skimming is satisficing.** Eye-tracking shows skimmers read the opening of each unit until the rate of information gain drops, then jump to the next unit (Duggan & Payne, CHI 2011). The first sentence of a paragraph is often the only sentence read. Whatever it says is what that paragraph said.
3. **Readers remember gist, not text.** Comprehension compresses the document into a macrostructure of a few propositions. Details that do not attach to one of those retained propositions are deleted (Kintsch & van Dijk). A reader leaves a 15-page document holding perhaps five sentences. The writer's job is to choose those five sentences, not to hope.
4. **Working memory holds one thread.** A section that develops one idea gets encoded. A section that braids three ideas gets a blur. Organize each section around one unifying thread and subordinate everything else to it.
5. **Within a sentence, readers assign meaning by position.** The opening (topic position) is read as context linking back to what came before. The end (stress position) is read as the news to emphasize (Gopen & Swan, *The Science of Scientific Writing*). Old information first, new information last.
6. **Long documents are read out of order.** Reviewers jump to the section their concern lives in. Each section must survive being someone's entry point.

## Document structure

- **The skeleton must stand alone.** Headings plus the first sentence of every paragraph, read in order with the figures, must deliver the complete argument. This is the document the skimming reader actually reads. Everything below the first sentence is elaboration for the reader who descends.
- **Headings carry claims where the format allows.** "Mobility embeddings recover field structure without citation data" navigates and asserts. "Preliminary results" only navigates. In formats with fixed heading conventions, push the claim into a bold lead-in or the first sentence instead.
- **Context, content, conclusion at every scale** (Mensh & Kording, *Ten Simple Rules for Structuring Papers*). The document opens with why and closes with what follows. Each section opens by placing itself in the argument and closes on what the reader should carry forward. Each paragraph opens with its point.
- **One point per paragraph, point first.** The first sentence states the point in plain declarative form. The rest gives evidence and mechanism. If a paragraph needs two point sentences, it is two paragraphs. Never open a paragraph with throat-clearing context that defers the point to sentence three, because the satisficing reader is gone by then.
- **Repeat the core claim at every entry point.** The summary, the introduction, and the section where the work lives each state the central claim, in words adapted to their scale. To a linear reader this is structure, not repetition. To a skimming reader it is the only insurance that the claim is seen at all.
- **Re-anchor at section boundaries.** Open each section by restating, in one clause, the referent it depends on ("The mobility embedding from Thrust 1..."), because the reader may arrive here directly. Never open a section with a bare demonstrative pointing across the section break.
- **Front-load by primacy.** Within any unit (document, section, paragraph, list), order items by importance to the argument, not by chronology or by the order you did the work.
- **Figures are read independently.** Skimmers read figures and captions as a parallel document. Each caption states what the figure shows and what it means for the argument, without requiring the body text. Keep per-cell annotations neutral and descriptive, not qualitative verdicts.

## The drafting–review loop

Draft and revise in explicit passes. Do not draft linearly start-to-finish and then polish. For a multi-section document, run the loop per section, then once over the whole document.

**Phase 0 — Takeaways.** Before writing, list the 3–5 sentences the busy reader must still hold after putting the document down, plus one sentence per section. Write these down (a scratch file is fine). These are the acceptance criteria for every later review pass. If the user has stated the takeaways, use theirs; otherwise propose the list and confirm before drafting at length.

**Phase 1 — Skeleton draft.** Write only the headings and the first sentence of every planned paragraph. Read this skeleton against the takeaway list. Fix ordering, missing steps, and buried claims here, where a change costs one line, not after paragraphs are built on top. Do not proceed until the skeleton alone tells the story.

**Phase 2 — Expand.** Grow each skeleton sentence into its paragraph, point first, in the voice defined below. Expansion must not demote the skeleton sentence from first position.

**Phase 3 — Skim review.** Reconstruct what the satisficing reader sees, and check it against the takeaways.
- Mechanically extract the skim view: headings, the first sentence of each paragraph (with one-sentence-per-line source layout this is the first line after each blank line or heading), figure captions, and bold text.
- Give ONLY this extract to a fresh subagent (Agent tool, general-purpose, no other context) with a prompt like: "You are a busy reviewer who skimmed this document. State in your own words: what is being proposed, why it matters, what the evidence is, and what you remain unconvinced by. Do not guess charitably." The drafter cannot simulate naivety about its own draft; a context-free agent can.
- Compare the subagent's readback to the Phase 0 takeaways. Every takeaway the readback misses or distorts marks a paragraph whose first sentence is not doing its job, a missing entry-point repetition, or a buried section. Fix at the skeleton level, not by adding text.

**Phase 4 — Deep review.** For the reader who does descend, check sentence-level style against the self-check list at the end of the Sentences section: colons/semicolons, causal "..., so ...", comma-coordinators and nested clauses beyond the earned few, bare demonstratives, "X, not Y" contrast count, apostrophe density, rhetorical filler, persuasive framing, repeated buzzwords, one sentence per source line, reader-stop test.

**Phase 5 — Attention budget.** Per section, name its one thread in a sentence. Anything in the section that does not serve that thread gets cut, demoted to a clause, or moved. Cut before adding. Drop preliminary numbers that are not load-bearing.

**Loop.** Repeat Phases 3–5 until the skim readback returns the intended takeaways without distortion and the deep check is clean. Two rounds are typical; one is suspicious. Then, per the user's global instruction, `git add`, commit, and push, ending commit messages with the project's `Co-Authored-By` trailer.

## Voice

- **Describe, do not convince.** Report what we did and what we observed. State the finding, then its cause. Avoid persuasive framing: "What sets X apart is...", "the key is...", "Importantly,", "Notably,", rhetorical questions, and setup-then-payoff contrasts ("not just X, but Y").
- **First person "We".** "We find", "We attribute", "We use", "We instead use". Not impersonal "This follows", "Here we have", "It can be seen that".
- **Formal, not bloggy.** This is a scientific paper. No conversational connectives, no hype adjectives ("powerful", "remarkable", "seamless"), no repeated buzzwords across nearby sentences.

## Attention budget

Every additional fact, qualifier, or contrast splits the reader's attention across more things, at the cost of how well any one of them lands. Before adding a sentence, weigh whether it earns the attention it costs its neighbors.

- **Prioritize, don't append.** Decide up front which components of a passage need full explanation with intuition and examples, and which need only a bare mention or a single clause. Do not give every detail equal weight by default; explain the load-bearing parts in depth and the rest lightly.
- **Mentioning X and Y both is not free.** A paragraph that explains X and Y as coequal points leaves the reader with less of each than a paragraph that commits to explaining one well. When a passage is doing this, cut the secondary point or demote it to a subordinate clause instead of listing it alongside the primary one.
- **Preliminary numbers are often not load-bearing.** Correlation coefficients, exact percentages, and intermediate statistics from preliminary work often cost more attention than they return when the qualitative claim alone would convince. Keep a number only when the reader needs it to judge the claim; otherwise state the qualitative result and move on.
- **Trim before adding.** When a paragraph risks covering too much, shorten or remove an existing point before writing a new one, instead of appending the new point on top.

## Sentences

- **Old before new.** Open a sentence with material that links back to the previous sentence, and end it on the new information the reader should carry forward (the stress position). A sentence that buries its news mid-sentence and trails off on old material reads flat even when grammatically clean.
- **No colons or semicolons** in prose. Break into separate sentences instead.
- **Prefer to split comma-coordinator chains, but allow one when splitting fragments.** The default is to avoid "..., but its ...", "..., and X becomes ..." by ending the sentence and starting a new one, carrying cause with "therefore" between sentences. Splitting is not free. When two facts are tightly linked and splitting them produces two short sentences the reader has to reconnect, a single ", and" / ", but" is the better choice. Use it deliberately, not by habit, and never chain three clauses.
- **Never join clauses with a causal "..., so ...".** A comma followed by "so" reads conversational and is one of the most common AI tells. End the sentence and carry the cause with a sentence-initial "Therefore,", or recast it cause-first with "because". Example: "weight barely predicts content, so the channel loses proportionality" becomes "weight barely predicts content. The channel therefore loses proportionality." or "Because weight barely predicts content, the channel loses proportionality." This overrides the "allow one coordinator" leniency above: "so" is never the coordinator you keep.
- **Prefer to split nested clauses, but allow one for flow.** The default is to break relative and subordinate clauses ("which ...", "in which ...", "X that does Y") into separate declarative sentences: "A is an adapter. The adapter drives generation." When that split leaves two short, choppy sentences, a single light relative clause restores flow: "A is an adapter that drives generation." First try compound predicates and appositives (below). Reach for the relative clause when those do not merge the sentences cleanly.
- **Avoid "X, not Y" / "X rather than Y" contrast constructions.** These read as a rhetorical tic, not a reported fact, and the sentence usually works without the pivot. Default to stating the one fact that matters, or splitting the comparison into two plain sentences, instead of building the sentence around a not/rather-than contrast. Reserve the construction for a genuine, load-bearing contrast the reader cannot get any other way, at most once across a whole section, and cut it everywhere else. Example: "produce points, not adapters" -> "produce points. A point has no adapter to decode, and an extrapolated position therefore never turns into a readable topic." Example: "is not incremental accuracy but mechanism" -> "is mechanism." Vary the rare genuine contrast with "instead", "instead of", or a separate sentence, not with a repeated "rather than".
- **No em-dash flourishes** (`---not just X---but Y`). Use parentheticals and plain commas.
- **Flow first, coordinators last.** The split-by-default rules above remove the usual sources of flow, so do not overcorrect into staccato fragments. Reach first for the cost-free devices: varied sentence length, sentence-initial transitions ("therefore", "instead", "by contrast"), prepositional phrases, and **compound predicates** (one subject, two verbs, no comma: "A token embedding only summarizes a document and cannot generate from it"). A compound predicate is not a comma-coordinator and is always encouraged. When those are not enough to connect two tightly linked facts, a single coordinator or relative clause is the right tool (see the two "prefer to split" rules). Aim for medium sentences, not a list of four-word ones.
- **The reader-stop test.** A run of short sentences fails when the reader has to stop at each period and work out how it connects to the next. Short is fine; disconnected is not. Try these before adding a coordinator or relative clause:
  - **Demote a standalone short sentence into an appositive or participial phrase** on its neighbor. "The information is present. Cosine similarity does not expose it." -> "...the relevant information, hidden from cosine similarity and naive Euclidean distance." This is a phrase, not a comma-coordinator.
  - **Bridge a turn with a sentence-initial connector**, not a mid-sentence one. Use "Even so,", "To surface it,", "In that space," to point back at the prior sentence before adding the new fact. A purpose- or reference-phrase opener ("To surface it, we train...") ties the sentence to what came before without a relative clause.
- **Return from an aside.** When a sentence resumes a thread that an intervening aside interrupted, the reader stalls because the link is two sentences back, not one. Trace each sentence to the one it actually depends on. If that is not the immediately preceding sentence, insert a short bridge that re-establishes the link. Example: "Combining two adapters blends their generative processes. [aside: a token embedding cannot generate, so interpolating token embeddings yields nothing.] Prior work merges fine-tuned weights..." stalls, because "Prior work" reconnects to the adapter thread across the aside. Fix with a one-clause bridge: "Adapters are weights. Prior work already merges fine-tuned weights...". The bridge names the shared term that lets the reader cross back.

## Source layout

- **One sentence per line.** In the source file, every sentence sits on its own line, with a line break after each sentence-ending period. Do not hard-wrap a single sentence across several lines, and do not pack two sentences onto one line. Line-per-sentence keeps vim motions, line-based editing, and git diffs scoped to one sentence, and makes the Phase 3 skim extraction (first line after each blank line) mechanical. Separate paragraphs with a single blank line. This is a source-layout rule only and does not change the rendered output.

## Reference and precision

- **Anchor every demonstrative.** Never open a sentence with a bare "This", "That", or "This difference". Name the referent: "This smooth structure", "this fusion ability".
- **Parenthetical evidence.** Cite numbers and sections inline in parentheses, in the user's own pattern: "(pairwise cosine similarity is 0.96 versus 0.44 ...)", "(\secref{semantics})". "suggesting that ..." is an acceptable hedge for an inference from a measurement.
- **Cut redundancy within a passage.** No doubled words ("new effective ones" -> "new and workable ones"). Each sentence should add a fact, not restate the previous one. This is distinct from the deliberate cross-scale repetition of the core claim at entry points, which is structure.
- **Few apostrophes (the user dislikes them).** Recast possessive 's with an "of" phrase or an attributive noun: "the surface wording of the source passages" not "the source passages' wording"; "one adapter per document" not "each document's adapter"; "the content of a document" not "a document's content". A stray possessive is fine, but do not stack several in a passage.
- **Direct English, no rhetorical filler.** Say plainly what a method does. Avoid back-pointing devices like "supply that model" or "this is where X shines"; write "train such a decoder a posteriori".
- **Prefer Latinate precision where the user uses it:** "a posteriori" over "after the fact".

## Quick contrast

Blog-like (avoid):
> What sets doc2lora apart is its smooth geometry: embeddings interpolate, and averaging papers moves toward the shared concept, so specific ideas sit around it. ICAE decodes points, but its embeddings fall in a narrow cone.

In style (use):
> Doc2LoRA embeddings form a smooth semantic space. Averaging a set of papers moves the embedding toward the concept those papers share. ICAE decodes constructed points. Its embeddings occupy a narrow cone. Averages over them remain as specific as a single paper.

Fragmented, fails the reader-stop test (avoid):
> The relevant information is present in the embedding. Cosine similarity and naive Euclidean distance do not expose it. A learnable bijective transform reshapes the geometry to surface it. We train this transform on a small set of citation pairs.

Connected, same bans respected (use):
> Even so, its embedding still carries the relevant information, hidden from cosine similarity and naive Euclidean distance. To surface it, we train a learnable bijective transform on a small set of citation pairs. This transform reshapes the geometry and brings doc2lora at least comparable with dedicated encoders.

Buried point, loses the skimmer (avoid):
> Prior efforts to map science have relied on citation networks, which take years to accumulate. Recent work has explored text embeddings as an alternative. Building on both lines, our preliminary analysis suggests that mobility patterns alone recover the field structure of science.

Point first, skimmer keeps it (use):
> Mobility patterns alone recover the field structure of science. Citation networks recover the same structure but take years to accumulate, and our preliminary analysis shows the mobility map matches them at a fraction of the delay.
