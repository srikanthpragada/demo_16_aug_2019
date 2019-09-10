def numbers():
    for i in range(1, 11):
        yield i


n = numbers()

print(next(n))
print(next(n))

gen = (n*n for n in range(1,11))

print(type(gen))
print(next(gen))

# for c in codes("Abc"):
#    print(c)
