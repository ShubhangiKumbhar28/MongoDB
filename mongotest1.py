import pymongo
client = pymongo.MongoClient("mongodb+srv://shubhangikumbhar28:shu28@cluster0.kakvj4a.mongodb.net/")
db = client.test
print(db)

d = {
    "name" : "Shubhangi",
    "email" : "123@gmail.com",
    "surname" : "kumbhar"
}
db1 = client['mongotest1']
coll = db1['test']
coll.insert_one(d)