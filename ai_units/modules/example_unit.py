import random
from datetime import datetime

name = "ExampleUnit"
version = "1.0"
status_state = "Online"

# Simulované úlohy, ktoré jednotka vykonáva
task_pool = [
    "generovanie článku o AI",
    "tvorba e-booku o pasívnom príjme",
    "pridanie affiliate odkazu do blogu",
    "naplánovanie YouTube videa",
    "analýza ziskov z predchádzajúcich výstupov",
    "vylepšenie SEO výstupu"
]

# Hlavná funkcia jednotky
def run():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = random.choice(task_pool)
    success = random.choice([True, True, True, False])  # vysoká úspešnosť
    earnings = round(random.uniform(0.5, 3.0), 2) if success else 0.00
    result = {
        "unit": name,
        "version": version,
        "timestamp": now,
        "task": task,
        "success": success,
        "earnings_bch": earnings,
        "status": "completed" if success else "failed",
        "next_step": "auto-optimize" if success else "retry_later"
    }
    return result

# Stav jednotky – voliteľná API na diagnostiku
def status():
    return {
        "unit": name,
        "version": version,
        "status": status_state,
        "task_count": len(task_pool),
        "ready": True
    }