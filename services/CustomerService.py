import json

from model.Customer import Customer

class CustomerService:
    def __init__(self, file_path):
        self.file_path = file_path


    def create(self, customer_id, customer):
        customers = self.load()

        if customer_id in customers.keys():
            raise ValueError("This customer ID already exists. Please create a new one.")

        customers[customer_id] = {
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "company": customer.company,
            "address": customer.address,
            "sign_up_date": customer.sign_up_date,
            "email": customer.email
        }

        self.save(customers)


    def search(self, customer_id):
        customers = self.load()
        if customer_id not in customers.keys():
            raise KeyError("This customer does not exist.")
        return customers[customer_id]


    def update(self, customer_id, customer):
        customers = self.load()

        if customer_id not in customers.keys():
            raise KeyError("This customer does not exist.")
        
        customers[customer_id] = {
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "company": customer.company,
            "address": customer.address,
            "sign_up_date": customer.sign_up_date,
            "email": customer.email
        }

        self.save(customers)


    def delete(self, customer_id):
        customers = self.load()
        if customer_id not in customers.keys():
            raise KeyError("This customer does not exist.")
        del customers[customer_id]
        self.save(customers)


    def load(self):
        with open(self.file_path) as customer_file:
            return json.load(customer_file)


    def save(self, data):
        with open(self.file_path, 'w') as customer_file:
            json.dump(data, customer_file)
