from model.Customer import Customer
from model.Address import Address

def dict_to_customer(dict):
    address = Address(
        line1=dict['line1'],
        line2=dict['line2'],
        city=dict['city'],
        province_state=dict['province_state'],
        postal_code=dict['postal_code'],
        country=dict['country']
        )

    return Customer(
        id=dict['customer_id'],
        first_name=dict['first_name'],
        last_name=dict['last_name'],
        company=dict['company'],
        sign_up_date=dict['sign_up_date'],
        email=dict['email'],
        address=address
        )

def customer_to_dict(customer):
    customer.address = customer.address.__dict__
    return customer.__dict__

