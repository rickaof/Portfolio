from src.data_loader import load_olist_datasets
from src.data_cleaning import (
    check_missing_and_duplicates,
    order_type_conversion,
    products_treatment,
    olist_filter_and_save
)
from src.exploratory_data_analysis import (
    merge_datasets,
    detect_outliers_iqr,
    calculate_vif,
    plot_boxplots_by_delivery

)
from src.model import train_evaluate_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier


def main():
    print("Starting Olist pre-processing pipeline...")


# 1. Load raw datasets into dictionary of DataFrames
dfs = load_olist_datasets()
print("Raw data successfully loaded.")

# Extract individual DataFrames from dictionary
orders = dfs["orders"]
order_items = dfs["order_items"]
payments = dfs["payments"]
customer = dfs["customer"]
products = dfs["products"]
sellers = dfs["sellers"]
geolocation = dfs["geolocation"]

# 2. Perform initial data audit (optional diagnostics)
check_missing_and_duplicates({
    "orders": orders,
    "order_items": order_items,
    "payments": payments,
    "customer": customer,
    "products": products,
    "sellers": sellers
})

# 3. Apply type conversions and missing value treatments
orders = order_type_conversion(orders)
products = products_treatment(products)
print("Type conversions and imputations applied.")


# 4. Filter datasets by relevant months and save to /data/processed/
dfs_filtered = olist_filter_and_save(
    orders, order_items, payments, customer, products, sellers
)
print("Filtered data saved to data/processed/ directory.")


# 5. Merge multiple pre-filtered Olist datasets into a single DataFrame
df_merged = merge_datasets(
    dfs_filtered["orders"],
    dfs_filtered["order_items"],
    dfs_filtered["customer"],
    dfs_filtered["products"],
    dfs_filtered["payments"],
    dfs_filtered["sellers"]
)
print(f"Datasets successfully merged. Shape: {df_merged.shape}")

# 5.5 Create target variable 'is_late'
df_merged["is_late"] = (
    df_merged["order_delivered_customer_date"] >
    df_merged["order_estimated_delivery_date"]
).astype(int)
print("Target variable 'is_late' created.")


# 6. Outlier detection (example: distance_seller_customer)
print("🔍 Checking outliers for 'freight_value'...")
detect_outliers_iqr(df_merged['freight_value'])


# 7. Calculate VIF for numeric variables
numeric_cols = [
    'freight_value', 'price', 'payment_value', 'product_length_cm',
    'product_height_cm', 'product_width_cm', 'product_weight_g'
]
df_numeric = df_merged[numeric_cols].dropna()
vif_result = calculate_vif(df_numeric)
print("VIF Scores:")
print(vif_result)


# 8. Select features and target
y = df_merged["is_late"]
X = df_merged.drop(columns='is_late')

# 9 Compare multiple models
print("\n Comparing Models...\n")

models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
}

for name, model in models.items():
    print(f"\n🔍 Model: {name}")
    train_evaluate_model(model, X, y, scale_data=(
        name == "Logistic Regression"))
