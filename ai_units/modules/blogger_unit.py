import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

OUTPUT_HTML = "storage/blog.html"
TREND_SOURCES = [
    "https://refresher.sk/",
    "https://www.startitup.sk/"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_trending_articles():
    articles = []
    for url in TREND_SOURCES:
        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")
            links = soup.find_all("a", href=True)
            for link in links:
                href = link["href"]
                if href.startswith("https://") and len(href) < 150:
                    articles.append(href)
        except Exception as e:
            print(f"[BLOGGER] Chyba pri načítaní {url}: {e}")
    return list(set(articles))[:5]

def copy_article_text(article_url):
    try:
        r = requests.get(article_url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = "\n".join([p.get_text() for p in paragraphs if len(p.get_text()) > 40])
        return content[:3000] + "..." if content else None
    except Exception as e:
        print(f"[BLOGGER] Chyba pri kopírovaní: {e}")
        return None

def generate_html_entry(title, url, content):
    return f"""
    <article style='margin-bottom: 40px; font-family: sans-serif;'>
        <h2>{title}</h2>
        <p><i>Zdroj: <a href="{url}" target="_blank">{url}</a></i></p>
        <p style='white-space: pre-wrap;'>{content}</p>
        <hr>
    </article>
    """

def save_html(entries):
    os.makedirs("storage", exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    html = f"""
    <html>
    <head><meta charset='utf-8'><title>AI Blog – {timestamp}</title></head>
    <body>
    <h1>Autonómny AI Blog – generovaný {timestamp}</h1>
    {''.join(entries)}
    </body>
    </html>
    """
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[BLOGGER] Blog uložený do {OUTPUT_HTML}")

def run():
    print("[BLOGGER] Vyhľadávam trendy články...")
    articles = fetch_trending_articles()
    if not articles:
        print("[BLOGGER] Žiadne články nenájdené.")
        return

    html_blocks = []
    for url in articles:
        content = copy_article_text(url)
        if content:
            title = f"Trend z {datetime.utcnow().strftime('%d.%m.%Y')}"
            block = generate_html_entry(title, url, content)
            html_blocks.append(block)

    if not html_blocks:
        print("[BLOGGER] Nepodarilo sa získať obsah.")
        return

    save_html(html_blocks)