import json
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb://localhost')

db = client.hw1

with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author'][0]})
    if author:
        db.quotes.insert_one(
            {'quote': quote['quote'],
             'tags': quote['keywords'],
             'author': ObjectId(author['_id'])})
        