"""
The file is about the data sorting and ranging

"""
import datetime

from pymongo import MongoClient

cluster = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

client = MongoClient(cluster)


db = client.test  #test is already craeted there

#connetion to todos
todos = db.todos


db = datetime.datetime(2021,2,9)

results = todos.find({"data": {"$lt":db}})

for result in results:
	print("in")
	print(result)
