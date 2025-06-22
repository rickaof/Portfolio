from pyspark.sql import SparkSession

_spark = None  # variável privada para guardar a instância


def get_spark_session(app_name="LendingClubETL"):
    """
    Cria ou retorna uma SparkSession singleton para todo o projeto.

    :param app_name: Nome do app que aparecerá no Spark UI.
    :return: SparkSession
    """
    global _spark

    if _spark is None:
        _spark = SparkSession.builder \
            .appName(app_name) \
            .master("local[*]") \
            .config("spark.driver.memory", "2g") \
            .getOrCreate()
    return _spark
