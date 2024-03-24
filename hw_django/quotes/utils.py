from pymongo import MongoClient

def get_mongo():
    client = MongoClient('mongodb://localhost')
    db = client.hw1
    return db