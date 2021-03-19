import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-pits-dashboard',
  templateUrl: './pits-dashboard.component.html',
  styleUrls: ['./pits-dashboard.component.sass']
})
export class PitsDashboardComponent implements OnInit {

  teamMembers = [
    {activo_mt:1, disponible_ops:0, location:'GDL', link_cv:'www.google.com', email:'a@correo.com', full_name:'Jose Chavez', role:'Dev', techSkill: 'Sr', english:10, current_team:'confie', next_team:'nexusfuel', date_start_team:'2020-05-02', main_1:'Python', main_1_score: 80, main_2:'.Net', main_2_score:79, secondary_1:'Python', secondary_1_score:90, secondary_2:'.Net', secondary_2_score:70, secondary_3:'Python', secondary_3_score:40, target_tech_main:'', next_tech_secondary:'', notes:'Vacaciones'},
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
