---
name: sn-write
description: Stage 4 of the Story Narration suite — write the full Vietnamese narration script of a long story video chapter by chapter in the tagged format ([HÌNH]/[DẪN]/[THOẠI]/[ÂM]/[NHẠC]/[NGỪNG]), designing each scene with an engine card, keeping visuals generable for AI video, hitting runtime, hooks, plants, payoffs and knowledge order, and updating the state card and ledger. Use when the user asks to "viết chương", "viết tiếp", "viết kịch bản chương N", "viết lời dẫn", "continue writing" for an sn project, or to rewrite a chapter.
---

# sn-write — Chapter-by-chapter narration

`{studio}` = the sibling `sn-studio` skill directory.

## Reference gate (before the first chapter of this session — read fully)

`{studio}/references/narration-format.md`, `{studio}/references/scene-craft.md`,
`{studio}/references/characters-and-dialogue.md` (§2–9), `{studio}/references/generability.md`,
`{studio}/references/hooks-and-retention.md`, `{studio}/references/anti-ai-vi.md`,
`{studio}/references/ai-failure-modes.md`. Also read
`bible/narrator.md` (voice sample) every session and `{studio}/references/profiles.md` for the project's
profile. Skipping the gate is not allowed; a previous session's reading doesn't count.

Precondition: outline approved and `sn.py outline` passing (stage `write`). Otherwise → `sn-outline`.

## Scope

- Write only the chapters asked for. "Viết tiếp" = the next unwritten chapter. Default batch 1, at most
  3 per turn. For "write everything", continue in batches of 3 through the requested range, validating
  each batch.
- Never write beyond the outline. If the story needs a structural change, stop and propose it.

## Per chapter

1. **Context pack** (load only what's needed): `state.md`; outline rows N and N+1; the last scene of
   chapter N−1; bible entries for N's cast and locations; ledger promises, knowledge and props touched in
   N. Write down the POV holder, goal, obstacle, what each character knows at the start, the planned end
   state, and **what must not change**.
2. **Constraint lock** (verify at the end): target minutes → **a written syllable target** (rule of thumb
   `minutes × rate × 0.96`; `sn.py duration` prints the exact need). **Underwriting warning** [measured in
   the sn pilot, 2026-09-26]: first drafts written "by feel" came out 16–38% short in 5 of 6 chapters.
   Plan scene lengths in syllables before writing (e.g. 4 scenes × ~230), draft to ~110% of target, then
   measure; the value turn; the choice; the outcome; scenes; plants,
   payoffs, learns/uses/reveals; the end hook; the N−1 hook to answer in the first minute; facts that
   must not break; costs that must carry forward.
3. **Design each scene** with the engine card (scene-craft.md §2): necessity, entry, goal, opposition,
   arena, strategy change, turn, exit. After a setback consider a sequel (reaction → dilemma → decision).
   Pick the arena by "why here, why now" within the approved locations.
4. **Write** `chapters/chNN.md` in the tagged format, Vietnamese:
   - Header with `ch`, `cast`, `mentions`, `plants`, `pays`, `learns`, `uses`, `reveals`, `props` matching
     what actually happens on the page.
   - Ch1 opens on the cold open: a moving image and the hook within the first 3 spoken lines; no greeting
     first. From ch4 on, one spoken re-anchor sentence early.
   - Scenes dramatised in real time at every turn; summary only between turns. Enter late, leave early.
   - Dialogue as action with subtext and agenda; distinct voices and xưng hô; clear attribution.
   - `[HÌNH]` one per 1–3 spoken lines: one moment of common, visible action; signatures and location
     anchors verbatim; no inner states, negative actions, micro-expressions, similes. Unavoidable risky
     images get `(rủi ro cao)` and a fallback.
   - Guard the common AI failures while writing (ai-failure-modes.md): stay in the narrator's POV (C1);
     keep one time frame per scene (C2); no signal lines like "không ai ngờ" (C3); characters misjudge,
     hesitate, act on feeling (D4); real speech is short, dodging, incomplete (D3); give the turning scene
     the most room (A2); every win costs something (F1); **canon lock** — any new name/place/rule/backstory
     goes to `bible/proposals.md` (pending the user's approval), never straight into canon (B2/G4); a
     real-world detail goes to `ledger.realworld` to be verified (G7).
   - `[NGỪNG 1–3]` after reveals and before the final hook. End on the planned hook — an action, line or
     image, never a moral.
5. **Validate** ⛔:
   ```bash
   python3 {studio}/scripts/sn.py duration <dir> --ch N
   python3 {studio}/scripts/sn.py lint <dir>/chapters/chNN.md
   python3 {studio}/scripts/sn.py continuity <dir>
   ```
   Duration outside ±10% → over: cut summary narration and repeated beats first; under: add what the
   story is missing — a sequel beat (reaction → dilemma → decision), a plant a later chapter needs, a
   stronger confrontation, a cost — never scenery or restated feelings. (In the pilot, every shortfall
   turned out to hide a real structural gap.) Lint: apply the anti-AI gates at the reported level;
   fix or knowingly keep each generability flag. Continuity ✗ → fix the chapter, or the ledger if the
   ledger was wrong. Re-run until clean.
6. **Detailed review — MANDATORY after every chapter written or rewritten** — run it by
   `{studio}/references/review-protocol.md` (logic → people → prose; one concern per pass; every finding
   with quote, basis, class; snapshot before prose edits: `sn.py snapshot <dir> --label chNN-edit`, then
   `sn.py changes` and log content changes) ⛔ (user rule, 2026-09-26;
   passing scripts is NOT a review, and a review written from memory is NOT a review):
   - **Re-read the whole chapter from the file**, top to bottom, after all edits — plus the last scene
     of N−1 and every earlier passage the chapter depends on. Inserted fixes must be read in context.
   - Run `python3 {studio}/scripts/sn.py audit <dir>` (cross-chapter repeats, endings, signal lines,
     unregistered names, voice fingerprints, scene-length spread) and read with the checklist in
     `ai-failure-modes.md` (sections B–F for the chapter; A across all chapters written so far).
   - Run the **fact audit** from `sn-review` Step 1b on it: timeline and day counts (solar vs lunar
     dates), numbers and ages, who knows / who did what and how it was physically possible, world rules
     vs the scene, dangling pointed details, narrator never stating a falsehood as fact, kinship terms
     and xưng hô, header vs page.
   - Check craft against the engine card: each scene turns a value, the choice belongs to the
     protagonist, dialogue has subtext and distinct voices, `[HÌNH]` generable, hook lands.
   - Fix every issue found, re-run the three checks, then re-read the changed passages once more.
   - Write `reviews/chNN-review.md`: what was checked (the audit tables in brief, which failure-mode
     items), issues found (quote · basis · class: lỗi rõ ràng / nguy cơ / lựa chọn phong cách) and how each
     was fixed, content changes from `sn.py changes`, **new proposals awaiting approval**, real-world items
     verified, anything left open. Never write "đã review" without this file.
   - After every **3 chapters** and after the **last chapter**, run the full `sn-review` over all written
     chapters (cross-chapter timeline, promises, mechanism, agency) — preferably by a fresh reviewer
     agent that did not write them.
7. **Lock & update** — only approved events go into memory: rewrite `state.md` (≤1.5 KB, template in continuity.md §4); in `ledger.json` mark
   paid promises, add new promises/knowledge/props/facts, set `died_in` if someone died. Keep
   `project.json.stage` = `"write"` (or `"review"` after the last chapter).

## Report (plain Vietnamese)

Per chapter: title, what happened in 1–2 sentences, estimated duration vs plan, the hook it ends on,
**what the detailed review found and fixed** (count + the main items, link to `reviews/chNN-review.md`),
anything the user must decide. One closing line with the running total. After every 3rd and the last
chapter, report the full `sn-review` too.

## Rewrite mode

"Sửa chương N" / "viết lại chương N": read the chapter and its review; state what changes and what must
stay (plants, payoffs, knowledge and facts later chapters rely on). **Change one beat → reread the beats
around it** for positions, objects in hand, who is present (shuohao). Re-run the three checks, do the
mandatory detailed review (step 6) on the rewritten chapter, re-run `sn.py shots` if the chapter has shot
files, and list later chapters affected.
