from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id=1,
    name="Piyush",
    email="piyush@gmail.com",
    createdAt=datetime(2026, 5, 4, 21, 38),
    address=Address (
        street="Something",
        city="AMT",
        zip_code="123456",
    ),
    is_active=False,
    tags=["premium","subscriber"]
)

python_dict = user.model_dump();
print(user)
print("="*30)
print(python_dict)
print("="*30)
json_str=user.model_dump_json()
print(json_str)