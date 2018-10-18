import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)  # 直接 client =

db = client.test
collection = db.students

# 查找一条数据
result = collection.find_one({'name': '白'})  # 查找出1条
#  {'_id': ObjectId('5bc743a5c09939184addef8d'), 'id': '20170701', 'name': '白', 'age': 20, 'gender': 'male'}
# 想要通过_id查找的话
from bson.objectid import ObjectId

result = collection.find_one({"_id": ObjectId('5bc743a5c09939184addef8d')}) #没有结果的话返回None
#  {'_id': ObjectId('5bc743a5c09939184addef8d'), 'id': '20170701', 'name': '白', 'age': 20, 'gender': 'male'}


# 查找多条数据
results = collection.find({'name': '网'})
for result in results:
    pass
    # print(result)
# {'_id': ObjectId('5bc744ddc0993919ec8218e3'), 'id': '20110203', 'name': '网', 'age': 19, 'gender': 'famale'}
# {'_id': ObjectId('5bc744e2c0993919f7fca34d'), 'id': '20110203', 'name': '网', 'age': 19, 'gender': 'famale'}


# 查找年龄大于多少
for result in collection.find({'age': {'$in': [18,19]}}):
    print(result)

