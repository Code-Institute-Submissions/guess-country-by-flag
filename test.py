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
        
    
    
    """ Test whether input password matches the password for that username """
    def test_if_password_matches_username(self):
        add_user_to_data_file("data/users.json", "testUser", "ka10")
        user_one_password_not_match = check_if_password_matches("data/users.json", "testUser", "ka9")
        user_one_password_matches = check_if_password_matches("data/users.json", "testUser", "ka10")
        
        self.assertFalse(user_one_password_not_match)
        self.assertTrue(user_one_password_matches)

        
    
    
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
    
    
       
    """ Test whether a data file can be created """
    def test_if_data_file_can_be_created(self):
        create_data_file("testFile")
                
        self.assertTrue(check_if_file_exists("testFile"))
    
    
    
    """ Test whether a data file can be deleted """
    def test_if_data_file_can_be_deleted(self):
        delete_data_file("testFile")
        
        self.assertFalse(check_if_file_exists("testFile"))
        
    
        
    """ Test whether a string containing the path to a file can be created """
    def test_if_string_path_to_file_can_be_created(self):
        create_data_file("testFile2")
        
        file_path = create_file_path("testFile2")
        
        self.assertEqual("data/testFile2.json", file_path)
        self.assertEqual(str, type(file_path))
        
        delete_data_file("testFile2")
        
    
    
    """ Test whether a user object can be removed from data file by its index number """
    def test_if_can_remove_user_by_index(self):
        create_data_file("testUsersList")
        file_path = create_file_path("testUsersList")
        add_user_to_data_file(file_path, "testUser", "none")
        add_user_to_data_file(file_path, "testUser2", "none")
        
        userIndexZero = create_user("testUser", "none", 0)
        userIndexOne = create_user("testUser2", "none", 0)
        
        with open(file_path, "r") as json_data:
            data = json.load(json_data)
        
        self.assertEqual(data[1], userIndexOne)
        
        remove_user_from_data_by_index(file_path, 0)
        
        with open(file_path, "r") as json_data:
            data = json.load(json_data)
            
        self.assertEqual(data[0], userIndexOne)
        
        delete_data_file("testUsersList")
        
    """ Test whether a data file containing 5 users actually contains 5 users, assert True if yes and False if not """
    def test_if_data_contains_five_users(self):
        create_data_file("testUsersList")
        file_path = create_file_path("testUsersList")
        add_user_to_data_file(file_path, "testUser", "none")
        add_user_to_data_file(file_path, "testUser2", "none")
        add_user_to_data_file(file_path, "testUser3", "none")
        add_user_to_data_file(file_path, "testUser4", "none")
        add_user_to_data_file(file_path, "testUser5", "none")
        
        create_data_file("testUsersList2")
        file_path2 = create_file_path("testUsersList2")
        add_user_to_data_file(file_path, "testUser", "none")
        add_user_to_data_file(file_path, "testUser2", "none")
        add_user_to_data_file(file_path, "testUser3", "none")
        
            
        self.assertTrue(check_number_of_multi_users(file_path))
        self.assertFalse(check_number_of_multi_users(file_path2))
        
        delete_data_file("testUsersList")
        delete_data_file("testUsersList2")
        
        
        
        
       
        
        
        
        
        
        
        
        
