import unittest
from utils import game_single, users

class app_tests(unittest.TestCase):
    
    def test_if_can_create_game_obj(self):
        game_object = game_single.create_game()
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
        self.assertEqual("not", game_object["win"])
        self.assertEqual(0, game_object["game_duration"])
        self.assertEqual(type({}), type(game_object))

    
    def test_value_of_key__in_game_obj_can_be_extracted(self):
        users.add_player_to_data("testUser11", "none", game_single.create_game())
        points = game_single.extract_value_from_game("testUser11", "points")
        question_number = game_single.extract_value_from_game("testUser11", "question_number")
        self.assertEqual(5, points)
        self.assertEqual(1, question_number)
        
        users.remove_player_from_data("testUser11")
        
    
    def test_that_question_number_can_be_increased(self):
        users.add_player_to_data("testUser12", "none", game_single.create_game())
        question_number = game_single.extract_value_from_game("testUser12", "question_number")
        self.assertEqual(1, question_number)
        
        game_single.increase_question_number("testUser12")
        question_number_updated = game_single.extract_value_from_game("testUser12", "question_number")
        self.assertEqual(2, question_number_updated)
        
        users.remove_player_from_data("testUser12")
        
    
    def test_that_question_number_can_be_reset(self):
        users.add_player_to_data("testUser13", "none", game_single.create_game())
        question_number = game_single.extract_value_from_game("testUser13", "question_number")
        self.assertEqual(1, question_number)
        
        game_single.increase_question_number("testUser13")
        question_number_updated = game_single.extract_value_from_game("testUser13", "question_number")
        self.assertEqual(2, question_number_updated)
        
        game_single.reset_question_number("testUser13")
        question_number_reset = game_single.extract_value_from_game("testUser13", "question_number")
        self.assertEqual(1, question_number_reset)
        
        users.remove_player_from_data("testUser13")

    
    def test_if_incorrect_answer_can_be_appended(self):
        users.add_player_to_data("testUser14", "none", game_single.create_game())
        list_of_incorrect_answers = game_single.extract_value_from_game("testUser14", "incorrect_answers")
        self.assertEqual([], list_of_incorrect_answers)
        self.assertEqual(0, len(list_of_incorrect_answers))
        
        game_single.append_incorrect_answers("testUser14", "im-a-wrong-answer")
        list_of_incorrect_answers_updated = game_single.extract_value_from_game("testUser14", "incorrect_answers")
        self.assertIn("im-a-wrong-answer", list_of_incorrect_answers_updated)
        self.assertEqual(1, len(list_of_incorrect_answers_updated))
        
        users.remove_player_from_data("testUser14")
        
    
    def test_if_incorrect_answer_list_can_be_reset(self):
        users.add_player_to_data("testUser15", "none", game_single.create_game())
        game_single.append_incorrect_answers("testUser15", "im-a-wrong-answer")
        game_single.append_incorrect_answers("testUser15", "im-a-wrong-answer-too")
        
        list_of_incorrect_answers = game_single.extract_value_from_game("testUser15", "incorrect_answers")
        self.assertEqual(["im-a-wrong-answer", "im-a-wrong-answer-too"], list_of_incorrect_answers)
        
        game_single.reset_incorrect_answers("testUser15")
        list_of_incorrect_answers_updated = game_single.extract_value_from_game("testUser15", "incorrect_answers")
        self.assertEqual([], list_of_incorrect_answers_updated)
        
        users.remove_player_from_data("testUser15")
        
    
    def test_if_can_reduce_points(self):
        users.add_player_to_data("testUser16", "none", game_single.create_game())
        points = game_single.extract_value_from_game("testUser16", "points")
        self.assertEqual(5, points)
        
        game_single.decrease_round_points("testUser16")
        points_two = game_single.extract_value_from_game("testUser16", "points")
        self.assertEqual(3, points_two)
        
        game_single.decrease_round_points("testUser16")
        points_three = game_single.extract_value_from_game("testUser16", "points")
        self.assertEqual(1, points_three)
        
        game_single.decrease_round_points("testUser16")
        points_four = game_single.extract_value_from_game("testUser16", "points")
        self.assertEqual(0, points_four)
        
        users.remove_player_from_data("testUser16")
        
   
    def test_if_can_reset_points(self):
        users.add_player_to_data("testUser17", "none", game_single.create_game())
        points = game_single.extract_value_from_game("testUser17", "points")
        self.assertEqual(5, points)
        
        game_single.decrease_round_points("testUser17")
        points_two = game_single.extract_value_from_game("testUser17", "points")
        self.assertEqual(3, points_two)
        
        game_single.reset_round_points("testUser17")
        points_two = game_single.extract_value_from_game("testUser17", "points")
        self.assertEqual(5, points_two)
        
        users.remove_player_from_data("testUser17")
        
   
    def test_if_win_state_can_be_set(self):
        users.add_player_to_data("testUser18", "none", game_single.create_game())
        win_state = game_single.extract_value_from_game("testUser18", "win")
        self.assertEqual("not", win_state)
        
        game_single.set_win_state("testUser18", "won")
        new_win_state = game_single.extract_value_from_game("testUser18", "win")
        self.assertEqual("won", new_win_state)
        
        users.remove_player_from_data("testUser18")
        
    
    def test_if_win_state_can_be_set_according_to_score(self):
        users.add_player_to_data("testUser19", "none", game_single.create_game())
        win_state = game_single.extract_value_from_game("testUser19", "win")
        score = users.return_player_score("testUser19")
        self.assertEqual("not", win_state)
        self.assertEqual(0, score)
        
        game_single.check_for_win(score, "testUser19")
        updated_win_state = game_single.extract_value_from_game("testUser19", "win")
        self.assertEqual("lost", updated_win_state)
        
        users.increase_player_score("testUser19", 100)
        updated_score = users.return_player_score("testUser19")
        self.assertEqual(100, updated_score)
        
        game_single.check_for_win(updated_score, "testUser19")
        updated_win_state_two = game_single.extract_value_from_game("testUser19", "win")
        self.assertEqual("won", updated_win_state_two)
        
        users.remove_player_from_data("testUser19")
        
   
    def test_if_game_duration_can_be_set(self):
        users.add_player_to_data("testUser20", "none", game_single.create_game())
        time = game_single.extract_value_from_game("testUser20", "game_duration")
        self.assertEqual(0, time)
        
        game_single.set_game_duration("testUser20", 20)
        new_time = game_single.extract_value_from_game("testUser20", "game_duration")
        self.assertEqual(20, new_time)
        
        users.remove_player_from_data("testUser20")
        
    
    def test_if_list_of_random_numbers_of_countries_in_game_obj_can_be_updated(self):
        users.add_player_to_data("testUser21", "none", game_single.create_game())
        list_of_numbers = game_single.extract_value_from_game("testUser21", "countries")
        
        def check_if_every_item_is_int_in_list(list_of_items):
            for item in list_of_items:
                if type(item) == int:
                    return True
                else:
                    return False
                    
        self.assertEqual(20, len(list_of_numbers))
        self.assertTrue(check_if_every_item_is_int_in_list(list_of_numbers))
        
        game_single.generate_new_list_of_random_countries("testUser21")
        new_list = game_single.extract_value_from_game("testUser21", "countries")
        self.assertEqual(20, len(new_list))
        self.assertTrue(check_if_every_item_is_int_in_list(new_list))
        self.assertNotEqual(list_of_numbers, new_list)
        
        users.remove_player_from_data("testUser21")