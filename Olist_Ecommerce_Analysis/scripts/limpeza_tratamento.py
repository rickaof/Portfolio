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

# ANALISANDO O DATASET "GEOLOCATION".

pd.set_option("display.max_columns", None)
print(geolocation.head())

# Verificando a existencia de dados nulos.
print(geolocation.isnull().sum())
""" O dataset não possui dados nulos. """

# Verificando se os tipos de dados estão corretos.
print(geolocation.dtypes)
""" Os tipos de dados estão corretos. """

# ANALISE EXPLORATÓRIA DOS DADOS COM VISUALIZAÇÕES.

# Contagem de pedidos por status.
plt.figure(figsize=(10, 5))
ax = sns.countplot(data=orders, x="order_status", order=orders[
    "order_status"].value_counts().index, palette="pastel")
plt.xticks(rotation=45)
plt.yscale("log")
plt.title("Distribuição dos Status dos Pedidos")
plt.xlabel("Status do pedido")
plt.ylabel("Quantidade")
for p in ax.patches:
    ax.annotate(
        f"{int(p.get_height())}",
        (p.get_x() + p.get_width() / 2, p.get_height()),
        ha="center",
        va="bottom",
        fontsize=10,
        color="black"
    )
plt.show()
""" A grande maioria dos pedidos foram entregues, indicando que o sistema de
entrega dos pedidos está funcionando bem. """

# Análise dos pedidos ao longo do tempo.

orders["order_purchase_month"] = orders["order_purchase_timestamp"].dt.to_period(
    "M")
monthly_orders = orders.groupby("order_purchase_month")["order_id"].count()
plt.figure(figsize=(12, 6))
plt.plot(monthly_orders.index.astype(
    str), monthly_orders.values, marker='o', linestyle="-", color="royalblue")
plt.title("Evolução dos pedidos ao Longo do tempo")
plt.xlabel("Mês")
plt.ylabel("Quantidade de Pedidos")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

""" Os pedidos tiveram uma tendência de crescimento entre dezembro de 2016 até 
novembro de 2017, seguido de um perído de estabilização entre dezembro de 2017 até
agosto de 2018. Contudo, houve uma queda acentuada do número de pedidos de Agosto a 
Outubro, por isso é preciso checar se existem dados referente aos últimos meses
ou se os dados simplesmente acabaram."""

# Verificando se existem informações de pedidos nos últimos meses.
print(monthly_orders.tail(12))  # Últimos 12 meses disponíveis
""" Houveram pedidos nos últimos meses."""

# Verificando os últimos 10 pedidos.
pd.set_option("display.max_columns", None)
print(orders.sort_values(by="order_purchase_timestamp", ascending=False).head(10))

""" Todos os últimos 10 pedidos foram cancelados, indicando que houve algum grave problema
nos últimos meses, ainda não é possível identificar a razão e o motivo dos
cancelamentos e da queda tão acentuada no número de pedidos. """

# Analisando o tempo de entrega dos pedidos.

# Criando coluna de tempo de entrega em dias.
orders["delivery_time"] = (
    orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"]).dt.days

# Análise do tempo de entrega.
print(orders["delivery_time"].describe())

plt.figure(figsize=(8, 5))
sns.histplot(orders["delivery_time"].dropna(), bins=20, kde=True, color="blue")
plt.title("Distribuição do Tempo de Entrega")
plt.xlabel("Dias")
plt.ylabel("frequência")
plt.show()

""" O gráfico indica que o tempo de entrega se concentra entre 10 e 20 dias, é importante
analisar se o tempo médio de entrega aumentou nos últimos meses, podendo ser uma
possível razão para a queda acentuada de pedidos nos últimos meses. """

# Analisando o tempo médio de entrega ao longo dos meses.

# Criando uma nova coluna com o mês de compra
orders["order_purchase_month"] = orders["order_purchase_timestamp"].dt.to_period(
    "M")

# Calculando o tempo médio de entrega por mês
monthly_delivery_time = orders.groupby("order_purchase_month")[
    "delivery_time"].mean()

# Plotando o gráfico
plt.figure(figsize=(12, 5))
plt.plot(monthly_delivery_time.index.astype(
    str), monthly_delivery_time.values, marker='o', linestyle="-", color="purple")
plt.xticks(rotation=45)
plt.title("Tempo Médio de Entrega ao Longo dos Meses")
plt.xlabel("Mês")
plt.ylabel("Tempo Médio de Entrega (dias)")
plt.grid(True)
plt.show()

""" O tempo médio de entregas era alto no início, mas abaixou consideravelmente a partir
do 3 mês. O tempo médio teve baixa oscilação ao longo dos meses posteriores, com uma ligeira
queda nos últimos 3 meses. Portanto, não se pode atribuir a queda no número de pedidos ao
tempo de entrega dos produtos. """

# Verificando a proporção de cancelamentos ao longo dos meses.
orders.groupby("order_purchase_month")["order_status"].value_counts(
    normalize=True).unstack()["canceled"].plot(kind="line", figsize=(12, 5))
plt.title("Proporção de Pedidos Cancelados por Mês")
plt.xlabel("Mês")
plt.ylabel("Cancelamentos (%)")
plt.show()
