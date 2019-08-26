import sqlite3

conn = sqlite3.connect("phones.db")
cursor = conn.cursor()
#cursor.execute("drop table  if exists phones")
#cursor.execute("create table phones (name varchar(100), ph_num INTEGER)")
cursor.execute("insert into phones values('test', 788987)")
cursor.execute("commit")
cursor.execute("select * from phones")
results = cursor.fetchall()
print(results)
conn.close()
