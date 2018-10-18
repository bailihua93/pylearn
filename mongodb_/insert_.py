import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)   # 直接 client =

db = client.test
collection = db.students

student1 = {
    "id": "20170701",
    "name": "白",
    "age": 28,
    "gender": "male"
}
student2 = {
    "id": "20110203",
    "name": "网",
    "age": 19,
    "gender": 'famale'
}
# 插入一条
result1 = collection.insert(student1)  # 添加一个元素 直接返回id； 5bc7457cc099391b0d91ebcc
student1["id"] = "hei"  # 不能缓解一次插入两个相同对象的错误
result2 = collection.insert([student1,student2]) # 插入同一个对象的时候,某个字段重复导致的BulkWriteError
#  [ObjectId('5bc74598c099391b27167f3a'), ObjectId('5bc74598c099391b27167f3b')]


# 不推荐直接insert了但是还能用
result3 = collection.insert_one(student1)  # <pymongo.results.InsertOneResult object at 0x7f1400afaa08>
print(result3.inserted_id)  # 5bc74665c099391c0c51f135
print(result3)

result4 = collection.insert_many([student1, student2]) #<pymongo.results.InsertManyResult object at 0x7fecce0f4a48>
print(result4)
