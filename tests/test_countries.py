import unittest
from utils import countries, files

class app_tests(unittest.TestCase):
    
    def test_if_can_return_value_of_key_in_country_object(self):
        data = files.read_data_file("countries")
        country_index_zero = {
            "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Afghanistan.svg/1024px-Flag_of_Afghanistan.svg.png",
            "name-common": "Afghanistan",
            "name-official": "Islamic Republic of Afghanistan"
        }
        self.assertEqual(country_index_zero, data[0])
        
        flag = countries.return_value_from_country(0, "flag")
        self.assertEqual(flag, country_index_zero["flag"])
        
        name_common = countries.return_value_from_country(0, "name-common")
        self.assertEqual(name_common, country_index_zero["name-common"])
