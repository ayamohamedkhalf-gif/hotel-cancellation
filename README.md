# 🏨 Hotel Booking Cancellation Predictor

A complete Machine Learning web application built to predict hotel booking cancellations and recommend optimal deposit policies.

## 🚀 Project Overview
This project leverages historical hotel booking data to train a Random Forest Classifier model that predicts whether a customer is likely to cancel their reservation. Based on the prediction probability, the app suggests tailored deposit policies (No Deposit, Partial Deposit, or Full Deposit).

## 🛠️ Tech Stack
* **Python** (Pandas, Scikit-learn, Joblib)
* **Streamlit** (for the interactive web interface)
* **Machine Learning:** Random Forest Classifier (ROC-AUC score > 0.98)

## 💻 How to Run Locally
1. Clone or download the repository.
2. Install dependencies:
   ```bash
   pip install pandas scikit-learn streamlit joblib