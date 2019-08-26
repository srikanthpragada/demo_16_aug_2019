def multiply(n1, n2):
    return n1 * n2


def process(a, b, fun):
    print(fun(a, b))


process(10, 20, multiply)
