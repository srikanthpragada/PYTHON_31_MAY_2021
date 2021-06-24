class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute


p1 = Person("Mike", 30)
print(p1.__dict__)
print(p1._Person__age)

p2 = Person("Mike", 30)
p3 = Person("Jack", 25)
