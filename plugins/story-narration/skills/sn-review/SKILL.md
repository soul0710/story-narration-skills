---
name: sn-review
description: Stage 5 of the Story Narration suite — review and revise written chapters of a long narrated story script: deterministic checks, 5-dimension scoring, agency and mechanism-exhaustion audit, template-feel and Vietnamese AI-voice passes, structural reverse outline, and final export (full script, plain TTS narration, voice-actor script, YouTube chapter timestamps). Use when the user asks to "kiểm tra chương", "review kịch bản", "đánh giá", "rà soát mạch truyện", "khử giọng AI", "xuất kịch bản", or after sn-write batches.
---

# sn-review — Score, fix, export

`{studio}` = the sibling `sn-studio` skill directory. Read `{studio}/references/anti-ai-vi.md`,
`{studio}/references/continuity.md`, `{studio}/references/mechanism-and-agency.md`,
`{studio}/references/ai-failure-modes.md` (the checklist) and `{studio}/references/review-protocol.md`
(the method: priority order, separate passes, evidence rules, the reviewer prompt for a fresh agent); for structural
passes also `{studio}/references/structure.md` and `{studio}/references/scene-craft.md` (§9 checklist).

## Scope

`review N`, `review N-M`, or `review all`. Default: chapters written since the last review.

## Step 1 — Deterministic checks

```bash
python3 {studio}/scripts/sn.py duration <dir>
python3 {studio}/scripts/sn.py continuity <dir>
python3 {studio}/scripts/sn.py lint <dir>/chapters/chNN.md …
python3 {studio}/scripts/sn.py audit <dir>
```

## Step 1b — Full read-through and fact audit ⛔ (cannot be replaced by the scripts or by memory)

Read every chapter in scope **completely, in order, from the files** — not from memory of writing them
and not from summaries. Prefer a fresh context: if subagents are available, give the chapters, bible,
ledger and this skill to a reviewer agent that did not write them (the writer's memory hides errors).
[Pilot, 2026-09-26: a memory-based review scored the draft 41/50; a real read-through then found 12
errors that every script had passed — wrong day counts, a lunar date on a postmark, a phone-call logic
hole, a world rule broken, a dangling clue, a narrator stating a falsehood as fact.]

For `review all` and at the end of the story: **read the whole story in one sitting first** (section A of
ai-failure-modes.md — the story as a whole, not chapter by chapter), then go item by item through sections
B–F and record each as checked / found / fixed.

While reading, build these tables in the review file and check each row:
- **Timeline**: every day/time mentioned per scene → do counts ("ba ngày nữa là rằm") add up? Calendar
  sense (postmarks and documents use the solar calendar; festivals the lunar one)?
- **Numbers**: ages across years, money (deposit, debts, savings), distances, durations → arithmetic.
- **Who knows / who did what**: for every reveal, how does the character know? For every action
  (call, visit, delivery), is it physically possible given who was where?
- **World rules vs scenes**: every rule in `bible/world.md` against every scene that touches it.
- **Dangling details**: every specific, pointed detail (a letter delivered by hand, a missing object)
  → where is it paid off? Unpaid → pay it, or cut the pointing.
- **Fair play**: does the narrator ever state as fact something later revealed false? (Allowed only as a
  character's belief.)
- **Terms and address**: kinship terms, titles, xưng hô correct for gender and relationship.
- **Header vs page**: `learns` / `reveals` / `props` in each header match what happens on the page.

## Step 2 — Judgment scoring (each 1–10, cite line evidence for every score below 8)

| Dimension | Looks at |
|---|---|
| Hook & rhythm | cold open in motion / previous hook answered / end hook; tension–release; information density not uniform |
| Payoff & agency | planned payoffs delivered with enough prior pressure; the protagonist decides and receives (four questions); witnesses amplify, don't replace; costs carried forward |
| Scene & dialogue | each scene turns a value via action or revelation; no repeated beats; dialogue as action, agenda, subtext; distinct voices & xưng hô; no moralising |
| Listenability & visuals | sentence length, attribution, names re-anchored, spoken time/place cues, numbers as words; `[HÌNH]` generable and consistent with signatures/anchors |
| Continuity | ledger/state consistent, knowledge order, three layers of truth, timeline, objects in hand, promises |

Total /50: 45–50 ship · 40–44 polish · 30–39 revise and re-review · <30 rewrite. (Adapted from
short-drama's five-dimension review; the thresholds are sn defaults.)

For `review all` (or every ~3 chapters) add the **long-story audits**:
- **Mechanism exhaustion** (mechanism-and-agency.md §1): shuffle test on the runs; symptoms (predictable
  outcomes, bigger scale / smaller change, opponent acting dumb). Fix by changing the vector, not the target.
- **Agency**: at each key node answer the four questions; flag rescues by outside force.
- **Endgame reserve & expectation debt**: any card played early? Delays paying interest?
- **Template feel** (anti-ai-vi.md §4): causal/strategy repetition, over-explaining, over-closing,
  uniform density, costs settled immediately — only with two or more cited locations each.

Save `reviews/chNN-review.md` (or `reviews/all-YYYY-MM-DD.md`) in Vietnamese: score table, then numbered
issues in the review-protocol format — **quote (chương:dòng) · basis · impact · minimal fix · class**
(`lỗi rõ ràng` / `nguy cơ cần xem xét` / `lựa chọn phong cách`), priority order logic → people → prose.
No quota: if nothing is wrong, say so; missing context → `chưa đủ dữ kiện`. Findings from any AI reviewer
(including yourself) are proposals: verify each against the text before fixing.

## Step 3 — Revision passes (big → small; don't polish what may be cut)

1. **Structure**: reverse-outline — one line per written chapter describing what it *actually* does, read
   without the outline; diff against the outline. Removable scenes (no state change, no payoff) → wire
   in, merge, or cut. Flat stretches → escalate.
2. **Character**: wants/needs visible, arcs moving, cover-the-names test.
3. **Continuity**: fix all `sn.py continuity` errors and judgment findings; update ledger and state.md.
4. **Pacing**: runtime within tolerance; intensity matches the plan.
5. **Line**: anti-AI gates at the level lint reports, minimal changes, never delete plot-bearing lines;
   generability fixes via the rewrite ladder.

Apply fixes only when the user asked for revision or approved the issue list. Audit-only requests get the
report without edits. `sn.py snapshot <dir> --label <pass>` before every pass; `sn.py changes` after, and
log content changes (facts, clues, motives, voice). Never fix by adding new facts or changing a motive —
raise those as questions for the user.

## Step 4 — Export (story complete or on request)

```bash
python3 {studio}/scripts/sn.py export <dir>
```

- `export/script-full.md` — clean full script.
- `export/narration.txt` — spoken text only, no labels: paste into TTS.
- `export/narration-cast.txt` — with `[Người dẫn]` / `[Tên | cách nói]` labels and pauses, for voice actors.
- `export/youtube-chapters.txt` — chapter timestamps for the video description (estimated from the rate;
  re-time after the real voice-over).

Report total runtime and chapter count; suggest `sn-shots`. After any chapter edit, re-run
`sn.py shots` for chapters that already have shot files — a changed narration makes them stale
(the check fails), then `sn.py segment --force` and re-align the SHOT visuals.
