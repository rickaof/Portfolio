import os


def get_mongo_uri():
    return os.environ.get("MONGODB_URI")