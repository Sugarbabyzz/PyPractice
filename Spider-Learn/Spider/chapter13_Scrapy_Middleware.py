

#****** 13.5 Downloader Middleware的用法 ******

# 对接项目-scrapydownloadertest


#   修改User-Agent、处理重定向、设置代理、失败重试、设置Cookies等功能都要借助它实现

# 作用：
#   1、在Scheduler调度处队列的Request发送给DOwnloader下载之前。对其进行修改
#   2、在下载后生成的Response发送给Spider之前，可修改

# 至少实现以下其中一个方法，即可定义一个Downloader Middleware
#   1、process_request(request, spider)
#       调度前被调用
#   2、process_response(request, response, spider)
#   3、process_exception(request, exception, spider)


# * 见scrapydownloadertest项目 ⏫


#  修改User-Ageng方法：
#   1、修改settings里面的USER_AGENT变量
#   2、通过Downloader Middleware的process_request()方法修改


#****** 13.6 Spider Middleware的用法 ******

#   用法同上

# 至少实现以下其中一个方法，即可定义一个Downloader Middleware
#   1、process_spider_input(response, spider)
#   2、process_spider_output(response, result, spider)
#   3、process_spider_exception(response, exception, spider)
#   4、process_start_request(start_requests, spider)



#****** 13.7 Item Pipeline 的用法 ******

# 对接项目-images360

# 必须实现的一个方法是 process_item(item, spider)
#   1、open_spider(spider)
#   2、close_spider(spider)
#   3、from_crawler(cls, crawler)
#       通过crawler对象，可以拿到Scrapy的核心组件，如全局配置等











