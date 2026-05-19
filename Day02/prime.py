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

'''
Console 
    %run prime.py
pdb> list
pdb> break 14
pdb> break
pdb> s
pdb> list
pdb> break 6
pdb> break
pdb> c
pdb> p num, mid, num % mid, num % mid == 0
pdb> c
pdb> p num, mid, num % mid, num % mid == 0
pdb> c
pdb> p num, mid, num % mid, num % mid == 0
pdb> c
pdb> p num, mid, num % mid, num % mid == 0
pdb> where
pdb> break 
pdb> clear 2
pdb> r
pdb> r
True
'''