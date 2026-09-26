---
name: sn-outline
description: Stage 3 of the Story Narration suite — plan a long narrated story video as acts → chapters (4–7 min each) with value turns, protagonist choices, scene outcomes, mechanism runs and costs, intensity curve, payoffs, plants, locations and chapter-end hooks; validated by sn.py (structural errors vs craft warnings, dramatic or calm profile). Use after sn-bible, or when the user asks to "lập dàn ý", "chia chương", "dàn ý kịch bản truyện dài", "kiểm tra dàn ý", or brings an existing outline to check.
---

# sn-outline — Chapter plan with validated rhythm

`{studio}` = the sibling `sn-studio` skill directory. Read `{studio}/references/profiles.md`,
`{studio}/references/structure.md`, `{studio}/references/mechanism-and-agency.md`,
`{studio}/references/hooks-and-retention.md`, and the payoff section of `{studio}/references/genres.md`.

Precondition: brief and bible approved (stage `outline`).

## Step 1 — Skeleton first (fast version) ⛔

Before any chapter rows, on one screen:
- Act boundaries in minutes (dramatic: `sn.py budget` anchors; calm: the four movements).
- Beat map placed on chapters; the lowest point; the climax set-piece; the final image.
- **Mechanism plan**: which loop runs where, how each run changes state and what it costs, how the loop
  ends (close / remodel / hand over) and what urgency the next loop inherits.
- **Payoff schedule** with ★ intensity (exactly one ★★★★★ in dramatic); **endgame reserve** unlock points.
- **Open-loop plan**: the 2–4 questions alive in each act; the recurring prop's three appearances.
- Opponent defeat order (small → big); the B-story that supplies the Act 3 solution.

Show the user three decisions: **where the biggest payoff lands, what the midpoint turn is, how it
ends** (adaptations: also what was cut and merged). Don't write rows until approved. A wrong skeleton
costs one round; a wrong 45-minute draft costs everything (shuohao).

## Step 2 — Chapter rows in project.json

`project.json.chapters`, ids 1..N in order. Content in Vietnamese:

```json
{
  "id": 1, "title": "Bức thư không người gửi", "minutes": 5, "act": "1",
  "beat": "opening-image, set-up, catalyst",
  "purpose": "Lan nhận thư của người ông đã mất bảy năm; thiết lập nhà bà nội và vết rạn giữa hai bà cháu",
  "turn": "bình yên → bất an",
  "cause": "Bức thư nét chữ ông gọi về trước rằm",
  "choice": "Lan quyết định về quê thay vì gọi điện hỏi bà",
  "consequence": "Bà chối có thư; Lan phát hiện thư gửi từ ngay trong xã",
  "outcome": "no-and",
  "mechanism": "", "cost": "",
  "scenes": ["Phòng trọ Sài Gòn", "Xe khách về quê", "Bữa cơm im lặng"],
  "locations": ["phòng trọ", "nhà bà nội"],
  "intensity": 2,
  "cold_open": "Lan chạy dưới mưa phùn ra hòm thư, ôm lá thư vào ngực; câu hỏi: ai viết thư khi ông đã mất?",
  "plants": ["P01", "P02"], "payoffs": [],
  "hook_type": "revelation",
  "end_hook": "Nét chữ trong thư không phải của ông"
}
```

Required (errors): `title`, `minutes`, `purpose`, `turn`; `cold_open` on chapter 1; minutes sum ±5%;
payoffs after plants. Everything else is craft — the validator warns:
- `end_hook` on all but the last chapter (calm stories may use a soft pull).
- `turn` names the value change; no turn → merge or cut the chapter.
- `cause` → `choice` → `consequence`: every turn is a causal chain; a wrong decision needs a reason from
  the character's point of view. `choice` (dramatic, Acts 2–3) = whose decision causes the turn —
  agency's four questions. Resources used in a resolution must be planted earlier (no rescue by luck or
  by a never-introduced ability).
- `outcome`: `yes` / `no` / `yes-but` / `no-and`; three `yes` in a row = no pressure.
- `mechanism` + `cost` per run; 3+ runs of one mechanism → check each changes state and costs something.
- `locations` within the budget; one-off locations → cut, merge, or reuse a variant.
- `intensity` 1–5 on the four-phase curve (dramatic); peak in the final 30%; midpoint at 40–55%.
- `hook_type` not repeated in consecutive chapters. Every failure in Act 2 teaches the protagonist one
  new thing — say what in `purpose`.
- Register every promise in `ledger.json.promises` with matching `planted` / `payoff`.

## Step 3 — Validate ⛔ (cannot skip)

```bash
python3 {studio}/scripts/sn.py outline <dir> --render
```

Fix every ✗ and re-run until PASS. For each ! either fix it or write down why the story wants it.
Then self-check what the script can't (ai-failure-modes.md A, B4, D4, F1–F4): each twist has ≥2 planned
traces before it; no step on the upgrade ladder skipped (power creep); at least one chapter where a
principal misjudges or acts on emotion; no problem solved without cost; one loss stands at the end and
the theme is never stated; every scene can turn a value; opponents act rationally; no
coincidence resolves the climax; no endgame card played early; the final image mirrors the opening.

## Step 4 — Approval ⛔

Show the rendered `outline.md` (or a compact version) with the intensity curve. Ask the user to read the
whole outline before writing starts. On approval set `stage` = `"write"` → `sn-write`.

## Check mode (existing outline)

Convert the user's outline into `project.json.chapters` (mark unknown fields and ask), run the validator,
report in plain language without rewriting unless asked.

## Upstream changes

After merging characters, moving payoffs, or changing runtime: update rows and ledger, re-run
`sn.py outline` and `sn.py continuity`, and list the written chapters affected.
