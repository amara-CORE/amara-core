import time
from datetime import datetime
import random

def generate_output():
    topics = ["AI", "kryptomeny", "dropshipping", "zarábanie", "psychológia", "trendy", "zdravie"]
    picked = random.choice(topics)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"[{now}] Amara vytvorila článok na tému: {picked}"

    with open("storage/output.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

    print("✅ Vytvorený obsah:", text)

def start_amara():
    print("🚀 Amara CORE aktívna – generovanie prebieha...")
    while True:
        generate_output()
        time.sleep(60)  # každú minútu