import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalEditTeamMemberComponent } from './modal-edit-team-member.component';

describe('ModalEditTeamMemberComponent', () => {
  let component: ModalEditTeamMemberComponent;
  let fixture: ComponentFixture<ModalEditTeamMemberComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ModalEditTeamMemberComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ModalEditTeamMemberComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
