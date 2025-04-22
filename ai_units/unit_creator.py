import os
import json
import random
from datetime import datetime
from pathlib import Path

TEMPLATE_PATH = "ai_units/modules/example_unit.py"
OUTPUT_DIR = "ai_units/modules"
REGISTRY_FILE = "ai_units/unit_registry.json"
CONFIG_FILE = "config/config.json"
LOG_FILE = "storage/unit_creator.log"

def log(message):
    os.makedirs("storage", exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] {message}"
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")
    print(line)

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except:
        log("⚠️ Nepodarilo sa načítať konfiguráciu. Pokračujem v predvolenom režime.")
        return {"self_improvement": True}

def generate_unit_name():
    return f"unit_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{random.randint(100,999)}"

def read_template():
    if not os.path.exists(TEMPLATE_PATH):
        log("❌ Šablóna jednotky chýba.")
        return None
    with open(TEMPLATE_PATH, "r") as f:
        return f.read()

def personalize_template(template, name):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return template.replace("example_unit", name).replace("status():", f"status():\n    # Created at {now}")

def save_unit(name, content):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, f"{name}.py")
    if os.path.exists(path):
        log(f"⚠️ Jednotka {name} už existuje, preskakujem.")
        return None
    with open(path, "w") as f:
        f.write(content)
    return path

def register_unit(name, path):
    os.makedirs("ai_units", exist_ok=True)
    if not os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE, "w") as f:
            json.dump([], f)

    with open(REGISTRY_FILE, "r") as f:
        registry = json.load(f)

    registry.append({
        "name": name,
        "path": path,
        "created_at": datetime.now().isoformat()
    })

    with open(REGISTRY_FILE, "w") as f:
        json.dump(registry, f, indent=2)

    log(f"✅ Jednotka {name} zaregistrovaná.")

def create_ai_unit():
    cfg = load_config()
    if not cfg.get("self_improvement", True):
        log("ℹ️ Self-improvement vypnutý. Jednotka nebude vytvorená.")
        return

    template = read_template()
    if not template:
        return

    unit_name = generate_unit_name()
    content = personalize_template(template, unit_name)
    path = save_unit(unit_name, content)

    if path:
        register_unit(unit_name, path)
    else:
        log("❌ Nepodarilo sa uložiť jednotku.")

# Priame spustenie súboru
if __name__ == "__main__":
    create_ai_unit()