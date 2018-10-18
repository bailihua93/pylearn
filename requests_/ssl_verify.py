import requests
import logging

logging.captureWarnings(True) #用日志捕获

print(logging)
# from requests import urllib3
#
# urllib3.disable_warnings()  # 用来屏蔽警告
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# 处理警告的方式

# 1. 引入urllib3屏蔽警告
# from requests import urllib3
# urllib3.disable_warnings()  # 用来屏蔽警告


# 2.
