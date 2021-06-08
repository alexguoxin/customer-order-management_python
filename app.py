from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os.path
import json
from model import Customers

def create_app():
    app = Flask(__name__)
    app.secret_key = 'voa87dy8p9wdep9aw'
    customer_file_path = 'customers.json'

    if not os.path.exists(customer_file_path):
        with open(customer_file_path, 'w') as customer_file:
            json.dump({}, customer_file)

    customers = Customers(customer_file_path)


    @app.route('/')
    def home():
        return render_template('home.html')


    @app.route('/create', methods=['POST'])
    def create():
        customer_id = request.form['customer_id']

        if customer_id in customers.data.keys():
            flash('This customer ID already exists. Please create a new one.')
            return redirect(url_for('home'))
        else:
            customers.create(
                customer_id=customer_id,
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                company=request.form['company'],
                address=request.form['address'],
                sign_up_date=request.form['sign_up_date'],
                email=request.form['email']
            )

            customers.save(customer_file_path)

            return 'Customer ' + customer_id + ' has been created.'


    @app.route('/search', methods=['GET'])
    def search():
        customer_id = request.args['customer_id']

        if customer_id in customers.data.keys():
            result = customers.search(customer_id)

            return render_template(
                'home.html', 
                customer_id=customer_id,
                first_name=result['first_name'], 
                last_name=result['last_name'], 
                company=result['company'], 
                address=result['address'], 
                sign_up_date=result['sign_up_date'], 
                email=result['email'])
        else:
            flash('This customer does not exist.')
            return redirect(url_for('home'))


    @app.route('/update', methods=['POST'])
    def update():
        customer_id = request.form['customer_id']

        if customer_id in customers.data.keys():
            customers.update(
                customer_id=customer_id,
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                company=request.form['company'],
                address=request.form['address'],
                sign_up_date=request.form['sign_up_date'],
                email=request.form['email']
            )

            customers.save(customer_file_path)

            return "Customer " + customer_id + "'s info has been updated."
        else:
            flash('This customer does not exist.')
            return redirect(url_for('home'))
        

    @app.route('/delete', methods=['POST'])
    def delete():
            customer_id = request.form['customer_id']
            
            if customer_id in customers.data.keys():
                customers.delete(customer_id)
                customers.save(customer_file_path)
                return "Customer " + customer_id + " has been deleted."
            else:
                flash('This customer does not exist.')
                return redirect(url_for('home'))

            
    @app.route('/api/search')
    def api_search():
            customer_id = request.args['customer_id']
            
            if customer_id in customers.data.keys():
                return jsonify(customers.search(customer_id))
            else:
                return 'This customer does not exist.'

    return app