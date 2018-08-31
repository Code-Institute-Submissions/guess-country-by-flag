import time
from operator import itemgetter

from utils import files, misc

def create_game(game_name):
    multi_game = {
        "game_name": game_name,
        "time_of_creation": time.time(),
        "players": [],
        "players_copy": [],
        "round_number": 1,
        "flag_number": 0,
        "turn_of_player": 0,
        "points": 5,
        "list_of_countries": [],
        "game_state": "ongoing"
    }
    
    return multi_game
    

def remove_game_from_data(game_name):
    data = files.read_data_file("game_multi")
    updated_data = []
    
    for game in data:
        if game["game_name"] != game_name:
            updated_data.append(game)
            
    files.overwrite_file("game_multi", updated_data)


def select_game(game_name, multi_data):
    data = multi_data
    target_game = {}
    
    for game in data:
        if game["game_name"] == game_name:
            target_game = game
            
    return target_game
          
            
def overwrite_game(game_name, target_game, multi_data):
    data = multi_data
    
    for index, game in enumerate(data):
       if game["game_name"] == game_name:
           data[index] = target_game
           
    files.overwrite_file("game_multi", data)


def create_player(username):
    player = {
        "username": username,
        "score": 0,
        "rank": 0,
        "start_time": 0.0,
        "elapsed_time": 0.0,
        "incorrect_answers": []
    }
    
    return player
        
        
def check_if_player_exists(game_name, username):
    data = files.read_data_file("game_multi")
    target_game = select_game(game_name, data)
    list_of_players = target_game["players"]
    
    if any(player["username"] == username for player in list_of_players):
        return True
    else:
        return False


def add_player_to_game(game_name, player):
    data = files.read_data_file("game_multi")
    target_game = select_game(game_name, data)
    
    target_game["players"].append(player)
    overwrite_game(game_name, target_game, data)


def check_if_five_players(game_name):
    data = files.read_data_file("game_multi")
    target_game = select_game(game_name, data)
    list_of_players = target_game["players"]
    
    if len(list_of_players) == 5:
        return True
    else:
        return False
       
       
def check_if_game_exists(game_name):
    data = files.read_data_file("game_multi")
    
    if any(game["game_name"] == game_name for game in data):
        return True
    else:
        return False


def extract_value_from_game(game_name, key_name):
    data = files.read_data_file("game_multi")
    target_game = select_game(game_name, data)
    
    return target_game[key_name]


def extract_value_from_player(game_name, username, key_name):
    list_of_players = extract_value_from_game(game_name, "players")
    given_player = {}
    
    for player in list_of_players:
        if player["username"] == username:
            given_player = player
            
    return given_player[key_name]


def overwrite_game_value(game_name, key_name, value):
    data = files.read_data_file("game_multi")
    
    for game in data:
        if game["game_name"] == game_name:
            game[key_name] = value
            
    files.overwrite_file("game_multi", data)


def overwrite_player_value(game_name, username, key_name, value):
    list_of_players = extract_value_from_game(game_name, "players")
    
    for player in list_of_players:
        if player["username"] == username:
            player[key_name] = value
            
    overwrite_game_value(game_name, "players", list_of_players)


def remove_player_from_game_by_index(game_name, index):
    list_of_players = extract_value_from_game(game_name, "players")
    
    if index > len(list_of_players):
        return False
    else:
        list_of_players.pop(index)
        
    overwrite_game_value(game_name, "players", list_of_players)


def increase_flag_number(game_name):
    data = files.read_data_file("game_multi")
    target_game = select_game(game_name, data)
    target_game["flag_number"] += 1
    
    overwrite_game(game_name, target_game, data)


def reset_flag_number(game_name):
    data = files.read_data_file("game_multi")
    target_game = select_game(game_name, data)
    target_game["flag_number"] = 0
    
    overwrite_game(game_name, target_game, data)


def set_turn_of_player(game_name, number_of_players):
    data = files.read_data_file("game_multi")
    target_game = select_game(game_name, data)
    
    if target_game["turn_of_player"] == number_of_players - 1:
        # number_of_players - 1 = last player's index number
        target_game["turn_of_player"] = 0
    else:
        target_game["turn_of_player"] += 1
        
    overwrite_game(game_name, target_game, data)


def increase_round_number(game_name):
    data = files.read_data_file("game_multi")
    target_game = select_game(game_name, data)
    target_game["round_number"] += 1
    
    overwrite_game(game_name, target_game, data)


def reset_round_number(game_name):
    data = files.read_data_file("game_multi")
    target_game = select_game(game_name, data)
    target_game["round_number"] = 0
    
    overwrite_game(game_name, target_game, data)


def increase_player_score(index_of_player, points, game_name):
    list_of_players = extract_value_from_game(game_name, "players")
    current_player = list_of_players[index_of_player]
    
    for player in list_of_players:
        if player == current_player:
            player["score"] += points
            
    overwrite_game_value(game_name, "players", list_of_players)


def reset_incorrect_answers(index_of_player, game_name):
    list_of_players = extract_value_from_game(game_name, "players")
    current_player = list_of_players[index_of_player]
    
    for player in list_of_players:
        if player == current_player:
            player["incorrect_answers"] = []
            
    overwrite_game_value(game_name, "players", list_of_players)


def reset_points(game_name):
    data = files.read_data_file("game_multi")
    target_game = select_game(game_name, data)
    target_game["points"] = 5
    
    overwrite_game(game_name, target_game, data)


def append_incorrect_answers(index_of_player, answer, game_name):
    list_of_players = extract_value_from_game(game_name, "players")
    current_player = list_of_players[index_of_player]
    
    current_player["incorrect_answers"].append(answer)
    
    for player in list_of_players:
        if player["username"] == current_player["username"]:
            player = current_player
            
    overwrite_game_value(game_name, "players", list_of_players)


def decrease_points(game_name):
    data = files.read_data_file("game_multi")
    target_game = select_game(game_name, data)
    
    if target_game["points"] == 1:
        target_game["points"] = 0
    else:
        target_game["points"] -= 2
        
    overwrite_game(game_name, target_game, data)


def return_player_score(index_of_player, game_name):
    list_of_players = extract_value_from_game(game_name, "players")
    
    for player in list_of_players:
        if player == list_of_players[index_of_player]:
            return player["score"]
       
            
def return_player_incorrect_answers(index_of_player, game_name):
    list_of_players = extract_value_from_game(game_name, "players")
    
    for player in list_of_players:
        if player == list_of_players[index_of_player]:
            return player["incorrect_answers"]


def return_player_by_turn(turn_of_player, game_name):
    data = files.read_data_file("game_multi")
    player_list = []
    
    for game in data:
        if game["game_name"] == game_name:
            player_list = game["players"]
            
    return player_list[turn_of_player]


def set_start_time_for_current_player(game_name):
    data = files.read_data_file("game_multi")
    list_of_players = extract_value_from_game(game_name, "players")
    turn_of_player = extract_value_from_game(game_name, "turn_of_player")
    
    for player in list_of_players:
        if player == list_of_players[turn_of_player]:
            player["start_time"] = time.time()
            
    for game in data:
        if game["game_name"] == game_name:
            game["players"] = list_of_players
            
    files.overwrite_file("game_multi", data)


def add_to_previous_players_elapsed_time(game_name):
    data = files.read_data_file("game_multi")
    list_of_players = extract_value_from_game(game_name, "players")
    turn_of_player = extract_value_from_game(game_name, "turn_of_player")
    current_player = list_of_players[turn_of_player]
    
    if((turn_of_player - 1) < 0):
        last_player_index_num = len(list_of_players) - 1
        previous_player = list_of_players[last_player_index_num]
    else:
        previous_player_index_num = turn_of_player - 1
        previous_player = list_of_players[previous_player_index_num]
        
    elapsed_time = current_player["start_time"] - previous_player["start_time"]
    previous_player["elapsed_time"]  += elapsed_time
    
    for game in data:
        if game["game_name"] == game_name:
            game["players"] = list_of_players
            
    files.overwrite_file("game_multi", data)
    
    
def add_to_elapsed_time_of_player_for_last_flag(game_name, end_time):
    data = files.read_data_file("game_multi")
    list_of_players = extract_value_from_game(game_name, "players")
    last_player = list_of_players[-1]
    last_player["elapsed_time"] += end_time - last_player["start_time"]
    list_of_players[-1] = last_player
    
    for game in data:
        if game["game_name"] == game_name:
            game["players"] = list_of_players
            
    files.overwrite_file("game_multi", data)
    
    
def sort_players_for_leaderboard_display(game_name):
    data = files.read_data_file("game_multi")
    list_of_players = extract_value_from_game(game_name, "players")
    players_sorted_by_game_duration = sorted(list_of_players, key=itemgetter('elapsed_time'))
    players_sorted_by_score = sorted(players_sorted_by_game_duration, key=itemgetter('score'), reverse=True)
    
    for game in data:
        if game["game_name"] == game_name:
            game["players"] = players_sorted_by_score
            
    return players_sorted_by_score


def change_rank_of_players(game_name):
    sorted_players = sort_players_for_leaderboard_display(game_name)
    
    for player in sorted_players:
        player["rank"] = sorted_players.index(player) + 1
        
    return sorted_players


def update_player_list(game_name):
    data = files.read_data_file("game_multi")
    sorted_players = change_rank_of_players((game_name))
    
    for game in data:
        if game["game_name"] == game_name:
            game["players"] = sorted_players
            
    files.overwrite_file("game_multi", data)
    
    
def list_players_elapsed_time(game_name):
    data = files.read_data_file("game_multi")
    list_of_players = extract_value_from_game(game_name, "players")
    list_of_player_times = []
    
    for player in list_of_players:
        player_time = misc.convert_time_for_display(player["elapsed_time"])
        list_of_player_times.append(player_time)
        
    return list_of_player_times
    
    
def reset_players(game_name):
    data = files.read_data_file("game_multi")
    list_of_players = extract_value_from_game(game_name, "players")
    
    for player in list_of_players:
        player["incorrect_answers"] = []
        player["rank"] = 0
        player["elapsed_time"] = 0.0
        player["start_time"] = 0.0
        player["score"] = 0
        
    for game in data:
        if game["game_name"] == game_name:
            game["players"] = list_of_players
            
    files.overwrite_file("game_multi", data)
    
    
def remove_games_older_than_a_day(current_time):
    data = files.read_data_file("game_multi")
    
    for game in data:
        if game["time_of_creation"] + 86400 < current_time:
            remove_game_from_data(game["game_name"])
            