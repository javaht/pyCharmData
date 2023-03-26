from selenium import webdriver

def cookie():
    browser = webdriver.Chrome()
    # 知乎发现页
    browser.get('https://www.zhihu.com/explore')
    # 获取cookie
    print(f'Cookies的值：{browser.get_cookies()}')
    # 添加cookie
    browser.add_cookie({'name': '才哥', 'value': '帅哥'})
    print(f'添加后Cookies的值：{browser.get_cookies()}')
    # 删除cookie
    browser.delete_all_cookies()
    print(f'删除后Cookies的值：{browser.get_cookies()}')


if __name__ == '__main__':
    cookie()