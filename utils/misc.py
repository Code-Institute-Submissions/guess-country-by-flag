import random
import time
import game_single





""" Generate a list of a given amount of index numbers between 0 and 204 """
def generate_random_numbers(amount):
    list_of_index_numbers = None
    
    list_of_index_numbers = random.sample(range(204), amount)
    
    return list_of_index_numbers
    
""" Calculate game_duration """ 
def calculate_game_duration(start_time, end_time, username):
    elapsed_time = end_time - start_time
    
    return elapsed_time


""" Convert user input to lowercase and then to titlecase """            
def answer_to_lowercase_then_titlecase(user_input):
    answer_unmodified = user_input
    answer_to_lowercase = user_input.lower()
    answer_to_titlecase = answer_to_lowercase.title()
        
    return answer_to_titlecase
                


        




            
            






                        
                        
        


    
    