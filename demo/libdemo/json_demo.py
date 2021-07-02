import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # Private attribute

    def __str__(self):
        return f"{self.name} - {self.age}"


p = Person("Abc", 30)
jsonstr = json.dumps(p.__dict__)
print(jsonstr)

people = [Person("One", 20), Person("Two", 22), Person("Three", 30)]
people_list = list(map(lambda p: p.__dict__, people))
jsonstr = json.dumps(people_list)
print(jsonstr)

persons = json.loads(jsonstr)
print(persons)
