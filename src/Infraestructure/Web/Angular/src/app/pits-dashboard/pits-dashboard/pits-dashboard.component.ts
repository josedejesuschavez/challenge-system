import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { PitsDashboardServiceService } from '../services/pits-dashboard-service.service';
import { TeamMemberDTO } from '../team-member-dto';


@Component({
  selector: 'app-pits-dashboard',
  templateUrl: './pits-dashboard.component.html',
  styleUrls: ['./pits-dashboard.component.sass']
})
export class PitsDashboardComponent implements OnInit {

  teamMembers: any
  response: any
  teamMember: TeamMemberDTO | undefined
  @ViewChild('btn-close-form') btnCloseForm: ElementRef | undefined;


  constructor(private pitsDashboardServiceService: PitsDashboardServiceService) { }

  ngOnInit(): void {
    this.refreshFeature()
  }

  refreshFeature() {
    setTimeout(()=>{ 
      this.pitsDashboardServiceService.getTeamMembers().subscribe(result => {
        this.response = result
        this.teamMembers = this.response.team_members
      })
    }, 1000);
  }

  teamMemberSelected(teamMember: TeamMemberDTO) {
    this.teamMember = teamMember
  }

  teamMemberDelete(teamMember: TeamMemberDTO) {
    this.pitsDashboardServiceService.deleteTeamMembers(teamMember.id).subscribe(result=>{
      this.refreshFeature()
    })
  }

  modalActionCompleted(event: string) {
    let btnClose:HTMLElement= document.getElementById('btn-close-form') as HTMLElement
    btnClose.click()
    this.refreshFeature()
  }
}
