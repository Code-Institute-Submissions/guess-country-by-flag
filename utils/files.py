import json

def create_file_path(name_of_file):
    file_path = "data/" + name_of_file + ".json"
    
    return file_path
 
 
def read_data_file(file_name):
    with open(create_file_path(file_name), "r") as json_data:
        data = json.load(json_data)
        
    return data
    
    
def overwrite_file(file_name, new_data):
    with open(create_file_path(file_name), "w") as json_data:
        json.dump(new_data, json_data, indent=4, sort_keys=True)


def append_to_file(stuff_to_append, file_name):
    data = read_data_file(file_name)
    
    data.append(stuff_to_append)
    
    overwrite_file(file_name, data)
 
 