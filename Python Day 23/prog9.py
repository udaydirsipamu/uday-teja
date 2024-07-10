import json
with open("Emp.json","r") as fr:
    employees=json.load(fr)
    while True:
        print("\nMenu")
        print("1.Display records of all employees:")
        print("2.Display no of employees working in specified department:")
        print("3.List the name of employee getting the highest salary:")
        print("4.Exit")
        choice=int(input("Enter your choice:"))
        match choice:
            case 1:
                for k,v in employees.items():
                    print(k,v)
            case 2:
                dept=input("Enter department")
                count=sum(1 for v in employees.values() if v['Department']==dept)
                print(count)
            case 3:
                h_sal=max(employees.values(),key=lambda x:int(x['Salary']))
                print(h_sal['name'])
            case 4:
                break
            case _:
                print("Invalid choice")
