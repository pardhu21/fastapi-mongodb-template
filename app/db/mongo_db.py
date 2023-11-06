from contextlib import contextmanager
from typing import Generator

from pymongo import MongoClient

from app.config.config import config

mongo_client = MongoClient(config.MONGODB_URI)


@contextmanager
def acquire_mongo_db(db: str = config.MONGODB_DATABASE) -> Generator:
    try:
        yield mongo_client.get_database(db)
    except Exception as ex:
        raise ex
