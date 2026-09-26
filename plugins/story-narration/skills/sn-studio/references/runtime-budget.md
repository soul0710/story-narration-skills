# Runtime budget

Runtime in a narrated video is almost entirely speech. Budget it before outlining and check it after
every chapter (`sn.py duration`). Method from shuohao `novel-script` (deterministic duration per episode,
±15% gate; lines at 4.5 Chinese characters/s) and story-skills audiobook runtime (words per minute).
**[src]** from source, **[sn]** sn heuristic or measurement.

## Speaking rate [sn]

Vietnamese is written syllable by syllable, so `sn.py` counts space-separated tokens as syllables.

- **Measured**: macOS Vietnamese TTS voice "Linh" at default speed read 82 syllables in 25.5 s ≈ **193
  syllables/min** (2026-09-26). Chinese TTS in shuohao's pipeline is 4.5 chars/s = 270/min for reference.
- **Default in sn**: 180/min (a little slower than default TTS, typical of a calm storyteller).
- **Pilot check** (2026-09-26, 30-minute story, voice Linh calibrated at 189/min): the script estimated
  27:52 of speech; the real TTS render of the whole narration took 29:03 (TTS adds its own breaths at line
  breaks), i.e. the estimate ran ~4% short. Expect real renders slightly longer than estimated.
- The range across voices and styles is wide (roughly 150 for slow emotional human reading to 220+ for
  fast recap channels). **Calibrate every project**: render or read one minute of a draft chapter with
  the real voice, count syllables, set `rate_spm` and `"rate_calibrated": true` in `project.json`.
  Until then `sn.py duration` prints a warning.

## Budget formula

`seconds = spoken syllables / rate × 60 + Σ[NGỪNG]` — the same formula for planning and checking.
`sn.py budget` shows the syllable count with no pauses and with pauses ≈ 4% of runtime; `sn.py duration`
prints how many syllables a chapter needs given the pauses it actually contains.

## Chapter sizing [sn]

| Target | Chapters | Minutes each | Notes |
|---|---|---|---|
| 30 min | 6–7 | 4–5 | Three acts, one midpoint, ≤1 subplot |
| 45 min | 8–10 | 4–6 | Room for one B-story |
| 60 min | 10–12 | 5–6 | Two subplots, a false win/loss at midpoint |
| 90 min | 14–18 | 5–7 | Consider four movements (split Act 2) |
| 120 min+ | 18–25 | 5–7 | Each ~30 min block is a movement with its own mini-climax |

These are working defaults, not rules. The first chapter includes a 45–90 s cold open.

## Structural anchors (dramatic profile) [src: Field, Snyder, McKee via jtydhr88]

| Anchor | % |
|---|---|
| Cold open / hook | 0–3% |
| Inciting incident | ~10% |
| Point of no return | 20–25% (protagonist chooses) |
| Midpoint turn | 45–55% |
| Lowest point | ~75% |
| Climax begins | 80–88% (last act ≤ 20%, McKee) |
| Resolution + final image | last 3–7% |

Calm profile uses the four movements in profiles.md instead.

## Tolerances

- Outline: chapter minutes sum to target ±5% (error).
- Chapter: estimated duration within ±10% of planned minutes (error; shuohao uses ±15%).
- Over budget → cut summary narration and repeated beats first, then compress dialogue; never cut a
  plant/payoff line. Under budget → add conflict or a scene that turns a value; never pad with scenery
  or restated feelings ("add conflict, not small talk" — shuohao).
