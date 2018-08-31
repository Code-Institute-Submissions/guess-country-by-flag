import random

def generate_random_numbers(amount):
    # create a list of a given amount of random numbers in the range of 0-199
    list_of_index_numbers = random.sample(range(200), amount)
    
    return list_of_index_numbers


def calculate_game_duration(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_time_two_decimal = round(elapsed_time, 2)
    
    return elapsed_time_two_decimal


def string_to_lowercase_then_titlecase(string):
    # Strip white space from begining and end then convert
    string_no_spaces_before_after = string.strip()
    string_to_lowercase = string_no_spaces_before_after.lower()
    string_to_titlecase = string_to_lowercase.title()
    
    return string_to_titlecase
    
    
def convert_time_for_display(time):
    # Based on number of seconds, convert them to hours or minutes.
    # If there are more seconds than there are in 24 hours, return a
    # string.
    if time > 86400:
        return "24hrs +"
    elif time > 3600:
        hours = time / 3600
        hours_to_two_decimal = (round(hours, 2))
        return "{}hrs".format(hours_to_two_decimal)
    elif time > 60:
        minutes = time / 60
        minutes_to_two_decimal = round(minutes, 2)
        return "{}min".format(minutes_to_two_decimal)
    else:
        seconds_to_two_decimal = round(time, 2)
        return "{}sec".format(seconds_to_two_decimal)
                


        




            
            






                        
                        
        


    
    