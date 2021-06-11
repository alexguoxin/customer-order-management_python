from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os.path
import json

from services.CustomerService import CustomerService
from utils import dict_to_customer

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
        new_customer = dict_to_customer(request.form)
        try:
            customer_service.create_customer(new_customer)
            return 'Customer {id} has been created.'.format(id=request.form["customer_id"])
        except ValueError:
            flash('This customer ID already exists. Please create a new one.')
            return redirect(url_for('home'))

    

    @app.route('/search', methods=['GET'])
    def search():
        try:
            result = customer_service.search_customer(request.args['customer_id'])
            return jsonify(result)
        except KeyError:
            flash('This customer does not exist.')
            return redirect(url_for('home'))


    @app.route('/update', methods=['POST'])
    def update():
        updated_customer = dict_to_customer(request.form)
        try:
            customer_service.update_customer(updated_customer)
            return "Customer {id}'s info has been updated.".format(id=request.form["customer_id"])
        except KeyError:
            flash('This customer does not exist.')
            return redirect(url_for('home'))


    @app.route('/delete', methods=['POST'])
    def delete():
            try:
                customer_service.delete_customer(request.form['customer_id'])
                return "Customer {id} has been deleted.".format(id=request.form['customer_id'])
            except KeyError:
                flash('This customer does not exist.')
                return redirect(url_for('home'))


    return app
