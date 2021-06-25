class Student:
    course_fees = {'c': 3000, 'python': 4000, 'java': 5000, 'javaee': 8000}

    @staticmethod
    def change_fee(course, fee):
        Student.course_fees[course] = fee

    def __init__(self, name, course='python', feepaid=0):
        # Object Attributes
        self.name = name
        if not course in Student.course_fees:
            raise ValueError("Invalid course!")

        self.course = course
        self.feepaid = feepaid

    def info(self):
        print("Student Name   : ", self.name)
        print("Course Name    : ", self.course)
        print("Fee Paid       : ", self.feepaid)

    def payment(self, amount):
        self.feepaid += amount

    def totalfee(self):
        return Student.course_fees[self.course]

    def getdue(self):
        return self.totalfee() - self.feepaid


Student.change_fee('javaee', 6000)
s = Student("Scott", "javaee")
s.payment(3000)
print(s.getdue())  # 2000
