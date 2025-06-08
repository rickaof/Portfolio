import pandas as pd
import os


def check_missing_and_duplicates(dfs):
    for name, df in dfs.items():
        print(f"--- {name} ---")
        print(f"Shape: {df.shape}")
        print(f"Duplicated rows: {df.duplicated().sum()}")
        print(f"Missing values:\n{df.isnull().sum()}")
        print()


def order_type_conversion(orders):
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
    for col in date_cols:
        orders[col] = pd.to_datetime(orders[col], errors="coerce")

    orders["order_status"] = orders["order_status"].astype("category")
    return orders


def products_treatment(products):
    products['product_category_name'].fillna('unknown', inplace=True)
    num_cols = [
        "product_weight_g", "product_length_cm",
        "product_height_cm", "product_width_cm"
    ]
    for col in num_cols:
        products[col].fillna(products[col].median(), inplace=True)
    return products


def olist_filter_and_save(
        orders, order_items, payments, customer, products, sellers):

    # Orders purchase count by month
    order_counts = orders['order_purchase_month'].value_counts()
    valid_months = order_counts[order_counts >= 500].index

    # Filtering the orders by valid months.
    orders_filtered = orders[orders['order_purchase_month'].isin(valid_months)]

    # Valid IDs
    valid_order_ids = orders_filtered['order_id']
    valid_customer_ids = orders_filtered['customer_id']

    # Filtering other dataframes based on valid data
    order_items_filtered = order_items[order_items['order_id'].isin(
        valid_order_ids)]
    payments_filtered = payments[payments['order_id'].isin(valid_order_ids)]
    customer_filtered = customer[customer['customer_id'].isin(
        valid_customer_ids)]
    products_filtered = products[products['product_id'].isin(
        order_items_filtered['product_id'])]
    sellers_filtered = sellers[sellers['seller_id'].isin(
        order_items_filtered['seller_id'])]

    # Dictionary with filtered DataFrames
    dfs = {
        "orders": orders_filtered,
        "order_items": order_items_filtered,
        "payments": payments_filtered,
        "customer": customer_filtered,
        "products": products_filtered,
        "sellers": sellers_filtered,
    }

    # Relative path to save files
    current_dir = os.getcwd()
    processed_path = os.path.abspath(os.path.join(
        current_dir, "..", "data", "processed"))

    # Save DataFrames to CSV files
    for file_name, df in dfs.items():
        file_path = os.path.join(processed_path, f"{file_name}.csv")
        df.to_csv(file_path, index=False)

    return dfs
