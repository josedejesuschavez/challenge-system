import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PitsDashboardComponent } from './pits-dashboard/pits-dashboard.component';
import { RouterModule, Routes } from '@angular/router';


const routes: Routes = [
  {
    path: '',
    component: PitsDashboardComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PitsDashboardModule { }
