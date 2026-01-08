import requests
import hashlib
from datetime import datetime
from config import SECTION_LABEL_MAP
from scraper.utils import clean_text

API_KEY = "e8121d9f-4561-4061-85e4-6d81bf3f9444"
BASE_URL = "https://content.guardianapis.com/search"

SECTIONS = [
    "politics",
    "world",
    "business",
    "technology",
    "science",
    "education",
    "sport",
    "environment",
    "society",
    "media",
    "law",
    "health",
    "culture",
    "economics"
]

def scrape_guardian(
    pages_per_section=50,
    from_date="2019-01-01",
    to_date=None
):
    data = []
    seen = set()

    to_date = to_date or datetime.today().strftime("%Y-%m-%d")

    for section in SECTIONS:
        print(f"\n🟩 Guardian section: {section}")

        for page in range(1, pages_per_section + 1):
            params = {
                "api-key": API_KEY,
                "section": section,
                "show-fields": "bodyText",
                "page": page,
                "page-size": 200,
                "from-date": from_date,
                "to-date": to_date
            }

            try:
                res = requests.get(BASE_URL, params=params, timeout=20).json()
                results = res["response"]["results"]

                if not results:
                    break

                for item in results:
                    text = clean_text(item["fields"].get("bodyText", ""))

                    if len(text) < 500:
                        continue

                    uid = hashlib.md5(text.encode()).hexdigest()
                    if uid in seen:
                        continue
                    seen.add(uid)

                    data.append({
                        "title": item["webTitle"],
                        "text": text,
                        "labels": SECTION_LABEL_MAP.get(section, []),
                        "source": "Guardian",
                        "url": item["webUrl"],
                        "section": section
                    })

                print(f"Page {page} ✔ | Total: {len(data)}")

            except Exception as e:
                print(f"⚠️ Error on {section} page {page}: {e}")
                continue

    return data
