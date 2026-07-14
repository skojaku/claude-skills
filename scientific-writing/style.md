# Style: voice, sentences, and layout

Sentence-scale rules encoding the user's voice. Apply from the first draft, not as a cleanup pass. The reader model and document-structure rules in SKILL.md are assumed.

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
- **Never join clauses with a causal "..., so ...".** A comma followed by "so" reads conversational and is one of the most common AI tells. End the sentence and carry the cause with a sentence-initial "Therefore,", or recast it cause-first with "because". Example: "weight barely predicts content, so the channel loses proportionality" becomes "weight barely predicts content. The channel therefore loses proportionality." or "Because weight barely predicts content, the channel loses proportionality." The so-ban overrides the "allow one coordinator" leniency above: "so" is never the coordinator you keep.
- **Prefer to split nested clauses, but allow one for flow.** The default is to break relative and subordinate clauses ("which ...", "in which ...", "X that does Y") into separate declarative sentences: "A is an adapter. The adapter drives generation." When that split leaves two short, choppy sentences, a single light relative clause restores flow: "A is an adapter that drives generation." First try compound predicates and appositives (below). Reach for the relative clause when those do not merge the sentences cleanly.
- **Avoid "X, not Y" / "X rather than Y" contrast constructions.** These pivots read as a rhetorical tic, not a reported fact, and the sentence usually works without the pivot. Default to stating the one fact that matters, or splitting the comparison into two plain sentences, instead of building the sentence around a not/rather-than contrast. Reserve the construction for a genuine, load-bearing contrast the reader cannot get any other way, at most once across a whole section, and cut it everywhere else. Example: "produce points, not adapters" -> "produce points. A point has no adapter to decode, and an extrapolated position therefore never turns into a readable topic." Example: "is not incremental accuracy but mechanism" -> "is mechanism." Vary the rare genuine contrast with "instead", "instead of", or a separate sentence, not with a repeated "rather than".
- **No em-dash flourishes** (`---not just X---but Y`). Use parentheticals and plain commas.
- **Flow first, coordinators last.** The split-by-default rules above remove the usual sources of flow, so do not overcorrect into staccato fragments. Reach first for the cost-free devices: varied sentence length, sentence-initial transitions ("therefore", "instead", "by contrast"), prepositional phrases, and **compound predicates** (one subject, two verbs, no comma: "A token embedding only summarizes a document and cannot generate from it"). A compound predicate is not a comma-coordinator and is always encouraged. When those are not enough to connect two tightly linked facts, a single coordinator or relative clause is the right tool (see the two "prefer to split" rules). Aim for medium sentences, not a list of four-word ones.
- **The reader-stop test.** A run of short sentences fails when the reader has to stop at each period and work out how it connects to the next. Short is fine; disconnected is not. Try these before adding a coordinator or relative clause:
  - **Demote a standalone short sentence into an appositive or participial phrase** on its neighbor. "The information is present. Cosine similarity does not expose it." -> "...the relevant information, hidden from cosine similarity and naive Euclidean distance." The appositive is a phrase, not a comma-coordinator.
  - **Bridge a turn with a sentence-initial connector**, not a mid-sentence one. Use "Even so,", "To surface it,", "In that space," to point back at the prior sentence before adding the new fact. A purpose- or reference-phrase opener ("To surface it, we train...") ties the sentence to what came before without a relative clause.
- **Return from an aside.** When a sentence resumes a thread that an intervening aside interrupted, the reader stalls because the link is two sentences back, not one. Trace each sentence to the one it actually depends on. If that is not the immediately preceding sentence, insert a short bridge that re-establishes the link. Example: "Combining two adapters blends their generative processes. [aside: a token embedding cannot generate, so interpolating token embeddings yields nothing.] Prior work merges fine-tuned weights..." stalls, because "Prior work" reconnects to the adapter thread across the aside. Fix with a one-clause bridge: "Adapters are weights. Prior work already merges fine-tuned weights...". The bridge names the shared term that lets the reader cross back.

## Source layout

- **One sentence per line.** In the source file, every sentence sits on its own line, with a line break after each sentence-ending period. Do not hard-wrap a single sentence across several lines, and do not pack two sentences onto one line. Line-per-sentence keeps vim motions, line-based editing, and git diffs scoped to one sentence, and makes the skim extraction in critique.md (first line after each blank line) mechanical. Separate paragraphs with a single blank line. One sentence per line is a source-layout rule only and does not change the rendered output.

## Reference and precision

- **Anchor every demonstrative.** Never open a sentence with a bare "This", "That", or "These". Name the referent: "This smooth structure", "this fusion ability". The anchor rule also covers mid-sentence demonstratives after a semicolon or dash, and it covers everything written under this skill (reports, briefs, summaries to the user), not only paper prose. A bare demonstrative forces the reader to stop and hunt for the referent, and a reader who guesses wrong is lost without knowing it.
- **Parenthetical evidence.** Cite numbers and sections inline in parentheses, in the user's own pattern: "(pairwise cosine similarity is 0.96 versus 0.44 ...)", "(\secref{semantics})". "suggesting that ..." is an acceptable hedge for an inference from a measurement.
- **Cut redundancy within a passage.** No doubled words ("new effective ones" -> "new and workable ones"). Each sentence should add a fact, not restate the previous one. Within-passage redundancy is distinct from the deliberate cross-scale repetition of the core claim at entry points, which is structure.
- **Few apostrophes (the user dislikes them).** Recast possessive 's with an "of" phrase or an attributive noun: "the surface wording of the source passages" not "the source passages' wording"; "one adapter per document" not "each document's adapter"; "the content of a document" not "a document's content". A stray possessive is fine, but do not stack several in a passage.
- **Direct English, no rhetorical filler.** Say plainly what a method does. Avoid back-pointing devices like "supply that model" or "this is where X shines"; write "train such a decoder a posteriori".
- **Prefer Latinate precision where the user uses it:** "a posteriori" over "after the fact".

## Self-check list

Before showing prose, check every touched sentence against: colons/semicolons (never), causal "..., so ..." (never), comma-coordinators and nested clauses beyond the earned few, bare demonstratives, "X, not Y" / "rather than" contrast count (near zero per section), apostrophe density, rhetorical filler, persuasive framing, repeated buzzwords, one sentence per source line, and the reader-stop test.

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
