# coding:utf-8

import requests

# from selenium import webdriver
# browser = webdriver.Chrome()

import aiohttp
import pyquery
import lxml
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>hello</p>', 'lxml')
print(soup.p.string)


