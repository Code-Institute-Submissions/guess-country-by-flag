from utils import files

def return_value_from_country(index, key):
    data = files.read_data_file("countries")
    country_obj = data[index] 
    
    return country_obj[key]