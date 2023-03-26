from selenium import webdriver
import time

def upOrBack():
    browser = webdriver.Chrome()
    # 设置浏览器全屏
    browser.maximize_window()
    browser.get('https://www.baidu.com')
    time.sleep(2)

    # 打开淘宝页面
    browser.get('https://www.taobao.com')
    time.sleep(2)

    # 后退到百度页面
    browser.back()
    time.sleep(2)

    # 前进的淘宝页面
    browser.forward()
    time.sleep(2)

    # 关闭浏览器
    browser.close()

if __name__ == '__main__':
    upOrBack()