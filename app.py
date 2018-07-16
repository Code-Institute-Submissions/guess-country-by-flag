import os
import json
from flask import Flask, render_template, request, redirect, url_for
from utils.utils import *

app = Flask(__name__)

file_path_single = "data/users.json"


@app.route("/", methods=["GET", "POST"])
def index():
    remove_user_from_data_file(file_path_single, "testUser")
    remove_user_from_data_file(file_path_single, "testUser2")
    
    if request.method == "POST":
        if request.form["action"] == "Play alone":
            return redirect(url_for("signIn"))
        else:
            return redirect(url_for("createRoom"))
    return render_template("index.html")


  
@app.route("/sign-in", methods=["GET", "POST"])
def signIn():
    username_error = None
    password_error = None
    if request.method == "POST":
        if request.form["action"] == "Enter game":
            if check_if_password_matches(file_path_single, request.form["username"], request.form["password"]):
                return redirect(url_for("gameMenu", username=request.form["username"]))
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
            username_error = "Username is taken"
    return render_template("sign-up.html", username_error=username_error)


   
@app.route("/game-menu/<username>", methods=["GET", "POST"])
def gameMenu(username):
    return render_template("game-menu.html")



@app.route("/create-room", methods=["GET", "POST"])
def createRoom():
    if request.method == "POST":
        create_data_file(request.form["game_name"])
        return redirect(url_for("addPlayers", game_name=game_name))
    return render_template("create-room.html")

 
    
@app.route("/add-players/<game_name>", methods=["GET", "POST"])
def addPlayers(game_name):
    username_error = None
    number_of_players_error = None
    
    with open(create_file_path(game_name), "r") as json_data:
        player_list = json.load(json_data)
        
    if request.method == "POST":
        for i in range(5):
            if str(i) in request.form:
                remove_user_from_data_by_index(create_file_path(game_name), i)
                return redirect(url_for("addPlayers", game_name=game_name))
        if "action" in request.form:
            delete_json_file(game_name)
            return redirect(url_for("gameMulti"))
        elif "username" in request.form:
            if check_number_of_multi_users(create_file_path(game_name)) == False:
                if check_if_username_does_exist(create_file_path(game_name), request.form["username"]):
                    add_user_to_data_file(create_file_path((game_name)), request.form["username"], "none")
                    return redirect(url_for("addPlayers", game_name=game_name))
                else:
                    username_error = "Username is taken"
            else:
                number_of_players_error = "The maximum number of players has been reached"
            
    return render_template("add-players.html", username_error=username_error, number_of_players_error=number_of_players_error, player_list=player_list)



if __name__ == "__main__":
    app.run(host = os.environ.get("IP"),
            port = int(os.environ.get("PORT")),
            debug = True)
            

