import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
r = requests.get('http://localhost:5000', auth=('username', 'password'))  # 简写，默认的东西
print(r.status_code)

from requests_oauthlib import OAuth1
url= ''
auth = OAuth1('APP_key','App_secret','user_auth_key','user-token_seleted')
requests.get(url,auth)