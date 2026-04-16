---
title: Iris Flower Predictor
emoji: 🌺
colorFrom: pink
colorTo: purple
sdk: streamlit
app_file: app.py
pinned: false
---

# 🌺 Iris Flower Species Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://huggingface.co/spaces/KarthikaKrishna123/Iris_Flower_Predictor)

An interactive, end-to-end **Machine Learning web application** that classifies Iris flowers into three species (*Iris-setosa*, *Iris-versicolor*, *Iris-virginica*) based on their sepal and petal dimensions.

This project was built entirely from scratch as part of an advanced Supervised Machine Learning assignment. It emphasizes underlying logic, real-world constraints, and full-stack deployment rather than high-level abstractions.

---

## 🚀 Live Demo

**[Try the app live on Hugging Face Spaces!](https://huggingface.co/spaces/KarthikaKrishna123/Iris_Flower_Predictor)**

---

## 🧠 The Machine Learning Challenge

While the Iris dataset is classically clean, this project simulates real-world imperfections with a strict constraint:

- **Training**: Models trained on only **50%** of the data (using `train_test_split`).
- **Evaluation**: Models evaluated against the **full 100%** dataset to test generalization and confidence.

### Models Implemented & Compared

| # | Model | Key Detail |
|---|-------|------------|
| 1 | **K-Nearest Neighbours (KNN)** | `n_neighbors=3` — majority vote from 3 closest points |
| 2 | **Logistic Regression** | Overcame `ConvergenceWarning` by increasing `max_iter` |
| 3 | **Naive Bayes (GaussianNB)** | Probabilistic classification for continuous features |

Models are serialized with **joblib** for instant loading in production.

---

## 🛠️ Tech Stack

| Python | pandas | scikit-learn | Streamlit | joblib | Hugging Face |
|:------:|:------:|:------------:|:---------:|:------:|:------------:|
| <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="60" alt="Python"> | <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width="90" alt="pandas"> | <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="90" alt="scikit-learn"> | <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="60" alt="Streamlit"> | **jb** | <img src="https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo-with-title.svg" width="100" alt="Hugging Face"> |
| **Python 3.x** | **pandas** | **scikit-learn** | **Streamlit** | **joblib** | **HF Spaces** |

**Additional tools**: Git, custom CSS for Dark Floral UI, GitHub + Hugging Face dual remote.

---

## ✨ Project Highlights

- **Dark Floral Aesthetic** — Custom Streamlit UI with deep gradient background, pulsing title animations, neon hover effects, and high-visibility result cards.
- **Real-time model switching** — Sidebar sliders for sepal/petal measurements with instant dropdown to swap between all three models.
- **Performance-optimized** — `@st.cache_resource` for efficient model loading.
- **Dual-platform README** — Professional documentation that renders cleanly on both GitHub and Hugging Face.

---

## 💻 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/KARTHIKAKRISHNA123/Iris-flower-predictor.git
cd Iris-flower-predictor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Streamlit app**
```bash
streamlit run app.py
```

---

## 📜 A-Z Project Journey

### Phase 1 — Data Architecture & Strategy
- Loaded `iris.csv` with **pandas** and dropped the `Id` column.
- Applied a strict 50/50 train-test split for training, but evaluated against 100% of the data to mimic real-world generalization challenges.

### Phase 2 — Model Engineering
- Trained and compared **KNN**, **Logistic Regression**, and **Gaussian Naive Bayes** from scratch using **scikit-learn**.
- Resolved convergence issues in Logistic Regression and serialized all winning models with **joblib** for production use.

### Phase 3 — Frontend Web App Development
- Built an interactive UI in **Streamlit** with dynamic sliders and instant model switching.
- Completely customized the look with **CSS** for a stunning "Dark Floral" theme.

### Phase 4 — Version Control & Cloud Deployment
- Authored a professional `README.md` compatible with both GitHub and Hugging Face.
- Dual remote setup: **GitHub** for version control + **Hugging Face Spaces** for live deployment.

---

## 📁 Repository Structure

```
Iris-flower-predictor/
│
├── app.py                  # Main Streamlit application
├── train_models.py         # Model training & serialization script
├── iris.csv                # Dataset
├── knn_model.pkl           # Serialized KNN model
├── logreg_model.pkl        # Serialized Logistic Regression model
├── nb_model.pkl            # Serialized Naive Bayes model
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 👩‍💻 Author

**Karthika Krishna M**  
Computer Science & Engineering | Full-Stack MERN Developer & ML Enthusiast  
[![GitHub](https://img.shields.io/badge/GitHub-KARTHIKAKRISHNA123-181717?style=flat&logo=github)](https://github.com/KARTHIKAKRISHNA123)

*Always prioritizing a from-scratch engineering mindset.*