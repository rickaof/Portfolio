import pandas as pd


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
