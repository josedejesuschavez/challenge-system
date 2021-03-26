import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LogInServiceService {

  constructor(private http: HttpClient) { }

  autenticate(email: any, password: any){
    const user = { email, password}

    return this.http.post("http://localhost:5000/auth/login", user)
  }
}
