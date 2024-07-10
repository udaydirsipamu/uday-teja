import { Component } from '@angular/core';
import { EmployeeService } from './employee.service';
import { NgForm } from '@angular/forms';
import { CRUDService } from './crud.service';
import { Book } from './Book';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Project1';

  myName : String = "Uday"
  imgSrc : String = "nature1.jpeg"
  imgSrc1 : String = "nature1.jpeg"
  imgSrc2 : String = "nature2.jpeg"
  imgSrc3 : String = "nature3.jpeg"
  imgSrc4 : String = "nature4.jpeg"
  imgSrc5 : String = "nature5.jpeg"

  buttonClicked(){
    alert("You clicked on a button..")
  }

  userID : String = ""
  verifyData(){
    if(this.userID=="Uday")
      alert("Valid user..")
    else
      alert("Given name is not Uday..")
  }

  bDisplayLoginForm : boolean = false
  UID : String =""
  enableFlag(){
    this.bDisplayLoginForm=true
  }
  validate(){
    if(this.UID=="Uday")
      alert("You are valid User")
    else
      alert("Invalid User,pls check the credentials")
  }

  ProductList=[
    {"product_id":101,"product_name":"TV","description":"LG","cost":35000},
    {"product_id":102,"product_name":"Mobile","description":"Samsung","cost":35000},
    {"product_id":103,"product_name":"Laptop","description":"HP","cost":55000},
    {"product_id":104,"product_name":"Earphones","description":"Boat","cost":5000},
    {"product_id":105,"product_name":"Speakers","description":"Dolby digital","cost":15000}
  ]
  bDisplayProductData : boolean =false
  enableProductDisplayFlag(){
    this.bDisplayProductData=true
  }

  strText : String ="I am learning Angular"

  nCurrency : number =1200

 todaysDate = new Date()

 num1 : number = 0
 num2 : number = 0
 res : number = 0
  SumData(){
    this.res = this.num1 + this.num2
    alert(`Sum of two numbers is : ${this.res}`)
  }
  
  bDisplayLoginForm1 : boolean = false
  bDisplayRegistrationForm : boolean =false
  UID1: String =""
  pwd : String =""
  enableFlag1(){
    this.bDisplayLoginForm1=true
    this.bDisplayRegistrationForm =false
  }
  validate1(){
    if(this.UID1=="Uday"&& this.pwd=="password")
      alert("You are valid user")
    else
      alert("Invalid user,please check credentials")
  }
  UID2: String =""
  pwd1 : String =""
  enableFlagReg(){
    this.bDisplayLoginForm1=false
    this.bDisplayRegistrationForm=true
  }
  validate2(){
    if(this.UID2== "Uday" && this.pwd1== "password")
      alert("You are registered")
    else
      alert("Invalid data,please register again")
  }

  EmployeeList=[
    {"Employee_id":101,"Employee_name":"Uday","Department":"IT","designation":"SDE"},
    {"Employee_id":102,"Employee_name":"Vishnu","Department":"IT","designation":"SE"},
    {"Employee_id":103,"Employee_name":"Pavan","Department":"IT","designation":"Testing"},
    {"Employee_id":104,"Employee_name":"Saikumar","Department":"IT","designation":"DA"},
    {"Employee_id":105,"Employee_name":"Sujith","Department":"IT","designation":"BA"}
  ]
  bDisplayEmployeeData : boolean =false
  enableEmployeeDisplayFlag(){
    this.bDisplayEmployeeData=true
  }

  /**constructor(private empService : EmployeeService){}
  bDisplayEmpData : boolean = false
  emplist : any =[]
  enableEmployeeFlag(){
    this.bDisplayEmpData = true
    this.emplist=this.empService.getEmployees()
  }**/

  onSubmit(loginForm : NgForm){
    let UID = loginForm.controls['username'].value
    let PWD = loginForm.controls['password'].value

    if (UID == "Uday" && PWD=='test123')
      alert("You are valid user")
    else
      alert("Invalid user,Pls check user id and password")
  }

  constructor(private empService : EmployeeService,private crudService:CRUDService){}
  booklist : any =[]
  getBookData(){
    this.crudService.getBooks().subscribe(
      (response)=>{this.booklist=response;},
      (error)=>console.log(error)
    );
  }
  bDisplayAddData:boolean=false;
  bDisplayUpdateData:boolean=false;
  addOrUpdateDisplay:String= "";
  book=new Book(0,"","",0);
  addBookData(){
    this.bDisplayAddData=true;
    this.bDisplayUpdateData=false;
    this.addOrUpdateDisplay="Add Book"
    this.book=new Book (0,"","",0);
  }
  createOrUpdateData(){
    if(this.addOrUpdateDisplay == "Add Book"){
      this.bDisplayAddData=false;
      this.crudService.insertBook(this.book).subscribe(
        (response) =>{console.log("Record inserted successfully.."); this.getBookData();},
        (error)=>console.log(error)
      );
    }
    else if(this.addOrUpdateDisplay=="Update Book"){
      this.bDisplayUpdateData=false;
      this.crudService.updateBook(this.book).subscribe(
        (response) =>{alert("Record updated successfully..");this.getBookData();},
        (error)=>console.log(error)
      );
    }
  }
  updateBook(book:Book){
    this.bDisplayUpdateData=true;
    this.bDisplayAddData=false;
    this.addOrUpdateDisplay="Update Book"
    this.book=book;
  }
  deleteBook(book_id:number){
    this.crudService.deleteBook(book_id).subscribe(
      (response) =>{alert("Record deleted successfully..");this.getBookData()},
        (error)=>console.log(error)
    );
  }
}
