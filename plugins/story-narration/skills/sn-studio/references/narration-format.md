# Narration script format (chapter files)

The tag format is an sn design. The "structured lines, not prose" principle comes from shuohao `novel-script` (every line = speaker + text + delivery, every action its own beat, so runtime, TTS and shots can be derived deterministically).

Every chapter lives in `chapters/chNN.md` (two-digit, 1-based). The format is line-tagged so
`sn.py` can time it, lint it, export a TTS file, and so `sn-shots` can cut it into shots.
Output language of the story text is **Vietnamese** unless the brief says otherwise; tags stay as below.

```markdown
# Chương 03 — Chiếc hộp gỗ dưới gầm giường
<!-- sn: ch=3 cast=lan,ba-noi mentions=ong-noi plants=P04 pays=P01 -->

## Cảnh 1 — Gác xép nhà bà nội · chiều mưa
[HÌNH] Gác xép thấp, mái tôn loang lổ. Lan quỳ cạnh chiếc giường sắt cũ, đèn pin trong tay.
[ÂM] Mưa gõ đều trên mái tôn.
[DẪN] Chiều hôm ấy mưa từ trưa chưa ngớt. Lan leo lên gác xép, chỉ định tìm cái quạt cũ cho bà.
[DẪN] Cô không ngờ dưới gầm giường lại có một chiếc hộp gỗ, khóa bằng sợi dây đồng đã xỉn màu.
[THOẠI: Bà nội | gọi vọng lên, hơi gắt] "Lan ơi, đừng động vào đồ trên đó!"
[NGỪNG 2]
[DẪN] Nhưng Lan đã mở nắp hộp.

## Cảnh 2 — ...
```

## Tags

| Tag | Spoken? | Meaning |
|---|---|---|
| `[HÌNH] …` | no | What the viewer sees. One concrete, filmable image per line; feeds `sn-shots`. |
| `[DẪN] …` | yes | Narrator voice-over. The backbone of the video. |
| `[THOẠI: Tên \| cách nói] "…"` | yes | A character's line, voiced by the narrator in character or a second voice. `Tên` = the character's display name from the ledger, or `VO` for an inner voice. |
| `[ÂM] …` | no | Diegetic sound / SFX cue. |
| `[NHẠC] …` | no | Music direction (mood, swell, drop, silence). |
| `[NGỪNG n]` | no (timed) | Deliberate silence of n seconds (breath after a reveal, chapter break). |

Rules the scripts enforce or rely on:

- Every non-empty body line starts with a tag. `## ` lines are scene headings (`## Cảnh k — địa điểm · thời điểm`). The `# ` line is the chapter title.
- The header comment is mandatory: `ch` (matches file number), `cast` (ledger ids of characters physically present), optional `mentions` (dead/absent characters remembered), `plants` / `pays` (promise ids), `learns` / `uses` (`who:K01` knowledge), `reveals` (K ids the audience learns), `suspects` (`who:K01` guesses), `props` (X ids), optional `pov` (whose
  point of view the chapter holds; a scene may override it in its heading: `## Cảnh 2 — Bến phà · chiều · POV: Minh`).
  See continuity.md.
- Numbers inside `[DẪN]`/`[THOẠI]` are written as words (TTS reads digits badly).
- A spoken line is one breath group: ideally 8–25 syllables per sentence, hard ceiling 40.

## Narrated-story craft specific to this format

- **Listen-first.** Many viewers listen with the screen off. All plot information must be in `[DẪN]`/`[THOẠI]`; `[HÌNH]` only illustrates. Never rely on a visual to carry a clue.
- **Narrator ≠ camera.** The narrator may compress time ("Ba năm sau…"), foreshadow ("Về sau Lan mới hiểu…"), and interpret, but should *show* key scenes in real time with dialogue and sensory detail. Rule of thumb: summary for connective tissue, scene for every turn.
- **Dialogue budget.** Around 15–35% of spoken syllables as `[THOẠI]` usually keeps it a story rather than an essay (a starting point, not a rule). Keep exchanges short (2–6 lines) and always attribute clearly — the ear cannot see quotation marks; a line from an unnamed speaker needs "bà nói", "hắn cười khẩy" in the narration or the tag's delivery note.
- **Names over pronouns.** Re-anchor names every few sentences and after any scene change; limit to ≤5 principal named characters in a 30–60 min story (≤7 for 90 min).
- **Time and place cues** at every scene change, spoken ("Sáng hôm sau, ở bến xe Miền Đông…"), not only in the heading.
- **Visual density.** Aim for one `[HÌNH]` per 1–3 spoken lines, so each 8-second clip has something to show (≈24 syllables of speech per 8 s clip at 180/min).
- **Generable visuals.** Every `[HÌNH]` is one moment of common, visible action — no inner states, negative actions, micro-expressions or similes. Rules in generability.md; `sn.py lint` flags the usual offenders.
- **Pauses are structure.** Put `[NGỪNG 1–3]` after reveals, before chapter-ending hooks, and at chapter breaks. They count toward runtime.
