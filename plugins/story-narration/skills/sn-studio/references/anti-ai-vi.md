# Removing the "AI voice" and template feel from Vietnamese narration

Sources: oh-story `story-deslop` (7 gates, minimal change, deletion caps) and `writing-craft.md` §1
(emotion landing order); drama-skills `anti-template-repair.md` (four diagnostic layers, over-explaining,
over-closing, uniform density, costs settled immediately). **The Vietnamese phrase lists in `sn.py lint`
are an sn experiment, not from a source corpus** — treat hits as prompts to reread, not verdicts.

## 1. Principles [src: oh-story]

1. **Change the flavour, not the facts.** Keep plot, clues, hooks, character beats, names, numbers.
   Never delete a paragraph wholesale; rewrite sentence by sentence. Deletion caps: light ≤15%, medium
   ≤25%, heavy ≤35%. Unsure → mark `[cần xem lại]` rather than delete.
2. **Smallest edit, biggest effect.** A word before a sentence, a sentence before a paragraph.
3. Don't promise any detector score. Don't add typos or scramble punctuation to "look human".

## 2. Emotion landing order [src: oh-story writing-craft §1]

At an emotional node, take the first that applies — only one:
1. Context already makes it clear → add nothing.
2. The emotion changes what happens next → write the choice, line, tactic, cost.
3. An object in the scene can carry the change (the contract, the medicine, the rice going cold) — only
   objects already in the scene.
4. The body is really affected (fails, hurts, loses balance) → write the consequence.
5. A plain statement is truest and cheapest ("Bà mệt rồi.") → say it.

Four anti-cliché questions: remove the body detail — is anything lost? Would it work with another name in
another room (then it's generic)? Is the chapter repeating "body part + tiny motion" (fingertips,
knuckles, eyes, lips, breath)? Is the same emotion explained twice?

## 3. The 7 gates [src: oh-story, adapted to Vietnamese]

| Gate | Symptom | Fix |
|---|---|---|
| A. Stock phrases | "không khỏi", "bất giác", "khẽ mỉm cười", "ánh mắt thoáng qua một tia…", "hít một hơi thật sâu", "trái tim như thắt lại", "thời gian như ngừng trôi", "một cảm giác khó tả", "len lỏi", "vỡ òa" | Delete, or replace with the character's actual action |
| B. Formula syntax | "Không phải A, mà là B"; "không chỉ… mà còn…"; triple parallels; stacked dashes; "Và rồi," openings | State B directly; break the triad |
| C. Emotion summaries | "Nỗi buồn tràn ngập trong lòng cô." | Landing order above |
| D. Uniform rhythm | Paragraphs all the same length; CCTV-style action lists | Compress climaxes, expand dread |
| E. Dialogue tags / tone | Every line "cô nói nhẹ nhàng"; everyone polished | Attribute by action; voice-words, xưng hô |
| F. Moralising endings | "Suy cho cùng, hạnh phúc đôi khi chỉ là…" | End on an image, action, or line |
| G. Explaining narrator | "Cô không biết rằng…" every chapter; explaining subtext just shown | ≤1 foreshadow per chapter; trust the listener |

Severity (from `sn.py lint`, stock phrases per 1000 syllables): light ≤2 → A+B; medium ≤6 → A–D+G;
heavy >6 or 4+ gates failing → all 7 and rewrite the worst scenes. These thresholds are sn guesses.

## 4. Template feel beyond wording [src: drama-skills]

Report only with two or more cited locations and the concrete loss.

- **Causal repetition** — every round solved by a stranger's answer, coincidence, or the opponent
  confessing.
- **Strategy repetition** — everyone argues accuse → deny → louder; nobody has their own leverage.
- **Over-explaining** — action or line already shows the choice, then a sentence translates it.
- **Over-closing** — every scene sealed with a summary or a quotable line, so the next scene must
  re-create pressure from zero.
- **Over-neatness** — every exchange paired with the same-length micro-gesture; every scene ends on the
  same rhetorical shape.
- **Uniform information density** — every beat carries the same amount of new information, so nothing
  feels like an *event*. Put scene beats side by side: a few should be free, one should hit hard.
- **Costs settled immediately** — every cost created in a chapter is paid off in the same chapter; nothing
  accumulates. List costs and the chapter where each lands.

Not template: intentional ritual, comic callbacks, a character's verbal tic, dialect, genre conventions
used once.

Fix by changing mechanism, not synonyms: give the character a choice that costs something instead of a
second piece of evidence; give each side different leverage instead of louder lines.

## 5. Natural Vietnamese spoken narration [sn]

- Everyday comparisons from the characters' world, rare and specific ("gầy như que củi"), not literary.
- Particles and colloquial rhythm in dialogue ("mà", "chứ", "hả", "thôi", "đi", "cơ", "đấy") per region.
- Ellipsis of the obvious; concrete time/place markers ("mùa gặt năm ấy").
- Chapter endings: action or dialogue, not reflection.
