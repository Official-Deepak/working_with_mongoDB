import pymongo
from pymongo import MongoClient
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import json
from bson.objectid import ObjectId

#office work
from requests_html import HTMLSession
# Connection details
host = 'srvr2px.cyberads.io'
port = 27017
username = 'cmrslpx1a'
password = 'u@YjkgD#)TR&7dC'
auth_source = 'admin'
database = 'quizes'
collection = 'mcq2'

# Create MongoClient with authentication
client = MongoClient(host=host, port=port, username=username, password=password,authSource=auth_source)

# Access the desired database and collection
db = client[database]
collection = db[collection]
collection1 =  db["mcq"]

#function for finding data by id and parsing into json
def fetch_data(id):
    data = collection.find_one(id)
    all_data = data["query"]
    parse = json.loads(all_data)
    return parse

#using above function
#basketball
#for id 1
#id = {"_id":ObjectId("64bc55f1501c0db6bd314810")}
#collection1.insert_many(fetch_data(id))


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    #print(client)
    db = client["deepak"]
    collection = db["placement"]
    """
    #inserting data
    #dic = {"name":"deepak","post":"software_services"}
    #collection.insert_one(dic)
    data = [
        {"name":"Aarti","post":"HR"},
        {"name":"Rohit","post":"acccountant"}
    ]
    collection.insert_many(data)
    """
    #fetching data
    """"
    #one = collection.find_one({"name":"Aarti"})
    #print(one)
    all_data = collection.find({},{"_id":0,})
    #print(all_data)
    print(all_data.count())
    for item in all_data:
        print(item)
     
    #code to check database
    a = client.list_database_names()
    print(a)
       """
    
    #code to check collection in a database
    #print(db.list_collection_names())

    #updating in database
    #pre = {"name":"Aarti"}
    #nextt = {"$set":{"post":"HR Manager"}}
    #collection.update_one(pre,nextt)
    #m = collection.update_many({},{"$set":{"category":"onCampus"}})
    #print(m.modified_count)

    #deletimg from database
    #rec = {"name":"Rohit"}
    #collection.delete_one(rec)
    #a = collection.delete_many(rec)
    #print(a.deleted_count)
    


    


