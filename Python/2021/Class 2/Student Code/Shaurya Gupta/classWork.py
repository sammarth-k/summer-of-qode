class MyClass():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name_and_age(self):
        print(self.age, self.name)


obj = MyClass("shaurya", 10)
obj.print_name_and_age()
