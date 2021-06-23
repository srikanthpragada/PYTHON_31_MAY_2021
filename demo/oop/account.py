class SavingsAccount:
    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # Object Attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    # Method
    def info(self):
        print("Account Number      : ", self.acno)
        print("Account holder name : ", self.ahname)
        print("Account Balance     : ", self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getbalance(self):
        return self.balance


a1 = SavingsAccount(1, "Andy")  # Create object
a1.deposit(10000)
a1.deposit(30000)
a1.withdraw(20000)

# a1.balance = 10000000
print(a1.getbalance())

a2 = SavingsAccount(2, "Joe", 20000)
a2.info()

