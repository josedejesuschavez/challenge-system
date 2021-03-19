import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PitsDashboardComponent } from './pits-dashboard/pits-dashboard.component';
import { RouterModule, Routes } from '@angular/router';
import { TeamMemberReadOnlyComponent } from './team-member-read-only/team-member-read-only.component';


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
    TeamMemberReadOnlyComponent
  ]
})
export class PitsDashboardModule { }
