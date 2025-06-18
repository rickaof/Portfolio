import logging
from load import load_to_mongo, log_pipeline_execution
from transform import transform_currency_data
from extract import extract_currency_data
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow import DAG
import os
import sys
# Adiciona o caminho da pasta ETL_Dolar_Airflow/src ao sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "src")))


logging.basicConfig(filename="logs/etl_dolar.log", level=logging.INFO)


def run_etl():
    today = datetime.today()
    if today == datetime(2025, 6, 1):
        start_date = "01-01-2025"
        end = (today - timedelta(days=1)).strftime("%m-%d-%Y")
    else:
        start_date = end = (today - timedelta(days=1)).strftime("%m-%d-%Y")
    try:
        logging.info(f"Iniciando ETL de {start_date} a {end}")
        raw_data = extract_currency_data(start_date, end)
        clean_data = transform_currency_data(raw_data)
        load_to_mongo(clean_data)
        log_pipeline_execution(start_date, end, len(
            clean_data), status="sucesso")
        logging.info("ETL finalizado com sucesso")
    except Exception as e:
        logging.error(f"Erro na execução do ETL: {str(e)}")
        log_pipeline_execution(
            start_date, end, 0, status="erro", mensagem_erro=str(e))
        raise


with DAG(
    dag_id="etl_dolar_bcb",
    start_date=datetime(2025, 6, 1),
    schedule="@daily",
    catchup=True,
    default_args={"retries": 1, "retry_delay": timedelta(minutes=2)},
    tags=["ETL", "BCB", "Dólar"]
) as dag:
    executar_etl = PythonOperator(
        task_id="executar_etl_dolar",
        python_callable=run_etl
    )
