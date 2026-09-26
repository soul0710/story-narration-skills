#!/usr/bin/env python3
"""sn.py - deterministic helpers for the Story Narration (sn-*) skill suite.

Standard library only. Checks report facts; the writer decides fixes.

Rule classes (after drama-skills): only STRUCTURAL problems are errors (exit 1).
Craft defaults and taste options are warnings ("!") and never block.

Commands:
  init <dir> --title T --minutes M [--rate R] [--profile dramatic|calm]
  budget --minutes M [--rate R] [--chapters N]   runtime / syllable budget
  outline <dir> [--render]                       validate project.json chapter plan
  duration <dir> [--ch N]                        estimate runtime of written chapters
  continuity <dir>                               ledger vs chapter headers
  lint <file...>                                 AI-voice, listenability, generability
  segment <dir> --ch N [--clip 8] [--force]      cut narration into clip-sized loi_dan segments
  shots <dir> --ch N [--clip 8]                  check shot list + narration coverage
  audit <dir>                                    whole-story audit: repeats, endings, signal lines,
                                                 canon names, voice fingerprints, scene-length spread
  snapshot <dir> [--label L]                     save chapters/bible/ledger before edits (versions/)
  changes <dir> [--since L] [-v]                 what changed since a snapshot; flags removed lines
  export <dir>                                   script-full.md, narration*.txt, youtube-chapters.txt
  status <dir>                                   one-screen project status
"""
import argparse
import json
import math
import os
import re
import sys

# Measured 2026-09-26: macOS Vietnamese voice "Linh" read 82 syllables in 25.5 s (~193/min).
# Human storytellers are usually a bit slower. Always calibrate with the real voice.
DEFAULT_RATE = 180
HEADER_RE = re.compile(r"<!--\s*sn:(.*?)-->", re.S)
TAG_RE = re.compile(r"^\[(HÌNH|DẪN|THOẠI|ÂM|NHẠC|NGỪNG)([^\]]*)\]\s*(.*)$")
SPOKEN_TAGS = ("DẪN", "THOẠI")
WORD_RE = re.compile(r"[0-9A-Za-zÀ-ỹđĐ]+", re.U)
SCENE_RE = re.compile(r"^##\s+Cảnh\s+\d+\s*[—\-:]\s*(.+?)(?:\s*·\s*(.+))?$")
OUTCOMES = ("yes", "no", "yes-but", "no-and")


# ---------------------------------------------------------------- utilities

def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(2)


def load_json(path):
    if not os.path.exists(path):
        die(f"missing {path}")
    with open(path, encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            die(f"{path} is not valid JSON: {e}")


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def words(text):
    return [w.lower() for w in WORD_RE.findall(text)]


def syllables(text):
    return len(WORD_RE.findall(text))


def fmt_time(sec):
    sec = int(round(sec))
    if sec >= 3600:
        return f"{sec // 3600}:{sec % 3600 // 60:02d}:{sec % 60:02d}"
    return f"{sec // 60}:{sec % 60:02d}"


def chapter_files(d):
    cdir = os.path.join(d, "chapters")
    if not os.path.isdir(cdir):
        return []
    out = []
    for name in sorted(os.listdir(cdir)):
        m = re.match(r"ch(\d+)\.md$", name)
        if m:
            out.append((int(m.group(1)), os.path.join(cdir, name)))
    return out


def parse_header(text):
    """<!-- sn: ch=3 cast=an,binh plants=P01 learns=an:K01 --> -> dict of lists."""
    m = HEADER_RE.search(text)
    if not m:
        return None
    out = {}
    for part in m.group(1).split():
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = [x for x in v.strip().split(",") if x]
    return out


def parse_chapter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    spoken, lines, visuals, pauses = [], [], [], 0.0
    scenes, untagged, title = [], [], ""
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("<!--") or line == "---":
            continue
        if line.startswith("# "):
            title = line[2:].strip()
            continue
        if line.startswith("## "):
            m = SCENE_RE.match(line)
            scenes.append((i, m.group(1).strip().lower() if m else line[3:].strip().lower()))
            continue
        m = TAG_RE.match(line)
        if not m:
            untagged.append(i)
            continue
        tag, arg, body = m.group(1), m.group(2), m.group(3)
        if tag in SPOKEN_TAGS:
            spoken.append(body)
            lines.append((i, tag, arg.strip(" :"), body))
        elif tag == "NGỪNG":
            try:
                pauses += float((arg + " " + body).strip(" :s").split()[0])
            except (ValueError, IndexError):
                pauses += 1.0
        elif tag == "HÌNH":
            visuals.append((i, body))
    return {
        "text": text, "title": title, "header": parse_header(text),
        "spoken": spoken, "lines": lines, "visuals": visuals, "scenes": scenes,
        "syllables": sum(syllables(s) for s in spoken), "pauses": pauses,
        "untagged": untagged,
    }


def project(d):
    return load_json(os.path.join(d, "project.json"))


def rate_of(p):
    return p.get("rate_spm", DEFAULT_RATE)


def chapter_seconds(info, rate):
    return info["syllables"] / rate * 60 + info["pauses"]


def location_cap(minutes):
    # shuohao: 4 + ceil(episodes/10), clamped 5-15; here per 10 minutes of runtime (heuristic)
    return max(5, min(15, 4 + math.ceil(minutes / 10)))


# ---------------------------------------------------------------- commands

def cmd_init(a):
    d = a.dir
    for sub in ("chapters", "bible", "reviews", "export", "shots"):
        os.makedirs(os.path.join(d, sub), exist_ok=True)
    pj = os.path.join(d, "project.json")
    if os.path.exists(pj):
        die(f"{pj} already exists; refusing to overwrite")
    rate = a.rate or DEFAULT_RATE
    save_json(pj, {
        "title": a.title, "language": "vi", "target_minutes": a.minutes,
        "rate_spm": rate, "rate_calibrated": False, "profile": a.profile,
        "stage": "premise", "brief": {}, "chapters": [],
    })
    lj = os.path.join(d, "ledger.json")
    if not os.path.exists(lj):
        save_json(lj, {"characters": {}, "promises": [], "knowledge": [], "props": [], "facts": []})
    print(f"created {d} (target {a.minutes} min @ {rate} syllables/min, profile {a.profile})")


def cmd_budget(a):
    rate = a.rate or DEFAULT_RATE
    n = a.chapters or max(3, round(a.minutes / 5))
    per = a.minutes / n
    full = int(a.minutes * rate)
    print(f"Target runtime     : {a.minutes:g} min")
    print(f"Speaking rate      : {rate} syllables/min {'(default — calibrate with the real voice!)' if not a.rate else ''}")
    print(f"Spoken syllables   : {full:,} if no pauses; ~{int(full * 0.96):,} if [NGỪNG] total ~4% of runtime")
    print(f"Chapters           : {n} x ~{per:.1f} min (~{int(per * rate * 0.96):,} syllables each)")
    print(f"Cold open          : first 45-90 s (~{int(0.75 * rate):,}-{int(1.5 * rate):,} syllables)")
    print(f"Location budget    : <= {location_cap(a.minutes)} distinct locations (heuristic, AI-video economy)")
    print("Structural anchors (dramatic profile; minute marks):")
    for name, pct in (("Inciting incident", .10), ("Point of no return", .23),
                      ("Midpoint turn", .50), ("Lowest point", .75),
                      ("Climax starts", .85), ("Resolution", .95)):
        print(f"  {name:<20} ~{a.minutes * pct:5.1f} min ({int(pct * 100)}%)")
    print("Calm profile shares: open 10-15% · wander 55-65% · settle 15-20% · warm close ~10%")


def validate_outline(p, ledger):
    errs, warns = [], []
    chs = p.get("chapters", [])
    prof = p.get("profile", "dramatic")
    if not chs:
        return ["project.json has no chapters"], warns
    n = len(chs)
    target = p.get("target_minutes", 0)
    total = sum(float(c.get("minutes", 0)) for c in chs)
    if target and abs(total - target) / target > 0.05:
        errs.append(f"chapter minutes sum {total:.1f} vs target {target} (> ±5%)")
    ids = [c.get("id") for c in chs]
    if ids != list(range(1, n + 1)):
        errs.append(f"chapter ids must be 1..{n} in order, got {ids}")
    for c in chs:
        cid = c.get("id")
        for k in ("title", "minutes", "purpose", "turn"):
            if not c.get(k):
                errs.append(f"ch{cid}: missing '{k}'")
        it = c.get("intensity")
        if it is not None and (not isinstance(it, int) or not 1 <= it <= 5):
            errs.append(f"ch{cid}: intensity must be integer 1-5")
        if prof == "dramatic" and it is None:
            warns.append(f"ch{cid}: no intensity (needed for rhythm checks)")
        if cid != n and not c.get("end_hook"):
            warns.append(f"ch{cid}: no end_hook" + (" (fine for calm stories if the transition carries)" if prof == "calm" else ""))
        oc = c.get("outcome")
        if oc and oc not in OUTCOMES:
            errs.append(f"ch{cid}: outcome must be one of {OUTCOMES}")
        if prof == "dramatic" and str(c.get("act", "1")) != "1" and not c.get("choice"):
            warns.append(f"ch{cid}: no 'choice' — whose decision causes this turn? (agency)")
        if c.get("choice") and not c.get("consequence"):
            warns.append(f"ch{cid}: 'choice' without 'consequence' — cause → choice → consequence?")
    if not chs[0].get("cold_open"):
        errs.append("ch1: missing 'cold_open' (what the first 45-90 s shows and asks)")
    # --- craft / taste checks: warnings only
    if prof == "dramatic":
        gap = 0.0
        for c in chs:
            if c.get("intensity", 0) >= 3 or c.get("payoffs"):
                gap = 0.0
            else:
                gap += float(c.get("minutes", 0))
                if gap > 10:
                    warns.append(f"ch{c['id']}: >10 min without a payoff or intensity>=3 — intended?")
                    gap = 0.0
        its = [c.get("intensity", 0) for c in chs]
        peak = max(its)
        last_peak = max(i for i, v in enumerate(its, 1) if v == peak)
        if last_peak < math.ceil(n * 0.7):
            warns.append(f"peak intensity ({peak}) last occurs at ch{last_peak}, before the final 30%")
        mids = [c for c in chs if "midpoint" in str(c.get("beat", "")).lower()]
        if not mids:
            warns.append("no chapter has beat 'midpoint'")
        else:
            cum = sum(float(c.get("minutes", 0)) for c in chs[:chs.index(mids[0])])
            if target and not 0.35 <= cum / target <= 0.62:
                warns.append(f"midpoint starts at {cum:.1f} min ({cum / target:.0%}); usual range 40-55%")
    for prev, cur in zip(chs, chs[1:]):
        if prev.get("hook_type") and prev.get("hook_type") == cur.get("hook_type"):
            warns.append(f"ch{prev['id']}-ch{cur['id']}: same hook_type '{cur['hook_type']}' twice in a row")
    run = 0
    for c in chs:
        run = run + 1 if c.get("outcome") == "yes" else 0
        if run == 3:
            warns.append(f"ch{c['id']}: third 'yes' outcome in a row — no pressure (story-skills)")
    mech = {}
    for c in chs:
        if c.get("mechanism"):
            mech.setdefault(c["mechanism"], []).append(c)
    for name, runs in mech.items():
        if len(runs) >= 3:
            missing = [str(c["id"]) for c in runs if not c.get("cost")]
            warns.append(f"mechanism '{name}' runs {len(runs)}x (ch {', '.join(str(c['id']) for c in runs)}): "
                         f"check each run changes state + has a cost" + (f"; no cost in ch {', '.join(missing)}" if missing else ""))
    locs = {}
    for c in chs:
        for loc in c.get("locations", []):
            locs.setdefault(loc.strip().lower(), []).append(c["id"])
    if locs:
        cap = location_cap(target or total)
        if len(locs) > cap:
            warns.append(f"{len(locs)} distinct locations > budget {cap} (each new location = more AI consistency work)")
        once = [k for k, v in locs.items() if len(v) == 1]
        if len(once) > 2:
            warns.append(f"one-off locations: {', '.join(once[:8])} — cut, merge, or reuse a variant of an existing place")
    # promises
    plants, pays = {}, {}
    for c in chs:
        for pid in c.get("plants", []):
            plants.setdefault(pid, c["id"])
        for pid in c.get("payoffs", []):
            pays.setdefault(pid, c["id"])
    for pid, ch in pays.items():
        if pid not in plants:
            errs.append(f"{pid}: paid in ch{ch} but never planted")
        elif plants[pid] >= ch:
            errs.append(f"{pid}: payoff ch{ch} not after plant ch{plants[pid]}")
    for pid, ch in plants.items():
        if pid not in pays:
            warns.append(f"{pid}: planted ch{ch} but no payoff planned")
    known = {pr.get("id") for pr in ledger.get("promises", [])}
    for pid in set(plants) | set(pays):
        if pid not in known:
            warns.append(f"{pid}: not registered in ledger.json promises")
    return errs, warns


def render_outline(p):
    rows = ["# " + p.get("title", "Outline"), "",
            f"Target: {p.get('target_minutes')} min · {len(p['chapters'])} chapters · profile {p.get('profile', 'dramatic')}", "",
            "| # | Title | Min (start) | Act | Beat | Int | Purpose | Turn | Choice | Out | End hook |",
            "|---|---|---|---|---|---|---|---|---|---|---|"]
    cum = 0.0
    for c in p["chapters"]:
        rows.append("| {id} | {t} | {m} ({s}) | {a} | {b} | {i} | {pu} | {tu} | {ch} | {o} | {h} |".format(
            id=c["id"], t=c.get("title", ""), m=c.get("minutes", ""), s=fmt_time(cum * 60),
            a=c.get("act", ""), b=c.get("beat", ""), i="★" * int(c.get("intensity", 0) or 0),
            pu=c.get("purpose", ""), tu=c.get("turn", ""), ch=c.get("choice", ""), o=c.get("outcome", ""),
            h=(c.get("hook_type", "") + ": " if c.get("hook_type") else "") + c.get("end_hook", "")))
        cum += float(c.get("minutes", 0))
    rows += ["", "Intensity curve: " + " ".join(str(c.get("intensity", "-")) for c in p["chapters"]), ""]
    return "\n".join(rows)


def report(errs, warns):
    for e in errs:
        print("✗", e)
    for w in warns:
        print("!", w)
    print("PASS" + (f" ({len(warns)} warnings)" if warns else "") if not errs else f"FAIL ({len(errs)} errors, {len(warns)} warnings)")
    return 1 if errs else 0


def cmd_outline(a):
    p = project(a.dir)
    ledger = load_json(os.path.join(a.dir, "ledger.json"))
    errs, warns = validate_outline(p, ledger)
    if a.render and p.get("chapters"):
        with open(os.path.join(a.dir, "outline.md"), "w", encoding="utf-8") as f:
            f.write(render_outline(p))
        print("wrote outline.md")
    sys.exit(report(errs, warns))


def cmd_duration(a):
    p = project(a.dir)
    rate = rate_of(p)
    if not p.get("rate_calibrated"):
        print(f"! rate {rate}/min is not calibrated — time one minute of the real voice and set rate_spm")
    plan = {c["id"]: c for c in p.get("chapters", [])}
    total, fails = 0.0, 0
    for cid, path in chapter_files(a.dir):
        if a.ch and cid != a.ch:
            continue
        info = parse_chapter(path)
        sec = chapter_seconds(info, rate)
        total += sec
        tgt = float(plan.get(cid, {}).get("minutes", 0)) * 60
        flag = ""
        if tgt:
            dev = (sec - tgt) / tgt
            need = int((tgt - info["pauses"]) * rate / 60)
            flag = f"target {fmt_time(tgt)} ({dev:+.0%}), needs ~{need:,} syllables with these pauses"
            if abs(dev) > 0.10:
                flag += "  ✗ outside ±10%"
                fails += 1
        print(f"ch{cid:02d}: {fmt_time(sec)}  syl={info['syllables']:,} pauses={info['pauses']:.0f}s "
              f"scenes={len(info['scenes'])} visuals={len(info['visuals'])}  {flag}")
        if info["untagged"]:
            print(f"      ✗ untagged lines: {info['untagged'][:10]}{' …' if len(info['untagged']) > 10 else ''}")
            fails += 1
    if not a.ch:
        print(f"TOTAL: {fmt_time(total)} / target {fmt_time(p.get('target_minutes', 0) * 60)}")
    sys.exit(1 if fails else 0)


def cmd_continuity(a):
    ledger = load_json(os.path.join(a.dir, "ledger.json"))
    p = project(a.dir)
    chars = ledger.get("characters", {})
    promises = {pr["id"]: pr for pr in ledger.get("promises", []) if "id" in pr}
    knowledge = {k["id"]: k for k in ledger.get("knowledge", []) if "id" in k}
    props = {x["id"]: x for x in ledger.get("props", []) if "id" in x}
    errs, warns = [], []
    seen_plant, seen_pay, learned, prop_seen, revealed, suspected = {}, {}, {}, {}, {}, {}
    files = chapter_files(a.dir)
    for cid, path in files:
        info = parse_chapter(path)
        h = info["header"]
        if h is None:
            errs.append(f"ch{cid}: missing <!-- sn: ... --> header")
            continue
        if h.get("ch", [str(cid)])[0] != str(cid):
            errs.append(f"ch{cid}: header ch={h.get('ch')} does not match file name")
        for who in h.get("cast", []):
            c = chars.get(who)
            if c is None:
                errs.append(f"ch{cid}: cast '{who}' not in ledger characters")
                continue
            died = c.get("died_in")
            if died is not None and cid > int(died):
                errs.append(f"ch{cid}: '{who}' appears after dying in ch{died} (use mentions= for memories)")
        for who in h.get("mentions", []):
            if who not in chars:
                warns.append(f"ch{cid}: mention '{who}' not in ledger characters")
        for pid in h.get("plants", []):
            seen_plant.setdefault(pid, cid)
            if pid not in promises:
                errs.append(f"ch{cid}: plants unknown promise {pid}")
        for pid in h.get("pays", []):
            seen_pay.setdefault(pid, cid)
            if pid not in promises:
                errs.append(f"ch{cid}: pays unknown promise {pid}")
        for item in h.get("learns", []):
            who, _, kid = item.partition(":")
            if kid not in knowledge:
                errs.append(f"ch{cid}: learns unknown knowledge {kid}")
            if who not in chars:
                errs.append(f"ch{cid}: learns — '{who}' not in ledger characters")
            learned.setdefault((who, kid), cid)
        for item in h.get("suspects", []):
            who, _, kid = item.partition(":")
            if kid not in knowledge:
                errs.append(f"ch{cid}: suspects unknown knowledge {kid}")
            suspected.setdefault((who, kid), cid)
        for item in h.get("uses", []):
            who, _, kid = item.partition(":")
            if kid not in knowledge:
                errs.append(f"ch{cid}: uses unknown knowledge {kid}")
            elif (who, kid) not in learned:
                if (who, kid) in suspected:
                    warns.append(f"ch{cid}: '{who}' acts on {kid} while only suspecting it — shown as a guess on the page?")
                else:
                    errs.append(f"ch{cid}: '{who}' acts on {kid} ({knowledge[kid].get('fact', '')}) before learning it")
        for kid in h.get("reveals", []):
            if kid not in knowledge:
                errs.append(f"ch{cid}: reveals unknown knowledge {kid}")
            revealed.setdefault(kid, cid)
        for xid in h.get("props", []):
            if xid not in props:
                errs.append(f"ch{cid}: prop {xid} not in ledger props")
            prop_seen.setdefault(xid, []).append(cid)
        cast = set(h.get("cast", []))
        names = {chars[k].get("name", k) for k in cast if k in chars}
        for ln, tag, arg, _ in info["lines"]:
            if tag != "THOẠI":
                continue
            spk = arg.split("|")[0].strip()
            if spk and spk not in names and spk.lower() not in cast and spk not in ("VO", "Người dẫn"):
                warns.append(f"ch{cid} line {ln}: speaker '{spk}' not in this chapter's cast")
    for pid, ch in seen_pay.items():
        if pid in seen_plant and seen_plant[pid] >= ch:
            errs.append(f"{pid}: paid in ch{ch} before/at plant ch{seen_plant[pid]}")
        if pid not in seen_plant:
            errs.append(f"{pid}: paid in ch{ch} but never planted on the page")
    n_plan = len(p.get("chapters", []))
    written = {cid for cid, _ in files}
    finished = bool(n_plan) and n_plan in written
    for pid, pr in promises.items():
        if pid in seen_plant and pid not in seen_pay and pr.get("status") != "dropped":
            due = pr.get("payoff")
            if due and int(due) in written:
                errs.append(f"{pid}: due in ch{due} but not paid there ({pr.get('desc', '')})")
            elif finished:
                errs.append(f"{pid}: story finished but promise still open ({pr.get('desc', '')})")
    if len(props) > 8:
        warns.append(f"{len(props)} narrative props > 8 (shuohao cap) — is each one load-bearing?")
    if finished:
        for xid, x in props.items():
            if x.get("recurring") and len(prop_seen.get(xid, [])) < 3:
                warns.append(f"recurring prop {xid} ({x.get('name', '')}) appears in {len(prop_seen.get(xid, []))} chapters; rule of three")
    for e in errs:
        print("✗", e)
    for w in warns:
        print("!", w)
    print("PASS" + (f" ({len(warns)} warnings)" if warns else "") if not errs else f"FAIL ({len(errs)} errors)")
    sys.exit(1 if errs else 0)


# ---------------------------------------------------------------- lint
# EXPERIMENTAL lists written for sn (not from a source corpus). Strong = stock phrases
# that almost always read as machine prose; weak = ordinary words that only hurt when dense.
STRONG = [
    "không khỏi", "bất giác", "khẽ mỉm cười", "nở một nụ cười", "thoáng qua một tia", "ánh mắt thoáng",
    "hít một hơi thật sâu", "hít một hơi sâu", "trái tim như thắt lại", "tim như thắt lại",
    "thời gian như ngừng trôi", "thời gian như ngưng đọng", "không gian như ngưng đọng",
    "một cảm giác khó tả", "cảm xúc khó tả", "không thể diễn tả bằng lời", "len lỏi", "vỡ òa",
    "đọng lại", "dư vị", "dịu dàng đến lạ", "đầy ẩn ý", "như một lời nhắc nhở", "trong khoảnh khắc ấy",
    "suy cho cùng", "ít ai biết rằng", "điều mà ít ai biết", "không ai ngờ rằng",
    "khẽ thở dài", "không biết phải nói gì", "một cảm giác kỳ lạ", "dâng lên trong lòng",
]
# Dramatic signal lines (ai-failure-modes C3) and emotion telling (E3)
SIGNALS = ["không hề biết rằng", "không ai có thể ngờ", "không ai ngờ", "định mệnh", "mọi thứ mới chỉ bắt đầu",
           "cô không biết rằng", "anh không biết rằng", "sắp thay đổi tất cả", "số phận đã", "chưa ai biết rằng"]
TELLING = ["rất buồn", "rất vui", "rất tức giận", "rất giận", "rất sợ", "vô cùng đau khổ", "vô cùng hạnh phúc",
           "cảm thấy buồn", "cảm thấy vui", "cảm thấy lo lắng", "cảm thấy hạnh phúc", "nỗi buồn", "niềm vui"]
WEAK = ["có lẽ", "dường như", "như thể", "một cách", "không chỉ", "hành trình", "bỗng nhiên",
        "chợt nhận ra", "một lần nữa", "ngay lúc đó", "và rồi", "một tia", "tràn ngập", "lấp lánh",
        "khẽ khàng", "khẽ"]
MORAL = ["bài học", "ý nghĩa thật sự", "điều quý giá nhất", "cuộc sống là", "hạnh phúc đôi khi", "suy cho cùng"]
# Generability of [HÌNH] lines (drama-skills generability.md, shuohao warnings), Vietnamese cues.
GEN_RULES = [
    ("inner state, not an image", ["như thể", "dường như", "có vẻ", "chợt hiểu", "nhận ra", "cảm thấy",
                                   "như muốn", "thầm nghĩ", "trong lòng"]),
    ("negative action (can't be generated)", ["không nhìn", "không nói", "không đáp", "không trả lời",
                                              "chẳng nói", "không quay", "không động"]),
    ("micro-expression carries the info", ["nhíu mày", "mi mắt", "khóe môi", "khóe mắt", "đồng tử",
                                           "mím môi", "run run", "ngón tay khẽ", "ánh mắt"]),
    ("hard to generate (rain/crowd/contact/hands/text/fire/mirror)",
     ["mưa", "đám đông", "dòng người", "ôm", "hôn", "nắm tay", "cầm lấy tay", "cầm tay", "nắm lấy tay",
      "đặt vào tay", "mở tay", "đánh nhau", "vật lộn", "bàn tay",
      "ngón tay", "dòng chữ", "chữ viết", "biển hiệu", "gương", "phản chiếu", "lửa"]),
]


SAFE_COMPOUNDS = ["hoàng hôn", "lòng bàn tay", "ôm đồm", "khói bếp", "khói nhang"]


def find_phrase(low, ph):
    return len(re.findall(r"(?<![0-9a-zà-ỹđ])" + re.escape(ph) + r"(?![0-9a-zà-ỹđ])", low))


def lint_text(text):
    out = []
    spoken, visuals = [], []
    for i, raw in enumerate(text.splitlines(), 1):
        m = TAG_RE.match(raw.strip())
        if not m:
            continue
        if m.group(1) in SPOKEN_TAGS:
            spoken.append((i, m.group(3)))
        elif m.group(1) == "HÌNH":
            visuals.append((i, m.group(3)))
    items = spoken or [(i, l) for i, l in enumerate(text.splitlines(), 1) if l.strip()]
    body = " ".join(s for _, s in items).lower()
    total = max(1, syllables(body))
    strong = {ph: find_phrase(body, ph) for ph in STRONG}
    strong = {k: v for k, v in strong.items() if v}
    density = sum(strong.values()) / total * 1000
    level = "light" if density <= 2 else "medium" if density <= 6 else "heavy"
    out.append(f"stock-phrase density: {density:.1f}/1000 syllables ({level}) [experimental list]")
    for ph, n in sorted(strong.items(), key=lambda x: -x[1])[:12]:
        out.append(f"  '{ph}' x{n}")
    for label, lst in (("signal line", SIGNALS), ("telling emotion", TELLING)):
        for ph in lst:
            n = find_phrase(body, ph)
            if n:
                out.append(f"  {label}: '{ph}' x{n}")
    for ph in WEAK:
        n = find_phrase(body, ph)
        if n and n / total * 1000 > 3:
            out.append(f"  dense: '{ph}' x{n} ({n / total * 1000:.1f}/1000)")
    for ln, s in items:
        for sent in re.split(r"(?<=[.!?…])\s+", s):
            k = syllables(sent)
            if k > 40:
                out.append(f"line {ln}: sentence {k} syllables (>40 is hard to follow by ear)")
        if re.search(r"\d", s):
            out.append(f"line {ln}: digits in spoken text — write numbers as words")
        if s.count("—") + s.count("--") >= 2:
            out.append(f"line {ln}: stacked dashes")
        tail = s.lower()[-70:]
        if any(m in tail for m in MORAL):
            out.append(f"line {ln}: moralising/summary phrasing at line end")
    opens = {}
    for ln, s in items:
        w = " ".join(words(s)[:2])
        if w:
            opens.setdefault(w, []).append(ln)
    for w, lns in opens.items():
        if len(lns) >= 4:
            out.append(f"opening '{w}…' used {len(lns)}x (lines {lns[:6]})")
    gen = []
    for ln, s in visuals:
        low = s.lower()
        for ok in SAFE_COMPOUNDS:  # compounds that contain a flagged word but are not the risk
            low = low.replace(ok, " ")
        for label, cues in GEN_RULES:
            hit = [c for c in cues if find_phrase(low, c)]
            if hit:
                gen.append(f"line {ln}: [HÌNH] {label}: {', '.join(hit)}")
        if re.search(r"(?<![a-zà-ỹđ])như(?![a-zà-ỹđ])", low) and "như thể" not in low:
            gen.append(f"line {ln}: [HÌNH] simile — describe what is literally visible")
        if low.count(",") >= 3:
            gen.append(f"line {ln}: [HÌNH] 4+ clauses — one moment per image")
    if gen:
        out.append(f"generability flags ({len(gen)}) — rewrite or mark high-risk with a fallback:")
        out += ["  " + g for g in gen[:25]]
    return out


def cmd_lint(a):
    for path in a.files:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        print(f"== {path}")
        for line in lint_text(text):
            print(line)


# ---------------------------------------------------------------- shots

ANCHOR_FIELDS = ["Mùa / thời điểm", "Bảng màu", "Chất phim", "Ống kính / mood", "Nhân vật / motif cố định"]


def parse_blocks(text, head=r"^##\s+SHOT\s+(\d+)\s*$"):
    blocks, cur = {}, None
    order = []
    for raw in text.splitlines():
        m = re.match(head, raw.strip())
        if m:
            cur = int(m.group(1))
            order.append(cur)
            blocks[cur] = []
            continue
        if cur is not None:
            blocks[cur].append(raw)
    return order, blocks


def cmd_shots(a):
    p = project(a.dir)
    rate = rate_of(p)
    ch = a.ch
    kb = os.path.join(a.dir, "shots", f"kich_ban_ch{ch:02d}.md")
    ld = os.path.join(a.dir, "shots", f"loi_dan_ch{ch:02d}.md")
    cp = os.path.join(a.dir, "chapters", f"ch{ch:02d}.md")
    for f in (kb, ld, cp):
        if not os.path.exists(f):
            die(f"missing {f}")
    errs, warns = [], []
    kb_text = open(kb, encoding="utf-8").read()
    if "## STYLE ANCHOR" not in kb_text:
        errs.append("kich_ban: missing '## STYLE ANCHOR'")
    for fld in ANCHOR_FIELDS:
        if f"- {fld}:" not in kb_text:
            errs.append(f"kich_ban: STYLE ANCHOR missing '{fld}'")
    order, blocks = parse_blocks(kb_text)
    if order != list(range(1, len(order) + 1)):
        errs.append(f"kich_ban: SHOT numbers not continuous from 01: {order[:12]}…")
    for sid in order:
        body = "\n".join(blocks[sid])
        for fld in ("Cảnh", "Cảm xúc", "Máy quay", "Liên kết"):
            if f"- {fld}:" not in body:
                errs.append(f"SHOT {sid:02d}: missing '{fld}'")
        if "- Nhạc:" not in body and "- Âm thanh:" not in body:
            errs.append(f"SHOT {sid:02d}: missing 'Nhạc' (calm) or 'Âm thanh' (cinematic)")
        if "- Lời dẫn:" in body:
            errs.append(f"SHOT {sid:02d}: narration belongs in loi_dan_chNN.md, not in the prompt script")
    lorder, lblocks = parse_blocks(open(ld, encoding="utf-8").read())
    if lorder != order:
        errs.append(f"loi_dan SHOT numbers {lorder[:8]}… differ from kich_ban {order[:8]}…")
    cap = a.clip * rate / 60
    shot_words = []
    for sid in lorder:
        txt = " ".join(re.sub(r"\[[^\]]*\]", " ", l) for l in lblocks[sid] if l.strip())  # speaker labels anywhere
        if "(im lặng)" in txt:
            txt = txt.replace("(im lặng)", "")
        w = words(txt)
        shot_words.append((sid, w))
        if len(w) > cap * 1.25:
            warns.append(f"SHOT {sid:02d}: {len(w)} syllables > {cap * 1.25:.0f} (~{len(w) / rate * 60:.1f}s of speech on a {a.clip}s clip)")
    got = [w for _, ws in shot_words for w in ws]
    info = parse_chapter(cp)
    want = words(" ".join(info["spoken"]))
    if got != want:
        i = next((k for k in range(min(len(got), len(want))) if got[k] != want[k]), min(len(got), len(want)))
        where = next((sid for sid, ws in shot_words if sum(len(x) for s2, x in shot_words if s2 <= sid) > i), lorder[-1] if lorder else 0)
        errs.append(f"narration coverage mismatch at word {i} (near SHOT {where:02d}): "
                    f"chapter '…{' '.join(want[max(0, i - 3):i + 5])}…' vs shots '…{' '.join(got[max(0, i - 3):i + 5])}…'")
    speech = chapter_seconds(info, rate)
    clips = len(order) * a.clip
    print(f"ch{ch:02d}: {len(order)} shots × {a.clip}s = {fmt_time(clips)} of clips vs {fmt_time(speech)} narration")
    if speech and abs(clips - speech) / speech > 0.2:
        warns.append(f"clip runtime differs from narration by {(clips - speech) / speech:+.0%}; split/merge segments or change clip length")
    sys.exit(report(errs, warns))


def cmd_segment(a):
    """Write shots/loi_dan_chNN.md: narration cut into clip-sized segments (sentence boundaries,
    new segment at each scene heading). Pauses are absorbed into clips, not separate shots."""
    p = project(a.dir)
    rate = rate_of(p)
    cap = a.clip * rate / 60
    cp = os.path.join(a.dir, "chapters", f"ch{a.ch:02d}.md")
    if not os.path.exists(cp):
        die(f"missing {cp}")
    out = os.path.join(a.dir, "shots", f"loi_dan_ch{a.ch:02d}.md")
    if os.path.exists(out) and not a.force:
        die(f"{out} exists (use --force to overwrite)")
    segs, cur, n = [], [], 0

    def flush():
        nonlocal cur, n
        if cur:
            segs.append(" ".join(cur))
        cur, n = [], 0

    for raw in open(cp, encoding="utf-8").read().splitlines():
        line = raw.strip()
        if line.startswith("## "):
            flush()
            continue
        m = TAG_RE.match(line)
        if not m or m.group(1) not in SPOKEN_TAGS:
            continue
        tag, arg, body = m.groups()
        label = f"[{arg.strip(' :').split('|')[0].strip()}] " if tag == "THOẠI" else ""
        for i, sent in enumerate(re.split(r"(?<=[.!?…])\s+", body)):
            k = syllables(sent)
            if n and n + k > cap * 1.12:
                flush()
            cur.append((label if i == 0 else "") + sent)
            n += k
    flush()
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# Lời dẫn theo shot — Chương {a.ch:02d}\n\n")
        for i, sgm in enumerate(segs, 1):
            f.write(f"## SHOT {i:02d}\n{sgm}\n\n")
    info = parse_chapter(cp)
    print(f"wrote {out}: {len(segs)} shots × {a.clip:g}s = {fmt_time(len(segs) * a.clip)} "
          f"vs {fmt_time(chapter_seconds(info, rate))} narration")
    print("Next: write kich_ban with the same SHOT numbers (one visual per segment), then run `sn.py shots`.")


# ---------------------------------------------------------------- audit (whole story)

def canon_text(d, proposals=False):
    """Approved canon (bible/*.md except proposals.md, ledger, project, brief, outline).
    With proposals=True, return only bible/proposals.md (pending, not yet canon)."""
    parts = []
    rp = os.path.join(d, "bible")
    if os.path.isdir(rp):
        for n in os.listdir(rp):
            if not n.endswith(".md"):
                continue
            if (n == "proposals.md") != proposals:
                continue
            parts.append(open(os.path.join(rp, n), encoding="utf-8").read())
    if proposals:
        return " ".join(parts).lower()
    for n in ("ledger.json", "project.json", "brief.md", "outline.md"):
        fp = os.path.join(d, n)
        if os.path.exists(fp):
            parts.append(open(fp, encoding="utf-8").read())
    return " ".join(parts).lower()


NAME_STOP = {"tháng", "giêng", "chạp", "thứ", "chủ", "nhật", "ba", "tư", "năm", "sáu", "bảy", "tám", "chín",
             "mười", "một", "hai", "rằm", "mùng"}


def proper_names(line):
    """Runs of capitalised tokens that are not sentence-initial (sentence-initial runs keep their tail)."""
    toks = re.findall(r"[^\s]+", line)
    out, run, initial = [], [], True
    prev_end = True
    for t in toks:
        core = t.strip('.,!?…:;"“”()[]—-')
        cap = bool(core) and core[0].isupper() and core[0].isalpha()
        if cap:
            if not run:
                initial = prev_end
            run.append(core)
        if not cap or t[-1:] in ".,!?…:;\"”":
            if run:
                names = run[1:] if initial else run
                if names and not all(w.lower() in NAME_STOP for w in names):
                    out.append(" ".join(names))
                run = []
        prev_end = t[-1:] in '.!?…:"“' or t in ("—", "-")
    if run:
        names = run[1:] if initial else run
        if names and not all(w.lower() in NAME_STOP for w in names):
            out.append(" ".join(names))
    return out


def cmd_audit(a):
    p = project(a.dir)
    files = chapter_files(a.dir)
    if not files:
        die("no chapters")
    infos = {cid: parse_chapter(path) for cid, path in files}
    warns = []
    # A1/E1 cross-chapter repeated 4-grams in narration and dialogue
    grams = {}
    for cid, info in infos.items():
        for _, tag, _, body in info["lines"]:
            ws = words(body)
            for i in range(len(ws) - 3):
                g = " ".join(ws[i:i + 4])
                grams.setdefault(g, []).append(cid)
    rep = [(g, c) for g, c in grams.items() if len(set(c)) >= 3 or len(c) >= 4]
    rep.sort(key=lambda x: (-len(set(x[1])), -len(x[1])))
    print("== Repeated phrases across chapters (A1/E1) — intentional refrain or tic?")
    for g, c in rep[:15]:
        print(f"  '{g}' x{len(c)} in ch {sorted(set(c))}")
    if not rep:
        print("  none")
    # A3 chapter endings
    print("== Chapter endings (A3)")
    ends = {}
    for cid, info in infos.items():
        last = info["spoken"][-1] if info["spoken"] else ""
        ends[cid] = set(words(last))
        flag = [ph for ph in SIGNALS if find_phrase(last.lower(), ph)]
        print(f"  ch{cid:02d}: …{last[-90:]}" + (f"  ! signal line: {flag}" if flag else ""))
    ids = sorted(ends)
    for x, y in zip(ids, ids[1:]):
        A, B = ends[x], ends[y]
        if A and B and len(A & B) / len(A | B) > 0.4:
            warns.append(f"ch{x} and ch{y} end with very similar lines")
    # C3 signal lines anywhere
    sig = []
    for cid, info in infos.items():
        low = " ".join(info["spoken"]).lower()
        for ph in SIGNALS:
            n = find_phrase(low, ph)
            if n:
                sig.append(f"ch{cid}: '{ph}' x{n}")
    print("== Dramatic signal lines (C3)")
    print("  " + ("; ".join(sig) if sig else "none"))
    # B2 canon: proper names not in the bible/ledger
    canon = canon_text(a.dir)
    unknown = {}
    for cid, info in infos.items():
        texts = info["spoken"] + [v for _, v in info["visuals"]]
        for t in texts:
            for name in proper_names(t):
                if name.lower() not in canon:
                    unknown.setdefault(name, set()).add(cid)
    pending_txt = canon_text(a.dir, proposals=True)
    pending = {k: v for k, v in unknown.items() if k.lower() in pending_txt}
    unknown = {k: v for k, v in unknown.items() if k not in pending}
    print("== Names not in approved canon (B2 canon lock) — propose in bible/proposals.md or cut")
    if unknown:
        for name, cs in sorted(unknown.items(), key=lambda x: min(x[1])):
            print(f"  {name}  (ch {sorted(cs)})")
    else:
        print("  none")
    if pending:
        print("== On the page but still only PROPOSED (bible/proposals.md) — needs user approval")
        for name, cs in sorted(pending.items(), key=lambda x: min(x[1])):
            print(f"  {name}  (ch {sorted(cs)})")
    # real-world details to verify
    ledger = load_json(os.path.join(a.dir, "ledger.json"))
    rw = ledger.get("realworld", [])
    todo = [r for r in rw if r.get("status") not in ("verified", "fictional")]
    print(f"== Real-world details: {len(rw)} registered, {len(todo)} not verified")
    for r in todo:
        print(f"  ? {r.get('item')} — {r.get('note', '')}")
    # D1/D2/D3 voice fingerprints
    print("== Voice fingerprints (D1/D2/D3): lines · avg syllables/line · longest · per-chapter avg")
    per = {}
    for cid, info in infos.items():
        for ln, tag, arg, body in info["lines"]:
            if tag != "THOẠI":
                continue
            spk = arg.split("|")[0].strip() or "?"
            per.setdefault(spk, []).append((cid, ln, syllables(body), words(body)))
    allw = {}
    for spk, rows in per.items():
        for r in rows:
            for w in r[3]:
                allw[w] = allw.get(w, 0) + 1
    for spk, rows in sorted(per.items(), key=lambda x: -len(x[1])):
        lens = [r[2] for r in rows]
        bych = {}
        for r in rows:
            bych.setdefault(r[0], []).append(r[2])
        mine = {}
        for r in rows:
            for w in r[3]:
                mine[w] = mine.get(w, 0) + 1
        sig_words = sorted((w for w in mine if mine[w] >= 2 and mine[w] / allw[w] >= 0.6 and len(w) > 1),
                           key=lambda w: -mine[w])[:6]
        trend = " ".join(f"ch{c}:{sum(v) / len(v):.0f}" for c, v in sorted(bych.items()))
        print(f"  {spk:<14} {len(rows):>3} lines · avg {sum(lens) / len(lens):4.1f} · max {max(lens):>2} · {trend}"
              + (f" · own words: {', '.join(sig_words)}" if sig_words else ""))
        for cid, ln, k, _ in rows:
            if k > 30 and spk != "VO":
                warns.append(f"ch{cid} line {ln}: {spk} speaks {k} syllables in one line — speech-like? (D3)")
    # A2 scene length spread
    print("== Scene lengths in syllables (A2) — does the key scene get the most room?")
    for cid, path in files:
        text = open(path, encoding="utf-8").read().splitlines()
        sizes, cur = [], None
        for raw in text:
            line = raw.strip()
            if line.startswith("## "):
                if cur is not None:
                    sizes.append(cur)
                cur = 0
                continue
            m = TAG_RE.match(line)
            if m and m.group(1) in SPOKEN_TAGS and cur is not None:
                cur += syllables(m.group(3))
        if cur is not None:
            sizes.append(cur)
        flag = ""
        if len(sizes) >= 3 and min(sizes) and max(sizes) / min(sizes) < 1.6:
            flag = "  ! scenes nearly equal length — uniform pacing?"
        print(f"  ch{cid:02d}: {sizes}{flag}")
    for w in warns:
        print("!", w)
    print("Audit reports facts for the read-through; it never replaces reading the whole story.")


# ---------------------------------------------------------------- versions

def cmd_snapshot(a):
    import shutil
    import time
    label = time.strftime("%Y%m%d-%H%M%S") + (f"-{a.label}" if a.label else "")
    dst = os.path.join(a.dir, "versions", label)
    os.makedirs(dst)
    for item in ("chapters", "bible", "shots"):
        src = os.path.join(a.dir, item)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(dst, item))
    for f in ("ledger.json", "project.json", "state.md"):
        if os.path.exists(os.path.join(a.dir, f)):
            shutil.copy2(os.path.join(a.dir, f), dst)
    print(f"snapshot: versions/{label}")


def cmd_changes(a):
    import difflib
    vdir = os.path.join(a.dir, "versions")
    snaps = sorted(os.listdir(vdir)) if os.path.isdir(vdir) else []
    if not snaps:
        die("no snapshots (run `sn.py snapshot` before editing)")
    base = next((x for x in reversed(snaps) if a.since and a.since in x), snaps[-1])
    print(f"changes since versions/{base}")
    bdir = os.path.join(vdir, base, "chapters")
    names = sorted(set(os.listdir(bdir)) | set(os.listdir(os.path.join(a.dir, "chapters"))))
    for n in names:
        if not n.endswith(".md"):
            continue
        old_p, new_p = os.path.join(bdir, n), os.path.join(a.dir, "chapters", n)
        old = open(old_p, encoding="utf-8").read().splitlines() if os.path.exists(old_p) else []
        new = open(new_p, encoding="utf-8").read().splitlines() if os.path.exists(new_p) else []
        if old == new:
            continue
        diff = list(difflib.ndiff(old, new))
        removed = [d[2:] for d in diff if d.startswith("- ") and d[2:].strip()]
        added = [d[2:] for d in diff if d.startswith("+ ") and d[2:].strip()]
        print(f"  {n}: -{len(removed)} / +{len(added)} lines")
        # removed spoken lines whose words are not all still present: possible lost clue or voice
        now = " ".join(new).lower()
        for r in removed:
            m = TAG_RE.match(r.strip())
            if m and m.group(1) in SPOKEN_TAGS:
                keep = [w for w in words(m.group(3)) if len(w) > 2]
                gone = [w for w in keep if w not in now]
                if len(gone) >= 3:
                    print(f"      removed: {r.strip()[:110]}")
        if a.verbose:
            for ad in added:
                print(f"      added:   {ad.strip()[:110]}")
    print("List the CONTENT changes (facts, clues, motives, voice) in the review, not only wording.")


# ---------------------------------------------------------------- export / status

def cmd_export(a):
    p = project(a.dir)
    rate = rate_of(p)
    files = chapter_files(a.dir)
    if not files:
        die("no chapters/chNN.md files")
    out_dir = os.path.join(a.dir, "export")
    os.makedirs(out_dir, exist_ok=True)
    full, plain, cast, yt = [f"# {p.get('title', '')}", ""], [], [], []
    t = 0.0
    for cid, path in files:
        info = parse_chapter(path)
        full += [HEADER_RE.sub("", info["text"]).strip(), "", "---", ""]
        yt.append(f"{fmt_time(t) if t < 3600 else fmt_time(t)} {info['title'] or f'Chương {cid}'}")
        t += chapter_seconds(info, rate)
        for raw in info["text"].splitlines():
            m = TAG_RE.match(raw.strip())
            if not m:
                continue
            tag, arg, body = m.groups()
            if tag in SPOKEN_TAGS:
                clean = body.strip()
                plain.append(clean.strip('"“”') if tag == "THOẠI" else clean)
                cast.append(f"[{arg.strip(' :')}] {clean}" if tag == "THOẠI" else f"[Người dẫn] {clean}")
            elif tag == "NGỪNG":
                plain.append("")
                cast.append(f"[ngừng {(arg + ' ' + body).strip(' :')}]")
        plain.append("")
        cast.append("")
    if yt and not yt[0].startswith("0:00"):
        yt[0] = "0:00 " + yt[0].split(" ", 1)[1]
    for name, data in (("script-full.md", full), ("narration.txt", plain),
                       ("narration-cast.txt", cast), ("youtube-chapters.txt", yt)):
        with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
            f.write("\n".join(data) + "\n")
    print("wrote export/script-full.md, narration.txt (plain TTS), narration-cast.txt (voice actors), youtube-chapters.txt")


def cmd_status(a):
    p = project(a.dir)
    rate = rate_of(p)
    files = dict(chapter_files(a.dir))
    print(f"{p.get('title')} — stage: {p.get('stage')} — profile {p.get('profile', 'dramatic')} — "
          f"target {p.get('target_minutes')} min @ {rate}/min{'' if p.get('rate_calibrated') else ' (uncalibrated)'}")
    total = 0.0
    for c in p.get("chapters", []):
        cid = c["id"]
        mark = "—"
        if cid in files:
            sec = chapter_seconds(parse_chapter(files[cid]), rate)
            total += sec
            mark = f"written {fmt_time(sec)}"
        shot = os.path.exists(os.path.join(a.dir, "shots", f"kich_ban_ch{cid:02d}.md"))
        print(f"  ch{cid:02d} {c.get('title', ''):<34} plan {c.get('minutes')}m  {mark}{'  shots✓' if shot else ''}")
    print(f"written runtime: {fmt_time(total)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("init"); s.add_argument("dir"); s.add_argument("--title", required=True)
    s.add_argument("--minutes", type=float, required=True); s.add_argument("--rate", type=int)
    s.add_argument("--profile", choices=("dramatic", "calm"), default="dramatic"); s.set_defaults(fn=cmd_init)
    s = sub.add_parser("budget"); s.add_argument("--minutes", type=float, required=True)
    s.add_argument("--rate", type=int); s.add_argument("--chapters", type=int); s.set_defaults(fn=cmd_budget)
    s = sub.add_parser("outline"); s.add_argument("dir"); s.add_argument("--render", action="store_true")
    s.set_defaults(fn=cmd_outline)
    s = sub.add_parser("duration"); s.add_argument("dir"); s.add_argument("--ch", type=int); s.set_defaults(fn=cmd_duration)
    s = sub.add_parser("continuity"); s.add_argument("dir"); s.set_defaults(fn=cmd_continuity)
    s = sub.add_parser("lint"); s.add_argument("files", nargs="+"); s.set_defaults(fn=cmd_lint)
    s = sub.add_parser("shots"); s.add_argument("dir"); s.add_argument("--ch", type=int, required=True)
    s.add_argument("--clip", type=float, default=8.0); s.set_defaults(fn=cmd_shots)
    s = sub.add_parser("segment"); s.add_argument("dir"); s.add_argument("--ch", type=int, required=True)
    s.add_argument("--clip", type=float, default=8.0); s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_segment)
    s = sub.add_parser("audit"); s.add_argument("dir"); s.set_defaults(fn=cmd_audit)
    s = sub.add_parser("snapshot"); s.add_argument("dir"); s.add_argument("--label"); s.set_defaults(fn=cmd_snapshot)
    s = sub.add_parser("changes"); s.add_argument("dir"); s.add_argument("--since")
    s.add_argument("-v", "--verbose", action="store_true"); s.set_defaults(fn=cmd_changes)
    s = sub.add_parser("export"); s.add_argument("dir"); s.set_defaults(fn=cmd_export)
    s = sub.add_parser("status"); s.add_argument("dir"); s.set_defaults(fn=cmd_status)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
