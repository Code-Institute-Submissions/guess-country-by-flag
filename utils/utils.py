import json

"""
Create user object with given values for username and score
"""
def create_user(username, password, score):
    user = {
        "username": username,
        "password": password,
        "score": score
    }
    return user


"""
Check if any of the user objects in the data file contain a certain username, 
if yes then return False if not then return True
"""
def check_if_username_does_exist(file, username):
    with open(file, "r") as json_data:
        data = json.load(json_data)
        
    if not any(obj["username"] == username for obj in data):
        return True
    else:
        return False


"""
Check if password matches username in the user object
"""
def check_if_password_matches(file, username, password):
    with open(file, "r") as json_data:
        data = json.load(json_data)
        
    if not check_if_username_does_exist(file, username):
        current_user = {}
    
        for obj in data:
            if obj["username"] == username:
                current_user = obj
    
        if current_user["password"] == password:
            print(current_user)
            return True
        else:
            return False
    else:
        return False
        
    


"""
Check if user object with given username exists in data file
if not then create user object with given username and append
it to the data file
"""
def add_user_to_data_file(file, username, password):
    if check_if_username_does_exist(file, username) == True:
        with open(file, "r") as json_data:
            data = json.load(json_data)
        data.append(create_user(username, password, 0))
        with open(file, 'w') as json_data:
            json.dump(data, json_data, indent=4, sort_keys=True)


"""
Interate over all user objects in data file and add them to a new
list if their username value is not equal to the given username value,
overwrite the data file with the new list of user object, effectively removing
the user object with the given username
"""
def remove_user_from_data_file(file, username):
    updated_data = []
    with open(file, "r") as json_data:
        data = json.load(json_data)
    
    for obj in data:
        if obj["username"] != username:
            updated_data.append(obj)
            
    with open(file, 'w') as json_data:
        json.dump(updated_data, json_data, indent=4, sort_keys=True)



"""
Interate over all user objects in data file and add them to a new
list if their username value is not equal to the given username value,
overwrite the data file with the new list of user object, effectively removing
the user object with the given username
"""
def remove_last_user_from_multi_data_file(file):
    updated_data = []
    with open(file, "r") as json_data:
        data = json.load(json_data)
    
    updated_data = data[:-1]
            
    with open(file, 'w') as json_data:
        json.dump(updated_data, json_data, indent=4, sort_keys=True)


""" Check if multi_users.json contains 5 users """ 
def check_number_of_multi_users(file):
    with open(file, "r") as json_data:
        data = json.load(json_data)
        
    if len(data) == 5:
        return True
    else:
        return False