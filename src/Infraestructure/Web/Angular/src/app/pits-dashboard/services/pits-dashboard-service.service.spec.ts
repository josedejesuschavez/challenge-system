import { TestBed } from '@angular/core/testing';

import { PitsDashboardServiceService } from './pits-dashboard-service.service';

describe('PitsDashboardServiceService', () => {
  let service: PitsDashboardServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PitsDashboardServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
