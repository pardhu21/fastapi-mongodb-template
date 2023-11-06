import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.api_key import APIKey
from app.db.mongo_db import acquire_mongo_db

from app.models.test import Test
from app.api.api_v1.test.controller import TestApi
from app.db.mongo_db import acquire_mongo_db


logger = logging.getLogger(__name__)

test_router = APIRouter(
    prefix="/test",
    tags=["test"],
)

@test_router.post('/add-doc')
def add_doc(doc: Test):
    with acquire_mongo_db() as db:
        return TestApi.add_doc(db, doc)