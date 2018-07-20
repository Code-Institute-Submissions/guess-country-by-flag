import unittest
import app
import json
import os
from utils import users, countries, file, misc, game_single

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
        users.add_user_to_data_file("data/users.json", "testUser", "ka10", "none")
        
        with open("data/users.json", "r") as json_data:
            data = json.load(json_data)
        
        user = {}
        
        for obj in data:
            if obj["username"] == "testUser":
                user = obj
        
        self.assertIn(user, data)
        
        users.remove_user_from_data_file("data/users.json", "testUser")
    
    
    
    """ Test whether a username already exists in data file, should return 'True' if doesn't and 'Flase' if does """
    def test_if_username_does_not_exist(self):
        users.add_user_to_data_file("data/users.json", "testUser", "ka10", "none")
        does_not_exist = users.check_if_username_does_exist("data/users.json", "I-Dont-Exist")
        does_exist = users.check_if_username_does_exist("data/users.json", "testUser")
        
        self.assertTrue(does_not_exist)
        self.assertFalse(does_exist)
        
        users.remove_user_from_data_file("data/users.json", "testUser")
    
    
    
    """ Test whether input password matches the password for that username """
    def test_if_password_matches_username(self):
        users.add_user_to_data_file("data/users.json", "testUser", "ka10", "none")
        user_one_password_not_match = users.check_if_password_matches("data/users.json", "testUser", "ka9")
        user_one_password_matches = users.check_if_password_matches("data/users.json", "testUser", "ka10")
        
        self.assertFalse(user_one_password_not_match)
        self.assertTrue(user_one_password_matches)

        users.remove_user_from_data_file("data/users.json", "testUser")
        
        
    
    """ Test whether a user can be added to the data file if a user with the same username already exists """
    def test_if_can_add_user_when_username_exists(self):
        users.add_user_to_data_file("data/users.json", "testUser", "ka10", "none")
        does_exists = users.check_if_username_does_exist("data/users.json", "testUser")
        
        def check_if_added():
            if users.add_user_to_data_file("data/users.json", "testUser", "ka10", "none"):
                return True
            else:
                return False
        
        self.assertFalse(does_exists)
        self.assertFalse(check_if_added())
    
        users.remove_user_from_data_file("data/users.json", "testUser")
       
       
       
    """ Test whether a data file can be created """
    def test_if_data_file_can_be_created(self):
        file.create_data_file("testFile")
        
                
        self.assertTrue(file.check_if_file_exists("testFile"))
        
        
        
    """ Test whether a file can be checked to exist or not """
    def check_if_can_be_check_to_exist(self):
        
        self.assertTrue(file.check_if_file_exists("testFile"))  
        self.assertFalse(file.check_if_file_exists("not-existing-file"))
        
        
        
    """ Test whether a data file can be deleted """
    def test_if_data_file_can_be_deleted(self):
        file.delete_data_file("testFile")
        
        self.assertFalse(file.check_if_file_exists("testFile"))
    
    
    
    """ Test whether a data file can be appended to """
    def test_if_can_append_to_file(self):
        file.create_data_file("testFile")
        
        data = file.read_data_file("testFile")
        
        data_two = []
        self.assertEqual(data_two, data)
        
        file.append_to_file("hello", "testFile")
        data_three = file.read_data_file("testFile")
        self.assertIn("hello", data_three)
        
        file.delete_data_file("testFile")
        
    
        
    """ Test whether a string containing the path to a file can be created """
    def test_if_string_path_to_file_can_be_created(self):
        file.create_data_file("testFile")
        
        file_path = file.create_file_path("testFile")
        
        self.assertEqual("data/testFile.json", file_path)
        self.assertEqual(str, type(file_path))
        
        file.delete_data_file("testFile")
        
    
    
    """ Test whether a user object can be removed from data file by its index number """
    def test_if_can_remove_user_by_index(self):
        file.create_data_file("testUsersList")
        file_path = file.create_file_path("testUsersList")
        users.add_user_to_data_file(file_path, "testUser", "none", "none")
        users.add_user_to_data_file(file_path, "testUser2", "none", "none")
        
        userIndexZero = users.create_user("testUser", "none", 0, "none")
        userIndexOne = users.create_user("testUser2", "none", 0, "none")
        
        with open(file_path, "r") as json_data:
            data = json.load(json_data)
        self.assertEqual(data[1], userIndexOne)
        
        users.remove_user_from_data_by_index(file_path, 0)
        with open(file_path, "r") as json_data:
            data = json.load(json_data)
        self.assertEqual(data[0], userIndexOne)
        
        file.delete_data_file("testUsersList")
        
        
        
    """ Test whether a data file containing 5 users actually contains 5 users, assert True if yes and False if not """
    def test_if_data_contains_five_users(self):
        file.create_data_file("testUsersList")
        file_path = file.create_file_path("testUsersList")
        
        users.add_user_to_data_file(file_path, "testUser", "none", "none")
        users.add_user_to_data_file(file_path, "testUser2", "none", "none")
        users.add_user_to_data_file(file_path, "testUser3", "none", "none")
        users.add_user_to_data_file(file_path, "testUser4", "none", "none")
        users.add_user_to_data_file(file_path, "testUser5", "none", "none")
        
        file.create_data_file("testUsersList2")
        file_path2 = file.create_file_path("testUsersList2")
        
        users.add_user_to_data_file(file_path, "testUser", "none", "none")
        users.add_user_to_data_file(file_path, "testUser2", "none", "none")
        users.add_user_to_data_file(file_path, "testUser3", "none", "none")
        
            
        self.assertTrue(users.check_number_of_multi_users(file_path))
        self.assertFalse(users.check_number_of_multi_users(file_path2))
        
        file.delete_data_file("testUsersList")
        file.delete_data_file("testUsersList2")
    
    
    
    """ Check that a user score can be returned """
    def test_if_user_score_returned(self):
        users.add_user_to_data_file("data/users.json", "testUser", "none", {})
        users.reset_user_score("testUser")
        
        returned_score = users.return_user_score("testUser")
        self.assertEqual(0, returned_score)
        
        users.increase_user_score("testUser", 200)
        updated_score = users.return_user_score("testUser")
        self.assertEqual(200, updated_score)
        
        users.remove_user_from_data_file("data/users.json", "testUser")
        
    
    
    """ Check that a user score can be increased by a given number of points """
    def test_if_user_score_increases(self):
        users.add_user_to_data_file("data/users.json", "testUser", 0, "none")
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
        
        users.remove_user_from_data_file("data/users.json", "testUser")
        
        
        
    """ Check whether a user score can be reset to zero"""
    def test_if_user_score_can_be_reset(self):
        users.add_user_to_data_file("data/users.json", "testUser", "none", {})
        users.increase_user_score("testUser", 5)
        test_score = users.return_user_score("testUser")
        
        self.assertEqual(5, test_score)
        
        users.reset_user_score("testUser")
        updated_test_score = users.return_user_score("testUser")
        
        self.assertEqual(0, updated_test_score)
        
        users.remove_user_from_data_file("data/users.json", "testUser")
        
        
        
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
    points(5), list of countries([]) and list of incorrect answers([random numbers]) """
    def test_if_can_create_game_obj(self):
        game_object = game_single.create_game_object()
            
        self.assertIn("countries", game_object)
        self.assertIn("question_number", game_object)
        self.assertIn("points", game_object)
        self.assertIn("incorrect_answers", game_object)
        self.assertEqual(type([]), type(game_object["countries"]))
        self.assertEqual(int, type(game_object["countries"][0]))
        self.assertEqual(type([]), type(game_object["incorrect_answers"]))
        self.assertEqual(1, game_object["question_number"])
        self.assertEqual(5, game_object["points"])
        self.assertEqual(type({}), type(game_object))



    """ Test that a value of a key inside a given game object can be extracted """
    def test_value_of_key__in_game_obj_can_be_extracted(self):
        users.add_user_to_data_file("data/users.json", "gameTest", "none", game_single.create_game_object())
        
        points_of_game = game_single.extract_key_value_from_game_obj("gameTest", "points")
        question_number_of_game = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        
        self.assertEqual(5, points_of_game)
        self.assertEqual(1, question_number_of_game)
        
        users.remove_user_from_data_file("data/users.json", "gameTest")
        
        
        
    """ Test that question number inside game object can be increased by 1 """
    def test_that_question_number_can_be_increased(self):
        users.add_user_to_data_file("data/users.json", "gameTest", "none", game_single.create_game_object())
        
        question_number_of_game = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        self.assertEqual(1, question_number_of_game)
        
        game_single.increase_question_number("gameTest")
        question_number_of_game_updated = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        self.assertEqual(2, question_number_of_game_updated)
        
        users.remove_user_from_data_file("data/users.json", "gameTest")
        
    
    
    """ Test that question number can be reset back to 1 """
    def test_that_question_number_can_be_reset(self):
        users.add_user_to_data_file("data/users.json", "gameTest", "none", game_single.create_game_object())
        
        question_number_of_game = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        self.assertEqual(1, question_number_of_game)
        
        
        game_single.increase_question_number("gameTest")
        question_number_of_game_updated = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        self.assertEqual(2, question_number_of_game_updated)
        
        game_single.reset_question_number("gameTest")
        question_number_reset = game_single.extract_key_value_from_game_obj("gameTest", "question_number")
        self.assertEqual(1, question_number_reset)
        
        users.remove_user_from_data_file("data/users.json", "gameTest")


    """ Test that a user's incorrect answer can be appended to a list inside the game obj """
    def test_if_incorrect_answer_can_be_appended(self):
        users.add_user_to_data_file("data/users.json", "gameTest", "none", game_single.create_game_object())
        
        list_of_incorrect_answers = game_single.extract_key_value_from_game_obj("gameTest", "incorrect_answers")
        self.assertEqual([], list_of_incorrect_answers)
        self.assertEqual(0, len(list_of_incorrect_answers))
        
        game_single.append_incorrect_answers("gameTest", "im-a-wrong-answer")
        list_of_incorrect_answers_updated = game_single.extract_key_value_from_game_obj("gameTest", "incorrect_answers")
        self.assertIn("im-a-wrong-answer", list_of_incorrect_answers_updated)
        self.assertEqual(1, len(list_of_incorrect_answers_updated))
        
        users.remove_user_from_data_file("data/users.json", "gameTest")
        
        
        
    """ Test that incorrect answers can be reset back to an empty list """
    def test_if_incorrect_answer_list_can_be_reset(self):
        users.add_user_to_data_file("data/users.json", "gameTest", "none", game_single.create_game_object())
        game_single.append_incorrect_answers("gameTest", "im-a-wrong-answer")
        game_single.append_incorrect_answers("gameTest", "im-a-wrong-answer-too")
        
        list_of_incorrect_answers = game_single.extract_key_value_from_game_obj("gameTest", "incorrect_answers")
        self.assertEqual(["im-a-wrong-answer", "im-a-wrong-answer-too"], list_of_incorrect_answers)
        
        game_single.reset_incorrect_answers("gameTest")
        list_of_incorrect_answers_updated = game_single.extract_key_value_from_game_obj("gameTest", "incorrect_answers")
        self.assertEqual([], list_of_incorrect_answers_updated)
        
        users.remove_user_from_data_file("data/users.json", "gameTest")
        
        
        
    """ Test that points can be decreased by 2, if points are less than 2 they are reduced to 0 """
    def test_if_can_reduce_points(self):
        users.add_user_to_data_file("data/users.json", "gameTest", "none", game_single.create_game_object())
        
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
        
        users.remove_user_from_data_file("data/users.json", "gameTest")
        
        
        
    """ Test that points can be reset back to 5 """
    def test_if_can_reset_points(self):
        users.add_user_to_data_file("data/users.json", "gameTest", "none", game_single.create_game_object())
        
        points = game_single.extract_key_value_from_game_obj("gameTest", "points")
        self.assertEqual(5, points)
        
        game_single.decrease_round_points("gameTest")
        points_two = game_single.extract_key_value_from_game_obj("gameTest", "points")
        self.assertEqual(3, points_two)
        
        game_single.reset_round_points("gameTest")
        points_two = game_single.extract_key_value_from_game_obj("gameTest", "points")
        self.assertEqual(5, points_two)
        
        
        
        users.remove_user_from_data_file("data/users.json", "gameTest")
        
        
    
    """ Test that a value is returned for a given key of a country object """
    def test_if_value_is_returned_for_key_of_country(self):
        file.create_data_file("testCountryFile")
        
        example_country_obj = {
            "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag_of_Albania.svg/1024px-Flag_of_Albania.svg.png",
            "name-common": "Albania",
            "name-official": "Republic of Albania"
        }
        
        file.append_to_file(example_country_obj, "testCountryFile")
        data = file.read_data_file("testCountryFile")
        self.assertIn(example_country_obj, data)
        
        value_of_key = countries.return_value_for_key_in_country_object_of_index("testCountryFile", 0, "name-common")
        self.assertEqual("Albania", value_of_key)
        
        file.delete_data_file("testCountryFile")
    
    
            
        
        
        
        
       
        
        
        
        
        
        
        
        
