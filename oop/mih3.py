class A:
    def process(self):
        print("Process in A")

class B(A):
    def process(self):
        print("Process in B")

class C(B,A):
    def process(self):
        print("Process in C")

print(C.mro())