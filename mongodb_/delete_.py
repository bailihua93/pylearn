import pymongo
c =pymongo.MongoClient('mongodb://localhost:27017')
d = c.test
collection = d.students
result   = collection.delete_one({"age":12})
count = result.deleted_count #1

find_one_and_delete()
find_one_and_repalce()
find_one_and_update()


对索引操作
create_index()
create_indexes()
drop_index()