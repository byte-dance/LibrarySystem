import pymysql
import threading

mutex = threading.Lock()


class mysql_setting:
    user = 'root'
    pwd = 'k0Ujyn^cB6X#'
    host = '43.139.15.162'
    database = 'library'
    prot = 3306


class DBHelper:
    # 构造函数
    def __init__(self,
                 host=mysql_setting.host,
                 user=mysql_setting.user,
                 pwd=mysql_setting.pwd,
                 db_name=mysql_setting.database,
                 port=mysql_setting.prot):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db_name
        self.conn = None
        self.cur = None
        self.port = port
        self.connect()

    def __del__(self):
        self.close()

    # 连接数据库
    def connect(self):
        try:
            self.conn = pymysql.connect(user=self.user,
                                        password=self.pwd,
                                        host=self.host,
                                        port=self.port,
                                        database=self.db,
                                        charset='utf8')
            self.cur = self.conn.cursor()
            print('数据库连接成功')
        except:
            print('数据库连接失败')
            return False
        return True

    # 如果连接断开，则使用conn.ping()重连，否则执行except
    def confirm_connection(self):
        try:
            self.conn.ping()
            self.cur = self.conn.cursor()
        except:
            print('confirm-connect')
            self.connect()

    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
            print("connection closed")
        return True

    # 用于批量插入数据
    def insert_data(self, sql, params):
        self.confirm_connection()
        try:
            if self.conn and self.cur:
                mutex.acquire()
                self.cur.executemany(sql, params)
                self.conn.commit()
                mutex.release()
        except Exception as e:
            print('批量插入数据失败')
            print(e)
            self.conn.rollback()
            # self.close()
            return False
        return True

    # 用来查询表数据
    def query_data(self, sql):
        data = None
        self.confirm_connection()
        try:
            if self.conn and self.cur:
                mutex.acquire()
                self.cur.execute(sql)
                self.conn.commit()
                query_result = self.cur.fetchall()
                mutex.release()
                data = list(query_result)  # 如果没有查询到数据也要返回空列表，空由外部处理
            else:
                print('数据库连接失败')
        except Exception as e:
            print(f'查询数据失败，sql{sql}')
            print(e)
            # self.close()
        return data

    # 删除数据
    def delete_data(self, sql):
        self.confirm_connection()
        try:
            if self.conn and self.cur:
                mutex.acquire()
                self.cur.execute(sql)
                self.conn.commit()
                mutex.release()
            else:
                print('数据库连接失败')
        except Exception as e:
            print(f'删除数据失败，sql{sql}')
            print(e)
            # self.close()
            return False
        return True
    # 更新数据
    def update_data(self, sql):
        self.confirm_connection()
        try:
            if self.conn and self.cur:
                mutex.acquire()
                self.cur.execute(sql)
                self.conn.commit()
                mutex.release()
            else:
                print('数据库连接失败')
        except Exception as e:
            print(f'更新数据失败，sql{sql}')
            print(e)
            # self.close()
            return False
        return True


dbhelper_singleton = DBHelper()

if __name__ == '__main__':
    sql_str = f'''UPDATE editor 
    SET `name` = '张三' 
    WHERE
	editor_id = 1;'''
    dbhelper_singleton.update_data(sql_str)
