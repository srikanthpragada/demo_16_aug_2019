
def sumofdigits(num):
    total = 0
    while num > 0:
        total +=  num % 10
        num //= 10

    return total


print( sumofdigits(12343))
print( sumofdigits(526))
