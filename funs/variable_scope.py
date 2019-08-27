a = 10
def f1():
    b = 20
    def f2():
        nonlocal b
        global a
        a = 1
        b = 40
        c = 30
        print(a, b, c)
    f2()
    print(b)  # 40

f1()
print(a)  # 1
