# Importando bibliotecas
from spark_session import get_spark_session
import os

# Leitura inicial do dataset
spark = get_spark_session()


def load_csv_spark(spark, folder, file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.abspath(os.path.join(current_dir, "..", folder))
    file_path = os.path.join(folder_path, file)
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    return df
