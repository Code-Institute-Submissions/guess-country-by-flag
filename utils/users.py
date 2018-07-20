import json

"""
Create user object with given values for username, passowrd, score and game
"""
def create_user(username, password, score, game):
    user = {
        "username": username,
        "password": password,
        "score": score,
        "game": game
    }
    return user



"""
Check if any of the user objects in the data file contain a certain username, 
if yes then return False if not then return True
"""
def check_if_username_does_exist(file_path, username):
    with open(file_path, "r") as json_data:
        data = json.load(json_data)
        
    if not any(obj["username"] == username for obj in data):
        return True
    else:
        return False



"""
Check if input password matches the password for that username
"""
def check_if_password_matches(file_path, username, password):
    with open(file_path, "r") as json_data:
        data = json.load(json_data)
        
    if not check_if_username_does_exist(file_path, username):
        current_user = {}
    
        for obj in data:
            if obj["username"] == username:
                current_user = obj
    
        if current_user["password"] == password:
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
def add_user_to_data_file(file_path, username, password, game):
    if check_if_username_does_exist(file_path, username) == True:
        with open(file_path, "r") as json_data:
            data = json.load(json_data)
            
        data.append(create_user(username, password, 0, game))
        
        with open(file_path, 'w') as json_data:
            json.dump(data, json_data, indent=4, sort_keys=True)



"""
Interate over all user objects in data file and add them to a new
list if their username value is not equal to the given username value,
overwrite the data file with the new list of user object, effectively removing
the user object with the given username
"""
def remove_user_from_data_file(file_path, username):
    updated_data = []
    with open(file_path, "r") as json_data:
        data = json.load(json_data)
    
    for obj in data:
        if obj["username"] != username:
            updated_data.append(obj)
            
    with open(file_path, 'w') as json_data:
        json.dump(updated_data, json_data, indent=4, sort_keys=True)



"""
Remove user from data file by index
"""
def remove_user_from_data_by_index(file_path, index):
    with open(file_path, "r") as json_data:
        data = json.load(json_data)
    if index > len(data):
        return False
    else:
        data.pop(index)
    
    updated_data = data
    
    with open(file_path, 'w') as json_data:
        json.dump(updated_data, json_data, indent=4, sort_keys=True)



""" 
Check if data file for multiplayer contains 5 users 
""" 
def check_number_of_multi_users(file_path):
    with open(file_path, "r") as json_data:
        data = json.load(json_data)
        
    if len(data) == 5:
        return True
    else:
        return False



""" 
Return score of a user 
"""
def return_user_score(username):
    with open("data/users.json", "r") as json_data:
        data = json.load(json_data)
    current_user = {}
    
    for user in data:
        if user["username"] == username:
            current_user = user
            
    return current_user["score"]

    

""" 
Increase score of a given user by a given number of points 
"""
def increase_user_score(username, points):
    with open("data/users.json", "r") as json_data:
        data = json.load(json_data)
    current_user = {}
    
    for user in data:
        if user["username"] == username:
            current_user = user
            
    current_user["score"] += points
    
    updated_data = data
            
    with open("data/users.json", 'w') as json_data:
        json.dump(updated_data, json_data, indent=4, sort_keys=True)


        
""" 
Reset score of a given user 
"""
def reset_user_score(username):
    with open("data/users.json", "r") as json_data:
        data = json.load(json_data)
        
    current_user = {}
    
    for user in data:
        if user["username"] == username:
            current_user = user
            
    current_user["score"] = 0
    
    updated_data = data
            
    with open("data/users.json", 'w') as json_data:
        json.dump(updated_data, json_data, indent=4, sort_keys=True)