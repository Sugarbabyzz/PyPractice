import requests
import pandas as pd
from lxml import etree
from urllib import parse


class CodeCrawler:

    def __init__(self, u):
        self.u = u
        self.df_result = pd.DataFrame(columns=('区划码', '名称'))
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            # 'Cookie': '_trs_uv=k21g8bwy_6_12r; AD_RS_COOKIE=20080918'
        }
        self.proxies = {'https': '183.167.217.152:63000'}
        self.errURL = []

    def recursion(self, url, term):

        session = requests.Session()
        res = session.get(url, headers=self.headers)
        res.encoding = 'gb2312'
        # 页面未响应的情况
        if res.status_code == 502:
            self.errURL.append([term, url])
            print(self.errURL)

        s = etree.HTML(res.text)
        for trr in s.xpath('//tr[@class="citytr" or @class="countytr" or @class="towntr" or @class="villagetr"]'):
            if 'villagetr' in trr.xpath('@class'):
                code = trr.xpath('td[1]/text()')[0]
                name = trr.xpath('td[3]/text()')[0]
            else:
                code = trr.xpath('td[1]/a/text()')[0]
                name = trr.xpath('td[2]/a/text()')[0]
            # print(code, name)
            # 存结果
            df = pd.DataFrame([[code, name]], columns=['区划码', '名称'])
            self.df_result = self.df_result.append(df, ignore_index=True)

            try:
                new_url = parse.urljoin(url, trr.xpath('td[1]/a/@href')[0])
                print(name, new_url)
                self.recursion(new_url, name)  # 重复调用自己，一直达到最深的页面
            except:
                pass

        return

    def process(self):
        # 打开页面
        session = requests.Session()
        response = session.get(self.u, headers=self.headers)
        response.encoding = 'gb2312'
        # 构造xpath对象
        selector = etree.HTML(response.text)

        # 开始处理
        for tr in selector.xpath('//tr[@class="provincetr"]'):

            for td in tr.xpath('td'):
                if len(td.xpath('a/@href')) > 0:
                    try:
                        name = td.xpath('a/text()')[0]
                        url = parse.urljoin(self.u, td.xpath('a/@href')[0])
                        print(name, url)
                        self.recursion(url, name)  # 递归
                    except Exception as e:
                        print(e)

        print(self.df_result)
        try:
            self.df_result.to_excel('result.xlsx', index=False)
        except:
            print('to excel error')

        print(self.errURL)
        try:
            with open('errFiles.txt', encoding='utf-8') as f:
                for item in self.errURL:
                    f.write(item)
                    f.write('\n')
        except:
            print('to txt error')


if __name__ == '__main__':

    u = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html'
    obj = CodeCrawler(u)
    obj.process()