import os
import json


""" 
Create data file with given name 
"""
def create_data_file(file_name):
    with open("data/" + file_name + ".json", "w") as json_data:
        json_data.write("[]") 



""" 
Check if file exists 
"""
def check_if_file_exists(file_name):
    if os.path.exists("data/" + file_name + ".json"):
        return True
    else:
        return False
 
 
     
""" 
Delete target data file 
"""
def delete_data_file(file_name):
    if os.path.exists("data/" + file_name + ".json"):
        os.remove("data/" + file_name + ".json")
    else:
        return False


    
""" 
Create file path to data file 
"""
def create_file_path(name_of_file):
    file_path = "data/" + name_of_file + ".json"
    return file_path
 

        
""" 
Read all the data from file 
"""
def read_data_file(file_name):
    with open(create_file_path(file_name), "r") as json_data:
        data = json.load(json_data)
        
    return data
    
"""
Overwrite file with new data
"""
def overwrite_file(file_name, new_data):
    with open(create_file_path(file_name), "w") as json_data:
        json.dump(new_data, json_data, indent=4, sort_keys=True)


""" 
Append to data file 
"""
def append_to_file(stuff_to_append, file_name):
    data = read_data_file(file_name)
        
    data.append(stuff_to_append)
    
    overwrite_file(file_name, data)
 
 