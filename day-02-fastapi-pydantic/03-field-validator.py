from pydantic import BaseModel, field_validator, EmailStr

class Candidate(BaseModel):
    name: str
    email: EmailStr

    @field_validator("name") #Tells Pydantic to run this function when validating the name field.
    @classmethod
    def validate_name(cls, value): # value: Contains the actual value being validated.
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters")

        return value


candidate = Candidate(
    name="ekjot",
    email="sample@gmail.com"
)

print(candidate)