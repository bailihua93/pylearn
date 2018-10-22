from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.PhantomJS()
# browser = webdriver.Chrome()

try:
    browser.get("https://www.taobao.com")
    search1 = browser.find_element_by_id('q')
    search2 = browser.find_element_by_name('q')
    search4 = browser.find_element_by_tag_name("a")
    search4 = browser.find_element_by_class_name("search-combobox-input")
    search3 = browser.find_element_by_css_selector("#q")  #css选择起
    search5 = browser.find_element_by_xpath('//*[@id="q"]') #xpath 要看安康
    search6 = browser.find_element_by_link_text("聚划算")  #a标签内部内容
    search7 = browser.find_element_by_partial_link_text("猫") # <a>天猫</a>
    print(search7.text)
    """
    #find_element 是上面的所有的基 方法
    """
    search1 = browser.find_element(By.ID,'q') # 等价与find_element_by_id
    """
    加s后得到的就是一个列表了
    + find_elements_by_id
    + find_elements_by_name
    + find_elements_by_class
    + find_elements_by_tag_name
    + find_elements_by_css_selector
    + find_elements_by_xpath
    + find_elements(By.Qeuery,'attr')
    """
except BaseException as e:
    print(e)
finally:
    browser.close()
