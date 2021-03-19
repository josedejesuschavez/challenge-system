import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./log-in/log-in.module').then(m => m.LogInModule)
  },
  {
    path: 'login',
    loadChildren: () => import('./log-in/log-in.module').then(m => m.LogInModule)
  },
  {
    path: 'pitsDashboard',
    loadChildren: () => import('./pits-dashboard/pits-dashboard.module').then(m => m.PitsDashboardModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
