class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # Private attribute

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age


p1 = Person("Mike", 30)
p2 = Person("Mike", 30)
p3 = Person("Jack", 25)

print(p1)  # str(p1) -->  p1.__str__()
print(str(p1))
print(p1.__str__())
print(p1 == p2)     # p1.__eq__(p2)
print(p1 == p3)     # p1.__eq__(p3)
print(p1 > p3)      # p1.__gt__(p2)
