import os
from dotenv import load_dotenv

load_dotenv()


def get_mongo_uri():
    return os.getenv("MONGODB_URI")


def get_mongo_db():
    # Se precisar usar o nome do DB em separado, coloque aqui ou extraia da URI
    return os.getenv("MONGODB_DATABASE") or "bcb_data"


def get_mongo_collection():
    return os.getenv("MONGODB_COLLECTION") or "cotacoes"
