# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v
    # naive solution - takes 2 nums, x = 2-14 and y 3-6
    # gets x to power of y, stores as variable int = v
    # then gets the factorial of that integer, ex. 5! = 5*4*3*2*1 = v
    # then takes that factorial total and divides it by the sum of the two original params 2-14,3-6 and sets that int as V
    # final step v %= 982451653

cache = {}
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.

    pseudo-
    take two random int params
    if sum of params arent already in cache
    make sum as key in table
    then set value as pow

    """
    # Your code here
    
    # sumParams = x + y
    # if sumParams not in cache:
    #     cache[sumParams] = 0
    #     for key in cache:
    #         v = math.pow(x,y)
    #         v = math.factorial(v)
    #         v //= (x + y)
    #         v %= 982451653
    #         cache[sumParams] = v
    #         return cache[key]
    # return cache

    sumParams = x + y
    if sumParams not in cache:
        cache[sumParams] = math.pow(x,y)
        v = math.factorial(cache[sumParams])
        v //= (x + y)
        v %= 982451653
        cache[sumParams] = v
        return cache[sumParams]
    return cache[sumParams]

    
    




# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
