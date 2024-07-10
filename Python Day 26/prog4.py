import sqlite3
con=sqlite3.connect("w4.db")
cur=con.cursor()
#cur.executescript("""
#                  create table doctors
#                  (
#                 did int primary key,
#                  dname text,
#                 spec text,
#                 dph text
#                 );
#                 create table patients
#                 (
#                 pid int primary key,
#                 pname text,
#                 pbd date,
#                 pph text
#                 );
#                 create table appointments
#                 (
#                 aid int primary key,
#                 did int,
#                 pid int,
#                 adate date,
#                 reason text,
#                 foreign key(did) references doctors(did),
#                 foreign key(pid) references patients (pid) 
#                 )
#                 """
#                 )
cur.execute("pragma foreign_keys=on")
#cur.executescript("""
#                 insert into doctors(did,dname,spec,dph) values
#                 (101,'Dr.Smith','Cardiology','656798765'),
#                 (102,'Dr.Patel','Dermatology','783549097'),
#                 (103,'Dr.Johnson','Pediatrics','1399876');
#                 """)
#cur.executescript("""
#                 insert into patients(pid,pname,pbd,pph) values
#                 (201,'John Doe','1999-01-15','358735665'),
#                 (202,'Jane smith','2000-11-30','98654435'),
#                 (203,'Alice','2001-09-09','09783676');
#                 """)
#cur.executescript("""
#                 insert into appointments(aid,did,pid,adate,reason) values
#                 (301,101,201,'2024-06-15','Regular checkup'),
#                 (302,101,202,'2024-06-16','Follow-up appointment'),
#                 (303,101,203,'2024-06-17','Skin rash'),
#                 (304,102,201,'2024-06-15','Fever'),
#                 (305,102,202,'2024-06-15','Fever'),
#                 (306,102,203,'2024-06-18','Body checkup'),
#                 (307,103,201,'2024-06-19','Baby checkup'),
#                 (308,103,202,'2024-06-20','Flu-shot'),
#                 (309,103,203,'2024-06-20','Acne treatment');
#                 """)
#c_d=cur.execute("select * from doctors")
#for row in c_d:
#   print(row)
#c_p=cur.execute("select * from patients")
#for row in c_p:
#   print(row)
#c_ap=cur.execute("select * from appointments")
#for row in c_ap:
#   print(row)
#c_d=cur.execute("select p.* from patients p join appointments a on p.pid=a.pid group by p.pid having count(a.aid)>2")
#c_d=cur.execute("select p.* from patients p join appointments a on p.pid=a.pid where a.reason=(select reason from appointments a join patients p on a.pid=p.pid where pname='Jane smith')")
#c_d=cur.execute("select d.* from doctors d join appointments a1 on d.did=a1.did join appointments a2 on a1.adate=a2.adate group by d.did,a1.adate having count(*)>2")
#c_d=cur.execute("select d.dname,count(*) from doctors d join appointments a on d.did=a.did group by d.did")
c_d=cur.execute("update appointments set adate='2024-06-30' where aid=301")
for row in c_d:
    print(row)
con.commit()
cur.close()
con.close()