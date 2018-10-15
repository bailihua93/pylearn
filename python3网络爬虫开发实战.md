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
import


