import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from config import SECTION_LABEL_MAP
from scraper.utils import clean_text

# -------------------------
# BBC CATEGORY URLS (12+)
# -------------------------
BBC_CATEGORY_URLS = {
    "politics": "https://www.bbc.com/news/politics",
    "world": "https://www.bbc.com/news/world",
    "business": "https://www.bbc.com/news/business",
    "technology": "https://www.bbc.com/news/technology",
    "health": "https://www.bbc.com/news/health",
    "science": "https://www.bbc.com/news/science_and_environment",
    "education": "https://www.bbc.com/news/education",
    "sport": "https://www.bbc.com/sport",
    "climate": "https://www.bbc.com/news/topics/cx1m7zg0gzdt",
    "crime": "https://www.bbc.com/news/topics/cdl8n2edk0jt",
    "international_affairs": "https://www.bbc.com/news/world",
    "economy": "https://www.bbc.com/news/business/economy",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; NewsDatasetBot/1.0)"
}

seen_hashes = set()
hash_lock = Lock()

# -------------------------
# URL FILTER (IMPORTANT)
# -------------------------
def extract_article_links(soup):
    links = set()
    for a in soup.select("a[href]"):
        href = a["href"]
        if (
            href.startswith("/news/")
            and href.count("/") >= 3
            and not any(x in href for x in ["/live/", "/topics/", "/av/"])
        ):
            links.add("https://www.bbc.com" + href.split("?")[0])
    return links

# -------------------------
# ARTICLE FETCHER
# -------------------------
def fetch_article(url, section):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return None

        soup = BeautifulSoup(r.text, "html.parser")
        paragraphs = soup.select("article p")

        if len(paragraphs) < 5:
            return None

        text = clean_text(" ".join(p.text for p in paragraphs))
        if len(text) < 500:
            return None

        text_hash = hash(text)
        with hash_lock:
            if text_hash in seen_hashes:
                return None
            seen_hashes.add(text_hash)

        return {
            "title": soup.title.text.strip() if soup.title else "",
            "text": text,
            "labels": SECTION_LABEL_MAP.get(section, []),
            "source": "BBC",
            "url": url,
        }

    except Exception:
        return None

# -------------------------
# MAIN SCRAPER
# -------------------------
def scrape_bbc(max_pages=50, max_threads=20):
    all_data = []

    for section, base_url in BBC_CATEGORY_URLS.items():
        print(f"\n🔹 Scraping BBC section: {section}")
        article_urls = set()

        # Step 1: Collect URLs
        for page in range(1, max_pages + 1):
            try:
                page_url = f"{base_url}?page={page}"
                r = requests.get(page_url, headers=HEADERS, timeout=10)
                if r.status_code != 200:
                    continue

                soup = BeautifulSoup(r.text, "html.parser")
                links = extract_article_links(soup)
                article_urls.update(links)

            except Exception:
                continue

        print(f"   → Found {len(article_urls)} URLs")

        # Step 2: Fetch articles (parallel)
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = [
                executor.submit(fetch_article, url, section)
                for url in article_urls
            ]

            for future in as_completed(futures):
                article = future.result()
                if article:
                    all_data.append(article)

        print(f"   ✓ Section done | Total articles: {len(all_data)}")

    return all_data
