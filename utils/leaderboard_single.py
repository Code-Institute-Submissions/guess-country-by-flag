import json
from operator import itemgetter

from utils import users, files, game_single, misc

def create_leaderboard_player(username):
    score = users.return_player_score(username)
    game_duration = game_single.extract_value_from_game(username, "game_duration")
    player = {
        "username": username,
        "score": score,
        "duration": game_duration,
        "rank": 0
    }
    
    return player


def sort_score_in_descending_order(data):
    sorted_by_game_duration_data = sorted(data, key=itemgetter('duration'))
    sorted_by_score_data = sorted(sorted_by_game_duration_data, key=itemgetter('score'), reverse=True)
    
    return sorted_by_score_data
    

def change_rank_ascending(data):
    sorted_data = sort_score_in_descending_order(data)
    
    for obj in sorted_data:
        obj["rank"] = sorted_data.index(obj) + 1
            
    return sorted_data
    

def update_leaderboard(data):
    updated_data = change_rank_ascending(data)
    
    files.overwrite_file("leaderboard", updated_data)


def create_top_ten_players_list(data):
    top_ten = []
    
    if len(data) > 10:
        for i in range(10):
            top_ten.append(data[i])
    else:
        for player in data:
            top_ten.append(player)
            
    return top_ten
    
    
def check_if_player_already_on_leaderboard(username, data):
    if not any(player["username"] == username for player in data):
        return False
    else:
        return True
        
        
def update_player_on_leaderboard(current_player, data):
    for player in data:
        if player["username"] == current_player["username"]:
            if player["score"] == current_player["score"] and player["duration"] > current_player["duration"]:
                player["duration"] = current_player["duration"]
            elif player["score"] < current_player["score"]:
                player["score"] = current_player["score"]
                player["duration"] = current_player["duration"]
                
    update_leaderboard(data)


def list_game_duration_for_each_player(data):
    list_of_player_times = []
    
    for player in data:
        player_time = misc.convert_time_for_display(player["duration"])
        list_of_player_times.append(player_time)
        
    return list_of_player_times
        
    

