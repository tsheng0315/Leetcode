
"""
Implement a function recursively to get the desired
Fibonacci sequence value.

0,1,1,2,3,5,8,13,21,34...

"""

def get_fib(position):
    if position <=1:
        return position
    else: 
        return get_fib(position-1) + get_fib(position-2)


# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)


