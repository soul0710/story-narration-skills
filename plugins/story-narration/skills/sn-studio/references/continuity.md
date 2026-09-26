# Continuity: ledger, three layers of truth, state card

Sources: story-skills `revision-continuity` and `chapter-writing` (deterministic checks: dead characters
walking, payoffs before setups; `knowledge-state`, `object-state`), oh-story file-based memory (capped
context card), drama-skills (world truth / character belief / audience knowledge kept apart; scene
handoff capsule), long-video-scriptwriting fiction.md (same three-layer rule).

## 1. Three layers of truth [src]

Keep separate — most long-story breakages come from mixing them:

| Layer | Where recorded | Question |
|---|---|---|
| **Author truth** | `ledger.json.knowledge[].fact` | What is actually true in the story world? |
| **Character belief** | chapter headers `learns=who:K01` (knows), `suspects=who:K01` (guesses), `uses=who:K01` (acts on it) | What does each character know or suspect *now* — from where, since when, how sure? |
| **Audience knowledge** | chapter headers `reveals=K01` | What has the viewer seen/heard so far? |

A twist is fair only if its necessary traces appeared before the answer. When you change a reveal,
re-check every later scene that uses that information. Wrong beliefs are knowledge entries too
(`"fact": "Lan tin rằng ông mất vì bệnh (thật ra không phải)"`).

## 2. ledger.json

```json
{
  "characters": {
    "lan":     {"name": "Lan", "role": "protagonist", "status": "alive", "died_in": null,
                "signature": "cô gái 28 tuổi, tóc buộc thấp, áo khoác len màu rêu", "xung_ho": "gọi bà là 'bà', xưng 'con'"},
    "ong-noi": {"name": "Ông nội", "role": "ghost", "status": "dead", "died_in": 0}
  },
  "promises": [
    {"id": "P01", "type": "mystery", "desc": "Ai gửi bức thư?", "planted": 1, "payoff": 6, "status": "open"}
  ],
  "knowledge": [
    {"id": "K01", "fact": "Bức thư do bà viết, giả nét chữ ông"}
  ],
  "props": [
    {"id": "X01", "name": "chìa khóa đồng", "function": "mở căn phòng khóa; chứng cứ bà giữ bí mật", "recurring": true}
  ],
  "facts": [
    {"ch": 2, "fact": "Bà nội đau chân trái, không leo được cầu thang"}
  ],
  "realworld": [
    {"item": "Chợ nổi Cái Răng đông nhất 4–6 giờ sáng", "status": "verified", "source": "…"},
    {"item": "Tên xã trên con dấu bưu điện", "status": "fictional", "note": "không nêu tên xã thật (sáp nhập 01/7/2025)"}
  ]
}
```

- `died_in: 0` = dead before the story starts (may only appear in `mentions`).
- Promise types: `mystery`, `chekhov` (object/skill that must be used), `threat`, `bond`, `setup`.
  Status `open` → `paid` (or `dropped` with a recorded reason).
- `props`: narrative props only (≤ 8; test in generability.md §7). `recurring: true` → rule of three.
- `facts`: fragile facts — ages, dates, injuries, distances, money.
- `realworld`: real-world details the plot leans on; status `verified` (with source) / `unverified` /
  `fictional` (deliberately invented). `sn.py audit` lists the unverified ones.

**Approved vs proposed.** `bible/*.md` + `ledger.json` = approved canon. `bible/proposals.md` = facts the
writing invented (new names, places, backstory, rules) awaiting the user's approval. `sn.py audit` reports
names that are on the page but only proposed, and names that are nowhere.

## 3. Chapter header

```
<!-- sn: ch=5 pov=lan cast=lan,ba-noi mentions=ong-noi plants=P04 pays=P01 learns=lan:K01 suspects=lan:K03 uses=lan:K02 reveals=K01 props=X01 -->
```

`sn.py continuity` errors on: unknown cast/promise/knowledge/prop ids; anyone appearing after `died_in`;
payoffs without earlier plants; promises due in a written chapter but unpaid; open promises when the final
chapter exists; a character acting on knowledge before learning it (a warning if they only suspect it). Warns on: speakers not in the cast,
> 8 props, recurring props seen < 3 times.

## 4. State card (state.md, ≤ 1.5 KB, rewritten after every chapter)

Only what the next chapter would get wrong without it [src: oh-story, drama-skills handoff capsule]:

```
## Sau chương 5
- Vị trí & thời gian: Lan ở nhà bà, tối thứ Bảy, mưa.
- Nhân vật: Bà giận Lan, chưa nói chuyện; Minh rời làng sáng nay.
- Ai biết gì — từ đâu — khi nào — chắc mức nào: Lan biết thư không phải nét chữ ông (K02 — tự so với sổ của ông, ch3, chắc chắn); Lan nghi bà giấu gì đó (K03 — thấy bà ra bến mỗi chiều, ch4, mới là nghi); bà chưa biết Lan đã đọc. Khán giả biết thêm K01.
- Trong tay ai: chìa khóa đồng (X01) trong túi áo Lan.
- Câu hỏi đang mở: P01, P04. Chi phí chưa trả: Lan đã nói dối bác Tư.
- Sắp phải trả: P02 ở chương 7.
- Cảnh tiếp theo cần: chức năng + trạng thái ra dự kiến.
```

Before writing chapter N read: state.md, outline rows N and N+1, the last scene of N−1, bible entries for
N's cast only. The capsule helps attention; when it disagrees with the chapter text, the text wins.

## 5. Revision passes (big → small) [src: story-skills]

structure → character → continuity → pacing → line (anti-AI) → proof. Never polish sentences a structural
pass may cut. Snapshot before multi-chapter passes (copy the project folder or commit in git).
