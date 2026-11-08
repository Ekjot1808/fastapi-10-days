from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr, field_validator

app = FastAPI()

candidates = []

# Models
class Education(BaseModel):
    degree: str
    university: str
    year: int = Field(ge=2000, le=2035)

class CandidateCreate(BaseModel):
    name: str = Field(min_length=3)
    email: EmailStr
    age: int = Field(ge=18, le=60)
    education: Education
    skills: list[str]
    password: str = Field(min_length=8)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name can only contain letters")
        
        return value
    
    
class CandidateResponse(BaseModel):
    id: int
    name: str = Field(min_length=3)
    email: EmailStr
    age: int = Field(ge=18, le=60)
    education: Education
    skills: list[str]

# Endpoints

@app.post("/candidates", response_model=CandidateResponse, status_code=status.HTTP_201_CREATED)
def create_candidate(candidate: CandidateCreate):
    new_candidate = {
        "id": len(candidates) + 1,
        **candidate.model_dump(exclude={"password"})
    }

    candidates.append(new_candidate)

    return new_candidate


@app.get("/candidates", response_model=list[CandidateResponse])
def get_candidates():
    return candidates


@app.get("/candidates/{candidate_id}")
def search_candidate(candidate_id: int):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate

    raise HTTPException(
        status_code=404,
        detail="Candidate not found"
    )