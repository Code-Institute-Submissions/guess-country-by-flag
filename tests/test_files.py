import unittest
from utils import files

class app_tests(unittest.TestCase):
    
    def test_if_file_can_be_overwritten(self):
        data = files.read_data_file("countries")
        data_copy = data
        self.assertEqual(200, len(data))
        
        files.overwrite_file("countries", "hello")
        data_overwritten = files.read_data_file("countries")
        self.assertEqual(5, len(data_overwritten))
        self.assertEqual("hello", data_overwritten)
        
        files.overwrite_file("countries", data_copy)
    

    def test_if_can_append_to_file(self):
        
        data = files.read_data_file("countries")
        data_copy = data
        self.assertNotIn("hello", data)
        
        files.append_to_file("hello", "countries")
        data_updated = files.read_data_file("countries")
        self.assertIn("hello", data_updated)
        
        files.overwrite_file("countries", data_copy)
    

    def test_if_string_path_to_file_can_be_created(self):
        file_path = files.create_file_path("countries")
        self.assertEqual("data/countries.json", file_path)
        self.assertEqual(str, type(file_path))
