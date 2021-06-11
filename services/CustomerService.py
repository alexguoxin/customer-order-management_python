import json

from utils import customer_to_dict

class CustomerService:
    def __init__(self, file_path):
        self.file_path = file_path


    def create_customer(self, customer):
        customers = self.load()
        if customer.id in customers.keys():
            raise ValueError("This customer ID already exists. Please create a new one.")
        customers[customer.id] = customer_to_dict(customer)
        self.save(customers)


    def search_customer(self, customer_id):
        customers = self.load()
        if customer_id not in customers.keys():
            raise KeyError("This customer does not exist.")
        return customers[customer_id]


    def update_customer(self, customer):
        customers = self.load()
        if customer.id not in customers.keys():
            raise KeyError("This customer does not exist.")
        customers[customer.id] = customer_to_dict(customer)
        self.save(customers)


    def delete_customer(self, customer_id):
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
