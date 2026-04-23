# 💡 Healthcare Premium Prediction using Machine Learning

Healthcare Premium Prediction ML project that estimates annual insurance cost based on demographic, medical, and lifestyle factors. Built using Scikit-learn with dual age-based models and deployed as an interactive Streamlit web app with a professional UI and real-time prediction.

---

## 📌 Project Overview

Insurance premium pricing depends on multiple factors such as age, medical history, smoking habits, BMI category, employment type, income, and genetic risk.

This project builds a predictive model to estimate the annual insurance premium using supervised machine learning techniques.

---

## 🧠 Machine Learning Approach

### 🔹 Data Preprocessing
- Categorical feature encoding
- Feature scaling using StandardScaler
- Medical history risk transformation
- Separate preprocessing for different age groups

### 🔹 Model Strategy
Two separate models were trained:

- **Young Model** → Age < 25  
- **Rest Model** → Age ≥ 25  

This improves accuracy by handling age-specific risk patterns.

### 🔹 Saved Artifacts
- `model_young.joblib`
- `model_rest.joblib`
- `scaler_young.joblib`
- `scaler_rest.joblib`

Each scaler contains:
- Scaler object
- Feature columns used for training

---

## 🚀 Web Application (Streamlit)

The project includes a fully interactive web app where users can:

- Enter personal and medical details
- Select lifestyle and employment information
- Choose insurance plan
- Get real-time premium prediction

### 🎨 UI Features
- Modern gradient background
- Clean and responsive form layout
- Highlighted prediction output
- Fast inference using saved ML models

---

## 📊 Input Features

- Age  
- Gender  
- Marital Status  
- Region  
- Number of Dependents  
- BMI Category  
- Smoking Status  
- Employment Status  
- Income (Lakhs)  
- Medical History  
- Insurance Plan  
- Genetic Risk Score  

---
   

## 🏗️ Project Structure

```
Healthcare-Premium-Prediction-using-ML/
│
├── app/
│   ├── main.py
│   └── artifacts/
│       ├── model_young.joblib
│       ├── model_rest.joblib
│       ├── scaler_young.joblib
│       └── scaler_rest.joblib
│
├── requirements.txt
├── .gitignore
└── README.md
```


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/Healthcare-Premium-Prediction-using-ML.git
cd Healthcare-Premium-Prediction-using-ML/app
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run main.py
```

---

## 🚀 Future Improvements

- Add SHAP-based feature importance explanation
- Implement model performance comparison dashboard
- Add prediction confidence interval
- Integrate user authentication system
- Connect database for storing prediction history
- Add API version using FastAPI for production use
- Implement CI/CD pipeline for automated deployment
- Improve UI animations and user experience 

---

## 👨‍💻 Author

**khagesh**  
Data Enthusiast

