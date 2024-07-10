import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

  constructor() { }

  employees=[
    {"Employee_id":101,"Employee_name":"Uday","Department":"IT","designation":"AI Developer"},
    {"Employee_id":102,"Employee_name":"Vishnu","Department":"IT","designation":"AI Developer"},
    {"Employee_id":103,"Employee_name":"Pavan","Department":"IT","designation":"Testing"},
    {"Employee_id":104,"Employee_name":"Saikumar","Department":"IT","designation":"DA"},
    {"Employee_id":105,"Employee_name":"Sujith","Department":"IT","designation":"BA"}
  ]
  getEmployees(){
    return this.employees;
  }
}
