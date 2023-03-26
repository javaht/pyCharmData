from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def sendKey():
    browser = webdriver.Chrome()
    browser.get(r'https://www.baidu.com')
    time.sleep(2)

    # 定位搜索框
    # input = browser.find_element(By.CLASS_NAME,'s_ipt')
    # # 输入python
    # input.send_keys('python')
    # time.sleep(2)

    # 选中新闻按钮 点击
    # click = browser.find_element(By.LINK_TEXT,'新闻')
    # click.click()
    # time.sleep(2)

    #清除python
    # input = browser.find_element(By.CLASS_NAME,'s_ipt')
    # input.send_keys('python')
    # time.sleep(2)
    # input.clear()
    # time.sleep(2)

    #回车确认
    input = browser.find_element(By.CLASS_NAME,'s_ipt')
    # 输入python
    input.send_keys('python')
    time.sleep(2)
    input.submit()
    time.sleep(5)


    # 关闭浏览器
    browser.close()

if __name__ == '__main__':
    sendKey()