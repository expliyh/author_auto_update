import pymysql


class Database:
    def __init__(self, basename, username, address, password):
        self.basename = basename
        self.username = username
        self.address = address
        self.password = password
        self.db = pymysql.connect(host=address, user=username, password=password, database=basename)
        return

    def connect(self):
        return pymysql.connect(host=self.address, user=self.username, password=self.password, database=self.basename)

    def is_connected(self):
        try:
            self.db.ping(reconnect=True)
            # print"db is connecting"
        except:
            # traceback.print_exc()
            self.db = self.connect()
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
                img_id = row[6]
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
            print("Database operation failure")
            self.db.rollback()
        cursor.close()

    def update_all(self, idd, title: str, author: str, pixiv_id, author_id, tags: str, caption: str, original_url: str, reply: str):
        cursor = self.db.cursor()
        sql = "UPDATE `imginfo` SET `name`='%s',`author`='%s',`pixivid`='%s',`author_id`='%s',`tags`='%s'," \
              "`caption`='%s',`original_url`='%s',`reply`='%s' WHERE `id`='%s'" % (title, author, pixiv_id,
                                                                                   author_id, tags, caption,
                                                                                   original_url, reply, idd)
        # print(sql)
        self.is_connected()
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except pymysql.Error:
            # 如果发生错误则回滚
            print("Database operation failure")
            self.db.rollback()
        cursor.close()
