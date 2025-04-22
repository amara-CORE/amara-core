import os

def guard_check():
    # Základná ochrana – môžeš neskôr rozšíriť
    allowed = os.environ.get("GUARD_MODE", "ON")
    if allowed != "OFF":
        print("🛡️ Guard AI aktívny – systém bezpečný.")
        return True
    else:
        print("⚠️ Guard AI deaktivovaný! Spustenie zakázané.")
        return False