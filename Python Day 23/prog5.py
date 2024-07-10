import csv
with open("Employee.csv","w",newline="") as fw:
    write=csv.writer(fw,delimiter=",")
    write.writerow(["Eid","Ename","sal","city"])
    for _ in range(5):
        l=[]
        l.append(int(input("Enter Eid:")))
        l.append(input("Enter Ename:"))
        l.append(int(input("Enter sal:")))
        l.append(input("Enter city:"))
        write.writerow(l)