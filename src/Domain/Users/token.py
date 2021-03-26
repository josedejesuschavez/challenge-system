from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: str
    token: str
    user_name: str