import { Component, ElementRef, EventEmitter, Input, OnInit, Output, ViewChild } from '@angular/core';
import { TeamMemberDTO } from '../team-member-dto';

@Component({
  selector: 'app-grid-team-members',
  templateUrl: './grid-team-members.component.html',
  styleUrls: ['./grid-team-members.component.sass']
})
export class GridTeamMembersComponent implements OnInit {
  @Input() teamMembers: Array<TeamMemberDTO> | undefined;
  @Output() teamMemberSelected: EventEmitter<TeamMemberDTO> = new EventEmitter()
  @Output() teamMemberDelete: EventEmitter<TeamMemberDTO> = new EventEmitter()
  currentPage: number = 1
  pageSize: number = 5
  totalItems: number | undefined

  constructor() {

  }

  ngOnInit(): void {
  }

  onClickEditTeamMember(team_member: TeamMemberDTO) {
    this.teamMemberSelected.emit(team_member)
  }

  onClickDeleteTeamMember(team_member: TeamMemberDTO) {
    this.teamMemberDelete.emit(team_member)
  }

  onClickNewTeamMember() {
    this.teamMemberSelected.emit(new TeamMemberDTO())
  }
}
