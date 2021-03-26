import { Component, Input, OnInit } from '@angular/core';
import { TeamMemberDTO } from '../team-member-dto';

@Component({
  selector: 'app-pagination',
  templateUrl: './pagination.component.html',
  styleUrls: ['./pagination.component.sass']
})
export class PaginationComponent implements OnInit {
  @Input() currentPage: number | undefined
  @Input() pageSize: number | undefined
  @Input() items: Array<TeamMemberDTO> | undefined;
  
  constructor() { }

  ngOnInit(): void {
    console.log(this.items?.length)
    debugger
  }

}
