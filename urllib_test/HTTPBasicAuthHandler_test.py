# coding:utf-8
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http:www.Baidu.com'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)
print(opener)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
except URLError as e:
    print(e.reason)
