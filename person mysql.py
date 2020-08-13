import mysql.connector
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table lavu_person(name varchar(10), dob varchar(10),address varchar(10), pan varchar(10))")
def insert_table():
    c.execute("insert into lavu_person values('teju','1999/05/20','sarakki','123456')")
    c.execute("insert into lavu_person values ('tom','2000/01/03','jpnagar','789000')")
    c.execute("insert into lavu_person values('jerry','2000/02/05','jayanagar','134778')")
    c.execute("insert into lavu_person values('mickey','1999/08/02','btm','914833')")
    c.execute("insert into lavu_person values('bheem','2000/05/20','bsk','997271')")
    con.commit()
def select_table():
    c.execute('select * from lavu_person')
    data=c.fetchall()
    for row in data:
        print(row)
create_table()
insert_table()
select_table()
c.close()
con.close()
