import os
import json
import pymongo

from dotenv         import load_dotenv
from bson.objectid  import ObjectId
load_dotenv()

ATLAS_URI   = os.getenv('ATLAS_URI')
DB_NAME     = os.getenv('DB_NAME')

def insert_data(table, adding_data):
    connection  = pymongo.MongoClient(ATLAS_URI)
    myDB        = connection [DB_NAME]
    table       = myDB[table]
    added       = table.insert_one(adding_data)
    data_id     = str(added.inserted_id)
    return data_id

def query_data_by_id(table, id):
    connection  = pymongo.MongoClient(ATLAS_URI)
    myDB        = connection [DB_NAME]
    table       = myDB[table]
    data        = table.find_one(ObjectId(id))
    return data

def query_data(table, colname=None, data_key=None):
    connection  = pymongo.MongoClient(ATLAS_URI)
    myDB        = connection [DB_NAME]
    table       = myDB[table]
    responses   = table.find()
    if colname != None:
        query       = {colname: data_key}
        responses   = table.find(query)
    data_list   = []
    for data in responses:
        data_list.append(data)
    return data_list

def update_data(table, condition, condition_data, colname, change_data):
    connection  = pymongo.MongoClient(ATLAS_URI)
    myDB        = connection [DB_NAME]
    table       = myDB[table]
    myquery     = {condition: condition_data}
    newvalues   = {"$set": {colname: change_data}}
    updated     = table.update_many(myquery, newvalues)
    return updated.modified_count
    
def duplicate_email(email):
    connection  = pymongo.MongoClient(ATLAS_URI)
    myDB        = connection [DB_NAME]
    table       = myDB["broker_info"]
    query       = {"email": email}
    responses        = table.find(query)
    for data in responses:
        if data == None:
            return False
        else:
            return True
        
def delete_data_by_id(table, id):
    connection  = pymongo.MongoClient(ATLAS_URI)
    myDB        = connection [DB_NAME]
    table       = myDB[table]
    query       = {'_id': ObjectId(id)}
    table.delete_one(query)
    
def delete_data(table, colname, data_key):
    connection  = pymongo.MongoClient(ATLAS_URI)
    myDB        = connection [DB_NAME]
    table       = myDB[table]
    query       = {colname: data_key}
    deleted     = table.delete_many(query)
    return deleted.deleted_count