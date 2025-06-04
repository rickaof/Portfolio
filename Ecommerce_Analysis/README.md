# 📦 Olist Delivery Delay Prediction

This project uses historical e-commerce data from Olist (Brazilian marketplace) to build a machine learning model that predicts whether a customer order will be delivered late. The main goal is to maximize recall for late orders, ensuring that as many delays as possible are identified early.

---

## 📌 Problem Statement

Delivery delays in e-commerce directly impact customer satisfaction and logistics efficiency. By predicting which orders are likely to be late before they are shipped, companies can:

* Take proactive actions (change carrier, contact customer)
* Optimize SLAs and delivery strategies

---

## 🔍 Dataset

The data comes from the public [Olist dataset on Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce). It includes:

* Orders, Items, Payments, Customers, Sellers, Products
* Delivery timestamps and geographic information

### Preprocessing Highlights

* Removed periods with low order volume (late 2018)
* Merged datasets by keys (order\_id, product\_id, etc.)
* Filtered orders with valid timestamps
* Created the target column: `is_late` (1 = late delivery, 0 = on time)

---

## 🛠️ Feature Engineering

Key features created:

* `product_volume` = product height × width × length
* `estimated_time` = estimated delivery duration in days
* `distance_seller_customer` = geo distance based on zip code prefixes
* One-hot encoding of state and month information

---

## 📊 Exploratory Data Analysis

* Visual analysis of delay rates by region, product category, and time
* Correlation analysis between delivery performance and key features
* Feature importance ranking (Random Forest)

---

## 🤖 Modeling & Evaluation

### Models tested:

* Logistic Regression
* Random Forest
* Gradient Boosting
* XGBoost
* SVM

### Metrics Used:

* **Primary metric**: Recall for delayed orders (class 1)
* Also tracked: Precision, F1-Score, Accuracy, CV Recall

### Model Selection:

* **SVM** achieved the highest recall (72%) but very low precision (17%)
* **Threshold-tuned Random Forest** reached 63% recall with better precision (20%) and higher F1-score (30%)

### Final Decision:

> In production, the adjusted Random Forest is recommended for a better balance of recall and precision, especially where false positives incur operational costs.

## 🚀 Tools & Technologies

* Python 3.11
* Pandas, NumPy, Seaborn, Matplotlib
* Scikit-learn
* XGBoost
* Jupyter Notebook

---

## 🧠 Author's Note

This project is part of my data science portfolio and simulates a real-world use case of predictive modeling in logistics. The emphasis on recall is aligned with the business goal of minimizing undetected delivery delays.

---

## 📬 Contact

**Author:** Henrique Ferreira

**LinkedIn:** [linkedin.com/in/henrique-ferreira-52506a261](https://www.linkedin.com/in/henrique-ferreira-52506a261/)

**Email:** [rick.a.o.f@gmail.com](mailto:rick.a.o.f@gmail.com)

