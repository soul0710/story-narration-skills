# Story structure for long narrated stories

Merged from jtydhr88 `sw-story-structure` (Field, Snyder, McKee, Hoxter, Hicks, Lu Jun), short-drama
`rhythm-curve`, and oh-story outline methods. Use the parts that fit; the story decides, not the template.
This file is for the **dramatic** profile; calm stories use profiles.md. Scene-level design is in
scene-craft.md; repeated mechanisms and agency in mechanism-and-agency.md.

Rule classes (drama-skills): beat percentages, intensity numbers and turn positions are *craft defaults*
— diagnostic tools, not proof of quality. The validator only warns on them.

## 1. Know four things before outlining (Field)

The **ending**, the **opening**, **Plot Point I** (why the protagonist can't go back), **Plot Point II**
(what launches the final act). Plus Hicks' premise questions: *Who? Wants what? Why now? Who stops them?
What happens?* If any is blank, stay in `sn-premise`.

## 2. Units

- **Beat** — one action/reaction exchange.
- **Scene** — continuous time/place; must **turn a value** (safe→danger, trust→suspicion, hope→despair).
  Write the value at start and end; if unchanged, cut the scene and move its information elsewhere (McKee).
- **Sequence / chapter** — 2–5 scenes escalating to a peak; give each chapter one idea ("the box", "the
  first lie"). One chapter ≈ one sequence ≈ 4–7 minutes.
- **Act** — sequences culminating in a major reversal.

## 3. Beat map (Save the Cat mapped to percent)

| # | Beat | % | Narration-specific note |
|---|---|---|---|
| 1 | Opening image | 0–1 | A concrete image that captures the "before" state; inverted in the final image |
| 2 | Theme stated | ~5 | Usually a side character says it; the narrator must *not* moralise it |
| 3 | Set-up | 1–10 | Introduce all main characters or mention them; plant the "flaws to fix" |
| 4 | Catalyst | ~10 | Bad news disguised as opportunity (or reverse). On screen, not reported |
| 5 | Debate | 10–20 | One real hesitation, not three |
| 6 | Break into 2 | 20–25 | Protagonist **decides**; never pushed in by coincidence |
| 7 | B-story | ~27 | Relationship line carrying the theme |
| 8 | Fun & games | 25–50 | Deliver the premise's promise — the reason the viewer clicked |
| 9 | Midpoint | ~50 | False victory or false defeat; stakes rise; a clock may start |
| 10 | Bad guys close in | 50–75 | External pressure + internal fracture |
| 11 | All is lost | ~75 | Worse than the start; a "whiff of death" (literal or symbolic) |
| 12 | Dark night | 75–80 | Short; the lesson is learned by losing |
| 13 | Break into 3 | ~80 | Solution comes from the B-story / theme |
| 14 | Finale | 80–97 | Defeat opponents from small to big; protagonist changes the world |
| 15 | Final image | 97–100 | Mirror of the opening image |

Common failures (Snyder's board): Act 1 bloated with backstory; Act 3 only "she knows what to do" +
"showdown" — go back to the flaws list, subplots and opponent roster.

## 4. Progressive complications (McKee)

- Each failure must teach the protagonist **one new thing** (Wei Minglun). List what they learn after each
  setback; a setback that teaches nothing merges into its neighbour.
- Protagonist takes the smallest, most conservative action first → the world reacts more strongly →
  a riskier action. Each step is a point of no return.
- Risk test: "If they don't get it, what do they lose?" If the answer is "back to normal", raise stakes.
- Crisis = a true dilemma (two goods or two evils), a deliberate still moment, on the page.
- Climax: "inevitable yet unexpected"; give the audience what they want, not the way they expect.
- Never resolve the climax by coincidence; no new coincidences after the midpoint.

## 5. Intensity curve across chapters (short-drama four phases, scaled to runtime)

| Phase | Share | Intensity | Job |
|---|---|---|---|
| Rise (起势) | first 15% | ★★ | Establish, 3+ open questions, a first small payoff |
| Climb (攀升) | 15–45% | ★★–★★★ | Main conflict in full; "two steps forward, one back"; first opponent beaten |
| Storm (风暴) | 45–80% | ★★★–★★★★ | Secrets revealed in layers; lowest point (keep it short); rebound begins |
| Showdown (决战) | last 20% | ★★★★★ then release | Final confrontation over 1–2 chapters; close every open question; 1 chapter of afterglow |

Warnings from `sn.py outline` (dramatic profile): >10 minutes without a payoff or intensity ≥3; the highest
intensity outside the final 30%; a `midpoint` beat outside 40–55% of runtime. Override with a reason.
Rules for judgment: two peaks back to back dilute each other; alternate main plot and relationship line
so they don't peak together; after a big payoff give one quieter chapter that still adds new information.

## 6. Openings and endings (Lu Jun, Chinese dramaturgy)

- **Enter late** (宜近不宜远): cut in near the conflict; deliver backstory later, inside action.
  Opening strategies: conflict-first; set the battlefield; unexpected arrival; flash-forward fragment;
  a "blow on the head" rule/decree; direct self-introduction by the narrator (useful for narration).
- **Endings**: thunderclap (climax = resolution), open question, extension, rebound, keynote line,
  echo of the opening, cycle. Avoid: too neat, too long ("end when it should end"), deus ex machina,
  soft landing via the narrator explaining the moral.
- **Change is drama**: relationships, character, fortune, balance of power, atmosphere, narrative mode.
  Priority of sources: character choice > craft > accident > outside force.

## 7. For adaptations of an existing story (shuohao `novel-outline`)

Choose fidelity: **faithful / core-extract (default) / borrowed shell**. Decide and show the user three
things before chapter planning: which lines are cut, which characters are merged, where the biggest
payoff lands. Every key keep/cut should cite a verbatim fragment of the source as evidence. Never invent
content from a title alone.
