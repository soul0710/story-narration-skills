# Mechanism loops, protagonist agency, and expectation economy

For long stories the danger is not a bad scene but a **thin middle**: the same trick repeated, a
protagonist carried by others, big cards spent too early. Sources: drama-skills
`short-drama-develop/mechanism-loop.md` and review rubric (STY-13, STY-17), oh-story
`reader-contract-and-progression.md` and `writing-craft.md` (recurring prop), jtydhr88 (prop chain).

## 1. Mechanism loops [src: drama-skills]

Between the story engine and the chapters sits a layer that is often skipped: a stretch of story is
usually **the same mechanism run several times** (she exposes a liar with evidence; the ghost punishes a
broken rule; he uses future knowledge to dodge a disaster). Half the pleasure is the mechanism; half is
"I know how this works — I'm waiting for it to run again".

- **Demonstrate the first run completely, even slowly.** Until the viewer understands the mechanism,
  later runs are just events.
- For each run record: who uses which known advantage; what the opponent acts on (opponents are not
  stupid — they act rationally on what they know); what the audience knows in advance; **what state
  changes**; **what it costs** the protagonist. A free loop exhausts fastest.
- **Run vs. repeat test**: shuffle the runs — is anything lost? If not, they are repeats.
  Checkable differences: the opponent's awareness (none / suspects / knows someone / knows who), the
  difficulty, the conditions where it still works, who has now seen it, which retreat is now closed.
- **Fix repetition by changing the vector, not the target.** Keep what the audience is tracking ("does she
  really own it?"); answer with a different kind of proof and a higher threshold. Changing to an unrelated
  new event removes repetition but snaps the line the viewer follows.
- **Exhaustion symptoms** (two or more → act): the audience predicts the outcome; payoffs get bigger in
  scale but smaller in state change; you need more humiliation / more money / more witnesses to keep
  intensity; **the opponent has to act dumber than they should** (the root cause — it kills trust).
- **A loop with no destination always exhausts.** Give it something concrete that can be finished ("make
  the village publicly correct the record" beats "become strongest").
- **Ending a loop**: close it (a run that can't be repeated — the mechanism is exposed or the cost lands
  on the protagonist), remodel it (change one premise: scope, cost, who knows, who bears risk), or hand it
  over (another character uses it; the viewer's side flips). Never just open a new loop beside the old one.
- **Hand over the urgency**: the new loop must inherit the deadline, the reason the protagonist can't
  quit, and the stakes the viewer already bet on. Test: "if she does nothing this round, what happens?" —
  the answer must be more concrete and worse than last time.
- **Bury the next loop inside this one**: let what the next loop needs appear once in a minor role (an
  unexplained person, a document set down). Leave a short low-pressure stretch between loops to let the
  last payoff land.

Record in `project.json.chapters[].mechanism` (loop name) and `cost`; sn.py warns when a loop runs 3+
times and asks you to check state change and cost per run.

## 2. Protagonist agency [src: oh-story, drama-skills]

At every key node ask the four questions (answers may point to another promised owner in ensemble or
mentor stories):
1. Who decides why/how this happens?
2. Who makes the irreplaceable choice?
3. Who bears or chooses the consequence?
4. Who receives the payoff (gain, recognition, power)?

- A protagonist who only endures until rescue is the episode's audience, not its lead (drama-skills
  STY-13). If a result arrives by outside force, cite the protagonist's earlier action that made it arrive
  now and what they do with it.
- Helpers may execute parts; they must not silently take the payoff. Witnesses' reactions amplify a
  payoff; they never replace it.
- Core assets (the secret, the evidence, the special ability) are never handed over for free — only in a
  visible exchange.
- For foreknowledge / special powers: define scope, failure conditions, cost and reliability **before**
  the device first acts; later abilities must trace to that contract. Strip the device out: does the
  chapter still contain a choice?

Record the choice that causes each turn in `project.json.chapters[].choice` (sn.py warns when missing in
Acts 2–3 of dramatic stories).

## 3. Expectation economy [src: oh-story]

- Every promise (she'll strike back, the secret will out, they'll reunite) creates **expectation debt**.
  Delay is allowed if you pay interest: partial progress, new information, a change in the situation, an
  emotional release, a clearer next goal. Delaying with explanation and procedure piles up
  "rationalisation debt".
- **Endgame reserve**: list the one-time cards (the final opponent, the ultimate truth, the identity
  endpoint, the final confirmation of the core bond) and the earliest point each may be played. Spending
  one early is the real cause of "nothing left to write". Multiple lines rising together is fine; playing
  an endgame card early is not.
- **Costs accumulate** [src: drama-skills anti-template]: if every cost a chapter creates is settled
  inside that chapter, nothing carries forward. List costs and the chapter where each lands.

## 4. Recurring prop — rule of three [src: oh-story; prop chain from jtydhr88]

Give each long story 1–2 recurring props (keepsake, tool, trace, number). Three appearances, three
meanings:

| Appearance | Function | Example |
|---|---|---|
| 1st (first quarter) | establish meaning | chiếc khóa vàng = quà sinh nhật chị tặng (ấm áp) |
| 2nd (midpoint turn) | meaning overturned | khóa vàng là đồ mạ (giả dối) |
| 3rd (ending) | emotional blow | khóa vàng bị ném vào sọt rác (đoạn tuyệt) |

Each change of meaning should be caused by **another person's action** on the prop. Register it in
`ledger.json.props` with `"recurring": true`; sn.py warns at the end if it appears in fewer than three
chapters.
