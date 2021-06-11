from dataclasses import dataclass

@dataclass
class Address:
    line1: str
    line2: str
    city: str
    province_state: str
    postal_code: str
    country: str
