from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os.path
import json

from model.Customer import Customer
from model.Address import Address
from services.CustomerService import CustomerService

def create_app():
    app = Flask(__name__)
    app.secret_key = 'voa87dy8p9wdep9aw'
    customer_file_path = 'customers.json'

    if not os.path.exists(customer_file_path):
        with open(customer_file_path, 'w') as customer_file:
            json.dump({}, customer_file)

    customer_service = CustomerService(customer_file_path)


    @app.route('/')
    def home():
        return render_template('home.html')


    @app.route('/create', methods=['POST'])
    def create():
        customer_id = request.form['customer_id']
        new_customer = Customer(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            company=request.form['company'],
            sign_up_date=request.form['sign_up_date'],
            email=request.form['email'],
            address=Address(
                request.form['line1'],
                request.form['line2'],
                request.form['city'],
                request.form['province_state'],
                request.form['postal_code'],
                request.form['country'],
            )
            )

        try:
            customer_service.create(customer_id, new_customer)
            return 'Customer ' + customer_id + ' has been created.'
        except ValueError:
            flash('This customer ID already exists. Please create a new one.')
            return redirect(url_for('home'))

    

    @app.route('/search', methods=['GET'])
    def search():
        customer_id = request.args['customer_id']
        try:
            result = customer_service.search(customer_id)
            return render_template(
                'home.html', 
                customer_id=customer_id,
                first_name=result['first_name'], 
                last_name=result['last_name'], 
                company=result['company'], 
                sign_up_date=result['sign_up_date'], 
                email=result['email'],
                line1=result['address']['line1'],
                line2=result['address']['line2'],
                city=result['address']['city'],
                province_state=result['address']['province_state'],
                postal_code=result['address']['postal_code'],
                country=result['address']['country'])
        except KeyError:
            flash('This customer does not exist.')
            return redirect(url_for('home'))


    @app.route('/update', methods=['POST'])
    def update():
        customer_id = request.form['customer_id']
        updated_customer = Customer(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            company=request.form['company'],
            sign_up_date=request.form['sign_up_date'],
            email=request.form['email'],
            address=Address(
                request.form['line1'],
                request.form['line2'],
                request.form['city'],
                request.form['province_state'],
                request.form['postal_code'],
                request.form['country'],
            )
            )

        try:
            customer_service.update(customer_id, updated_customer)
            return "Customer " + customer_id + "'s info has been updated."
        except KeyError:
            flash('This customer does not exist.')
            return redirect(url_for('home'))


    @app.route('/delete', methods=['POST'])
    def delete():
            customer_id = request.form['customer_id']
            try:
                customer_service.delete(customer_id)
                return "Customer " + customer_id + " has been deleted."
            except KeyError:
                flash('This customer does not exist.')
                return redirect(url_for('home'))

            
    @app.route('/api/search')
    def api_search():
            customer_id = request.args['customer_id']
            try:
                result = customer_service.search(customer_id)
                return jsonify(result)
            except KeyError:
                return 'This customer does not exist.'


    return app
