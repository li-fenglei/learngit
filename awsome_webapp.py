#coding=utf-8
import mysql,mysql.connector
conn=mysql.connector.connect(user='root',password='892671472',database='test',use_unicode=True)
cursor=conn.cursor()
#cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user(id,name) values (%s,%s)',['1','felix'])
cursor.rowcount
conn.commit()
cursor.close()
