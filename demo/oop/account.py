class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Invalid amount {self.amount} for transaction!"


class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.amount = amount
        self.balance = balance

    def __str__(self):
        return f"Insufficient balance {self.balance} for withdraw of {self.amount}"


class SavingsAccount:
    # Class attribute or Static attribute
    minbal = 5000

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal

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
        if amount <= 0:
            raise InvalidAmountError(amount)

        self.balance += amount

    def withdraw(self, amount):
        if self.balance - SavingsAccount.minbal >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsError(self.balance, amount)

    def getbalance(self):
        return self.balance


print(SavingsAccount.getminbal())  # Call static method

a1 = SavingsAccount(1, "Andy")  # Create object
a1.deposit(10000)
a1.deposit(30000)
a1.withdraw(200000)

# a1.balance = 10000000
print(a1.getbalance())

a2 = SavingsAccount(2, "Joe", 20000)
a2.info()
