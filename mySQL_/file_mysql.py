"""
文件存储
1. 存储文件路径 ’/home/tarena/xxxx
2. 将文件以二进制存储在数据库中
"""

import re
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
#存储图片
with open('re1.png','rb') as f:
    data = f.read()
try:
    sql = 'update class set image = %s where name = "Jame"'
    cur.execute(sql,[data])
except Exception as e:
    print(e)
    db.rollback()
db.commit()

#获取图片
sql = 'select image from class where name = "Jame" '
cur.execute(sql)
data = cur.fetchone()
print(data)
with open('re2.jpg','wb') as f:
    f.write(data[0])
db.close()
cur.close()