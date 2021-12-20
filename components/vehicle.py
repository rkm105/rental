from constants import *
from . import data_handle

add_obj = data_handle.add()
fetch_obj = data_handle.fetch()
delete_obj = data_handle.delete()

def _check_availablity(vehicle: str)->int:
    """
    Check is the given vehicle type is Available
    """
    if vehicle:
        ret, data = fetch_obj.get_data(VEHICLE_DATA_FILE, key=vehicle)
        # ret, data = data_handle.get_data(VEHICLE_DATA_FILE, key=vehicle)
        if ret == 0:
            return True if (data.get("Available") > 0) else False
    return False


def rent_vehicle(vehicle:str) -> tuple[int, str]:
    """
    Rent a vehicle
    Required:
        vehicle: type of vehicle
    Return:
        vehicle_id, ret_code
    """
    if _check_availablity(vehicle):
        _, data = fetch_obj.get_data(VEHICLE_DATA_FILE, key=vehicle)
        # _, data = data_handle.get_data(VEHICLE_DATA_FILE, key=vehicle)
        data['Available'] -= 1
        data['Rented'] += 1
        for id, availablity in data["Registration_ids"].items():
            if availablity:
                data['Registration_ids'][id] = False
                reg_id = id
                break
        add_obj.create(VEHICLE_DATA_FILE, vehicle, value=data)
        # data_handle.create(VEHICLE_DATA_FILE, vehicle, value=data)
        return 0, reg_id
    return VEHICLE_REGISTER_FAILED_ERROR_CODE, VEHICLE_REGISTER_FAILED_ERROR.format(vehicle)


def get_vehicle_list()->tuple[int, dict]:
    """
    Get the list of vehicles and related data
    """
    return fetch_obj.get_all_data(VEHICLE_DATA_FILE)
    # return data_handle.get_all_data(VEHICLE_DATA_FILE)


def return_vehicle(vehicle:str, vehicle_id:str)->tuple[int, str]:
    """
    Return the Rented vehicle
    Required:
        vehicle: Rented vehicle type
        vehicle_id: vehicle id provided during registration 
    """
    _, data = fetch_obj.get_data(VEHICLE_DATA_FILE, key=vehicle)
    # _, data = data_handle.get_data(VEHICLE_DATA_FILE, key=vehicle)
    for id, availablity in data["Registration_ids"].items():
        if id == vehicle_id and not availablity:
            data["Available"] += 1
            data["Rented"] -= 1
            data["Registration_ids"][id] = True
            add_obj.create(VEHICLE_DATA_FILE, vehicle, value=data)
            # data_handle.create(VEHICLE_DATA_FILE, vehicle, value=data)
            return 0, ""
    return INVALID_VEHICLE_ID_ERROR_CODE, INVALID_VEHICLE_ID_ERROR.format(vehicle_id, vehicle)



