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

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Hugging_Face_Spaces-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/spaces/KarthikaKrishna123/Iris_Flower_Predictor)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)

---

An interactive, end-to-end **Machine Learning web application** that classifies Iris flowers into three species (*Iris-setosa*, *Iris-versicolor*, *Iris-virginica*) based on their sepal and petal dimensions.

Built entirely from scratch as part of an advanced Supervised Machine Learning assignment, emphasizing underlying logic, real-world constraints, and full-stack cloud deployment.

---

## 🧠 The Machine Learning Challenge

Training constraint: models trained on **50%** of data, evaluated against **100%** to test real-world generalization.

### Models Implemented

| Model | Key Detail |
|-------|------------|
| **K-Nearest Neighbours** | `n_neighbors=3` — majority vote |
| **Logistic Regression** | `max_iter=200` — resolved ConvergenceWarning |
| **Gaussian Naive Bayes** | Probabilistic, Bayes' theorem |

Models serialized with **joblib** for instant production loading.

---

## 🛠️ Tech Stack

| Tool | Role |
|------|------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) **Python 3.x** | Core language |
| ![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white) **pandas** | Data preprocessing |
| ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) **scikit-learn** | ML training & evaluation |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) **Streamlit** | Web app framework |
| **joblib** | Model serialization |
| ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) **Git** | Dual remote version control |

---

## 💻 How to Run Locally

```bash
git clone https://github.com/KARTHIKAKRISHNA123/Iris-flower-predictor.git
cd Iris-flower-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 👩‍💻 Author

**Karthika Krishna M** — Computer Science & Engineering | Full-Stack MERN Developer & ML Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-KARTHIKAKRISHNA123-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/KARTHIKAKRISHNA123)