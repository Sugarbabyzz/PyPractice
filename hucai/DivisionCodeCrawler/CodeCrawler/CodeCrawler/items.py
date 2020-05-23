from scrapy import Field, Item


class CodeItem(Item):
    """ 区划码和名称 """
    code = Field()  # 区划码
    name = Field()  # 名称