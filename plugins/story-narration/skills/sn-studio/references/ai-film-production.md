# AI film production: seven stations, adapted to narrated stories

Read the relevant sections during premise (§1), bible (§3), writing (§2), and shot planning
(§4–7). This is a production companion to `generability.md`, not a new story stage or permission
to generate media. Existing approval gates, canon, narration coverage and profile rules still apply.

## Source and scope

Source: user-supplied Vietnamese video **“Phim AI đẹp không nhờ prompt thần chú — 7 trạm của
creator Trung Quốc”**, 4:47.85, supplied 2026-10-30. Evidence is sampled on-screen text and
burned-in subtitles, not a complete audio transcript. Times below are approximate. **[video]**
means observed advice; **[sn adaptation]** means its application here. Examples are rewritten.
Claims attributed by the video to official model guides have not been independently verified here.
Follow-up evidence: the supplied `*_2-transcription-report.txt` lists 82 flagged entries out of
95 subtitle lines, not the full transcript. Its text supplies the missing end-frame, short-scene
and model-format advice below. Spelling and timestamps may be unreliable; normalize obvious
ASR variants such as Kling/Seedance and seconds, but do not reconstruct omitted lines as quotes.
The limited official-document cross-check in §6 is separately attributed, not verification of
all claims in the video.

| Video station | Approximate section | Owner in this suite |
|---|---|---|
| One-sentence story | 0:20–0:42 | `sn-premise` logline; reuse, do not create a second brief |
| Write in pictures | 0:42–1:08 | `sn-write` `[HÌNH]`, then `sn-shots` |
| Storyboard before generation | 1:08–1:40 | `sn-shots` planning and downstream handoff |
| Lock character | 1:40–2:25 | `sn-bible` identity/reference plan |
| Image first, video second | 2:25–2:52 | `sn-shots` first-state contract and prompt skill |
| Layer the prompt | 2:52–3:32 | downstream prompt skill; shot script supplies facts |
| One camera move | 3:32–4:08 | each continuous shot, or each storyboard subshot |
| Try, revise, edit | 4:08–end | production handoff when assets are actually generated |

## 1. One sentence defines what changes

**[video]** Ask who the protagonist is, what they want, and what blocks them. A robot giving
water to a seed while its own energy runs out illustrates an action, a result and a cost.
**[sn adaptation]** Use the existing logline with why-now/stakes; ensure its key change can be
recognised through actions or objects. Do not compress the whole long-form plot into one clip.
For calm stories, a small desire or a route of discovery is enough; do not manufacture danger,
sacrifice or a villain. For scenery without people, state what the viewer discovers and what
visibly changes between opening and ending.

## 2. Convert inner state into a visible carrier

**[video]** Fear is shown by stopping, stepping back or gripping a hand, rather than only the
label “afraid”; supernatural effects also need visible shape, source and direction.
**[sn adaptation]** Select one readable action appropriate to the beat. Do not reproduce all
three fear actions in one short shot. Keep the intended meaning and the narrator's knowledge.

| Weak image instruction | More useful image instruction |
|---|---|
| Mai is afraid. | Mai stands beside the chair, her closed hand pressed against her jacket. |
| The room feels nostalgic. | Late sun crosses the worn table; the old cup remains beside the empty chair. |
| Magical energy, epic. | A narrow blue glow leaves the pendant and lights the nearby wall. |

These are examples, not new canon: use only objects, powers and actions allowed by the source.
Emotion adjectives may remain in `Cảm xúc`; the corresponding `Cảnh` must carry visible evidence.
In narrated stories, sound or voice may carry what cannot be shown; do not duplicate every feeling
in narration and exaggerated acting. Respect the generability risk/fallback ladder.

## 3. Separate identity canon, reference assets and changing state

**[video]** A production character sheet may show front/side/back views; fixed descriptions
are repeated while actions and shot sizes change. The video discusses Kling's digital actor and
Vidu's reference workflow as tool-specific examples.
**[sn adaptation]** In each recurring character's existing bible entry record:

- **Identity lock:** the verbatim visual signature, readable age/appearance, hair, clothing
  shape/material/colour and distinguishing features already established by canon. A name alone
  is not a face reference. Do not invent facial canon during shot conversion.
- **Changeable state:** expression, pose, position, wetness, damage and props held. Carry changes
  forward. An approved time jump/outfit change gets an explicit variant, not silent identity drift.
- **Reference plan:** face close-up and full-body views in the same outfit; additional views only
  when useful. Record actual paths/attachment IDs and status (`planned`, `provided`, `reviewed`).
  A written description or a planned filename is not an existing image. Missing images do not
  prevent writing the script; tell production what must be prepared before generation.
- **Reference check when images exist:** same face, proportions, hair, wardrobe and style across
  views; one depicted person per separate reference image unless the selected tool expects otherwise.

**Model exception observed around 2:00–2:12:** the video specifically warns that **Seedance 2.0**
may read a multi-view character collage as multiple people and suggests a face close-up plus a
full-body reference instead. A design sheet for the creator is not automatically a suitable model
input. This is a video-reported, version-specific warning, not a universal ban on character sheets
or a current guarantee about Veo, Kling, Vidu or Hailuo. Check the actual selected tool's current
documentation before execution. Do not change the user's model or promise exact identity from text.

## 4. Build the board before generating

**[video]** Individually attractive clips can fail to edit together. Plan images, emotional lighting,
sound and progress before pressing generate; settle aspect ratio and frame rate for production.
**[sn adaptation]** Use existing `Cảnh`, `Hình ảnh` (cinematic), `Máy quay`, `Nhạc`/`Âm thanh`
and `Liên kết`, not a second required shot schema. Pin ratio in STYLE ANCHOR. Record fps only if
known or needed by the renderer; a prompt cannot enforce an export setting. Do not invent fps.

Before downstream prompting, check each shot against:

1. Narrative purpose and exact source beat; visible start state and one end-state change.
2. Cast/reference needs, place, props in hand, orientation and source of light.
3. Shot size/angle and one camera choice; show enough room for that camera path.
4. Mood expressed through motivated light/colour, compatible with the fixed palette and wardrobe.
5. Ambience vs post-production narration, dialogue, music and effects.
6. End-to-start handoff: eyeline/object/screen direction/location transition.

If production tracking is requested, add a compact table **outside** `kich_ban_chNN.md` and
`loi_dan_chNN.md`: `SHOT | needed refs | image status | video status | issue / next change`.
Use `planned`, `generated`, `reviewed`, `accepted` only when true. It is not a new mandatory artifact
or new JSON schema; the checker still validates structural facts, not visual quality.

### Short scenes: recommendation, contract and model limit are different

**[video, report entries 34–35]** One guide is reported to recommend scenes no longer than
eight seconds because later parts of longer generations can degrade, with one main action per scene.
**[sn adaptation]** Eight seconds is a useful planning default, not an experimentally established
quality threshold or universal model maximum. `sn-shots` already has a configurable clip length;
honor the downstream skill's actual contract. Do not silently shorten a requested longer shot or
split it if that changes the approved story, cut count or narration map. For an agreed split, preserve
the action/state handoff, then re-segment and recheck full in-order narration coverage. For a longer
continuous shot, verify selected-tool duration support and recheck motion/narration load.

## 5. Image first, motion second

**[video]** If the input image already fixes the sunset, ground and robot, the motion instruction
can focus on the robot slowly bending rather than redescribing a new landscape.
**[sn adaptation]** In each `Cảnh`, distinguish the **start state** that can be drawn as a still
from the **action → end state** that follows. Do not draw an action's completed result in the
first frame and then ask the video to perform it again. A cup on the table cannot start in the hand.

Downstream image prompt: identity + static start pose + set/props + framing/lens + motivated
light + palette/style. Downstream I2V prompt: attached first frame + identifying context + one
action + one camera choice + modest environmental motion + locked visual conditions + timing/audio.
Repeat the identity/style needed for a standalone line, but do not add competing visual design
or an extra action just to make a longer prompt. Inspect and fix the still before animating it.
`sn-shots` supplies this information in Vietnamese; it does not start emitting English prompt files.

### Optional end frame: same scene, reachable result

**[video, report entries 58–59]** The video mentions Kling's `Add End Frame` control and warns that
very different first/last images can cause a scene jump. The control's name/location is video-reported,
not a promise about the current interface. Check the selected model, mode and actual attachment controls.
**[sn adaptation]** Use an end frame only when supplied/requested and supported; it is not a mandatory
third artifact, and a storyboard's last panel is not automatically an end-frame attachment.

- Compare identity, hair, outfit, set geometry, time/weather/light, props and hands, framing and direction
  between both images. The end pose must be reachable through the planned action and camera path within
  the clip. Similar does not mean pixel-identical: a head turn or small camera displacement should change
  the view while preserving the scene. Do not demand a return to the opening pose unless it is a loop.
- State `first state → one action → target last state` without introducing an extra cut, outfit change,
  day/night switch or different person. If the two references conflict, identify the exact conflict and
  have the incompatible asset corrected or the intended transition clarified. Do not force a morph.
- Example: the same seated woman, same blue jacket/daylit cafe, looking down in the first frame and
  toward the window in the last is compatible with a small gaze turn. A different face in evening wear
  at night is not that shot's final state; treat an intended place/time change as a separate planned shot.
- Describe the desired result if no end image exists; do not invent attachment IDs or claim one is bound.
  If a correction changes the image, check the paired motion and the next shot's start as well.

## 6. Layer instructions without mixing tool dialects

**[video]** Kling is presented as subject + motion + scene, with camera as an added control.
The Seedance example adds camera, light, style and quality. Multi-image examples assign each
image a role. Hailuo is shown with bracketed camera commands.
**[sn adaptation]** These demonstrate information categories, not a required cross-model syntax.
Write concrete composition/light/material instead of relying on “cinematic, masterpiece, 8K”.
If attachments are actually supported, identify which image is the character, location or storyboard.
Use real attachment bindings, not fabricated `@Image1` tokens. An illustrative filename must be
labelled planned. Keep tool-specific commands out of generic shot scripts and Veo prompts unless
the selected tool supports them. Never infer supported reference counts from the video's examples.

### Separate the editing timeline from the selected model's prompt dialect

**[video, report entries 83–85]** Seedance 2.0 is described as using scene labels rather than forcing
seconds into the prompt; Kling 4.0 is described as using time markers. These are video-reported writing
examples, not universal requirements or prohibitions. Keep the approved timing plan independently of
how a renderer accepts controls. A scene-labelled prompt does not itself set an exact clip duration.

| Destination | Adaptation when that destination is actually selected and documented |
|---|---|
| Seedance 2.0, video example | `Scene 1: medium view of the seated character; Scene 2: closer view of the same pose.` Set duration through supported controls; do not discard the editorial timing plan. |
| Kling 4.0, video example | Use supported shot durations/time markers for the same beats, e.g. `0–4s` and `4–8s`; verify mode/API rather than assuming free text enforces timing. |
| Hailuo, video example | Bracketed camera commands are tool syntax; do not copy them into another tool automatically. |
| Existing Veo scene/storyboard skills | Keep their standalone lines, 8-second contract and storyboard timestamps. Video advice about another model does not rewrite these outputs. |

**[official cross-check, 2026-10-30]** Kling's guide describes longer clips and multiple keyframes;
Seedance's launch page describes multi-shot output. Neither establishes the video's exclusive syntax
rules: [Kling guide](https://kling.ai/blog/kling-4-ai-video-model),
[Seedance launch](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0/).
Use these as limited supporting context, not a substitute for the current target mode's prompt/API
documentation. User-selected tool changes require a compatible downstream skill; never merely replace
the model name while retaining incompatible bindings or dropping narration/timing invariants.

## 7. One camera choice per uninterrupted shot; revise one variable

**[video]** Choose one move (push/pull/pan/tilt/follow/orbit/static) rather than stacking moves.
**[sn adaptation]** Calm: a very slow constant-speed move, or locked-off; no easing. Cinematic:
speed serves the source and genre. In storyboard mode, **each subshot** has one choice; cuts
between panels are allowed. Do not impose one continuous camera move on a multi-shot clip.

Weak: “pan, orbit, zoom, then push closer.” Better: “slow push-in toward the seated character;
window light stays steady.” Orbit is a video example, not permission to bypass calm restrictions.

**[video, closing section]** A few finished seconds can require many attempts; change one factor
at a time, then combine voice, effects, music and editing.
**[sn adaptation]** On actual returned media, name one observed defect; locate its cause in
reference/still, action, camera, light or timing. Hold the accepted parts fixed and change only the
causal variable. Wrong face/outfit or missing prop → correct the reference/still first. Good still,
overloaded action → simplify motion. Broken edit → check both adjoining shots, not just one clip.
Do not add blanket negative prompts or silently rewrite story canon to hide a production defect.

Keep accepted frames and versions. If generation is authorized, run only within the user's scope
and budget; stop at an acceptable result, the agreed attempt/budget limit, or a missing decision.
“Many attempts” never authorizes unlimited paid retries. With prompts only, hand over the intended
check and next revision, never claim rendered identity, sound, captions or camera quality was tested.
