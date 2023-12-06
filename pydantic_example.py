from pydantic import BaseModel,ValidationError, Field


# class User(BaseModel):
#     name: str
#     surname: str
#
#
# data_dict = {"name": "John", "surname": "Doe"}
# user = User(**data_dict)
# print(user)
# print(user.json())
# print(user.dict())

class User(BaseModel):
    name: str
    surname: str
    age: int

data_dict = {"name": "John", "surname": "Doe"}
try:
    user = User(**data_dict)
except ValidationError as e:
    print(e)

# print(user)
print(user.json())
print(user.dict())


