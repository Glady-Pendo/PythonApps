"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time_in_minutes):
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time_in_minutes
    
bake_time_remaining(20)

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation_time_in_minutes.
    
    :param preparation_time_in_minutes: int - preparation time already elapsed.
    :return: int - preparation_time_in_minutes (in minutes) derived from the 
     multiplication of 2 minutes.

    Function that takes the number_of_layers the lasagna has been made of as
    an argument and returns the total preparation_time_in_minutes the lasagna has taken 
    based on the number of layers.
    """
    return number_of_layers * 2

preparation_time_in_minutes(5)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    result = number_of_layers * 2
    
    return result + elapsed_bake_time
    
elapsed_time_in_minutes(3, 20)