import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  
  constructor(private authService: AuthService, private router: Router){}
  username: String= "";
  password: String= "";

  login() {
    this.authService.login(this.username,this.password).subscribe(
      (response: any) => {
        console.log("Login respone:", response);
        if(response.message === "Username or password is missing"){ alert("All fields are required"); }
        else if(response.message === "Login successful"){ alert("Login successful");
            this.router.navigate(['/dashboard']); 
        }
        else {alert("Username or password is incorrect");}
      }
    );
  }
}
