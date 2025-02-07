from pymongo import MongoClient

class DataBase:
    def __init__(self, DB_Name: str, MongoURI: str):
        self.client = MongoClient(MongoURI)
        self.dataBase = self.client[DB_Name]

    # Create Operations
    def add_doc(self, collection, document):
        return self.dataBase[collection].insert_one(document)

    def add_docs(self, collection, documents):
        return self.dataBase[collection].insert_many(documents)

    # Read Operations
    def find_doc(self, collection, query):
        return self.dataBase[collection].find_one(query)

    def find_docs(self, collection, query):
        return self.dataBase[collection].find(query)

    def find_all(self, collection):
        return self.dataBase[collection].find()

    def count_docs(self, collection, query):
        return self.dataBase[collection].count_documents(query)

    # Update Operations
    def update_doc(self, collection, filter_query, update_data):
        result = self.dataBase[collection].update_one(filter_query, {'$set': update_data})
        return result.modified_count

    def update_docs(self, collection, filter_query, update_data):
        result = self.dataBase[collection].update_many(filter_query, {'$set': update_data})
        return result.modified_count

    # Delete Operations
    def delete_doc(self, collection, query):
        result = self.dataBase[collection].delete_one(query)
        return result.deleted_count

    def delete_docs(self, collection, query):
        result = self.dataBase[collection].delete_many(query)
        return result.deleted_count

    # Aggregate Operations
    def aggregate(self, collection, pipeline):
        return self.dataBase[collection].aggregate(pipeline)

    # Index Operations
    def create_index(self, collection, keys, **kwargs):
        return self.dataBase[collection].create_index(keys, **kwargs)

    def drop_index(self, collection, index_name):
        return self.dataBase[collection].drop_index(index_name)

    def list_indexes(self, collection):
        return self.dataBase[collection].list_indexes()

    # Collection Operations
    def drop_collection(self, collection):
        self.dataBase[collection].drop()

    def list_collections(self):
        return self.dataBase.list_collection_names()

    # Transactions
    def start_session(self):
        return self.client.start_session()

    # Bulk Write
    def bulk_write(self, collection, operations):
        return self.dataBase[collection].bulk_write(operations)

    # Replace Document
    def replace_doc(self, collection, filter_query, replacement):
        result = self.dataBase[collection].replace_one(filter_query, replacement)
        return result.modified_count

    # Distinct
    def distinct(self, collection, field, query=None):
        return self.dataBase[collection].distinct(field, query)

    # MapReduce
    def map_reduce(self, collection, map_function, reduce_function, out):
        return self.dataBase[collection].map_reduce(map_function, reduce_function, out)

    # Rename Collection
    def rename_collection(self, old_name, new_name):
        return self.dataBase[old_name].rename(new_name)

    # Watch for Changes
    def watch(self, collection=None, pipeline=None):
        if collection:
            return self.dataBase[collection].watch(pipeline)
        return self.dataBase.watch(pipeline)

    # Server Status
    def server_status(self):
        return self.client.admin.command("serverStatus")

    # Database Stats
    def db_stats(self):
        return self.dataBase.command("dbstats")

    # Collection Stats
    def collection_stats(self, collection):
        return self.dataBase.command("collstats", collection)

    # Close Connection
    def close_connection(self):
        self.client.close()
