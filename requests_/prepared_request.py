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
