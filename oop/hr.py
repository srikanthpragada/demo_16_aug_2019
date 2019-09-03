class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name


class Programmer(Employee):
    def __init__(self,id,name,lang):
        super().__init__(id,name)
        self.lang = lang

    def __str__(self):
        return f"{self.id} - {self.name} - {self.lang}"


p = Programmer(1,"Bill","Python")
print(p)
