# Guess The Flag

A "riddle me this" game created using the Flask microframework where players are presented with an single random flag image and have to
guess which country it belongs to. Features two game modes to choose from, a single player mode with a global online leaderboard and a 
local multiplayer mode where players can play against each other on a single device and are presented with a local leaderboard.


## UX

The game is designed to emulate the feel of an actual game so it doesn't include a navigation bar or a footer and is instead contained in a container at the center
of the page. 

The user is first presented with a choice between game modes, either single player or multiplayer. 

In the case of selecting single player, the user is taken to a simple login page containing an option to go to the account registration page in case a user does not have an account yet. 
Once the user logs into the game, they are then taken to the main game menu where they have a choice of either starting a new game, checking out the leaderboards or logging out to the 
game mode selection page.
In the case of selecting multiplayer, the user is taken to a game room creation page where they have to input the game room name, the name of the game room cannot be a name of a game room
which already exists. Once thats done, the user is presented with a page where they can add players to the game up to a maximum of 5 players, each player added also can be removed from the
list by pressing a button beside their username. The game cannot be started without less than two player first being added. 
Each player has to select a unique username and afterwards they can begin the game.

On bigger screens(>1025px) I thought it best to limit the game in size to about 50% of the screen width in order to not overwhelm the player with the size of the flag and to
have the inputs closer together for ease of use.

The game page itself features:
* Username display to provide feedback to the user that they are in fact playing on their account.
* A progress bar reflecting the percentage of the game finished in addition to textual feedback stating what question the user is on, out of the total number of questions.
* Score and remaining points being displayed just under the progress bar in order to group the progress feedback in one place.
* 3 buttons, one for skipping a question, one for giving up on the game if the player wants to quit early and another for submitting their question. Each button is color coded to make
it easier for the user to see which is which.
  * The 'give up' button is placed out of the way of the rest of the buttons, up top with the progress feedback group so the user doesn't accidentally click it. 
  If a user gives up on the game, they are still presented with their overall score up until that point and the duration they played for but they are not added to the leaderboard.
  * The skip button awards no points for the question skipped.
* An area where a user can input their answer. Once the answer has been input, it can be submitted either by the submit button or by pressing the Enter key on the keyboard. Autocomplete
is disabled on the text input field so any correct answers aren't later displayed during another game.
* A display of each incorrect answer input by the user which is initially hidden until an incorrect answer is submitted. I thought it best to decrement the amount of points gained upon guessing
the answer for each incorrect answer until the remaining points equal to zero. This way a player cannot keep guessing until they get the right answer and still get the full amount of points for it, while
at the same time the player can keep guessing however long they want, being only penalized by the increasing duration of their time played without being forced to skip to the next question
upon getting the answer incorrect three times.
* The field containing the flag image itself.
* Once the last question is answered or skipped, the player is taken to the leaderboard page where they are presented with a message informing them of their overall score and duration of 
their game. The player can then choose to either play another game or view the leaderboard by pressing 'continue' where if they qualified, their username, score and time played will be displayed.
* The global leaderboard displays only the top 10 players. If a player is present on the leaderboard, they will be highlighted on it in order to make it more obvious where they placed.
* Score is determined by overall points and time played in ordered to differentiate between players with equal scores.

The multiplayer game page is very similar in features but differs by:
* Each player is coded with a different color.
* Additional textual and visual feedback to reflect which player's turn it is, as well as color coding elements such as username, turn feedback or list of incorrect answers to current
player's color.
* Instead of progressing through 20 questions, players progress through rounds of which there is 5 total. For each round, a player has to guess a single flag, once all player's have had a 
turn, then the round is incremented. Overall, each player gets to guess 5 flags in order to not keep the game going on for too long.
* Multiplayer features only a local leaderboard where players are ranked against each other at the end of the game. Their scores don't count towards the global leaderboard.
* Once players finish the game they can play another game or quit to the game mode selection page.
* The 'give up' button is removed to prevent players from leaving while the game is ongoing.

Mockups in a pdf format and user stories can be found here [UX assets](assets/ux)

The final version of the project differs from the mockups. 
As I developed the project I would realize that some of the design decisions weren't 
the right solutions and I would update them on the go.

## Features 

* 2 game modes:
   * Single player cosisting of 20 levels(or flags).
   * Local multiplayer where up to 5 players can play against each other for 5 rounds, each player 
     having a single turn per round. Multiplayer games older than a day are automatically deleted from data.
* A scoring system with 5 initial points per level/turn. Points are reduced by 2 for each incorrect
  answer, resulting in 0 points after 3 incorrect answers. Full amount of total points has to be scored in order 
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

<<<<<<< HEAD
=======
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
 
>>>>>>> 0216f9eb6016ca7a8a49470affa0fa3fe5b1b3e0
## Technologies

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
  * Used for structuring content
* [SCSS](https://sass-lang.com/)
  * Used for the presentation of the page
* [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)
  * Used for the layout of the page
* [JavaScript](https://www.javascript.com/)
  * Used for interactive functionality
* [JQuery](https://jquery.com/)
  * Used to simplify DOM manipulation
* [Flask](http://flask.pocoo.org/)
  * Used for structuring the back-end
* [Jinja](http://jinja.pocoo.org/)
  * Used for generating web pages
* [Python](https://www.python.org/)
  * Used for logic of the game
* [UnitTest](https://docs.python.org/3/library/unittest.html)
  * Used for automatic python tests
* [JSON](https://www.json.org/)
  * File format used for data
* [Markdown](https://en.wikipedia.org/wiki/Markdown)
  * Used for formatting user_stories.md and README.md

## Deployment 

Deployed on Heroku at [Guess The Flag](https://guess-the-country-by-flag.herokuapp.com/).

## Testing 

### Manual Tests

1. Sign-in page:

   i. Attempt to log in without having a registered account, verify that error message appears stating 'A user with this username does not exist'
   
   ii. Attempt to log in with a registered account but input the wrong password, verify an error message appears stating 'Wrong password, try again'
   
   iii. Attempt to log in with a registered account and a correct password, verify being redirected to the game menu page

2. Sign-up page:

   i. Attempt to create an account with an existing username, verify an error message appears stating 'Username is taken'
   
   ii. Attempt to create an account with a unique username and a password shorter than 8 characters, verify being informed that the password has to be at least 8 characters long
   
   iii. Attempt to create an account with a unique username, verify being redirected to the game menu page
   
3. Game-menu page:

   i. Attempt to start a new game, verify being redirected to the game page
   
   ii. Attempt to access the leaderboard page by pressing the 'Go To Leaderboards' button, verify being redirected to the leaderboard page
   
   iii. Attempt to log out, verify being redirected back to the game mode selection page and having to log in again
   
4. Game-single page:

   i. On entering the page verify that it starts at question 1 and the progress bar reflects that, theres a flag image present,
   your username is displayed on the top, current score is equal to 0 and remaining points is equal to 5
   
   ii. Attempt to enter an incorrect answer, verify a list of incorrect answers appears below the game containing the answer
   you submit and remaining points is now equal to 3
   
   iii. Attempt to keep entering incorrect answers, verify that after 2 more your remaining score is equal to 0 and doesn't go into
   negative value with more incorrect answers submitted. Verify that all your incorrect answers are being listed at the bottom of the game
   
   iv. Attempt to skip a question, verify that a new flag appears, question number is now 2 out of 20 instead of 1 out of 20 with the
   progress bar reflecting that, your score is still 0, remaining points have been reset back to 5 and the list of incorrect
   answers has been reset as well, not being displayed anymore since currently there are no incorrect answers.
   
   v. Attempt to enter a correct answer, verify that you are taken to the next question, now 3 out of 20 with
   the progress bar reflecting it, your score has increased by 5
   
   vi. Attempt to get to the end of the game by either skipping question 20 out of 20 or answering it correctly, verify
   being redirected to the leaderboard page where a message informs you of your overall score for that game and the time you 
   played for. Verify you are presented with two options to either continue to the leaderboard or play again.
   
      * Attempt to play again, verify being redirected to game page with all values and scores reset and being shown a new 
      random flag image.
      
      * Attempt to continue, verify the leaderboard shows top 10 users with their username, score and time played listed.
      If you appear on the leaderboard, verify you are highlighted and your listing stands out from the rest.
   
   vii. Attempt to press the 'give-up' button, verify being redirected to the leaderboard page where you are shown a message
   informing you of your score and time played. Verify you don't appear on the leaderboard.
   
5. Create-room page:
 
   i. Attempt to create a room with a name of an already existing game room, verify a message appears stating 'A game with that name already exists'
   
   ii. Attempt to create a room with a unique name, verify being redirected to the add-players page

6. Add-players page:

   i. Attempt to start the game without adding any players, verify a message appears stating 'At least 2 players are needed to start the game'.
   
   ii. Attempt to start the game with just one player, verify a message appears stating 'At least 2 players are needed to start the game'

   iii. Attempt to add a player, verify a player field containing chosen username apepars in the list below
   
   iv. Attempt to add a player with an existing player's username, verify a message appears stating 'Username is taken'

   v. Attempt to add more than 5 players, verify a message appears stating 'The maximum number of players has been reached'
   
   vi. Attempt to remove a player from the list, verify only that player gets removed
   
   vii. Attempt to start the game with 2-5 players, verify being redirected to the game page
   
   viii. Attempt to add a player without inputing a username, verify being informed that a username has to be supplied
   
7. Game-multi page:

   i. On start of game, verify textual and visual progress feedback is the color of the current player. Verify the round is 1 out of 5,
   under the information stating which round number it is, verify that text stating {{username}}'s turn...' is displayed, where {{username}}
   is the current player's username. Verify there are a number of blocks equal to the number of players beneath this text and the first block is
   blue in color while the rest white signifying it is the first player's turn.
   
   ii. Verify the game otherwise behaves like the singleplayer game in regards to answers and score
   
   iii. Attempt to skip or answer the question and verify that the progress bar hasnt increased or round number hasn't increased.
   Verify that the username display has changed to show the next player's username and colors of elements have changed to that
   player's colors, as well as that verify that the second block is now colored and the rest are white.
   Verify that the second player starts with a new random flag and his own score.
   
   iv. Attempt to finish the game, verify that for each round, each player gets a turn, verify that one player cannot affect the
   score of another and that as the game progresses, the round number increases and the progress bar incremements.
   Verify that upon reaching the last round and the last player's turn, if that player skips or answers the question correctly the game finishes.
   
   v. Finish the game and verify being redirected to a leaderboard where all players for that game are listed including their username,
   score, time played and color. Verify that players are places in descending order based on score and ascending order of time played.
   
   vi. Attempt to play again and verify being redirected to a new multiplayer game.
   
   vii. Attempt to continue and verify being redirected to the game mode selection menu.


Tested on mobile, tablet and desktop devices using different devices and developer tools,
and in different browsers(Firefox, Microsoft Edge and Google Chrome) to test browser compatibility.

### Automated Tests

Python logic extensively tested with unittest, a python unit testing framework. All tests pass. They can be found at [Unit Tests](tests/) and are split into 
multiple files for better readability.

Additionally:

* [W3C Markup Validation Service](https://validator.w3.org/)
  * Used for testing html
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
  * Used for testing css
* [Mobile Friendly Test](https://search.google.com/test/mobile-friendly)
  * Used for testing mobile layout
* [JSHint](https://jshint.com/)
  * Used for testing JavaScript
 
### Bugs

* Once a room is created, if a user return to the create-room page, the room created before that will not be deleted and the
name supplied will be taken. Solved by deleting any game rooms that are older than a day so as not to keep storing them unnecessarily.

## Installation 

Clone the repository by copying the clone url

In the terminal type `git clone` followed by the copied url

`cd` into `guess-the-flag`, in the terminal type `pip3 install -r requirements.txt` to install all the dependencies then open
`app.py`


To run all tests, in the terminal type in `python3 -m unittest`

## Credits

### Countries' data

* JSON formatted countries' data used for countries common and official names - [mledoze GitHub](https://github.com/mledoze/countries/blob/master/countries.json)

### Images 

* Background image - [Wikipedia](https://en.wikipedia.org/wiki/File:World_blank_map_countries.PNG)
* Flag images - [Wikipedia](https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags)

### CSS 

* Hover effects - [Hover.css](http://ianlunn.github.io/Hover/)

#### Fonts

* Roboto - [Google Fonts](https://fonts.google.com/)
* Font Awesome - [Font Awesome](https://fontawesome.com/?from=io)


## License

MIT
