import random


""" Generate a list of a given amount of index numbers between 0 and 204 """
def generate_random_numbers(amount):
    list_of_index_numbers = None
    
    list_of_index_numbers = random.sample(range(204), amount)
    
    return list_of_index_numbers
    
""" Calculate game_duration and round the result to two decimal places """ 
def calculate_game_duration(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_time_two_decimal = round(elapsed_time, 2)
    return elapsed_time_two_decimal


""" Convert string to lower and then title case """            
def answer_to_lowercase_then_titlecase(string):
    string_to_lowercase = string.lower()
    string_to_titlecase = string_to_lowercase.title()
        
    return string_to_titlecase
                


        




            
            






                        
                        
        


    
    