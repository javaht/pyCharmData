from selenium import webdriver

def pagebasic():
    browser = webdriver.Chrome()
    browser.get(r'https://www.baidu.com')

    # 网页标题
    print(browser.title)
    # 当前网址
    print(browser.current_url)
    # 浏览器名称
    print(browser.name)
    # 网页源码
    print(browser.page_source)
if __name__ == '__main__':
    pagebasic()