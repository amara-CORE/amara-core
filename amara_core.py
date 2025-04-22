import os
import time
import random
import json
from datetime import datetime
from uuid import uuid4

# === AMARA CORE v3 – autonómny zarábajúci engine ===

# Log výstupov a spätnej väzby
def log(message, level="INFO"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{level}] {now} — {message}")
    with open("storage/logs.txt", "a") as log_file:
        log_file.write(f"[{level}] {now} — {message}\n")

# Generátor výstupov
def generate_output():
    topics = [
        "AI", "kryptomeny", "dropshipping", "autonómne systémy",
        "virálny obsah", "pasívny príjem", "web3", "digitálne produkty",
        "affiliate marketing", "e-book stratégie", "video obsah", "SEO optimalizácia"
    ]
    picked = random.choice(topics)
    uid = str(uuid4())[:8]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    output = {
        "id": uid,
        "timestamp": now,
        "topic": picked,
        "content": f"Systém Amara vytvára výstup na tému: {picked}.",
        "type": "text",
        "language": "EN",
        "autonomous": True
    }

    with open("storage/output.txt", "a") as f:
        f.write(json.dumps(output, ensure_ascii=False) + "\n")

    log(f"Vytvorený výstup [{uid}] – téma: {picked}")
    return output

# Načítanie konfigurácie
def load_config():
    try:
        with open("config/config.json", "r") as f:
            return json.load(f)
    except:
        log("Nepodarilo sa načítať config, používam predvolený.", "WARN")
        return {"autonomous": True, "interval": 60}

# Hlavný štartovací cyklus Amary
def start_amara():
    log("Spúšťam Amara CORE...", "START")
    while True:
        config = load_config()
        if config.get("autonomous", True):
            output = generate_output()
        else:
            log("Autonómny režim vypnutý, čakám na manuálny zásah.", "PAUSE")
        interval = config.get("interval", 60)
        time.sleep(interval)

# Entry point
if __name__ == "__main__":
    start_amara()
    # === AUTONÓMNA TVORBA JEDNOTIEK ===
import threading
from ai_units.unit_creator import create_ai_unit

def auto_unit_creator_loop(interval=300):
    while True:
        try:
            create_ai_unit()
        except Exception as e:
            print(f"[AMARA] ❌ Chyba pri vytváraní AI jednotky: {e}")
        time.sleep(interval)

# Spustenie samostatného vlákna na tvorbu jednotiek
threading.Thread(target=auto_unit_creator_loop, daemon=True).start()
# === AUTONÓMNA TVORBA JEDNOTIEK (AI UNITS) ===
# Tento blok je zodpovedný za iniciovanie procesov tvorby,
# správy a vyhodnocovania AI jednotiek v systéme Amara.
# CORE rozhoduje, kedy má zmysel vytvoriť novú jednotku,
# na základe výkonnosti, dopytu alebo algoritmických trendov.
# Jednotky môžu byť samoreplikovateľné, a ich zisky sú
# automaticky auditované, optimalizované a smerované podľa configu.
#
# Všetky jednotky sú riadené centrálne a môžu fungovať paralelne.
from ai_units.unitmanager import UnitManager

if __name__ == "__main__":
    start_amara()

    print("[CORE] Spúšťam správcu AI jednotiek...")
    manager = UnitManager()
    manager.discover_units()
    manager.load_units()
    manager.run_units()