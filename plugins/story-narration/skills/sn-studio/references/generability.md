# Generability: writing `[HÌNH]` that AI video can actually render

Applies whenever the visuals will be generated (Veo, Seedance, MiniMax, Kling… via scene or storyboard prompt skills). Does not
apply to live-action. Sources: drama-skills `short-drama-video-prompts/generability.md`, shuohao
`novel-script/script-pass.md` (hard rule 4 & 6), `novel-outline` warnings and scene caps, `novel-art`
scene-pass, `novel-storyboard/shot-writing.md`. Tags: **[src]** = from source, **[sn]** = sn heuristic.

## 1. The one test [src]

**Is this action common in ordinary footage?** Read the line to someone who hasn't read the script:
can they mime it immediately? If it needs explaining first, the model will probably fail it too.

| Safe | Rewrite |
|---|---|
| walk in, sit down, stand up, turn the head, nod, hand something over, take it, hug, push a door open, put something on a table, turn a page, reach for something, carry a load, board a boat | block a moving object with a tool, centimetre-level movements, single-finger precise operations, 4+ step two-handed choreography, micro-expressions as the load-bearing information |

## 2. Four high-risk patterns [src]

- **Precise interception** — two bodies timing on one small object; catching something in motion.
- **Invisible inner state** — "như thể nghe thấy gì", "chợt hiểu ra", "thoáng bối rối". Inference, not image.
- **Negative actions** — "không nhìn anh", "không trả lời". What doesn't happen cannot be generated;
  write the substitute action that *is* happening ("cô quay mặt ra cửa sổ").
- **Fine choreography chains** — three or more hand actions in one beat, left/right split.

Plus shuohao's generation-difficulty list, to be flagged whenever it appears: **rain, physical contact,
crowds, hand close-ups** [src]; sn adds readable text on screen (letters, signs), mirrors/reflections,
fire [sn].

## 3. Where the drama comes from [src]

**Dramatic information comes from the combination and timing of common actions, not from the finesse
of one action.**

- High-risk: "Anh dùng lòng bàn tay chặn mép cuốn sổ đang gập lại."
- Generable: "Anh gập cuốn sổ lại, tay vẫn đặt trên bìa, không rời." — control and refusal are visible.

## 4. Rewrite ladder (take the first that works) [src]

1. **Move the change to an object or the environment** — "Cửa bị gió đóng sập" beats "anh lấy chân móc cửa".
2. **Split across adjacent shots** — before and result; skip the process ("ngòi bút dừng trên giấy" / "trên giấy đã có thêm một dòng").
3. **Replace with a hold** — do the action, then the hand stays. Holding is the easiest performance.
4. **Hand it to sound** — the narration or an `[ÂM]` carries what can't be seen. (A natural fit for narrated video.)
5. If truly irreplaceable: keep it, mark `(rủi ro cao)` in the shot, and give a fallback.

Never use generability as a reason to cut drama — change the carrier, keep the beat. If the only
generable version changes the story result, send it back to the writer.

## 5. Emotion as body, not adjectives [src: shuohao shot-writing]

"Rất buồn" is not an image. Grief: head lowered, shoulders shaking slightly, fingers gripping a sleeve.
Tension: checking the clock, tapping the table, eyes darting. Anger: fists tight, jaw set, chest heaving.
Prefer slow, continuous small movements; avoid sprinting, jumping, rolling. Write the bridge between
actions ("quay người rồi thuận đà đưa tay lên").
But: in narrated video the **voice** can carry emotion, so don't stack both — see anti-ai-vi.md
(emotion landing order).

## 6. The cold open moves [src: shuohao]

The first image carries the hook **in motion**: ✗ static close-up (knuckles white on a suitcase)
✓ running through fog clutching the suitcase. Save static details for their second appearance.

## 7. World economy [src: shuohao novel-outline / novel-art]

- **One main line + at most one subplot** for short runtimes; each cut line gets a reason.
- **Location budget**: shuohao caps main scenes at 4 + ⌈episodes/10⌉ (5–15). sn applies it per 10 minutes
  of runtime [sn]. Every new location is another environment to keep consistent across dozens of clips.
- **One-off locations**: cut, or reuse a variant of an existing place (change time of day, weather,
  foreground, props) instead of opening a new one.
- **Narrative props ≤ 8**. Test: *if it broke, got lost, or was swapped, would the story collapse?* Yes →
  narrative prop (register in ledger). No → set dressing, belongs to the location's anchors.
- **Location anchors** must be drawable, recognisable, checkable ("mái tôn vá một mảng xanh", "bậc thềm thứ
  ba sứt góc"), never adjectives ("không khí cũ kỹ").
- **Pin a concrete era**. Never "ngày xưa", "cổ trang", "thời phong kiến" in visuals — the model picks a
  random century for each shot. Name it: "Hà Nội thập niên 1990", "Huế thời Nguyễn cuối thế kỷ 19",
  "miền Tây những năm 1970". If fictional, say what it *looks like*.
- **Surface condition** follows the real upkeep of the place: lived-in (worn, stained, patina) vs
  maintained (clean lacquer, wear only where people walk). Don't age a palace like a ruin.
- **Crowds**: when 3+ characters share a frame, decide how to stage it (who is foreground, who is
  back/over-shoulder) — shuohao's `crowdPlan`.

## 8. Revision discipline [src: shuohao]

Change one beat → reread the beat before and after. Check three things: **where each person is**, **what
is in whose hand**, **who is present**. When the image changes, the sound note (and later the shot) must
change with it.
