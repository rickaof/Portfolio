# 📦 Olist Delivery Delay Prediction

## Project Overview

This project uses historical e-commerce data from Olist (a Brazilian marketplace) to build a machine learning model that predicts whether a customer order will be delivered late. The main goal is to maximize recall for late orders, ensuring that as many delays as possible are identified early.

## Business Motivation

Delivery delays impact customer satisfaction, logistics efficiency, and operational cost. By identifying late deliveries in advance, companies can:

* Proactively notify customers
* Adjust carrier choices or shipment priorities
* Improve SLA (Service Level Agreement) performance

This project simulates a real-world predictive scenario.

## Project Structure

```
Ecommerce_Analysis/
├── data/
│   ├── raw/                # Raw Olist data (CSV files)
│   └── processed/          # Cleaned and filtered data
├── src/                    # Modular Python scripts
│   ├── __init__.py         # Declares src as a package
│   ├── data_loader.py      # Functions to load datasets
│   ├── data_cleaning.py    # Cleaning, filtering, saving
│   ├── exploratory_data_analysis.py  # EDA, outliers, VIF
│   ├── model.py            # Training, CV, metrics, plots
├── outputs/                # Visualizations, metrics, SHAP plots
├── main.py                 # Master pipeline to execute all steps
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```


## Workflow Overview

The pipeline is implemented in main.py, which orchestrates the following steps:

* Load raw datasets using src/data_loader.py

* Clean and filter the data with src/data_cleaning.py

* Merge tables and engineer the target (is_late)

* Perform EDA: outlier detection, boxplots, VIF (multicollinearity)

* Train multiple models: Random Forest, Logistic Regression, XGBoost

* Evaluate each model: Cross-validation + Test metrics

## How to Run the Pipeline

1. Ensure you have Python 3.11+ and clone the repo

2. Install the dependencies:

- pip install -r requirements.txt

3. Place the Olist CSV files in data/raw/

4. Run the full pipeline:

- python main.py

You can also run individual functions inside a Jupyter Notebook:

- from src.data_cleaning import order_type_conversion
- from src.model import train_evaluate_model

(Ensure src/__init__.py exists for package recognition.)

## Dataset

The project uses the [Olist e-commerce dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce), which includes:

* Orders, order items, customers, sellers, geolocation
* Products, payments, timestamps, delivery estimates

### Preprocessing Steps:

* Removal of periods with low order volume (to ensure time consistency)
* Merging multiple tables using unique keys
* Filtering only valid delivered or shipped orders
* Target creation: `is_late` (1 = late delivery, 0 = on time)

## Feature Engineering

Key features engineered include:

* `product_volume` = height × width × length
* `estimated_time` = delivery estimate in days
* `distance_seller_customer` = Euclidean distance based on geolocation means
* Region mapping from states (Norte, Nordeste, etc.)
* One-hot encoding for categorical features like purchase month and customer region

## Exploratory Data Analysis

* Visualized delay distribution and seasonality
* Analyzed correlation between numerical variables
* Identified feature importance using Random Forest
* Verified multicollinearity via VIF scores

## Modeling & Evaluation

### Models tested:

* Logistic Regression
* Random Forest
* XGBoost

### Metrics:

* Primary: **Recall** (for class 1 = late deliveries)
* Others: Precision, F1-Score, Accuracy, ROC AUC

### Results:

| Model               | F1-Score | Precision | Recall | ROC AUC |
| ------------------- | -------- | --------- | ------ | ------- |
| Random Forest       | 0.30     | 0.20      | 0.58   | 0.78    |
| XGBoost             | 0.40     | 0.35      | 0.46   | 0.82    |
| Logistic Regression | 0.22     | 0.13      | 0.64   | 0.73    |

> The XGBoost model achieved the best overall performance.&#x20;

## Tools & Technologies

* Python 3.11
* Pandas, NumPy, Matplotlib, Seaborn
* Scikit-learn
* XGBoost
* Jupyter Notebook

## Project Conclusion

This project showcases a complete end-to-end workflow: data ingestion, preprocessing, feature engineering, exploratory analysis, model training, evaluation, and interpretation. The XGBoost model provided the most balanced performance in terms of recall and precision for predicting late deliveries.

**## 📬 Contact**

\*\*Author:\*\* Henrique Ferreira

\*\*LinkedIn:\*\* \(https://www.linkedin.com/in/henrique-ferreira-52506a261/)

\*\*Email:\*\* \[rick.a.o.f@gmail.com]

This project is licensed under the MIT License.
