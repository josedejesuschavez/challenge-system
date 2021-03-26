from dataclasses import dataclass


@dataclass(frozen=True)
class TeamMember:
    active_mt: bool
    current_team: str
    date_start_team: str
    available_ops: bool
    email: str
    english: int
    full_name: str
    link_cv: str
    location: str
    main_1: str
    main_1_score: int
    main_2: str
    main_2_score: int
    next_team: str
    next_tech_secondary: str
    notes: str
    role: str
    secondary_1: str
    secondary_1_score: int
    secondary_2: str
    secondary_2_score: int
    secondary_3: str
    secondary_3_score: int
    target_tech_main: str
    techSkill: str