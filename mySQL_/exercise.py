"""
编写一个程序模拟注册和登录过程
创建一个user表 包含用户名和密码
应用程序中模拟注册和登录

"""

import pymysql

count_number = 0
#链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
#创建游标对象
cur = db.cursor()

def login():
    while True:
        name = input('name:')
        password = input('password:')
        try:
            sql = 'select * from user where name = %s and password = %s'
            result = cur.execute(sql,[name,password])
            if not result:
                print('用户名或密码错误')
                break
            return True
        except Exception as e:
            print('错误',e)
            db.rollback()
def sign_in():
    while True:
        name = input('请输入name:')
        password = input('password:')
        try:
            sql = 'insert into user(name,password) value(%s,%s)'
            cur.execute(sql,[name,password])
            db.commit()
            print('注册成功 欢迎登录')
            break
        except Exception as e:
            print('错误,已经有这个用户',e)
            db.rollback()
            continue

def main():
    while True:
        print('1.登录\n2.注册\n不输入退出')
        input_val= input('>>>')
        if not input_val:
            break
        elif input_val == '1':
            if login():
                print('登录成功！！')

        elif input_val == '2':
            sign_in()




if __name__ == '__main__':
    main()

db.close()
cur.close()














db.close()
cur.close()