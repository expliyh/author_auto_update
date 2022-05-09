import pymysql


class Database:
    def __init__(self, basename, username, address, password):
        self.db = pymysql.connect(host=address, user=username, password=password, database=basename)
        return

    def is_connected(self):
         """Check if the server is alive"""
        try:
            self.conn.ping(reconnect=True)
            # print"db is connecting"
        except:
            # traceback.print_exc()
            self.conn = self.to_connect()
            print("db reconnect")

    def max_id(self):
        sql = "SELECT MAX(id) FROM `imginfo` WHERE 1"
        self.is_connected()
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            # print(results)
            for row in results:
                idd = row[0]
            return idd
        except pymysql.Error:
            return 'Error'

    def get_image_id(self, idd):
        sql = "SELECT * FROM `imginfo` WHERE `id` = '%s'" % idd
        self.is_connected()
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            img_id = -1
            for row in results:
                img_id = row[5]
            return img_id
        except pymysql.Error:
            return 'Error'

    def update_author(self, idd, author: str, author_id):
        cursor = self.db.cursor()
        sql = "UPDATE `imginfo` SET `author`='%s',`author_id`='%s' WHERE `id`='%s'" % (author, author_id, idd)
        self.is_connected()
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except pymysql.Error:
            # 如果发生错误则回滚
            self.db.rollback()
        cursor.close()
