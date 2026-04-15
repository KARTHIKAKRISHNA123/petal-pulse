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

## 🚀 Live Demo
**[Try the app live on Hugging Face Spaces!](https://huggingface.co/spaces/KarthikaKrishna123/Iris_Flower_Predictor)**

## 🧠 The Machine Learning Challenge
While the Iris dataset is classically clean, this project simulates real-world imperfections with a strict constraint:
- **Training**: Models trained on only **50%** of the data (using `train_test_split`).
- **Evaluation**: Models evaluated against the **full 100%** dataset to test generalization and confidence.

### Models Implemented & Compared
1. **K-Nearest Neighbours (KNN)** — `n_neighbors=3` (majority vote from 3 closest points)
2. **Logistic Regression** — Overcame `ConvergenceWarning` by increasing `max_iter`
3. **Naive Bayes (GaussianNB)** — Probabilistic classification for continuous features

Models are serialized with **joblib** for instant loading in production.

## 🛠️ Tech Stack

Here’s the complete technology stack used to build this end-to-end pipeline:

<div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; margin: 20px 0;">

  <!-- Python -->
  <div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" width="80" height="80" style="filter: drop-shadow(0 0 8px #3776AB);">
    <p><strong>Python 3.x</strong></p>
  </div>

  <!-- pandas -->
  <div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" alt="pandas" width="120" height="50" style="filter: drop-shadow(0 0 8px #150458);">
    <p><strong>pandas</strong></p>
  </div>

  <!-- scikit-learn -->
  <div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit-learn" width="110" height="60" style="filter: drop-shadow(0 0 8px #F7931E);">
    <p><strong>scikit-learn</strong></p>
  </div>

  <!-- Streamlit -->
  <div style="text-align: center;">
    <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit" width="80" height="80" style="filter: drop-shadow(0 0 8px #FF4B4B);">
    <p><strong>Streamlit</strong></p>
  </div>

  <!-- joblib -->
  <div style="text-align: center;">
    <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #00C853, #64DD17); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto; box-shadow: 0 0 15px rgba(0, 200, 83, 0.6); color: white; font-weight: bold; font-size: 18px;">
      jb
    </div>
    <p><strong>joblib</strong></p>
  </div>

  <!-- Hugging Face -->
  <div style="text-align: center;">
    <img src="https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo-with-title.svg" alt="Hugging Face" width="140" height="50" style="filter: drop-shadow(0 0 8px #FFD21E);">
    <p><strong>Hugging Face Spaces</strong></p>
  </div>

</div>

**Additional tools**: Git, custom CSS for Dark Floral UI, GitHub + Hugging Face dual remote.

## ✨ Project Highlights – Dark Floral Aesthetic
- Custom **Streamlit** UI with deep gradient background, pulsing title animations, neon hover effects, and high-visibility result cards.
- Sidebar with real-time sliders for sepal/petal measurements and dropdown to switch models instantly.
- `@st.cache_resource` for efficient model loading.
- Professional `README.md` that works seamlessly on both GitHub and Hugging Face.

## 💻 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/KARTHIKAKRISHNA123/Iris-flower-predictor.git
   cd Iris-flower-predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

## 📜 A-Z Project Journey Summary

### Phase 1: Data Architecture & Strategy
- Loaded `iris.csv` with **pandas** and dropped the `Id` column.
- Applied strict 50/50 train-test split for training, but evaluated on 100% of data to mimic real-world challenges.

### Phase 2: Model Engineering
- Trained and compared **KNN**, **Logistic Regression**, and **Gaussian Naive Bayes** from scratch using **scikit-learn**.
- Handled convergence issues and serialized winning models with **joblib** for production use.

### Phase 3: Frontend Web App Development
- Built interactive UI in **Streamlit** with dynamic sliders and model switching.
- Completely customized the look with **CSS** for a stunning "Dark Floral" theme.

### Phase 4: Version Control & Cloud Deployment
- Authored professional `README.md` compatible with both platforms.
- Dual remote setup: **GitHub** for version control + **Hugging Face Spaces** for live deployment.

---



**Author**  
**Karthika Krishna M**  
Computer Science & Engineering | Full-Stack MERN Developer & ML Enthusiast  
*Always prioritizing a from-scratch engineering mindset.*

---

