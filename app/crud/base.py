from typing import Generic, Optional, TypeVar

from bson.objectid import ObjectId
from pydantic import BaseModel
from pymongo.collection import Collection

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class MongoCRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, collection: Collection):
        """
        MongoDB CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        Parameters:
        - collection: A MongoDB collection where CRUD operations will be performed.
        """
        self.collection = collection

    def create(self, obj_in: CreateSchemaType) -> str:
        obj_data = obj_in.dict()
        result = self.collection.insert_one(obj_data)
        return str(result.inserted_id)

    def read(self, item_id: str) -> Optional[ModelType]:
        item = self.collection.find_one({"_id": ObjectId(item_id)})
        if item:
            return ModelType(**item)
        return None

    def update(self, item_id: str, obj_in: UpdateSchemaType) -> Optional[ModelType]:
        obj_data = obj_in.dict(exclude_unset=True)
        result = self.collection.update_one(
            {"_id": ObjectId(item_id)}, {"$set": obj_data}
        )
        if result.modified_count > 0:
            return ModelType(**obj_data)
        return None

    def delete(self, item_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(item_id)})
        return result.deleted_count > 0
