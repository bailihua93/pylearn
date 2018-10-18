import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)   # 直接 client =

db = client.test
collection = db.students
