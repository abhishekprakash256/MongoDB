"""
A program to connect to the mongodb and get the data 
"""

import pymongo

from pymongo import MongoClient

cluster ="mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false" 

client = MongoClient(cluster)

print(client.list_database_names())

db = client.test

print(db.list_collection_names())

#make a dictionary to add the data 

todo1 = {"Name": "Abhi", "Task": "my first task2", "Status":"open"
	}


#make a list to add multiple data in the db
todo2 = [{"Name": "Abhi2", "Task": "my first task", "Status":"open"
	}, {"Name": "Abhi3", "Task": "my first task", "Status":"open"
	}]


todos = db.todos

#result = todos.insert_one(todo1) #one addition 

#result = todos.insert_many(todo2)  #muti addition 


#to retrive the items

#result = todos.find_one()

#to find matches

result = todos.find_one({"Name":"Abhi2"})

print(result)

#deleting an item

from bson.objectid import ObjectId

#removing_item = todos.delete_one({"Name": "Abhi"})

#update the items

result = todos.update_one({"Name":"Abhi2"}, {"$set":{"Alias":"Abhi_new"}})


