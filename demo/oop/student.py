class Student:
    def __init__(self, name, course='python', feepaid=0):
        # Object Attributes
        self.name = name
        self.course = course
        self.feepaid = feepaid

    def info(self):
        print("Student Name   : ", self.name)
        print("Course Name    : ", self.course)
        print("Fee Paid       : ", self.feepaid)

    def payment(self, amount):
        self.feepaid += amount

    def totalfee(self):
        if self.course == 'c':
            return 3000
        elif self.course == 'java':
            return 5000
        else:
            return 4000

    def getdue(self):
        return self.totalfee() - self.feepaid


s = Student("Scott", "java")
s.payment(3000)
print(s.getdue())  # 2000
