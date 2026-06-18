---
name: scientific-writing
description: Edit or draft scientific-paper prose in the user's style. Invoke whenever writing or revising academic paper text (abstract, intro, results, discussion, related work, captions), especially LaTeX manuscripts. Enforces terse first-person description over persuasive, blog-like phrasing.
---

# Scientific Writing Style

Write and revise paper prose the way the user does: terse, descriptive, first-person, formal. The user repeatedly corrects AI-sounding drafts toward this style. Apply these rules from the first draft, not as a cleanup pass.

## Voice

- **Describe, do not convince.** Report what we did and what we observed. State the finding, then its cause. Avoid persuasive framing: "What sets X apart is...", "the key is...", "Importantly,", "Notably,", rhetorical questions, and setup-then-payoff contrasts ("not just X, but Y").
- **First person "We".** "We find", "We attribute", "We use", "We instead use". Not impersonal "This follows", "Here we have", "It can be seen that".
- **Formal, not bloggy.** This is a scientific paper. No conversational connectives, no hype adjectives ("powerful", "remarkable", "seamless"), no repeated buzzwords across nearby sentences.

## Sentences

- **No colons or semicolons** in prose. Break into separate sentences instead.
- **No comma-coordinator chains.** Avoid "..., but its ...", "..., so ...", "..., and X becomes ...". End the sentence and start a new one. Carry cause with "therefore" *between* sentences, never with ", so" inside one.
- **No nested clauses.** Split relative and subordinate clauses ("which ...", "in which ...", "X that does Y") into separate short declarative sentences. Prefer "A is an adapter. The adapter drives generation." over "A is an adapter that drives generation."
- **Sparse "rather than".** At most once per passage. Carry contrasts with a separate sentence or with "instead".
- **No em-dash flourishes** (`---not just X---but Y`). Use parentheticals and plain commas.
- **Flow without coordination.** The bans above remove the usual sources of flow, so do not overcorrect into staccato fragments. Carry flow with varied sentence length, sentence-initial transitions ("therefore", "instead", "by contrast"), prepositional phrases, and **compound predicates** (one subject, two verbs, no comma: "A token embedding only summarizes a document and cannot generate from it"). A compound predicate is not a comma-coordinator and is encouraged. Aim for medium sentences, not a list of four-word ones.
- **The reader-stop test.** A run of short sentences fails when the reader has to stop at each period and work out how it connects to the next. Short is fine; disconnected is not. Two fixes that keep the bans intact:
  - **Demote a standalone short sentence into an appositive or participial phrase** on its neighbor. "The information is present. Cosine similarity does not expose it." -> "...the relevant information, hidden from cosine similarity and naive Euclidean distance." This is a phrase, not a comma-coordinator.
  - **Bridge a turn with a sentence-initial connector**, not a mid-sentence one. Use "Even so,", "To surface it,", "In that space," to point back at the prior sentence before adding the new fact. A purpose- or reference-phrase opener ("To surface it, we train...") ties the sentence to what came before without a relative clause.

## Reference and precision

- **Anchor every demonstrative.** Never open a sentence with a bare "This", "That", or "This difference". Name the referent: "This smooth structure", "this fusion ability".
- **Parenthetical evidence.** Cite numbers and sections inline in parentheses, in the user's own pattern: "(pairwise cosine similarity is 0.96 versus 0.44 ...)", "(\secref{semantics})". "suggesting that ..." is an acceptable hedge for an inference from a measurement.
- **Cut redundancy.** No doubled words ("new effective ones" -> "new and workable ones"). Each sentence should add a fact, not restate the previous one.

## Workflow

1. Draft in this voice from the start. Do not produce a polished-AI version and then strip it.
2. Before showing prose, self-check against the list: colons/semicolons, comma-coordinators, nested clauses, bare demonstratives, "rather than" count, persuasive framing, repeated buzzwords, and the reader-stop test (does each short sentence connect to the next, or does the reader stall at the period?).
3. Condense. Few declarative sentences beat one long one.
4. Match the surrounding text's density and idiom — read neighboring paragraphs first.
5. Per the user's global instruction, after editing a paper file: `git add`, commit, and push. End commit messages with the project's `Co-Authored-By` trailer.

## Quick contrast

Blog-like (avoid):
> What sets doc2lora apart is its smooth geometry: embeddings interpolate, and averaging papers moves toward the shared concept, so specific ideas sit around it. ICAE decodes points, but its embeddings fall in a narrow cone.

In style (use):
> Doc2LoRA embeddings form a smooth semantic space. Averaging a set of papers moves the embedding toward the concept those papers share. ICAE decodes constructed points. Its embeddings occupy a narrow cone. Averages over them remain as specific as a single paper.

Fragmented, fails the reader-stop test (avoid):
> The relevant information is present in the embedding. Cosine similarity and naive Euclidean distance do not expose it. A learnable bijective transform reshapes the geometry to surface it. We train this transform on a small set of citation pairs.

Connected, same bans respected (use):
> Even so, its embedding still carries the relevant information, hidden from cosine similarity and naive Euclidean distance. To surface it, we train a learnable bijective transform on a small set of citation pairs. This transform reshapes the geometry and brings doc2lora at least comparable with dedicated encoders.
