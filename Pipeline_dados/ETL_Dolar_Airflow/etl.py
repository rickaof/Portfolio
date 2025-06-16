from src.extract import extract_currency_data
from src.transform import transform_currency_data
from src.load import load_to_mongodb, show_inserted_data
import logging
import os

# Criando a pasta logs
current_dir = os.path.dirname(__file__)
log_dir = os.path.join(current_dir, "logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "etl.log")
logging.basicConfig(filename=log_file, level=logging.INFO)


def run_pipeline(start_date, end_date):
    try:
        logging.info(f"Iniciando ETL de {start_date} até {end_date}")
        raw_data = extract_currency_data(start_date, end_date)
        logging.info(f"Extração concluída com {len(raw_data)} registros.")

        clean_data = transform_currency_data(raw_data)
        logging.info("Transformação concluída")

        load_to_mongodb(clean_data)
        logging.info("Dados carregados com sucesso no MongoDB")

        show_inserted_data()

    except Exception as e:
        logging.error(f"Pipeline falhou: {str(e)}")


if __name__ == "__main__":
    print("=== ETL de Cotações do Dólar ===")
    start = input("Informe a data inicial (dd/mm/yyyy): ")
    end = input("Informe a data final (dd/mm/yyyy): ")
    run_pipeline(start, end)
