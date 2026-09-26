# AI failure modes in long-form fiction — prevention and detection

A checklist of the errors AI writers make most often in long stories (compiled 2026-09-26, extended with
a 24-point guide on writing fiction with AI on 2026-09-27) and mapped onto the sn suite. How to run the review
itself (order, evidence, classification, reviewer prompt) is in review-protocol.md. The most dangerous one comes first: **every chapter reads fine but the
whole story doesn't**, because the model optimises the passage in front of it instead of seeing the
story as a whole. Most items below are symptoms of that.

Legend — **Prevent**: the rule applied while planning/writing. **Detect**: `[auto]` = `sn.py` flags it,
`[read]` = only a full read-through finds it (sn-write step 6, sn-review Step 1b/2).

## A. Whole-story blindness

| # | Failure | Prevent | Detect |
|---|---|---|---|
| A1 | Each chapter fine, story as a whole not | Outline first, state card, endgame reserve; write against the outline row, not "what would be nice now" | [read] full-story read in one sitting at the end (sn-review); reverse outline vs plan; [auto] `sn.py audit` cross-chapter repetition |
| A2 | Uniform pacing — key scenes and minor scenes the same length | Budget scene syllables by importance before writing: the turning scene of the chapter gets the most room, connective scenes are summarised | [auto] `sn.py audit` scene-length spread per chapter; [read] does the climax scene breathe? |
| A3 | Every chapter ends the same way ("nhưng cô không biết rằng mọi thứ mới chỉ bắt đầu") | Planned `hook_type` per chapter, never twice in a row; end on an action, line or image | [auto] `sn.py outline` repeated hook types; `sn.py audit` similar chapter endings and stock foreshadow lines |

## B. Continuity and canon

| # | Failure | Prevent | Detect |
|---|---|---|---|
| B1 | Forgotten details — eye colour, age, relationships, places, objects, wounds, time | Everything fragile goes in `ledger.json.facts` / bible the moment it is written; read the state card and the cast's bible entries before each chapter | [auto] `sn.py continuity` (deaths, knowledge, props); `sn.py audit` canon names; [read] fact audit tables |
| B2 | AI invents lore — hometowns, pasts, organisations, new rules | **Canon lock**: the bible is canon. A new name, place, organisation, rule or backstory fact may only enter the page if it is first added to the bible/ledger, and the chapter review lists it as "new canon" for the user | [auto] `sn.py audit` proper names not found in bible/ledger/outline; [read] "new canon" list |
| B3 | World without hard rules — magic/ability limited one scene, limitless the next | Every rule written as rule + cost + exception + reliability in `bible/world.md` before first use | [read] world rules vs every scene that touches them |
| B4 | Power creep (action/fantasy) — hero keeps getting stronger to meet bigger threats | Upgrade ladder with a fixed number of steps and the chapter each unlocks (endgame reserve); raise stakes by cost, relationship and dilemma, not only by power | [read] compare ability and threat level chapter by chapter |
| B5 | Timeline errors — morning becomes night too fast, impossible travel times, wrong day counts | Time and place spoken at each scene change; distances and travel times in `facts` | [read] timeline table with day/time per scene and travel durations |
| B6 | Information a character cannot know | `learns` / `uses` in chapter headers; ask "how does she know?" at every reveal | [auto] `sn.py continuity` (uses before learns); [read] who-knows table |

## C. Point of view and narration

| # | Failure | Prevent | Detect |
|---|---|---|---|
| C1 | POV jumps — telling from A, suddenly inside B's head | Fix the narrator's distance in `bible/narrator.md`. Close third on Lan = only Lan's thoughts; others are shown through what Lan can see and hear | [read] mark every "nghĩ", "thấy lòng", "biết rằng" and check whose head it is in |
| C2 | Tense / time-frame drift | Vietnamese has no grammatical tense, but the frame can drift: pick past-telling ("hôm ấy… đã…") or present-telling ("Lan bước vào…") per scene; flashbacks need an explicit marker in and out | [read] time markers (đã/đang/sẽ, "bây giờ", "hôm ấy") consistent within a scene |
| C3 | Dramatic signal lines — "Anh không hề biết rằng…", "Không ai có thể ngờ…", "Định mệnh sắp thay đổi tất cả" | At most one foreshadowing line per act, concrete ("Về sau Lan mới hiểu, đó là lần cuối…") | [auto] `sn.py lint` / `audit` signal phrases |

## D. Characters

| # | Failure | Prevent | Detect |
|---|---|---|---|
| D1 | Personality changes without cause — cold at first, gushing later | Each change of behaviour must sit on the arc in the bible, with a pressure test, a choice and a visible cost before it; xưng hô changes only at planned turning points | [read] for each principal, compare first and last appearance against the arc; [auto] `sn.py audit` voice fingerprints per chapter |
| D2 | Everyone talks the same (15-year-old, professor, assassin) | voice-words / voice-avoid, sentence length, dialect, xưng hô per character | [auto] `sn.py audit` per-speaker line length and signature words; [read] cover-the-names test |
| D3 | Dialogue too polite, too complete, speech-like | Real people interrupt, dodge, leave things unsaid; keep lines short; subtext and agenda (characters-and-dialogue.md) | [auto] `sn.py audit` long dialogue lines; [read] could half of this line be cut or left implied? |
| D5 | Emotions and relationships move too fast — hostile → in love, suspicion → trust, hurt → forgiveness in one conversation | Build small steps through actions and evidence; after an event show what changed **and what is still unresolved** | [read] list each relationship's steps chapter by chapter |
| D6 | Personality bent to serve the plot — the careful one suddenly reckless because the plot needs a trap | Bible records wants, fears, beliefs and limits; acting against habit needs pressure or experience that explains it | [read] for every out-of-character act, name the pressure |
| D4 | Characters too rational — always know the right move | Give each principal a bias, a misreading and a moment of acting on emotion; the first attempt should be the conservative wrong one (McKee) | [read] where does someone misjudge, hesitate or act on feeling? None → add one |

## E. Prose

| # | Failure | Prevent | Detect |
|---|---|---|---|
| E1 | Repeated phrases — "anh khẽ thở dài", "cô không biết phải nói gì", "một cảm giác kỳ lạ dâng lên trong lòng" | Emotion landing order (anti-ai-vi.md) | [auto] `sn.py lint` stock phrases; `sn.py audit` phrases repeated across chapters |
| E2 | Smooth but soulless — nothing memorable | At least one specific, sensory, era-true detail per scene that could only be in this story (the purple ink, the split third plank of the jetty) | [read] after reading, name one image per scene; can't → add a specific detail |
| E3 | Telling instead of showing — "cô rất buồn" | Action, line, object, consequence (anti-ai-vi.md §2) | [auto] `sn.py lint` emotion-summary phrases; [read] |
| E4 | The same emotion described 3–4 times in a paragraph | One carrier per emotional node | [read] per paragraph: how many times is the feeling named or shown? |
| E5 | Unnatural (translated-sounding) Vietnamese; unstable xưng hô | xưng hô rules per pair **including the conditions for changing them**; read aloud (TTS render) | [read] read-aloud pass; xưng hô table |
| E6 | Padding to hit length; every scene given equal room | Purpose before length: summarise transitions, spend room on choices and consequences; quiet scenes still must develop relationship, mood or understanding | [auto] `audit` scene lengths; [read] |

## G. Process and control (how the AI is directed)

| # | Failure | Prevent | Detect |
|---|---|---|---|
| G1 | Writing before the direction is fixed | sn-premise: genre, protagonist, goal, obstacle, what can be lost, planned ending — before any chapter | stage gates |
| G2 | The whole novel in one request | Staged pipeline; chapters in batches of ≤3; approve key decisions first | stage gates |
| G3 | Too little or too much context | A **context pack** per chapter/scene: relevant rules, character states, bridge from the previous scene, goal, what must not change | sn-write step 1 |
| G4 | AI adds important facts on its own | **Approved vs proposed**: new facts go to `bible/proposals.md`; only user approval moves them into canon | [auto] `audit` unregistered / proposed names |
| G5 | "Make it better" replaces the whole draft — voice, clues, deliberate nuance lost | Narrow edit tasks; `sn.py snapshot` first; `sn.py changes` after, and list content changes | [auto] `changes` flags removed spoken lines |
| G6 | Trusting one AI self-check | Quote + basis + class for every finding; separate passes; fresh reviewer; verify turning points by hand | review-protocol.md |
| G7 | Unverified real-world details (history, geography, administrative names, professions, technology) | Register them in `ledger.realworld` with status verified / unverified / fictional and a source | [auto] `audit` unverified list; web search |

## F. Plot

| # | Failure | Prevent | Detect |
|---|---|---|---|
| F5 | Events strung together without causality — this happens, then that, but no decision leads to a consequence | Every turn written as **cause → choice → consequence** (`cause`/`choice`/`consequence` in outline rows); wrong decisions need a reason from the character's view | [auto] `sn.py outline` missing consequence; [read] causal chain |
| F6 | Rescue by luck or a never-introduced ability | Resources used in a solution must be set up earlier (a promise/setup); limits and costs apply | [read] for each resolution, find the earlier setup |
| F1 | Problems solved too easily, cleanly, without cost | Every win is `yes-but` or paid for; costs carry across chapters (mechanism-and-agency.md) | [auto] `sn.py outline` outcomes, `cost` field; [read] what did this solution cost, and does it carry forward? |
| F2 | Fake foreshadowing — mysterious details never used | Every pointed detail is either a registered promise (P-id) or cut | [auto] `sn.py continuity` open promises; [read] dangling-details table |
| F3 | Unprepared twists — a villain or secret out of nowhere | Twists are knowledge entries (K-id) with at least two earlier traces on the page (`reveals` history) | [read] fair-play check: list the traces before each twist |
| F4 | Ending too perfect — every fate resolved, theme explained aloud | Leave one cost standing and one thread open by design; never state the theme; end on an image | [read] final chapter: what is lost for good? any line that explains the meaning? |

## How to use

- **While writing** (sn-write): keep sections B–E in mind; register new canon before using it.
- **After every chapter** (sn-write step 6): run `sn.py lint` and `sn.py audit`, then read with this
  checklist; the chapter review lists which items were checked and what was found.
- **Every 3 chapters and at the end** (sn-review): section A first — read the whole story in one
  sitting, then the rest. Prefer a fresh reviewer agent.
