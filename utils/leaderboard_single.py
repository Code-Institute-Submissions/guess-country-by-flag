import json
from utils import users, files, game_single
from operator import itemgetter

"""
Create leaderboard player object based on username and score of a player
"""
def create_leaderboard_player(username):
    score = users.return_user_score(username)
    game_duration = game_single.extract_key_value_from_game_obj(username, "game_duration")
    
    player = {
        "username": username,
        "score": score,
        "duration": game_duration,
        "rank": 0
    }
    
    return player

"""" Sort leaderboard data by game duration in ascending order and then by score in descending """
def sort_score_in_descending_order(file_name):
    data = files.read_data_file(file_name)
    
    
    sorted_by_game_duration_data = sorted(data, key=itemgetter('duration'))
    sorted_by_score_data = sorted(sorted_by_game_duration_data, key=itemgetter('score'), reverse=True)
            
    
    return sorted_by_score_data
    
""" Change rank in ascending order starting from 1 """
def change_rank_ascending(file_name):
    data = sort_score_in_descending_order(file_name)
    
    for obj in data:
        obj["rank"] = data.index(obj) + 1
            
    return data
    
""" Update leaderboard data """
def update_leaderboard(file_name):
    updated_data = change_rank_ascending(file_name)
    files.overwrite_file(file_name, updated_data)
    
    
""" Return top 10 """
def update_top_ten(file_name):
    data = files.read_data_file(file_name)
    top_ten = []
    
    if len(data) > 10:
        for i in range(10):
            top_ten.append(data[i])
    else:
        for player in data:
            top_ten.append(player)
        
    return top_ten
    
""" Return game duration for given user """
def return_user_game_duration(username, file_name):
    data = files.read_data_file(file_name)
    
    current_user = {}
    
    for user in data:
        if user["username"] == username:
            current_user = user
    
    return current_user["duration"]

