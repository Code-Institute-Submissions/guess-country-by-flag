import unittest
import time
from utils import files, game_multi

class app_tests(unittest.TestCase):
    
    def test_if_multi_game_obj_can_be_created(self):
        game_obj = game_multi.create_game("testGame")
        test_game = {
            "game_name": "testGame",
            "time_of_creation": game_obj["time_of_creation"],
            "players": [],
            "players_copy": [],
            "round_number": 1,
            "flag_number": 0,
            "turn_of_player": 0,
            "points": 5,
            "list_of_countries": [],
            "game_state": "ongoing"
        }
        self.assertIn("game_name", game_obj)
        self.assertIn("time_of_creation", game_obj)
        self.assertIn("players", game_obj)
        self.assertIn("players_copy", game_obj)
        self.assertIn("round_number", game_obj)
        self.assertIn("flag_number", game_obj)
        self.assertIn("turn_of_player", game_obj)
        self.assertIn("points", game_obj)
        self.assertIn("list_of_countries", game_obj)
        self.assertIn("game_state", game_obj)
        self.assertEqual(test_game, game_obj)
        self.assertEqual(float, type(game_obj["time_of_creation"]))
    
    
    def test_if_game_exists(self):
        game_obj = game_multi.create_game("testGame")
        files.append_to_file(game_obj, "game_multi")
        does_exist = game_multi.check_if_game_exists("testGame")
        self.assertTrue(does_exist)
        
        game_multi.remove_game_from_data("testGame")
        
        
    def test_if_target_game_can_be_removed_from_data(self):
        game_obj = game_multi.create_game("testGame1")
        files.append_to_file(game_obj, "game_multi")
        does_exist = game_multi.check_if_game_exists("testGame1")
        self.assertTrue(does_exist)
        
        game_multi.remove_game_from_data("testGame1")
        does_not_exist = game_multi.check_if_game_exists("testGame1")
        self.assertFalse(does_not_exist)
        
        
    def test_if_target_game_can_be_selected_by_name(self):
        game = game_multi.create_game("testGame2")
        files.append_to_file(game, "game_multi")
        data = files.read_data_file("game_multi")
        game = game_multi.select_game("testGame2", data)
        self.assertEqual(game, game)
        
        game_multi.remove_game_from_data("testGame2")
        
        
    def test_that_a_game_can_be_overwritten(self):
        game = game_multi.create_game("testGame3")
        files.append_to_file(game, "game_multi")
        data = files.read_data_file("game_multi")
        game = game_multi.select_game("testGame3", data)
        self.assertEqual(game, game)

        test_game = {
            "game_name": "testGame3",
            "time_of_creation": 0,
            "players": 0,
            "players_copy": 0,
            "round_number": 0,
            "flag_number": 0,
            "turn_of_player": 0,
            "points": 0,
            "list_of_countries": 0,
            "game_state": 0
        }
        game_multi.overwrite_game("testGame3", test_game, data)
        overwritten_game = game_multi.select_game("testGame3", data)
        self.assertEqual(0, overwritten_game["players"])
        self.assertEqual(0, overwritten_game["game_state"])
        self.assertEqual(0, overwritten_game["points"])
        self.assertEqual(0, overwritten_game["round_number"])
        
        game_multi.remove_game_from_data("testGame3")
        
        
    def test_if_multiplayer_player_can_be_created(self):
        player = {
            "username": "testPlayer24",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        test_player = game_multi.create_player("testPlayer24")
        self.assertEqual(player, test_player)
    
    
    def test_if_player_can_be_added_to_game(self):
        files.append_to_file(game_multi.create_game("testGame4"), "game_multi")
        data = files.read_data_file("game_multi")
        game = game_multi.select_game("testGame4", data)
        self.assertEqual([], game["players"])
        
        test_player = {
            "username": "testPlayer25",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame4", test_player)
        data_two = files.read_data_file("game_multi")
        game_two = game_multi.select_game("testGame4", data_two)
        self.assertIn(test_player, game_two["players"])
        
        game_multi.remove_game_from_data("testGame4")
        
        
    def test_if_can_check_whether_player_exists_in_game_by_name(self):
        files.append_to_file(game_multi.create_game("testGame5"), "game_multi")
        data = files.read_data_file("game_multi")
        game = game_multi.select_game("testGame5", data)
        self.assertEqual([], game["players"])
        
        test_player = {
            "username": "testPlayer26",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame5", test_player)
        check = game_multi.check_if_player_exists("testGame5", "testPlayer26")
        self.assertTrue(check)
        
        game_multi.remove_game_from_data("testGame5")
        
        
    def test_whether_game_contains_five_players(self):
        files.append_to_file(game_multi.create_game("testGame6"), "game_multi")
        data = files.read_data_file("game_multi")
        check = game_multi.check_if_five_players("testGame6")
        game = game_multi.select_game("testGame6", data)
        self.assertFalse(check)
        
        test_player = {
            "username": "testPlayer27",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame6", test_player)
        game_multi.add_player_to_game("testGame6", test_player)
        game_multi.add_player_to_game("testGame6", test_player)
        game_multi.add_player_to_game("testGame6", test_player)
        game_multi.add_player_to_game("testGame6", test_player)
        check_two = game_multi.check_if_five_players("testGame6")
        self.assertTrue(check_two)
        
        game_multi.remove_game_from_data("testGame6")
        
        
    def test_if_can_extract_value_for_given_key_from_target_game(self):
        files.append_to_file(game_multi.create_game("testGame7"), "game_multi")
        data = files.read_data_file("game_multi")
        game = game_multi.select_game("testGame7", data)
        self.assertEqual(1, game["round_number"])
        
        extracted_value = game_multi.extract_value_from_game("testGame7", "round_number")
        self.assertEqual(extracted_value, game["round_number"])
        
        game_multi.remove_game_from_data("testGame7")
        
        
    def test_if_value_for_given_key_can_be_extracted_from_target_player_in_game(self):
        files.append_to_file(game_multi.create_game("testGame8"), "game_multi")
        test_player = {
            "username": "testPlayer28",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame8", test_player)
        data = files.read_data_file("game_multi")
        game = game_multi.select_game("testGame8", data)
        player_start_time = game["players"][0]["start_time"]
        self.assertEqual(0.0, player_start_time)
        
        extracted_value = game_multi.extract_value_from_player("testGame8", "testPlayer28", "score")
        self.assertEqual(extracted_value, player_start_time)
        
        game_multi.remove_game_from_data("testGame8")
        
        
    def test_if_can_overwrite_value_of_a_given_key_of_game(self):
        files.append_to_file(game_multi.create_game("testGame9"), "game_multi")
        flag_number = game_multi.extract_value_from_game("testGame9", "flag_number")
        self.assertEqual(0, flag_number)
        
        game_multi.overwrite_game_value("testGame9", "flag_number", 20)
        flag_number_two = game_multi.extract_value_from_game("testGame9", "flag_number")
        self.assertEqual(20, flag_number_two)
        
        game_multi.remove_game_from_data("testGame9")
        
        
    def test_if_can_overwrite_value_of_given_key_of_player_in_game(self):
        files.append_to_file(game_multi.create_game("testGame10"), "game_multi")
        test_player = {
            "username": "testPlayer29",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame10", test_player)
        player_rank = game_multi.extract_value_from_player("testGame10", "testPlayer29", "rank")
        self.assertEqual(0, player_rank)
        
        game_multi.overwrite_player_value("testGame10", "testPlayer29", "rank", 1)
        player_rank_two = game_multi.extract_value_from_player("testGame10", "testPlayer29", "rank")
        self.assertEqual(1, player_rank_two)
        
        game_multi.remove_game_from_data("testGame10")
        
        
    def test_if_can_remove_player_by_index_from_game(self):
        files.append_to_file(game_multi.create_game("testGame11"), "game_multi")
        test_player = {
            "username": "testPlayer30",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame11", test_player)
        player_list = game_multi.extract_value_from_game("testGame11", "players")
        self.assertIn(test_player, player_list)
        
        game_multi.remove_player_from_game_by_index("testGame11", 0)
        player_list_two = game_multi.extract_value_from_game("testGame11", "players")
        self.assertNotIn(test_player, player_list_two)
        
        game_multi.remove_game_from_data("testGame11")
        
        
    def test_if_can_increase_flag_number_by_one(self):
        files.append_to_file(game_multi.create_game("testGame12"), "game_multi")
        flag_number = game_multi.extract_value_from_game("testGame12", "flag_number")
        self.assertEqual(0, flag_number)
        
        game_multi.increase_flag_number("testGame12")
        flag_number_two = game_multi.extract_value_from_game("testGame12", "flag_number")
        self.assertEqual(1, flag_number_two)
        
        game_multi.remove_game_from_data("testGame12")
        
        
    def test_if_can_reset_flag_number_to_zero(self):
        files.append_to_file(game_multi.create_game("testGame13"), "game_multi")
        flag_number = game_multi.extract_value_from_game("testGame13", "flag_number")
        self.assertEqual(0, flag_number)
        
        game_multi.increase_flag_number("testGame13")
        game_multi.increase_flag_number("testGame13")
        game_multi.increase_flag_number("testGame13")
        game_multi.increase_flag_number("testGame13")
        flag_number_two = game_multi.extract_value_from_game("testGame13", "flag_number")
        self.assertEqual(4, flag_number_two)
        
        game_multi.reset_flag_number("testGame13")
        flag_number_three = game_multi.extract_value_from_game("testGame13", "flag_number")
        self.assertEqual(0, flag_number_three)
            
        game_multi.remove_game_from_data("testGame13")
        
        
    def test_if_can_increase_and_reset_player_turn(self):
        files.append_to_file(game_multi.create_game("testGame14"), "game_multi")
        turn = game_multi.extract_value_from_game("testGame14", "turn_of_player")
        self.assertEqual(0, turn)
        
        game_multi.set_turn_of_player("testGame14", 2)
        turn_two = game_multi.extract_value_from_game("testGame14", "turn_of_player")
        self.assertEqual(1, turn_two)
        
        game_multi.set_turn_of_player("testGame14", 2)
        turn_three = game_multi.extract_value_from_game("testGame14", "turn_of_player")
        self.assertEqual(0, turn_three)
        
        game_multi.remove_game_from_data("testGame14")    
        
        
    def test_if_can_increase_round_number_by_one(self):
        files.append_to_file(game_multi.create_game("testGame15"), "game_multi")
        round_number = game_multi.extract_value_from_game("testGame15", "round_number")
        self.assertEqual(1, round_number)
        
        game_multi.increase_round_number("testGame15")
        round_number_two = game_multi.extract_value_from_game("testGame15", "round_number")
        self.assertEqual(2, round_number_two)
        
        game_multi.remove_game_from_data("testGame15")    
        
        
    def test_if_can_reset_round_number(self):
        files.append_to_file(game_multi.create_game("testGame16"), "game_multi")
        round_number = game_multi.extract_value_from_game("testGame16", "round_number")
        self.assertEqual(1, round_number)
        
        game_multi.increase_round_number("testGame16")
        game_multi.increase_round_number("testGame16")
        game_multi.increase_round_number("testGame16")
        round_number_two = game_multi.extract_value_from_game("testGame16", "round_number")
        self.assertEqual(4, round_number_two)
        
        game_multi.reset_round_number("testGame16")
        round_number_three = game_multi.extract_value_from_game("testGame16", "round_number")
        self.assertEqual(0, round_number_three)
        
        game_multi.remove_game_from_data("testGame16")    
        
        
    def test_if_can_select_player_by_index_and_return_score(self):
        files.append_to_file(game_multi.create_game("testGame17"), "game_multi")
        test_player = {
            "username": "testPlayer31",
            "score": 22,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame17", test_player)
        test_player_score = game_multi.return_player_score(0, "testGame17")
        self.assertEqual(22, test_player_score)
        
        game_multi.remove_game_from_data("testGame17")    
        
        
    def test_if_can_select_player_by_index_and_increase_score(self):
        files.append_to_file(game_multi.create_game("testGame18"), "game_multi")
        test_player = {
            "username": "testPlayer31",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        test_player_two = {
            "username": "testPlayer32",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame18", test_player)
        game_multi.add_player_to_game("testGame18", test_player_two)
        test_player_score = game_multi.return_player_score(0, "testGame18")
        test_player_two_score = game_multi.return_player_score(1, "testGame18")
        self.assertEqual(0, test_player_score)
        self.assertEqual(0, test_player_two_score)
        
        game_multi.increase_player_score(1, 5, "testGame18")
        test_player_score_two = game_multi.return_player_score(0, "testGame18")
        test_player_two_score_two = game_multi.return_player_score(1, "testGame18")
        self.assertEqual(0, test_player_score_two)
        self.assertEqual(5, test_player_two_score_two)
        
        game_multi.remove_game_from_data("testGame18")    
    
    
    def test_if_can_select_player_by_index_and_return_incorrect_answers(self):
        files.append_to_file(game_multi.create_game("testGame19"), "game_multi")
        test_player = {
            "username": "testPlayer34",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": ["wrong", "wrong-again"]
        }
        game_multi.add_player_to_game("testGame19", test_player)
        test_player_answers =  game_multi.return_player_incorrect_answers(0, "testGame19")
        self.assertIn("wrong", test_player_answers)
        self.assertIn("wrong-again", test_player_answers)
        self.assertEqual(["wrong", "wrong-again"], test_player_answers)
        self.assertEqual(2, len(test_player_answers))
        
        game_multi.remove_game_from_data("testGame19")
        
        
    def test_if_can_select_player_by_index_and_append_answer(self):
        files.append_to_file(game_multi.create_game("testGame20"), "game_multi")
        test_player = {
            "username": "testPlayer33",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame20", test_player)
        test_player_answers = game_multi.return_player_incorrect_answers(0, "testGame20")
        self.assertEqual([], test_player_answers)
        
        game_multi.append_incorrect_answers(0, "wrong answer", "testGame20")
        test_player_answers_two = game_multi.return_player_incorrect_answers(0, "testGame20")
        self.assertIn("wrong answer", test_player_answers_two)
        
        game_multi.remove_game_from_data("testGame20")    
       
       
    def test_if_can_select_player_by_index_and_reset_incorrect_answers(self):
        files.append_to_file(game_multi.create_game("testGame21"), "game_multi")
        test_player = {
            "username": "testPlayer35",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame21", test_player)
        test_player_answers = game_multi.return_player_incorrect_answers(0, "testGame21")
        self.assertEqual([], test_player_answers)
        self.assertEqual(0, len(test_player_answers))
        
        game_multi.append_incorrect_answers(0, "wrong answer", "testGame21")
        test_player_answers_two = game_multi.return_player_incorrect_answers(0, "testGame21")
        self.assertIn("wrong answer", test_player_answers_two)
        self.assertEqual(1, len(test_player_answers_two))
        
        game_multi.reset_incorrect_answers(0, "testGame21")
        test_player_answers_three = game_multi.return_player_incorrect_answers(0, "testGame21")
        self.assertEqual([], test_player_answers_three)
        self.assertEqual(0, len(test_player_answers_three))
        
        game_multi.remove_game_from_data("testGame21")    
        
        
    def test_if_can_decrease_points_by_two_if_less_than_two_set_to_zero(self):
        files.append_to_file(game_multi.create_game("testGame22"), "game_multi")
        points = game_multi.extract_value_from_game("testGame22", "points")
        self.assertEqual(5, points)
        
        game_multi.decrease_points("testGame22")
        points_two = game_multi.extract_value_from_game("testGame22", "points")
        self.assertEqual(3, points_two)
        
        game_multi.decrease_points("testGame22")
        points_three = game_multi.extract_value_from_game("testGame22", "points")
        self.assertEqual(1, points_three)
        
        game_multi.decrease_points("testGame22")
        points_four = game_multi.extract_value_from_game("testGame22", "points")
        self.assertEqual(0, points_four)
        
        game_multi.remove_game_from_data("testGame22")  
        
        
    def test_if_can_return_player_by_turn(self):
        files.append_to_file(game_multi.create_game("testGame23"), "game_multi")
        test_player = {
            "username": "testPlayer36",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        test_player_two = {
            "username": "testPlayer37",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame23", test_player)
        game_multi.add_player_to_game("testGame23", test_player_two)
        data = files.read_data_file("game_multi")
        game = game_multi.select_game("testGame23", data)
        list_of_players = game["players"]
        turn_of_player = game_multi.extract_value_from_game("testGame23", "turn_of_player")
        self.assertEqual(0, turn_of_player)
        self.assertEqual(2, len(list_of_players))
        self.assertEqual(test_player, list_of_players[0])
        self.assertEqual(test_player_two, list_of_players[1])
        self.assertIn(test_player, list_of_players)
        self.assertIn(test_player_two, list_of_players)
        
        turn_one_player = game_multi.return_player_by_turn(0, "testGame23")
        self.assertEqual(test_player, turn_one_player)
        
        game_multi.set_turn_of_player("testGame23", 2)
        turn_two_player = game_multi.return_player_by_turn(1, "testGame23")
        self.assertEqual(test_player_two, turn_two_player)
        
        game_multi.set_turn_of_player("testGame23", 2)
        turn_one_player_repeat = game_multi.return_player_by_turn(0, "testGame23")
        self.assertEqual(test_player, turn_one_player_repeat)
        
        game_multi.remove_game_from_data("testGame23") 
        
        
    def test_if_can_set_start_time_of_player_to_current_time(self):
        files.append_to_file(game_multi.create_game("testGame24"), "game_multi")
        test_player = {
            "username": "testPlayer38",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame24", test_player)
        player_time = game_multi.extract_value_from_player("testGame24", "testPlayer38", "start_time")
        self.assertEqual(0.0, player_time)
        
        game_multi.set_start_time_for_current_player("testGame24")
        current_time = time.time()
        player_time_two = game_multi.extract_value_from_player("testGame24", "testPlayer38", "start_time")
        
        def within(current_time, player_time, max_difference):
            # check if current time is within .01sec of player_time_two
            difference = current_time - player_time
            if difference > max_difference:
                return False
            return True
            
        time_within = within(current_time, player_time_two, .01)
        self.assertTrue(time_within)
        
        game_multi.remove_game_from_data("testGame24") 
        
        
    def test_if_can_add_to_previous_players_elapsed_time(self):
        files.append_to_file(game_multi.create_game("testGame25"), "game_multi")
        test_player = {
            "username": "testPlayer39",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        test_player_two = {
            "username": "testPlayer40",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        test_player_three = {
            "username": "testPlayer41",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame25", test_player)
        game_multi.add_player_to_game("testGame25", test_player_two)
        game_multi.add_player_to_game("testGame25", test_player_three)
        game_multi.set_start_time_for_current_player("testGame25")
        game_multi.set_turn_of_player("testGame25", 3)
        game_multi.set_start_time_for_current_player("testGame25")
        game_multi.add_to_previous_players_elapsed_time("testGame25")
        player_start = game_multi.extract_value_from_player("testGame25", "testPlayer39", "start_time")
        player_elapsed = game_multi.extract_value_from_player("testGame25", "testPlayer39", "elapsed_time")
        player_two_start = game_multi.extract_value_from_player("testGame25", "testPlayer40", "start_time")
        elapsed_time = player_two_start - player_start
        self.assertEqual(elapsed_time, player_elapsed)
        
        game_multi.set_turn_of_player("testGame25", 3)
        game_multi.set_start_time_for_current_player("testGame25")
        game_multi.add_to_previous_players_elapsed_time("testGame25")
        player_two_start_two = game_multi.extract_value_from_player("testGame25", "testPlayer40", "start_time")
        player_two_elapsed = game_multi.extract_value_from_player("testGame25", "testPlayer40", "elapsed_time")
        player_three_start = game_multi.extract_value_from_player("testGame25", "testPlayer41", "start_time")
        elapsed_time_two = player_three_start - player_two_start_two
        self.assertEqual(elapsed_time_two, player_two_elapsed)
        
        game_multi.set_turn_of_player("testGame25", 3)
        game_multi.set_start_time_for_current_player("testGame25")
        game_multi.add_to_previous_players_elapsed_time("testGame25")
        player_three_start_two = game_multi.extract_value_from_player("testGame25", "testPlayer41", "start_time")
        player_three_elapsed = game_multi.extract_value_from_player("testGame25", "testPlayer41", "elapsed_time")
        player_start_two = game_multi.extract_value_from_player("testGame25", "testPlayer39", "start_time")
        elapsed_time_three = player_start_two - player_three_start_two
        self.assertEqual(elapsed_time_three, player_three_elapsed)
        
        game_multi.remove_game_from_data("testGame25") 
        
        
    def test_if_can_add_to_elapsed_time_for_last_flag_of_game(self):
        files.append_to_file(game_multi.create_game("testGame26"), "game_multi")
        test_player = {
            "username": "testPlayer42",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        test_player_two = {
            "username": "testPlayer43",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }
        game_multi.add_player_to_game("testGame26", test_player)
        game_multi.add_player_to_game("testGame26", test_player_two)
        game_multi.set_turn_of_player("testGame26", 2)
        game_multi.set_start_time_for_current_player("testGame26")
        player_start = game_multi.extract_value_from_player("testGame26", "testPlayer43", "start_time")
        player_elapsed = game_multi.extract_value_from_player("testGame26", "testPlayer43", "elapsed_time")
        self.assertEqual(0.0, player_elapsed)
        
        current_time = time.time()
        game_multi.add_to_elapsed_time_of_player_for_last_flag("testGame26", current_time)
        player_elapsed_two = game_multi.extract_value_from_player("testGame26", "testPlayer43", "elapsed_time")
        elapsed_time = current_time - player_start
        self.assertEqual(elapsed_time, player_elapsed_two)
        
        game_multi.remove_game_from_data("testGame26") 
        
        
    def test_if_can_sort_players_for_leaderboard(self):
        files.append_to_file(game_multi.create_game("testGame27"), "game_multi")
        list_of_test_players = [{
            "username": "testPlayer44",
            "score": 43,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 100,
            "incorrect_answers": []
        },
        {
            "username": "testPlayer45",
            "score": 66,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 100,
            "incorrect_answers": []
        },
        {
            "username": "testPlayer46",
            "score": 2,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 50,
            "incorrect_answers": []
        },
        {
            "username": "testPlayer47",
            "score": 66,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 99,
            "incorrect_answers": []
        }]
        
        for player in list_of_test_players:
            game_multi.add_player_to_game("testGame27", player)
            
        list_of_players = game_multi.extract_value_from_game("testGame27", "players")
        self.assertEqual(list_of_test_players, list_of_players)
        self.assertEqual(list_of_test_players[1], list_of_players[1])
        self.assertEqual(list_of_test_players[2], list_of_players[2])
        
        sorted_players = game_multi.sort_players_for_leaderboard_display("testGame27")
        list_of_players_two = game_multi.extract_value_from_game("testGame27", "players")
        self.assertEqual(list_of_test_players[0], sorted_players[2])
        self.assertEqual(list_of_test_players[1], sorted_players[1])
        self.assertEqual(list_of_test_players[2], sorted_players[3])
        self.assertEqual(list_of_test_players[3], sorted_players[0])
        
        game_multi.remove_game_from_data("testGame27") 
    
    
    def test_if_can_set_rank_for_each_player_ascending(self):
        files.append_to_file(game_multi.create_game("testGame28"), "game_multi")
        list_of_test_players = [{
            "username": "testPlayer48",
            "score": 43,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 100,
            "incorrect_answers": []
        },
        {
            "username": "testPlayer49",
            "score": 66,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 100,
            "incorrect_answers": []
        },
        {
            "username": "testPlayer50",
            "score": 2,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 50,
            "incorrect_answers": []
        },
        {
            "username": "testPlayer51",
            "score": 66,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 99,
            "incorrect_answers": []
        }]
        
        for player in list_of_test_players:
            game_multi.add_player_to_game("testGame28", player)
            
        list_of_players = game_multi.extract_value_from_game("testGame28", "players")
        self.assertEqual(list_of_test_players, list_of_players)
        
        game_multi.update_player_list("testGame28")
        ranked_players = game_multi.extract_value_from_game("testGame28", "players")
        
        for index, player in enumerate(ranked_players):
            player_rank = player["rank"]
            # check if rank increases by 1 for each consecutive player in list
            self.assertEqual(index + 1, player_rank)
            
        game_multi.remove_game_from_data("testGame28") 
            
            
    def test_if_can_list_elapsed_time_for_each_player(self):
        files.append_to_file(game_multi.create_game("testGame29"), "game_multi")
        list_of_test_players = [{
            "username": "testPlayer52",
            "score": 43,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 50,
            "incorrect_answers": []
        },
        {
            "username": "testPlayer53",
            "score": 66,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 100,
            "incorrect_answers": []
        }]
        
        for player in list_of_test_players:
            game_multi.add_player_to_game("testGame29", player)
            
        list_of_times = game_multi.list_players_elapsed_time("testGame29")
        self.assertIn("1.67min", list_of_times)
        self.assertIn("50sec", list_of_times)
        
        game_multi.remove_game_from_data("testGame29") 
        
        
    def test_if_can_reset_all_players_in_list_to_default_values(self):
        files.append_to_file(game_multi.create_game("testGame30"), "game_multi")
        list_of_test_players = [{
            "username": "testPlayer54",
            "score": 43,
            "rank": 2,
            "start_time": 1,
            "elapsed_time": 50,
            "incorrect_answers": ["wrong"]
        },
        {
            "username": "testPlayer55",
            "score": 66,
            "rank": 1,
            "start_time": 4,
            "elapsed_time": 100,
            "incorrect_answers": []
        }]
        
        for player in list_of_test_players:
            game_multi.add_player_to_game("testGame30", player)
            
        game_multi.reset_players("testGame30")
        list_of_players = game_multi.extract_value_from_game("testGame30", "players")
        list_of_test_players_default = [{
            "username": "testPlayer54",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        },
        {
            "username": "testPlayer55",
            "score": 0,
            "rank": 0,
            "start_time": 0.0,
            "elapsed_time": 0.0,
            "incorrect_answers": []
        }]
        self.assertEqual(list_of_test_players_default, list_of_players)
        
        game_multi.remove_game_from_data("testGame30") 
        
        
    def test_if_can_remove_games_older_than_a_day(self):
        files.append_to_file(game_multi.create_game("testGame31"), "game_multi")
        creation_time = game_multi.extract_value_from_game("testGame31", "time_of_creation")
        current_time = time.time()
        game_multi.remove_games_older_than_a_day(current_time)   
        data = files.read_data_file("game_multi")
        game = game_multi.select_game("testGame31", data)
        self.assertIn(game, data)
        
        day_from_now = current_time + 86400
        game_multi.remove_games_older_than_a_day(day_from_now) 
        data_two = files.read_data_file("game_multi")
        self.assertNotIn(game, data_two)
        
        