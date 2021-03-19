import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LogInModule } from './log-in/log-in.module';
import { PitsDashboardModule } from './pits-dashboard/pits-dashboard.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    LogInModule,
    PitsDashboardModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
