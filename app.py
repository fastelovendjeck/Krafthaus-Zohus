
import streamlit as st, random

st.set_page_config(page_title="Kraft-Planer • No Supersets", page_icon="🏋️", layout="wide")

EXERCISES = [
  {
    "name": "Back Squat",
    "pattern": "squat",
    "muscle": "Quadrizeps/Gluteus",
    "equip": [
      "barbell"
    ],
    "execution": "Stange auf dem oberen Trapez, Füße schulterbreit, Zehen leicht außen. Core bracen, Hüfte+Knie beugen bis mind. parallel; Knie folgen Fußspitzen. Über Mittelfuß/Ferse explosiv hoch, Rücken neutral."
  },
  {
    "name": "Front Squat",
    "pattern": "squat",
    "muscle": "Quadrizeps/Core",
    "equip": [
      "barbell"
    ],
    "execution": "Front-Rack (Ellenbogen hoch), Oberkörper aufrecht, Core bracen. Tief bis parallel/tiefer; Knie nach vorn über Fuß erlaubt. Druck über Mittelfuß/Ferse, Ellenbogen oben halten."
  },
  {
    "name": "Zercher Squat",
    "pattern": "squat",
    "muscle": "Quadrizeps/Core",
    "equip": [
      "barbell"
    ],
    "execution": "Stange in den Ellenbeugen, Brust hoch. Hüfte+Knie beugen, Knie nach vorn. Stange körpernah, kontrolliert tief, kraftvoll hoch."
  },
  {
    "name": "Safety Bar Squat",
    "pattern": "squat",
    "muscle": "Quadrizeps/Gluteus",
    "equip": [
      "safetybar",
      "barbell"
    ],
    "execution": "Safety-Bar auf dem Rücken, Griffe fassen, Blick neutral. Tief beugen, Knie folgen Fußspitzen. Über Fersen strecken, Core stabil."
  },
  {
    "name": "Box Squat",
    "pattern": "squat",
    "muscle": "Hintere Kette/Quadrizeps",
    "equip": [
      "barbell",
      "box"
    ],
    "execution": "Box hinter dir; Hüfte weit nach hinten, weicher Kontakt (nicht sitzen). Schienbeine fast senkrecht. Aus Fersen druckvoll hoch."
  },
  {
    "name": "Bulgarian Split Squat",
    "pattern": "squat",
    "muscle": "Quadrizeps/Gluteus",
    "equip": [
      "dumbbell",
      "barbell",
      "body"
    ],
    "execution": "Hinterer Fuß auf Bank, vorn Ferse belastet. Torso leicht vor, Core fest. Hüfte gerade nach unten, dann aus der vorderen Ferse hoch."
  },
  {
    "name": "Walking Lunges",
    "pattern": "squat",
    "muscle": "Quadrizeps/Gluteus",
    "equip": [
      "dumbbell",
      "barbell",
      "body"
    ],
    "execution": "Lange Schritte, vordere Ferse belastet, Knie folgt Zehe. Hinteres Knie zum Boden, dann kraftvoll in den nächsten Schritt."
  },
  {
    "name": "Reverse Lunges",
    "pattern": "squat",
    "muscle": "Quadrizeps/Gluteus",
    "equip": [
      "dumbbell",
      "barbell",
      "body"
    ],
    "execution": "Rückwärts ausfallschreiten, Hüfte sinkt zwischen die Füße. Vordere Ferse belastet, Torso aufrecht. Aktiv zurückdrücken."
  },
  {
    "name": "Lateral Lunges",
    "pattern": "squat",
    "muscle": "Adduktoren/Gluteus",
    "equip": [
      "dumbbell",
      "kettlebell",
      "body"
    ],
    "execution": "Seitlich absetzen, Hüfte zurück, Standbein beugen, anderes Bein gestreckt. Fuß flach, dann druckvoll zurück."
  },
  {
    "name": "Step-Ups",
    "pattern": "squat",
    "muscle": "Quadrizeps/Gluteus",
    "equip": [
      "dumbbell",
      "barbell",
      "box"
    ],
    "execution": "Fuß komplett auf Box, Core fest. Über Ferse hoch, Hüfte strecken, kontrolliert absteigen."
  },
  {
    "name": "Hack Squat (Maschine)",
    "pattern": "squat",
    "muscle": "Quadrizeps",
    "equip": [
      "machine"
    ],
    "execution": "Rücken/Schultern anlehnen, Füße leicht vor. Tief beugen, Knie folgen Zehen. Druckvoll strecken, Fersen flach."
  },
  {
    "name": "Cossack Squat",
    "pattern": "squat",
    "muscle": "Adduktoren/Gluteus",
    "equip": [
      "kettlebell",
      "dumbbell",
      "body"
    ],
    "execution": "Sehr breiter Stand, tief in eine Seite, anderes Bein gestreckt/Zehen hoch. Brust hoch, dann aktiv hoch und zur Mitte."
  },
  {
    "name": "Deadlift",
    "pattern": "hinge",
    "muscle": "Gluteus/Beinbeuger",
    "equip": [
      "barbell"
    ],
    "execution": "Füße hüftbreit, Schienbein dicht an der Stange. Lat aktiv, Rücken neutral. Druck in den Boden, Stange nah am Körper, Hüfte+Knie strecken."
  },
  {
    "name": "Romanian Deadlift",
    "pattern": "hinge",
    "muscle": "Beinbeuger/Gluteus",
    "equip": [
      "barbell",
      "dumbbell"
    ],
    "execution": "Leichte Kniebeuge, Hüfte weit zurück, Rücken neutral. Bis Dehnung Beinbeuger, dann Hüfte nach vorn strecken."
  },
  {
    "name": "Trap Bar Deadlift",
    "pattern": "hinge",
    "muscle": "Hintere Kette",
    "equip": [
      "trapbar"
    ],
    "execution": "In Hex-Bar stehen, Brust hoch, Core fest. Druck über Mittelfuß/Ferse, Hüfte+Knie gemeinsam strecken."
  },
  {
    "name": "Sumo Deadlift",
    "pattern": "hinge",
    "muscle": "Adduktoren/Beinbeuger",
    "equip": [
      "barbell"
    ],
    "execution": "Sehr breiter Stand, Hände schmal. Schienbeine senkrecht, Hüfte näher zur Stange. Knie nach außen, Hüfte nach vorn treiben."
  },
  {
    "name": "Deficit Deadlift",
    "pattern": "hinge",
    "muscle": "Beinbeuger/Gluteus",
    "equip": [
      "barbell",
      "plate"
    ],
    "execution": "Auf flacher Erhöhung; mehr Kniewinkel am Start. Stange nah, Rücken neutral, kontrolliert ablassen."
  },
  {
    "name": "Snatch-Grip Deadlift",
    "pattern": "hinge",
    "muscle": "Oberer Rücken/Beinbeuger",
    "equip": [
      "barbell"
    ],
    "execution": "Sehr weiter Griff, Hüfte tiefer, Lat hart. Stange eng am Körper, Rücken flach halten."
  },
  {
    "name": "Good Morning",
    "pattern": "hinge",
    "muscle": "Beinbeuger/Rückenstrecker",
    "equip": [
      "barbell"
    ],
    "execution": "Knie minimal beugen, Hüfte weit zurück, Rücken neutral. Nur so tief wie stabile Spannung; Hüfte nach vorn strecken."
  },
  {
    "name": "Hip Thrust",
    "pattern": "hinge",
    "muscle": "Gluteus",
    "equip": [
      "barbell",
      "bench"
    ],
    "execution": "Oberer Rücken auf Bank, Schienbeine oben vertikal. Core bracen, Hüfte bis Linie Knie–Schulter. Oben Gesäß anspannen, kontrolliert ablassen."
  },
  {
    "name": "Barbell Glute Bridge",
    "pattern": "hinge",
    "muscle": "Gluteus",
    "equip": [
      "barbell"
    ],
    "execution": "Am Boden, Fersen nah am Gesäß. Hüfte strecken, oben Gesäß maximal anspannen, langsam ab."
  },
  {
    "name": "Single-Leg Deadlift",
    "pattern": "hinge",
    "muscle": "Beinbeuger/Gluteus",
    "equip": [
      "dumbbell",
      "kettlebell"
    ],
    "execution": "Einbeiniger Hinge, Becken parallel halten. Gewicht nah am Bein, Rücken neutral, aus der Hüfte aufrichten."
  },
  {
    "name": "Kettlebell Swing",
    "pattern": "hinge",
    "muscle": "Hintere Kette",
    "equip": [
      "kettlebell"
    ],
    "execution": "Hinge-Pendel, kein Squat. KB eng „hiken“, Hüfte explosiv strecken, Arme als Haken, keine Überstreckung."
  },
  {
    "name": "LH Bankdrücken",
    "pattern": "push_h",
    "muscle": "Brust/Trizeps",
    "equip": [
      "barbell",
      "bench"
    ],
    "execution": "Schulterblätter zurück/unten, Füße fest. Zur unteren Brust absenken, Unterarm senkrecht. Explosiv hoch, Gesäß auf Bank."
  },
  {
    "name": "KH Bankdrücken",
    "pattern": "push_h",
    "muscle": "Brust/Trizeps",
    "equip": [
      "dumbbell",
      "bench"
    ],
    "execution": "Ellbogen ~45° zur Körperlinie, tief in Stretch, sauber hoch. Handgelenke neutral, kein Zusammenklatschen."
  },
  {
    "name": "Schrägbankdrücken",
    "pattern": "push_h",
    "muscle": "Obere Brust/Schulter",
    "equip": [
      "barbell",
      "dumbbell",
      "bench"
    ],
    "execution": "Bank 15–30°, Scapulasetzung, Core fest. Pfad leicht bogenförmig zur oberen Brust, kontrollierte Exzentrik."
  },
  {
    "name": "Close-Grip Bench",
    "pattern": "push_h",
    "muscle": "Trizeps/Brust",
    "equip": [
      "barbell",
      "bench"
    ],
    "execution": "Griff schulterbreit, Ellbogen nah am Körper. Zur unteren Brust, lockout aktiv, Handgelenke neutral."
  },
  {
    "name": "Dips (gewichtet)",
    "pattern": "push_h",
    "muscle": "Brust/Trizeps",
    "equip": [
      "dipbar",
      "weightbelt"
    ],
    "execution": "Schultern unten, leichte Vorlage. Bis Oberarm parallel/etwas tiefer, ohne Schwung hochdrücken."
  },
  {
    "name": "Floor Press",
    "pattern": "push_h",
    "muscle": "Trizeps/Brust",
    "equip": [
      "barbell",
      "dumbbell"
    ],
    "execution": "Am Boden begrenzte ROM. Engerer Pfad, Fokus Trizeps/Lockout, kontrolliert bewegen."
  },
  {
    "name": "Langhantel Shoulder Press",
    "pattern": "push_v",
    "muscle": "Delts/Trizeps",
    "equip": [
      "barbell"
    ],
    "execution": "Stand schulterbreit, Rippen runter, Gesäß/Bauch fest. Stange geradlinig über Kopf, Kopf kurz zurück, kein Hohlkreuz."
  },
  {
    "name": "Push Press",
    "pattern": "push_v",
    "muscle": "Delts/Trizeps",
    "equip": [
      "barbell"
    ],
    "execution": "Kleiner Dip, dann Beinantrieb nach oben, Arme verriegeln. Kontrolle beim Absenken."
  },
  {
    "name": "KH Overhead Press",
    "pattern": "push_v",
    "muscle": "Delts/Trizeps",
    "equip": [
      "dumbbell"
    ],
    "execution": "Stehend/sitzend, Core fest, Ellbogen unter Hanteln. Ohne Schwung drücken, oben stabil verriegeln."
  },
  {
    "name": "Arnold Press",
    "pattern": "push_v",
    "muscle": "Delts",
    "equip": [
      "dumbbell"
    ],
    "execution": "Start supiniert vor Brust, beim Drücken nach außen/oben rotieren. Langsam zurückrotieren, sauberer Pfad."
  },
  {
    "name": "Landmine Press",
    "pattern": "push_v",
    "muscle": "Delts/Core",
    "equip": [
      "landmine"
    ],
    "execution": "Diagonal nach vorn-oben drücken, Rippen unten, Core stabil. Ellbogen kontrolliert, gleichmäßig atmen."
  },
  {
    "name": "Barbell Row",
    "pattern": "pull_h",
    "muscle": "Lat/Traps",
    "equip": [
      "barbell"
    ],
    "execution": "Hinge-Position, Rücken neutral. Stange zur Bauchregion, Schulterblätter nach hinten/unten, kontrolliert ablassen."
  },
  {
    "name": "Pendlay Row",
    "pattern": "pull_h",
    "muscle": "Lat/Rückenstrecker",
    "equip": [
      "barbell"
    ],
    "execution": "Torso fast parallel, jede Wdh vom Boden. Explosiv ziehen, unten ablegen, Rücken hart stabil."
  },
  {
    "name": "Dumbbell Rudern",
    "pattern": "pull_h",
    "muscle": "Lat/Rhomboiden",
    "equip": [
      "dumbbell",
      "bench"
    ],
    "execution": "Eine Hand/Knie auf Bank, Rücken flach. Hantel zur Hüfte ziehen, unten voller Stretch, kein Schwung."
  },
  {
    "name": "Gorilla Rows",
    "pattern": "pull_h",
    "muscle": "Lat/Core",
    "equip": [
      "kettlebell",
      "dumbbell"
    ],
    "execution": "Breiter Stand, Hinge. Abwechselnd strikt ziehen, Core gegen Rotation stabilisieren."
  },
  {
    "name": "Seal Row",
    "pattern": "pull_h",
    "muscle": "Lat/Rhomboiden",
    "equip": [
      "barbell",
      "dumbbell",
      "bench"
    ],
    "execution": "Bauchlage auf hoher Bank, ohne Schwung zur Brust. Scapula arbeiten lassen, langsam ablassen."
  },
  {
    "name": "Chest-Supported Row",
    "pattern": "pull_h",
    "muscle": "Lat/Rhomboiden",
    "equip": [
      "machine",
      "bench",
      "dumbbell"
    ],
    "execution": "Brust angelegt, neutraler Rücken. Zur unteren Brust/Taille ziehen, kontrollierte Exzentrik."
  },
  {
    "name": "Kabelrudern",
    "pattern": "pull_h",
    "muscle": "Lat/Rhomboiden",
    "equip": [
      "cable"
    ],
    "execution": "Aufrecht, leichte Hüftbeuge. Griff zur Taille, Schultern unten, Ellbogen hinter den Körper, ruhig vorlassen."
  },
  {
    "name": "Pull-Ups",
    "pattern": "pull_v",
    "muscle": "Lat/Bizeps",
    "equip": [
      "pullupbar"
    ],
    "execution": "Aktiv aushängen, Brust zur Stange, Kinn drüber. Langsam bis volle Streckung ablassen."
  },
  {
    "name": "Chin-Ups",
    "pattern": "pull_v",
    "muscle": "Bizeps/Lat",
    "equip": [
      "pullupbar"
    ],
    "execution": "Supiniert, schulterbreit. Körperspannung, Brust zur Stange, kontrolliert senken."
  },
  {
    "name": "Lat Pulldown",
    "pattern": "pull_v",
    "muscle": "Lat/Rhomboiden",
    "equip": [
      "machine"
    ],
    "execution": "Leichte Rücklage, Stange zur oberen Brust. Ellbogen unten, kontrolliert strecken, Schultern unten halten."
  },
  {
    "name": "Farmer’s Carry",
    "pattern": "carry_core",
    "muscle": "Core/Griffkraft",
    "equip": [
      "dumbbell",
      "kettlebell",
      "trapbar"
    ],
    "execution": "Schwere Gewichte seitlich, Schulterblätter hinten/unten. Aufrecht gehen, kurze Schritte, Rippen unten, ruhige Atmung."
  },
  {
    "name": "Suitcase Carry",
    "pattern": "carry_core",
    "muscle": "Obliques/Core",
    "equip": [
      "dumbbell",
      "kettlebell"
    ],
    "execution": "Einseitig tragen, Becken nicht kippen. Core gegen Seitneigung, kleine kontrollierte Schritte."
  },
  {
    "name": "Front Rack Carry",
    "pattern": "carry_core",
    "muscle": "Oberer Rücken/Core",
    "equip": [
      "barbell",
      "kettlebell"
    ],
    "execution": "Front-Rack, Ellenbogen vorn, Rippen unten. Aufrecht, kleine Schritte, Ellbogen leicht angehoben."
  },
  {
    "name": "Overhead Carry",
    "pattern": "carry_core",
    "muscle": "Schultern/Core",
    "equip": [
      "dumbbell",
      "kettlebell"
    ],
    "execution": "Arm gestreckt über Kopf, Schulterblatt rotiert. Rippen unten, keine Hyperlordose, stabile Linie."
  },
  {
    "name": "Turkish Get-Up",
    "pattern": "carry_core",
    "muscle": "Schulter/Core",
    "equip": [
      "kettlebell"
    ],
    "execution": "Schrittweise aufstehen: Stützen–Hüfte hoch–Durchschieben–Ausfallschritt–Stand. Blick zur KB, Rückweg rückwärts."
  },
  {
    "name": "Pallof Press",
    "pattern": "carry_core",
    "muscle": "Obliques/Anti-Rotation",
    "equip": [
      "cable",
      "band"
    ],
    "execution": "Seitlich zur Zugquelle, Griff vor Brust. Arme vor, Widerstand halten, Becken neutral, ruhig atmen."
  },
  {
    "name": "Ab Wheel Rollout",
    "pattern": "carry_core",
    "muscle": "Bauch/Rückenstrecker",
    "equip": [
      "abwheel"
    ],
    "execution": "Core maximal bracen, langsam vorrollen bis knapp vor Hohlkreuz. Aktiv zurückziehen, Spannung halten."
  },
  {
    "name": "Hanging Straight Leg Raises",
    "pattern": "carry_core",
    "muscle": "Unterer Bauch/Hüftbeuger",
    "equip": [
      "pullupbar"
    ],
    "execution": "Aktiv aushängen, Beine gestreckt über Hüfte heben, am Ende Becken kippen. Ohne Schwung senken."
  },
  {
    "name": "Dead Bug",
    "pattern": "carry_core",
    "muscle": "Core/Koordination",
    "equip": [
      "body"
    ],
    "execution": "LWS in Boden drücken, gegenüberliegend Arm/Bein strecken, Rippen unten, ruhig atmen, Seiten wechseln."
  },
  {
    "name": "Copenhagen Plank",
    "pattern": "carry_core",
    "muscle": "Adduktoren/Core",
    "equip": [
      "body",
      "bench"
    ],
    "execution": "Seitstütz, oberes Bein auf Bank. Hüfte hoch, Core/Adduktoren anspannen, halten oder kurze Wiederholungen."
  },
  {
    "name": "Snatch",
    "pattern": "power",
    "muscle": "Ganzkörper/Explosivkraft",
    "equip": [
      "barbell"
    ],
    "execution": "Weiter Griff, erster Zug kontrolliert, zweiter Zug explosiv Hüfte. Tief im Overhead-Squat fangen, stabil aufstehen."
  },
  {
    "name": "Clean",
    "pattern": "power",
    "muscle": "Ganzkörper/Explosivkraft",
    "equip": [
      "barbell"
    ],
    "execution": "Vom Boden kontrolliert bis Knie, dann Hüfte explosiv, Fangen im Front-Rack. Stabil aufstehen."
  },
  {
    "name": "Clean & Jerk",
    "pattern": "power",
    "muscle": "Ganzkörper/Power",
    "equip": [
      "barbell"
    ],
    "execution": "Clean, dann Dip+Drive, unter der Stange fangen (Split/Power). Über Kopf stabil verriegeln."
  },
  {
    "name": "Power Clean",
    "pattern": "power",
    "muscle": "Hintere Kette/Traps",
    "equip": [
      "barbell"
    ],
    "execution": "Wie Clean, aber höher fangen (halb-knie). Explosiv strecken, weich abfangen."
  },
  {
    "name": "High Pull",
    "pattern": "power",
    "muscle": "Traps/Power",
    "equip": [
      "barbell"
    ],
    "execution": "Explosiv strecken, Ellbogen hoch/außen, Stange körpernah. Ruhig ablassen."
  },
  {
    "name": "Thruster",
    "pattern": "power",
    "muscle": "Quadrizeps/Schultern",
    "equip": [
      "barbell",
      "dumbbell"
    ],
    "execution": "Front Squat + Überkopfdrücken in einem Fluss. Core fest, Pfad sauber, oben verriegeln."
  },
  {
    "name": "Landmine Squat to Press",
    "pattern": "power",
    "muscle": "Beine/Schultern",
    "equip": [
      "landmine"
    ],
    "execution": "Front-Landmine halten, Squat tief, dann diagonal nach vorn-oben drücken. Keine Hyperextension."
  },
  {
    "name": "Sled Push/Drag",
    "pattern": "power",
    "muscle": "Beine/Core",
    "equip": [
      "sled"
    ],
    "execution": "Lehne leicht vor, kräftige Schritte, Spannung halten. Beim Ziehen Core gegen Rotation/Überstreckung stabilisieren."
  }
]
PAIRINGS = {
  "squat": [
    "pull_h",
    "pull_v",
    "carry_core",
    "push_h",
    "push_v"
  ],
  "hinge": [
    "push_h",
    "push_v",
    "carry_core",
    "pull_h",
    "pull_v"
  ],
  "push_h": [
    "pull_h",
    "pull_v",
    "carry_core",
    "hinge"
  ],
  "push_v": [
    "pull_h",
    "pull_v",
    "carry_core",
    "hinge"
  ],
  "pull_h": [
    "push_h",
    "push_v",
    "carry_core",
    "squat"
  ],
  "pull_v": [
    "push_h",
    "push_v",
    "carry_core",
    "squat"
  ],
  "carry_core": [
    "push_h",
    "pull_h",
    "push_v",
    "pull_v",
    "squat",
    "hinge"
  ],
  "power": [
    "pull_h",
    "push_h",
    "carry_core"
  ]
}
PATTERNS_LABEL = {
  "squat": "Knie-dominant (Squat)",
  "hinge": "Hüft-dominant (Hinge)",
  "push_h": "Oberkörper-Druck (Horizontal)",
  "push_v": "Oberkörper-Druck (Vertikal)",
  "pull_h": "Oberkörper-Zug (Horizontal)",
  "pull_v": "Oberkörper-Zug (Vertikal)",
  "carry_core": "Carries & Core",
  "power": "Power/Olympisch"
}

# Styles
st.markdown("""
<style>
:root { --bg:#0B0B0B; --card:#111214; --text:#FFFFFF; --muted:#B8BDC7; --accent:#00E0FF; --border:#1C1E22; }
html, body, [class*="css"] { color:var(--text); background-color:var(--bg); }
.block-card { background:linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,0)); border:1px solid var(--border); border-radius:14px; padding:14px 16px; margin-bottom:12px; }
.badge { display:inline-block; padding:2px 10px; border-radius:999px; font-size:12px; border:1px solid var(--border); color:var(--muted); }
.focus { border-color:var(--accent); box-shadow:0 0 0 1px rgba(0,224,255,.15) inset; }
.kpi { display:flex; gap:12px; margin:.2rem 0 1rem 0; flex-wrap:wrap; }
.kpi .pill { background:#0E0F11; border:1px solid var(--border); border-radius:999px; padding:6px 10px; font-size:12px; color:var(--muted); }
.kpi .pill b { color:var(--text); }
.stDownloadButton > button { border-radius:999px !important; padding:.5rem 1rem; }
.exec { color:var(--muted); font-size:13px; line-height:1.4; margin-top:6px; }
</style>
""", unsafe_allow_html=True)

def equip_ok(ex_equip, available):
    return any(e in available for e in ex_equip) or (len(ex_equip)==1 and ex_equip[0]=="body")

def add_unique_from(pool, used_names, any_pool_if_empty=None):
    candidates = [e for e in pool if e["name"] not in used_names]
    if not candidates and any_pool_if_empty is not None:
        candidates = [e for e in any_pool_if_empty if e["name"] not in used_names]
    if not candidates:
        return None
    pick = random.choice(candidates)
    used_names.add(pick["name"]); return pick

def assert_enough_unique(pool, blocks):
    need = blocks * 2
    if len({e["name"] for e in pool}) < need:
        st.warning(f"Nicht genug unterschiedliche Übungen für {blocks} Blöcke à 2 Übungen. "
                   f"Benötigt: {need}. Verfügbar: {len({e['name'] for e in pool})}. "
                   "Erweitere das Equipment oder aktiviere weitere Kategorien.")

def is_time_based(ex):
    return ex["pattern"]=="carry_core" and any(k in ex["name"] for k in ["Carry","Get-Up","Plank"])

def set_time_seconds(ex, reps):
    if is_time_based(ex):
        return 40 + 10
    return reps*3 + 10

def fixed_reps(ex, is_focus=False):
    p = ex["pattern"]
    if is_time_based(ex): return "40 s"
    if p in ["squat","hinge"]:
        return 5 if (is_focus or "Deadlift" in ex["name"] or "Squat" in ex["name"]) else 6
    if p in ["push_h","push_v","pull_h","pull_v"]:
        return 8
    if p=="power":
        return 3
    if p=="carry_core":
        if any(k in ex["name"] for k in ["Rollout","Raises","Bug","Pallof","Copenhagen"]):
            return 10
        else:
            return "40 s"
    return 8

def plan_time_seconds(plan):
    total=0
    for blk in plan:
        for slot in ["A1","A2"]:
            ex = blk[slot]["exercise"]; cfg = blk[slot]["cfg"]
            reps = cfg["reps"]
            per_set = set_time_seconds(ex, 10 if reps=='40 s' else int(reps))
            total += cfg["sets"] * per_set + max(0, cfg["sets"]-1)*cfg["rest"]
        total += 45
    return total

def adjust_to_time(plan, target_min):
    target = target_min*60
    MIN_REST_FOCUS, MIN_REST_ACC = 150, 60
    MAX_REST_ACC = 90
    def recalc(): return plan_time_seconds(plan)
    cur = recalc()

    while cur > target:
        changed=False
        for blk in plan:
            if not blk["focus"]:
                for slot in ["A1","A2"]:
                    cfg = blk[slot]["cfg"]
                    if cfg["rest"] > MIN_REST_ACC:
                        cfg["rest"] = max(MIN_REST_ACC, cfg["rest"]-10); changed=True
        cur = recalc()
        if cur <= target or changed: break
    while cur > target:
        changed=False
        for blk in plan:
            if blk["focus"]:
                cfg = blk["A2"]["cfg"]
                if cfg["rest"] > 90:
                    cfg["rest"] = max(90, cfg["rest"]-10); changed=True
        cur = recalc()
        if cur <= target or changed: break
    while cur > target:
        changed=False
        for blk in plan:
            if blk["focus"]:
                cfg = blk["A1"]["cfg"]
                if cfg["rest"] > MIN_REST_FOCUS:
                    cfg["rest"] = max(MIN_REST_FOCUS, cfg["rest"]-10); changed=True
        cur = recalc()
        if not changed: break

    tries=0
    while cur < target-60 and tries < 40:
        tries+=1; added=False
        for blk in plan:
            if not blk["focus"]:
                for slot in ["A1","A2"]:
                    cfg = blk[slot]["cfg"]
                    if cfg["rest"] < MAX_REST_ACC:
                        cfg["rest"] += 5; added=True; cur = recalc()
                        if cur >= target-60: break
                if cur >= target-60: break
        if not added: break
    return plan

st.title("Kraft-Planer — keine Supersets (feste Wdh., 3 Sätze/Übung)")
st.caption("Blockweise nacheinander: Jede Übung 3 Sätze mit festen Wiederholungen. Keine Übungsdopplungen pro Einheit.")

col1, col2, col3 = st.columns([1.4,1,1])
with col1:
    blocks = st.radio("Anzahl Blöcke", [3,4], index=0, horizontal=True)
    target_min = st.slider("Gesamtdauer", 35, 60, 45, step=5)
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

excluded = set([x.strip().lower() for x in exclude_list.split(",") if x.strip()])
must_have = [x.strip() for x in must_have_list.split(",") if x.strip()]
available = set(sel_equip)

pool = []
for ex in EXERCISES:
    if ex["name"].lower() in excluded: continue
    if ex["pattern"]=="power" and not include_power: continue
    if not bodyweight_ok and "body" in ex.get("equip",[]) and len(ex.get("equip",[]))==1: continue
    if not equip_ok(ex.get("equip",[]), available): continue
    pool.append(ex)

pool_by_pattern = {}
for ex in pool:
    pool_by_pattern.setdefault(ex["pattern"], []).append(ex)

assert_enough_unique(pool, blocks)

if focus=="Auto":
    focus_pattern = random.choice(["squat","hinge","push_h","push_v"])
elif "Kniebeuge" in focus: focus_pattern = "squat"
elif "Hinge" in focus: focus_pattern = "hinge"
elif "Horizontal Press" in focus: focus_pattern = "push_h"
elif "Vertical Press" in focus: focus_pattern = "push_v"
elif "Horizontal Pull" in focus: focus_pattern = "pull_h"
else: focus_pattern = "pull_v"

used=set(); plan=[]

A1 = add_unique_from(pool_by_pattern.get(focus_pattern, []), used, any_pool_if_empty=pool)
if A1 is None:
    st.error("Keine passende Fokus-Übung gefunden. Bitte Equipment/Filter anpassen."); st.stop()

complist = PAIRINGS.get(focus_pattern, ["pull_h","push_h","carry_core","hinge","squat"])
compl_pat = next((p for p in complist if pool_by_pattern.get(p)), None)
A2 = add_unique_from(pool_by_pattern.get(compl_pat, []), used, any_pool_if_empty=pool)
if A2 is None:
    st.error("Keine Ergänzungsübung gefunden. Bitte Filter anpassen."); st.stop()

plan.append({
    "label":"A","focus":True,
    "A1": {"exercise":A1, "cfg": {"sets":3, "reps": fixed_reps(A1, is_focus=True), "rest":180, "rir":"1–3"}},
    "A2": {"exercise":A2, "cfg": {"sets":3, "reps": fixed_reps(A2, is_focus=False), "rest":90,  "rir":"1–2"}},
})

patterns_cycle = ["squat","hinge","push_h","push_v","pull_h","pull_v","carry_core"]
if focus_pattern in patterns_cycle: patterns_cycle.remove(focus_pattern)

for i in range(blocks-1):
    lead_pat = patterns_cycle[i % len(patterns_cycle)] if patterns_cycle else random.choice(list(PATTERNS_LABEL.keys()))
    if not pool_by_pattern.get(lead_pat): lead_pat = random.choice(list(PATTERNS_LABEL.keys()))
    B1 = add_unique_from(pool_by_pattern.get(lead_pat, []), used, any_pool_if_empty=pool)
    compl = PAIRINGS.get(lead_pat, ["carry_core","pull_h","push_h","hinge","squat"])
    pat2 = next((p for p in compl if pool_by_pattern.get(p)), None)
    B2 = add_unique_from(pool_by_pattern.get(pat2, []), used, any_pool_if_empty=pool)
    if B1 is None or B2 is None:
        st.error("Nicht genug unterschiedliche Übungen für alle Blöcke. Equipment/Filter erweitern."); st.stop()
    plan.append({
        "label": chr(ord("A")+i+1), "focus": False,
        "A1": {"exercise":B1, "cfg": {"sets":3, "reps": fixed_reps(B1, False), "rest":75, "rir":"1–2"}},
        "A2": {"exercise":B2, "cfg": {"sets":3, "reps": fixed_reps(B2, False), "rest":75, "rir":"1–2"}},
    })

plan = adjust_to_time(plan, target_min)

all_names = [blk[slot]["exercise"]["name"] for blk in plan for slot in ["A1","A2"]]
if len(all_names) != len(set(all_names)):
    st.error("Interner Check: doppelte Übung erkannt. Bitte erneut generieren oder Filter anpassen."); st.stop()

total_sec = plan_time_seconds(plan)
st.markdown('<div class="kpi">'
            f'<div class="pill">Ziel: <b>{target_min} min</b></div>'
            f'<div class="pill">Schätzung: <b>{round(total_sec/60)} min</b></div>'
            f'<div class="pill">Blöcke: <b>{blocks}</b></div>'
            '</div>', unsafe_allow_html=True)

def render_exercise(slot):
    ex = slot["exercise"]; cfg = slot["cfg"]
    reps = cfg["reps"]
    st.markdown(f"<div style='display:flex;justify-content:space-between;gap:12px;'><div><div style='font-weight:700;font-size:18px'>{ex['name']}</div><div style='color:var(--muted);font-size:13px'>{PATTERNS_LABEL.get(ex['pattern'], ex['pattern'])} · {ex['muscle']}</div><div class='exec'>{ex['execution']}</div></div><div style='text-align:right'><div style='font-weight:700'>{cfg['sets']} × {reps}</div><div style='color:var(--muted);font-size:13px'>Pause {cfg['rest']} s · RIR {cfg['rir']}</div></div></div>", unsafe_allow_html=True)

st.subheader("Dein Plan (blockweise, keine Supersets)")
for blk in plan:
    st.markdown(f"<div class='block-card {'focus' if blk['focus'] else ''}'><span class='badge'>Block {blk['label']} {'· Fokus' if blk['focus'] else ''}</span>", unsafe_allow_html=True)
    render_exercise(blk["A1"])
    render_exercise(blk["A2"])
    st.markdown("</div>", unsafe_allow_html=True)

lines = ["# 45-Minuten Kraftplan — keine Supersets\n", f"**Blöcke:** {blocks} · **Ziel:** {target_min} min · **Schätzung:** {round(total_sec/60)} min\n"]
for blk in plan:
    lines.append(f"## Block {blk['label']}{' — Fokus' if blk['focus'] else ''}")
    for slot in ["A1","A2"]:
        ex = blk[slot]["exercise"]; cfg = blk[slot]["cfg"]
        lines.append(f"- **{ex['name']}** — {PATTERNS_LABEL.get(ex['pattern'], ex['pattern'])} · {ex['muscle']} · {cfg['sets']} × {cfg['reps']}, Pause {cfg['rest']} s · RIR {cfg['rir']}")
        lines.append(f"  - Ausführung: {ex['execution']}")
    lines.append("")
st.download_button("📥 Plan als Markdown", "\n".join(lines), file_name="kraftplan_no_supersets.md", type="primary")
