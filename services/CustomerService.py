import json

class CustomerService:
    def __init__(self, file_path):
        self.file_path = file_path


    def create(self, customer_id, customer):
        customers = self.load()

        if customer_id in customers.keys():
            raise ValueError("This customer ID already exists. Please create a new one.")

        customer.address = customer.address.__dict__
        customers[customer_id] = customer.__dict__
        
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

        customer.address = customer.address.__dict__
        customers[customer_id] = customer.__dict__

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
