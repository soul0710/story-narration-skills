# Review protocol — order, evidence, and the reviewer prompt

From the guide "Những điều cần tránh và giải pháp khi viết truyện bằng AI" (2026-09-27), merged
with story-skills' named revision passes and drama-skills' rule classes.

## 1. Priority: logic before people before prose

Fix in this order, and never polish prose in a passage whose logic is still wrong:
1. **Logic & consistency** — canon, timeline, cause → choice → consequence, who knows what.
2. **Characters, POV & pacing** — motives, voice, emotional steps, where the room goes.
3. **Prose** — repetition, clichés, rhythm, natural Vietnamese.

A beautiful paragraph never compensates for a character acting without reason or a story that
contradicts itself.

## 2. Separate passes (one concern per pass)

| Pass | Checks | Tools |
|---|---|---|
| 1. Canon & time | contradictions with bible/ledger/state card; timeline, day counts, travel times; numbers | `sn.py continuity`, `audit`; timeline table |
| 2. Causality & resolution | each turn = cause → choice → consequence; wrong decisions have reasons from the character's view; no rescue by luck or a never-introduced ability; resources used in the solution were set up earlier | outline `choice`/`cause`/`consequence`; promises |
| 3. POV & knowledge | whose POV each scene holds; limited POV tells only what that person sees, remembers, knows or guesses; who knows what — from where — since when — how sure | chapter header `pov`, `learns`/`suspects`/`uses`/`reveals` |
| 4. Character, emotion & voice | behaviour fits wants/fears/beliefs/limits, or pressure explains the change; relationships move in steps (hostile → trust is not one conversation); voice profile; xưng hô per pair | `audit` voice fingerprints; bible |
| 5. Promises & new facts | every pointed detail tracked (planted – meaning – planned payoff – status); twists designed backwards from the truth and re-read in that light; **no new fact enters canon unapproved** | ledger promises; `audit` canon/proposals |
| 6. Prose & rhythm | repetition of words *and* meaning; clichés; ornate but empty lines; uniform scene length; same-shaped chapter endings; unnatural (translated-sounding) Vietnamese — read aloud | `lint`, `audit`; TTS read-aloud |
| 7. Real-world facts | history, geography, administrative names (e.g. communes merged on 01/7/2025), professions, technology the plot leans on | `ledger.realworld` + `audit`; web search |

## 3. Evidence rules for every finding

- **Quote the exact passage** (chapter:line) — no quote, no finding.
- **State the basis**: the bible/ledger entry, the earlier line, the timeline row, or the real-world source.
- **Impact** on the viewer/listener in one sentence.
- **Minimal fix**: the smallest change that repairs it. Never add new facts or change a character's
  motive to fix a flaw — if that is the only fix, raise it as a question for the user.
- **Classify**: `lỗi rõ ràng` (clear error) / `nguy cơ cần xem xét` (risk to consider) /
  `lựa chọn phong cách` (style choice — keep unless the user wants otherwise).
- **Don't invent errors to fill a quota.** If context is missing, write `chưa đủ dữ kiện` and name the
  missing data.
- Keep creative suggestions separate from approved information.

Telling, long sentences, metaphors and open endings are **not errors by themselves** — the question is
whether they serve the scene. Banning a technique outright makes prose mechanical in a different way.

## 4. AI self-review is a proposal, not a verdict

- One pass of the writer checking itself is not enough (the pilot proved it twice). Prefer a **fresh
  reviewer** that did not write the text; if subagents are available, send the reviewer prompt below.
- Verify each finding against the text before fixing; reject findings that "fix" something correct.
- Cross-check every turning point by hand.
- Final rule: **an AI suggestion never becomes story truth automatically.** New facts go to
  `bible/proposals.md`; only the user's approval moves them into canon.

## 5. Versions and content change logs

- `sn.py snapshot <dir> --label <why>` before any multi-line edit, revision pass, or "make it better" request.
- Give edit tasks **narrow scopes** (cut repetition / tighten this dialogue / clarify this action), never
  "rewrite it better" over a whole chapter.
- After editing, `sn.py changes <dir>` and record **content changes** in the review (facts, clues,
  motives, voice) — not only wording. Removed spoken lines are flagged so lost clues surface.

## 6. Reviewer prompt (Vietnamese) — for a fresh reviewer agent

```text
Bạn là biên tập viên cho bản thảo dưới đây. Chỉ phân tích và đề xuất; KHÔNG viết lại chương.

DỮ LIỆU (đọc từ file trong thư mục dự án):
- Hồ sơ truyện đã duyệt: bible/characters.md, bible/world.md, bible/narrator.md, ledger.json
  (bible/proposals.md là ĐỀ XUẤT, chưa phải canon)
- Dòng thời gian và trạng thái trước chương: state.md (bản trước chương), outline.md
- Nhân vật biết gì ở đầu chương: header các chương trước (learns/suspects/reveals)
- Mục tiêu của chương: dòng tương ứng trong project.json.chapters
- Bản thảo cần kiểm tra: chapters/chNN.md (và các chương liền trước nếu cần đối chiếu)

Kiểm tra theo thứ tự, mỗi lượt một mối quan tâm:
1. Mâu thuẫn với hồ sơ truyện, thời gian và trạng thái nhân vật.
2. Quan hệ nhân quả, động cơ, cách giải quyết xung đột (có nhờ may mắn/năng lực mới không?).
3. Điểm nhìn và thông tin nhân vật chưa thể biết.
4. Diễn biến cảm xúc, tốc độ thay đổi quan hệ, giọng đối thoại, xưng hô.
5. Chi tiết đã gieo, lời hứa với người xem, tình tiết/sự thật mới phát sinh ngoài hồ sơ.
6. Lặp từ và lặp ý, diễn đạt sáo, nhịp kể, tiếng Việt thiếu tự nhiên.
7. Chi tiết đời thực cần kiểm chứng (địa danh, lịch sử, nghề nghiệp, thủ tục).

Với mỗi vấn đề:
- Trích nguyên văn đoạn liên quan (chương:dòng).
- Nêu căn cứ; chỉ rõ thông tin đối chiếu.
- Giải thích ảnh hưởng đến trải nghiệm xem/nghe.
- Đề xuất cách sửa ít làm thay đổi bản thảo nhất.
- Phân loại: lỗi rõ ràng / nguy cơ cần xem xét / lựa chọn phong cách.

Không bịa lỗi để đủ số lượng. Khi thiếu ngữ cảnh, ghi "chưa đủ dữ kiện" và nêu dữ kiện còn thiếu.
Không tự thêm sự thật mới hoặc đổi động cơ nhân vật để sửa lỗi.
Tách các đề xuất sáng tạo khỏi thông tin đã được duyệt.
```

## 7. Per-chapter workflow (from the guide)

1. **Prepare** — POV holder, goal, obstacle, what each character knows, the planned end state
   (the context pack: relevant rules, character states, bridge from the previous scene, goal, and what
   must not change).
2. **Draft** within the agreed scope.
3. **Structural check** — logic, information, motive, time, planted details. Fix these first.
4. **Prose edit** — rhythm, dialogue, repetition, voice; snapshot before big changes.
5. **Lock & update** — only approved events go into the bible/ledger/state card; then write on.

After each stretch (every 3 chapters), read **several chapters in a row** to check relationship arcs,
overall rhythm, and mystery progress — not just each chapter alone.
