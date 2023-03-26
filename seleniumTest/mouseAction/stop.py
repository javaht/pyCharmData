from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def move_to_element():
    browser = webdriver.Chrome()
    url = 'https://www.baidu.com'
    browser.get(url)
    time.sleep(2)

    # 定位悬停的位置
    move = browser.find_element(By.CSS_SELECTOR,"body > div:nth-child(5) > div:nth-child(2) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1) > span:nth-child(4)")

    # 悬停操作
    ActionChains(browser).move_to_element(move).perform()
    time.sleep(5)

    # 关闭浏览器
    browser.close()


if __name__ == '__main__':
    move_to_element()

