import json
from constants import *

class add:
    def create(self, file: str, key: str, value: dict)->int:
        with open(file, 'r') as f:
            data = json.load(f)
        data[key] = value
        with open(file, 'w') as f: 
            json.dump(data, f, indent=4, sort_keys=True)
        return 0

    def update(self):
        # Nothing for now
        pass


class fetch:
    return_type = tuple[int, dict]

    def get_all_data(self, file: str)->return_type:
        """
        Return all the data present in the specific database
        Required:
            file: File containing the database
        """
        all_data = {}
        with open(file, 'r') as f:
            data = json.load(f)
            for key, val in data.items():
                if key == "_syntax":
                    continue
                all_data[key] = val
        return (0, all_data)   


    def get_data(self, file: str, key: str)-> return_type:
        """
        Get data of a key from database
        Required:
            file: File containing the data
            key: value of specific key to fetch
        """
        _, data = self.get_all_data(file)
        if key:
            value = data.get(key)
            if value:
                return (0, value)
        return (DATA_NOT_FOUND_ERROR_CODE, DATA_NOT_FOUND.format("key"))


    def get_all_key(self, file: str) ->return_type:
        """
        Return all the keys from the given json file
        Required:
            file: File containing the data
        """
        _, data = self.get_all_data(file)
        if data:
            return (0, list(data.keys()))
        else:
            return (0, [])


class delete:
    def unregister(self, file: str, key: str)->tuple[int, str]:
        with open(file, 'r') as f:
            data = json.load(f)
        del data[key]
        with open(file, 'w') as f: 
            json.dump(data, f, indent=4, sort_keys=True)
        return 0, ""


###################################
#Below is the old implementation which I had to use due to my incompetance ;p
###################################

# import json
# from constants import *

# # class add:
# def create(file: str, key: str, value: dict)->int:
#     with open(file, 'r') as f:
#         data = json.load(f)
#     data[key] = value
#     with open(file, 'w') as f: 
#         json.dump(data, f, indent=4, sort_keys=True)
#     return 0

# def update():
#     # Nothing for now
#     pass


# # class fetch:
# return_type = tuple[int, dict]

# def get_all_data(file: str)->return_type:
#     """
#     Return all the data present in the specific database
#     Required:
#         file: File containing the database
#     """
#     all_data = {}
#     with open(file, 'r') as f:
#         data = json.load(f)
#         for key, val in data.items():
#             if key == "_syntax":
#                 continue
#             all_data[key] = val
#     return (0, all_data)   


# def get_data(file: str, key: str)-> return_type:
#     """
#     Get data of a key from database
#     Required:
#         file: File containing the data
#         key: value of specific key to fetch
#     """
#     _, data = get_all_data(file)
#     if key:
#         value = data.get(key)
#         if value:
#             return (0, value)
#     return (DATA_NOT_FOUND_ERROR_CODE, DATA_NOT_FOUND.format(key))


# def get_all_key(file: str) ->return_type:
#     """
#     Return all the keys from the given json file
#     Required:
#         file: File containing the data
#     """
#     _, data = get_all_data(file)
#     if data:
#         return (0, list(data.keys()))
#     else:
#         return (0, [])


# def unregister(file: str, key: str)->int:
#     with open(file, 'r') as f:
#         data = json.load(f)
#     del data[key]
#     with open(file, 'w') as f: 
#         json.dump(data, f, indent=4, sort_keys=True)
#     return
