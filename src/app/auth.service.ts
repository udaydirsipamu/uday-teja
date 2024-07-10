import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError } from 'rxjs';
import { Appointments } from './Appointments';

@Injectable({
  providedIn: 'root'
})
export class AuthService {


  baseURL = 'http://localhost:5000';
  constructor(private httpClient: HttpClient) {}

  login(username:String, password:String):Observable<any>{
    return this.httpClient.post(`${this.baseURL}/login`,{username,password});
  }
  register(user: any):Observable<any>{
    return this.httpClient.post(`${this.baseURL}/reg`,user);
  }
  getAppData():Observable<any>{
    return this.httpClient.get(`${this.baseURL}/appointment`);
  }
  createAppointment(app:Appointments):Observable<any>{
    return this.httpClient.post(`${this.baseURL}/appointment`,app);
  }
  updateAppointment(app:Appointments):Observable<any>{
    return this.httpClient.put(`${this.baseURL}/appointment/${app.id}`,app);
  }
  deleteAppointment(id:number):Observable<any>{
    return this.httpClient.delete(this.baseURL+"/appointment/"+id);
  }

}
