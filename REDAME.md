# Amara CORE V3 – Plne autonómny AI systém na generovanie legálneho zisku

Amara CORE je neurónovo riadený, bezpečnostne chránený a výstupovo orientovaný AI systém s jediným cieľom: **generovať legálny zisk pre používateľa bez potreby zásahu.**

---

## Obsah systému

### `main.py`
Spúšťač celého systému – inicializuje FastAPI server, overuje bezpečnosť cez Guard AI a spúšťa výstupný engine Amary.

### `core/amara_core.py`
Autonómny engine, ktorý generuje obsah (text, video, e-booky) v intervaloch. Využíva stratégiu `auto_trend + predefined_topics + random_choice`, zapisuje výstupy do `storage/output.txt`.

### `guard/guard_ai.py`
Bezpečnostný modul, ktorý vykonáva predštartovú kontrolu systému. Detekuje zmeny v kóde, podozrivé úpravy a zastavuje štart, ak je systém mimo bezpečného režimu.

### `config/config.json`
Centrálne nastavenia – jazyk, cieľové trhy, výstupné formáty, zapnutie samovylepšovania a BCH peňaženka.

### `storage/output.txt`
Zapisujú sa sem všetky výstupy AI systému v inteligentnej štruktúre – názov, typ, zisk, timestamp, spätná väzba.

### `requirements.txt`
Zoznam knižníc potrebných na spustenie systému.

---

## Funkcie

- **Autonómne generovanie zarábajúceho obsahu** (články, videá, PDF, e-booky, affiliate výstupy)
- **Zber trendov** a adaptácia výstupov na základe algoritmov platforiem
- **Self-programming** – systém sa dokáže sám upraviť a vylepšiť s cieľom zvýšiť výkon a zisk
- **Guard AI** – nezávislý bezpečnostný štít sledujúci integrity systému
- **Multijazyčné výstupy** – angličtina, čínština, slovenčina (dynamicky prepínané)
- **Auto-replikácia (Auto-Genesis)** – ak niečo zarába, systém to vie sám rozšíriť
- **Profit redirekcia** – výnosy smerované na BCH peňaženku používateľa

---

## Nastavenia a konfigurácia (`config/config.json`)

```json
{
  "project_name": "Amara",
  "autonomy": true,
  "guard_ai_enabled": true,
  "self_improvement": true,
  "output_modes": ["article", "video", "ebook", "dropshipping", "affiliate"],
  "languages": ["en", "zh", "sk"],
  "crypto_wallet": {
    "type": "BCH",
    "address": "qzxacgqtx02la20e7wlmef9wggkuakvkl5nqqmn9rx"
  },
  "profit_distribution": {
    "send_to_user": 70,
    "reinvest": 30,
    "initial_hold": 5
  },
  "auto_genesis": true,
  "target": "maximize_legal_profit"
}