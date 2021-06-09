class MyClass():
    def __init__(self, shoe_size, name):
        self.shoe_size = shoe_size
        self.name = name

    name = "somePerson"

    def func1(self):
        print("10")
        print(self.name)


obj = MyClass(10, "someGuy")
print("your shoe size is", obj.shoe_size)
print(obj.name)
