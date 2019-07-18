"""
write_db.py
pymysql 写操作示例 （insert update delete ）
"""
import pymysql
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
#获取游标
cur = db.cursor()
#写操作
try:
    #写sql语句
    # name = input('Name：')
    # age = int(input('Age:'))
    # score = float(input('Score:'))
    # sql = "insert into class(name,age,score,Date) values('%s',%d,%.1f,curdate())"%(name,age,score)
    # print(sql)
    ###增加
    # name = input('Name：')
    # age = input('Age:')
    # score = input('Score:')
    # sql = "insert into class(name,age,score,Date) values(%s,%s,%s,curdate())"
    # print(sql)
    # cur.execute(sql,[name,age,score])
    ###修改
    # sql = "update interest set price = 11800 where name = 'Abby';"
    # cur.execute(sql)
    ###删除操作
    sql = "delete from class where  score <= 80;"
    cur.execute(sql)

    db.commit()
except Exception as e:
    print(e)
    print('操作回滚')
    db.rollback()#退回到commit执行之前的数据库状态
finally:
    cur.close()
    db.close()