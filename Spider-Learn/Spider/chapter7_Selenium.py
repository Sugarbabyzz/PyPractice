


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


'''
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
'''


# 7、动作链
#   对于没有特定执行对象，如拖拽动作

'''
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
'''

# 8、执行JavaScript
#   执行某些操作，如下拉进度条
#   基本上API没有提供的功能，都可以执行JavaScript来实现

'''
from selenium import webdriver

browser = webdriver.Chrome()
url = 'http://www.zhihu.com/explore'
browser.get(url)
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
'''

# 9、获取节点信息

# * 获取属性
# 使用get_attribute()方法获得节点的属性
'''
from selenium import webdriver

browser = webdriver.Chrome()
url = 'http://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
print(logo.get_attribute('href'))
'''

# * 获取文本值

'''
from selenium import webdriver

browser = webdriver.Chrome()
url = 'http://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
'''

# * 获取id、位置、标签名和大小

'''
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
'''

# 10、切换Frame
#   打开页面后，有一种节点叫iframe，相当于子页面。Selenium默认是在父级Frame里面操作，此时如果页面中还有子Frame，是不能获取到里面的节点的
#   需要用switch_to.frame()方法来切换

'''
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
'''

# 11、延时等待
#   刚打开页面获得的源码并不是完全的，还有额外的Ajax请求，所以需要延时等待

# * 隐式等待
#   当查找的节点没有立即出现时，将等待一段时间再查找，超出设定时间找不到，则抛出异常

'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)
'''

# * 显式等待
#   指定一个最长等待时间，加载出来则返回节点，超时则抛出异常
#   ***** 更多等待条件见书 P259 *****

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))   # 节点加载出来
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))   # 节点可点击
print(input, button)
'''

# 12、前进和后退
#   back() and forward()
'''
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.zhihu.com')
browser.back()
time.sleep(1)
browser.forward()
browser.close()
'''

# 13、Cookies
#   可以对Cookies进行获取、添加、删除等操作

'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
'''

# 14、选项卡管理

'''
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://www.zhihu.com')
'''

# 15、异常处理
#   更多异常类，查看官方文档

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baodu.com')
except TimeoutException:
    print('Time out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()


































































