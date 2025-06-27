# 🧠 Personality Type Predictor

A simple and interactive Streamlit web app that predicts whether a person is an **Introvert** or **Extrovert** based on their habits, social behavior, and online activity. The prediction is made using a trained machine learning model (`RandomForestClassifier`) with preprocessed features.

---

## 🚀 Features

- Takes 7 user inputs (e.g., time spent alone, social event attendance, etc.)
- Predicts personality type using a trained ML model
- Interactive UI built using Streamlit
- Handles categorical and numerical input via a pipeline
- Clean and responsive layout
- "Created by Aadi" footer credit

---

## 🧩 Technologies Used

- Python
- Streamlit
- Pandas, Scikit-learn
- Pickle (for saving/loading model)

---

## 📦 Files

- `personality_predictor_app.py` — Main Streamlit app
- `model.pkl` — Trained machine learning model pipeline
- `personality_dataset.csv` — (Optional) Original dataset used for training
- `README.md` — Project documentation

---

## 🛠️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/personality-predictor.git
cd personality-predictor
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Make sure model.pkl is in the same directory as the Streamlit app.

Run the Streamlit app:

bash
Copy
Edit
streamlit run personality_predictor_app.py
📈 Model Overview
The app uses a RandomForestClassifier trained on a dataset of behavioral inputs. Categorical features like stage fear and social exhaustion are encoded as binary, and numerical features are scaled using StandardScaler.
