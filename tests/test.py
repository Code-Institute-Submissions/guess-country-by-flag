import unittest
import json
import sys
import os

from utils import countries, files, game_single, leaderboard_single, misc, users, game_multi




class app_tests(unittest.TestCase):
    
    """ Test that a user object can be created containing username and score""" 
    def test_can_create_user_object(self):
        
        user = users.create_user("testUser", "ka10", 0, "none")
        
        self.assertEqual("testUser", user["username"])
        self.assertEqual("ka10", user["password"])
        self.assertEqual(0, user["score"])
        self.assertEqual("none", user["game"])
        self.assertEqual(user, {"username": "testUser", "password": "ka10", "score": 0, "game": "none"})
    
    
    
    """ Test whether a user can be added to data file """
    def test_if_user_can_be_added(self):
        users.add_user_to_data_file("users", "testUser", "ka10", "none")
        
        with open("data/users.json", "r") as json_data:
            data = json.load(json_data)
        
        user = {}
        
        for obj in data:
            if obj["username"] == "testUser":
                user = obj
        
        self.assertIn(user, data)
        
        users.remove_user_from_data_file("users", "testUser")
    
    
    
    """ Test whether a username already exists in data file, should return 'True' if doesn't and 'Flase' if does """
    def test_if_username_does_not_exist(self):
        users.add_user_to_data_file("users", "testUser", "ka10", "none")
        does_not_exist = users.check_if_username_does_exist("users", "I-Dont-Exist")
        does_exist = users.check_if_username_does_exist("users", "testUser")
        
        self.assertTrue(does_not_exist)
        self.assertFalse(does_exist)
        
        users.remove_user_from_data_file("users", "testUser")
    
    
    
    """ Test whether input password matches the password for that username """
    def test_if_password_matches_username(self):
        users.add_user_to_data_file("users", "testUser", "ka10", "none")
        user_one_password_not_match = users.check_if_password_matches("users", "testUser", "ka9")
        user_one_password_matches = users.check_if_password_matches("users", "testUser", "ka10")
        
        self.assertFalse(user_one_password_not_match)
        self.assertTrue(user_one_password_matches)

        users.remove_user_from_data_file("users", "testUser")
        
        
    
    """ Test whether a user can be added to the data file if a user with the same username already exists """
    def test_if_can_add_user_when_username_exists(self):
        users.add_user_to_data_file("users", "testUser", "ka10", "none")
        does_exists = users.check_if_username_does_exist("users", "testUser")
        
        def check_if_added():
            if users.add_user_to_data_file("users", "testUser", "ka10", "none"):
                return True
            else:
                return False
        
        self.assertFalse(does_exists)
        self.assertFalse(check_if_added())
    
        users.remove_user_from_data_file("users", "testUser")
       
       
       
    """ Test whether a data file can be created """
    def test_if_data_file_can_be_created(self):
        files.create_data_file("testFile")
        
                
        self.assertTrue(files.check_if_file_exists("testFile"))
        
        
        
    """ Test whether a file can be checked to exist or not """
    def check_if_can_be_check_to_exist(self):
        
        self.assertTrue(files.check_if_file_exists("testFile"))  
        self.assertFalse(files.check_if_file_exists("not-existing-file"))
        
        
        
    """ Test whether a data file can be deleted """
    def test_if_data_file_can_be_deleted(self):
        files.delete_data_file("testFile")
        
        self.assertFalse(files.check_if_file_exists("testFile"))
    
    
    
    """ Test whether a data file can be appended to """
    def test_if_can_append_to_file(self):
        files.create_data_file("testFile")
        
        data = files.read_data_file("testFile")
        data_two = []
        self.assertEqual(data_two, data)
        
        files.append_to_file("hello", "testFile")
        data_three = files.read_data_file("testFile")
        self.assertIn("hello", data_three)
        
        files.delete_data_file("testFile")
        
    
    
    """ Test whether a file can be overwritten """
    def test_if_file_can_be_overwritten(self):
        files.create_data_file("testFile")
        
        data = files.read_data_file("testFile")
        data_two = []
        self.assertEqual(data_two, data)
        
        files.overwrite_file("testFile", "hello")
        data_overwritten = files.read_data_file("testFile")
        self.assertIn("hello", data_overwritten)
        self.assertEqual("hello", data_overwritten)
        
        files.delete_data_file("testFile")
        
    
        
    """ Test whether a string containing the path to a file can be created """
    def test_if_string_path_to_file_can_be_created(self):
        files.create_data_file("testFile")
        
        file_path = files.create_file_path("testFile")
        
        self.assertEqual("data/testFile.json", file_path)
        self.assertEqual(str, type(file_path))
        
        files.delete_data_file("testFile")
        
    
    
    """ Test whether a user object can be removed from data file by its index number """
    def test_if_can_remove_user_by_index(self):
        files.create_data_file("testUsersList")
        file_path = files.create_file_path("testUsersList")
        users.add_user_to_data_file("testUsersList", "testUser", "none", "none")
        users.add_user_to_data_file("testUsersList", "testUser2", "none", "none")
        
        userIndexZero = users.create_user("testUser", "none", 0, "none")
        userIndexOne = users.create_user("testUser2", "none", 0, "none")
        
        with open(file_path, "r") as json_data:
            data = json.load(json_data)
        self.assertEqual(data[1], userIndexOne)
        
        users.remove_user_from_data_by_index("testUsersList", 0)
        with open(file_path, "r") as json_data:
            data = json.load(json_data)
        self.assertEqual(data[0], userIndexOne)
        
        files.delete_data_file("testUsersList")
    
    
    """ Check that a user score can be returned """
    def test_if_user_score_returned(self):
        users.add_user_to_data_file("users", "testUser", "none", {})
        users.reset_user_score("testUser")
        
        returned_score = users.return_user_score("testUser")
        self.assertEqual(0, returned_score)
        
        users.increase_user_score("testUser", 200)
        updated_score = users.return_user_score("testUser")
        self.assertEqual(200, updated_score)
        
        users.remove_user_from_data_file("users", "testUser")
        
    
    
    """ Check that a user score can be increased by a given number of points """
    def test_if_user_score_increases(self):
        users.add_user_to_data_file("users", "testUser", 0, "none")
        users.reset_user_score("testUser")
        users.increase_user_score("testUser", 2)
        
        with open("data/users.json", "r") as json_data:
            data = json.load(json_data)
        current_user = {}
        for user in data:
            if user["username"] == "testUser":
                current_user = user
        
        self.assertEqual(2, current_user["score"])
        
        users.increase_user_score("testUser", 10)
        
        with open("data/users.json", "r") as json_data:
            data = json.load(json_data)
        current_user = {}
        for user in data:
            if user["username"] == "testUser":
                current_user = user
                
        self.assertEqual(12, current_user["score"])
        
        users.remove_user_from_data_file("users", "testUser")
        
        
        
    """ Check whether a user score can be reset to zero"""
    def test_if_user_score_can_be_reset(self):
        users.add_user_to_data_file("users", "testUser", "none", {})
        users.increase_user_score("testUser", 5)
        test_score = users.return_user_score("testUser")
        
        self.assertEqual(5, test_score)
        
        users.reset_user_score("testUser")
        updated_test_score = users.return_user_score("testUser")
        
        self.assertEqual(0, updated_test_score)
        
        users.remove_user_from_data_file("users", "testUser")
        
        
        
    """ Check to see if a list of a given number of random numbers ranging between 0 and 204 can be created """
    def test_if_list_of_random_numbers_can_be_created(self):
        
        list_of_random_numbers = misc.generate_random_numbers(5)
        list_of_other_numbers = [-1, 205, 34, "a", 55, 1000, 0]
        
        def check_if_between_given_numbers(list_of_numbers):
            for num in list_of_numbers:
                if num > 0 and num < 205:
                    return True
                else:
                    return False
            
        self.assertEqual(5, len(list_of_random_numbers))
        self.assertEqual(int, type(list_of_random_numbers[0]))
        self.assertEqual(int, type(list_of_random_numbers[1]))
        self.assertEqual(int, type(list_of_random_numbers[2]))
        self.assertEqual(int, type(list_of_random_numbers[3]))
        self.assertEqual(int, type(list_of_random_numbers[4]))
        self.assertTrue(check_if_between_given_numbers(list_of_random_numbers))
        self.assertFalse(check_if_between_given_numbers(list_of_other_numbers))
        
        
        
    """ Test whether a game object can be created containing keys and values for question number(1),
    points(5), list of countries([]), win state(str), game duration(seconds) and list of incorrect answers([random numbers]) """
    def test_if_can_create_game_obj(self):
        game_object = game_single.create_game_object()
            
        self.assertIn("countries", game_object)
        self.assertIn("question_number", game_object)
        self.assertIn("points", game_object)
        self.assertIn("incorrect_answers", game_object)
        self.assertIn("win", game_object)
        self.assertIn("game_duration", game_object)
        self.assertEqual(type([]), type(game_object["countries"]))
        self.assertEqual(int, type(game_object["countries"][0]))
        self.assertEqual(type([]), type(game_object["incorrect_answers"]))
        self.assertEqual(1, game_object["question_number"])
        self.assertEqual(5, game_object["points"])
        self.assertEqual("not-won", game_object["win"])
        self.assertEqual(0, game_object["game_duration"])
        self.assertEqual(type({}), type(game_object))



    """ Test that a value of a key inside a given game object can be extracted """
    def test_value_of_key__in_game_obj_can_be_extracted(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        
        points_of_game = game_single.extract_key_value_from_game_obj("gameTest", "points")
        question_number_of_game = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        
        self.assertEqual(5, points_of_game)
        self.assertEqual(1, question_number_of_game)
        
        users.remove_user_from_data_file("users", "gameTest")
        
        
        
    """ Test that question number inside game object can be increased by 1 """
    def test_that_question_number_can_be_increased(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        
        question_number_of_game = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        self.assertEqual(1, question_number_of_game)
        
        game_single.increase_question_number("gameTest")
        question_number_of_game_updated = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        self.assertEqual(2, question_number_of_game_updated)
        
        users.remove_user_from_data_file("users", "gameTest")
        
    
    
    """ Test that question number can be reset back to 1 """
    def test_that_question_number_can_be_reset(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        
        question_number_of_game = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        self.assertEqual(1, question_number_of_game)
        
        
        game_single.increase_question_number("gameTest")
        question_number_of_game_updated = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        self.assertEqual(2, question_number_of_game_updated)
        
        game_single.reset_question_number("gameTest")
        question_number_reset = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        self.assertEqual(1, question_number_reset)
        
        users.remove_user_from_data_file("users", "gameTest")


    """ Test that a user's incorrect answer can be appended to a list inside the game obj """
    def test_if_incorrect_answer_can_be_appended(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        
        list_of_incorrect_answers = game_single.extract_key_value_from_game_obj("gameTest", "incorrect_answers")
        self.assertEqual([], list_of_incorrect_answers)
        self.assertEqual(0, len(list_of_incorrect_answers))
        
        game_single.append_incorrect_answers("gameTest", "im-a-wrong-answer")
        list_of_incorrect_answers_updated = game_single.extract_key_value_from_game_obj("gameTest", "incorrect_answers")
        self.assertIn("im-a-wrong-answer", list_of_incorrect_answers_updated)
        self.assertEqual(1, len(list_of_incorrect_answers_updated))
        
        users.remove_user_from_data_file("users", "gameTest")
        
        
        
    """ Test that incorrect answers can be reset back to an empty list """
    def test_if_incorrect_answer_list_can_be_reset(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        game_single.append_incorrect_answers("gameTest", "im-a-wrong-answer")
        game_single.append_incorrect_answers("gameTest", "im-a-wrong-answer-too")
        
        list_of_incorrect_answers = game_single.extract_key_value_from_game_obj("gameTest", "incorrect_answers")
        self.assertEqual(["im-a-wrong-answer", "im-a-wrong-answer-too"], list_of_incorrect_answers)
        
        game_single.reset_incorrect_answers("gameTest")
        list_of_incorrect_answers_updated = game_single.extract_key_value_from_game_obj("gameTest", "incorrect_answers")
        self.assertEqual([], list_of_incorrect_answers_updated)
        
        users.remove_user_from_data_file("users", "gameTest")
        
        
        
    """ Test that points can be decreased by 2, if points are less than 2 they are reduced to 0 """
    def test_if_can_reduce_points(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        
        points = game_single.extract_key_value_from_game_obj("gameTest", "points")
        self.assertEqual(5, points)
        
        game_single.decrease_round_points("gameTest")
        points_two = game_single.extract_key_value_from_game_obj("gameTest", "points")
        self.assertEqual(3, points_two)
        
        game_single.decrease_round_points("gameTest")
        points_three = game_single.extract_key_value_from_game_obj("gameTest", "points")
        self.assertEqual(1, points_three)
        
        game_single.decrease_round_points("gameTest")
        points_four = game_single.extract_key_value_from_game_obj("gameTest", "points")
        self.assertEqual(0, points_four)
        
        users.remove_user_from_data_file("users", "gameTest")
        
        
        
    """ Test that points can be reset back to 5 """
    def test_if_can_reset_points(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        
        points = game_single.extract_key_value_from_game_obj("gameTest", "points")
        self.assertEqual(5, points)
        
        game_single.decrease_round_points("gameTest")
        points_two = game_single.extract_key_value_from_game_obj("gameTest", "points")
        self.assertEqual(3, points_two)
        
        game_single.reset_round_points("gameTest")
        points_two = game_single.extract_key_value_from_game_obj("gameTest", "points")
        self.assertEqual(5, points_two)
        
        
        
        users.remove_user_from_data_file("users", "gameTest")
        
    
        
    """ Test that win state can be set to a given value """
    def test_if_win_state_can_be_set(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        
        win_state = game_single.extract_key_value_from_game_obj("gameTest", "win")
        self.assertEqual("not-won", win_state)
        
        game_single.set_win_state("gameTest", "won")
        new_win_state = game_single.extract_key_value_from_game_obj("gameTest", "win")
        self.assertEqual("won", new_win_state)
        
        users.remove_user_from_data_file("users", "gameTest")
        
    
    
    """ Check if win state can be set to "lost" or "won" based on whether user score == 100 """
    def test_if_win_state_can_be_set_according_to_score(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        
        win_state = game_single.extract_key_value_from_game_obj("gameTest", "win")
        score = users.return_user_score("gameTest")
        self.assertEqual("not-won", win_state)
        self.assertEqual(0, score)
        
        game_single.check_for_win(score, "gameTest")
        
        updated_win_state = game_single.extract_key_value_from_game_obj("gameTest", "win")
        self.assertEqual("lost", updated_win_state)
        
        users.increase_user_score("gameTest", 100)
        updated_score = users.return_user_score("gameTest")
        self.assertEqual(100, updated_score)
        
        game_single.check_for_win(updated_score, "gameTest")
        
        updated_win_state_two = game_single.extract_key_value_from_game_obj("gameTest", "win")
        self.assertEqual("won", updated_win_state_two)
        
        users.remove_user_from_data_file("users", "gameTest")
        
    """ Test that given string can be converted to lowercase and then again to titlecase """
    def test_if_string_can_be_converted_to_lower_and_title_case(self):
        string = "HeLLO woRld"
        
        converted_string = misc.answer_to_lowercase_then_titlecase(string)
        
        self.assertEqual("Hello World", converted_string)
        
        
    """ Test that time can be set to specified value """
    def test_if_game_duration_can_be_set(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        
        time = game_single.extract_key_value_from_game_obj("gameTest", "game_duration")
        self.assertEqual(0, time)
        
        game_single.set_game_duration("gameTest", 20)
        new_time = game_single.extract_key_value_from_game_obj("gameTest", "game_duration")
        self.assertEqual(20, new_time)
        
        users.remove_user_from_data_file("users", "gameTest")
        
        
    
    """ Test that game duration can be calculated by taking away start time from end time """
    def test_if_game_duration_can_be_calculated(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        
        game_single.set_game_duration("gameTest", 13)
        start_time = game_single.extract_key_value_from_game_obj("gameTest", "game_duration")
        self.assertEqual(13, start_time)
        
        end_time = 40
        elapsed_time = misc.calculate_game_duration(start_time, end_time)
        self.assertEqual(27, elapsed_time)
        
        users.remove_user_from_data_file("users", "gameTest")
        
        
        
    """ Test that list of random country index numbers can be updated in game object """
    def test_if_list_of_random_numbers_of_countries_in_game_obj_can_be_updated(self):
        users.add_user_to_data_file("users", "gameTest", "none", game_single.create_game_object())
        
        list_of_numbers = game_single.extract_key_value_from_game_obj("gameTest", "countries")
        
        def check_if_every_item_is_int(li):
            for item in li:
                if type(item) == int:
                    return True
                else:
                    return False
                    
                    
        self.assertEqual(20, len(list_of_numbers))
        self.assertTrue(check_if_every_item_is_int(list_of_numbers))
        
        game_single.generate_new_list_of_random_countries("gameTest")
        new_list = game_single.extract_key_value_from_game_obj("gameTest", "countries")
        
        self.assertEqual(20, len(new_list))
        self.assertTrue(check_if_every_item_is_int(new_list))
        self.assertNotEqual(list_of_numbers, new_list)
        
        users.remove_user_from_data_file("users", "gameTest")
        
        
        
    """ Test that a value is returned for a given key of a country object """
    def test_if_value_is_returned_for_key_of_country(self):
        files.create_data_file("testCountryFile")
        
        test_country_obj = {
            "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag_of_Albania.svg/1024px-Flag_of_Albania.svg.png",
            "name-common": "Albania",
            "name-official": "Republic of Albania"
        }
        
        files.append_to_file(test_country_obj, "testCountryFile")
        data = files.read_data_file("testCountryFile")
        self.assertIn(test_country_obj, data)
        
        value_of_key = countries.return_value_for_key_in_country_object_of_index("testCountryFile", 0, "name-common")
        self.assertEqual("Albania", value_of_key)
        
        files.delete_data_file("testCountryFile")
        
    
    
    """ 
    Test whether a leaderboard player object can be created containing keys 
    for username, score, duration and rank 
    """
    def test_if_can_create_leaderboard_obj(self):
        users.add_user_to_data_file("users", "testPlayer", "none", game_single.create_game_object())
        leaderboard_object = leaderboard_single.create_leaderboard_player("testPlayer")
            
        self.assertIn("username", leaderboard_object)
        self.assertIn("duration", leaderboard_object)
        self.assertIn("score", leaderboard_object)
        self.assertIn("rank", leaderboard_object)
        self.assertEqual("testPlayer", leaderboard_object["username"])
        self.assertEqual(0, leaderboard_object["score"])
        self.assertEqual(0, leaderboard_object["rank"])
        self.assertEqual(0, leaderboard_object["duration"])
        
        users.remove_user_from_data_file("users", "testPlayer")
        
        
        
    """ 
    Test whether leaderboard data can be sorted by duration in ascending order and 
    score in descending order and rank changed in ascending order for each player 
    """
    def test_if_leaderboard_can_be_sorted(self):
        data = [{"duration": 3, "rank": 1, "score": 90, "username": "testPlayer1"}, 
                {"duration": 1, "rank": 999, "score": 50, "username": "testPlayer2"}, 
                {"duration": 1, "rank": 10, "score": 55, "username": "testPlayer3"}]
        
        files.overwrite_file("testLeaderboard", data)
        
        test_sorted_data = [{"duration": 3, "rank": 1, "score": 90, "username": "testPlayer1"}, 
                       {"duration": 1, "rank": 2, "score": 55, "username": "testPlayer3"}, 
                       {"duration": 1, "rank": 3, "score": 50, "username": "testPlayer2"}]
                
        
        
        leaderboard_single.update_leaderboard("testLeaderboard")
        sorted_data = files.read_data_file("testLeaderboard")
        
        self.assertEqual(test_sorted_data, sorted_data)
        
        files.delete_data_file("testLeaderboard")
        
        
        
    """ 
    Test a list of top ten player can be returned from leaderboard data 
    """
    def test_if_top_ten_returned(self):
        data = [{"duration": 1, "rank": 1, "score": 50, "username": "testPlayer1"}, 
                {"duration": 2, "rank": 2, "score": 50, "username": "testPlayer2"}, 
                {"duration": 3, "rank": 3, "score": 50, "username": "testPlayer3"},
                {"duration": 4, "rank": 4, "score": 50, "username": "testPlayer4"},
                {"duration": 5, "rank": 5, "score": 50, "username": "testPlayer5"},
                {"duration": 6, "rank": 6, "score": 50, "username": "testPlayer6"},
                {"duration": 7, "rank": 7, "score": 50, "username": "testPlayer7"},
                {"duration": 8, "rank": 8, "score": 50, "username": "testPlayer8"},
                {"duration": 9, "rank": 9, "score": 50, "username": "testPlayer9"},
                {"duration": 10, "rank": 10, "score": 50, "username": "testPlayer10"},
                {"duration": 11, "rank": 11, "score": 50, "username": "testPlayer11"},
                {"duration": 12, "rank": 12, "score": 50, "username": "testPlayer12"}]
        
        files.overwrite_file("testLeaderboard", data)
        
        test_top_ten = [{"duration": 1, "rank": 1, "score": 50, "username": "testPlayer1"}, 
                        {"duration": 2, "rank": 2, "score": 50, "username": "testPlayer2"}, 
                        {"duration": 3, "rank": 3, "score": 50, "username": "testPlayer3"},
                        {"duration": 4, "rank": 4, "score": 50, "username": "testPlayer4"},
                        {"duration": 5, "rank": 5, "score": 50, "username": "testPlayer5"},
                        {"duration": 6, "rank": 6, "score": 50, "username": "testPlayer6"},
                        {"duration": 7, "rank": 7, "score": 50, "username": "testPlayer7"},
                        {"duration": 8, "rank": 8, "score": 50, "username": "testPlayer8"},
                        {"duration": 9, "rank": 9, "score": 50, "username": "testPlayer9"},
                        {"duration": 10, "rank": 10, "score": 50, "username": "testPlayer10"}]
        
        top_ten = leaderboard_single.update_top_ten("testLeaderboard")
        
        self.assertEqual(test_top_ten, top_ten)
  
        files.delete_data_file("testLeaderboard")
        
        
        
    """ Test that game duration can be returned for a given user in leaderboard data """
    def test_if_duration_can_be_returned_for_player_in_leaderboard_data(self):
        users.add_user_to_data_file("users", "testPlayer2", "none", game_single.create_game_object())
        game_single.set_game_duration("testPlayer2", 999)
        test_player = leaderboard_single.create_leaderboard_player("testPlayer2")
        files.create_data_file("testLeaderboard2")
        files.append_to_file(test_player, "testLeaderboard2")

                
        duration = leaderboard_single.return_user_game_duration("testPlayer2", "testLeaderboard2")
        
        self.assertEqual(999, duration)
        
        users.remove_user_from_data_file("users", "testPlayer2")
                
        files.delete_data_file("testLeaderboard2")
        
    
    """ Test if multi game object can be created """
    def test_if_multi_game_obj_can_be_created(self):
        # game_obj = game_multi.create_multi_game_object("game name")
        
        # if game_multi.check_if_game_name_does_exist("game_multi", "game name"):
        #     files.append_to_file(game_obj, "game_multi")
            
        # player = game_multi.create_player("robot")
        # if game_multi.check_if_player_does_exist("game_multi", "game name", "robot"):   
        #     game_multi.add_player_to_multi_game_obj("game name", player)
            
        # while game_multi.check_number_of_players("game_multi", "game name") == False:
        #     game_multi.add_player_to_multi_game_obj("game name", game_multi.create_player("test"))
            
        # v = game_multi.extract_key_value_from_multi_game("game_multi", "game name", "game_name")
        
        
        
        # game_multi.overwrite_player_key_value("game_multi", "game name", "robot", "score", 3)
        
        # v2 = game_multi.extract_key_value_from_player_in_game("game_multi", "game name", "robot", "incorrect_answers")
        
        # game_multi.overwrite_game_key_value("game_multi", "game name", "list_of_countries", 10)
        
        # print(v)
        # print(v2)
        
        list_of_country_index_numbers = game_multi.extract_key_value_from_multi_game("game_multi", "c", "list_of_countries")
        
        print(list_of_country_index_numbers)
            
        # game_multi.remove_player_by_index_from_multi_game("game_multi", "ds", 2)
        game_multi.increase_flag_number("ds")
        game_multi.append_incorrect_answers(0, "hey", "ds")
        
        print(game_multi.return_player_score(1, "ds"))
        
       
        
        
        
        
        
        
        
        
