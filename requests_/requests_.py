import requests

# r = requests.get('http://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# # print(r.text)
# print(r.cookies)
#
# data = {
#     'name': 'germey',
#     'age': 18
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)
# print(r.content)  #二进制数据，英语字符是字符  \n 这些是
# print(r.json())
# print(type(r.json()))




# 文件读写
# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
#
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

# header
from flask.signals import request_started

from commen.header import headers

# r = requests.get('https://www.zhihu.com/explore')
# print(r.text)

# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# if not r.status_code == requests.codes.ok:
#     print('erroe')
# else:
#     # with   open('cookies.conf', 'wb') as  f:
#     # f.write(r.cookies) #这里有问题
#     print('request success')

# cookies
# 直接在header里面添加cookie字符串
# 用RequestsCookieJar()
# cookies = ''
# jar = requests.cookies.RequestsCookieJar()
# for cookie in cookies.split(';'):
#     key, value = cookie.split("=", 1)
#     jar.set(key, value)
#
# r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)


# SSL证书验证

# requests 发送请求的时候，会检查SSL证书，我们可以用verify参数控制是否检查此证书
# response = requests.get('https://www.12306.cn', verify=False)  # 12306的坑
#
# print(response.status_code)


# 代理
# pip3 install 'requests[socks]'

# proxies = {
#     'http': 'http://user:password@10.10.1.10:3128'
# }
#
# requests.get('https://www.taobao.com', proxies=proxies)
#
# proxies  = {
#     'http':'socks5://user:password@host:port',
#     'https':'socks5://user:password@host:port'
# }
# requests.get('https://www.taobao.com',proxies = proxies)


# 超时设定

requests.get('https://www.baidu.com',
             timeout=1)  # 默认是None 也就是会一直等待；  timeout是 链接和读取的综合想要分别设置的话传入元祖  timeout = (5,11,30)

# auth
from requests_oauthlib import OAuth1 #  https://requests-oauthlib .readthedocs.org

# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth=auth)
