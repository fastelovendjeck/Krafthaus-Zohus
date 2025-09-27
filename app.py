
import streamlit as st, json, random, math, os

st.set_page_config(page_title="45-Min Kraft-Planer", page_icon="💪", layout="wide")

# ---------- Styles (Freeletics-esque) ----------------------------------------
st.markdown("""
<style>
:root {
  --bg: #0B0B0B;
  --card: #111214;
  --text: #FFFFFF;
  --muted: #B8BDC7;
  --accent: #00E0FF;
  --accent-2: #6BFFB8;
  --border: #1C1E22;
}
html, body, [class*="css"]  { color: var(--text); background-color: var(--bg); }
section.main > div { padding-top: 0.6rem; }
h1, h2, h3 { letter-spacing: .4px; }
.block-card {
  background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.00));
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 14px 16px;
  margin-bottom: 12px;
}
.badge { display:inline-block; padding:2px 10px; border-radius:999px; font-size:12px; border:1px solid var(--border); color: var(--muted); }
.focus { border-color: var(--accent); box-shadow: 0 0 0 1px rgba(0,224,255,.15) inset; }
.kpi { display:flex; gap:12px; margin:.2rem 0 1rem 0; flex-wrap:wrap; }
.kpi .pill { background:#0E0F11; border:1px solid var(--border); border-radius:999px; padding:6px 10px; font-size:12px; color:var(--muted); }
.kpi .pill b { color: var(--text); }
hr { border-color: var(--border); }
.stDownloadButton > button { border-radius: 999px !important; padding: .5rem 1rem; }
</style>
""", unsafe_allow_html=True)

# ---------- Data --------------------------------------------------------------
BASE = os.path.dirname(__file__)
def load_json(name):
    with open(os.path.join(BASE, name), "r", encoding="utf-8") as f:
        return json.load(f)
EXERCISES = load_json("exercises.json")
PAIRINGS = load_json("pairings.json")
PATTERNS_LABEL = load_json("patterns_label.json")

def equip_ok(ex_equip, available):
    return any(e in available for e in ex_equip) or (len(ex_equip)==1 and ex_equip[0]=="body")
def pick_exercise(pool, used_names):
    cand = [e for e in pool if e["name"] not in used_names] or pool
    return random.choice(cand)
def estimate_set_time_seconds(reps, type_):
    return (reps + 3) * 3 if type_=="lift" else reps + 10
def is_time_based(ex):
    if ex["pattern"] != "carry_core": return False
    return any(k in ex["name"] for k in ["Carry","Get-Up"])
def reps_label(ex, low, high):
    if is_time_based(ex): return "30–45 s"
    if ex["pattern"] == "carry_core" and any(k in ex["name"] for k in ["Rollout","Plank","Bug","Raises","Pallof"]):
        return "8–12"
    return f"{low}–{high}"
def default_cfg(is_focus):
    if is_focus:
        return {"A1":{"sets":4,"reps_range":[4,6],"rest":150},
                "A2":{"sets":3,"reps_range":[6,8],"rest":60}}
    return {"A1":{"sets":3,"reps_range":[6,10],"rest":75},
            "A2":{"sets":3,"reps_range":[6,10],"rest":75}}
def plan_time_seconds(plan):
    total=0
    for blk in plan:
        for slot in ["A1","A2"]:
            ex, cfg = blk[slot]["exercise"], blk[slot]["cfg"]
            sets = cfg["sets"]; low, high = cfg["reps_range"]
            reps = (low+high)//2
            set_time = estimate_set_time_seconds(40, "carry") if is_time_based(ex) else estimate_set_time_seconds(reps,"lift")
            total += sets*set_time + max(0, sets-1)*cfg["rest"]
        total += 50  # block transition
    return total
def adjust_to_time(plan, target_min):
    target = target_min*60
    MIN_REST_FOCUS, MIN_REST_ACC = 120, 45
    MAX_REST_ACC = 90
    def recalc(): return plan_time_seconds(plan)
    cur = recalc(); changed = True
    while cur > target and changed:
        changed=False
        # reduce accessory rest
        for blk in plan:
            if not blk["focus"]:
                for slot in ["A1","A2"]:
                    cfg=blk[slot]["cfg"]
                    if cfg["rest"]>MIN_REST_ACC:
                        cfg["rest"]=max(MIN_REST_ACC,cfg["rest"]-10); changed=True
        cur = recalc()
        if cur<=target: break
        # drop accessory sets
        for blk in plan:
            if blk["focus"]: continue
            for slot in ["A1","A2"]:
                cfg=blk[slot]["cfg"]
                if cfg["sets"]>2:
                    cfg["sets"]-=1; changed=True; cur=recalc()
                    if cur<=target: break
            if cur<=target: break
        if cur<=target: break
        # reduce focus A2 sets
        for blk in plan:
            if blk["focus"]:
                cfg=blk["A2"]["cfg"]
                if cfg["sets"]>2:
                    cfg["sets"]-=1; changed=True
        cur=recalc()
        if cur<=target: break
        # reduce focus A1 rest
        for blk in plan:
            if blk["focus"]:
                cfg=blk["A1"]["cfg"]
                if cfg["rest"]>MIN_REST_FOCUS:
                    cfg["rest"]=max(MIN_REST_FOCUS,cfg["rest"]-10); changed=True
        cur=recalc()
        if cur<=target: break
        # reduce focus A1 sets to 3
        for blk in plan:
            if blk["focus"]:
                cfg=blk["A1"]["cfg"]
                if cfg["sets"]>3:
                    cfg["sets"]-=1; changed=True
        cur=recalc()
    tries=0
    while cur<target-60 and tries<40:
        tries+=1; added=False
        for blk in plan:
            if not blk["focus"]:
                for slot in ["A1","A2"]:
                    cfg=blk[slot]["cfg"]
                    if cfg["rest"]<MAX_REST_ACC:
                        cfg["rest"]+=5; added=True; cur=recalc()
                        if cur>=target-60: break
                if cur>=target-60: break
        if added: continue
        for blk in plan:
            if not blk["focus"]:
                for slot in ["A1","A2"]:
                    cfg=blk[slot]["cfg"]
                    if cfg["sets"]<4:
                        cfg["sets"]+=1; added=True; cur=recalc(); break
            if added: break
        if not added: break
    return plan

# ---------- UI ----------------------------------------------------------------
st.title("45-Minuten Kraft-Planer")
st.caption("Freeletics-ähnliche Optik · Fokusblock + 2er-Supersets · Zielzeit angepasst")

col1, col2, col3 = st.columns([1.2,1,1])
with col1:
    blocks = st.radio("Anzahl Blöcke", [3,4], index=1, horizontal=True)
    target_min = st.slider("Gesamtdauer", 35, 60, 45, step=5, help="Zielzeit inkl. Pausen & Übergängen")
with col2:
    focus = st.selectbox("Fokus für Block A", ["Auto","Kniebeuge (Squat)","Hinge (Deadlift)","Horizontal Press","Vertical Press","Horizontal Pull","Vertical Pull"])
with col3:
    eq_all = ["barbell","bench","dumbbell","kettlebell","machine","cable","pullupbar","dipbar","trapbar","plate","landmine","box","sled","band","abwheel","safetybar"]
    sel_equip = st.multiselect("Ausstattung", eq_all, default=["barbell","bench","dumbbell","kettlebell","pullupbar","cable"])

adv = st.expander("Erweitert", expanded=False)
with adv:
    include_power = st.checkbox("Power/Olympische Lifts", value=False)
    bodyweight_ok = st.checkbox("Körpergewichtsübungen zulassen", value=True)
    exclude_list = st.text_input("Übungen ausschließen (Komma-getrennt)", value="")
    must_have_list = st.text_input("Bevorzugte Übungen (Komma-getrennt)", value="")

# Filter
excluded = set([x.strip().lower() for x in exclude_list.split(",") if x.strip()])
must_have = [x.strip() for x in must_have_list.split(",") if x.strip()]
available = set(sel_equip)

pool = []
for ex in EXERCISES:
    if ex["name"].lower() in excluded: continue
    if ex["pattern"]=="power" and not include_power: continue
    if not bodyweight_ok and "body" in ex["equip"] and len(ex["equip"])==1: continue
    if not equip_ok(ex["equip"], available): continue
    pool.append(ex)

pool_by_pattern = {}
for ex in pool:
    pool_by_pattern.setdefault(ex["pattern"], []).append(ex)

def choose_by_pattern(p, used):
    cand = pool_by_pattern.get(p, [])
    return pick_exercise(cand or pool, used)

# Focus pattern
if focus=="Auto":
    focus_pattern = random.choice(["squat","hinge","push_h","push_v"])
elif "Kniebeuge" in focus: focus_pattern = "squat"
elif "Hinge" in focus: focus_pattern = "hinge"
elif "Horizontal Press" in focus: focus_pattern = "push_h"
elif "Vertical Press" in focus: focus_pattern = "push_v"
elif "Horizontal Pull" in focus: focus_pattern = "pull_h"
else: focus_pattern = "pull_v"

# Build plan
used=set(); plan=[]

# try to inject must_have first if in pool
def try_pick_by_name(name):
    for e in pool:
        if e["name"].lower()==name.lower() and e["name"] not in used:
            used.add(e["name"]); return e
    return None

A1 = try_pick_by_name(must_have[0]) if must_have else None
if not A1 or A1["pattern"]!=focus_pattern:
    A1 = choose_by_pattern(focus_pattern, used)
used.add(A1["name"])

complist = PAIRINGS.get(focus_pattern, ["pull_h","push_h","carry_core","hinge","squat"])
compl_pat = next((p for p in complist if pool_by_pattern.get(p)), random.choice(list(PATTERNS_LABEL.keys())))
A2 = choose_by_pattern(compl_pat, used); used.add(A2["name"])
blockA_cfg = default_cfg(is_focus=True)
plan.append({"label":"A","focus":True,"A1":{"exercise":A1,"cfg":blockA_cfg["A1"]},"A2":{"exercise":A2,"cfg":blockA_cfg["A2"]}})

patterns_cycle = ["squat","hinge","push_h","push_v","pull_h","pull_v","carry_core"]
if focus_pattern in patterns_cycle: patterns_cycle.remove(focus_pattern)

for i in range(blocks-1):
    pat = patterns_cycle[i % len(patterns_cycle)] if patterns_cycle else random.choice(list(PATTERNS_LABEL.keys()))
    if not pool_by_pattern.get(pat): pat = random.choice(list(PATTERNS_LABEL.keys()))
    B1 = choose_by_pattern(pat, used); used.add(B1["name"])
    compl = PAIRINGS.get(pat, ["carry_core","pull_h","push_h","hinge","squat"])
    pat2 = next((p for p in compl if pool_by_pattern.get(p)), random.choice(list(PATTERNS_LABEL.keys())))
    B2 = choose_by_pattern(pat2, used); used.add(B2["name"])
    cfg = default_cfg(is_focus=False)
    plan.append({"label": chr(ord("A")+i+1),"focus":False,"A1":{"exercise":B1,"cfg":cfg["A1"]},"A2":{"exercise":B2,"cfg":cfg["A2"]}})

plan = adjust_to_time(plan, target_min)

# ---------- Output ------------------------------------------------------------
total_sec = plan_time_seconds(plan)
st.markdown('<div class="kpi">'
            f'<div class="pill">Ziel: <b>{target_min} min</b></div>'
            f'<div class="pill">Schätzung: <b>{round(total_sec/60)} min</b></div>'
            f'<div class="pill">Blöcke: <b>{blocks}</b></div>'
            '</div>', unsafe_allow_html=True)

def render_block(blk):
    tag = "Fokus" if blk["focus"] else "Superset"
    st.markdown(f'<div class="block-card {"focus" if blk["focus"] else ""}"><span class="badge">Block {blk["label"]} · {tag}</span>', unsafe_allow_html=True)
    for slot in ["A1","A2"]:
        ex = blk[slot]["exercise"]; cfg = blk[slot]["cfg"]
        low, high = cfg["reps_range"]
        st.markdown(f"""
        <div style='display:flex;justify-content:space-between;gap:12px;margin-top:10px'>
          <div style='flex:1'>
            <div style='font-weight:700;font-size:18px'>{ex['name']}</div>
            <div style='color:var(--muted);font-size:13px'>{PATTERNS_LABEL.get(ex['pattern'], ex['pattern'])} · {ex['muscle']}</div>
          </div>
          <div style='text-align:right'>
            <div style='font-weight:700'>{cfg["sets"]} × {reps_label(ex, low, high)}</div>
            <div style='color:var(--muted);font-size:13px'>Pause {cfg["rest"]} s</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.subheader("Dein Plan")
for blk in plan:
    render_block(blk)

# Export
lines = ["# 45-Minuten Kraftplan\n", f"**Blöcke:** {blocks} · **Ziel:** {target_min} min · **Schätzung:** {round(total_sec/60)} min\n"]
for blk in plan:
    lines.append(f"## Block {blk['label']}{' — Fokus' if blk['focus'] else ''}")
    for slot in ["A1","A2"]:
        ex = blk[slot]["exercise"]; cfg = blk[slot]["cfg"]; low, high = cfg["reps_range"]
        lines.append(f"- **{ex['name']}** — {PATTERNS_LABEL.get(ex['pattern'], ex['pattern'])} · {ex['muscle']} · {cfg['sets']} × {reps_label(ex, low, high)}, Pause {cfg['rest']} s")
    lines.append("")
md = "\n".join(lines)
st.download_button("📥 Plan als Markdown", md, file_name="kraftplan.md", type="primary")

with st.expander("Hinweise & Progression", expanded=False):
    st.write("""
- **Block A zuerst**: schwer, 4×4–6, 120–180 s Pause.
- **Supersets** in B/C/D: abwechselnd A1/A2, 45–90 s Pause, sauberer Rhythmus.
- **Progression**: Wenn alle Zielwdh. sauber → +2.5–5 kg (Oberkörper) / +5–10 kg (Unterkörper).
- **Tempo**: 3 s exzentrisch, zügig konzentrisch, volle ROM.
""")
