import csv
with open("student.csv") as fr:
    x=csv.reader(fr,delimiter="@")
    for line in x:
        print(line)