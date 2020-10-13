from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()  # 相当于 extract_first() 的功能

class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s: s.strip())  # Join()也是一个Processor，将列表拼合成一个字符串
    source_out = Compose(Join(), lambda s: s.strip())  # 第二个参数是一个匿名函数，将字符串的头尾空白字符去掉

