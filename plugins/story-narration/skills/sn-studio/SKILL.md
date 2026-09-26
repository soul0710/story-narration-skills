---
name: sn-studio
description: Entry point and router for the Story Narration suite (sn-*) — writing long (30–120+ min) narrated story videos (kể chuyện có lời dẫn, truyện audio, phim truyện kể) with Vietnamese output. Use when the user wants to start, resume, or check a long narrated story script ("viết kịch bản truyện dài", "video kể chuyện 30 phút/1 tiếng", "tiếp tục dự án truyện", "kiểm tra tiến độ kịch bản"), or asks which sn-* skill to use. Holds the shared references and the sn.py checker used by sn-premise, sn-bible, sn-outline, sn-write, sn-review, and sn-shots.
---

# sn-studio — Story Narration suite

One pipeline for long narrated story videos: idea (or source story) → brief & runtime budget → story
bible → chapter outline → chapter-by-chapter narration script → review → shot list for image/video
prompting. Skill instructions are in English; **all story output is Vietnamese** unless the user asks
otherwise. Talk to the user in the language they use.

`{studio}` = this skill's directory. Shared references live in `{studio}/references/`, the checker in
`{studio}/scripts/sn.py` (Python 3, stdlib only). Other sn-* skills reference these paths.

## Pipeline

| Stage | Skill | Produces | Gate |
|---|---|---|---|
| 1. Premise | `sn-premise` | `project.json` brief + runtime budget, `brief.md` | User approves logline, genre, runtime, narrator |
| 2. Bible | `sn-bible` | `bible/characters.md`, `bible/world.md`, `bible/narrator.md`, `ledger.json` | User approves cast & narrator voice |
| 3. Outline | `sn-outline` | `project.json.chapters`, `outline.md` | `sn.py outline` PASS + user approves 3 key decisions |
| 4. Write | `sn-write` | `chapters/chNN.md`, `state.md` | `sn.py duration` within ±10%, `sn.py continuity` PASS |
| 5. Review | `sn-review` | `reviews/*.md`, fixes, `export/` | Scores ≥ 40/50, lint clean enough |
| 6. Shots | `sn-shots` | `shots/kich_ban_chNN.md` + `shots/loi_dan_chNN.md` | `sn.py shots` PASS; feeds image/video prompt skills (scene / storyboard) |

Stages 4–5 loop per batch of chapters. The user can jump in anywhere (e.g. bring an existing outline to
`sn-outline` in check mode, or a finished chapter to `sn-review`).

## Project layout

```
<project>/
├── project.json      brief, target_minutes, rate_spm, profile, stage, chapters[] (plan)
├── brief.md          human-readable brief
├── ledger.json       characters, promises, knowledge (author truth), props, fragile facts
├── state.md          ≤1.5 KB context card, rewritten after each chapter
├── outline.md        rendered from project.json by `sn.py outline --render`
├── bible/            characters.md, world.md, narrator.md
├── chapters/         ch01.md … (tagged narration format)
├── reviews/          review reports
├── export/           script-full.md, narration.txt (plain TTS), narration-cast.txt, youtube-chapters.txt
└── shots/            kich_ban_chNN.md (for prompt skills) + loi_dan_chNN.md (narration per shot)
```

## Starting or resuming

1. Ask for (or detect) the project folder. Default: a new folder named after the working title (ascii,
   kebab-case) in the current directory.
2. If `project.json` exists, run `python3 {studio}/scripts/sn.py status <dir>` and resume at
   `project.json.stage`; tell the user in one or two plain sentences where things stand and what's next.
3. If not, hand off to `sn-premise`.

## Commands (sn.py)

```bash
python3 {studio}/scripts/sn.py init <dir> --title "…" --minutes 45 [--rate 180] [--profile dramatic|calm]
python3 {studio}/scripts/sn.py budget --minutes 45 [--rate 180] [--chapters 9]
python3 {studio}/scripts/sn.py outline <dir> [--render]
python3 {studio}/scripts/sn.py duration <dir> [--ch 3]
python3 {studio}/scripts/sn.py continuity <dir>
python3 {studio}/scripts/sn.py lint <file...>
python3 {studio}/scripts/sn.py segment <dir> --ch 3 [--clip 8]
python3 {studio}/scripts/sn.py shots <dir> --ch 3 [--clip 8]
python3 {studio}/scripts/sn.py audit <dir>
python3 {studio}/scripts/sn.py snapshot <dir> [--label why]
python3 {studio}/scripts/sn.py changes <dir> [--since label] [-v]
python3 {studio}/scripts/sn.py export <dir>
python3 {studio}/scripts/sn.py status <dir>
```

Checks report facts. `✗` = structural error (exit 1): fix and re-run until PASS. `!` = craft/taste
warning: fix it or consciously accept it with a reason. Never claim a gate passed without running it.

## Shared references (load only what the current step needs)

| File | Use for |
|---|---|
| `references/profiles.md` | dramatic vs calm profile, rule classes (what may block) |
| `references/runtime-budget.md` | speaking rate + calibration, chapter sizing, anchors, tolerances |
| `references/structure.md` | beats, acts, progressive complications, intensity curve, openings/endings, adaptation |
| `references/scene-craft.md` | scene engine card, McKee's five steps, outcomes & sequels, location, props, suspense |
| `references/mechanism-and-agency.md` | repeated mechanisms & exhaustion, protagonist agency, expectation debt, rule of three |
| `references/hooks-and-retention.md` | cold open, chapter-end/start hooks, open loops, re-hooks |
| `references/genres.md` | genre cards (sn synthesis), payoff types, opponent tiers |
| `references/characters-and-dialogue.md` | character sheet, narrator voice, dialogue as action, dialogue checklist |
| `references/narration-format.md` | the tagged chapter format and narration craft |
| `references/generability.md` | writing `[HÌNH]` that AI video can render; location/prop economy; era |
| `references/continuity.md` | ledger.json, three layers of truth, chapter header, state card, revision order |
| `references/anti-ai-vi.md` | AI voice and template feel in Vietnamese narration |
| `references/review-protocol.md` | **how to review**: logic → people → prose, separate passes, quote + basis + class, reviewer prompt, versions |
| `references/ai-failure-modes.md` | **the 23 most common AI long-form errors** → prevention + detection; the review checklist |

Provenance: each reference tags ideas **[src]** (from a named source skill) or **[sn]** (sn heuristic or
measurement). Treat [sn] numbers as defaults to question.

## Working principles

- **Progressive, not one-shot.** Confirm each stage before the next; write chapters in batches of ≤3.
  A wrong outline costs one round; a wrong 45-minute draft costs everything.
- **Files are memory.** Long stories never rely on conversation memory. Before each chapter read
  `state.md`, the outline rows, the previous chapter's last scene, and bible entries for that cast only.
- **Validators over memory.** After upstream edits (merge characters, move a payoff) re-run
  `sn.py outline` and `sn.py continuity`; they name what broke downstream.
- **See the whole story, not just the chapter.** The deadliest AI failure: every chapter fine, the story as a
  whole not. Write against the outline row and the state card; audit the whole story (`sn.py audit`) and
  read it in one sitting at the end. Checklist: `references/ai-failure-modes.md`.
- **An AI suggestion never becomes story truth automatically.** Bible + ledger = approved canon; anything
  newly invented goes to `bible/proposals.md` until the user approves it. Real-world details are verified
  or marked fictional (`ledger.realworld`).
- **Fix in order: logic → people → prose.** Snapshot before edits; log content changes, not only wording.
- **Review in detail after every write.** Every chapter written or rewritten gets a full re-read from the
  file plus the fact audit (sn-write step 6, sn-review Step 1b), with a `reviews/chNN-review.md`. Scripts
  passing is not a review; memory is not a review. Full cross-chapter `sn-review` every 3 chapters and at
  the end.
- **Report plainly.** Tell the user what was written/changed, what they need to decide (one plain
  question + recommended default), and the next step. No field names or script jargon in the report.

## Credits

Distilled from MIT/Apache-2.0 projects: 0xsline/short-drama, eternityspring/shuohao-skills,
zenstory-ai/drama-skills, zenstory-ai/oh-story-claudecode, jtydhr88/screenwriting-skills,
danjdewhurst/story-skills. See `CREDITS.md` and `licenses/`.
