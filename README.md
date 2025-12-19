# Medical Cost Predictor (India)

A Django web application that estimates medical insurance costs for the Indian market using a Linear Regression model.

## Features
- **AI-Powered Prediction**: Estimates costs based on Age, Sex, BMI, Children, Smoking Status, and Region.
- **Indian Market Localization**:
  - Currency converted to **INR (₹)**.
  - Indian regions (North, South, East, West).
- **Insurance Plans**: Recommends Silver, Gold, or Platinum plans based on the predicted cost.
- **Data Analysis**: Includes EDA scripts and visualizations.

## Project Structure
- `insurance_project/`: Django project settings.
- `predictor/`: Django app containing views, forms, and templates.
- `eda_analysis.py`: Script for Exploratory Data Analysis.
- `train_model.py`: Script to train and save the model (`model_linear_reg.pkl`).
- `insurance.csv`: Dataset used for training.

## Setup & Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Start Server**:
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/`.