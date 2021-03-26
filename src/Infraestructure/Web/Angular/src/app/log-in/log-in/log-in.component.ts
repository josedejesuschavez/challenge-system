import { Component, OnInit } from '@angular/core';
import { LogInServiceService } from '../services/log-in-service.service';
import { FormGroup, FormControl } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.sass']
})
export class LogInComponent implements OnInit {

  response: any
  logInForm = new FormGroup({
    email: new FormControl(''),
    password: new FormControl('')
  });

  constructor(private router: Router, private logInServiceService: LogInServiceService) { }

  ngOnInit(): void {
  }

  onSubmit() {
    this.logInServiceService.autenticate(this.logInForm.value.email, this.logInForm.value.password).subscribe(result=>{
      debugger
      this.response = result
      localStorage.setItem('token', this.response.token)
      this.router.navigate(['/pitsDashboard']);
    })
  }

}
