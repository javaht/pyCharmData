import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def getAttrbute():
    option = webdriver.ChromeOptions()
    # option.add_argument("headless")#这个参数是不显示界面
    option.add_argument("incognito")  # 无痕模式
    option.add_argument("disable-plugins")  # 禁用插件
    browser = webdriver.Chrome(options=option)
    browser.maximize_window()
    browser.get("https://www.baidu.com")

    # logo = browser.find_element(By.CLASS_NAME,'index-logo-src')
    # print(logo)
    # print(logo.get_attribute('src'))

    # logo = browser.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/ul[1]/li[3]/a[1]")
    # print(logo.text)
    # print(logo.get_attribute('href'))

    logo = browser.find_element(By.CLASS_NAME,'index-logo-src')
    print(logo.id)
    print(logo.location)
    print(logo.tag_name)
    print(logo.size)



if __name__ == '__main__':
    getAttrbute()

