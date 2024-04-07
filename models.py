from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float


class Address(BaseModel):
    city: str
    country: str



class Student(BaseModel):
    name: str
    age: int
    address: Address
