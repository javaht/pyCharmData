from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# WebDriverWait的参数说明：
# WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
# driver: 浏览器驱动
# timeout: 超时时间，等待的最长时间（同时要考虑隐性等待时间）
# poll_frequency: 每次检测的间隔时间，默认是0.5秒
# ignored_exceptions:超时后的异常信息，默认情况下抛出NoSuchElementException异常
# until(method,message='')
# method: 在等待期间，每隔一段时间调用这个传入的方法，直到返回值不是False
# message: 如果超时，抛出TimeoutException，将message传入异常
# until_not(method,message='')
# until_not 与until相反，until是当某元素出现或什么条件成立则继续执行，until_not是当某元素消失或什么条件不成立则继续执行，参数也相同。
def wait():
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    # 设置等待时间10s
    wait = WebDriverWait(browser, 10)
    # 设置判断条件：等待id='kw'的元素加载完成
    input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
    # 在关键词输入：关键词
    input.send_keys('Python')

    # 关闭浏览器
    time.sleep(2)
    browser.close()

if __name__ == '__main__':
    wait()