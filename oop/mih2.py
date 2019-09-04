class A:
    def process(self):
        print("Process in A")

class B(A):
    def process(self):
        print("Process in B")

class C(A):
    def process(self):
        print("Process in C")


class D(B,C):
    pass


print(D.mro())