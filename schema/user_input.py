from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities


class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the customer")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the customer")]
    height: Annotated[
        float, Field(..., gt=0, lt=2.5, description="height of the customer in mtr")
    ]
    income_lpa: Annotated[float, Field(..., description="Income of the customer")]
    smoker: Annotated[
        bool, Field(..., description="Whether the customer is a smoker or not")
    ]
    city: Annotated[
        str, Field(..., description="The city from where the customer belongs from")
    ]
    occupation: Annotated[
        Literal[
            "retired",
            "freelancer",
            "student",
            "government_job",
            "business_owner",
            "unemployed",
            "private_job",
        ],
        Field(..., description="The occupation of the customer"),
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        else:
            return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

    @field_validator("city")  # type: ignore
    @classmethod
    def normalize_city(cls, value: str) -> str:
        value = value.strip().title()
        return value
