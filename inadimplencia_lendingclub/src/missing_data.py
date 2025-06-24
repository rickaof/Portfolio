# Bibliotecas
from pyspark.sql.functions import col, trim, lower, isnan
from pyspark.sql.types import StringType, NumericType
from pyspark.sql import Row


# Verificando valores ausentes
def missing_report(df):
    """
    Gera um relatório com contagem e percentual de valores ausentes (nulls, strings vazias, etc).

    :param df: DataFrame Spark
    :return: DataFrame Spark com ['column_name', 'data_type', 'missing_count', 'missing_percent']
    """
    total_rows = df.count()
    spark = df.sparkSession
    missing_info = []

    # Lista de valores textuais considerados como ausentes
    missing_strings = ["", "na", "n/a", "null", "none", "nan"]

    for field in df.schema.fields:
        col_name = field.name
        dtype = field.dataType
        c = col(col_name)

        # Começa com null como condição base
        condition = c.isNull()

        # Se for string, adiciona condições extras
        if isinstance(dtype, StringType):
            condition = condition | (trim(c) == "") | lower(
                trim(c)).isin(missing_strings)

        # Se for numérico, adiciona isnan()
        elif isinstance(dtype, NumericType):
            condition = condition | isnan(c)

        # Conta valores ausentes
        missing_count = df.filter(condition).count()
        missing_percent = round((missing_count/total_rows)*100, 2)

        missing_info.append(Row(
            column_name=col_name,
            data_type=dtype.simpleString(),
            missing_count=missing_count,
            missing_percent=missing_percent
    ))

    return spark.createDataFrame(missing_info)
