import { Component, Input, OnInit } from '@angular/core';
import { TeamMemberDTO } from '../team-member-dto';

@Component({
  selector: 'app-grid-team-members',
  templateUrl: './grid-team-members.component.html',
  styleUrls: ['./grid-team-members.component.sass']
})
export class GridTeamMembersComponent implements OnInit {
  @Input() teamMembers: Array<TeamMemberDTO> | undefined;

  constructor() { }

  ngOnInit(): void {
  }

}
