import sqlite3
con=sqlite3.connect("Wipro.db")
print("Database connected successfully")
cur=con.cursor()
#cur.execute("""
#           Create table Emp
#            (
#           eid int primary key,
#           ename text not null,
#            sal int check(sal>5000)
#           );
#           """)
#cur.execute("insert into Emp values(101,'Uday',6000)")
#cur.execute("insert into Emp values(102,'Teja',7000)")
#cur.execute("insert into Emp values(103,'Ali',8000)")
#cur.execute("insert into Emp values(104,'vishnu',12000)")
name=input("Enter name")
s=int(input("Enter salary"))
#result=cur.execute("select * from Emp")
result=cur.execute("select * from Emp where ename=? or sal=? ",(name,s))
for row in result:
    print(row)
print("")
#result=cur.execute("select * from Emp")
#rall=result.fetchall()
#print(rall)
con.commit()
cur.close()
con.close()