import urllib.request

# urllib.request.Request(url,data =None,headers={},origin_req_host=None,urverifiable = False,method = None)

request = urllib.request.Request('http://pathon.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
