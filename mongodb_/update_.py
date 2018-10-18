import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students
condition = {'age':10}
# result = collection.find_one(condition)
# result['age'] = 19;

print(collection.update(condition,{"age":18})) # 直接更新就行，但是一次貌似只更新一条,执行的替换
#{'n': 1, 'nModified': 0, 'ok': 1.0, 'updatedExisting': True}  ok 执行成功  noModified   影响的条数
# for result in collection.find({'age':{"$gt":17}}):
#     print(result)
print(collection.update(condition,{'$set':{"age":16}}))  # $set 执行的是asign
# $set 只更新result中存在的字段，原来还有其他的话，不更新也不删除； 否则整个重写了就

result = collection.update_one(condition,{"$set":{'age':11}})  # 推荐的方法，并且只支持$这种写法
print(result,result.matched_count)
result = collection.update_many(condition,{"$set":{'age':12}})
print(result,result.matched_count,result.modified_count)

result = collection.update_one(condition,{"$inc":{'age':1}}) #符合条件的age +1

for result in collection.find({'age':{"$gt":0}}):
    print(result)