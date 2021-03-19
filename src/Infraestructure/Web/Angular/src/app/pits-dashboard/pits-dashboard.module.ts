import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PitsDashboardComponent } from './pits-dashboard/pits-dashboard.component';
import { RouterModule, Routes } from '@angular/router';
import { TeamMemberReadOnlyComponent } from './team-member-read-only/team-member-read-only.component';
import { GridTeamMembersComponent } from './grid-team-members/grid-team-members.component';
import { PaginationComponent } from './pagination/pagination.component';
import { ModalEditTeamMemberComponent } from './modal-edit-team-member/modal-edit-team-member.component';


const routes: Routes = [
  {
    path: '',
    component: PitsDashboardComponent
  }
];

@NgModule({
  imports: [
    RouterModule.forChild(routes),
    CommonModule
  ],
  exports: [RouterModule],
  declarations: [
    PitsDashboardComponent,
    TeamMemberReadOnlyComponent,
    GridTeamMembersComponent,
    PaginationComponent,
    ModalEditTeamMemberComponent
  ]
})
export class PitsDashboardModule { }
