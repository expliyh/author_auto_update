# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import pixivapi
import os
import database

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    database_name = os.environ['database']
    username = os.environ['username']
    password = os.environ['password']
    address = os.environ['address']
    pixiv_name = os.environ['pixiv_username']
    pixiv_pass = os.environ['pixiv_password']
    refresh = os.environ['pixiv_refresh']
    db = database.Database(database_name, username, address, password)
    idd = db.max_id()
    pixiv_client = pixivapi.Client()
    # pixiv_client.login(pixiv_name, pixiv_pass)
    pixiv_client.authenticate(refresh)
    print('There are %s images in the database, updating.\n' % (idd + 1))
    for i in range(idd + 1):
        pixiv_id = db.get_image_id(i)
        illustration = pixiv_client.fetch_illustration(pixiv_id)
        author = illustration.user
        author_id = author.id
        author_name = author.name

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
