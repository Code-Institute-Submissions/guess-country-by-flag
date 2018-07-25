import json
import time
from utils import files, misc

""" 
Create unique game object for a user 
"""
def create_game_object():
    game = {
        "countries": misc.generate_random_numbers(20),
        "incorrect_answers": [],
        "question_number": 1,
        "points": 5,
        "win": "not-won",
        "game_duration": 0
    }
    return game



"""
Extract value of key from game object inside a given user object
"""
def extract_key_value_from_game_obj(username, key_name):
    data = files.read_data_file("users")
    current_game = {}
    key_value = None
    
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
    data = files.read_data_file("users")
    current_game = {}
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    current_game["question_number"] += 1
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    files.overwrite_file("users", data)
        

"""
Reset question number 
"""
def reset_question_number(username):
    data = files.read_data_file("users")
    current_game = {}
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    current_game["question_number"] = 1
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    files.overwrite_file("users", data)
        


""" 
Append user's incorrect answers to game object 
"""
def append_incorrect_answers(username, answer):
    data = files.read_data_file("users")
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
                    
    files.overwrite_file("users", data)
        
        
        
""" 
Reset incorrect answers 
"""
def reset_incorrect_answers(username):
    data = files.read_data_file("users")
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
                    
    files.overwrite_file("users", data)        

        
""" 
Decrease round points by 2 
"""
def decrease_round_points(username):
    data = files.read_data_file("users")
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
                    
    files.overwrite_file("users", data)
        
""" 
Reset round points 
"""
def reset_round_points(username):
    data = files.read_data_file("users")
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
                    
    files.overwrite_file("users", data)



""" 
Set win state to given value 
"""
def set_win_state(username, state):
    data = files.read_data_file("users")
    current_game = {}
    
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    current_game["win"] = state
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    files.overwrite_file("users", data)
 
 
""" Check if the user scored 100 points or less, set win state accordingly """         
def check_for_win(user_score, username):
    if user_score == 100:
        set_win_state(username, "won")
    else:
        set_win_state(username, "lost")
        
        

""" 
Set game duration to specified time 
"""
def set_game_duration(username, time):
    data = files.read_data_file("users")
    current_game = {}
    
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    current_game["game_duration"] = time
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    files.overwrite_file("users", data)
    
    
""" 
Set game duration to current time
"""
def set_game_duration_current(username):
    data = files.read_data_file("users")
    current_game = {}
    
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    current_game["game_duration"] = time.time()
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    files.overwrite_file("users", data)
    
    
    
""" 
Update game object with new list of random countries
"""
def generate_new_list_of_random_countries(username):
    data = files.read_data_file("users")
    current_game = {}
    
    
    for user in data:
        if user["username"] == username:
            for key, value in user.items():
                if key == "game":
                    current_game = value
    
    
    current_game["countries"] = misc.generate_random_numbers(20)
    
    for user in data:
        if user["username"] == username:
            user["game"] = current_game
                    
    files.overwrite_file("users", data)
        
        
