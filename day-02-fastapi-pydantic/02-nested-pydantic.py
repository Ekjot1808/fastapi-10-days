from pydantic import BaseModel

class Education(BaseModel):
    degree: str
    university: str
    year: int

class Candidate(BaseModel):
    name: str
    email: str
    education: Education

class JobApplication(BaseModel):
    application_id: int
    candidate: Candidate
    skills: list[str]


application = JobApplication(
    application_id=12,
    candidate={
        "name": "Ekjot",
        "email": "sample@gmail.com",
        "education": {
            "degree": "B-Tech",
            "university": "IIT Bombay",
            "year": 2027
        }
    },
    skills=["Python", "FastAPI", "Git & Github", "Js", "React", "MongoDB", "Postgres"]
)

print(application.candidate.education.year)