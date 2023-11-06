from pymongo.database import Database
from app.models.test import Test
from app.crud.test import CRUDTests


class TestApi:
    @staticmethod
    def add_doc(db: Database, doc: Test):
        crud_tests = CRUDTests(db)
        return crud_tests.create(doc)