from pydantic import BaseModel,EmailStr #EmailStr is a speacial type for email validation that comes from pydantic
from pydantic import Field #Field is used to provide additional information about the field
from typing import Optional
class Student(BaseModel):
    name : str
    #name : str = 'avis' # default value
    age :Optional[int] = None # Optional field
    email:EmailStr # Email field
    #field function
    cgpa : float = Field(lt = 10, gt=0,default=8,description="obtained grade in each subject and its cummulative value , full form is cummulative gpa") # lt = less than, gt = greater than, default = default value
     
# newStudent = {'name':'avi'}
newStudent = {'name':'avi','age':'36','cgpa':8} # i have provided age as string, but pydantic is smart enough and convert it to integer hence this is called as type coercion(i.e implicit type conversion)

student = Student(**newStudent) 

print(student)