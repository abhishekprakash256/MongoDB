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

### Commands - 

```shell
mongod   #to list data
```





### Notes 

- Fix mongod not staring

- ```sh
  sudo rm -rf /tmp/mongodb-27017.sock 
  sudo systemctl start mongod
  ```

  









### Links 

```
https://www.youtube.com/watch?v=pWbMrx5rVBE
https://askubuntu.com/questions/823288/mongodb-loads-but-breaks-returning-status-14   (momgodb not starting)
```

