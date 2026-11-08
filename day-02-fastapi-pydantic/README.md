# FastAPI DAY - 2

Pydantic: Pydantic is a Python library that validates, parses, and serializes data using Python type annotations.

Important: Pydantic can perform type conversion
```
student = Student(
    name="Ekjot",
    age="21",
    city="London"
)
```

In Pydantic's default configuration, the string "21" can be converted into integer 21.But "hello" cannot be converted into an integer. This is called type **coercion.**

**Pydantic Serialization**
This is extremely important when working with FastAPI, databases, and GenAI applications.
- model_dump() # to dict
- model_dump_json() # to json
- model_validate() #dict -> pydantic object
- model_validate_json() #json -> pydantic object 

### What is serialization
This is a Python object, not a normal dictionary.

But sometimes you need to convert it into a dictionary or JSON to:
- Store data.
- Send data to another API.
- Return data from an endpoint.
- Work with databases.
This process is called serialization.

**What is Request body**: the data send by the frontend like: {
    "name": "Ekjot, 
    "email": "sample@gmail.com"
}

#### Exercise:
Day 2 – Candidate Registration API
Final practical
 Independent coding

1. What are we building?
A Candidate Registration API that allows users to register their professional profiles.

We'll use the same concepts that are useful in your HireMatch AI project.
2. Requirements
Three Pydantic models:
Model	Fields
Education	degree, university, year
CandidateCreate	name, email, age, education, skills, password
CandidateResponse	id, name, email, age, education, skills

Validation rules
- Name: minimum 3 characters.
- Email: valid email format.
- Age: between 18 and 60.
- Education year: between 2000 and 2035.
- Password: minimum 8 characters.
- Skills: list of strings.

API endpoints
```
________________________________________________________________
Method    | 	Endpoint                  |      Purpose
________________________________________________________________
POST	  |  /candidates	              |  Register candidate
GET	      |  /candidates	              |  Get all candidates
GET	      |  /candidates/{candidate_id}   |	Get candidate by ID
_________________________________________________________________
```