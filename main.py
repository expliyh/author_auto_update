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
    db = database.Database(database_name, username, address, password)
    idd = db.max_id()
    print(idd)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
