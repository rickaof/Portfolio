# 📦 Olist Delivery Delay Prediction

## Project Overview

This project uses historical e-commerce data from Olist (a Brazilian marketplace) to build a machine learning model that predicts whether a customer order will be delivered late. The main goal is to maximize recall for late orders, ensuring that as many delays as possible are identified early.

## Business Motivation

Delivery delays impact customer satisfaction, logistics efficiency, and operational cost. By identifying late deliveries in advance, companies can:

* Proactively notify customers
* Adjust carrier choices or shipment priorities
* Improve SLA (Service Level Agreement) performance

This project simulates a real-world predictive scenario applicable to marketplaces and fintechs like C6 Bank.

## Project Files

```
├── data_preparation.ipynb   # Data cleaning, feature engineering, and EDA
├── model.ipynb              # Model training, evaluation, and selection
├── requirements.txt         # Python package dependencies
├── README.md                # Project documentation
```

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

\*\*LinkedIn:\*\* \[linkedin.com/in/henrique-ferreira-52506a261]\([https://www.linkedin.com/in/henrique-ferreira-52506a261/](https://www.linkedin.com/in/henrique-ferreira-52506a261/))

\*\*Email:\*\* \[[rick.a.o.f@gmail.com](mailto:rick.a.o.f@gmail.com)]\(mailto:[rick.a.o.f@gmail.com](mailto:rick.a.o.f@gmail.com))License

This project is licensed under the MIT License.
