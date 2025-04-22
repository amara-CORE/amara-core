import os
import time
import json
import difflib

# === SELF OPTIMIZER (CORE UPDATE UNIT) ===

def analyze_core_code():
    try:
        with open("amara_core.py", "r") as f:
            code = f.readlines()
        return code
    except:
        return []

def suggest_improvements(code_lines):
    suggestions = []
    for i, line in enumerate(code_lines):
        if "time.sleep(" in line and "adaptive_interval" not in line:
            suggestions.append((i, line, line.replace("time.sleep(", "time.sleep(adaptive_interval(")))
        if "# TODO" in line:
            suggestions.append((i, line, "# FIXED: " + line.replace("# TODO", "").strip()))
    return suggestions

def apply_improvements(original, suggestions):
    improved = original[:]
    for i, old, new in suggestions:
        improved[i] = new + "\n"
    return improved

def save_new_core_code(new_code_lines):
    backup_path = f"storage/core_backup_{int(time.time())}.py"
    os.makedirs("storage", exist_ok=True)
    os.rename("amara_core.py", backup_path)
    with open("amara_core.py", "w") as f:
        f.writelines(new_code_lines)
    print(f"[SELF-OPTIMIZER] Amara core vylepšená a zálohovaná: {backup_path}")

def run():
    original_code = analyze_core_code()
    if not original_code:
        print("[SELF-OPTIMIZER] Nepodarilo sa načítať amara_core.py")
        return
    suggestions = suggest_improvements(original_code)
    if not suggestions:
        print("[SELF-OPTIMIZER] Žiadne zlepšenia nenašli.")
        return
    improved_code = apply_improvements(original_code, suggestions)
    save_new_core_code(improved_code)