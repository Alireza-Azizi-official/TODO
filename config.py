from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os


uri = os.getenv('URI')

client = MongoClient(uri, server_api=ServerApi("1"))

db = client.todo_db
collection = db["todos"]
