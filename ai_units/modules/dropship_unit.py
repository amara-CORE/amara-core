import requests
import random
import os
from datetime import datetime

OUTPUT_FILE = "storage/output.txt"
API_URL = "https://fakestoreapi.com/products"

# === Záložné produkty ===
FALLBACK_PRODUCTS = [
    {
        "title": "Smart LED Light Strip",
        "description": "Create mood lighting at home with smart LED colors.",
        "price": 19.99,
        "profit": 8.5,
        "affiliate_url": "https://example.com/led-strip"
    },
    {
        "title": "Posture Corrector",
        "description": "Fix your posture and reduce back pain with daily use.",
        "price": 14.49,
        "profit": 6.2,
        "affiliate_url": "https://example.com/posture"
    },
    {
        "title": "Portable Blender",
        "description": "Blend your smoothies on the go, USB charged.",
        "price": 22.99,
        "profit": 9.3,
        "affiliate_url": "https://example.com/blender"
    }
]

# === Získanie real-time produktov z API ===
def fetch_products():
    try:
        response = requests.get(API_URL, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for product in data:
                product["profit"] = round(product["price"] * random.uniform(0.2, 0.5), 2)
                product["affiliate_url"] = f"https://yourstore.com/product/{product['id']}"
            return data
        else:
            print(f"[DROPSHIP] Chyba API: {response.status_code}")
    except Exception as e:
        print(f"[DROPSHIP] API výpadok: {e}")
    return FALLBACK_PRODUCTS

# === Pomocné funkcie ===
def generate_tags(product):
    words = product['title'].lower().split()
    return " ".join(["#dropshipping", "#ai"] + [f"#{w}" for w in words[:3]])

def generate_seo_title(product):
    return f"{product['title']} – {product['description'].split('.')[0]}"

def generate_block(product):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"""
[DROPSHIP UNIT REPORT]
Generated: {timestamp}

Product: {product['title']}
Price: ${product['price']} | Profit: ${product['profit']}
SEO Title: {generate_seo_title(product)}

Description:
{product['description']}

Affiliate Link: {product['affiliate_url']}
Tags: {generate_tags(product)}

[END REPORT]
"""

def save_output(text):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "a") as f:
        f.write(text + "\n")
    print("[DROPSHIP] Výstup bol uložený.")

# === Spustenie jednotky ===
def run():
    print("[DROPSHIP] Načítavam produkty...")
    products = fetch_products()
    best = max(products, key=lambda p: p["profit"])
    print(f"[DROPSHIP] Vybraný produkt: {best['title']} (${best['profit']} zisk)")
    block = generate_block(best)
    save_output(block)