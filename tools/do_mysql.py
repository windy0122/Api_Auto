import mysql.connector
from tools.project_path import *
from tools.read_config import ReadConfig


class DoMysql(object):
    def do_mysql(self, query_sql, state='all'):
        # 数据库连接信息
        db_config = eval(ReadConfig().get_config(test_config_path, 'DB', 'db_config'))
        # 创建数据库连接
        cnn = mysql.connector.connect(**db_config)

        # 创建游标
        cursor = cnn.cursor()

        # sql语句(做成配置)
        # query_sql = "select * from member where MobilePhone=13700000356"

        # 执行语句
        cursor.execute(query_sql)

        # 获取结果，打印结果
        if state == 1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()
        # print(res)

        # 关闭游标
        cursor.close()

        # 关闭连接
        cnn.close()

        return res


if __name__ == '__main__':
    query_sql = "select * from member where MobilePhone=13700000356"
    res = DoMysql().do_mysql(query_sql)
    print(res)



