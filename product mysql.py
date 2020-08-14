import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table lavanya_product(product_id varchar(10),product_name varchar(10),price Integer(10))")
def insert_table():
    c.execute("insert into lavanya_product values('001','pen','10')")
    c.execute("insert into lavanya_product values('002','pencil','20')")
    c.execute("insert into lavanya_product values('003','sketch','30')")
    c.execute("insert into lavanya_product values('004','eraser','40')")
    c.execute("insert into lavanya_product values('005','scale','50')")
    con.commit()
def update_table():
    c.execute("update lavanya_product set  product_id='006',product_name='fevicol' where price='60'")
    con.commit()
def delete_table():
    c.execute("delete from lavanya_product where product_id='005'")
def select_table():
    c.execute('select * from lavanya_product')
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
