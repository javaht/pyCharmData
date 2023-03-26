from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 左键  其实就是页面交互操作中的点击click()操作
# 右键  context_click()
# ActionChains(browser)：调用ActionChains()类，并将浏览器驱动browser作为参数传入
# context_click(right_click)：模拟鼠标双击，需要传入指定元素定位作为参数
# perform()：执行ActionChains()中储存的所有操作，可以看做是执行之前一系列的操作

def action():
    browser = webdriver.Chrome()
    browser.get(r'https://www.baidu.com')
    time.sleep(2)

    # 定位到要右击的元素，这里选的新闻链接
    right_click = browser.find_element(By.LINK_TEXT,'新闻')

    # 执行鼠标右键操作
    ActionChains(browser).context_click(right_click).perform()
    time.sleep(2)

    # 关闭浏览器
    browser.close()

if __name__ == '__main__':
    action()