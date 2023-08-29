#!/usr/bin/env python
# coding: utf-8

# Q-1 What is MongoDB ? Explain non-relational database in short . In which scenaries it is perforred to use MongoDB over SQL databases ?

# Ans-1 MongoDB is an open-source document-oriented database that is designed to store a large scale of data and also allows you to work with that data and also allows you to work with that data very efficiently . It is categorized under the NoSQL database because the storage and retrieval of data in the MongoDB are not in the form of table.
# 
# NoSQL is non-relational database allow structure and semistructure data to be stored and manipulated .
# MongoDB used when large dataset constantly changed as sql work on static dataset.

# Q-2 State and Explain the features of MongoDB .

# Ans-2 
#     
#     Schema-less Database:  It is the great feature provided by the mongodb . A schema-less database means one collection can                                 hold different types of document in it.
#     
#     
#     Document Oriented:     In mongodb all the data stored in the documents instead of tables like in RDBMS .In these documents,                            the data is stored in fields (key value pair) instead of rows  and columns which make the data much                              more flexible in comparison to RDBMS.
#     
#     INDEXING:    In mongodb database , every field in the document is indexed with primary and secondary  indices this makes                      easier  and takes less time to get or search data from the pool of data.If the data is not indexed , then                        database search each document with the specified query which takes lots of time and not so efficient.
#     
#     
#     Scalability: Mongodb provides horizontal scalability with the help of sharding . sharding means to distribute data on                        multiple servers , here a large amount of data is partitioned into data chunks using the shared key , and these                  data chunks are evenly distributed across shards that reside across many physical servers.It will also add new                  machines to a running database.

# Q-3 Write a code to connect mongodb to python . Also , create a database and a collection in mongodb.

# In[1]:


from connecting mongodb in python 
pip install pymango
import pymango
myclient = pymango.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol= mydb["customers"]


# Q-4 Using the database and the collection created in question number 3, write a code to insert one record,and insert many records. Use the find() and find_one() methods to print the inserted record.

# In[2]:


import pymango
myclient = pymango.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol= mydb["customers"]
mydict= {"name":"john","address":"highway 37"}
x= mycol.insert_one(mydict)

import pymango
myclient = pymango.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol= mydb["customers"]

mylist=[
    {"name":"Amy","address":"apple st 650"},
    {"name":"Hannah","address":"Mountain 21"},
    {"name":"Michael","address":"valley 345"},
    {"name":"Sandy","address":"ocean blvd 2"},
    {"name":"Betty","address":"green grass 1"}
]
x=mycol.insert_many(mylist)
print(x.inserted_ids)

import pymango
myclient = pymango.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol= mydb["customers"]

for x in mycol.find():
    print(x)


# Q-5 Explain how you can use the find() method to query the mongodb database. writea simple code to demonstrate this.

# In[3]:


'''
To select data from a table in mongodb , we use the find() method . the finf() return all occurences in the selection 
first paramerter of the find() method is a query object.

db.inventory.insert_one(
 {
    "item":"canvas",
    "qty":100,
    "tags":["cotton"],
    "size":{"h":"28","w":35.5,"uom":"cm"},
 })
  cursor= db.inventory.find({"item":"canvas"})
  '''


# Q-6 Explain the sort() method .Give an exampl to demostrate sorting in mongodb.

# In[4]:


'''
sort() method are used to sort the result in asceding and descending order.sort() method takes one parameter for "field 
 and one parameter for "direcrtion",
 
 import pymango
myclient = pymango.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol= mydb["customers"]
mydoc= mycol.find().sort("name")
for x in mydoc:
print(x)
'''


# Q-7 Explain why delete_one(), delete_many(), and drop() is used.

# In[5]:


'''delete_one() used to delete one document , the first parameters of delete_one() method is a query object defining which do to delete.
delete_many() used to delete more than one document, the first parameter of delete_many() method is a query object defining document to delete.
drop() used to delete a table , or collection as it is called in mongodb by using dro() methods.drop() method return true was dropped successfully, and false if the collection does not exists.'''


# In[ ]:




