


#****** 7.1 Selenium的使用******

#   直接使用模拟浏览器运行的方式来实现，所见即所爬

# 1、安装
#   pip3 install -U selenium
#   配置ChromeDriver ，一定放在/usr/local/bin下

# 2、基本用法

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookie())
finally:
    browser.close()
'''


# 3、声明浏览器对象
#   支持多浏览器

# 4、访问页面

'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
print(browser.page_source)
browser.close()
'''

# 5、查找节点

# *单个节点
#   淘宝搜索框
#   所有单节点获取方法，见书P252

'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
#通用函数
input_first = browser.find_element(By.ID, 'q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()
'''

# *多个节点
# find_elements，多个s，结果是列表类型

'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_element(By.CSS_SELECTOR, '.service-bd li')
print(lis)
browser.close()
'''

# 6、节点交互
#   输入文字：send_keys()
#   清空文字：clear()
#   点击按钮：click()

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()









