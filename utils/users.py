import json
from utils import files

def create_player(username, password, score, game):
    user = {
        "username": username,
        "password": password,
        "score": score,
        "game": game
    }
    
    return user


def check_if_username_exists(username):
    data = files.read_data_file("users")
    
    if any(obj["username"] == username for obj in data):
        return True
    else:
        return False


def check_if_password_matches(username, password):
    data = files.read_data_file("users")
    
    for player in data:
        if player["username"] == username:
            if player["password"] == password:
                return True
            else:
                return False


def add_player_to_data(username, password, game):
    if check_if_username_exists(username) == False:
        data = files.read_data_file("users")
        data.append(create_player(username, password, 0, game))
        files.overwrite_file("users", data)


def remove_player_from_data(username):
    data = files.read_data_file("users")
    updated_data = []
    
    for obj in data:
        if obj["username"] != username:
            updated_data.append(obj)
            
    files.overwrite_file("users", updated_data)


def remove_player_from_data_by_index(index):
    data = files.read_data_file("users")
    
    if index > len(data):
        return False
    else:
        data.pop(index)
        
    files.overwrite_file("users", data)


def return_player_score(username):
    data = files.read_data_file("users")
    current_user = {}
    
    for user in data:
        if user["username"] == username:
            current_user = user
            
    return current_user["score"]


def increase_player_score(username, points):
    data = files.read_data_file("users")
    current_user = {}
    
    for user in data:
        if user["username"] == username:
            current_user = user
            
    current_user["score"] += points
    
    files.overwrite_file("users", data)


def reset_player_score(username):
    data = files.read_data_file("users")
    current_user = {}
    
    for user in data:
        if user["username"] == username:
            current_user = user
            
    current_user["score"] = 0
    
    files.overwrite_file("users", data)