"""
mysql.py
pymysql 操作数据库基本流程演示
"""
import pymysql
#链接数据库
db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database ='stu',
                     charset = 'utf8')

#获取游标(用来操作数据库 ，执行sql语句)
cur = db.cursor()

#执行sql语句
# sql = "insert into class values(null,'Lilid',17,'w',85.5,'2018-10-8');"
# cur.execute(sql)
# #将写操作提交
# db.commit()  #将写操作提交，多次写操作一同提交
#获取数据库数据
sql = "select * from class where sex='m';"
cur.execute(sql)
# one_row = cur.fetchone()
# print(one_row)
# many_row = cur.fetchmany(2)
# for i in range(2):
#     print(many_row[i])
all_row = cur.fetchall()
for i in all_row:
    print(i)
#关闭数据库
db.close()
#关闭游标
cur.close()

