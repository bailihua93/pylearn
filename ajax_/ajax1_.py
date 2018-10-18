# https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1076032830678474&page=2
# http://m.weibo.cn/api/container/getIndextype=uid&value=2830678474&containerid=1076032830678474&page=2
from urllib.parse import urlencode

import requests

from pyquery import PyQuery as jq

baseurl = "https://m.weibo.cn/api/container/getIndex"
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'm.weibo.cn'
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = baseurl + "?" + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print(e.reason)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            
            pass