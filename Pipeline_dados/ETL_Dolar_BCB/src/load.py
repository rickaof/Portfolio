from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os


def connection():
    """Retorna a string de conexão com MongoDB lida da variável de ambiente."""
    uri = os.getenv("MONGODB_URI")
    if not uri:
        raise ValueError(
            "A variável de ambiente MONGODB_URI não está configurada.")
    return uri


def get_mongo_collection(db_name="bcb_data", collection_name="cotacoes"):
    """Conecta no MongoDB e retorna a coleção desejada."""
    uri = connection()
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection


def load_to_mongodb(data, db_name="bcb_data", collection="cotacoes"):
    """Insere os dados transformados no MongoDB"""
    collection = get_mongo_collection()
    collection.insert_many(data)
    print(f"Inseridos {len(data)} documentos.")


def show_inserted_data(db_name="bcb_data", collection="cotacoes", limit=5):
    """Exibe os dados inseridos no MongoDB."""
    collection = get_mongo_collection()
    documentos = collection.find().sort("dataHoraCotacao", -1).limit(limit)

    print("\n Exibindo os últimos dados inseridos:")
    for doc in documentos:
        print(doc)
