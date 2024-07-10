import csv
with open("Employee.csv") as fr:
    x=csv.reader(fr,delimiter="@")
    for line in x:
        #print(line)
        if len(line)==4:
            Eid,Ename,sal,city=line
            if int(sal)>10000 or city=='Pune':
                print(f"Eid: {Eid}, Ename:{Ename},sal:{sal},city:{city}")