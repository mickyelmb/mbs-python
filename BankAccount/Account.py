

class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

"""
Account transactions

account=Account("balance.txt")
print(account.balance)
account.withdraw(100)
account.deposit(8700)
print(account.balance)
account.commit()

"""
class Checking(Account):
    """ This class generates checking account records """

    type="checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance-amount - self.fee


Jacks_checking=Checking("Jacks_balance.txt", 3)

Jacks_checking.deposit(5799)
Jacks_checking.transfer(300)
Jacks_checking.commit()
print(Jacks_checking.balance)
print(Jacks_checking.__doc__)
print(Jacks_checking.type)

Johns_checking=Checking("Johns_balance.txt", 3)

Johns_checking.deposit(5799)
Johns_checking.transfer(300)
Johns_checking.commit()
print(Johns_checking.balance)
