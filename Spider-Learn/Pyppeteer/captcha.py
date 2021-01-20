from pyppeteer import launch
import asyncio


def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


async def main():
    browser = await launch(headless=False, ignoreDefaultArgs=['--enable-automation'])
    context = await browser.createIncognitoBrowserContext()
    page = await context.newPage()

    width, height = screen_size()
    await page.setViewport({'width': width, 'height': height})
    await page.setUserAgent(
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15')
    await page.setCookie()
    await page.setExtraHTTPHeaders()
    await page.goto('https://verify.meituan.com/v2/web/general_page?action=spiderindefence&requestCode=95855950be274273bb1cac1e609b9db0&platform=1000&adaptor=auto&succCallbackUrl=https%3A%2F%2imus-mtsi.meituan.com%2Foptimus%2FverifyResult%3ForiginUrl%3Dhttp%253A%252F%252Fwww.dianping.com%252Fshop%252Fj2YKOXx6douJI0Af%252Freview_all%252Fp379%253FqueryType%253DsortType%2526queryVal%253Dlatest&theme=dianping', {'timeout': 0})


    print('已打开验证页')
    print(await page.content())
    await asyncio.sleep(100)





asyncio.get_event_loop().run_until_complete(main())