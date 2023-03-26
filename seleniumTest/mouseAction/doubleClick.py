from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def double():
    browser = webdriver.Chrome()
    browser.get(r'https://www.baidu.com')
    browser.maximize_window()
    time.sleep(2)
    # 定位到要双击的元素
    double_click = browser.find_element(By.CSS_SELECTOR,"body > div:nth-child(5) > div:nth-child(2) > div:nth-child(7) > div:nth-child(1) > p:nth-child(9)")
    # 双击
    ActionChains(browser).double_click(double_click).perform()
    time.sleep(15)

    # 关闭浏览器
    browser.close()


if __name__ == '__main__':
    double()