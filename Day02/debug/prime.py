import math 
import pdb

def is_prime(num): 
    for mid in range(2, int(math.sqrt(num)) + 1): 
        if num % mid == 0:
            return False 
        #
    #

    return True 
#
pdb.set_trace()
print(is_prime(71))