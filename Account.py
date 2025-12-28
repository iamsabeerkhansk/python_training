class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} is debited, bal is {self.getbal()}")
        else:
            print("insufficient balance")

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} is credited, bal is {self.getbal()}")

    def getbal(self):
        return self.balance

    def checkbal(self):
        print(f"Balance is {self.balance}")


acc1 = Account(1000, "acc123")
acc1.credit(500)
acc1.debit(1000)
acc1.checkbal()
