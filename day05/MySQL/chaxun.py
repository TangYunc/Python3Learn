import pymysql

#1.建立数据库连接
db = pymysql.connect("localhost", "root", "123456", "db2", charset="utf8")


sql_select = "select * from city;"
#2创建游标对象
cursor = db.cursor(sql_select)

data = cursor.fetchone()
print("fetchone的结果为",data)

data2 = cursor.fetchmany(2)
print("fetchmany(2)的结果为",data2)
for i in data2:
	print(i)

data3 = cursor.fetchall()
print("fetchall()的结果为",data3)
for i in data3:
	print(i)

#3.使用游标对象的方法操作数据库
cursor.execute("insert into sheng values(1,20000,\'四川省');")



#4.提交commit
db.commit()
#5.关闭游标对象
cursor.close()
#6.关闭数据库连接
db.close()