import json
from utils.file import create_file_path

""" 
Return value of a given key from a country object of certain index 
"""
def return_value_for_key_in_country_object_of_index(file_name, index, key):
    with open(create_file_path(file_name), "r") as json_data:
        data = json.load(json_data)
    country_obj = data[index]    
    
    for k, v in country_obj.items():
        if k == key:
            return v