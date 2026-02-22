
import pymongo
from bson import ObjectId


class Crud:
    """Reusable CRUD class for MongoDB operations."""

    def __init__(self, uri, db_name="school", collection_name="students"):
        """Initialize MongoDB connection."""
        try:
            self.client = pymongo.MongoClient(uri)
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]

        except pymongo.errors.ConnectionFailure as error:
            print(f"MongoDB connection error: {error}")
            self.client = None

    def insert_data(self, data: dict):
        """Insert a new document."""
        if not self.client:
            print("Connection not established.")
            return None

        try:
            result = self.collection.insert_one(data)
            return result.inserted_id

        except pymongo.errors.PyMongoError as error:
            print(f"Insert error: {error}")
            return None

    def create_query(self, filter_query: dict):
        """Return documents that match filter."""
        if not self.client:
            print("Connection not established.")
            return []

        try:
            documents = list(self.collection.find(filter_query))
            return documents

        except pymongo.errors.PyMongoError as error:
            print(f"Query error: {error}")
            return []

    def read_documents(self):
        """Return all documents."""
        if not self.client:
            print("Connection not established.")
            return []

        try:
            return list(self.collection.find())

        except pymongo.errors.PyMongoError as error:
            print(f"Read error: {error}")
            return []

    def update(self, document_id: str, new_values: dict):
        """Update document by ID."""
        if not self.client:
            print("Connection not established.")
            return 0

        try:
            result = self.collection.update_one(
                {"_id": ObjectId(document_id)},
                {"$set": new_values},
            )
            return result.modified_count

        except pymongo.errors.PyMongoError as error:
            print(f"Update error: {error}")
            return 0

    def delete(self, filter_query: dict):
        """Delete documents matching filter."""
        if not self.client:
            print("Connection not established.")
            return 0

        try:
            result = self.collection.delete_one(filter_query)
            return result.deleted_count

        except pymongo.errors.PyMongoError as error:
            print(f"Delete error: {error}")
            return 0

    def close_connection(self):
        """Close database connection."""
        if self.client:
            self.client.close()
