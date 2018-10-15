# coding:utf-8


import urllib.request
import urllib.parse
import urllib.error
import socket

response = urllib.request.urlopen('http://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')  # 转化为字节流
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print(e)
        print(e.reason)
        print(socket.timeout)
        print('timeout')

