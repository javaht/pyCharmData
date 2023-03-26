from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# drag_and_drop(source,target)拖拽操作嘛，开始位置和结束位置需要被指定，这个常用于滑块类验证码的操作之类。

def drag():
    browser = webdriver.Chrome()
    browser.maximize_window()
    url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    time.sleep(2)

    browser.switch_to.frame('iframeResult')

    # 开始位置
    source = browser.find_element(By.CSS_SELECTOR,"#draggable")

    # 结束位置
    target = browser.find_element(By.CSS_SELECTOR,"#droppable")

    # 执行元素的拖放操作
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()
    # 拖拽
    time.sleep(15)

    # 关闭浏览器
    browser.close()

if __name__ == '__main__':
    drag()