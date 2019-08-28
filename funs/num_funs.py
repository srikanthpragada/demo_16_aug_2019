
def iseven(n):
    """
    Returns true if given number is even otherwise false

    Params:
       n : is a number
    return:
       True or false
    """
    return  n % 2 == 0

def next_even(n):
    return  n + 2 if n % 2 == 0 else n + 1

if __name__ == '__main__':
    print("In module num_funs")