# FUTURE_ML_01 - Sales & Demand Forecasting

## Project Overview

This project was developed as part of the Future Interns Machine Learning Internship Program.

The objective was to build a sales forecasting system using historical business sales data and generate future sales predictions to support business decision-making.

---

## Dataset

* Superstore Sales Dataset
* Historical retail sales transactions
* Time-based sales forecasting problem

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Jupyter Notebook

---

## Project Workflow

### 1. Data Cleaning

* Loaded and explored the dataset
* Converted date columns to datetime format
* Checked missing values and data types

### 2. Exploratory Data Analysis

* Daily sales aggregation
* Monthly sales trend visualization
* Trend and seasonality analysis

### 3. Feature Engineering

Created time-based features:

* Year
* Month
* Day
* Day of Week
* Quarter

Created forecasting features:

* lag_1
* lag_7
* rolling_mean_7

### 4. Model Building

Model Used:

* Random Forest Regressor

### 5. Model Evaluation

Baseline Model:

* MAE: 1799.84
* RMSE: 2531.34

Improved Model:

* MAE: 1748.98
* RMSE: 2337.73

### 6. Future Forecasting

Generated a 30-day sales forecast using recursive forecasting and lag features.

---

## Business Impact

The forecasting system can help businesses:

* Plan inventory levels
* Improve demand forecasting
* Optimize staffing decisions
* Support budgeting and planning
* Reduce stock shortages and overstocking

---

## Results

The improved model achieved lower forecasting errors and produced more reliable future sales predictions by incorporating lag-based historical sales features.

---

## Author

Future Interns ML Track - Task 01
