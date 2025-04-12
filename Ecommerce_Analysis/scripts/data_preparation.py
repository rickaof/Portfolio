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

# Orders Dataframe: treatment and Type Conversion
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

# Orders Items Dataframe: treatment and Type Conversion

order_items = dfs["order_items"]  # Extract the 'order_items' DataFrame

pd.set_option("display.max_columns", None)
print(order_items.head())

# Identifying null or missing values.
# Check data_preparation.ipynb notebook for treatment details.
print(order_items.isnull().sum())

# Checking column data types
print(order_items.dtypes)

# Columns type conversion
# Converting date columns from object to datetime
order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"], errors="coerce")

# Checking if the type conversion was succeessful
print(order_items.dtypes)

# Customers Dataframe: treatment and Type Conversion

customer = dfs["customer"]  # Extract the 'customers' DataFrame

pd.set_option("display.max_columns", None)
print(customer.head())

# Identifying null or missing values.
# Check data_preparation.ipynb notebook for treatment details.
print(customer.isnull().sum())

# Checking column data types
# Check data_preparation.ipynb notebook for treatment details.
print(customer.dtypes)

# Products Dataframe: treatment and Type Conversion

products = dfs["products"]  # Extract the 'products' DataFrame

pd.set_option("display.max_columns", None)
print(products.head())

# Identifying null or missing values.
# Check data_preparation.ipynb notebook for treatment details.
print(products.isnull().sum())

# Null and missing values treatment.
products["product_category_name"].fillna("Unknown", inplace=True)
num_cols = [
    "product_name_lenght", "product_description_lenght",
    "product_photos_qty", "product_weight_g", "product_length_cm",
    "product_height_cm", "product_width_cm"
]
for col in num_cols:
    products[col].fillna(products[col].median(), inplace=True)

# Checking if the null and missing values were treated.
print(products.isnull().sum())

# Checking column data types
# Check data_preparation.ipynb notebook for treatment details.
print(customer.dtypes)

# Sellers Dataframe: treatment and Type Conversion

sellers = dfs["sellers"]  # Extract the 'sellers' DataFrame

pd.set_option("display.max_columns", None)
print(sellers.head())

# Identifying null or missing values.
# Check data_preparation.ipynb notebook for treatment details.
print(sellers.isnull().sum())

# Checking column data types
# Check data_preparation.ipynb notebook for treatment details.
print(sellers.dtypes)

# Payments Dataframe: treatment and Type Conversion

payments = dfs["payments"]  # Extract the 'payments' DataFrame

pd.set_option("display.max_columns", None)
print(payments.head())

# Identifying null or missing values.
# Check data_preparation.ipynb notebook for treatment details.
print(payments.isnull().sum())

# Checking column data types
print(payments.dtypes)

# Converting 'payment_type' column from object to category.
print(payments["payment_type"].unique())
payments["payment_type"] = payments["payment_type"].astype("category")

# Checking if the type conversion was succeessful
print(payments["payment_type"].dtypes)

# Sellers Geolocation: treatment and Type Conversion

geolocation = dfs["geolocation"]  # Extract the 'geolocation' DataFrame

pd.set_option("display.max_columns", None)
print(geolocation.head())

# Identifying null or missing values.
# Check data_preparation.ipynb notebook for treatment details.
print(geolocation.isnull().sum())

# Checking column data types
# Check data_preparation.ipynb notebook for treatment details.
print(geolocation.dtypes)

# Saving the processed Dataframes in the "../data/processed".
processed_path = os.path.abspath(
    os.path.join(current_dir, "..", "data", "processed"))

for file, df in dfs.items():
    df.to_csv(os.path.join(processed_path, file), index=False)
    print(f"Processed dataset '{file}' saved to {processed_path}")
