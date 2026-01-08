import os
import pandas as pd
from scraper import  bbc_scraper, guardian_scraper
from labeling.weak_labeler import apply_weak_labels

# -----------------------
# Create directories
# -----------------------
os.makedirs("data/raw/bbc", exist_ok=True)
os.makedirs("data/raw/guardian", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# -----------------------
# Helper: label & filter
# -----------------------
def apply_labels(data):
    cleaned = []
    for item in data:
        labels = apply_weak_labels(item["text"], item.get("labels"))
        if labels:
            item["labels"] = labels
            cleaned.append(item)
    return cleaned

# -----------------------
# BBC
# -----------------------
print("\n🟦 Scraping BBC...")
bbc_raw = bbc_scraper.scrape_bbc(max_pages=70)
pd.DataFrame(bbc_raw).to_csv("data/raw/bbc/bbc_raw.csv", index=False)

bbc = apply_labels(bbc_raw)
pd.DataFrame(bbc).to_csv("data/processed/bbc_labeled.csv", index=False)
print(f"✓ BBC saved: {len(bbc)} articles")

# -----------------------
# Guardian
# -----------------------
print("\n🟩 Scraping Guardian...")
guardian_raw = guardian_scraper.scrape_guardian()
pd.DataFrame(guardian_raw).to_csv("data/raw/guardian/guardian_raw.csv", index=False)

guardian = apply_labels(guardian_raw)
pd.DataFrame(guardian).to_csv("data/processed/guardian_labeled.csv", index=False)
print(f"✓ Guardian saved: {len(guardian)} articles")

# -----------------------
# Reuters
# -----------------------


# -----------------------
# MERGE ALL
# -----------------------
all_data = bbc + guardian
df = pd.DataFrame(all_data)
df.to_csv("data/processed/news_multilabel_merged.csv", index=False)

print("\n🔥 FINAL DATASET")
print("Total articles:", len(df))

