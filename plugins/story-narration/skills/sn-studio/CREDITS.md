# Credits

The sn-* suite is an original synthesis written for narrated long-form story videos. Methods and ideas
were distilled (not copied wholesale) from these open-source projects; their licenses are in `licenses/`.

| Project | License | What was adapted |
|---|---|---|
| [0xsline/short-drama](https://github.com/0xsline/short-drama) | MIT | staged commands (start/plan/characters/outline/episode/review), four-phase rhythm curve, five hook types, satisfaction matrix, four-tier villain system, 5-dimension review scoring, opening templates |
| [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | Apache-2.0 | deterministic duration per episode, structured lines not prose, cold-open-in-first-3-beats + hook in motion, common-actions-only rule for AI video, generation-difficulty warnings, location cap formula and reuse plans, narrative-prop collapse test and cap, concrete era, surface condition, crowd plans, revision "change one beat, reread three", two-round skeleton approval with source evidence |
| [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills) | MIT | rule classes (structural vs reviewed vs craft vs taste; numbers are not quality proof), scene engine card, mechanism loops and exhaustion, agency (STY-13) and device contracts (STY-17), generability rewrite ladder, anti-template diagnostics, world truth / belief / audience knowledge, handoff capsule, continuity locks |
| [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) | MIT | file-based memory with a capped context card, chapter hook catalogues, expectation relay and expectation debt, endgame reserve, agency four questions, emotion landing order, recurring prop rule of three, numbers as narrative tools, dialogue power games and agenda, opening event density, de-AI gates and deletion caps |
| [jtydhr88/screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills) | MIT | structure synthesis (Field, Snyder, McKee, Hoxter, Hicks, Lu Jun), scene design five steps and checklist, location/props/details/suspense craft, dialogue as action, exposition as ammunition, McKee's four flaw families, dialogue checklist |
| [danjdewhurst/story-skills](https://github.com/danjdewhurst/story-skills) | MIT | promise/payoff and death-order checks, knowledge-state, scene outcomes (yes / no / yes-but / no-and) and scene–sequel, named revision passes, audiobook runtime estimation, voice-words / voice-avoid |

Apache-2.0 notice (shuohao-skills): portions of the methodology are derived from that work; no source
files were copied. Changes: rewritten in English for Vietnamese narrated video, merged with the other
methods above, and re-implemented checks in Python.

sn's own contributions (marked [sn] in the references): the tagged narration format, Vietnamese
listenability rules, the experimental Vietnamese AI-phrase lists, the speaking-rate measurement, the
calm profile (a four-movement structure for contemplative storytelling), and chapter-sizing defaults.
