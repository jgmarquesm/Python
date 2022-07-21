EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time: int) -> int:
    
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(layers: int) -> int:
    """Calculate the preparating time in minutes.
    
    :param layers: int - number os layers of lasagna.
    :return: int - preparating time (in minutes) derived from 'EXPECTED_BAKE_TIME' and 'layers'.
    
    Function that takes the numbers of layers of the lasagna as
    an argument and returns how many minutes the lasagna still needs to prepare
    based on the `EXPECTED_BAKE_TIME`."""
    
    return layers * PREPARATION_TIME 
def elapsed_time_in_minutes(layers: int, elapsed_time: int) -> int:
    """Calculate the elapsed time in minutes.
    
    :param layers: int - number os layers of lasagna.
    :param elapsed_time: int - elapsed bake time.
    :return: int - elapsed time (in minutes) derived from 'layers' and 'elapsed_time'.
    
    Function that takes the numbers of layers of the lasagna and elapsed bake time as
    an arguments and returns how many minutes the lasagna needs to be caked
    based on the 'layers' and 'elapsed_time'."""
    
    return PREPARATION_TIME*layers + elapsed_time
