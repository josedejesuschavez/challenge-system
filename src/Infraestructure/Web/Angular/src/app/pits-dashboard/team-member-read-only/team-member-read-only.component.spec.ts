import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamMemberReadOnlyComponent } from './team-member-read-only.component';

describe('TeamMemberReadOnlyComponent', () => {
  let component: TeamMemberReadOnlyComponent;
  let fixture: ComponentFixture<TeamMemberReadOnlyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TeamMemberReadOnlyComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TeamMemberReadOnlyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
