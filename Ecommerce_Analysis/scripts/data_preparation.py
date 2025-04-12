# script/data_preparation.py
import pandas as pd
import os

# Define path to raw data files
current_dir = os.path.dirname(__file__)
data_path = os.path.abspath(os.path.join(current_dir, "..", "data", "raw"))

# List files in the data directory
files = os.listdir(data_path)

# Create a dictionary where each key is a file name and the value is a DataFrame with the data.
custom_names = {
    "olist_customers_dataset.csv": "customer",
    "olist_geolocation_dataset.csv": "geolocation",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "payments",
    "olist_orders_dataset.csv": "orders",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers"
}

dfs = {
    custom_names[file]: pd.read_csv(os.path.join(data_path, file))
    for file in files if file in custom_names
}

# Orders Dataset: treatment and Type Conversion
orders = dfs["orders"]  # Extract the 'orders' DataFrame

pd.set_option("display.max_columns", None)
print(orders.head())

# Identifying null or missing values.
# Check data_preparation.ipynb notebook for treatment details.
print(orders.isnull().sum())

# Checking column data types
print(orders.dtypes)

# Columns type conversion
# Converting date columns from object to datetime
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

# Converting "order status" column from object to category
orders["order_status"] = orders["order_status"].astype("category")

# Checking if the type conversion was succeessful
print(orders.dtypes)

