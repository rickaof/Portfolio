# scripts/leitura_dados.py
import pandas as pd
import os

# Define path to raw data files
current_dir = os.path.dirname(__file__)
data_path = os.path.abspath(os.path.join(current_dir, "..", "data", "raw"))

# List files in the data directory
files = os.listdir(data_path)

# Create a dictionary where each is a file name and the value is a DataFrame with the data.
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
# Display information about each loaded dataset.
for file, df in dfs.items():
    print(f"\nDataset: {file}")
    print(df.shape)
    print(df.head())

