import pymysql
import json


class Processor:
    """
        讽刺文本comments字段格式处理程序
    """

    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='reddit_data')
        self.c1 = self.db.cursor()
        self.c2 = self.db.cursor()

    def process(self, name):

        if name == 'submission_ps4':
            query_sql = "SELECT * FROM " + name + " WHERE pubtime > '2017-07-27 22:01:56'"
            count_sql = "SELECT COUNT(1) FROM " + name + " WHERE pubtime > '2017-07-27 22:01:56'"
        else:
            query_sql = "SELECT * FROM " + name
            count_sql = "SELECT COUNT(1) FROM " + name

        self.c1.execute(query_sql)
        self.c2.execute(count_sql)
        total = self.c2.fetchone()[0]
        count = 1
        errors = []

        row = self.c1.fetchone()
        while row:
            # 获取并处理字段数据
            id = row[0]
            comments = row[8]
            try:
                comments = json.dumps(eval(json.loads(comments)), default=str).replace("b\\\"", "").replace("\\\\n", "\\n").replace("\\\"", "").replace("b'", "").replace("'\"", "\"")
            except:
                errors.append(id)

            # 更新字段
            update_sql = "UPDATE " + name + " SET comments = %s WHERE id = %s"
            try:
                self.c2.execute(update_sql, (comments, id))
                self.db.commit()
            except:
                self.db.rollback()

            # next
            print("{}  {}/{} 处理完毕。".format(id, count, total))
            row = self.c1.fetchone()
            count += 1


        print('错误的')
        print(errors)
        print(len(errors))


if __name__ == '__main__':

    processor = Processor()
    # submission_apple
    # submission_xboxone
    # submission_ps4
    processor.process('submission_xboxone')



