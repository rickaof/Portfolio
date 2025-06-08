import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def merge_datasets(orders_filtered, order_items_filtered, customer_filtered,
                   products_filtered, payments_filtered, sellers_filtered):
    """ Merge multiple pre-filtered Olist datasets into a single DataFrame,
    Returns:
        DataFrame: Merged dataset containing all relevant features."""

    df_merged = orders_filtered.merge(
        order_items_filtered, on='order_id', how='left')
    df_merged = df_merged.merge(
        customer_filtered, on='customer_id', how='left')
    df_merged = df_merged.merge(products_filtered, on='product_id', how='left')
    df_merged = df_merged.merge(payments_filtered, on='order_id', how='left')
    df_merged = df_merged.merge(sellers_filtered, on='seller_id', how='left')
    return df_merged


def calculate_vif(df_numeric):
    vif_data = pd.DataFrame()
    vif_data["feature"] = df_numeric.columns
    vif_data["VIF"] = [variance_inflation_factor(
        df_numeric.values, i) for i in range(df_numeric.shape[1])]
    return vif_data


def plot_boxplots_by_delivery(df_merged, df_numeric, target_col='is_late'):
    log_scale_vars = ['freight_value', 'payment_value', 'price']
    for col in df_numeric.columns:
        # Chose the plot column
        plot_col = f'{col}_log' if col in log_scale_vars else col
        ylabel = f'Log(1 + {col.replace("_", " ").title()})' if col in log_scale_vars else col.replace(
            "_", " ").title()

        # if necessary create a new column
        if col in log_scale_vars and f'{col}_log' not in df_merged.columns:
            df_merged[plot_col] = np.log1p(df_merged[col])

        # plot
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='is_late', y=plot_col, data=df_merged, palette='Set2')
        plt.title(f'{ylabel} by Delivery Status')
        plt.xlabel('Is Late')
        plt.ylabel(ylabel)

        # show statistics
        stats = df_merged.groupby('is_late')[col].agg(
            ['mean', 'median']).round(2)
        for idx in stats.index:
            plt.text(idx, df_merged[plot_col].max()*0.9,
                     f"Mean: {stats.loc[idx, 'mean']}\nMedian: {stats.loc[idx, 'median']}",
                     ha='center', fontsize=9, bbox=dict(facecolor='white', alpha=0.6))

        plt.tight_layout()
        plt.show()
