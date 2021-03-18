import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LogInModule } from './log-in/log-in.module';
import { PitsDashboardModule } from './pits-dashboard/pits-dashboard.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    LogInModule,
    PitsDashboardModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
