# Customer Churn Prediction

Welcome to the **Customer Churn Prediction** project! This repository contains the code and analysis used to predict customer churn for a bank, leveraging a real-world business case study. The project includes detailed exploratory data analysis (EDA), data preprocessing, and the application of machine learning techniques to predict which customers are likely to leave the bank.

## Project Overview
Customer churn, or customer attrition, refers to the phenomenon where customers stop using a company's product or service. This project focuses on predicting customer churn for a bank by analyzing various customer features such as credit score, account balance, and tenure with the bank. The goal is to identify customers with a high probability of leaving, enabling the bank to take proactive measures to retain them.

## Key Features of the Project
- **Exploratory Data Analysis (EDA):** In-depth analysis of customer data to understand key trends and patterns.
- **Feature Engineering:** Creation and selection of relevant features to improve model performance.
- **Modeling and Evaluation:** Application of various machine learning models to predict customer churn, with a focus on model accuracy and interpretability.
- **Imbalanced Data Handling:** Techniques such as resampling and the use of appropriate evaluation metrics to address data imbalance.

## Data Overview
The dataset used in this project contains information about 10,000 customers of a bank. The features include:
- **Credit Score:** The customer's credit score.
- **Geography:** The customer's location (France, Spain, Germany).
- **Gender:** The customer's gender.
- **Age:** The customer's age.
- **Tenure:** The number of years the customer has been with the bank.
- **Balance:** The customer's account balance.
- **Number of Products:** The number of bank products the customer uses.
- **Has Credit Card:** Indicates whether the customer has a credit card.
- **Is Active Member:** Indicates whether the customer is an active bank member.
- **Estimated Salary:** The customer's estimated salary.
- **Exited:** The target variable, indicating whether the customer left the bank.

## Project Structure
- **Data Exploration:** Initial exploration of the dataset to gain insights into the distribution of features and the relationship between different variables.
- **Data Cleaning:** Handling missing values, outliers, and irrelevant features to prepare the dataset for modeling.
- **Feature Engineering:** Transforming categorical variables, scaling numerical features, and creating new features to enhance model performance.
- **Modeling:** Implementation of various machine learning algorithms including Logistic Regression, Random Forest, and Gradient Boosting to predict customer churn.
- **Model Evaluation:** Evaluation of model performance using metrics like accuracy, precision, recall, F1-score, and ROC-AUC curve.
- **Interpretation:** Analysis of feature importance and model interpretability using techniques such as SHAP values.

## Technologies Used
- **Python:** Primary programming language used.
- **Pandas & NumPy:** For data manipulation and analysis.
- **Matplotlib & Seaborn:** For data visualization and exploratory analysis.
- **Scikit-learn:** For machine learning model building and evaluation.
- **PyCaret:** For automated machine learning and model selection.
- **Google Colab:** For running the notebooks and performing the analysis.

## How to Use the Code
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/customer-churn-prediction.git
