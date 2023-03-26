from selenium import webdriver
import time

def refresh():
    browser = webdriver.Chrome()

    # 设置浏览器全屏
    browser.maximize_window()
    browser.get(r'https://www.baidu.com')
    time.sleep(2)

    try:
        # 刷新页面
        browser.refresh()
        print('刷新页面')
    except Exception as e:
        print('刷新失败')

    # 关闭浏览器
    browser.close()

if __name__ == '__main__':
    refresh()