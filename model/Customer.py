from dataclasses import dataclass
from model import Address

@dataclass
class Customer:
    id: str
    first_name: str
    last_name: str 
    company: str
    address: Address
    sign_up_date: str
    email: str
