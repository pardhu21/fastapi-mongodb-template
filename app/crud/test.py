from typing import Any
from pymongo.database import Database
from app.models.test import Test
from app.crud.base import MongoCRUDBase
from app.config.config import config
from bson.objectid import ObjectId


class CRUDTests(
    MongoCRUDBase[Test, Test, Test]
):
    def __init__(self, db: Database):
        super().__init__(db['test'])
