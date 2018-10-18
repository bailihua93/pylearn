# coding:utf-8
from urllib.parse import urlparse, urlunparse, parse_qs, parse_qsl,urlencode,quote,unquote

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# # print(type(result), result)

#
# print(urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=True))
# print(urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False))
print(result[0])
print(result.scheme)

# print(urlunparse({'scheme': 'http', 'netloc': 'www.baidu.com'}))
# print(urljoin('www.baidu.com', '?name=100', allow_fragments=True))
print(parse_qs('http://www.baidu.com/index.html;user?id=5&name=100#comment'))
print(parse_qsl('id=5&name=100#comment'))

c = urlencode({'name':'中国'})
print(c)
print(unquote(c))
print(quote('中国'))
