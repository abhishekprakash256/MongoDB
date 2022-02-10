## MongoDB



### Installation 

- ```bash
  wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
  sudo apt-get install gnupg
  wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
  echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
  sudo apt-get update
  sudo apt-get install -y mongodb-org
  ```

- ```bash
  sudo systemctl start mongod  (to start)
  sudo systemctl stop mongod  (to stop)
  sudo systemctl status mongod  (to check the status)
  
  ```

  - Install mongodb compass from website (it's a GUI tool)

  - To official driver are there (pymongo (it is preferred)) 

    ```
    pip install pymongo
    ```

### Working - 

- Code example  (connection to the mongodb)

  ```python
  from pymongo import MongoClient
  cluster ="mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false" 
  client = MongoClient(cluster)
  ```

- test a database is already created in the mongodd

- to insert and object in the database use a dictionary and the list data structure 

  ```python
  #make a list to add multiple data in the db
  todo2 = [{"Name": "Abhi2", "Task": "my first task", "Status":"open"
  	}, {"Name": "Abhi3", "Task": "my first task", "Status":"open"
  	}]
  ```

- Insertion in the db 

  ```python
  result = todos.insert_one(todo1) #one addition 
  result = todos.insert_many(todo2)  #muti addition 
  ```

- find one 

  ```python
  result = todos.find_one({"Name":"Abhi2"})
  ```

- to get the id of the object 

  ```python
  from bson.objectid import ObjectId
  ```

- to update or add an item 

```python
result = todos.update_one({"Name":"Abhi2"}, {"$set":{"Alias":"Abhi_new"}})
```

### Pymongo methods

- db collection and listing

```python
client.list_database_names()        #list all the dataabses
db = client.test  #connection to the database
db.list_collection_names()  #to list the collections names

```

- db insertion inside collections

```python
db = client.test  #test is already craeted there
#creating a new collection there
todo1 = {"_id": 1, "name": "abhi", "age": 25}
#connetion to todos
todos = db.todos
result = todos.insert_one(todo1)
```

- if _id is same the data will not be inserted in the MongoDB will raise bulk error , it should be unique

- Finding the data 

  ```python
  db = client.test  #test is already craeted there
  #connetion to todos
  todos = db.todos
  result = todos.find_one({"name" : "abhi"})
  ```

- iteration over the collection objects

```python
db = client.test  #test is already craeted there
#connetion to todos
todos = db.todos
results = todos.find({"name" : "abhi"})
#iteration oever the results
for result in results:
	print(result)
```

- we can also convert to the list to objects

- get the number of the items

  ```python
  print(todos.count_documents({"name": "abhi"}))
  ```

- to remove the data 

  ```python
  todos = db.todos
  from bson import ObjectId
  result = todos.delete_one({"_id": 1}) #delete many
  ```

- to update use 

```python
todos.update_item(previous_item, new_item)  #as above 
```



### Notes 

- stores data in form of BSon  (binary json file)

- No single record can be greater than 16 MB

- Application database

- micro service thing 

- it is a document database 

- range of query is focused 

- No SQL database

- mongod is the parent process 

- pymongo is a driver to interact with MongoDB

- Can make a id if specified in the data 

- easy to scale and faster in most operation]

- collections are used 

- works on doc like system

  
  
  ```python
  {'_id':1, 'Name': "Abhi"}
  ```


### Data base 

- database should have collections 
- create a database and then collections 
- multiple insert can take list of dictionaries 
- collection can be multilevel and nested

### Commands - 

```shell
mongod   #to list data
```

### Fixing notes 

- Fix mongod not staring

- ```sh
  sudo rm -rf /tmp/mongodb-27017.sock 
  sudo systemctl start mongod
  ```

  









### Links 

```
https://www.youtube.com/watch?v=pWbMrx5rVBE
https://askubuntu.com/questions/823288/mongodb-loads-but-breaks-returning-status-14   (momgodb not starting)
https://www.youtube.com/watch?v=qWYx5neOh2s
```

