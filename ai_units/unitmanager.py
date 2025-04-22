import os
import importlib
import time
import traceback

class AIUnit:
    def __init__(self, name, module_path):
        self.name = name
        self.module_path = module_path
        self.module = None
        self.active = False

    def load(self):
        try:
            self.module = importlib.import_module(self.module_path)
            self.active = True
            print(f"[LOAD] Jednotka {self.name} načítaná.")
        except Exception as e:
            print(f"[ERROR] Načítanie jednotky {self.name} zlyhalo: {e}")
            traceback.print_exc()
            self.active = False

    def execute(self):
        if self.active and self.module:
            try:
                result = self.module.run()
                print(f"[EXECUTE] Výsledok jednotky {self.name}: {result}")
                return result
            except Exception as e:
                print(f"[ERROR] Výkon jednotky {self.name} zlyhal: {e}")
                traceback.print_exc()
                return None
        return None

class UnitManager:
    def __init__(self, directory="ai_units/modules"):
        self.directory = directory
        self.units = []

    def discover_units(self):
        print("[DISCOVER] Hľadanie jednotiek...")
        for filename in os.listdir(self.directory):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]
                unit = AIUnit(module_name, f"ai_units.modules.{module_name}")
                self.units.append(unit)
        print(f"[DISCOVER] Nájdených jednotiek: {len(self.units)}")

    def load_all(self):
        for unit in self.units:
            unit.load()

    def run_all(self):
        for unit in self.units:
            unit.execute()

    def loop(self, interval=60):
        while True:
            self.run_all()
            time.sleep(interval)

if __name__ == "__main__":
    manager = UnitManager()
    manager.discover_units()
    manager.load_all()
    manager.loop()