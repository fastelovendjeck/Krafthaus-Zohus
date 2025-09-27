
# 45-Minuten Kraft-Planer – iPhone (kostenlos)

Erstellt Trainingspläne mit **3–4 Blöcken × 2 Übungen** für **~45 Min**. Freeletics-ähnliche UI, läuft als Web-App-Icon auf dem iPhone.

---

## 0) Was du brauchst
- **GitHub Account** (free)
- **Streamlit Community Cloud** (free)
- iPhone mit Safari

---

## 1) Repo auf GitHub anlegen (direkt am iPhone)
1. Öffne **github.com** in Safari → einloggen.
2. Tippe rechts oben auf **+** → **New repository**.
3. Name: `kraftplan-app` · **Private** · Create.
4. Dateien hochladen (**Add file → Upload files**):
   - `app.py`
   - `requirements.txt`
   - `exercises.json`
   - `pairings.json`
   - `patterns_label.json`
5. **Commit changes**.

> Tipp: Du kannst die Dateien hier aus dem Chat herunterladen und direkt auf GitHub hochladen.

---

## 2) Kostenlos deployen (Streamlit Cloud)
1. Öffne **streamlit.io/cloud** → **Sign in** (GitHub/Google).
2. **Deploy an app** → Dein Repo wählen.
3. **Main file path** = `app.py` → **Deploy**.
4. Nach kurzer Zeit bekommst du eine URL wie `https://…streamlit.app`.

Wenn du später Änderungen an Dateien in GitHub speicherst, baut Streamlit automatisch neu.

---

## 3) App auf den iPhone‑Home‑Screen
1. Öffne die App‑URL in **Safari**.
2. Tippe **Teilen** (Quadrat mit Pfeil) → **Zum Home‑Bildschirm**.
3. Name: „Kraft‑Planer“ → **Hinzufügen**. Fertig.

---

## 4) Nutzung
- Wähle **3 oder 4 Blöcke**, **Zielzeit** (Standard 45 Min), **Fokus‑Muster**, **Equipment**.
- Optional: **Power/Olympic** aktivieren, Übungen **bevorzugen**/**ausschließen**.
- Die App passt **Sätze & Pausen** auf die Zielzeit an und exportiert den Plan als **Markdown**.

---

## 5) Deinen Übungskatalog anpassen
- Öffne z. B. `exercises.json` → **Edit** in GitHub.
- Felder pro Übung:
  - `name` (String) – z. B. „Back Squat“
  - `pattern` (Enum) – `squat|hinge|push_h|push_v|pull_h|pull_v|carry_core|power`
  - `muscle` (String) – kurzer Fokus
  - `equip` (Liste) – z. B. `["barbell","bench"]`
- Die Labels je `pattern` stehen in `patterns_label.json`.
- Logische **Kombinationen** (Supersets) definierst du in `pairings.json`.

---

## 6) Freeletics‑ähnliche UI
- Dunkles, kontrastreiches Design, **Pills** für KPI (Ziel/Schätzung/Blöcke), **Cards** pro Block, Badge „Fokus“.
- Mobile‑optimierte Typo/Abstände; große Touch‑Targets; Download‑Button als Primäraktion.
- Du kannst die Farben im CSS‑Block (`--accent`, `--accent-2`) anpassen.

---

## 7) Häufige Fragen
**Offline?** Streamlit läuft im Web, daher Internet erforderlich.  
**Kosten?** GitHub Free + Streamlit Cloud Free = 0 €.  
**Eigenes Icon?** Über „Zum Home‑Bildschirm“ generiert iOS automatisch ein Icon.  
**Datenschutz?** Es werden keine persönlichen Trainingsdaten gespeichert; der Plan wird nur im Browser angezeigt.

Stand: 2025-09-27
