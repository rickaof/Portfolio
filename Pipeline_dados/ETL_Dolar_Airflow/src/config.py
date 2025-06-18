from dotenv import load_dotenv
import os

load_dotenv()

try:
    from airflow.models import Variable

    def get_variable(key, default=None):
        return Variable.get(key, default_var=default)
except ImportError:
    def get_variable(key, default=None):
        return os.getenv(key, default)


def get_mongo_uri():
    return get_variable("MONGODB_URI")
