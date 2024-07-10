import sqlite3
con=sqlite3.connect("w2.db")
cur=con.cursor()
#cur.executescript("""
#                 create table student
#                  (
#                  rgno text primary key,
#                  stud_name text not null,
#                  class text not null
#                  );
#                  """)
#cur.executescript("""
#                  create table competition
#                  (
#                  cno int primary key,
#                  cname text
#                  );
#                  """)
#cur.executescript("""
#                  create table stud_competition
#                  (
#                  rgno text,
#                  cno int,
#                  rank int,
#                  year int,
#                  foreign key(rgno) references student(rgno)
#                  foreign key(cno) references competition(cno)
#                  );
#                  """)
cur.execute("pragma foreign_keys=on")
#cur.executescript("""
#                     insert into student(rgno,stud_name,class) values
#                     ('S1001','Cleta','F.Y.BBA'),
#                     ('S1002','Shilpi','S.Y.BCA'),
#                     ('S1003','Hussain','F.Y.BBA'),
#                     ('S1004','Kaustubh','F.Y.BBA'),
#                     ('S1005','Appurvi','F.Y.BCA');
#                     insert into competition(cno,cname) values
#                     (1,'Programming comp'),
#                     (2,'Hackathon comp'),
#                     (3,'Speech comp');
#                     insert into stud_competition(rgno,cno,rank,year) values
#                     ('S1002',1,3,2014),
#                     ('S1003',3,2,2015),
#                     ('S1001',1,2,2014),
#                     ('S1004',1,1,2014),
#                     ('S1002',3,3,2015),
#                     ('S1001',3,1,2015),
#                     ('S1003',3,4,2015),
#                     ('S1002',2,4,2014),
#                     ('S1003',2,3,2014),
#                     ('S1004',2,2,2014),
#                     ('S1001',2,1,2014),
#                     ('S1005',1,4,2014),
#                     ('S1005',2,5,2014);
#                     """)
#c_stud=cur.execute("select * from student")
#for row in c_stud:
#    print(row)
#c_comp=cur.execute("select * from competition")
#for row in c_comp:
#    print(row)
#c_SC=cur.execute("select * from stud_competition")
#for row in c_SC:
#    print(row)
#r_cus=cur.execute("select s.stud_name from student s join stud_competition sc on s.rgno=sc.rgno join competition c on sc.cno=c.cno where s.class='F.Y.BCA' and c.cname='Programming comp'")
#r_cus=cur.execute("select count(distinct s.rgno) from student s join stud_competition sc on s.rgno=sc.rgno join competition c on sc.cno=c.cno where c.cname='Programming comp'")
#r_cus=cur.execute("select c.cname,s.stud_name from stud_competition sc join competition c on sc.cno=c.cno join student s on sc.rgno=s.rgno where rank<=3 order by sc.cno,sc.rank")
r_cus=cur.execute("select count(distinct cno) from stud_competition where year=2014")
for row in r_cus:
    print(row)

con.commit()
cur.close()
con.close()