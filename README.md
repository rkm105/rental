# Rental App

A small self made project keeping a rental hub in mind. This provides an api to register a customer, rent a vehicle among available ones and return the vehicle.

## How to use:

1. Create the docker image using command: `docker build -t rental:1.0 .`
2. Run the docker container using `docker compose up`

Refer rental_api.yml for the api structure.
Example:
- Run following command: 

`curl -kv -X POST --data "name=Rahul Mittal" -d "email=rahul@gmail.com" -d "contact=xxxxxxxx97" http://127.0.0.1:5000/customer/register/`

## Version:

- 1.0 -
    Basic flask based api using json file to store the data
