import os
import json
from flask import Flask, render_template, request, redirect, url_for
from utils.utils import *

app = Flask(__name__)

file_path_single = "data/users.json"
file_path_multi = "data/multi_users.json"


@app.route("/", methods=["GET", "POST"])
def index():
    remove_user_from_data_file(file_path_single, "testUser")
    remove_user_from_data_file(file_path_single, "testUser2")
    
    with open(file_path_multi, "r") as json_data:
        player_list = json.load(json_data)
        
    player_list = []
    
    with open(file_path_multi, "w") as json_data:
        json.dump(player_list, json_data)
    
    if request.method == "POST":
        if request.form["action"] == "Play alone":
            return redirect(url_for("signIn"))
        else:
            return redirect(url_for("addPlayers"))
    return render_template("index.html")


  
@app.route("/sign-in", methods=["GET", "POST"])
def signIn():
    username_error = None
    password_error = None
    if request.method == "POST":
        if request.form["action"] == "Enter game":
            if check_if_password_matches(file_path_single, request.form["username"], request.form["password"]):
                return redirect(url_for("gameMenu"))
            elif check_if_username_does_exist(file_path_single, request.form["username"]):
                username_error = "A user with this username does not exist"
            else:
                password_error = "Wrong password, try again"
            
    return render_template("sign-in.html", password_error=password_error, username_error=username_error)


   
@app.route("/sign-up", methods=["GET", "POST"])
def signUp():
    username_error = None
    if request.method == "POST":
        if check_if_username_does_exist(file_path_single, request.form["username"]):
            add_user_to_data_file(file_path_single, request.form["username"], request.form["password"])
            return redirect(url_for("gameMenu"))
        else:
            username_error = "This username is taken"
    return render_template("sign-up.html", username_error=username_error)


   
@app.route("/game-menu", methods=["GET", "POST"])
def gameMenu():
    return render_template("game-menu.html")
    

    
@app.route("/add-players", methods=["GET", "POST"])
def addPlayers():
    username_error = None
    number_of_players_error = None
    
    with open(file_path_multi, "r") as json_data:
        player_list = json.load(json_data)
        
    
    if request.method == "POST":
        if "remove_player" in request.form:
            remove_last_user_from_multi_data_file(file_path_multi)
            return redirect(url_for("addPlayers"))
        elif "username" in request.form:
            if check_number_of_multi_users(file_path_multi) == False:
                if check_if_username_does_exist(file_path_multi, request.form["username"]):
                    add_user_to_data_file(file_path_multi, request.form["username"], "none")
                    return redirect(url_for("addPlayers"))
                else:
                    username_error = "Player already exists"
            else:
                number_of_players_error = "The maximum number of players has been reached"
            
        
    return render_template("multiplayer.html", username_error=username_error, number_of_players_error=number_of_players_error, player_list=player_list)



if __name__ == "__main__":
    app.run(host = os.environ.get("IP"),
            port = int(os.environ.get("PORT")),
            debug = True)
            

