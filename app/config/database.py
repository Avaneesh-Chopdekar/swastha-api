from pymongo import MongoClient

from .env import DB_URI


client = MongoClient(DB_URI)


def get_db():
    return client.get_database("arogyadb")
