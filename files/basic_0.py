"""
The file is about the database connection and handing the collections

"""




from pymongo import MongoClient

cluster = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"


client = MongoClient(cluster)


#connection sanity check
if client:
	print("connetion done")
else:
	raise (ValueError("not connected"))


##printing the databases
print(client.list_database_names())

#printing inside the bd 

db = client.test

#list the collections

print(db.list_collection_names())