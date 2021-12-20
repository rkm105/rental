import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "components"))

from flask import Flask, request, url_for
from markupsafe import escape
from werkzeug.exceptions import ExpectationFailed
from components import vehicle
from components import rental
from components import customer

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = "/api/v1"

@app.route('/')
def get_available_vehicle_list():
    return vehicle.get_vehicle_list()[1]


@app.route('/customers', methods=["GET"])
def get_customer_list():
    return {"customer_names": customer.fetch_customer_names()[1]}


@app.route('/customer/<email>', methods=['GET'])
def get_customer_detail(email):
    return customer.fetch_customer_detail(escape(email))[1]


@app.route('/customer/register/', methods=['POST'])
def register_customer_details():
    """
    Required form:
        name: name of the customer
        contact: contact number of the customer
        email: email id of the customer
    """
    data = request.form.to_dict()
    try:
        return customer.register({
            "name": data["name"],
            "contact": data["contact"],
            "email": data["email"]
        })[1]
    except KeyError as e:
        return "Proper data not present"


@app.route('/customer/unregister/<email>', methods=['DELETE'])
def unregister_customer(email):
    return customer.unregister(escape(email))[1]


@app.route('/rent', methods=['PUT'])
def rent_vehicle():
    """
    Required inputs in form:
    - vehicle: "Type of vehicle"
    - email: "Registered vehicle id"
    """
    data = request.form.to_dict()
    try:
        return rental.rent_vehicle(vehicle_type=data["vehicle"], email=data["email"])[1]
    except KeyError as e:
        return "Proper data not present"


@app.route('/rent/return', methods=['PUT'])
def return_vehicle():
    """
    Required inputs:
    - vehicle: "Type of vehicle"
    - vehicle_id: "Registration id of the vehicle"
    - email: "Registered email id of the customer"
    """
    data = request.form.to_dict()
    try:
        return rental.return_vehicle(vehicle_type=data["vehicle"], vehicle_id=data["vehicle_id"], email=data["email"])[1]
    except KeyError as e:
        return "Proper data not present."


@app.route('/rent/<email>')
def get_rent_history(email):
    """
    Get the rent history of the given email
    """
    return {"Rental History": rental.get_rental_history(email)[1]}


app.run(host = "0.0.0.0")

"""
curl -kv -X POST --data "name=Rahul Mittal" -d "email=rahulmittal1005@gmail.com" -d "contact=7xxxxxxx97" http://localhost:5000/customer/register/
"""