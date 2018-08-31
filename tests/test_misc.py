import unittest
from utils import misc

class app_tests(unittest.TestCase):
    
    def test_if_list_of_random_numbers_can_be_created(self):
        list_of_random_numbers = misc.generate_random_numbers(5)
        list_of_other_numbers = [-1, 205, 34, 55, 1000, 0]
        
        def check_if_numbers_in_range(list_of_numbers):
            for num in list_of_numbers:
                if num < 0 or num > 199 or type(num) != int:
                    return False
            return True
            
        def perform_check_number_of_times(num_of_times, list_of_numbers):
            for i in range(num_of_times):
                if not check_if_numbers_in_range(list_of_numbers):
                    return False
            return True
            
        self.assertEqual(5, len(list_of_random_numbers))
        self.assertEqual(int, type(list_of_random_numbers[0]))
        self.assertEqual(int, type(list_of_random_numbers[1]))
        self.assertEqual(int, type(list_of_random_numbers[2]))
        self.assertEqual(int, type(list_of_random_numbers[3]))
        self.assertEqual(int, type(list_of_random_numbers[4]))
        self.assertTrue(check_if_numbers_in_range(list_of_random_numbers))
        self.assertFalse(check_if_numbers_in_range(list_of_other_numbers))
        self.assertTrue(perform_check_number_of_times(100, list_of_random_numbers))
        
        
    def test_if_can_calculate_game_duration(self):
        start_time = 88
        end_time = 120
        difference = end_time - start_time
        elapsed_time = misc.calculate_game_duration(start_time, end_time)
        self.assertEqual(difference, elapsed_time)
        

    def test_if_string_can_be_converted_to_lower_and_title_case(self):
        string = "HeLLO woRld"
        converted_string = misc.string_to_lowercase_then_titlecase(string)
        self.assertEqual("Hello World", converted_string)
        
        
    def test_if_time_can_be_calculated_for_display(self):
        list_of_times = [86500, 5560, 500, 22]
        more_than_day = misc.convert_time_for_display(list_of_times[0])
        self.assertEqual("24hrs +", more_than_day)
        
        hours = misc.convert_time_for_display(list_of_times[1])
        self.assertEqual("1.54hrs", hours)
        
        minutes = misc.convert_time_for_display(list_of_times[2])
        self.assertEqual("8.33min", minutes)
        
        seconds = misc.convert_time_for_display(list_of_times[3])
        self.assertEqual("22sec", seconds)