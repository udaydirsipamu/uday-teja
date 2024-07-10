import sqlite3
con=sqlite3.connect("uday.db")
print("Database connected successfully")
cur=con.cursor()
#cur.executescript("""
#            Create table dept
#            (
#             dname text primaty key,
#             hod text not null
#             );
#             create table emp
#             (
#                   eid int primary key,
#                   ename text not null,
#                   sal int check(sal>2000),
#                   city text,
#                   dname text,
#                   foreign key(dname) references dept(dname)
#                  );
#             """)

#cur.executescript("""
#                   insert into dept(dname,hod) values
#                   ('IT','Uday'),
#                   ('Fin','Teja'),
#                    ('HR','Ali');
#                  """)
# cur.executescript("""
#                    insert into emp(eid,ename,sal,city,dname) values
#                   (101,'Huzaifa',12000,'Mumbai','IT'),
#                   (102,'Harshida',15000,'Mumbai','Fin'),
#                   (103,'Divyanshu',14000,'Hyd','IT'),
#                   (104,'Vishnu',13000,'Pune','HR');
#                   """)
#result_dept=cur.execute("select * from dept")
#for row in result_dept:
#    print(row)
#print("")
#dept_name = input("Enter deparment name ")
#emp_name='Huzaifa'
#result_emp=cur.execute("select ename from emp where dname=(select dname from emp where ename=?) ",(emp_name,))
#dept_name='IT'
#result_emp=cur.execute("update emp set sal=sal+(sal * 0.1) where dname= ? ",(dept_name,))
#result_emp=cur.execute("select ename from emp order by sal desc limit 3")
#result_emp=cur.execute("select ename from emp order by sal desc limit 1,1")
#result_emp=cur.execute("select * from emp inner join dept on emp.dname=dept.dname where dept.dname in ('HR','IT') order by emp.sal desc ")
result_emp=cur.execute("select dept.dname,count(emp.eid) from dept left join emp on dept.dname=emp.dname group by dept.dname")
for row in result_emp:
   print(row)
con.commit()
cur.close()
con.close()