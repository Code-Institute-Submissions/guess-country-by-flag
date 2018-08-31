import unittest
from utils import files, game_single, leaderboard_single, users

class app_tests(unittest.TestCase):
    """
    Warning: running these tests will clear all data in file
    """
    def test_if_can_create_leaderboard_player_obj(self):
        users.add_player_to_data("testUser24", "none", game_single.create_game())
        leaderboard_player = leaderboard_single.create_leaderboard_player("testUser24")
        self.assertIn("username", leaderboard_player)
        self.assertIn("duration", leaderboard_player)
        self.assertIn("score", leaderboard_player)
        self.assertIn("rank", leaderboard_player)
        self.assertEqual("testUser24", leaderboard_player["username"])
        self.assertEqual(0, leaderboard_player["score"])
        self.assertEqual(0, leaderboard_player["rank"])
        self.assertEqual(0, leaderboard_player["duration"])
        
        users.remove_player_from_data("testUser24")
        
        
    def test_if_leaderboard_can_be_sorted_and_ranked(self):
        data = [{"duration": 3, "rank": 1, "score": 90, "username": "testPlayer1"}, 
                {"duration": 1, "rank": 999, "score": 50, "username": "testPlayer2"}, 
                {"duration": 1, "rank": 10, "score": 55, "username": "testPlayer3"}]
                
        test_sorted_data = [{"duration": 3, "rank": 1, "score": 90, "username": "testPlayer1"}, 
                      {"duration": 1, "rank": 10, "score": 55, "username": "testPlayer3"}, 
                      {"duration": 1, "rank": 999, "score": 50, "username": "testPlayer2"}]
                      
        test_ranked_data = [{"duration": 3, "rank": 1, "score": 90, "username": "testPlayer1"}, 
                      {"duration": 1, "rank": 2, "score": 55, "username": "testPlayer3"}, 
                      {"duration": 1, "rank": 3, "score": 50, "username": "testPlayer2"}]
        sorted_data = leaderboard_single.sort_score_in_descending_order(data)
        self.assertEqual(test_sorted_data, sorted_data)
        
        ranked_data = leaderboard_single.change_rank_ascending(data)
        self.assertEqual(test_ranked_data, ranked_data)
    
    
    def test_if_can_update_player_on_leaderboard_and_if_can_update_leaderboard(self):
        test_ranked_data = [{"duration": 250, "rank": 1, "score": 90, "username": "testPlayer4"}, 
                            {"duration": 400, "rank": 2, "score": 55, "username": "testPlayer5"}, 
                            {"duration": 200, "rank": 3, "score": 50, "username": "testPlayer6"}]
        leaderboard_single.update_leaderboard(test_ranked_data)
        data = files.read_data_file("leaderboard")
        test_player = {"duration": 300, "rank": 2, "score": 90, "username": "testPlayer4"}
        leaderboard_single.update_player_on_leaderboard(test_player, data)
        test_player_two = {"duration": 500, "rank": 2, "score": 95, "username": "testPlayer5"}
        leaderboard_single.update_player_on_leaderboard(test_player_two, data)
        test_ranked_data_two = [{"duration": 500, "rank": 1, "score": 95, "username": "testPlayer5"},
                                {"duration": 250, "rank": 2, "score": 90, "username": "testPlayer4"}, 
                                {"duration": 200, "rank": 3, "score": 50, "username": "testPlayer6"}]
        data = files.read_data_file("leaderboard")
        self.assertEqual(test_ranked_data_two, data)
        
        empty_data = []
        leaderboard_single.update_leaderboard(empty_data)
        
        
    def test_if_can_return_player_times_in_list(self):
        test_ranked_data = [{"duration": 250, "rank": 1, "score": 90, "username": "testPlayer4"}, 
                            {"duration": 400, "rank": 2, "score": 55, "username": "testPlayer5"}, 
                            {"duration": 200, "rank": 3, "score": 50, "username": "testPlayer6"}]
        leaderboard_single.update_leaderboard(test_ranked_data)
        data = files.read_data_file("leaderboard")
        list_of_times = leaderboard_single.list_game_duration_for_each_player(data)
        self.assertEqual("4.17min", list_of_times[0])
        self.assertEqual("6.67min", list_of_times[1])
        self.assertEqual("3.33min", list_of_times[2])
        

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
        top_ten = leaderboard_single.create_top_ten_players_list(data)
        self.assertEqual(test_top_ten, top_ten)
