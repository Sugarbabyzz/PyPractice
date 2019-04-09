

#****** 13.11 Scrapyrt的使用 ******

#   在任意一个Scrapy项目中运行如下命令来启动HTTP服务：scrapyrt
#   运行后，默认在9080端口上启动服务
#   可更换运行端口：scrapyrt -p 9081


#   ***注意：在Terminal中输入 & 符号，前面必须加反斜杠
#   1、GET请求
#   curl http://localhost:9080/crawl.json?spider_name=quotes&url=http://quotes.toscrape.com/

#   2、POST请求
#   需要用JSON格式
#   curl http://localhost:9080/crawl.json -d '{"request":{"url": "http://quotes.toscrape.com/", "dont_filter": "True", "callback": "parse", "cookies": {"foo": "bar"}}, "max_requests": 2, "spider_name": "quotes"}'




#****** 13.12 Scrapy对接Docker ******


#   Docker为了解决环境的安装配置、环境的版本冲突解决等问题




