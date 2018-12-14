# User-Stories

* As a user, on the first page I am presented with an option to create a new user or login as an existing user.
   
   **New user page:**
   * As a user, when I choose to create a new user, I am redirected to another page where I am presented with two input fields, one for 		          username and another for password and a button to submit the input.
   * As a user, when I create a new user, if my chosen username already exists, I am informed of it and told to pick another username.
   * As a user, when I submit my chosen username and password, I am redirected to the game menu page.
	
   **Existing user page:**
   * As a user, when I choose to login as an existing user, I am redirected to another page wher I am presented with two input fields, one 	          for my username and one for my password
   * As a user, if I input in a username that does not exist, I am informed of it and asked to input in a username that exists
   * As a user, if I input in my password and it doesn't match, I am informed of it and asked to input in my password again
   * As a user, if I input my username and the matching password, I am redirected to the game menu page.

* As a user, on the game menu page I am presented with a welcome message directed at my username and two buttons, one to start the game and       another to see the leaderboard.
	
   **Start Game page:**
   * As a user, when I start the game, I am redirected to the game page and presented with a number of elements. My username is displayed on           the top along with a button allowing me to quit the game in case I don’t know the correct answer. A progress bar reflecting my current            score, my current score(0) compared against the total maximum score, a picture of a flag in the center, a text input field where I can            type my answer and a button to submit my answer. 

   **Leaderboard page:**
   * As a user, if I check the leaderboard, I am presented with a list of top ten scores. The leaderboard consists of rank, player and score           columns. Each row has a rank, a username and that user's score. The score is displayed in a descending order, starting from the highest 	  to the lowest while the rank in ascending order, 1 being the top rank.

* As a user, when I enter the correct answer and submit it, my score increments by 1, the progress bar increments to reflect it, I am presented     with a new picture of a flag and the text input field is cleared.

* As a user, when I enter a wrong answer, the text input field is cleared and my wrong answer is displayed below the flag. My score doesn’t         change.

* As a user, if I can't get the right answer, I can quit the game early at which point I am redirected to the leaderboard. If my score was high    enough to qualify, my username and score is displayed on the leaderboard along with my rank.

* As a user, if I get all the answers correct, I am redirected to the leaderboard where I can see my score on the leaderboard.
 
* As a user, I can play the game at the same time as other users. Each user plays their own separate instance of the game.

* As a user, if my score is the same as another user’s score already shown on the leaderboard, the score which takes precedence is decided by       comparing total time played to get to that score. The shorter time takes precedence and that user’s score is pushed above the other score.

* As a user, if I quit the game or win, my progress is reset and I have to start from the beginning.

