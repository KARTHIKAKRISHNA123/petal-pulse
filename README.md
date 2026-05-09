# <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=28&pause=1000&color=FF6B9D&center=false&width=600&lines=Iris-Intel+Iris+Flower+Predictor" alt="Iris Flower Species Predictor" />

<div align="center">

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Hugging_Face_Spaces-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/spaces/KarthikaKrishna123/Iris_Flower_Predictor)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KARTHIKAKRISHNA123/Iris-flower-predictor)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)

</div>

---

<div align="center">

*An interactive, end-to-end Machine Learning web application that classifies Iris flowers into three species —*
***Iris-setosa**, **Iris-versicolor**, and **Iris-virginica** — based on sepal and petal dimensions.*

*Built entirely from scratch as part of an advanced Supervised Machine Learning assignment, emphasizing*
*underlying logic, real-world constraints, and full-stack cloud deployment.*

</div>

---

## 📌 Table of Contents

- [Live Demo](#-live-demo)
- [Project Overview](#-project-overview)
- [The ML Challenge](#-the-machine-learning-challenge)
- [Models Implemented](#-models-implemented--compared)
- [Tech Stack](#️-tech-stack)
- [Project Highlights](#-project-highlights)
- [Repository Structure](#-repository-structure)
- [A-Z Project Journey](#-a-z-project-journey)
- [How to Run Locally](#-how-to-run-locally)
- [Results & Performance](#-results--performance)
- [Author](#-author)

---

## 🚀 Live Demo

<div align="center">

### 👉 [Try the App Live on Hugging Face Spaces](https://huggingface.co/spaces/KarthikaKrishna123/Iris_Flower_Predictor)

| Platform | Link | Status |
|----------|------|--------|
| 🤗 Hugging Face Spaces | [KarthikaKrishna123/Iris_Flower_Predictor](https://huggingface.co/spaces/KarthikaKrishna123/Iris_Flower_Predictor) | ![Active](https://img.shields.io/badge/status-active-brightgreen?style=flat-square) |
| 🐙 GitHub Repository | [KARTHIKAKRISHNA123/Iris-flower-predictor](https://github.com/KARTHIKAKRISHNA123/Iris-flower-predictor) | ![Active](https://img.shields.io/badge/status-active-brightgreen?style=flat-square) |

</div>

---

## 🌿 Project Overview

The **Iris Flower Species Predictor** is a fully deployed, production-grade machine learning web application built on the classic Iris dataset. The project goes beyond a typical classroom notebook — it simulates real-world ML engineering constraints, implements multiple classification algorithms from scratch, and delivers a polished interactive UI with a custom Dark Floral aesthetic.

> **Core Philosophy**: Every decision in this project — from train/test strategy to UI design — was made with a *from-scratch engineering mindset*, prioritizing deep understanding over high-level abstraction.

### What makes this different from a typical Iris project?

| Typical Iris Project | This Project |
|----------------------|-------------|
| Train 80%, test 20% | Train 50%, evaluate on 100% |
| Single model | 3 models with live switching |
| Plain Streamlit UI | Custom Dark Floral CSS theme |
| Local notebook | Deployed to Hugging Face Spaces |
| Single remote | Dual remote: GitHub + Hugging Face |

---

## 🧠 The Machine Learning Challenge

While the Iris dataset is classically clean, this project deliberately introduces real-world imperfections through a strict experimental constraint:

```
Training Data  →  50% of dataset  (train_test_split)
Evaluation     →  100% of dataset (full generalization test)
```

**Why evaluate on 100%?**
This simulates a production scenario where a model trained on historical data must perform on the entire known population — exposing overfitting risks that a standard 80/20 split might hide.

---

## 🤖 Models Implemented & Compared

### 1. K-Nearest Neighbours (KNN)

```python
KNeighborsClassifier(n_neighbors=3)
```

- Classification by majority vote from the 3 nearest data points in feature space.
- No explicit training phase — learns by memorizing the training set.
- Sensitive to feature scaling; highly interpretable decision boundaries.

### 2. Logistic Regression

```python
LogisticRegression(max_iter=200)
```

- Linear decision boundary learned via gradient descent.
- Default `max_iter=100` caused `ConvergenceWarning` — resolved by increasing to `200`.
- Outputs calibrated class probabilities via the softmax function.

### 3. Gaussian Naive Bayes

```python
GaussianNB()
```

- Probabilistic classifier assuming feature independence and Gaussian distributions.
- Extremely fast training; strong baseline for continuous feature classification.
- Applies Bayes' theorem: `P(class | features) ∝ P(features | class) × P(class)`

### Model Serialization

All trained models are serialized using **joblib** for zero-latency loading in production:

```python
import joblib
joblib.dump(model, 'knn_model.pkl')   # Save
model = joblib.load('knn_model.pkl')  # Load in app.py
```

---

## 🛠️ Tech Stack

<div align="center">

| Tool | Role |
|------|------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) **Python 3.x** | Core language |
| ![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white) **pandas** | Data loading & preprocessing |
| ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) **scikit-learn** | ML model training & evaluation |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) **Streamlit** | Web app framework |
| **joblib** | Model serialization (`.pkl`) |
| ![HuggingFace](https://img.shields.io/badge/🤗_Hugging_Face_Spaces-FFD21E?style=flat-square) **Hugging Face Spaces** | Cloud deployment |
| ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) **Git** | Version control + dual remote |

</div>

---

## ✨ Project Highlights

### 🎨 Dark Floral UI Theme
Custom CSS injected via `st.markdown()` featuring:
- Deep gradient background (`#0d0015` → `#1a0030`)
- Pulsing animated title with neon pink glow
- Neon hover effects on interactive elements
- High-contrast result cards with species-specific color coding

### ⚡ Performance Optimizations
- `@st.cache_resource` decorator ensures models load once and stay in memory across rerenders
- Lightweight `.pkl` files for near-instant prediction inference

### 🔄 Real-Time Model Switching
- Sidebar dropdown to swap between KNN, Logistic Regression, and Naive Bayes instantly
- All four feature sliders (sepal length/width, petal length/width) update predictions live

### ☁️ Dual Remote Deployment
```bash
git remote add origin https://github.com/KARTHIKAKRISHNA123/Iris-flower-predictor.git
git remote add hf https://huggingface.co/spaces/KarthikaKrishna123/Iris_Flower_Predictor
git push origin main   # → GitHub
git push hf main       # → Hugging Face Spaces (auto-deploys)
```

---

## 📁 Repository Structure

```
Iris-flower-predictor/
│
├── 📄 app.py                  # Main Streamlit application (UI + inference logic)
├── 🏋️ train_models.py         # Model training & joblib serialization script
│
├── 📊 iris.csv                # Raw dataset (150 samples × 5 columns)
│
├── 🤖 knn_model.pkl           # Serialized K-Nearest Neighbours model
├── 🤖 log_model.pkl           # Serialized Logistic Regression model
├── 🤖 nb_model.pkl            # Serialized Gaussian Naive Bayes model
│
├── 📦 requirements.txt        # Python dependencies for deployment
└── 📖 README.md               # This file
```

---

## 📜 A-Z Project Journey

### Phase 1 — Data Architecture & Strategy

- Loaded `iris.csv` using **pandas**, inspected shape `(150, 6)`, and dropped the redundant `Id` column.
- Separated features (`X`) from target (`y`) with `LabelEncoder` for species mapping.
- Designed the unconventional **50/100 split strategy**: train on half, evaluate on all.

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
# Evaluate on full X, y — not just X_test
```

### Phase 2 — Model Engineering

- Instantiated and trained all three classifiers on `X_train`, `y_train`.
- Resolved `ConvergenceWarning` in Logistic Regression by tuning `max_iter`.
- Ran `.predict()` and `.score()` against the full dataset to measure generalization.
- Serialized all three models with `joblib.dump()` into `.pkl` files.

### Phase 3 — Frontend Web App Development

- Scaffolded `app.py` with Streamlit sidebar for model selection and four feature sliders.
- Injected custom CSS via `st.markdown(unsafe_allow_html=True)` for the Dark Floral theme.
- Implemented result cards with conditional color coding per predicted species.
- Added `@st.cache_resource` for production-grade model loading performance.

### Phase 4 — Version Control & Cloud Deployment

- Initialized local Git repo, created `.gitignore`, and staged all project files.
- Set up **dual remote**: GitHub for version control, Hugging Face Spaces for live hosting.
- Verified live deployment on Spaces and tested all three models end-to-end.

---

## 💻 How to Run Locally

### Prerequisites
- Python 3.8 or higher
- pip

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/KARTHIKAKRISHNA123/Iris-flower-predictor.git
cd Iris-flower-predictor
```

**2. Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Train the models (if .pkl files are missing)**
```bash
python train_models.py
```

**5. Launch the app**
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 📊 Results & Performance

| Model | Training Accuracy | Full-Dataset Accuracy |
|-------|:-----------------:|:---------------------:|
| K-Nearest Neighbours | ~100% | ~97% |
| Logistic Regression | ~98% | ~96% |
| Gaussian Naive Bayes | ~96% | ~95% |

> Accuracy values are approximate and may vary by run due to `random_state` in the 50/50 split. All three models demonstrate strong generalization despite the aggressive training constraint.

### Iris Species Measurement Reference

| Species | Sepal Length | Sepal Width | Petal Length | Petal Width |
|---------|:------------:|:-----------:|:------------:|:-----------:|
| *Iris-setosa* | 4.3–5.8 cm | 2.3–4.4 cm | 1.0–1.9 cm | 0.1–0.6 cm |
| *Iris-versicolor* | 4.9–7.0 cm | 2.0–3.4 cm | 3.0–5.1 cm | 1.0–1.8 cm |
| *Iris-virginica* | 4.9–7.9 cm | 2.2–3.8 cm | 4.5–6.9 cm | 1.4–2.5 cm |

---

## 👩‍💻 Author

<div align="center">

**Karthika Krishna M**

*Computer Science & Engineering | Full-Stack MERN Developer & ML Enthusiast*

[![GitHub](https://img.shields.io/badge/GitHub-KARTHIKAKRISHNA123-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KARTHIKAKRISHNA123)

*"Always prioritizing a from-scratch engineering mindset."*

</div>

---

<div align="center">

*Built with 🌺 and Python — Karthika Krishna M*

</div>
