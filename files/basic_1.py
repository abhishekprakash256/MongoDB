"""
The file is about the data insertion and the data retriving

"""
from pymongo import MongoClient

cluster = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

client = MongoClient(cluster)


db = client.test  #test is already craeted there

#creating a new collection there

todo1 = {"_id": 1, "name": "abhi", "age": 25}

todo3 = [{"_id": 8, "name": "abi", "age": 5}, 
{"_id": 6, "name": "abfi", "age": 6}]

#connetion to todos
todos = db.todos

result = todos.insert_many(todo3)
