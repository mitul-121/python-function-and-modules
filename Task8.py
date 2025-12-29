import math

def square1(x):
    """returns the square value of x"""
    return math.pow(x, 2)

def func(integers, functions):
    output = []
    for integer in integers:
        output.append(functions(integer))
    return output

input1 = [1, 2, 3]
print(func(input1, square1))

