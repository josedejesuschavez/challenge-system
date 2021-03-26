import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { TeamMemberDTO } from '../team-member-dto';

@Injectable({
  providedIn: 'root'
})
export class PitsDashboardServiceService {

  constructor(private http: HttpClient) { }

  getTeamMembers() {
    let headers = new HttpHeaders()
          .set('Authorization', 'Bearer ' + localStorage.getItem('token'))
    
    return this.http.get("http://localhost:5000/pits/teammembers", { headers })
  }

  addTeamMembers(teamMember: TeamMemberDTO) {
    teamMember.active_mt = teamMember.active_mt ? 1: 0
    teamMember.available_ops = teamMember.available_ops ? 1: 0
    let headers = new HttpHeaders()
          .set('Authorization', 'Bearer ' + localStorage.getItem('token'))
    
    return this.http.post("http://localhost:5000/pits/teammember", teamMember, { headers })
  }

  updateTeamMembers(teamMember: TeamMemberDTO) {
    teamMember.active_mt = teamMember.active_mt ? 1: 0
    teamMember.available_ops = teamMember.available_ops ? 1: 0
    let headers = new HttpHeaders()
          .set('Authorization', 'Bearer ' + localStorage.getItem('token'))
    
    return this.http.put("http://localhost:5000/pits/teammember", teamMember, { headers })
  }

  deleteTeamMembers(id: string) {
    let headers = new HttpHeaders()
          .set('Authorization', 'Bearer ' + localStorage.getItem('token'))
    
    return this.http.delete("http://localhost:5000/pits/teammember/" + id, { headers })
  }
}
