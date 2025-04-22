from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
import string
import os
import json

# === Realistická identita ===
def generate_identity():
    first_names = ["Marek", "Jana", "Tomáš", "Lucia", "Peter", "Eva", "Martin", "Zuzana"]
    last_names = ["Novák", "Kováčová", "Urban", "Horváthová", "Tóth", "Šimek", "Král", "Bartošová"]
    first = random.choice(first_names)
    last = random.choice(last_names)
    username = f"{first.lower()}.{last.lower()}{random.randint(10,99)}"
    email = username + "@examplemail.com"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return {
        "full_name": f"{first} {last}",
        "username": username,
        "email": email,
        "password": password
    }

# === Nastavenie prehliadača (headless režim) ===
def setup_browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)

# === Adaptívna registrácia (AI sa prispôsobí formuláru) ===
def register_on_site():
    identity = generate_identity()
    browser = setup_browser()
    try:
        browser.get("https://example.com/register")  # <- Zmeň na reálnu stránku
        time.sleep(2)

        fields = browser.find_elements(By.TAG_NAME, "input")
        for field in fields:
            name = field.get_attribute("name") or ""
            lname = name.lower()

            if "user" in lname or "name" in lname:
                field.send_keys(identity["username"])
            elif "mail" in lname:
                field.send_keys(identity["email"])
            elif "pass" in lname:
                field.send_keys(identity["password"])

        submit = browser.find_element(By.XPATH, "//input[@type='submit' or @type='button']")
        submit.click()
        print(f"[IDENTITY AGENT] Registrovaný ako: {identity['full_name']} ({identity['email']})")
        return identity

    except Exception as e:
        print(f"[IDENTITY AGENT] Chyba pri registrácii: {e}")
        return None
    finally:
        browser.quit()

# === Záznam a učenie na základe histórie ===
def save_identity(data):
    os.makedirs("storage", exist_ok=True)
    log_file = "storage/identity_log.txt"
    json_file = "storage/identity_log.json"

    with open(log_file, "a") as f:
        f.write(str(data) + "\n")

    try:
        if os.path.exists(json_file):
            with open(json_file, "r") as f:
                log_data = json.load(f)
        else:
            log_data = []

        log_data.append(data)
        with open(json_file, "w") as f:
            json.dump(log_data, f, indent=2)
    except Exception as e:
        print(f"[IDENTITY AGENT] Chyba pri ukladaní JSON: {e}")

    print("[IDENTITY AGENT] Údaje boli uložené a pripravené na autonómne učenie.")

# === Spustenie agenta ===
def run():
    print("[IDENTITY AGENT] Spúšťam autonómnu jednotku pre vytváranie účtov...")
    identity = register_on_site()
    if identity:
        save_identity(identity)
        # === Adaptívne učenie a zlepšovanie ===
def analyze_identities():
    json_file = "storage/identity_log.json"
    if not os.path.exists(json_file):
        print("[IDENTITY AGENT] Žiadne záznamy na analýzu.")
        return

    with open(json_file, "r") as f:
        data = json.load(f)

    domains = {}
    usernames = []

    for entry in data:
        email = entry.get("email", "")
        if "@" in email:
            domain = email.split("@")[1]
            domains[domain] = domains.get(domain, 0) + 1
        usernames.append(entry.get("username", ""))

    most_common_domain = max(domains, key=domains.get, default="unknown")
    print(f"[LEARNING] Najčastejšie používaná doména: {most_common_domain}")
    print(f"[LEARNING] Posledných 5 používateľských mien: {usernames[-5:]}")
    print("[LEARNING] Pripravený na ďalšie učenie a optimalizáciu.")

# === Samospustenie pre učenie po registráciách ===
if __name__ == "__main__":
    run()
    time.sleep(1)
    analyze_identities()
    # === Dynamická doména podľa úspešnosti ===
def get_best_email_domain():
    fallback_domains = ["examplemail.com", "testmail.ai", "trymebot.io"]
    stats_file = "storage/domain_stats.json"
    
    try:
        if os.path.exists(stats_file):
            with open(stats_file, "r") as f:
                stats = json.load(f)
        else:
            stats = {d: 0 for d in fallback_domains}

        # Vyber najčastejšie fungujúcu
        best = max(stats, key=stats.get, default=fallback_domains[0])
        return best
    except:
        return fallback_domains[0]

def record_domain_success(domain):
    stats_file = "storage/domain_stats.json"
    if os.path.exists(stats_file):
        with open(stats_file, "r") as f:
            stats = json.load(f)
    else:
        stats = {}

    stats[domain] = stats.get(domain, 0) + 1

    with open(stats_file, "w") as f:
        json.dump(stats, f, indent=2)

# === Testovacia simulácia na vlastnej stránke ===
def simulate_dummy_site():
    identity = generate_identity()
    domain = get_best_email_domain()
    identity["email"] = identity["username"] + "@" + domain

    print(f"[SIMULÁTOR] Testujem registráciu pre {identity['email']}...")
    time.sleep(1.2)
    print(f"[SIMULÁTOR] Úspešná registrácia simulovaná.")
    record_domain_success(domain)
    save_identity(identity)

# === Spúšťanie režimu TEST alebo LIVE ===
def full_autonomous_mode():
    mode = os.environ.get("IDENTITY_MODE", "LIVE")

    if mode == "TEST":
        print("[AGENT] Spúšťam v TEST režime.")
        simulate_dummy_site()
    else:
        print("[AGENT] Spúšťam v LIVE režime.")
        run()

    analyze_identities()

# === Skutočný štart systému ===
if __name__ == "__main__":
    full_autonomous_mode()
    # === Pokročilé generovanie hesla podľa vzoru ===
def generate_secure_password(pattern="Aa1!Aa1!"):
    symbols = "!@#$%&*"
    password = ""
    for char in pattern:
        if char == "A":
            password += random.choice(string.ascii_uppercase)
        elif char == "a":
            password += random.choice(string.ascii_lowercase)
        elif char == "1":
            password += random.choice(string.digits)
        elif char == "!":
            password += random.choice(symbols)
        else:
            password += char
    return password

# === Generovanie geo-lokalizovaných mien (SK, CZ, US) ===
def generate_geo_identity(region="SK"):
    if region == "CZ":
        first_names = ["Jan", "Petr", "Anna", "Tereza"]
        last_names = ["Svoboda", "Dvořák", "Novotná", "Beneš"]
    elif region == "US":
        first_names = ["John", "Emily", "Michael", "Sarah"]
        last_names = ["Smith", "Johnson", "Williams", "Brown"]
    else:  # SK default
        first_names = ["Marek", "Lucia", "Peter", "Zuzana"]
        last_names = ["Novák", "Tóthová", "Horváth", "Kováčová"]

    first = random.choice(first_names)
    last = random.choice(last_names)
    username = f"{first.lower()}.{last.lower()}{random.randint(100,999)}"
    email = username + "@" + get_best_email_domain()
    password = generate_secure_password()

    return {
        "full_name": f"{first} {last}",
        "username": username,
        "email": email,
        "password": password,
        "region": region
    }