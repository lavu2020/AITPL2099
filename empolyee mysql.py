#create table name_empolyee
import mysql.connector
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table lavanya_emp(emp_id varchar(10),name varchar(20),salary Integer(10))")
def insert_table():
    c.execute("insert into lavanya_emp values('001','lavanya',10000)")
    c.execute("insert into lavanya_emp values('002','tom',20000)")
    c.execute("insert into lavanya_emp values('003','jerry',30000)")
    c.execute("insert into lavanya_emp values('004','mickey',40000)")
    c.execute("insert into lavanya_emp values('005','bheem',50000)")
    con.commit()
def select_table():
    c.execute('select * from lavanya_emp')
    data=c.fetchall()
    for row in data:
        print(row)
create_table()
insert_table()
select_table()
c.close()
con.close()
