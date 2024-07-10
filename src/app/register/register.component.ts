import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {
  username: string="";
  firstname: string="";
  lastname: string="";
  emailid: string="";
  password: string="";
  constructor(private authService: AuthService,private router: Router){}
  register() {
    this.authService.register({username:this.username,
      firstname:this.firstname,
      lastname:this.lastname,
      emailid:this.emailid,
      password:this.password}).subscribe(
      (response:any) => {
        if(response.message === "Missing details") {
          alert("All fields are required");}
        else if(response.message === "User registered successfully") {
          alert("User registered successfully");
          this.router.navigate(['/login']);}
        else {
          alert ("Register user already exists");
        }
      });
  } 
}
