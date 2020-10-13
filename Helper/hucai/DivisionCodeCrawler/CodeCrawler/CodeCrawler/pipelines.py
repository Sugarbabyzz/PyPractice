import pymysql


class MysqlPipeline:

    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT')
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):

        table = 'division_code'
        dic = {
            'name': item['name'],
            'code': item['code'],
        }

        # 入库操作
        keys = ','.join(dic.keys())
        values = ','.join(['%s'] * len(dic))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'\
              .format(table=table, keys=keys, values=values)
        update = ','.join([" {key} = %s".format(key=key) for key in dic])
        sql += update
        try:
            if self.cursor.execute(sql, tuple(dic.values()) * 2):
                self.db.commit()
        except Exception as err:
            self.db.rollback()

        return item

    def closer_spider(self, spider):
        self.db.close()