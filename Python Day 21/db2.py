import sqlite3
con=sqlite3.connect("w1.db")
cur=con.cursor()
#cur.executescript("""
#                  create table account
#                 (
#                  ano int primary key,
#                  bname text not null,
#                 bal int check(bal>500));

#cur.executescript("""
#               create table customer
#                (
#                cust_no int primary key,
#                cust_name text not null,
#                street text,
#                city text);
#               """) 
#cur.executescript("""
#                 create table acc_customer
#                (
#                ano int,
#                cust_no int,
#                foreign key(ano) references account(ano),
#                foreign key(cust_no) references customer(cust_no));
#                 """)
#while True:
#   ano=int(input("Enter account number:"))
#   bname=input("Enter bname:")
#   bal=int(input("Enter balance"))
#   cur.execute("insert into account values(?,?,?)",(ano,bname,bal))
#   choice=input("Do you want to insert more records Yes/No").lower()
#   if choice=='no':
#       break
#while True:
#   cust_no=int(input("Enter customer number:"))
#   cust_name=input("Enter customer name:")
#   street=input("Enter street name")
#   city=input("Enter city name")
#   cur.execute("insert into customer values(?,?,?,?)",(cust_no,cust_name,street,city))
#   choice=input("Do you want to insert more records Yes/No").lower()
#   if choice=='no':
#       break
#while True:
#   ano=int(input("Enter account number:"))
#   cust_no=int(input("Enter customer number:"))
#   cur.execute("insert into acc_customer values(?,?)",(ano,cust_no))
#   choice=input("Do you want to insert more records Yes/No").lower()
#   if choice=='no':
#       break
#result_acc=cur.execute("select * from account")
#for row in result_acc:
#    print(row)
#print("")
#result_cust=cur.execute("select * from customer")
#for row in result_cust:
#   print(row)
#result_acc_cust=cur.execute("select * from acc_customer")
#for row in result_acc_cust:
#    print(row)
#r_cust=cur.execute("select customer.*,account.bal from customer join acc_customer on customer.cust_no=acc_customer.cust_no join account on acc_customer.ano=account.ano where account.bal between 100000 and 200000")
#r_cust=cur.execute("select c.cust_name from customer c join acc_customer ac on c.cust_no=ac.cust_no join account a on ac.ano=a.ano where a.bname='Chinchwad' group by c.cust_no having count(*)>2")
#r_cust=cur.execute("select cust_name from customer where street like '%road%' and  city ='Mumbai' ")
#r_cust=cur.execute("select a.bname,count(distinct ac.cust_no) from account a join acc_customer ac on a.ano=ac.ano group by a.bname")
#r_cust=cur.execute("update account set bal=bal+(bal * 0.1) where bname='Chinchwad'")
#r_cust=cur.execute("select c.cust_name from customer c join acc_customer ac on c.cust_no=ac.cust_no join account a on ac.ano=a.ano group by c.cust_name order by a.bal desc limit 1,2")
#r_cust=cur.execute("select c.cust_name,a.bal from customer c join acc_customer ac on c.cust_no=ac.cust_no join account a on ac.ano=a.ano group by c.cust_name order by a.bal desc")
#r_cust=cur.execute("select c.cust_name from customer c join acc_customer ac on c.cust_no=ac.cust_no join account a on ac.ano=a.ano order by a.bal limit 1")
r_cust=cur.execute("delete from account where bal<5000")
for row in r_cust:
    print(row)
con.commit()
cur.close()
con.close()