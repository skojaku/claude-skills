# Claim-first palette (the ink instance)

This is **this install's reference instance** of the data-viz method: the
parameters the method needs, filled in with an ink-first, publication-grade
palette. It replaces the eight-hue screen palette as the default. That palette
is not deleted — it is still the right instance for dashboards and many-series
product UI, and now lives in `palette-screen.md`. See *Which instance* at the
bottom.

Source: the data figures of Laurent Hébert-Dufresne (Vermont Complex Systems
Center) — e.g. Figs. 2 and 3 of *The network epidemiology of an Ebola epidemic*
(arXiv:2111.08686) — as codified in
`~/Documents/projects/teams4industry/paper/current/figs/scripts/DESIGN_SPEC.md`
(rev. 2, 2026-09-08, amended 2026-09-09). Every contrast number below was
measured with `scripts/validate_palette.js`, not copied from the source spec;
where the two disagree, the measured value is here and the discrepancy is noted
at the end.

## The one rule

> **Colour marks the claim. Everything else is ink.**

A reader's eye goes to the saturated thing, so saturation is a budget. A figure
gets **at most two saturated colours**, and they are spent on the contrast the
panel is making. Every other series — context, baselines, the other conditions,
the rest of a sweep — is a step of neutral ink.

Per panel, the assignment procedure is one question: *what single sentence does
this panel exist to prove?* Colour only the marks that sentence names.

- Two series contrasted as favourable vs adverse → the two accents.
- One result against context → the result takes one accent, the rest go ink.
- No favourable/adverse claim at all (a posterior, a schematic of a task) →
  **entirely ink**, like Laurent's Fig. 3B–E.

This is the opposite default from a dashboard palette, where every series gets a
hue because identity is the job. Here identity is carried by **direct labels**,
and hue is reserved for the argument.

## Slots

Measured against the print surface, paper white `#ffffff`.

| Role | Hex | Contrast on white | Where |
|---|---|---|---|
| ink — primary data, the reference series | `#1a1a1a` | 17.40 | the black line in Laurent's Fig. 3A |
| ink 2 — a second neutral series | `#767676` | 4.54 | |
| ink 3 — context, a de-emphasized series | `#bdbdbd` | 1.88 | deliberately recessive; see the ordinal caveat |
| fill — histogram bodies, neutral areas | `#e6e6e6` | 1.25 | |
| **accent, favourable pole** | `#0072b2` | 5.19 | right answer, recovery, correction, "X helps" |
| **accent, adverse pole** | `#d55e00` | 3.87 | wrong answer, trap, internalization, "X hurts" |
| axis, tick marks | `#c3c2b7` | 1.79 | |
| axis label, panel letter | `#1a1a1a` | 17.40 | |
| tick label, direct label on a neutral series | `#52514e` | 7.94 | |

**No green.** Not for a model, not for a series, not for a highlight. (Green is
reserved for status in `palette-screen.md`; letting it also mean "series 3" is
what makes a status colour stop meaning anything.)

## The accent pair, validated

`#0072b2` / `#d55e00` is Okabe-Ito blue and vermillion — the canonical pair that
survives protanopia, deuteranopia and tritanopia:

```
$ node scripts/validate_palette.js "#d55e00,#0072b2" --mode light --surface "#ffffff"
  [PASS] Lightness band         all 2 inside L 0.43–0.77
  [PASS] Chroma floor           all 2 >= 0.1
  [PASS] CVD separation         worst adjacent #0072b2↔#d55e00 ΔE 21.9 (protan) · tritan 30.9
  [PASS] Normal-vision floor    worst adjacent #0072b2↔#d55e00 ΔE 31.2 (normal)
  [PASS] Contrast vs surface    all 2 >= 3:1
  → ALL CHECKS PASS
```

ΔE 21.9 under simulated CVD is far clear of the ≥ 8 target — this pair is the
reason the two-accent budget is affordable at all.

**But greyscale is thin.** Measured relative luminance is 0.15 (blue) vs 0.22
(vermillion). Printed in black and white, or photocopied, they nearly collapse.
So: **never let colour alone carry a distinction — every series is also directly
labelled.** That is a hard rule here, not the "secondary encoding" escape hatch
of the six checks.

## Categories

A category is **three steps of ink** (`ink_steps`) plus a direct label at the end
of each line. Not three hues.

**The one exception** — earned on a real render, not in principle: a category the
panel makes the reader compare *mark by mark*. In the source spec's F2(b), three
models × (band + posterior mean + counting line + whisker) are packed into a
1.12 in row; at 0.9 pt the ink steps `#1a1a1a` / `#595959` / `#949494` did not
separate — the row read as one grey mass. Only there do the three categories take
a hue each:

```
MODEL_HUES = ink #1a1a1a, vermillion #d55e00, blue #0072b2
```

That is the whole set. A reddish purple was tried as a fourth/alternate and
rejected on the render. **Three hues is the ceiling, and the hue never replaces
the direct label.** Nothing else categorical gets hues. If a chart needs more
than three hues to be readable, the answer is fewer series, facets, or small
multiples — not a bigger palette. (Same conclusion the screen palette reaches by
measurement: its own all-pairs cap is three slots.)

## Ordinal

One hue, light → dark, every step directly labelled. More of the variable means
more of the accent, so an ordinal variable that runs toward the favourable pole
is the blue ramp (`seq_blue`).

**Scoping rule:** an ordinal ramp inside a panel that already belongs to one
category is built on *that* category's hue (`seq_from(hue, n)`). Once blue means
one model, blue cannot also mean "high p" in the panel next door. Space every
ramp evenly in contrast (3.0:1 → 13:1) so the same ordinal value lands on the
same lightness in every row.

**Light-end caveat (measured, and a correction to the source spec).** Used as an
ordinal ramp, the ink steps fail the light end:

```
$ node scripts/validate_palette.js "#1a1a1a,#767676,#bdbdbd" --ordinal --mode light --surface "#ffffff"
  [FAIL] Light-end contrast     #bdbdbd at 1.88:1 vs surface — below 2:1 floor
```

`#bdbdbd` is fine as **ink 3 = context meant to recede** (a de-emphasized series
the reader is not asked to read off). It is not fine as the light end of a ramp
whose steps carry discrete ordered values. For that, stop at `#b4b4b4`:

```
$ node scripts/validate_palette.js "#1a1a1a,#767676,#b4b4b4" --ordinal --mode light --surface "#ffffff"
  → ALL CHECKS PASS   (light end 2.07:1)
```

## Diverging

**vermillion ↔ white ↔ blue** (`div_wrong_right`), for a plane whose low end is
the adverse pole — e.g. a share of groups ending right, where 0 means every group
holds the wrong answer.

Why not a sequential ramp off neutral grey: grey says "nothing here" exactly
where the panel means "all of them ended up wrong", and it spends the accent on
only one of the two poles. The **white midpoint is not decoration** — it puts the
crossing the panel is about onto the plane itself. Equal step count per arm.

## Uncertainty

Uncertainty is **always drawn**, and always the same way:

- a continuous interval → a pale envelope of the series colour, no outline;
- an interval at a discrete x → a whisker in the series colour, 0.7 pt, **no
  caps**, drawn behind the marker;
- a posterior over a parameter → the density filled `#e6e6e6` with a `#1a1a1a`
  outline.

Say in the caption *what* the interval is (cluster bootstrap over tasks at 95 %,
or the 95 % credible interval). Never on the figure. A quantity plotted with no
interval must be one that has none.

## Text and chrome

Text wears text tokens, never the series colour: `#1a1a1a` for axis labels and
panel letters, `#52514e` for tick labels and direct labels on neutral series.
Axis and ticks are `#c3c2b7` — present, recessive, never competing with data.

A direct label on an accented series may take that accent; a label on an ink
series stays `#52514e`.

## Surfaces (for the validator)

- Print / paper surface: `#ffffff`
- Light screen surface: `#fcfcfb`

For an HTML chart, define the slots you use as CSS custom properties in a local
`<style>` block and reference them by role — the mechanics (and the light/dark
scoping pattern) are in `palette-screen.md` § How to use these values.

This instance is **print-first** and has no selected dark mode. A chart that must
render on a dark surface uses `palette-screen.md`, whose dark column is a
selected, validated set — do not flip these values automatically.

## Which instance

| Situation | Instance |
|---|---|
| Paper / manuscript figure, slide figure, anything print-bound | **this file** |
| ≤ 3 series and one clear claim, on screen | **this file** |
| Dashboard, product UI, many-series identity work, dark mode required | `palette-screen.md` |
| Status (good → critical), delta cues | `palette-screen.md` § Status — fixed, never themed |

The *method* is unchanged either way: the four jobs, the six checks, and the
validator in `color-formula.md` apply to both. Only these parameters differ.

## Where this instance disagrees with its source

The source spec states two contrast figures that do not reproduce. Measured on
white with `contrast()` from `validate_palette.js`:

| Claim in DESIGN_SPEC.md | Measured |
|---|---|
| `#d55e00` "clears 4.6:1" | **3.87:1** — clears the 3:1 mark floor, not 4.5:1 text |
| `#de8f05` (the rejected old accent) "sat at 2.2:1" | **2.61:1** |
| greyscale luminance "0.24 vs 0.32" | **0.22 (vermillion) vs 0.15 (blue)** |

The decisions those numbers were used to justify all still hold — vermillion
really is the stronger mark, `#de8f05` really did disappear as a 1 pt line, and
the greyscale gap really is too thin to carry a distinction alone. Only the
digits were off. Use `#d55e00` for marks; if it must carry small text, darken it.
