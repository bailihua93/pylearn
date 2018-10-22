from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
try:
    browser.get('https://www.taobao.com')
    input = browser.find_element_by_id('q')
    input.send_keys('iPhone')
    input.send_keys(Keys.ENTER)  # 回车，然后input就不见了，会导致报错
    time.sleep(4)
    input.clear()  # 清除内容
    input.send_keys('小米')
    button = browser.find_element_by_class_name('btn-search')
    button.click()  # 点击事件




except  BaseException as e:
    print(e)
finally:
    browser.close()
    # pass
