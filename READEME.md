📰 Multi-Label Topic Classification of News Articles
An end-to-end machine learning pipeline for multi-label topic classification of news articles, covering data collection, preprocessing, training, ONNX optimization, and deployment-ready inference.
This project is designed for research, production, and deployment scenarios, with large trained models stored externally for efficiency.
🚀 Project Highlights
🔖 Multi-label text classification (one article → multiple topics)
🧠 Transformer-based architecture
⚡ Optimized ONNX inference
🧩 Modular pipeline (scraping → training → inference)
🌐 Deployment-ready (Hugging Face / API friendly)
📦 Large models stored externally (GitHub-safe)

Multi-Label-Topic-Classification-of-News-Articles/
│
├── data/                     # Raw & processed datasets
├── dataloaders/              # Data loaders & preprocessing artifacts
├── labeling/                 # Label encoding & mappings
├── models/                   # (Ignored) trained models
├── notebooks/                # Experiments & analysis notebooks
├── pipeline/                 # Training & inference pipelines
├── scraper/                  # News scraping utilities
├── website_deployment/       # Web / API deployment code
├── huggingface_deployment/   # HF-compatible inference setup
│
├── config.py                 # Central configuration
├── requirements.txt          # Dependencies
├── test.py                   # Inference testing
├── README.md                 # Project documentation
└── .gitignore                # Git ignore rules

🧠 Model Architecture
Base Model: Transformer-based encoder
Task: Multi-label classification
Output: Binary relevance per topic
Inference format: ONNX (CPU-optimized)


📥 Download Trained Models (Required)
Due to GitHub file size limits, trained models are hosted externally.
🔗 Download links:
Final ONNX Model
https://drive.google.com/file/d/1fuhW4hpIsLmlKlwadirXNzquwU3F5Xxw/view
Final PyTorch / Pickle Model
https://drive.google.com/file/d/1rILhNxyiOb8LnWiJbsRVwyVpnokjIBIf/view
Stage / Backup Model
https://drive.google.com/file/d/1vwKPcRc28kgrJ_jS6MDkNyNx6eE6NEtd/view

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/mdfaisalahmed025/Multi-Label-Topic-Classification-of-News-Articles-.git
cd Multi-Label-Topic-Classification-of-News-Articles-
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows

