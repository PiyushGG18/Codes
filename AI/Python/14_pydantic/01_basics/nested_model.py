from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="123, something",
    city="Amravati",
    postal_code="123456",
)

user = User(
    id=1,
    name="Piyush",
    address=address
)

user_data = {
    "id": 1,
    "name": "Piyush",
    "address" : {
        "street": "321, something",
        "city": "Paris",
        "postal_code": "123098"
    }
}

user = User(**user_data)
print(user)