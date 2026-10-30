---
name: sn-premise
description: >-
  Stage 1 of the Story Narration suite — turn an idea or an existing story/novel into an approved brief for a long narrated story video (30–120+ min): logline, genre and core emotion, dramatic or calm profile, narrator stance, runtime and syllable budget with speaking-rate calibration, chapter count. Use when the user brings a story idea or source text for a long "video kể chuyện", "truyện audio", "kịch bản truyện dài", "chuyển thể truyện thành video", or says "bắt đầu dự án truyện mới". Not for writing chapters (sn-write) or outlining (sn-outline).
---

# sn-premise — Idea → approved brief

`{studio}` = the sibling `sn-studio` skill directory (`../sn-studio` from this file).
Read `{studio}/references/profiles.md`, `{studio}/references/runtime-budget.md`,
`{studio}/references/genres.md`. For an existing story to adapt, also read §7 of
`{studio}/references/structure.md`.

## Step 0 — Collect parameters in ONE message (no drip questioning)

Must have (ask if missing — no safe default):
1. **Target runtime** (minutes).
2. **Story seed**: idea, or source text to adapt (file path or pasted; paste → save as `source.txt`).

Offer defaults; let the user confirm or change:

| Parameter | Default |
|---|---|
| Profile | inferred: `dramatic` for conflict-driven ideas, `calm` for healing / nostalgic / piano-covered ideas — say which and why |
| Genre + core emotion | inferred from the idea |
| Narrator | third-person storyteller, warm and restrained |
| Voice & speaking rate | 180 syllables/min until calibrated; ask which voice (TTS name or human) |
| Audience | general YouTube audience, adults |
| Ending type | earned, emotionally closed (per genre) |
| Adaptation fidelity (if source) | core-extract (faithful / core-extract / borrowed shell) |
| Era & place | the concrete era the story implies — never "ngày xưa" |

## Step 1 — Initialise

```bash
python3 {studio}/scripts/sn.py init <dir> --title "<working title>" --minutes <M> --profile <dramatic|calm> [--rate R]
python3 {studio}/scripts/sn.py budget --minutes <M> [--rate R]
```

**Calibration** (recommend strongly, it changes every number): once a narrator sample exists (sn-bible
writes one), render or read it with the real voice, time it, compute syllables/min, and set `rate_spm`
and `"rate_calibrated": true` in `project.json`. On macOS a rough check is
`say -v Linh -o /tmp/s.aiff "<text>" && afinfo /tmp/s.aiff | grep duration`.

## Step 2 — Draft the brief (Vietnamese content)

Write `project.json.brief` and a readable `brief.md`:

- `titles`: 3 options with a one-line reason (curiosity + emotion; no lies).
- `logline`: *who* wants *what*, *why now*, *who/what stops them*, *what's at stake* (Hicks' five questions).
- `genre`, `core_emotion`, `premise_promise` (what the "fun & games" must deliver).
- `theme`: the value question the ending answers — never a moral said aloud.
- `setting`: concrete era, place, social world (2–3 sentences).
- `narrator`: person, distance, tone, 1–2 signature devices.
- `ending`: type + final image idea (mirrors the opening image).
- `four_anchors` (dramatic): opening, plot point I, plot point II, ending (Field). Calm: the four movements.
- `engine`: the mechanism that will repeat, and its concrete destination (mechanism-and-agency.md §1).
- `endgame_reserve`: one-time cards and the earliest point each may be played.
- `runtime`: target minutes, rate (calibrated or not), syllable budget, chapters × minutes.
- `cold_open_idea`: hook template, the moving first image, the first three spoken lines' content.
- Adaptations: `adaptation` = fidelity; kept lines with a short verbatim evidence quote each; cut lines
  with a reason ("this means the story now ends at…"); merged characters; where the biggest payoff lands.
  Never invent source content from a title. For a long unread source, read it in parts (e.g. per 10–15
  chapters; parallel subagents if available) and summarise each part before deciding.

## Step 3 — Approval gate ⛔

Show a compact card in plain Vietnamese: titles, logline, profile + genre/emotion, narrator, runtime plan
(and whether the rate is calibrated), the anchors or movements, the engine; for adaptations the three
decisions (cut / merge / biggest payoff). Ask for approval or changes. Don't proceed until approved. On
approval set `project.json.stage` = `"bible"` and hand off to `sn-bible`.

## Quality bar

- Apply `sn-studio/references/ai-film-production.md` §1 to the existing logline: who wants what,
  what blocks them, and the visible change. For calm/no-character stories, use a gentle desire or
  discovery, not invented danger. Do not add a second brief or an image-generation step.
- The logline contains a concrete conflict ("một câu chuyện cảm động về tình thân" is not a logline).
- The premise promise is specific enough to generate 3+ set-pieces; the engine has a destination.
- The plan is realistic: a 30-minute story with 4 subplots and 9 characters is flagged and trimmed.
