import os

DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), "data")
CUSTOMER_ENTRY_FILE = os.path.join(DATA_DIRECTORY, "customer_entry.json")
VEHICLE_DATA_FILE = os.path.join(DATA_DIRECTORY, "vehicles.json")
RENT_HISTORY_FILE = os.path.join(DATA_DIRECTORY, "rent_history.json")

DATA_ERROR_CODE = 2
INCOMPLETE_DATA_ERROR = "Given data is not complete. Required: {}"
INVALID_DATA_ERROR = "Invaild input {}"

DATA_NOT_FOUND_ERROR_CODE = 3
DATA_NOT_FOUND = "No data found for the given query: {}"

VEHICLE_REGISTER_FAILED_ERROR_CODE = 3
VEHICLE_REGISTER_FAILED_ERROR = "Failed to register vehicle: {}"

VEHICLE_NOT_AVAILABLE_ERROR_CODE = 4
VEHICLE_NOT_AVAILABLE_ERROR = "Vehicle {} is not available to rent"

INVALID_VEHICLE_ID_ERROR_CODE = 5
INVALID_VEHICLE_ID_ERROR = "Vehicle id {} for vehicle {} is not valid"

INVALID_EMAIL_ID_ERROR_CODE = 6
INVALID_EMAIL_ID_ERROR = "Email ID {} is invalid" 

