# 🏏 IPL Match Win Probability Predictor

An end-to-end Machine Learning project that predicts the **winning probability of the chasing team** during an IPL match using historical ball-by-ball data.

🔗 **Live Demo:** https://ipl-win-probability-predictor-4wrrnpckoz5socfw3zdkgl.streamlit.app/

📂 **GitHub Repository:** https://github.com/Kush91-bit/IPL-Win-Probability-Predictor

---

## 📌 Project Overview

This project predicts the live winning probability of the chasing team based on the current match situation.

The application takes the following inputs:

- Batting Team
- Bowling Team
- Host City
- Target Score
- Current Score
- Overs Completed
- Wickets Fallen

Using these inputs, the application computes important match-state features such as:

- Runs Left
- Balls Left
- Wickets Remaining
- Current Run Rate (CRR)
- Required Run Rate (RRR)

These features are then passed to a trained Machine Learning model to estimate the winning probability of both teams.

---

## 🚀 Live Demo

The project is deployed on **Streamlit Community Cloud**.

👉 **Live Application:**  
https://LIVE_DEMO_LINK

---

## 📂 Dataset

The project uses historical IPL datasets.

### Files Used

- **matches.csv** – Match-level information
- **deliveries.csv** – Ball-by-ball information

### Data Preprocessing

The dataset was cleaned by:

- Removing Duckworth-Lewis (D/L) affected matches
- Standardizing old franchise names
- Filtering only second innings data
- Removing missing values
- Creating match-state features

---

## ⚙️ Feature Engineering

The following features were created:

| Feature | Description |
|----------|-------------|
| Runs Left | Runs required to win |
| Balls Left | Balls remaining |
| Wickets Remaining | Wickets left |
| Target Score | First innings score |
| Current Run Rate | Current scoring rate |
| Required Run Rate | Required scoring rate |
| Batting Team | Chasing team |
| Bowling Team | Defending team |
| City | Match venue |

These engineered features describe the current match situation and are used as inputs to the Machine Learning models.

---

## 🤖 Machine Learning Models

The following classification models were trained and compared:

- Logistic Regression
- Random Forest Classifier
- K-Nearest Neighbors (KNN)

To obtain realistic evaluation results, the dataset was split using **GroupShuffleSplit**, ensuring that deliveries from the same IPL match never appeared in both the training and testing sets.

This prevented **data leakage** and produced reliable performance estimates.

---

## 📊 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **76.13%** |
| Random Forest | 75.78% |
| K-Nearest Neighbors | 69.61% |

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC Curve
- Confusion Matrix

---

## 🎯 Final Model

Among all evaluated models, **Logistic Regression** was selected for deployment because it:

- Achieved the highest accuracy
- Produced stable probability estimates
- Was computationally efficient
- Was well-suited for live probability prediction

---

## 🌐 Streamlit Application

The web application allows users to:

- Select Batting Team
- Select Bowling Team
- Choose Host City
- Enter Target Score
- Enter Current Score
- Enter Overs Completed
- Enter Wickets Fallen
- Predict live winning probabilities instantly

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Jupyter Notebook

---

## 📁 Project Structure

```text
IPL-Win-Probability-Predictor
│
├── app.py
├── pipe.pkl
├── matches.csv
├── deliveries.csv
├── requirements.txt
├── README.md
└── ipl_win_probability.ipynb
```

---

## 🔄 Project Workflow

```text
Raw IPL Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
GroupShuffleSplit
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Selection
        │
        ▼
Streamlit Deployment
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Kush91-bit/IPL-Win-Probability-Predictor.git
```

Move into the project directory

```bash
cd IPL-Win-Probability-Predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💡 Future Improvements

- Train on the latest IPL seasons
- Add player-level statistics
- Include venue-specific performance
- Experiment with XGBoost and LightGBM
- Improve UI/UX with richer visualizations

---

## 👨‍💻 Author

**Kush Agarwal**

Computer Science Engineering Student

GitHub: https://github.com/Kush91-bit

Live Demo: https://ipl-win-probability-predictor-4wrrnpckoz5socfw3zdkgl.streamlit.app/
