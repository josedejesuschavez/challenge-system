import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PitsDashboardComponent } from './pits-dashboard.component';

describe('PitsDashboardComponent', () => {
  let component: PitsDashboardComponent;
  let fixture: ComponentFixture<PitsDashboardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PitsDashboardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PitsDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
