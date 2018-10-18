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
