# coding 'utf-8'

import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.zhihu.com')
for item in cookie:
    print(item.name, "  ", item.value)

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.zhihu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

filename = 'cookie2.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.zhihu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

cookie3 = http.cookiejar.LWPCookieJar()
cookie3.load('cookie2.txt', ignore_expires=True, ignore_discard=True)
print(cookie3)
handler = urllib.request.HTTPCookieProcessor(cookie3)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.zhihu.com')
print(response.read().decode('utf-8'))
