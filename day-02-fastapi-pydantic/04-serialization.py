from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    city: str
    college: str = "IIT"

student = Student(
    name="Ekjot",
    age=21,
    city="Patiala"
)

data = student.model_dump(exclude="city") # converts into dictionary, and also perform normal dict tasks like exclude dict
# include={"name", "age"}
data2 = student.model_dump(exclude_unset=True) # it dont show default set field

json_data = student.model_dump_json()

print(json_data)
print(type(json_data))

# print(data)
# print(data2)

"""Dictionary to Pydantic Object"""
data = {
    "name": "Ekjot",
    "age": 21,
    "city": "London"
}

data_json = """
{
    "name": "Ekjot",
    "age": 21,
    "city": "London"
}
"""

student2 = Student.model_validate(data) #converts dict inot pydantic object
student3 = Student.model_validate_json(data_json) # converts json to pydantic object

print(student2)
print(student3)