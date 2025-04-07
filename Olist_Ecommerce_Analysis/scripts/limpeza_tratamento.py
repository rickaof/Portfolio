import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# carregando os datasets.

orders = pd.read_csv(
    'C:/Users/ricka/Desktop/Area de Trabalho/Projeto de Estudo Machine '
    'Learning/Projetos e Estudos Git - Machine Learning/Portifolio/'
    'Olist_Ecommerce_Analysis/data/datasets originais/olist_orders_dataset.csv'
)
order_items = pd.read_csv(
    'C:/Users/ricka/Desktop/Area de Trabalho/Projeto de Estudo Machine '
    'Learning/Projetos e Estudos Git - Machine Learning/Portifolio/'
    'Olist_Ecommerce_Analysis/data/datasets originais/olist_order_items_dataset.csv'
)
customers = pd.read_csv(
    'C:/Users/ricka/Desktop/Area de Trabalho/Projeto de Estudo Machine '
    'Learning/Projetos e Estudos Git - Machine Learning/Portifolio/'
    'Olist_Ecommerce_Analysis/data/datasets originais/olist_customers_dataset.csv'
)
products = pd.read_csv(
    'C:/Users/ricka/Desktop/Area de Trabalho/Projeto de Estudo Machine '
    'Learning/Projetos e Estudos Git - Machine Learning/Portifolio/'
    'Olist_Ecommerce_Analysis/data/datasets originais/olist_products_dataset.csv'
)
sellers = pd.read_csv(
    'C:/Users/ricka/Desktop/Area de Trabalho/Projeto de Estudo Machine '
    'Learning/Projetos e Estudos Git - Machine Learning/Portifolio/'
    'Olist_Ecommerce_Analysis/data/datasets originais/olist_sellers_dataset.csv'
)
payments = pd.read_csv(
    'C:/Users/ricka/Desktop/Area de Trabalho/Projeto de Estudo Machine '
    'Learning/Projetos e Estudos Git - Machine Learning/Portifolio/'
    'Olist_Ecommerce_Analysis/data/datasets originais/olist_order_payments_dataset.csv'
)
geolocation = pd.read_csv(
    'C:/Users/ricka/Desktop/Area de Trabalho/Projeto de Estudo Machine '
    'Learning/Projetos e Estudos Git - Machine Learning/Portifolio/'
    'Olist_Ecommerce_Analysis/data/datasets originais/olist_geolocation_dataset.csv'
)

# Verificando o números de linhas e colunas de cada dataset.

print("Orders:", orders.shape)
print("Order Items:", order_items.shape)
print("Customers:", customers.shape)
print("Products:", products.shape)
print("Sellers:", sellers.shape)
print("Payments:", payments.shape)
print("Geolocation:", geolocation.shape)

# ANALISANDO O DATASET "ORDERS"
pd.set_option("display.max_columns", None)
print(orders.head())


# Verificando se existem valores nulos.
print(orders.isnull().sum())

""" Existem dados numéricos nulos na coluna de data de aprovação da ordem,
indicando que as ordens não foram aprovadas. A coluna de data de envio também
possui dados nulos, indicando que o pedido não foi enviado. E, por fim, na coluna
data de entrega, indicando que o pedido não foi entregue. Contudo, os dados serão
mantidos como estão, pois o tipo da coluna será alterado para datetime e os valores
nulos serão NaT (Not a time). Isso mantém a coerência dos dados e evita problemas
com operações envolvendo datas."""

# Verificando o tipo dos dados.
print(orders.dtypes)

# Convertendo conlunas de data para datetime
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

# Convertendo colunas IDs para string.
orders["order_id"] = orders["order_id"].astype(str)
orders["customer_id"] = orders["customer_id"].astype(str)

# Convertendo a coluna "order status" para o tipo categoria.
orders["order_status"] = orders["order_status"].astype("category")

# Verificando se os tipos das variáveis corrigido.
print(orders.dtypes)

# ANALISANDO O DATASET "ORDERS_ITEMS."

pd.set_option("display.max_columns", None)
print(order_items.head())

# Verificando a existência de dados nulos.
print(order_items.isnull().sum())
""" Não existem dados nulos."""

# Verificando o tipo dos dados.
print(order_items.dtypes)
""" O tipo de dado encontrado que não condiz com o tipo de dado correto
da coluna, é o Shipping_limit_date, portanto essa coluna será convertida
do tipo objeto para datetime."""

# Convertendo a coluna shipping_limit_date para datetime.
order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"], errors="coerce")

# Verificando se o tipo de dado foi alterado.
print(order_items.dtypes)

# ANALISANDO O DATASET "CUSTOMERS".

pd.set_option("display.max_columns", None)
print(customers.head())

# Verificando a existência de dados nulos.
print(customers.isnull().sum())
""" Não existem dados nulos."""

# Verificando o tipo de dados de cada coluna.
print(customers.dtypes)
""" Os tipos de dados estão corretos."""

# ANALISANDO O DATASET "PRODUCTS".

pd.set_option("display.max_columns", None)
print(products.head())

# Verificando a existência de dados nulos.
print(products.isnull().sum())
""" Foram encontrados dados nulos no nome da categoria do produto,
o que será preenchido por "Desconhecido". Dados nulos também foram
encontrados nas colunas: comprimento do nome do produto, comprimento
da descrição e quantidade de fotos, os dados serão preenchidos com a 
mediana para evitar distorções causadas por valores extremos. Por fim,
fora encontrados dois dados nulos na colunas: peso, comprimento, altura
e largura, todos os dados também serão preenchidos com a mediana. 
"""
# Verificando o tipo de dados de cada coluna.
print(products.dtypes)
""" Os tipos de dados estão corretos."""

# Tratando os dados nulos.
products["product_category_name"].fillna("Desconhecido", inplace=True)
num_cols = [
    "product_name_lenght", "product_description_lenght",
    "product_photos_qty", "product_weight_g", "product_length_cm",
    "product_height_cm", "product_width_cm"
]
for col in num_cols:
    products[col].fillna(products[col].median(), inplace=True)

# Verificando se os dados nulos foram tratados.
print(products.isnull().sum())
""" Os dados foram tratados."""

# ANALISANDO O DATASET "SELLERS".

pd.set_option("display.max_columns", None)
print(sellers.head())

# Verificando a existência de dados nulos.
print(sellers.isnull().sum())
"""O dataset não possui dados nulos."""

# Verificando o tipo de dados de cada coluna.
print(sellers.dtypes)
""" Os tipos de dados estão corretos."""

# ANALISANDO O DATASET "PAYMENTS".

pd.set_option("display.max_columns", None)
print(payments.head())

# Analisando a presença de dados nulos.
print(sellers.isnull().sum())
""" O dataset não possui dados nulos. """

# Analisando os tipos de dados de cada coluna.
print(payments.dtypes)

# Alterando o tipo de dados da coluna payment_type para categoria.
print(payments["payment_type"].unique())
payments["payment_type"] = payments["payment_type"].astype("category")

# Verificando se o tipo da coluna foi alterado.
print(payments["payment_type"].dtypes)
""" O tipo de dado foi alterado. """
