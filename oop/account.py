class SavingsAccount:
    minbal = 10000

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal

    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def print(self):
        print("Account No.    : ", self.acno)
        print("Account Holder : ", self.ahname)
        print("Current Balance: ", self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - SavingsAccount.minbal >= amount:
            self.balance -= amount
        else:
            raise ValueError('Insufficient Balance')


if __name__ == '__main__':
    a1 = SavingsAccount(1, "Abc", 15000)
    a1.deposit(10000)
    a1.withdraw(5000)
    a1.print()
    # a1.withdraw(8000)

    a2 = SavingsAccount(2, "Roberts")
    a2.print()
