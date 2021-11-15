from pymongo import MongoClient

client = MongoClient()
db = client.password_manager_test01 
userdata = db.userdata

var = userdata

dbnames = db.list_collection_names()
if var not in dbnames:
    print("here")
else:
    print("not here")