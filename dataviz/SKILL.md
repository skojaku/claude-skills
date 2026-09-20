---
name: dataviz
description: Use this skill whenever you are about to create ANY chart, graph, plot, dashboard, or data visualization, in ANY output medium — an HTML or React artifact, inline SVG, plotting code in any library (matplotlib, plotly, d3, Recharts, …), an image/PNG you will render and upload, a figure for a paper or slide deck, or a chart shared into Slack. Read it BEFORE writing the first line of chart code, choosing chart colors, building a stat tile / meter / KPI row, or laying out a dashboard. Triggers on "chart", "graph", "plot", "figure", "data viz", "visualization", "dashboard", "analytics", "visualize data", "categorical colors", "sequential / diverging palette", "stat tile", "sparkline", "heatmap", "legend", "axis", "tooltip", "chart colors", "color by series".
---

# Data Visualization

A chart is **read by people and executed by you**. This skill turns "make it look
good" into a procedure with checks, so the result is right by construction rather
than by taste.

**The method here is design-system-agnostic.** Nothing in the procedure, the form
heuristic, the six checks, or the mark specs is specific to one product. A design
system supplies a small set of *parameters* (its ramps, a categorical order, a
diverging pair, a status palette, a texture, its surfaces, its filter components);
the method consumes them unchanged.

**This install ships two instances of those parameters:**

- `references/palette.md` — **the default.** A claim-first, ink-based palette:
  colour marks the claim, everything else is neutral ink, at most two saturated
  colours per figure. Print-first. Derived from the data figures of Laurent
  Hébert-Dufresne. Use it for paper and slide figures, and for any on-screen
  chart with ≤ 3 series and one clear claim.
- `references/palette-screen.md` — the eight-hue identity palette (the upstream
  default). Use it for dashboards, many-series product UI, anything needing a
  selected dark mode, and for the fixed status scale.

> The single most important habit: **the color part is computable, so compute it.**
> Never eyeball whether a palette is colorblind-safe - run `scripts/validate_palette.js`.

## The procedure - do these in order

Color comes LAST. Most bad charts pick colors first.

1. **Pick the form.** What is the data's job - magnitude, identity, polarity, a
   single headline, change-over-time? The job picks the chart type, and sometimes
   the answer is *not a chart* (a stat tile or hero number). -> `references/choosing-a-form.md`
2. **Name the claim, then spend colour on it.** Write the one sentence the chart
   exists to prove. Colour only the marks that sentence names; everything else is
   ink. Then assign by job — categorical (identity), ordinal, sequential
   (magnitude), diverging (polarity), or status (state). -> `references/palette.md`,
   then `references/color-formula.md`
3. **VALIDATE the palette - run the script, don't reason about Delta E.**
   `node scripts/validate_palette.js "<hex,hex,...>" --mode light --surface "<surface>"`
   (relative to this skill's base directory - or load it as `<script type="module">`
   in the chart's own page, where it reads `data-palette` off `<body>` and logs a
   `console.table` report). It returns pass/fail on the lightness band, chroma
   floor, adjacent-pair CVD separation, the normal-vision floor, and contrast.
   Fix anything that FAILs before continuing. Validate the **hues** as a
   categorical set and any **ink ramp** with `--ordinal` — running the categorical
   checks on neutral ink FAILs by design (zero chroma) and is not a real failure.
   Re-run per mode against that mode's actual surface.
4. **Apply mark specs & spacers.** Thin marks, 4px rounded data-ends anchored to
   the baseline, 2px lines, >=8px markers, a 2px surface gap between fills (stacked
   segments and adjacent bars alike) and a 2px surface ring on overlapping marks,
   selective direct labels. -> `references/marks-and-anatomy.md`
5. **Add the hover layer - by default** *(screen output only)*. An HTML/SVG chart
   *is* interactive; ship a crosshair+tooltip on line/area and a per-mark hover
   tooltip on bar/dot/cell. Hit targets bigger than the mark; filters in one row
   above the charts. A print figure skips this and puts the same information in
   the caption. -> `references/interaction.md`
6. **Final accessibility pass.** Every series is directly labelled — under the
   claim-first palette that is mandatory, not a fallback, because the accent pair
   is thin in greyscale. For >= 2 series a legend is present unless every series is
   already labelled in place; a table view exists; dark mode, if needed at all, is
   **selected** from `palette-screen.md`, never an automatic flip; texture is
   available for the CVD/print/forced-colors case.
7. **Render it and look at it.** The validator checks color, not layout - open or
   screenshot the output and eyeball it for label collisions, geometry, and overflow
   before calling it done.

Then check the result against **`references/anti-patterns.md`** - it is the catalog
of what goes wrong. If your chart matches an entry, it's wrong.

## Non-negotiables

- **Colour marks the claim; everything else is ink.** At most two saturated
  colours per figure. A panel making no favourable/adverse claim is entirely ink.
  *(This install's first rule — it overrides "give every series a hue".)*
- **Three hues is the ceiling** — ink, vermillion, blue — and only for a category
  the reader must compare mark by mark. Past that: fewer series, facets, or small
  multiples. Never a generated hue.
- **Identity is carried by direct labels, never by colour alone.** The accent pair
  is thin in greyscale (luminance 0.22 vs 0.15), so this is a hard rule.
- **One axis.** Never a dual-axis chart (two y-scales). Two measures of different
  scale -> two charts, small multiples, or indexed to a common base. *(This is the
  #1 chart mistake - see anti-patterns.)*
- **Color follows the entity, never its rank.** A filter that changes the series
  count must not repaint the survivors. An ordinal ramp inside a panel that
  belongs to one entity is built on *that* entity's hue.
- **Sequential = one hue, light->dark. Diverging = two hues + a neutral midpoint.**
  Never a rainbow; never a hue at the diverging midpoint.
- **No green.** Not for a series, not for a highlight — it is reserved for status.
- **Uncertainty is always drawn**, and always the same way (envelope, capless
  whisker, or filled density). What the interval *is* goes in the caption.
- **Run the validator before shipping any palette.** CVD Delta E >= 8 is the target
  (OKLab ×100); a normal-vision floor below 15 is a hard FAIL. A contrast WARN
  obligates visible labels or a table view - it is not dismissable.
- **Thin marks; recessive grid/axes; selective direct labels** (never a number on
  every point).
- **Text wears text tokens, never the series color** - values, labels, and legends
  stay in primary/secondary/muted ink; a colored mark beside them carries identity.
- **Status colors are reserved** (good/warning/serious/critical) and never reused
  for "series 4"; they ship with an icon + label, never color alone.

## Plugging in a design system

The method is invariant; only these parameters change per system.

| Parameter | What the system provides |
|---|---|
| **Ink steps** | the neutral ramp everything non-claim is drawn in |
| **Accents** | the two saturated poles (favourable / adverse) |
| **Ramps** | the hue scales sequential/ordinal encodings draw from |
| **Categorical theme** | the fixed hue order, for the identity-work case only |
| **Diverging pair** | two warm/cool poles + a neutral midpoint |
| **Status palette** | good / warning / serious / critical - distinct from series hues |
| **Texture fill** | one directional hand-drawn fill, used at 45° / 135° |
| **Surfaces** | light & dark chart-surface colors (the validator needs these) |
| **Filter controls** | date-range & dimension controls (spec in `interaction.md`) |

To onboard a new system: fill those rows, feed its ramps to the validator, and let
it snap each slot to the nearest passing step. Structure and rules stay as written.

## Reference files

| File | What it answers |
|------|-----------------|
| `references/choosing-a-form.md` | Which chart type / is it even a chart? |
| `references/palette.md` | **The default instance** - claim-first ink palette, validated |
| `references/palette-screen.md` | The eight-hue identity instance, for dashboards & dark mode |
| `references/color-formula.md` | The four jobs, the six checks, snap-to-passing |
| `references/marks-and-anatomy.md` | Mark specs, spacers, labels, figures, hero number |
| `references/interaction.md` | Tooltips & hover, filters & time ranges |
| `references/components.md` | The pieces a chart is made of - build each in plain HTML |
| `references/anti-patterns.md` | **What goes wrong - check every chart against this** |
| `scripts/validate_palette.js` | Runnable six-checks validator (run it; don't eyeball) |
