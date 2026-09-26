# Hooks and retention for 30+ minute narrated videos

Merged from short-drama `hook-design` / `opening-rules`, oh-story `long-chapter-hooks` and
`long-suspense`, and shuohao's "cold open must pay the hook within the first 3 beats" gate.

## Cold open (first 45–90 s)

The hook is not a label, it is the **first beats**. Pick one:

| Template | Shape (narration) |
|---|---|
| Flash-forward | Start at the most charged moment, then "Nhưng để hiểu vì sao…, phải quay lại ba tháng trước." |
| Impossible fact | "Bức thư đến vào sáng thứ Hai. Người ký tên đã mất được bảy năm." |
| Extreme situation | Protagonist already trapped / humiliated / out of time. |
| Direct promise | Narrator states the question the video answers — concrete, not generic ("Đây là câu chuyện về…" alone is not a hook). |
| Contrast | Two images side by side (wedding banquet / hospital corridor). |
| Rule that must break | "Nhà họ Trần có một quy định: không ai được mở căn phòng cuối hành lang." |

Checklist: a specific person, a specific problem, a question the viewer needs answered, within 3 spoken
lines (shuohao: the hook must land in the first 3 beats). No weather-only openings, no "Xin chào các bạn"
before the hook. **The first image moves** (shuohao): running through fog clutching the case, not a static
close-up of white knuckles. **Event density** (oh-story): the first ~100 syllables should contain 2–3
things *happening* ("Ngày ông mất tròn bảy năm, Lan nhận được thư của ông. Chị gọi về cho bà. Bà cúp máy.").

## Chapter-end hooks (every chapter except the last)

| Type | Formula | Example (vi) |
|---|---|---|
| Revelation | Drop a fact that changes everything | "Ngày ghi trên thư là bảy ngày sau khi ông mất." |
| Crisis | A threat the next chapter must answer | "Tiếng bước chân dừng lại ngay trước cửa." |
| Interrupted action | The act is cut by a new variable | "Cô vừa chạm vào tay nắm, thì có ai đó giữ chặt cổ tay cô." |
| Identity twist | Identity departs from expectation | "Hồ sơ ghi: Nguyễn Thị Lan — đã qua đời năm 1998." |
| Dilemma | Two bad options | "Ký thì giữ được căn nhà. Nhưng mẹ cô sẽ phải ra đi." |
| Mystery object | Important object, meaning unknown | "Trong hộp chỉ có một chiếc chìa khóa và mẩu giấy: 'Con nợ bà.'" |
| Countdown | Not enough time | "Bác sĩ nói còn ba tháng. Đó là chuyện của hai tháng trước." |
| Threat / promise | Someone declares intent | "Trước nửa đêm, tôi sẽ cho cả làng biết cô đã làm gì." |
| Hidden meaning | Innocent line with a buried contradiction | "'Con giống em gái con ghê.' Nhưng Lan là con một." |
| Echo | Last line repeats an earlier line, one detail changed | |
| Silent reaction | Show the reaction, withhold the cause | "Ông đọc thư. Mặt tái đi. Ông gấp lại, không nói một lời." |
| Emotional cut | Cut at the peak of feeling (confession interrupted, tears) | |

Rules:
- Never use the same hook type in two consecutive chapters (`sn.py outline` warns).
- Reversal hooks ≤ 5–7 per video, each must be set up earlier (fair play).
- The next chapter must answer or advance the hook within its first minute — never ignore it.
- Payoff chapters (big reveals) still end with a new question: "resolve one, open one".

## Chapter-start hooks

Suspense dialogue; flash-forward fragment ("Về sau Lan mới biết, cuộc gọi ấy đã thay đổi tất cả. Nhưng lúc
này…"); countdown; mysterious monologue; contrast; action in progress; ominous image.

## Retention rhythm inside a long video

Items below marked [sn] are heuristics for YouTube narration, not from a source.

- **Open loops ledger.** Keep 2–4 unanswered questions alive at all times. Close one only after opening
  another (oh-story "expectation relay").
- [sn] **Re-hook every 3–5 minutes**: a new question, a reveal, a reversal, a promised event ("Đêm đó, điều bà
  sợ nhất đã xảy ra.").
- **Reader foreknowledge**: tell the viewer something the character doesn't know to create dread
  ("Cô không biết rằng…" — use sparingly, it is also an AI-ism when overused).
- **Suspense vs. surprise**: suspense (viewer knows the bomb is there) holds attention longer than surprise.
- [sn] **Recap lines after breaks**: at the start of chapters 4+ add one spoken sentence that re-anchors the
  situation for viewers who drift ("Ba ngày sau khi tìm thấy chiếc hộp, Lan vẫn chưa dám hỏi bà.").
- Expectation beats payoff: the build-up to a payoff should be longer than the payoff.
