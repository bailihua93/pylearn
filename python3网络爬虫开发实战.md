




### 基础环境配置


+ tesserocr  识别图形验证码   
   -  debian 
    ```
    sudo apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev   安装
    git clone https://github.com/tesseract-ocr/tessdata.git   安装语言包
    sudo mv tessdata/* /usr/share/tesseract/tessdata
    
    pip3 install tesserocr pillow
    ```
   
   -  centos   yum install -y tesseract
   
   
+ msyql
sudo apt-get install -y mysql-server mysql-clinet   

sudo service  mysql start
sudo service  mysql stop
sudo service mysql restart 


sudo mysql -uroot -p 修改用户密码  

:q

+ mongo

sud口 apt-key
开发环境 配直

sudo apt-get install mongodb  

service mongodb start
service mongodb stop     

mongod --port 27017 --dbpath /data/db


链接: mongo --port 27017
创建用户
db.createUser({user:'admin',pwd:'admin123',roles:[{role:'root',db:'admin'}]})

admin
admin123



- 修改配置文件  
vim /etc/mongodb.conf

```conf
bind_ip = 0.0.0.0



noauth = true
auth = true
```


+ redis  
sudo apt-get -y install redis-server

redis-cli 进入


sudo  vim /etc/redis/redis.conf
```angular2html
注释：  bind:127.0.0.1
取消  requirepass foobared  这里是添加密码，默认的是  foobared 可以该
 ```

sudo /etc/init.d/redis-server  restart  重启
sudo /etc/init.d/redis-server  start  开始


+ charles  
/usr/bin/charles/bin/charles 启动


+ docker

$ sudo apt install docker.io
$ sudo systemctl start docker
$ sudo systemctl enable docker
查看是否安装成功

$ docker -v
Docker version 17.12.1-ce, build 7390fc6


###爬虫原理   
url（同意资源定位符）是uri（统一资源标识符）的子集

uri的另一个子集 urn 命名资源的名称



## 基本库的使用  



###urllib
#### urllib.request.Request
urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
+ url
+ data 必须传字节流  bytes(urllib.parse.urlencode({})) 
+ headers  字典，可以直接构造，也可以调用  实例的 add_header()
+ origin_req_host 请求方的host名称或者ip地址
+ unverifiable 请求无法验证，默认False； 例如：请求图片的时候，没有权限，这时unverifiable值为true
+ method   'GET' 'POST' 'PUT'
```python
#urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# coding:utf-8
import urllib.request
import urllib.parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

```



#### urllib.parse


1. urllib.parse.urlparse(url,scheme,allow_fragments)
* scheme://netloc/path ;params?query#fragment

+ url
+ scheme 如果url中没有scheme 则将设置的设置为默认值  urlparse(url,scheme='http')
+ allow_fragment  False fragment部分会被忽略，被解析为 path 


+ 结果  result[index]  result['name'] 是一个元组，可以用索引来获取也可以用属性名获取
```python
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')

print(urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=True))
#ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
print(urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False))
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5#comment', fragment='')
```


2. urlunparse([scheme,netloc,path,param,query,comment]) 长度必须是7
3. urlsplit()
返回的param添加在了path中  
通过index或者属性访问
urlunsplit() 出入的数组长度必须是5

4. urljoin(base,url,allow_fragment)
base一url 提供了三项内容 scheme 、 netloc 和 path 。 如果这 3 项在新的链接里不存在，就予以补充；如果新的链接存在，就使用新的链接的部分。
 而 base_url 中的 pa rams 、 query 和 fragment是不起作用的 。

```python
from urllib.parse import urljoin
print(urljoin('www.baidu.com', '?name=100', allow_fragments=True))

```

5. urlencode()  将字典序列化为get请求的参数   {'name':'中国'}  name=%E4%B8%AD%E5%9B%BD 
6. parse_qs()  
```python
from urllib.parse import parse_qs,parse_qsl
print(parse_qs('http://www.baidu.com/index.html;user?id=5&name=100#comment'))
#{'user?id': ['5'], 'name': ['100#comment']}
print(parse_qsl('id=5&name=100#comment'))
# [('id', '5'), ('name', '100#comment')]
```
parse_qsl()   


7. quote()   将内容转化为url编码   urlencode 内部调用了这个应该
8. unquote() 
```python
from urllib.parse import urlencode,quote,unquote
c = urlencode({'name':'中国'})
print(c) # name=%E4%B8%AD%E5%9B%BD
print(unquote(c)) #name=中国
print(quote('中国'))  #%E4%B8%AD%E5%9B%BD
```


###robotparser
```python
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

rp = RobotFileParser()
url = 'https://www.zhihu.com/robots.txt'
rp.set_url(url)
rp.read()
print(rp.can_fetch('*', url))



# 第二种用法
rp = RobotFileParser()
rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))

```









### requsets

#### SSL 认证

+ requsets.get(12306) 抛出 SSSLError 

+ response = requests.get('https://www.12306.cn', verify=False)  解决方法 verify = False 不认证  

+ 出现警告，解决方法
两种
```python
#禁止掉
from requests import urllib3
urllib3.disable_warnings()  # 用来屏蔽警告


#捕获
import logging
logging.captureWarnings(True) #用日志捕获
```

#### 身份认证
1. auth
```python
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
r = requests.get('http://localhost:5000', auth=('username', 'password'))  # 简写，默认的东西
print(r.status_code)

```

2. OAuth1认证

pip3 install  requests_oathlib
```python
import requests
from requests_oauthlib import OAuth1
url= ''
auth = OAuth1('APP_key','App_secret','user_auth_key','user-token_seleted')
requests.get(url,auth)
```

#### 引入兄弟包的方法
各自目录下创建__init_.py
在各自的文件的开头添加  
```python
import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
sys.path.append(parentUrl)
```

#### prepared reuqest
```python
from requests import Request, Session
from commen.header import headers

url = 'http://httpbin.org/post'
data = {
    "name": "germey"
}

s = Session()
req = Request('POST', url, data=data, headers=headers, files=None, params=None, auth=None, cookies=None, hooks=None, json=None)

prepped = s.prepare_request(req)
r = s.send(prepped, timeout=1)
print(r.text)

```

### 正则  

1. 常用规则
-     \w            字母数字下划线
-     \W            非
-     \s            空白符号
-     \S            飞空
-     \d            0~9
-     \D            非数字
-     \A            匹配字符串开头
-     \Z            匹配字符串结尾，如果存在换行，只匹配到换行前的字符串
-     \z            匹配字符串结尾，如果存在换行，匹配到换行符
-     \G            匹配最后匹配完成的位置
-     \n            回车
-     \t            tab
-     ^             一行字符串的开头
-     $             一行字符串的结尾
-     .             任意字符，不直接包含换行符
-     [abc]          abc 中选一个
-     [^abc]        不  在abc中任意个
-     *             > =  0个匹配项
-     +             >=1  个
-     ?             0 或1 非贪婪模式
-     {n}           n个
-     {n,m}         n～m个  贪婪模式
-     a|b           a或者 b
-     ()            括号内的表达式

 
-     .*?       非贪婪模式匹配

2. 修饰符
+ re.I
+ re..L
+ re.M 多行匹配影响^  $
+ re.S 使得 . 包含换行符
3. 转意字符

4. match(pattern,str,re.S) 整个的字符串开头匹配的，用于验证字符串是否满足某个结构

```python
import re

# 从字符串起始位置开始匹配正则，成功返回结果，失败返回None
content = 'hello 1234567 World_this is Regex Demo'
result = re.match('^hello\s(\d+)\s\w{4}(.*?)', content)
print(result)
print(result.group())  # hello 123 4567 Worl    group()返回总的结果
print(result.group(1))  # hello 123 4567 Worl   group(n)返回小括号的结果
print(result.span())

# result = re.match('^hell.*(\d+)\s.*',content)
# print(result.group(1))  # 结果只有7     .*贪婪模式匹配尽量多的字符，

result = re.match('^hel.*?(\d+)\s.*Demo', content)
print(result.group(1))  # 结果只有7     .*非贪婪模式匹配尽量少的字符，后面没有正则的话，当前只匹配最初的匹配方式；
cs = 'abbbb'
result = re.match('ab+', cs)  #abbbb
result = re.match('ab+?', cs)  # ab  非贪婪模式，只会返回最少的匹配
print(result.group())
```
+ 非贪婪模式  
在 + * 等后面加上 ? 返回最少字符的匹配项

+ attributeError 访问不存在的属性  多数是None上访问属性


5. search(patter,str,mode) 返回第一个匹配到的内容

















## 数据存储

### mongo


#### 插入
```python
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)   # 直接 client  = pymongo.MongoClient('mongodb://localhost:27017') 链接数据库
db = client.test  # 指定库
collection = db.students  # 指定表   
# insert(dict|list) insert_one insert_many  插入文件

student1 = {
    "id": "20170701",
    "name": "白",
    "age": 20,
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

```

#### 查找
1. 方法
collection.find  collection.find_one      
```python
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
print(collection.find_one({'age': {'$gt': 20}}))

```

2. 比较符号

+  $lt    {'age': {'$lt': 20}}   little than小于
+  $gt    {'age': {'$gt': 20}}   great than大于
+  $lte                          little than equeal  小于等于
+  $gte                           大于等于
+  $ne                           not equel  不等于
+  in    {'age':{"$in":[20,23]}    在范围内  包含边界 
+  nin              


3.高级属性
+ $regex   正则　　　　　　　　　　　　   colletion.find(｛"name":{'$regex':'^M.*?'}｝) # 以M开头的  
+ $exists  属性是否存在　　　　　　　　   colletion.find({"name":{'$exists':False}})  # name属性不存在的
+ $type  类型判断　　　　　　　　　　　　　　　　　　{"age":{"$type":'int'}　　　
+ $mod   数字摸操作　　　　　　　　　　　　　　　　　{"age":{"$mod":[5,0]}  年龄模５余０
+ $text  文本查询　　　　　　　　　　　　　{"$text":{"$search":"Mike"}} 属性中含有　Ｍｉｋｅ的
+ $where  高级条件查询                 {"$where":'obj.fans_count==obj.follows_count'} 自身粉丝数等于关注数

4. 计数 

collection.find().count() 返回条数

5. 排序   
collection.find().sort('name',pymongo.ASCENDING) 生序     pymongo.DESENDING


6. 偏移     
find().skip(2)        跳过两个元素，直接访问第三个
7. 限制    
find().limit(5)   结果只有5条



 


#### 更新

```python

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
```

#### 删除
```python
import pymongo
c =pymongo.MongoClient('mongodb://localhost:27017')
d = c.test
collection = d.students
result   = collection.delete_one({"age":12})
count = result.deleted_count #1


```

#### 直接操作
find_one_and_delete()
find_one_and_repalce()
find_one_and_update()


对索引操作
create_index()
create_indexes()
drop_index()