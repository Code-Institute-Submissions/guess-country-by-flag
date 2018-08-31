import os
import sys
import time
from flask import Flask, render_template, request, redirect, url_for 

from utils import countries, files, game_multi, game_single, leaderboard_single, misc, users

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Route for the home page where players can choose to either
    play single player or local multiplayer
    """
    if request.method == "POST":
        if request.form["action"] == "Play alone":
            return redirect(url_for("signIn"))
        else:
            return redirect(url_for("createRoom"))
            
    return render_template("index.html")


@app.route("/sign-in", methods=["GET", "POST"])
def signIn():
    """
    Route for the sign in page, players login with an existing account.
    """
    username_error = None
    password_error = None
    
    if request.method == "POST":
        if "enter-game" in request.form:
            if users.check_if_password_matches(request.form["username"],
                                               request.form["password"]):
                return redirect(url_for("gameMenu", username=request.form["username"]))
            elif not users.check_if_username_exists(request.form["username"]):
                username_error = "A user with this username does not exist"
            else:
                password_error = "Wrong password, try again"
        elif "new-user" in request.form:
            return redirect(url_for("signUp"))
            
    return render_template("sign-in.html",
                            password_error=password_error,
                            username_error=username_error)


@app.route("/sign-up", methods=["GET", "POST"])
def signUp():
    """
    Route for the sign up page where players can create a new account.
    Adds a player object to the users data.
    """
    username_error = None
    list_of_countries = []
    
    if request.method == "POST":
        if not users.check_if_username_exists(request.form["username"]):
            users.add_player_to_data(request.form["username"], request.form["password"],
                                        game_single.create_game())
            return redirect(url_for("gameMenu", username=request.form["username"]))
        else:
            username_error = "Username is taken"
            
    return render_template("sign-up.html",
                            username_error=username_error)


@app.route("/game-menu/<username>", methods=["GET", "POST"])
def gameMenu(username):
    """
    Route for the game menu with where players can start the game,
    check out the leaderboard or log out/return back to home page.
    """
    if request.method == "POST":
        if "play" in request.form:
            game_single.set_game_duration_current(username)
            return redirect(url_for("gameSingle", username=username))
        elif "leaderboard" in request.form:
            return redirect(url_for("leaderboard", username=username))
        else:
            return redirect(url_for("index"))
            
    return render_template("game-menu.html")


@app.route("/game-single/<username>", methods=["GET", "POST"])
def gameSingle(username):
    user_score = users.return_player_score(username)
    
    question_number = game_single.extract_value_from_game(username, "question_number")
    points = game_single.extract_value_from_game(username, "points")
    incorrect_answers = game_single.extract_value_from_game(username, "incorrect_answers")
    list_of_countries = game_single.extract_value_from_game(username, "countries")
    
    country_for_current_round = list_of_countries[question_number - 1]
    flag = countries.return_value_from_country(country_for_current_round, "flag")
    official_name = countries.return_value_from_country(country_for_current_round, "name-official")
    common_name = countries.return_value_from_country(country_for_current_round, "name-common")
    
    official_name_title_cased = misc.string_to_lowercase_then_titlecase(official_name)
    common_name_title_cased = misc.string_to_lowercase_then_titlecase(common_name)
    
    if request.method == "POST":
        """
        Single player game functionality. Provides behaviour for buttons used to
        skip questions and to give up on the game, as well as conditions for what
        happens if the player submits an answer. Submitted information is checked against data
        to see whether it's correct or not. Upon winning the game or simply completing it by skipping
        the last question, player is redirected to the leaderboard page. Players are either added to 
        leaderboard data in the event of it being their first time playing or updated if they already exist 
        on the leaderboard. If a player gives up on the game, leaderboard data is not updated. Winning 
        conditions are based on the number of questions and total player score. Full points - 100 are 
        needed in order to win otherwise the game is just completed.
        """
        if "skip" in request.form:
            if question_number == 20:
                end_time = time.time()
                start_time = game_single.extract_value_from_game(username, "game_duration")
                game_single.set_game_duration(username, misc.calculate_game_duration(start_time, end_time))
                game_single.check_for_win(user_score, username)
                leaderboard_player = leaderboard_single.create_leaderboard_player(username)
                if leaderboard_single.check_if_player_already_on_leaderboard(username, files.read_data_file("leaderboard")) == True:
                    leaderboard_single.update_player_on_leaderboard(leaderboard_player, files.read_data_file("leaderboard"))
                else:
                    files.append_to_file(leaderboard_player, "leaderboard")
                leaderboard_single.update_leaderboard(files.read_data_file("leaderboard"))
                return redirect(url_for("leaderboard", username=username))
            else:
                game_single.increase_question_number(username)
                game_single.reset_incorrect_answers(username)
                game_single.reset_round_points(username)
                return redirect(url_for("gameSingle", username=username))
        elif "give-up" in request.form or "play-again" in request.form:
            end_time = time.time()
            start_time = game_single.extract_value_from_game(username, "game_duration")
            game_single.set_game_duration(username, misc.calculate_game_duration(start_time, end_time))
            game_single.check_for_win(user_score, username)
            return redirect(url_for("leaderboard", username=username))
        elif "answer" in request.form:
            answer = misc.string_to_lowercase_then_titlecase(request.form["answer"])
            if question_number == 20 and (answer == official_name or answer == common_name):
                users.increase_player_score(username, points)
                end_time = time.time()
                start_time = game_single.extract_value_from_game(username, "game_duration")
                game_single.set_game_duration(username, misc.calculate_game_duration(start_time, end_time))
                game_single.check_for_win(user_score, username)
                leaderboard_player = leaderboard_single.create_leaderboard_player(username)
                if leaderboard_single.check_if_player_already_on_leaderboard(username, files.read_data_file("leaderboard")) == True:
                    leaderboard_single.update_player_on_leaderboard(leaderboard_player, files.read_data_file("leaderboard"))
                else:
                    files.append_to_file(leaderboard_player, "leaderboard")
                leaderboard_single.update_leaderboard(files.read_data_file("leaderboard"))
                return redirect(url_for("leaderboard", username=username))
            else:
                if answer == official_name_title_cased or answer == common_name_title_cased:
                    game_single.increase_question_number(username)
                    users.increase_player_score(username, points)
                    game_single.reset_incorrect_answers (username)
                    game_single.reset_round_points(username)
                    return redirect(url_for("gameSingle", username=username))
                else:
                    game_single.append_incorrect_answers(username, request.form["answer"])
                    game_single.decrease_round_points(username)
                    return redirect(url_for("gameSingle", username=username))
                    
    return render_template("game-single.html", 
                            username=username,
                            flag_url=flag,
                            question_number=question_number,
                            round_points=points,
                            incorrect_answers=incorrect_answers,
                            score=user_score)
 
    
@app.route("/leaderboard/<username>", methods=["GET", "POST"])
def leaderboard(username):
    """
    Route for the leaderboard page which displays a global leaderboard available to
    any player who creates an account. The leaderboard displays only the top ten best players.
    """
    top_ten = leaderboard_single.create_top_ten_players_list(files.read_data_file("leaderboard"))
    list_of_times = leaderboard_single.list_game_duration_for_each_player(files.read_data_file("leaderboard"))
    
    win = game_single.extract_value_from_game(username, "win")
    time = game_single.extract_value_from_game(username, "game_duration")
    
    user_score = users.return_player_score(username)
    users.reset_player_score(username)
    
    game_single.reset_question_number(username)
    game_single.reset_incorrect_answers(username)
    game_single.reset_round_points(username)
    game_single.generate_new_list_of_random_countries(username)
    
    
    
    if request.method == "POST":
        game_single.set_win_state(username, "not-won")
        if "play-again" in request.form:
            game_single.set_game_duration_current(username)
            return redirect(url_for("gameSingle", username=username))
        elif "continue" in request.form:
            return redirect(url_for("leaderboard", username=username))
            
    return render_template("leaderboard-single.html",
                            username=username, win=win,
                            score=user_score,
                            top_ten=top_ten,
                            time=time,
                            list_of_times=list_of_times)
                            
                            
@app.route("/create-room", methods=["GET", "POST"])
def createRoom():
    """
    Route where players create their local multiplayer game,
    adds a game object to the data with a unique name.
    """
    game_name_error = None
    
    game_multi.remove_games_older_than_a_day(time.time())
    
    if request.method == "POST":
        if not game_multi.check_if_game_exists(request.form["game_name"]):
            files.append_to_file(game_multi.create_game(request.form["game_name"]),
                                "game_multi")
            return redirect(url_for("addPlayers", game_name=request.form["game_name"]))
        else:
            game_name_error = "A game with that name already exists"
            
    return render_template("create-room.html", game_name_error=game_name_error)


@app.route("/add-players/<game_name>", methods=["GET", "POST"])
def addPlayers(game_name):
    """
    Route to add players page where up to five players can be
    added to the game created on the previous create room page. 
    A list of random countries is generated for the game upon
    starting game, the number of them based on the number of players
    """
    username_error = None
    max_number_of_players_error = None
    no_players_error = None
    player_list = game_multi.extract_value_from_game(game_name, "players")
    
    if request.method == "POST":
        for i in range(5):
            if str(i) in request.form:
                game_multi.remove_player_from_game_by_index(game_name, i)
                return redirect(url_for("addPlayers", game_name=game_name))
        if "action" in request.form:
            if len(player_list) > 1:
                game_multi.overwrite_game_value(game_name, "players_copy", player_list)
                game_multi.overwrite_game_value(game_name, "list_of_countries",
                                                    misc.generate_random_numbers((len(player_list) * 5)))
                return redirect(url_for("gameMulti", game_name=game_name))
            else:
                no_players_error = "At least 2 players are needed to start the game"
        elif "username" in request.form:
            if not game_multi.check_if_five_players(game_name):
                if not game_multi.check_if_player_exists(game_name, request.form["username"]):
                    game_multi.add_player_to_game(game_name,
                                                  game_multi.create_player(request.form["username"]))
                    return redirect(url_for("addPlayers", game_name=game_name))
                else:
                    username_error = "Username is taken"
            else:
                max_number_of_players_error = "The maximum number of players has been reached"
                
    return render_template("add-players.html",
                            username_error=username_error,
                            max_number_of_players_error=max_number_of_players_error,
                            no_players_error=no_players_error,
                            player_list=player_list)
          
                            
@app.route("/multiplayer/<game_name>", methods=["GET", "POST"])
def gameMulti(game_name):
    """
    Route for multiplayer game. Takes information from given game and
    the players of that game and updates/manipulates it in order to provide
    game functionality.
    """
    players_initial = game_multi.extract_value_from_game(game_name, "players_copy")
    turn_of_player = game_multi.extract_value_from_game(game_name, "turn_of_player")
    list_of_players = game_multi.extract_value_from_game(game_name, "players")
    round_number = game_multi.extract_value_from_game(game_name, "round_number")
    list_of_country_index_numbers = game_multi.extract_value_from_game(game_name, "list_of_countries")
    game_flag_number = game_multi.extract_value_from_game(game_name, "flag_number")
    game_state = game_multi.extract_value_from_game(game_name, "game_state")
    points = game_multi.extract_value_from_game(game_name, "points")
    
    game_country_index = list_of_country_index_numbers[game_flag_number]
    flag = countries.return_value_from_country(game_country_index, "flag")
    official_name = countries.return_value_from_country(game_country_index, "name-official")
    common_name = countries.return_value_from_country(game_country_index, "name-common")
    
    official_name_title_cased = misc.string_to_lowercase_then_titlecase(official_name)
    common_name_title_cased = misc.string_to_lowercase_then_titlecase(common_name)
    
    current_player = game_multi.return_player_by_turn(turn_of_player, game_name)
    current_player_score = game_multi.return_player_score(turn_of_player, game_name)
    current_player_incorrect_answers = game_multi.return_player_incorrect_answers(turn_of_player, game_name)
    elapsed_times = game_multi.list_players_elapsed_time(game_name)
    
    number_of_players = len(list_of_players)
    index_num_of_last_player = len(list_of_players) - 1
    
    if request.method == "POST":
        """
        Multiplayer game main functionality, allowing players to play locally(on a single device) against each other. 
        Provides behaviour for skipping questions, submitting answers and the round/turn system. Each player has 
        a single turn each round. Players are provided with a total number(number_of_players * 5) of random flags. 
        Each player get's to guess 5 flags(one per round). Player with most points wins. If multiple players hold 
        the same score, whoever goes on top is decided by their total time taken to play the game. Skipping their 
        turn awards no points. Once the game ends, players information is used to create a leaderboard which exists 
        only for that game.
        """
        if "play-again" in request.form:
            # Reset game and players for a new game.
            game_multi.overwrite_game_value(game_name, "flag_number", 0)
            game_multi.overwrite_game_value(game_name, "round_number", 1)
            game_multi.overwrite_game_value(game_name, "turn_of_player", 0)
            game_multi.overwrite_game_value(game_name, "players", players_initial)
            game_multi.overwrite_game_value(game_name, "game_state", "ongoing")
            game_multi.overwrite_game_value(game_name, "list_of_countries",
                                                misc.generate_random_numbers((len(list_of_players) * 5)))
            return redirect(url_for("gameMulti", game_name=game_name))
        elif "continue" in request.form:
            game_multi.remove_game_from_data(game_name)
            return redirect(url_for("index"))
        elif request.form["answer"]:
            answer = misc.string_to_lowercase_then_titlecase(request.form["answer"])
            if answer == official_name_title_cased or answer == common_name_title_cased:
                if round_number == 5 and turn_of_player == index_num_of_last_player:
                    # Check  if the last flag for the last round has been reached
                    game_multi.add_to_elapsed_time_of_player_for_last_flag(game_name, time.time())
                    game_multi.update_player_list(game_name)
                    game_multi.overwrite_game_value(game_name, "game_state", "ended")
                elif round_number < 5 and turn_of_player == index_num_of_last_player:
                    game_multi.increase_round_number(game_name)
                    
                if game_flag_number < (number_of_players) * 5 - 1:
                    """
                    Check to see if the last flag of the game has been reached
                    e.g 'number_of_players' = 5, 5 * 5 = 20 but index number of last flag
                    is 24(25 flags in list, 5 for each player) hence - 1
                    
                    Increases turn_of_player before adding to elapsed time of previous player
                    so that on the first turn, last player's elapsed time wont be updated as a result of
                    that player being classed as the previous player of the first player
                    """ 
                    game_multi.increase_flag_number(game_name)
                    game_multi.set_turn_of_player(game_name, number_of_players)
                    game_multi.set_start_time_for_current_player(game_name)
                    game_multi.add_to_previous_players_elapsed_time(game_name)
                game_multi.increase_player_score(turn_of_player, points, game_name)
                game_multi.reset_incorrect_answers(turn_of_player, game_name)
                game_multi.reset_points(game_name)
                return redirect(url_for("gameMulti", game_name=game_name))
            else:
                game_multi.append_incorrect_answers(turn_of_player, request.form["answer"], game_name)
                game_multi.decrease_points(game_name)
                return redirect(url_for("gameMulti", game_name=game_name))            
        elif "skip" in request.form:
            if round_number == 5 and turn_of_player == index_num_of_last_player:
                game_multi.add_to_elapsed_time_of_player_for_last_flag(game_name, time.time())
                game_multi.update_player_list(game_name)
                game_multi.overwrite_game_value(game_name, "game_state", "ended")
            elif round_number < 5 and turn_of_player == index_num_of_last_player:
                game_multi.increase_round_number(game_name)
                
            if game_flag_number < ((number_of_players) * 5) - 1:
                game_multi.increase_flag_number(game_name)
                game_multi.set_turn_of_player(game_name, number_of_players)
                game_multi.set_start_time_for_current_player(game_name)
                game_multi.add_to_previous_players_elapsed_time(game_name)
            game_multi.reset_incorrect_answers(turn_of_player, game_name)
            game_multi.reset_points(game_name)
            return redirect(url_for("gameMulti", game_name=game_name))
            
    if game_flag_number == 0: 
        """
        Set start time of the first player for the first turn of the first round.
        
        If placed before conditions for request.form == "POST",
        sets the start time of the first player again at the start of the second turn
        resulting in an inaccurate elapsed time of the first turn of the first round.
        """
        game_multi.set_start_time_for_current_player(game_name)
        
    return render_template("game-multi.html", 
                            players=list_of_players,
                            times_list=elapsed_times,
                            flag_url=flag, 
                            turn_of_player=turn_of_player, 
                            incorrect_answers=current_player_incorrect_answers,
                            player_score=current_player_score,
                            points=points,
                            round_number=round_number,
                            game_state=game_state,
                            current_player=current_player,
                            number_of_players=number_of_players)

if __name__ == "__main__":
    app.run(host = os.environ.get("IP"),
            port = int(os.environ.get("PORT", "5000")),
            debug = True)
            

