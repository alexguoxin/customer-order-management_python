import json

class Customers():
    def __init__(self, file_path):
        with open(file_path) as customer_file:
            self.data = json.load(customer_file)

    def create(self, customer_id, first_name, last_name, company, address, sign_up_date, email):
        self.data[customer_id] = {
            'first_name': first_name, 
            'last_name': last_name,
            'company': company,
            'address': address,
            'sign_up_date': sign_up_date,
            'email': email
            }

    def search(self, customer_id):
        return self.data[customer_id]

    def update(self, customer_id, first_name, last_name, company, address, sign_up_date, email):
        self.data[customer_id]['first_name'] = first_name
        self.data[customer_id]['last_name'] = last_name
        self.data[customer_id]['company'] = company
        self.data[customer_id]['address'] = address
        self.data[customer_id]['sign_up_date'] = sign_up_date
        self.data[customer_id]['email'] = email

    def delete(self, customer_id):
        del self.data[customer_id]

    def save(self, file_path):
        with open(file_path, 'w') as customer_file:
            json.dump(self.data, customer_file)
