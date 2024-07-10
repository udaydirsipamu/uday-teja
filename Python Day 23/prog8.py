import json
employees={}
for i in range(5):
    eid=int(input("Enter eid:"))
    name=input("Enter name:")
    dept=input("Enter department")
    sal=int(input("Enter salary:"))
    desg=input("Enter desegnation")
    while dept not in ["IT","HR","Sales"]:
        print("Invalid depsrtment.Please enter 'IT','HR' or 'Sales'.")
    while desg not in ["Manager","Sr.Exec"]:
        print("Invalid desegnation.Please enter 'Manager' or 'Sr.Exec'.")
    employees[eid]={"name":name,"Department":dept,"Salary":sal,"Desegnation":desg}
with open("Emp.json","w") as fw:
    json.dump(employees,fw)
print("Json created successfully")
