import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table lavanya_car(number varchar(10),car_name varchar(10),manufacture varchar(10),price Integer(10))")
def insert_table():
    c.execute("insert into lavanya_car values('001','toyata','1998','50000')")
    c.execute("insert into lavanya_car values('002','bmw','1999','100000')")
    c.execute("insert into lavanya_car values('003','ferari','2000','150000')")
    c.execute("insert into lavanya_car values('004','duster','2001','200000')")
    c.execute("insert into lavanya_car values('005','innova','2002','100000')")
    con.commit()
def update_table():
    c.execute("update lavanya_car set  number='006',car_name='suzuki' where price=60000")
    con.commit()
def delete_table():
    c.execute("delete from lavanya_car where car_name='innova'")
def select_table():
    c.execute('select * from lavanya_car')
    data=c.fetchall()
    for row in data:
        print(row)
#create_table()
#insert_table()
update_table()
delete_table()
select_table()
c.close()
con.close()
