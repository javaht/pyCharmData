from selenium import webdriver



def jietu():
    option = webdriver.ChromeOptions()
    # option.add_argument("headless")#这个参数是不显示界面
    option.add_argument("incognito")  # 无痕模式
    option.add_argument("disable-plugins")  # 禁用插件
    browser = webdriver.Chrome(options=option)

    browser.maximize_window()

    # 访问百度首页
    browser.get('https://www.baidu.com/')
    # 截图预览
    browser.get_screenshot_as_file('截图.png')

    # 关闭浏览器
    browser.close()
if __name__ == '__main__':
    jietu()