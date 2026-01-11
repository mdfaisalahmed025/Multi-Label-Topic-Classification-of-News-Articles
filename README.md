# <span style="color:#1E90FF;">Multi-Label Topic Classification of News Articles using BBC News and Guardian Data.</span>

An end-to-end project to build a **multi-label news classification system**, enabling accurate categorization of articles across multiple topics such as politics, economy, technology, and climate.

---

## <span style="color:#FF4500;">Motivation</span>

Modern news articles often cover **multiple overlapping topics**, making it difficult for traditional single-label classifiers to capture the full context. Poor classification limits **content organization, analytics, and recommendation systems**.

This project aims to:

- Automatically assign **multiple relevant topics** to news articles.
- Enable **scalable and accurate news categorization**.
- Facilitate insights for journalists, analysts, and AI-driven news platforms.

Students, researchers, and news platforms can answer questions like:

- Which topics frequently overlap in news coverage?
- How to automatically tag news articles with multiple relevant categories?
- Which models provide the best performance for multi-label classification?

By leveraging **transformer-based models and large-scale datasets**, this project empowers **data-driven news analysis and organization**.

---

## <span style="color:#FF4500;">Project Background</span>

**MultiLabelNews** is built on **real-world news data** collected from reputable sources: BBC News and The Guardian. The pipeline includes:

- **Data collection:** Scraping ~97K articles from BBC and The Guardian and final cleaned data set is 92K
- **Preprocessing:** Cleaning text, encoding labels, handling multi-label annotations
- **Modeling:** Transformer-based models for multi-label classification
- **Evaluation:** Analysis of label distributions, overlaps, and classifier performance
- **Deployment:** ONNX optimization and inference-ready scripts

Key aspects:

- Multi-label classification for **10+ categories**
- Standardized datasets for reproducible research
- Modular pipeline for scraping → preprocessing → training → inference

---

## <span style="color:#FF4500;">Project Overview</span>

The system processes news articles and assigns **multiple topic labels** simultaneously.

### Target Categories (10+)

- Politics
- Economy
- Business
- Technology
- Health
- Climate & Environment
- Science
- Education
- Sports
- Crime & Law
- International Affairs
- Society

## <span style="color:#FF4500;">Dataset Validation & Processing</span>

This repository contains the cleaned and processed **multi-label news dataset**, along with the steps taken to ensure **data quality, consistency, and readiness for machine learning**.

### <span style="color:#32CD32;">Dataset Validation & Processing Results

- **Initial Dataset:** ~97,000 articles scraped from BBC News and The Guardian
- **Final Clean Dataset:** ~92,500 articles after preprocessing
- **Missing Values:** Rows with missing titles, content, or labels were removed
- **Duplicates:** Removed duplicate articles based on `title` and `description`
- **Text Cleaning:** Removed HTML tags, special characters, and normalized whitespace
- **Lowercasing & Tokenization:** Standardized text for NLP models
- **Weak Labeling / Encoding:** Multi-label target encoding using binary vectors
- **Train-Test Split:** Dataset split into training, validation, and test sets while maintaining label distributions

### <span style="color:#32CD32;">Data Quality Checks</span>

- **Completeness:** Ensured every article has text content and at least one label
- **Uniqueness:** Removed duplicates to avoid data leakage in training
- **Validity:** Checked labels to ensure they match the predefined category list
- **Consistency:** Standardized category names and multi-label encoding
- **Integrity:** Ensured no mismatch between article content and associated labels

### <span style="color:#32CD32;">Dataset Columns</span>

| Column Name    | Description                                         | Data Type     |
| -------------- | --------------------------------------------------- | ------------- |
| title          | Title of the news article                           | String        |
| text           | Full content of the article                         | String        |
| labels         | Original multi-label topics associated with article | List / String |
| source         | News source (e.g., BBC News, The Guardian)          | String        |
| url            | URL of the original article                         | String        |
| section        | Section of the news website (e.g., Politics, Tech)  | String        |
| revised_labels | Cleaned & standardized multi-label topics           | List / String |

---

This **cleaned and processed dataset** is ready for:

- **Transformer-based multi-label classification**
- **Exploratory Data Analysis (EDA) of topic distributions and overlaps**
- **Training, validation, and testing of machine learning models**

> The dataset ensures that all articles are fully labeled, duplicates are removed, and multi-label encoding is consistent for **high-quality model training and evaluation**.

## <span style="color:#FF4500;">Training & Model Evaluation</span>

### 🛠️ <span style="color:#32CD32;">Model Training</span>

- **Base Model:** `distilroberta-base` transformer encoder
- **Task:** Multi-label topic classification of news articles
- **Training Strategy:** Two-stage training with custom data loader
- **Epochs:** 5 cycles per stage
- **Accuracy:** Achieved **91% validation accuracy**, demonstrating strong generalization across multiple news topics
- **Frameworks & Libraries:** PyTorch, Hugging Face Transformers, BLURR

**Training Workflow:**

1. **Stage 1:** Initial training on full dataset to learn general topic distributions.
2. **Stage 2:** Fine-tuning on preprocessed and cleaned dataset for higher accuracy and label balance.
3. **BLURR Inference:** Used BLURR for accelerated inference pipelines, ensuring batch-efficient processing.
4. **ONNX Conversion:** Exported the trained model to **ONNX** for CPU-optimized inference and deployment.
5. **Quantization Attempt:** Model quantization failed due to shape inconsistencies; inference continues with full precision ONNX models.

---

### 📊 <span style="color:#32CD32;">Model Benchmarking</span>

## 📊 Model Benchmarking

| Base Architecture      | Validation Accuracy | Epochs | Remarks                                                             |
|------------------------|---------------------|--------|----------------------------------------------------------------------|
| distilroberta-base     | 91%                 | 10     | Lightweight model with strong performance and fast inference        |
| bert-base-uncased      | 91%                 | 10      | Stable baseline with consistent convergence                         |
| roberta-base           | **92%**             | 10     | Best-performing model with superior contextual representation       |

---

## ✅ Conclusion

- **RoBERTa-base** achieved the highest validation accuracy (**92%**), making it the most effective model for multi-label text classification in this setup.
- **DistilRoBERTa** delivered competitive accuracy with reduced computational overhead, making it ideal for resource-efficient deployment.
- **BERT-base-uncased** provided stable and reliable results, serving as a strong baseline architecture.
- BLURR-based inference enables efficient batch prediction while maintaining compatibility with the fastai ecosystem.
- ONNX export ensures deployment readiness; however, post-training quantization was not feasible due to dynamic shape inconsistencies in multi-label outputs.


---

### 🔍 <span style="color:#32CD32;">Evaluation & Metrics</span>

- **Metric:** Multi-label F1-score, Precision, and Recall were used to assess model performance across all topic labels
- **Confusion Analysis:** Observed model accurately predicts multiple overlapping topics such as _Politics + Economy_ or _Technology + Science_
- **Label-wise Performance:** Best performance on high-frequency labels (Politics, Economy), slightly lower recall on niche categories (Climate & Environment, Society)

<p align="center">
  <img src="/screenshots/learning rate.png" width="650" height="450" alt="Multi-Label Confusion Matrix"/>
</p>

✅ **Interpretation:**

- Diagonal blocks indicate correct multi-label predictions.
- Off-diagonal misclassifications show overlapping topic predictions where articles belong to multiple categories.
- Overall, the model demonstrates strong predictive power for multi-label classification tasks.

---

### ⚡ <span style="color:#32CD32;">Deployment & Inference</span>

- **BLURR Inference Pipelines:** Fast batch predictions with tokenized inputs
- **ONNX Models:** Optimized for CPU inference; ready for API integration
- **Quantization Limitation:** Unable to quantize due to shape mismatch; models still perform efficiently in full precision

## <span style="color:#FF4500;">Model Deployment</span>

The model has been deployed to **Hugging Face Spaces** using **Gradio**:

- Interactive UI allows users to input article text and receive **multi-label predictions with confidence scores**
- BLURR inference ensures fast batch predictions
- ONNX model used for CPU-optimized inference

🔗 [HuggingFace Space Demo](https://huggingface.co/spaces/mdfaisalahmed025/Multilabel-News-Article-Classifier)

---

### Interactive Gradio Interface

<p align="center">
  <img src="/screenshots/gradio_interface.png" width="750" height="400" alt="Gradio App Screenshot"/>
</p>

---

### Web Integration

- Deployed website integrates Hugging Face API via **Render / GitHub Pages**
- Users can input news articles directly from browser
- API returns predictions displayed in the web interface

<p align="center">
  <img src="/screenshots/render_webpage.png" width="750" height="400" alt="Gradio App Screenshot"/>
</p>

🔗 [Live NewsLens Website](https://multi-label-topic-classification-of-news.onrender.com)

---

## <span style="color:#FF4500;">Future Work</span>

- Expand dataset with more sources for richer topic coverage
- Experiment with larger transformer models for improved accuracy
- Quantize ONNX model to optimize deployment performance
- Add real-time article streaming and multi-label batch inference

---

### 📌 <span style="color:#FF4500;">Directory & File Overview</span>

- **data/** – Contains all raw and processed datasets used for model training and evaluation.
- **dataloaders/** – Includes custom data loaders, tokenizers, and preprocessing artifacts for model input.
- **labeling/** – Manages multi-label category encoding and mappings to maintain consistency.
- **models/** – Trained model artifacts (ignored in Git; download externally due to large size).
- **notebooks/** – Jupyter notebooks for experimentation, model evaluation, and analysis.
- **pipeline/** – Scripts for training, validation, and inference pipelines.
- **scraper/** – Utilities for scraping news articles from sources like BBC and The Guardian.
- **website_deployment/** – Frontend and backend code for deploying the model as an interactive web application.
- **huggingface_deployment/** – Hugging Face-compatible deployment setup, including BLURR and ONNX inference.

**Key Files:**

- **config.py** – Central configuration for paths, hyperparameters, and model settings.
- **requirements.txt** – Python dependencies required to run the project.
- **test.py** – Quick inference scripts for testing model predictions.
- **README.md** – Project documentation.
- **.gitignore** – Specifies files and directories ignored by Git (e.g., large model files).

## <span style="color:#FF4500;">Installation & Setup</span>

1️⃣ **Clone Repository**

```bash
git clone https://github.com/mdfaisalahmed025/Multi-Label-Topic-Classification-of-News-Articles-.git
cd Multi-Label-Topic-Classification-of-News-Articles-


# 📞 Contact / Author

**Project Maintainer:** Md Faisal Ahmed
**Portfolio:** [mdfaisalahmed.online](https://mdfaisalahmed.online/)
**GitHub:** [@mdfaisalahmed025](https://github.com/mdfaisalahmed025)


```
