def zero(num):
    print(id(num))
    num = 0
    print(id(num))


def insert(lst, value):
    lst.insert(0, value)


a = 10
print(id(a))
zero(a)
print(a)

l = [10, 20]
insert(l, 5)
print(l)
