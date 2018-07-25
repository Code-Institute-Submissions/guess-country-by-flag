import json
import files


""" 
Return value of a given key from a country object of certain index 
"""
def return_value_for_key_in_country_object_of_index(file_name, index, key):
    data = files.read_data_file(file_name)
    country_obj = data[index]    
    
    for k, v in country_obj.items():
        if k == key:
            return v