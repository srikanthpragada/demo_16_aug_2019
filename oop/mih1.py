class A:
    def process(self):
        print("Process in A")

class B:
    def process(self):
        print("Process in B")

class C(A, B):
    pass
    # def process(self):
    #     print("Process in C")

print(C.__bases__)
obj = C()
obj.process()

