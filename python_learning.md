### print
```py
print('a',end='') #end指定输出后会跟什么，默认是\n
print('b',end='\n')

#print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
print('The quick brown fox', 'jumps over', 'the lazy dog')
#print()会依次打印每个字符串，遇到逗号“,”会输出一个空格，因此，输出的字符串是这样拼起来
```
### input
c = input('请输出内容，然后会被赋值给c')
### 数字
py  有三种数字类型   整数 浮点   复数    2  2.0 2+3j
```python
print(type('cc'))
print(type(1))
print(type(1.1))
print(type(1+2j))
#<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'complex'>
```




### 赋值操作
x, y, z = 1, 2, 3
e= f= g = 10
x, y = y,x  交换操作







### 运算符
没有 ++ --
```py
+  加
-  减
* 
**  幂运算    2**3   == 8
/   除法      8/6  ==  1.6666666  
//  取整除法    5//3 == 1   留下整数商
%   取余数      5%3 == 2
<<  左移       *2**位数
>>  右移       /2***位数
&   按位与
|   按位或
^   异或
~   取反
<   
>
>= 
<=
==         字符串相同的时候相等
!=    
not       非   返回布尔值
and     短路与  返回项
or     短路或   返回项
```



### 控制语句

没有switch
boolean值只有 True False 区分大小写
#### if
```py 
number = 23
guess = int(input("enter a number"))
if guess == number:
    print('cagralations')
elif guess > number:
    print("small")
else:
    print("bigger")
```

#### while

```py
number = 23
running = True
while running:
    guess = int(input('请输入猜的数字'))
    if guess == number:
        running = False
        print("猜对了")
    elif guess > number:
        print("大了")
    else:
        print('小了')
        break
else:
    print('跳出循环')
```

while中可以用break；可以在后面加个else；行为类似判断语句的else，但是break跳出的话，后面的else不会执行
#### range([start],end[,step])
生成的东西是range ；只能被for in  
或者   list(range(10)) 转化为数组


#### random 
```python
import random
print(random.random())  # 生成0-1之间的数字
print(random.randint(0,5))  # 生成 0- 5包含 0 5 的 整数
```
 
#### for循环
for in 遍历可遍历的  数组 ，range ，对象
for in  遍历数组返回项，遍历对象返回key  
```python
for i  in [1,2,3,4]:
    print(i) # 1 2 3 4
    
for i in range(1, 5):  # range 包头不包尾
    print(i)   # 1 2 3 4
    if i == 5:
        print(i)
    # break
else:
    print(i + "else")
print(i)
```

**所有的控制语句之后必须跟着一定的操作**


#### break

#### continue

### 函数
def 定义  冒号定义行结尾
```py
def sayHello(a,b):
    print('hello')
```
#### 局部变量
函数内部声明的变量是局部变量；
内部可以访问外部的变量但是，不能存在同名的变量;
不能修改外部的变量，因为会出现undefined或者只在局部有效
```py
a = 10
def sayHello():
    # a = a
    b = a
    # a = b+1
    print(a)
```

##### 使用global语句获取全局变量
通过global函数可以把全局变量引入函数中，并且会一直存在函数中，修改的话也是修改的全局变量
```py
a = 5
def sayHello():
   global a
   print(a)  #5
   a=10
   print(a)  # 10
   a+=10
   print(a)  #20

sayHello()
print(a)   # 20
```

##### nonlocal语句 函数中的函数调用的
```js
def outer():
    x = 20
    print(x)       #20
    def inner():
        nonlocal x   
        x = 10
        print(x)  #10
    inner()
    print(x)     #10
outer()
```


##### 函数形参默认值  （只有写在后面的有效，并且必须按照一定的顺序来写）
```py
def say(name, a="hello",b='ha'):
   print(name,a,b)

say("hi")  #hi hello ha
say('hi','body')  # hi  body ha
asy('hi',b='haha') # hi hello haha   这里指定参数名话，后面部分有些不赋值也行了
```

#### 可变参数
```py
def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
        print(number)
    for key in keywords:
        count += keywords[key]
        print(key)
    return count


# print(total(10, 1, 1, hai=100, 2, 3, hello=10)) 调用的时候纯数字还是在等号参数的前面，这种情况会报错
print(total(10, 1, 1, 100, 2, 3, hello=10))
```

写参数的时候 字面量必须写在 字典前
*param  这个参数点之后的所有实参都会被收集为  tuple  其实是元组
**param  所有用 = 生命的实参会被收集到一个字典 dictionary



定义只能通过关键字赋值的形参的时候，可以先在前面添加一个*的参数
def demo(init =5,*param,vegetables)

这样就只能通过key= 形式来赋值了；并且必须赋值才行



只需要 keyword-only的实参: 不给与参数名字就行
def total(initial=5,*,vegetables)




#### return  
不带返回值的retern 相当于返回 return None;表示返回值不存在
每一个函数都隐式包含return none；



#### DocStrings
文档字符串是一个多行字符串，其中第一行以大写字母开头，并以句号结尾。

接下来的第二行为空行，从第三行开始为详细的描述。

我强烈建议你在你的正规函数中遵循这个编写文档字符串的惯例。
我们可以通过使用函数的__doc__属性(注意双下划线)存取 printMax 的文档字符
串。








### 模块
#### import
引入的时候回自动执行一遍  

入果它不是一个已编译好的模块， 即用 Python 编写的模块， 那么 Python 解释器将从它的
sys.path 变量所提供的目录中进行搜索   
初始化工作只需在我们第一次导入模块时完成

```js
import sys
print("The command line arguments are:")
j = 0
for i in sys.argv:
    j += 1
    print(i)
    print(j)
print('\n\n ', sys.path)

```
+ 脚本名称在 sys.argv 的列表中总会位列第一。 因此， 在这一案
例中我们将会有如下对应关系： 'module_using_sys.py' 对应 sys.argv[0] ， 'we' 对应
sys.argv[1] ， 'are' 对应 sys.argv[2] ， 'arguments' 对应 sys.argv[3]     


+ sys.path  返回当前目录 、兄弟目录的、 py的环境变量

+ os.getcwd()  返回命令行执行的时候的路径

#### .pyc
创建.pyc 加速导入文件

.pyc 文件一般被创建在与其对应的.py 文件所在的相同目录下。如果 python 没有
这个目录的写权限，则.pyc 文件不会被创建。

####  from ... import ...
from sys import argv;
就可以直接用argv  

from math import sqrt
print(sqrt(9))
避免这么用


#### __name__  独立运行的时候最开始的文件
作为独立运行的的程序时候  '__main__'
作为引用的时候 返回文件名   

if __name__ == '__main__'  时是单独运行的，
作为引用运行的时候不是这个值


#### 制作自己的模块

```py
#!usr/bin/python
# Filename: mymodule


def sayHi():
    print('hi')
__version__ = '0.1'
```
将文件放在需要引入的目录
```py
import mymodule
mymodule.sayHi()  # 文件.method()
print(sayhi.__name__)  # 文件名
print(sayhi.__version__)

```
也可以
```python
from mymodule import say_hi, __version__  
# 或者  引入全部方法
from sayhi import *  # 不会引入 __开头的变量
say_hi()
```


#### dir函数  返回一个属性列表
+ 当你为 dir() 函数提供一个模块名，它将返回定义在其中的所有名字。

+ 当 dir()的参数为空时，返回定义在当前模块中所有属性,包含引入的方法和模块名

+ 删除变量   del name  之后该属性就变成不存在了 ，不能访问了

+ dir(str)  返回str类的属性

#### vars()  
返回的就是key:value 的  列表了；
不能针对所有类都有效



#### 包
包仅仅是包含模块的文件夹，并带有一个特殊的文件__init__.py 用于指示 pytho
这个文件夹是特殊的，因为它包含 python 模块。



### 数据结构 


#### int  
数字+字符串不能直接相加  需要       18+int('2') 强制转化
#### float

#### 字符串          Unicode编码的
+ 转成Ascii      Str.encode('ascii')   
  调用encode之后产生了一个bytes对象

+ 字符串对象    
  -  单引号
  -  双引号
  -  三引号  可以使用换行
+ 转义字符  
   \'    \\     \n 换行   \t
+  取消转义  在字符串前面加上  r或者 R   ；   r"new lines are indicated by n"
+  写正则的时候可以用r
+ 注意： 单行字符串末尾  使用  \ 并且换行的话，会自动连接在一起
+ 同一行的两个相邻的字符串会被自动合并到一起  'a'  'b' 变成了  ab

+  format()
  ```py
  age = 35
  name = 'bai'
  hello  = '{}  is {} old'.format(name, age); 注意函数中逗号后面有一个空格
  hello  = '{0}  is {1} old'.format(name, age); 注意函数中逗号后面有一个空格
  
  info = "姓名：%s \n年龄：%d \n分数：%f" % ("老王", 18,100.1)
  ```
  也可以直接 
  ```py
  hello = name + 'is" + age + "old";
  ```

  高级用法
  '{0:.3}'.format(1/3)   小数点后保留3位   0.333

  '{0:_^11}'.format('hello')  下划线填充到11位长，hello在中间

  '{name} wrote '.format(name="bai")    # 这里等号两边没有空格

+ str.startswith('str')  是否以开头，返回boolean


+  find                  === indexof
+  in
+   join
```py
str = "abcdefghijklmhnopqrstuvw"
print(str.startswith('e'))  # str.startswith('str)  boolea
print('ab' in str)     # 字符串是否字符串中
print(str.find('hi'))  # 找到h的index ，不存在的话返回-1


arr = ['a', 'b']
arr = "_".join(arr)      # a_b
arr = '_'.join("Aca")    # 列表添加join与其他语言不同,并且字符串也支持join ： A_c_a
print(arr)

```
+ upper()
+ lower()
+ replace('a',"b") a替换为b

+ 一般不写 ； 写 ；也可以表示是结尾


####bool
<class 'bool'>  
bool的值为：True | False，注意首字母都要大写。
**在python中0,、空字符、空列表[]、空元祖()、空字典都等于False。**
#### 列表  [1,2,3,4,5,6]

```py
#! /usr/bin/python
# Filename: list.py
shoplist = ['apple', 'egg', 'cattot']
print(len(shoplist))       # len 获取长度
for item in shoplist:      # for in 循环项目
    print(item, end='')    # end = ''结尾是为了不换行
shoplist.append('rice')    # append 添加元素
shoplist.sort()            # sort()
print(shoplist)            # ['apple', 'cattot', 'egg', 'rice']
print(shoplist[0])         # apple
olditem = shoplist[0]      # 看起来是值传递
del shoplist[0]            # 删除对应项
print(shoplist)            # ['cattot', 'egg', 'rice']
print(olditem)             # app
[].index(ele)              # [].index(ele)
[].remove(ele)
```

*  列表解析
用于先有列表派生新列表 filter+map操作

你想让其中所有大于 2 的元素乘以 2 并组成一个新的列表。
```py
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]   # [6, 8]
```

#### 元组（不可修改的列表） tuple
```py
#!/usr/bin/python
# Filename: using_tuple.py    逗号分隔，小括号闭合
zoo = ('python', 'elephant', 'penguin')   # 注意小括号是可选的
print(len(zoo))  # len  3                                
new_zoo = ('monkey', 'camel', zoo)       # ('monkey', 'camel', ('python', 'elephant', 'penguin')
print(len(new_zoo))                      # len  3
print(new_zoo[2])                        # ('python', 'elephant', 'penguin')
print(new_zoo[2][2])                     # penguin
```
有0个元素的元组   number =()
有一个元素的元组   number = (1,)   写下逗号



#### 序列   Sequence
列表  元组  字符串  都是序列的例子

序列主要特点是支持成员的从属测试（in 和not in）和支持索引操作


序列的下标为负值的时候  length-该值 得到内容


**切片操作, 包前不包后** 
```python
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# Indexing or 'Subscription' operation
print('Item 0 is', shoplist[0])     #apple
print('Item -1 is', shoplist[-1])   #banana
print('Character 0 is', name[0])    # s

# Slicing on a list
print('Item 1 to 3 is', shoplist[1:3])      #['mango','carrot']
print('Item 2 to end is', shoplist[2:-2])   # []
print('Item 1 to -1 is', shoplist[1:-1])    # ['mango','carrot']
print('Item start to end is', shoplist[:])  # 没有指定任何值的时候是输出全部
# Slicing on a string
print('characters 1 to 3 is', name[1:3])    # ’wa'      字符串直接返回字符串
print('characters 2 to end is', name[2:])   # 没有指定后面的时候 到末尾


# 指定步长
shoplist[::2] #步长是2  next- now = 2
shoplist[::-2]   #反向从末尾开始，隔一个取一个
def reverse(text):
  return text[::-1]  #reverse实现
```
### 字典  dictionary
key value的键值对，类似于json ; 键是不可变的对象（字符串等）；值是任意的
```py
#!/usr/bin/python
# Filename: using_dict.py
ab = {'Swaroop': 'swaroop@swaroopch.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }
print(ab['Swaroop'])                      # 访问  ab['key']


del ab['Spammer']                          # 删除一个键值对

print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))
# There are 3 contacts in the address-book


# 遍历  指定两个值得时候自动是 key + value    # 遍历
for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))


# 添加一个键值对
ab['Guido'] = 'guido@python.org'


if 'Guido' in ab:  # OR ab.has_key('Guido')     in   类似于indexof
    print("\nGuido's address is", ab['Guido'])
```


###集合   set     无序集合
集合是简单对象的无序集合，适合**关心元素是否存在**在集合中而不是顺序和次数

**测试从属关系**  
**寻找两个集合的交集**

```py
bri = set(['hello', 'haosdaf', 'haoda'])
strset = set('hello')
print(strset)           # {'h', 'o', 'e', 'l'}
print('ha'in bri)       # False
print('hello' in bri)   # True
brc = bri.copy()        # clone
brc.add('haha')         # 添加元素  add   序列是 append、
print(brc.issuperset(bri))  # a.issuperset(b) 是父集
bri.remove('hello')      # 删除  remove
print(bri & brc)  # 并集   #   & 求交集
```


### 地址引用  

**列表 是 地址引用  []**

**clone的方法    通过切片 b = a[:]**


### 字符串
```js
str = "abcdefghijklmhnopqrstuvw"
print(str.startswith('e'))  # str.startswith('str)  boolea
print('ab' in str)     # 字符串是否字符串中
print(str.find('hi'))  # 找到h的index ，不存在的话返回-1


arr = ['a', 'b']
arr = "_".join(arr)      # a_b
arr = '_'.join("Aca")    # 列表添加join与其他语言不同,并且字符串也支持join ： A_c_a
print(arr)
```

str(object)  返回字符串


### 解决问题



###面向对象
class 封装 

#### 类中的方法 
+ self 类方法必须有一个额外的形参，必须处于第一形参位置，py自调用，每个函数在定义的时候都得写；可以直接用self  类似于 this
+ __init__  构造函数
+ __del__    del或者 指针指向别处的时候调用
+ 类变量  Peopel.population   全局的 静态变量，从任何地方都能访问到 。  也可以通过 self.__class__.population 访问
+ 静态方法    @classmethod  # 类方法， cls 表示当前的类       People.fn staticmethod将一个方法转化为静态方法，并且会返回改方法，用赋值语句的话得到的是同一个对象

```python
class Robot:
    # 一个类变量， 用来计数机器人的数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))
        # 当有人被创建时， 机器人
        # 将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了。 """
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候
        没问题， 你做得到。 """
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod  # 类方法， cls 表示当前的类
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

```
**静态不静态是一样的**
```python
class Hi:
    def hi():
        print('hi')

Hi.hi()
```

#### 继承  多态



```python
#!/usr/bin/python
# Filename: inherit.py


class SchoolMember:
    '''Represents any school member.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {0})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{0}" Age:"{1}"'.format(self.name, self.age), end="")


class Teacher(SchoolMember):      # 类后面跟一个包含基类名称的元组#括号里面写出父类

    '''Represents a teacher.'''

    def __init__(self, name, age, salary):

        SchoolMember.__init__(self, name, age)    #调用父类的init,注意传入了self
        self.salary = salary
        print('(Initialized Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)    # 调用了父类的方法，导致内容拼接了
        print('Salary: "{0:d}"'.format(self.salary))


class Student(SchoolMember):

    '''Represents a student.'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{0:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
print()  # 打印一个空行

for member in [t, s]:
    member.tell()         #多态调用的是子类的方法
 


c = {
    'name': "bai",
    "age": 20
}
SchoolMember.tell(c)  # 传入值就是self了，只有对象有 . 操作
```

(Initialized SchoolMember: Mrs. Shrividya)75 / 99
(Initialized Teacher: Mrs. Shrividya)
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)
Name:"Mrs. Shrividya" Age:"40" Salary: "30000"
Name:"Swaroop" Age:"25" Marks: "75



* 只有对象有 .  操作  
* 类名.fn()   传入参数会自东转化为self和其他的，没卵用的设计 




### 输入输出 

#### 终端

+ ar something = input("Enter text")   # Enter text 然后让输入，输入的内容被保存在something中

+ print("输出")

#### 文件
+ open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
  - mode  打开模式可以为读模式('r')，写模式('w')或追加模式('a')。
          另外我们也可以处理文本文件('t')和二进制文件('b')。   读取mp3  'rb' ; 读取txt  'rt'
          默认的 open 将文件对待为文本文件't'，并以读模式'r'打开。
  - buffering    0 无缓冲直接将数据写到硬盘上      
                 1 有缓冲，先写到内存，只有使用flush或者close函数才会将数据更新到硬盘       
                 大于1   缓冲区大小
                 -1或任何负数    使用默认缓冲区大小
  - encoding = "utf-8"               
             

+ write(str)
并调用 close 将其关闭。

+  读取
   -  readline()  readline 方法读取文件的每一行,返回一整行文本其中包括末尾的换行符。
                   当返回一个空字符串时，意味着我们已经来到文件尾，len(line) == 0
                   空白行也是有 回车符号的
   - f.read()  所有内容读取到内存中 
                          
+   f.close()     最后关闭文件 简化版
```python
with open('./130000.txt','r') as fileReader:
    print(fileReader.read())  #读取全部的
    for line in fileReader: # 等于  while  readline
        print(line)
```
           

```python
#!usr/bin/python
# Filename: file.py
# 多行文本中len返回的是字符长度  换行符虽然没显示，但是仍然是 1个长度
poem = """
Programming is fun
when work is down
if you want make your google
run python
"""      


f = open('hello.txt', "w")
f.write(poem)
f.close()

f = open('./hello.txt')

while True:
    line = f.readline()
    print(len(line))
    if len(line) == 0:
        break
    print(line, end="")
f.close()

```



```python
"""
备份
"""
import os
import time

# 1. 需要备份的文件与目录将被
# 指定在一个列表中。
# 例如在 Windows 下：
# source = ['"C:\\My Documents"', 'C:\\Code']
# 又例如在 Mac OS X 与 Linux 下：
source = ['/Users/swa/notes']
# 在这里要注意到我们必须在字符串中使用双引号
# 用以括起其中包含空格的名称。
# 2. 备份文件必须存储在一个
# 主备份目录中
# 例如在 Windows 下：
# target_dir = 'E:\\Backup'
# 又例如在 Mac OS X 和 Linux 下：
target_dir = '/Users/swa/backup'
# 要记得将这里的目录地址修改至你将使用的路径
# 如果目标目录还不存在， 则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录
# 3. 备份文件将打包压缩成 zip 文件。
# 4. 将当前日期作为主备份目录下的
# 子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')
# 添加一条来自用户的注释以创建
# zip 文件的文件名import os
import time

# 1. 需要备份的文件与目录将被
# 指定在一个列表中。
# 例如在 Windows 下：
# source = ['"C:\\My Documents"', 'C:\\Code']  # 在这里要注意到我们必须在字符串中使用双引号用以括起其中包含空格的名称。
# 又例如在 Mac OS X 与 Linux 下：
source = ['/Users/swa/notes']
#



# 2. 备份文件必须存储在一个
# 主备份目录中
# 例如在 Windows 下：
# target_dir = 'E:\\Backup'
# 又例如在 Mac OS X 和 Linux 下：
target_dir = '/Users/swa/backup'
# 要记得将这里的目录地址修改至你将使用的路径
# 如果目标目录还不存在， 则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

# 3. 备份文件将打包压缩成 zip 文件。
# 4. 将当前日期作为主备份目录下的
# 子目录名称   os.sep window的 \\  linux 的 /
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')
# 添加一条来自用户的注释以创建
# zip 文件的文件名
comment = input('Enter a comment --> ')
# 检查是否有评论键入
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'
# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
print('Successfully created directory', today)
# 5. 我们使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))
# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

```











#### Pickle
将纯python对象存储到文件中
```python
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # 转储对象到文件
f.close()
del shoplist # 销毁 shoplist 变量
# 从文件找回对象
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # 从文件加载对象
print(storedlist)
```


####unicode

阅读或写入某一文件或当我们希望与互联网上的其它计算机通信时， 我们需要将我们的 Unicode 字符串转换至一个能够被发送和接收的格式
```python
# encoding=utf-8
import io
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)
```

###  模块


#### 捕获
try-     except                                 -else
         后面跟着error类型，类似case操作           没有报错的时候执行
```py
try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')    # ctrl+d
except KeyboardInterrupt:
    print('You cancelled the operation.')     #ctrl+c
else:
    print('You entered {0}'.format(text))
```




##### 抛出异常

raise Exception
并且错误可以通过  except   Exception as ex; ex 是抛出的错误
```py

class ShortInputException(Exception):
    '''A user-defined exception class.'''

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input("输入你的名字")
    if len(text) > 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print("hello")
except ShortInputException as ex:   # 自定义的的错误可带信息
    print(ex.length, ex.atleast)
except Exception as ex:
    # 这时 ex  没有任何东西
    print("ex")
else:       
    print("ok")       # 没有报错的时收执行

finally:               # 可选，必定会执行的
    print("finally")
```


try + finally 确保会关闭资源  ： 用with简化

```py
with open("poem.py") as f :
    for line in f:
        print(line,end=")
```
会自动关闭文件


#### sys模块

sys   warning

```py
import sys,warning
sys.version_info    py的版本信息   （3,0,0，‘beta',2)
sys.version_info[0]   3

warning.warn("hello gogo")
```

#### loggin模块
得到存在某处的重要信息或者调试信息，以便检查是否如期运行;将信息存储在某地 


```py
#!/usr/bin/python
# Filename: use_logging.py
import os                #与系统交互
import platform          # 获取平台信息
import logging           # 输出日志文件


if platform.platform().startswith('Windows'):
    print(os.path)      
    # <module 'ntpath' from 'D:\\program\\py\\lib\\ntpath.py'>
    print(os.getenv('HOMEDRIVE'))     # c
    print(os.getenv('HOMEPATH'))      # \Users\Administrator
    logging_file = os.path.join(
        os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
    print(logging_file)
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
```

### 特殊用法

####传递元组

a, b = <某些表达式>的使用，它会将表达式的结果解释为带有两个值的元组;并分别赋值
```py
def get_error_details():
    return (2, 'second error details')
errnum, errstr = get_error_details()
```
快速交换两个变量的值
a,b = b,a


#### 对象 []操作

方法名 解释
__init__(self, ...) 在对象被返回以变的可用前调用
__del__(self) 在对象被销毁前调用
__str__(self) 在使用 print 函数或 str()时调用
__lt__(self, other) 在使用小于运算符时(<)调用。
类似的其它运算符也存在对象的特殊方法(+, >
等)
__getitem__(self, key) 当使用 x[key]索引操作时调用；list也是这么实现的
__len__(self) 当使用内建 len()函数时调用。

#### lambda表达式
创建新函数对象用的；lambda 需要一个参数后跟一个相当于函数体的单表达式，这个表达
式的值将成为函数的返回值。**只能是表达式**



#### exec和eval
exec 函数用于执行 python 语句，不过这些语句储存在字符串或文件中而不是程序自身中。

eval 函数用于执行合法的存储在字符串中的 python 表达式。

#### asset语句
assert 用于断言一个表达式为真。为假的话会触发一个 AsserError并终止程序

#### repr函数
repr 函数用于获得对象的正规字符串表示。有趣的是多数时候 eval(repr(object))
等于 object。




#### whois  buildwith
builtwith.parse('https://zhihu.com')  
whois.whois('diyibanzhu.xyz')
