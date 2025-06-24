# Importando bibliotecas
from spark_session import get_spark_session
import os
import pandas as pd

# Leitura inicial do dataset
spark = get_spark_session()

# Carregando dados csv spark
def load_csv_spark(spark, folder, file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.abspath(os.path.join(current_dir, "..", folder))
    file_path = os.path.join(folder_path, file)
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    return df

# Salvando em um arquivo parquet
def save_parquet_spark(df, folder, file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.abspath(os.path.join(current_dir, '..', folder))
    file_path = os.path.join(folder_path, file)
    df.write.mode("overwrite").parquet(file_path)

# Carregando arquivos parquet pandas
def read_parquet_pandas(folder):
    current_dir = os.path.dirname(__file__)
    data_path = os.path.abspath(os.path.join(current_dir, "..", folder))

    files = [file for file in os.listdir(data_path) if file.endswith(".parquet")]
    files.sort()

    dfs = [
        pd.read_parquet(os.path.join(data_path, file), engine="pyarrow")
        for file in files
    ]
    return pd.concat(dfs, ignore_index=True)