import json
import time

from utils import files, misc

def create_game():
    game = {
        "countries": misc.generate_random_numbers(20),
        "incorrect_answers": [],
        "question_number": 1,
        "points": 5,
        "win": "not",
        "game_duration": 0
    }
    
    return game


def select_game_of_player(username, user_data):
    data = user_data
    target_user = {}
    
    for user in data:
        if user["username"] == username:
            target_user = user
            
    target_game = target_user["game"]
    
    return target_game


def overwrite_game(username, game, user_data):
    data = user_data
    
    for user in data:
        if user["username"] == username:
            user["game"] = game
            
    files.overwrite_file("users", data)


def extract_value_from_game(username, key_name):
    data = files.read_data_file("users")
    target_game = select_game_of_player(username, data)
    value = target_game[key_name]
    
    return value
    
    
def increase_question_number(username):
    data = files.read_data_file("users")
    target_game = select_game_of_player(username, data)
    target_game["question_number"] += 1
    
    overwrite_game(username, target_game, data)
    
    
def reset_question_number(username):
    data = files.read_data_file("users")
    target_game = select_game_of_player(username, data)
    target_game["question_number"] = 1
    
    overwrite_game(username, target_game, data)
        

def append_incorrect_answers(username, answer):
    data = files.read_data_file("users")
    target_game = select_game_of_player(username, data)
    
    target_game["incorrect_answers"].append(answer)
    
    overwrite_game(username, target_game, data)
        
        
def reset_incorrect_answers(username):
    data = files.read_data_file("users")
    target_game = select_game_of_player(username, data)
    target_game["incorrect_answers"] = []
    
    overwrite_game(username, target_game, data)


def decrease_round_points(username):
    data = files.read_data_file("users")
    target_game = select_game_of_player(username, data)
    
    if target_game["points"] < 2:
        target_game["points"] = 0
    else:
        target_game["points"] -= 2
        
    overwrite_game(username, target_game, data)
        
        
def reset_round_points(username):
    data = files.read_data_file("users")
    target_game = select_game_of_player(username, data)
    target_game["points"] = 5
    
    overwrite_game(username, target_game, data)


def set_win_state(username, state):
    data = files.read_data_file("users")
    target_game = select_game_of_player(username, data)
    target_game["win"] = state
    
    overwrite_game(username, target_game, data)
 
 
def check_for_win(user_score, username):
    if user_score == 100:
        set_win_state(username, "won")
    else:
        set_win_state(username, "lost")
        
        
def set_game_duration(username, time):
    data = files.read_data_file("users")
    target_game = select_game_of_player(username, data)
    target_game["game_duration"] = time
    
    overwrite_game(username, target_game, data)
    
    
def set_game_duration_current(username):
    data = files.read_data_file("users")
    target_game = select_game_of_player(username, data)
    target_game["game_duration"] = time.time()
    
    overwrite_game(username, target_game, data)
    
    
def generate_new_list_of_random_countries(username):
    data = files.read_data_file("users")
    target_game = select_game_of_player(username, data)
    target_game["countries"] = misc.generate_random_numbers(20)
    
    overwrite_game(username, target_game, data)
        
        
