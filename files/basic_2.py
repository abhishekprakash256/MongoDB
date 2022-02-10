"""
The file is about the data retriving

"""

from pymongo import MongoClient

cluster = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

client = MongoClient(cluster)


db = client.test  #test is already craeted there

#connetion to todos
todos = db.todos

results = todos.find({"name" : "abhi"})

#iteration oever the results

for result in results:
	print(result)

print(todos.count_documents({"name": "abhi"}))