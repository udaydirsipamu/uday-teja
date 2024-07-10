import csv
with open("student.csv","w",newline="") as fw:
    write=csv.writer(fw,delimiter=",")
    write.writerow(["Rno","Name","Age","City"])
    for _ in range(3):
        l=[]
        l.append(int(input("Enter Rno:")))
        l.append(input("Enter Name:"))
        l.append(int(input("Enter Age:")))
        l.append(input("Enter City:"))
        write.writerow(l)
