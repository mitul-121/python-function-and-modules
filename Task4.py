example1 = 1, 2, 3, 4, 5

def arbitrary_function(*args):
    """Print each number in new line."""
    for num in args:
        print(num)

arbitrary_function(*example1)