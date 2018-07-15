import unittest
import app
import json
from utils.utils import *

class app_tests(unittest.TestCase):
    
    """ Test that a user object can be created containing username and score""" 
    def test_can_create_user_object(self):
        user = create_user("testUser", "ka10", 0)
        
        self.assertEqual("testUser", user["username"])
        self.assertEqual("ka10", user["password"])
        self.assertEqual(0, user["score"])
        self.assertEqual(user, {"username": "testUser", "password": "ka10", "score": 0})
    
    
    
    """ Test whether a user can be added to data file """
    def test_if_user_can_be_added(self):
        add_user_to_data_file("data/users.json", "testUser", "ka10")
        
        with open("data/users.json", "r") as json_data:
            data = json.load(json_data)
        
        user = {}
        
        for obj in data:
            if obj["username"] == "testUser":
                user = obj
        
        self.assertIn(user, data)
        
    
    
    """ Test whether a username already exists in data file, should return 'True' if doesn't and 'Flase' if does """
    def test_if_username_does_not_exist(self):
        add_user_to_data_file("data/users.json", "testUser", "ka10")
        does_not_exist = check_if_username_does_exist("data/users.json", "I-Dont-Exist")
        does_exist = check_if_username_does_exist("data/users.json", "testUser")
        
        self.assertTrue(does_not_exist)
        self.assertFalse(does_exist)
        
    
    
    """ Test whether password matches the username """
    def test_if_password_matches_username(self):
        add_user_to_data_file("data/users.json", "testUser", "ka10")
        user_one_password_not_match = check_if_password_matches("data/users.json", "testUser", "ka9")
        user_one_password_matches = check_if_password_matches("data/users.json", "testUser", "ka10")
        
        add_user_to_data_file("data/users.json", "testUser2", "ka10waii")
        user_two_password_not_match = check_if_password_matches("data/users.json", "testUser", "***SSS")
        user_two_password_matches = check_if_password_matches("data/users.json", "testUser2", "ka10waii")
        user_three_password_matches = check_if_password_matches("data/users.json", "falon", "ka10waii")
        
        self.assertFalse(user_one_password_not_match)
        self.assertTrue(user_one_password_matches)
        
        self.assertFalse(user_two_password_not_match)
        self.assertTrue(user_two_password_matches)
        
        self.assertFalse(user_three_password_matches)
        
    
    
    """ Test whether a user can be added to the data file if a user with the same username already exists """
    def test_if_can_add_user_when_username_exists(self):
        add_user_to_data_file("data/users.json", "testUser", "ka10")
        does_exists = check_if_username_does_exist("data/users.json", "testUser")
        
        def check_if_added():
            if add_user_to_data_file("data/users.json", "testUser", "ka10"):
                return True
            else:
                return False
                
                
        self.assertFalse(does_exists)
        
        self.assertFalse(check_if_added())
        
        
        
        
        
        
        
