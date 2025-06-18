from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from config import get_mongo_uri


def load_to_mongo(data, db_name="bcb_data", collection_name="cotacoes"):
    """Conecta no MongoDB e retorna a coleção desejada."""
    uri = get_mongo_uri()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    if data:
        collection.insert_many(data)
        print(f"Inseridos {len(data)} documentos.")


def log_pipeline_execution(start_date, end, qtd_registros, status="sucesso", mensagem_erro=None):
    uri = get_mongo_uri()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["bcb_data"]
    log = {
        "timestamp_execucao": datetime.now().isoformat(),
        "data_inicio": start_date,
        "data_fim": end,
        "qtd_registros": qtd_registros,
        "status": status,
        "mensagem_erro": mensagem_erro
    }
    db["log_execucoes"].insert_one(log)
