import unittest
from utils import files, users

class app_tests(unittest.TestCase):

    def test_can_create_player_object(self):
        user = users.create_player("testUser", "ka10", 0, "none")
        self.assertEqual("testUser", user["username"])
        self.assertEqual("ka10", user["password"])
        self.assertEqual(0, user["score"])
        self.assertEqual("none", user["game"])
        self.assertEqual(user, {"username": "testUser", "password": "ka10", "score": 0, "game": "none"})
    
    
    def test_if_player_can_be_added(self):
        users.add_player_to_data("testUser1", "ka10", "none")
        data = files.read_data_file("users")
        user = {}
        
        for player in data:
            if player["username"] == "testUser1":
                user = player
        
        self.assertIn(user, data)
        
        users.remove_player_from_data("testUser1")
    
    
    def test_if_username_does_exist(self):
        users.add_player_to_data("testUser2", "ka10", "none")
        does_not_exist = users.check_if_username_exists("I-Dont-Exist")
        does_exist = users.check_if_username_exists("testUser2")
        self.assertFalse(does_not_exist)
        self.assertTrue(does_exist)
        
        users.remove_player_from_data("testUser2")
    
    
    def test_if_password_matches_username(self):
        users.add_player_to_data("testUser4", "ka10", "none")
        user_one_password_not_match = users.check_if_password_matches("testUser4", "ka9")
        user_one_password_matches = users.check_if_password_matches("testUser4", "ka10")
        self.assertFalse(user_one_password_not_match)
        self.assertTrue(user_one_password_matches)

        users.remove_player_from_data("testUser4")
        
        
    def test_if_can_add_user_when_username_exists(self):
        does_not_exist = users.check_if_username_exists("testUser5")
        self.assertFalse(does_not_exist)
        
        users.add_player_to_data("testUser5", "ka10", "none")
        does_exists = users.check_if_username_exists("testUser5")
        self.assertTrue(does_exists)
    
        users.remove_player_from_data("testUser5")
        

    def test_if_can_remove_user_by_index(self):
        file_path = files.create_file_path("users")
        data = files.read_data_file("users")
        data_length = len(data)

        users.add_player_to_data("testUser6", "none", "none")
        users.add_player_to_data("testUser7", "none", "none")
        
        user_index_zero = users.create_player("testUser6", "none", 0, "none")
        user_index_one = users.create_player("testUser7", "none", 0, "none")
        
        data_two = files.read_data_file("users")
        self.assertEqual(data_two[data_length], user_index_zero)
        users.remove_player_from_data_by_index(data_length)
        
        data_three = files.read_data_file("users")
        self.assertEqual(data_three[data_length], user_index_one)
        users.remove_player_from_data_by_index(data_length)
        

    def test_if_user_score_returned(self):
        users.add_player_to_data("testUser8", "none", {})
        users.reset_player_score("testUser8")
        reset_score = users.return_player_score("testUser8")
        self.assertEqual(0, reset_score)
        
        users.increase_player_score("testUser8", 200)
        increased_score = users.return_player_score("testUser8")
        self.assertEqual(200, increased_score)
        
        users.remove_player_from_data("testUser8")
        
    
    def test_if_user_score_increases(self):
        users.add_player_to_data("testUser9", 0, "none")
        score_one = users.return_player_score("testUser9")
        self.assertEqual(0, score_one)
        
        users.increase_player_score("testUser9", 2)
        score_two = users.return_player_score("testUser9")
        self.assertEqual(2, score_two)
        
        users.increase_player_score("testUser9", 10)
        score_three = users.return_player_score("testUser9")
        self.assertEqual(12, score_three)
            
        users.remove_player_from_data("testUser9")
        

    def test_if_user_score_can_be_reset(self):
        users.add_player_to_data("testUser10", "none", {})
        users.increase_player_score("testUser10", 5)
        score = users.return_player_score("testUser10")
        self.assertEqual(5, score)
        
        users.reset_player_score("testUser10")
        reset_score = users.return_player_score("testUser10")
        self.assertEqual(0, reset_score)
        
        users.remove_player_from_data("testUser10")