import pandas as pd
import os

# Loading the main dataset


def load_olist_datasets(data_folder="data/raw"):
    """
    Load Olist CSV files into a dictionary of dataframes
    Parameteres:
        data_folder : relative path from the root directory to the data folder.
    Returns:
        dict: Dictionary with table names as keys and pandas
        Dataframes as values.
    """
    current_dir = os.getcwd()
    data_path = os.path.abspath(os.path.join(current_dir, '..', data_folder))

    custom_names = {
        "olist_customers_dataset.csv": "customer",
        "olist_geolocation_dataset.csv": "geolocation",
        "olist_order_items_dataset.csv": "order_items",
        "olist_order_payments_dataset.csv": "payments",
        "olist_orders_dataset.csv": "orders",
        "olist_products_dataset.csv": "products",
        "olist_sellers_dataset.csv": "sellers"
    }

    files = os.listdir(data_path)

    dfs = {
        custom_names[file]: pd.read_csv(os.path.join(data_path, file))
        for file in files if file in custom_names
    }
    return dfs
