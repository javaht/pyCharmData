import time
from selenium import webdriver


def size():
    option = webdriver.ChromeOptions()
    # option.add_argument("headless")#这个参数是不显示界面
    option.add_argument("incognito")  # 无痕模式
    option.add_argument("disable-plugins")  # 禁用插件
    browser = webdriver.Chrome(options=option)

    # 设置浏览器大小：全屏
    browser.maximize_window()
    browser.get('https://www.baidu.com')
    time.sleep(2)

    # 设置分辨率 500*500
    browser.set_window_size(500, 500)
    time.sleep(2)

    # 设置分辨率 1000*800
    browser.set_window_size(1000, 800)
    time.sleep(2)


    # 关闭浏览器
    browser.close()
if __name__ == '__main__':
    size()