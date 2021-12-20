# Driver script for the rent requests

from . import data_handle
from constants import *
from . import customer
from . import vehicle

add_obj = data_handle.add()
fetch_obj = data_handle.fetch()
delete_obj = data_handle.delete()

def rent_vehicle(vehicle_type: str, email: str)-> tuple[int, str]:
    """
    This script will rent the vehicle and add it in customer's entry
    Required:
        vehicle_type: type of vehicle rented
        email: id of the customer
    Returns the registeration id of the vehicle
    """
    ret, reg_id = vehicle.rent_vehicle(vehicle_type)
    if ret == 0:
        ret, out = customer.allocate_rent(email, vehicle_type, reg_id)
        if ret == 0:
            return 0, reg_id
        return ret, out
    return ret, reg_id


def return_vehicle(vehicle_id: str, vehicle_type: str, email: str):
    """
    This script will return the vehicle, unregister it from customer's rents and add a rental history for it
    """
    ret, out = customer.deallocate_rent(email, vehicle_id)
    if not ret == 0:
        return ret, out
    ret, out = vehicle.return_vehicle(vehicle_type, vehicle_id)
    return ret, out


def get_rental_history(email:str)-> tuple[int, dict]:
    """
    Return the rental history of the given email
    """
    ret, out = fetch_obj.get_data(file=RENT_HISTORY_FILE, key=email)
    # ret, out = data_handle.get_data(file=RENT_HISTORY_FILE, key=email)
    if ret == 0:
        return 0, out.get('Rental History')
    else:
        return ret, out

