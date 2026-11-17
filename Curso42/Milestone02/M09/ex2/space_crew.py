from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    # if the validator does not raise an error, it returns the class object.
    # the return type is the class name as text because when mypy first
    # reads it SpaceMission does not exist yet, but it indicates
    # that it returns a SpaceMission object
    @model_validator(mode='after')
    def mission_validator_rules(self) -> "SpaceMission":
        flag: bool = False
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        for member in self.crew:
            if (member.rank is Rank.CAPTAIN or
                    member.rank is Rank.COMMANDER):
                flag = True
            if not member.is_active:
                raise ValueError("All members must be active")
        if not flag:
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        if self.duration_days > 365:
            # count the crew members with 5 or more years of experience
            experienced: int = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1
            # at least half: experienced / total >= 0.5
            if experienced * 2 < len(self.crew):
                raise ValueError(
                    "Long missions need at least 50% experienced crew")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        # pydantic would also accept each crew member as a dict and
        # convert it into a CrewMember, but mypy would flag it as an error
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 7, 1, 8, 0),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(member_id="CM001", name="Sarah Connor",
                           rank=Rank.COMMANDER, age=45,
                           specialization="Mission Command",
                           years_experience=20),
                CrewMember(member_id="CM002", name="John Smith",
                           rank=Rank.LIEUTENANT, age=38,
                           specialization="Navigation",
                           years_experience=12),
                CrewMember(member_id="CM003", name="Alice Johnson",
                           rank=Rank.OFFICER, age=29,
                           specialization="Engineering",
                           years_experience=3),
            ],
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) - "
                  f"{member.specialization}")
    except ValidationError as e:
        print("Unexpected validation error:")
        print(e.errors()[0]["msg"])

    print("\n=========================================")
    try:
        # no commander or captain -> the model_validator fails
        SpaceMission(
            mission_id="M2025_MOON",
            mission_name="Lunar Survey",
            destination="Moon",
            launch_date=datetime(2027, 2, 15, 6, 30),
            duration_days=30,
            budget_millions=300.0,
            crew=[
                CrewMember(member_id="CM010", name="Bob Lee",
                           rank=Rank.LIEUTENANT, age=35,
                           specialization="Geology", years_experience=6),
                CrewMember(member_id="CM011", name="Eva Ruiz",
                           rank=Rank.OFFICER, age=27,
                           specialization="Medicine", years_experience=2),
            ],
        )
    except ValidationError as e:
        print("Expected validation error:")
        # the error comes from our ValueError: the clean text is in ctx
        print(e.errors()[0]["ctx"]["error"])


if __name__ == "__main__":
    main()
