---
name: scientific-writing
description: Draft and revise multi-page scientific documents (papers, grant proposals) in the user's style. Structures documents for busy readers who skim, using a skeleton-first drafting loop with skim-reader and adversarial claim-and-evidence review passes. Also enforces the user's sentence-level voice (terse first-person description over persuasive, blog-like phrasing). Use whenever writing, rewriting, or reviewing paper or proposal prose, even for a single paragraph.
---

# Scientific Writing for Busy Readers

Write multi-page documents (papers, proposals) for a reader who will not read them in depth. This file holds the shared foundation, the reader model and the document-structure rules that every task uses. The task-specific instructions live in three companion files. Read the ones the task needs before producing anything.

## Which file to read, by task

- **`style.md`** — voice, attention budget, sentence rules, source layout, worked examples. Read before writing or editing ANY prose, down to a single sentence. For a small edit (a few sentences), this file plus the rules below suffice.
- **`workflow.md`** — the phased drafting–review loop and its rewrite entry path. Read when drafting or rewriting anything longer than a paragraph.
- **`critique.md`** — the skim-review and adversarial-review passes, including the risk–return audit. Read when the loop reaches a review phase, and whenever the user asks for a review or critique of existing text, theirs or anyone's.

A full drafting or rewriting task reads all three. A review-only task reads `critique.md` (and `style.md` if sentence-level faults are in scope). Never draft from this file alone.

## The reader model

Every rule in this skill derives from how a busy expert actually processes a long document. Hold this model while drafting and while reviewing.

1. **Readers skim before, or instead of, reading.** A reviewer with a stack of proposals scans headings, first sentences, figures, and bold text to orient, and only descends into full paragraphs where the skim raised interest or doubt (Rogers & Lasky-Fink, *Writing for Busy Readers*).
2. **Skimming is satisficing.** Eye-tracking shows skimmers read the opening of each unit until the rate of information gain drops, then jump to the next unit (Duggan & Payne, CHI 2011). The first sentence of a paragraph is often the only sentence read. Whatever it says is what that paragraph said.
3. **Readers remember gist, not text.** Comprehension compresses the document into a macrostructure of a few propositions. Details that do not attach to one of those retained propositions are deleted (Kintsch & van Dijk). A reader leaves a 15-page document holding perhaps five sentences. The writer's job is to choose those five sentences, not to hope.
4. **Working memory holds one thread.** A section that develops one idea gets encoded. A section that braids three ideas gets a blur. Organize each section around one unifying thread and subordinate everything else to it.
5. **Within a sentence, readers assign meaning by position.** The opening (topic position) is read as context linking back to what came before. The end (stress position) is read as the news to emphasize (Gopen & Swan, *The Science of Scientific Writing*). Old information first, new information last.
6. **Long documents are read out of order.** Reviewers jump to the section their concern lives in. Each section must survive being someone's entry point.

## Document structure

- **The skeleton must stand alone.** Headings plus the first sentence of every paragraph, read in order with the figures, must deliver the complete argument. The skeleton is the document the skimming reader actually reads. Everything below the first sentence is elaboration for the reader who descends.
- **Headings carry claims where the format allows.** "Mobility embeddings recover field structure without citation data" navigates and asserts. "Preliminary results" only navigates. In formats with fixed heading conventions, push the claim into a bold lead-in or the first sentence instead.
- **Context, content, conclusion at every scale** (Mensh & Kording, *Ten Simple Rules for Structuring Papers*). The document opens with why and closes with what follows. Each section opens by placing itself in the argument and closes on what the reader should carry forward. Each paragraph opens with its point.
- **One point per paragraph, point first.** The first sentence states the point in plain declarative form. The rest gives evidence and mechanism. If a paragraph needs two point sentences, it is two paragraphs. Never open a paragraph with throat-clearing context that defers the point to sentence three, because the satisficing reader is gone by then.
- **Repeat the core claim at every entry point.** The summary, the introduction, and the section where the work lives each state the central claim, in words adapted to their scale. To a linear reader this is structure, not repetition. To a skimming reader it is the only insurance that the claim is seen at all.
- **Re-anchor at section boundaries.** Open each section by restating, in one clause, the referent it depends on ("The mobility embedding from Thrust 1..."), because the reader may arrive here directly. Never open a section with a bare demonstrative pointing across the section break.
- **Front-load by primacy.** Within any unit (document, section, paragraph, list), order items by importance to the argument, not by chronology or by the order you did the work.
- **Figures are read independently.** Skimmers read figures and captions as a parallel document. Each caption states what the figure shows and what it means for the argument, without requiring the body text. Keep per-cell annotations neutral and descriptive, not qualitative verdicts.

## After editing

Per the user's global instruction, after editing a document file: `git add`, commit, and push. End commit messages with the project's `Co-Authored-By` trailer.
