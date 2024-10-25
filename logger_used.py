from logger_param import logger
import random


@logger('dice.org')
def dice(dice_type):

    
    result = random.choice(range(1, dice_type))
    print(result)
    return result
dice(24)