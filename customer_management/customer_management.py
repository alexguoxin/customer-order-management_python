from flask import render_template, request, redirect, url_for, flash, jsonify, Blueprint
import json
import os.path

bp = Blueprint('customer_management', __name__)

@bp.route('/')
def home():
    return render_template('home.html')


@bp.route('/create', methods=['POST'])
def create():
    customer_id = request.form['customer_id']
    customers = {}

    if os.path.exists('customers.json'):
        with open('customers.json') as customer_file:
            customers = json.load(customer_file)

    if customer_id in customers.keys():
        flash('This customer ID already exists. Please create a new one.')
        return redirect(url_for('customer_management.home'))

    customers[customer_id] = {
        'first_name': request.form['first_name'], 
        'last_name': request.form['last_name'],
        'company': request.form['company'],
        'address': request.form['address'],
        'sign_up_date': request.form['sign_up_date'],
        'email': request.form['email']
        }

    with open('customers.json', 'w') as customer_file:
        json.dump(customers, customer_file)

    return 'Customer ' + customer_id + ' has been created.'


@bp.route('/search')
def search():
    if os.path.exists('customers.json'):
        with open('customers.json') as customer_file:
            customers = json.load(customer_file)

        customer_id = request.args['customer_id']
        
        if customer_id in customers.keys():
            return render_template(
                'home.html', 
                customer_id=customer_id,
                first_name=customers[customer_id]['first_name'], 
                last_name=customers[customer_id]['last_name'], 
                company=customers[customer_id]['company'], 
                address=customers[customer_id]['address'], 
                sign_up_date=customers[customer_id]['sign_up_date'], 
                email=customers[customer_id]['email'])
        else:
            flash('This customer does not exist.')
            return redirect(url_for('customer_management.home'))
    else:
        flash('No customer has been created yet.')
        return redirect(url_for('customer_management.home'))


@bp.route('/update', methods=['POST'])
def update():
    if os.path.exists('customers.json'):
        with open('customers.json') as customer_file:
            customers = json.load(customer_file)

        customer_id = request.form['customer_id']
        
        if customer_id in customers.keys():
            customers[customer_id]['first_name'] = request.form['first_name']
            customers[customer_id]['last_name'] = request.form['last_name']
            customers[customer_id]['company'] = request.form['company']
            customers[customer_id]['address'] = request.form['address']
            customers[customer_id]['sign_up_date'] = request.form['sign_up_date']
            customers[customer_id]['email'] = request.form['email']
        else:
            flash('This customer does not exist.')
            return redirect(url_for('customer_management.home'))

        with open('customers.json', 'w') as customer_file:
            json.dump(customers, customer_file)

        return "Customer " + customer_id + "'s info has been updated."
    else:
        flash('No customer has been created yet.')
        return redirect(url_for('customer_management.home'))


@bp.route('/delete', methods=['POST'])
def delete():
    if os.path.exists('customers.json'):
        with open('customers.json') as customer_file:
            customers = json.load(customer_file)

        customer_id = request.form['customer_id']
        
        if customer_id in customers.keys():
            del customers[customer_id]
        else:
            flash('This customer does not exist.')
            return redirect(url_for('customer_management.home'))

        with open('customers.json', 'w') as customer_file:
            json.dump(customers, customer_file)

        return "Customer " + customer_id + " has been deleted."
    else:
        flash('No customer has been created yet.')
        return redirect(url_for('customer_management.home'))


@bp.route('/api/search')
def api_search():
    if os.path.exists('customers.json'):
        with open('customers.json') as customer_file:
            customers = json.load(customer_file)

        customer_id = request.args['customer_id']
        
        if customer_id in customers.keys():
            return jsonify(customers[customer_id])
        else:
            return 'This customer does not exist.'
    else:
        return 'No customer has been created yet.'
