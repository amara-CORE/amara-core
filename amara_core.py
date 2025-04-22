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
        interval = adaptive_interval(config.get("interval", 60))
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
    # === VÝKONOVÝ BOOST + AUTONÓMNE ROZHODNUTIA ===
# Tento modul posúva Amaru na vyššiu úroveň: sleduje, kedy výstupy zarábajú, 
# ktoré jednotky fungujú, a podľa toho rozhoduje o posilnení aktivity.

def adaptive_performance_optimizer():
    log_file = "storage/output.txt"
    try:
        with open(log_file, "r") as f:
            lines = f.readlines()[-10:]  # Sleduj posledných 10 výstupov
        topics = [json.loads(line).get("topic", "unknown") for line in lines]
        top_topic = max(set(topics), key=topics.count)
        log(f"[BOOST] Detegovaný záujem o tému: {top_topic}. Posilňujem generovanie.")
        for _ in range(3):
            generate_output()
    except Exception as e:
        log(f"[BOOST] Zlyhalo zlepšenie výkonu: {e}", "ERROR")

# Aktivuj optimalizáciu každých pár cyklov (samostatné vlákno)
def performance_loop(interval=600):
    while True:
        try:
            adaptive_performance_optimizer()
        except Exception as e:
            log(f"[BOOST] Chyba v optimalizačnom vlákne: {e}", "ERROR")
        time.sleep(interval)

threading.Thread(target=performance_loop, daemon=True).start()
# === ADAPTÍVNE PRISPÔSOBENIE INTERVALU PODĽA ÚSPEŠNOSTI ===

def analyze_performance(window=10):
    path = "storage/output.txt"
    if not os.path.exists(path):
        return 1.0
    with open(path, "r") as f:
        lines = f.readlines()[-window:]
    return sum(1 for line in lines if '"success": true' in line) / max(len(lines), 1)

def adaptive_interval(base=60):
    rate = analyze_performance()
    if rate >= 0.7:
        return base
    elif rate >= 0.4:
        return base * 1.5
    else:
        return base * 3
    from ai_units.self_optimizer import run as optimize_core

def self_update_loop():
    while True:
        try:
            optimize_core()
        except Exception as e:
            log(f"[CORE SELF-UPDATE] Zlyhanie: {e}", "ERROR")
        time.sleep(900)  # každých 15 minút

threading.Thread(target=self_update_loop, daemon=True).start()
def smart_upgrade_generation():
    path = "ai_units/amara_core.py"
    backup_path = f"storage/backups/amara_core_smart_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"

    try:
        with open(path, "r") as f:
            code = f.read()

        # Ak je výstup obmedzený na "text", zmeň to na dynamický výber typu
        if '"type": "text"' in code:
            improved = code.replace(
                '"type": "text"',
                '"type": random.choice(["text", "video", "ebook", "thread"])'
            )

            # Ulož zálohu a prepíš
            os.makedirs("storage/backups", exist_ok=True)
            with open(backup_path, "w") as f:
                f.write(code)
            with open(path, "w") as f:
                f.write(improved)

            print("[SELF-OPTIMIZER] Amara rozšírila typy výstupov (text → video, ebook, thread).")

    except Exception as e:
        print(f"[SELF-OPTIMIZER] Zlyhanie pri smart upgradu: {e}")
        # === AUTONÓMNE ZLEPŠOVANIE AMARY (SELF-OPTIMIZER) ===
from ai_units.modules.self_optimizer import run as run_self_optimizer
threading.Thread(target=run_self_optimizer).start()