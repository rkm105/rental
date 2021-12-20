# Services specific to the customer

from datetime import datetime
from . import data_handle
from constants import *

add_obj = data_handle.add()
fetch_obj = data_handle.fetch()
delete_obj = data_handle.delete()

def register(data: dict)-> tuple[int, str]:
    """
    Using email as the key 
    Required:
        data:{
            name
            contact
            email
        }
    """
    try:
        required_data = {
            "Contact": data["contact"],
            "Name": data["name"]
        }
        add_obj.create(CUSTOMER_ENTRY_FILE, key=data["email"], value=required_data)
        # data_handle.create(CUSTOMER_ENTRY_FILE, key=data["email"], value=required_data)
        return (0, "")
    except KeyError:
        return (DATA_ERROR_CODE, INCOMPLETE_DATA_ERROR.format(required_data))


def unregister(email: str)-> tuple[int, str]:
    """
    Unregister the customer if they want
    """
    if email:
        return delete_obj.unregister(CUSTOMER_ENTRY_FILE, email)
    return DATA_ERROR_CODE, INCOMPLETE_DATA_ERROR


def fetch_customer_names()-> tuple[int, list]:
    """
    Fetch complete list of customers
    """
    _, data = fetch_obj.get_all_data(CUSTOMER_ENTRY_FILE)
    # _, data = data_handle.get_all_data(CUSTOMER_ENTRY_FILE)
    if data:
        return (0,[v["Name"] for k,v in data.items()])
    else:
        return (0,[])


def fetch_customer_detail(email:str)-> tuple[int, dict]:
    """
    Fetch detail of a specific customer
    Required:
        email: get the customer's detail based on the email (key)
    """
    ret, data = fetch_obj.get_data(CUSTOMER_ENTRY_FILE, key=email)
    # ret, data = data_handle.get_data(CUSTOMER_ENTRY_FILE, key=email)
    if ret == 0:
        data["email"] = email
    return (ret, data)


def allocate_rent(email: str, vehicle_type:str, vehicle_id: str)-> tuple[int, str]:
    """
    Allocate rent details to an employee
    """
    ret, data = fetch_obj.get_data(CUSTOMER_ENTRY_FILE, key=email)
    # ret, data = data_handle.get_data(CUSTOMER_ENTRY_FILE, key=email)
    if ret == 0:
        details = data.get("Rent Details")
        if not details:
            details = {}
        now = datetime.today().strftime('%d-%b-%Y-%H:%M:%S')
        details[vehicle_id] = {"Type": vehicle_type, "Rental Date": now}
        data["Rent Details"] = details
        add_obj.create(CUSTOMER_ENTRY_FILE, key=email, value=data)
        # data_handle.create(CUSTOMER_ENTRY_FILE, key=email, value=data)
        return 0, "" 
    return INVALID_EMAIL_ID_ERROR_CODE, INVALID_EMAIL_ID_ERROR.format(email)


def deallocate_rent(email:str, vehicle_id: str)-> tuple[int, str]:
    """
    Deallocate rent details and store the history
    """
    ret, data = fetch_obj.get_data(CUSTOMER_ENTRY_FILE, key=email)
    # ret, data = data_handle.get_data(CUSTOMER_ENTRY_FILE, key=email)
    if ret == 0:
        details = data.get("Rent Details")
        if details:
            if details.get(vehicle_id):
                history_details = {
                    "Vehicle Type": details[vehicle_id]["Type"],
                    "Registration ID": vehicle_id,
                    "Rent Date": details[vehicle_id]["Rental Date"]
                }
                _maintain_rent_history(email, history_details)
                del data["Rent Details"][vehicle_id]
                add_obj.create(CUSTOMER_ENTRY_FILE, key=email, value=data)
                # data_handle.create(CUSTOMER_ENTRY_FILE, key=email, value=data)
                return (0, "")
            return (INVALID_VEHICLE_ID_ERROR_CODE, INVALID_VEHICLE_ID_ERROR.format(vehicle_id, ""))
    return (INVALID_EMAIL_ID_ERROR_CODE, INVALID_EMAIL_ID_ERROR.format(email))


def _maintain_rent_history(email, details):
    """
    data: {
            "vehicle_type": "tyep of vehicle",
            "Registration ID": "vehicle id",
            "Rent Date": "date: %Y-%b-%d-%H:%M:%S",
        }
    """
    now = datetime.today().strftime('%d-%b-%Y-%H:%M:%S')
    details["Return Date"] = now
    ret, data = fetch_obj.get_data(RENT_HISTORY_FILE, key=email)
    # ret, data = data_handle.get_data(RENT_HISTORY_FILE, key=email)
    if not ret == 0:
        data = {}
        data["Rental History"] = []
    data["Rental History"].append(details)
    add_obj.create(RENT_HISTORY_FILE, key=email, value=data)
    # data_handle.create(RENT_HISTORY_FILE, key=email, value=data)
    return


