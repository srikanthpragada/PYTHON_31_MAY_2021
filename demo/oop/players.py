from abc import ABC, abstractmethod


# Abstract class
class Player(ABC):
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def show(self):
        print('Name    : ', self.name)
        print('Country : ', self.country)

    @abstractmethod
    def getpoints(self):
        pass


class Cricketer(Player):
    def __init__(self, name, country, runs, wickets):
        super().__init__(name, country)
        self.runs = runs
        self.wickets = wickets

    def show(self):
        super().show()
        print("Runs    : ", self.runs)
        print("Wickets : ", self.wickets)

    def getpoints(self):
        return (self.runs // 200) + (self.wickets // 10)


class Footballer(Player):
    def __init__(self, name, country, goals):
        super().__init__(name, country)
        self.goals = goals

    def show(self):
        super().show()
        print("Goals   : ", self.goals)

    def getpoints(self):
        return self.goals


c = Cricketer("Dhoni", "India", "4939", 0)
c.show()
f = Footballer("Ronaldo", "Portgual", 200)
f.show()
