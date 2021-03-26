import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { PitsDashboardServiceService } from '../services/pits-dashboard-service.service';
import { TeamMemberDTO } from '../team-member-dto';

@Component({
  selector: 'app-modal-edit-team-member',
  templateUrl: './modal-edit-team-member.component.html',
  styleUrls: ['./modal-edit-team-member.component.sass']
})
export class ModalEditTeamMemberComponent implements OnInit {
  @Input() teamMember: TeamMemberDTO | undefined;
  @Output() modalActionCompleted: EventEmitter<string> = new EventEmitter()

  teamMemberForm = new FormGroup({
    id: new FormControl(''),
    active_mt: new FormControl(''),
    current_team: new FormControl(''),
    date_start_team: new FormControl(''),
    available_ops: new FormControl(''),
    email: new FormControl(''),
    english: new FormControl(''),
    full_name: new FormControl(''),
    link_cv: new FormControl(''),
    location: new FormControl(''),
    main_1: new FormControl(''),
    main_1_score: new FormControl(''),
    main_2: new FormControl(''),
    main_2_score: new FormControl(''),
    next_team: new FormControl(''),
    next_tech_secondary: new FormControl(''),
    notes: new FormControl(''),
    role: new FormControl(''),
    secondary_1: new FormControl(''),
    secondary_1_score: new FormControl(''),
    secondary_2: new FormControl(''),
    secondary_2_score: new FormControl(''),
    secondary_3: new FormControl(''),
    secondary_3_score: new FormControl(''),
    target_tech_main: new FormControl(''),
    techSkill: new FormControl('')
  });
  
  constructor(private pitsDashboardServiceService: PitsDashboardServiceService) { }

  ngOnInit(): void {
  }

  onSubmit() {
    const teamMember = this.teamMemberForm.value

    if (teamMember.id != '') {
      this.pitsDashboardServiceService.updateTeamMembers(teamMember).subscribe(result=>{
        this.modalActionCompleted.emit('complete')
      })
    }
    else {
      this.pitsDashboardServiceService.addTeamMembers(teamMember).subscribe(result=>{
        this.modalActionCompleted.emit('complete')
      })
    }
  }
}
