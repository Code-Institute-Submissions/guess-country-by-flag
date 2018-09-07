# Guess The Flag game

 A "riddle me this" based game where players are presented with an image of a random flag and have to
 guess which country it belongs to.
 
 ## Features
 
 * 2 game modes:
    * Single player cosisting of 20 levels(or flags).
    * Local multiplayer where up to 5 players can play against each other for 5 rounds, each player 
      having a single turn per round. Multiplayer games older than a day are automatically deleted from data.
 * A scoring system with 5 initial points per level/turn. Points are reduced by 2 for each incorrect
   answer, resulting in 0 points after 3 incorrect answers. Full amount of points has to be scored in order 
   to win the game.
 * Logging and displaying incorrect answers for level being played.
 * Abillity to skip questions in the event of not knowing the correct answer resulting in 0 points being scored
   for that level/turn.
 * Ability to give up/quit the game early resulting in not being placed on the leaderboard.
 * 200 flags of sovereign states
 * Persistent user accounts with players being able to choose their username and password.
 * A global, persistent leaderboard visible to all players in single player mode. Position on the leaderboard is
   decided by total score at the end of the game as well as total time played.
 * A local, non-persistent leaderboard for multiplayer mode where players can see how they ranked against each other 
   at the end of the game.
 
## Technologies
 * Layout and presentation created through a mix of HTML, CSS/SCSS and Javascript + jQuery
 * Jinja, a template engine used for generating web pages
 * Python used for the functionality of the game
 * Flask, a python micro web framework used to structure the back-end
 * Unittest python testing framework used for testing the application.
 * JSON file format used for data

## Deployment 

Deployed to Heroku

Link: [https://guess-the-country-by-flag.herokuapp.com/).

## Testing 

Functionality tested with the use of Unittest, a python testing framework, using a "test after" approach as well as manually.
Tested for responsivness on mobile, tablet and desktop devices and for cross-browser support.


## Installation 

Clone the repository by copying the clone url

In the terminal type `git clone` followed by the copied url

`cd` into `guess-the-flag`, in the terminal type `pip3 install -r requirements.txt` to install all the dependencies then open
`app.py`


To run all tests, in the terminal type in `python3 -m unittest`

## License

MIT
