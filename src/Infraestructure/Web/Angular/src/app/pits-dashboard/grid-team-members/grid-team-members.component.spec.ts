import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GridTeamMembersComponent } from './grid-team-members.component';

describe('GridTeamMembersComponent', () => {
  let component: GridTeamMembersComponent;
  let fixture: ComponentFixture<GridTeamMembersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GridTeamMembersComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GridTeamMembersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
