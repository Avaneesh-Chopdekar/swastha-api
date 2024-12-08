from pymongo import MongoClient

from .env import DB_URI


client = MongoClient(DB_URI)


def get_db():
    try:
        db = client.get_database("swastha")
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
    finally:
        client.close()
