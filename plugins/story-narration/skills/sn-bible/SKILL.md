---
name: sn-bible
description: Stage 2 of the Story Narration suite — build the story bible for a long narrated story video: characters (want/need, voice, xưng hô, verbatim visual signature, arc), opponent tiers, world and locations with drawable anchors and a concrete era, narrative props, narrator voice sample, and the continuity ledger (characters, promises, author-truth knowledge, props, fragile facts). Use after sn-premise is approved, or when the user asks to "tạo nhân vật", "hồ sơ nhân vật", "thiết lập thế giới", "giọng người kể", "sửa nhân vật" for an sn project.
---

# sn-bible — Characters, world, narrator, ledger

`{studio}` = the sibling `sn-studio` skill directory. Read
`{studio}/references/characters-and-dialogue.md` (§1–2), `{studio}/references/continuity.md`,
`{studio}/references/generability.md` (§7 world economy), and the opponent tiers in
`{studio}/references/genres.md`.

Precondition: brief approved (stage `bible`). If missing, route to `sn-premise`.

## Step 1 — Cast

From the brief (for adaptations: from the source text, not invention):
- Principals within the limit (≤5 for 30–60 min, ≤7 for 90 min+). Merge characters that share a
  function; list the merges.
- `bible/characters.md` (Vietnamese), one section per character per characters-and-dialogue.md §1.
  The **visual signature is one fixed phrase** reused verbatim in every shot file.
- Opponents: tiers (minor / middle / major / optional hidden); each with a believable want and one
  concrete cruelty the audience will see. Opponents act rationally on what they know.
- Relationship map (Mermaid `graph TD`) at the end.

## Step 2 — World, locations, props

`bible/world.md`:
- **Era** pinned concretely (generability.md §7).
- **Locations** within the budget from `sn.py budget`: each with its design intent (which scenes it
  exists for), 2–4 drawable anchors, surface condition (lived-in / maintained), the lighting states the
  story actually needs. Prefer variants of one place over new places.
- **Rules** (supernatural, social, device): rule + cost + exception + reliability — fixed before the
  device first acts (mechanism-and-agency.md §2).
- **Narrative props** (≤ 8), each with the collapse test answered and its function; choose 1–2 recurring
  props for the rule of three.

## Step 3 — Narrator

`bible/narrator.md`: person, distance, tone, signature devices, forbidden moves, and a 150–250 syllable
**voice sample** in the tagged format (the cold open draft works well). Use it to calibrate the speaking
rate (sn-premise Step 1).

## Step 4 — Ledger

Fill `ledger.json` (schema in continuity.md §2):
- `characters`: every principal and recurring minor character.
- `promises`: initial mysteries, Chekhov objects, threats, bonds (P01…), planned plant/payoff if known.
- `knowledge`: the author truths the plot turns on (K01…), including false beliefs worth tracking.
- `props`: narrative props (X01…), `recurring: true` for the rule-of-three ones.
- `facts`: fragile facts.

Validate by running `python3 {studio}/scripts/sn.py status <dir>` (loads the files).

## Canon lock

The bible + ledger are **approved canon** from here on. Anything the writing invents later (names, places,
organisations, rules, backstory) goes to `bible/proposals.md` first and enters canon only when the user
approves it — an AI suggestion never becomes story truth automatically. `sn.py audit` lists names that
are unregistered or only proposed.

Register every **real-world detail** the plot leans on (places, administrative names, history,
professions, procedures) in `ledger.json.realworld` with status verified / unverified / fictional;
verify with a source (web search) or make it deliberately fictional. Example: Vietnamese communes were
merged on 01/7/2025 — an old commune name in a present-day story is an error. Upgrade ladders (power, rank, wealth) are written here with a fixed number of steps to prevent
power creep.

## Step 5 — Approval gate ⛔

Present a compact cast card (name — role — want vs need — one-line voice), the locations list, the
recurring prop(s), and the narrator sample. Ask for approval. On approval set `stage` = `"outline"` and
hand off to `sn-outline`.
