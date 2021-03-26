from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: str
    user_name: str
    password: str