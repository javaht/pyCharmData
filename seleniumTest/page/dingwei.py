import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
    # 3.下边是八种元素定位
def location():
    option = webdriver.ChromeOptions()
    option.add_argument("incognito")  # 无痕模式
    option.add_argument("disable-plugins")  # 禁用插件
    browser = webdriver.Chrome(options=option)
    browser.maximize_window()
    browser.get("https://www.baidu.com")
    browser.find_element(By.ID,'kw').send_keys("python")
    # browser.find_element(By.NAME,'wd').send_keys('孙小船')
    # browser.find_element(By.CLASS_NAME,'s_ipt').send_keys('哈哈哈哈')
    # browser.find_element(By.TAG_NAME,'input').send_keys('python')  #通过tag  也就是input标签定位
    # browser.find_element(By.LINK_TEXT,"贴吧").click()
    # browser.find_element(By.PARTIAL_LINK_TEXT,"贴").click()  #模糊查询
    # browser.find_element(By.XPATH,"//input[@id='kw']").send_keys("贴吧")
    # browser.find_element(By.CSS_SELECTOR,"#kw").send_keys("5666")
    time.sleep(5)

if __name__ == '__main__':
    location()