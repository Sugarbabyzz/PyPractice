


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
    print(browser.page_source)
finally:
    browser.close()

