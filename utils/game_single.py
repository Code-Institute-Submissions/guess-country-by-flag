import json
from utils import file, misc

""" 
Create unique game object for a user 
"""
def create_game_object():
    game = {
        "countries": misc.generate_random_numbers(11),
        "incorrect_answers": [],
        "question_number": 1,
        "points": 5
    }
    return game



"""
Extract value of key from game object inside a given user object
"""
def extract_key_value_from_game_obj(username, key_name):
    data = file.read_data_file("users")
    current_game = {}
    key_value = []
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
                    
    for item in current_game:
        for key, value in current_game.items():
            if key == key_name:
                key_value = value
                
                        
    return key_value
 
 
    
""" 
Increase question_number by 1 inside game object 
"""
def increase_question_number(username):
    data = file.read_data_file("users")
    current_game = {}
    val = 0
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    current_game["question_number"] += 1
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    with open("data/users.json", "w") as json_data:
        json.dump(data, json_data, indent=4, sort_keys=True)
        

"""
Reset question number 
"""
def reset_question_number(username):
    data = file.read_data_file("users")
    current_game = {}
    val = 0
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    current_game["question_number"] = 1
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    with open("data/users.json", "w") as json_data:
        json.dump(data, json_data, indent=4, sort_keys=True)
        


""" 
Append user's incorrect answers to game object 
"""
def append_incorrect_answers(username, answer):
    data = file.read_data_file("users")
    current_game = {}
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    current_game["incorrect_answers"].append(answer)
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    with open("data/users.json", "w") as json_data:
        json.dump(data, json_data, indent=4, sort_keys=True)
        
        
        
""" 
Reset incorrect answers 
"""
def reset_incorrect_answers(username):
    data = file.read_data_file("users")
    current_game = {}
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    current_game["incorrect_answers"] = []
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    with open("data/users.json", "w") as json_data:
        json.dump(data, json_data, indent=4, sort_keys=True)        

        
""" 
Decrease round points by 2 
"""
def decrease_round_points(username):
    data = file.read_data_file("users")
    current_game = {}
    
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    if current_game["points"] < 2:
        current_game["points"] = 0
    else:
        current_game["points"] -= 2
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    with open("data/users.json", "w") as json_data:
        json.dump(data, json_data, indent=4, sort_keys=True)
        
""" 
Reset round points 
"""
def reset_round_points(username):
    data = file.read_data_file("users")
    current_game = {}
    
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    current_game["points"] = 5
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    with open("data/users.json", "w") as json_data:
        json.dump(data, json_data, indent=4, sort_keys=True)