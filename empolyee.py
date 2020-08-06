import sqlite3
con=sqlite3.connect('db3.sqlite3')
c=con.cursor()
def create():
    c.execute('create table empolyee(emp_id int primary key,emp_name text,emp_salary )')
def insert():
    c.execute("insert into empolyee values('01','tom','10000')")
    c.execute("insert into empolyee values('02','mickey','20000')")
    c.execute("insert into empolyee values('03','jerry','30000')")
    c.execute("insert into empolyee values('04','bheem','40000')")
    con.commit()
def select():
    c.execute('select * from empolyee')
    data=c.fetchall()
    print(data)
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
    c.close()
    con.close()
create()
insert()
select()
