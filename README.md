# 🏏 IPL Win Probability Predictor

An end-to-end Machine Learning project that predicts the winning probability of the chasing team during an IPL match using ball-by-ball match data.

---
## 📌 Project Overview

This project predicts the winning probability of the chasing team during an Indian Premier League (IPL) match using Machine Learning.

The model takes the current match situation as input, including:

- Batting Team
- Bowling Team
- Host City
- Target Score
- Current Score
- Balls Remaining
- Wickets Remaining
- Current Run Rate (CRR)
- Required Run Rate (RRR)

Based on these features, the model predicts the probability of both teams winning the match.

The project also includes a Streamlit web application where users can interactively enter match details and get live win probability predictions.
## 📂 Dataset

The project uses historical IPL ball-by-ball data.

### Files Used

- **matches.csv** – Contains match-level information such as teams, venue, winner, city, and target score.
- **deliveries.csv** – Contains ball-by-ball data including runs scored, wickets, over number, and batting/bowling teams.

### Data Preprocessing

The dataset was cleaned before training the models by:

- Removing Duckworth-Lewis (D/L) affected matches.
- Standardizing old team names.
- Selecting only the teams available in the dataset.
- Filtering only second innings data for win probability prediction.
- Creating new match-state features using ball-by-ball information.
## ⚙️ Feature Engineering

The following features were engineered from the raw match data:

| Feature | Description |
|---------|-------------|
| Runs Left | Runs required to win |
| Balls Left | Balls remaining in the innings |
| Wickets | Wickets remaining |
| Target Score | First innings total |
| Current Run Rate (CRR) | Current scoring rate |
| Required Run Rate (RRR) | Required scoring rate |
| Batting Team | Team chasing the target |
| Bowling Team | Team defending the target |
| Host City | Match venue city |

These engineered features represent the current state of the match and are used as inputs to the machine learning models.
# 🏏 IPL Win Probability Predictor

An end-to-end Machine Learning project that predicts the winning probability of the chasing team during an IPL match using ball-by-ball match data.

---

## 📌 Project Overview

This project predicts the winning probability of the chasing team during an Indian Premier League (IPL) match using Machine Learning.

The model takes the current match situation as input, including:

- Batting Team
- Bowling Team
- Host City
- Target Score
- Current Score
- Balls Remaining
- Wickets Remaining
- Current Run Rate (CRR)
- Required Run Rate (RRR)

Based on these features, the model predicts the probability of both teams winning the match.

The project also includes a Streamlit web application where users can interactively enter match details and get live win probability predictions.

---

## 📂 Dataset

The project uses historical IPL ball-by-ball data.

### Files Used

- **matches.csv** – Match-level information
- **deliveries.csv** – Ball-by-ball information

### Data Preprocessing

The dataset was cleaned by:

- Removing Duckworth-Lewis (D/L) affected matches
- Standardizing old team names
- Filtering only second innings matches
- Engineering match-state features
- Removing missing values

---

## ⚙️ Feature Engineering

The following features were created from the raw dataset:

| Feature | Description |
|----------|-------------|
| Runs Left | Runs required to win |
| Balls Left | Balls remaining |
| Wickets | Wickets remaining |
| Target Score | First innings total |
| Current Run Rate | Current scoring rate |
| Required Run Rate | Required scoring rate |
| Batting Team | Chasing team |
| Bowling Team | Defending team |
| City | Match venue |

---

## 🤖 Machine Learning Models

Three machine learning algorithms were trained and evaluated.

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Random Forest Classifier

To obtain realistic evaluation results, the dataset was split using **GroupShuffleSplit**, ensuring that deliveries from the same match were never present in both the training and testing sets. This prevents data leakage and provides a more reliable estimate of model performance.

---

## 📊 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **76.13%** |
| Random Forest | 75.78% |
| K-Nearest Neighbors | 69.61% |

Additional evaluation metrics used:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve
- Feature Importance (Random Forest)

---

## 🎯 Final Model Selection

Although multiple machine learning models were evaluated, **Logistic Regression** was selected as the final deployment model because it achieved the best overall accuracy on the match-wise split dataset while also providing well-calibrated probability estimates suitable for win probability prediction.

---

## 🌐 Streamlit Web Application

The project includes a Streamlit application where users can:

- Select batting and bowling teams
- Choose the host city
- Enter the current match situation
- Predict win probabilities instantly

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Jupyter Notebook

---

## 📁 Project Structure

```
IPL_WIN_PREDICTOR
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

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Kush91-bit/IPL_WIN_PREDICTOR.git
```

Go to project directory

```bash
cd IPL_WIN_PREDICTOR
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

- Train using the latest IPL dataset
- Include player-level statistics
- Incorporate venue-specific performance metrics
- Explore advanced models such as XGBoost and LightGBM
- Deploy the application on Streamlit Community Cloud

---

## 👨‍💻 Author

**Kush Agarwal**

Computer Science Engineering Student

GitHub: https://github.com/Kush91-bit