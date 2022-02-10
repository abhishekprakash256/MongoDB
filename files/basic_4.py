"""
remove the data from the db

"""

import datetime

from pymongo import MongoClient

cluster = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

client = MongoClient(cluster)


db = client.test  #test is already craeted there

#connetion to todos
todos = db.todos

from bson import ObjectId

result = todos.delete_one({"_id": 8})

print(type(result))