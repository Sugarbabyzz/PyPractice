import asyncio
import random
from pyppeteer import launch
import pyppeteer.chromium_downloader


def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


def get_cookies(page):
    """获取cookie"""
    cookies_list = page.cookies()
    cookies = ''
    for cookie in cookies_list:
        str_cookie = '{0}={1}'.format(cookie.get('name'), cookie.get('value'))
        cookies += str_cookie
    print(cookies)
    return cookies


async def main():
    browser = await launch(headless=False,
                           ignoreDefaultArgs=['--enable-automation'],
                           args=['--no-sandbox', '--proxy-server=218.67.20.252:28517'])
    # context = await browser.createIncognitoBrowserContext()
    page = await browser.newPage()

    width, height = screen_size()
    await page.setViewport({'width': width, 'height': height})
    await page.setUserAgent(
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15')
    await page.goto('https://account.dianping.com/login', {'timeout': 0})
    print('已打开登录页')
    await asyncio.sleep(3)

    await page.frames[1].click('span[class*="bottom-password-login"]')
    print('点击登录窗口')
    await asyncio.sleep(1)
    await page.frames[1].click('#tab-account')
    print('切换成功')
    await asyncio.sleep(1)
    await page.frames[1].type('#account-textbox', '17172395742', {'delay': random.randint(51, 100)})
    await asyncio.sleep(1)
    await page.frames[1].type('#password-textbox', 'caiji123456', {'delay': random.randint(51, 100)})
    print('已输入账号密码')
    await asyncio.sleep(2)
    await page.frames[1].click('#login-button-account')
    print('已点击登录')
    await asyncio.sleep(3)
    # await page.goto('http://www.dianping.com/shop/G7e7SA1l2Evq5oMn')
    print('进入店铺详情页')
    await asyncio.sleep(3)

    # 验证是否正确进入
    # print(await page.content())

    # cookies = get_cookies(page)


    await asyncio.sleep(100000000)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

