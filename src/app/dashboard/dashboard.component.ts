import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import { Appointments } from '../Appointments';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {
  imgSrc1 : String = "img8.jpeg";

  constructor(private authService:AuthService,private router:Router){}  
  bDisplayHome:boolean=false;
  bDisplayServices:boolean=false;
  login(){
    this.router.navigate(['/login']);
  }
  home(){
    this.bDisplayHome=true;
    this.bDisplayAddData=false;
    this.bDisplayAppData=false;
    this.bDisplayUpdateData=false;
    this.bDisplayServices=false;
  }
  services(){
    this.bDisplayServices=true;
    this.bDisplayAddData=false;
    this.bDisplayAppData=false;
    this.bDisplayUpdateData=false;
    this.bDisplayHome=false;

  }

  appList:any=[];
  bDisplayAppData: boolean=false
  getAppData(){
    this.bDisplayAppData=true
    this.bDisplayHome=false
    this.bDisplayServices=false
    this.authService.getAppData().subscribe(
      (response) => {this.appList = response;},
      (error) => console.log(error));
  }
  bDisplayAddData : boolean =false;
  bDisplayUpdateData : boolean =false;
  addOrUpdateDisplay : String ="";
  appointment = new Appointments(0,"","","","");
  bookAppointment(){
    this.bDisplayAddData=true;
    this.bDisplayHome=false
    this.bDisplayServices=false
    this.addOrUpdateDisplay="Book Appointment"
    this.appointment = new Appointments(0,"","","","");
  }
  updateAppointment(appointment:Appointments){
    this.bDisplayUpdateData=true;
    this.bDisplayAddData=false;
    this.bDisplayHome=false
    this.bDisplayServices=false
    this.addOrUpdateDisplay="Update Appointment";
    this.appointment=appointment;
  }
  createOrUpdateData(){
    if(this.addOrUpdateDisplay=="Book Appointment"){
      this.bDisplayAddData=false;
      this.bDisplayHome=false
      this.bDisplayServices=false
      this.authService.createAppointment(this.appointment).subscribe((response:any) => {
        if (response.message === "Missing details")
          {alert("Enter all required fields");this.bookAppointment();}
        else if (response.message === "Slot not available")
          {alert("This slot is not available..Please choose another slot..");this.bookAppointment();}
        else
          {alert("Appointment booked successfully.."); this.getAppData();}
      });
    }
    else if(this.addOrUpdateDisplay=="Update Appointment"){
      this.bDisplayUpdateData=false;
      this.bDisplayHome=false
      this.bDisplayServices=false
      this.authService.updateAppointment(this.appointment).subscribe((response:any) => {
        if (response.message==="Slot not available")
          {alert("This slot is not available..Please choose another slot..");this.updateAppointment(this.appointment);}
        else
        {alert("Appointment details updated successfully.."); this.getAppData();}
      });
    }
  }
  deleteAppointment(id:number){
    this.authService.deleteAppointment(id).subscribe(
      (response)=> {alert("Appointment cancelled successfully.."); this.getAppData();},
      (error) => console.log(error));
  }
}
