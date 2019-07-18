"""
将单词存入数据库
1.创建数据库 dict(utf8)
2.创建数据表worlds 将单词和单词解释分别存入不同的字段
3.将单词存入worlds；
闯过19500 条 即可

"""
#create database dict charset='utf8'
#use dict
#create table worlds (id int primary key auto_increment,worlds varchar(64) , decipher text);

import re
import pymysql

count_number = 0
#链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
#创建游标对象
cur = db.cursor()

#打开文件读取
fd = open('../IO/dict.txt','r',encoding='utf-8')
#
# print(strlist)
for i in fd:
    #读取每行 并返回单词与解释的元祖  #只返回括号内匹配内容 并合并成元祖

    tup = re.findall(r"(\S+)\s+(.*)",i)[0]
    sql = 'insert into worlds(worlds,decipher) values(%s,%s)'
    print(tup)
    try:
        cur.execute(sql,[tup[0],tup[1]])
    except Exception as e:
        print(e)
        db.rollback()
db.commit()
db.close()
cur.close()
fd.close()
