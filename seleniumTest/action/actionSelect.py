from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By

def select():
    url = "C:/Users/Administrator/Downloads/aaa.html"

    browser = webdriver.Chrome()

    browser.get(url)
    time.sleep(2)

    # 根据索引选择
    Select(browser.find_element("帅哥")).select_by_index("2")
    time.sleep(2)
    # 根据value值选择
    Select(browser.find_element_by_name("帅哥")).select_by_value("草儿")
    time.sleep(2)
    # 根据文本值选择
    Select(browser.find_element_by_name("帅哥")).select_by_visible_text("才哥")
    time.sleep(2)

    # 关闭浏览器
    browser.close()

if __name__ == '__main__':
    select()