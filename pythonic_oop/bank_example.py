from random import randrange


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def __repr__(self):
        return f'{self.__dict__}'

    def __call__(self, *args, **kwargs):
        print("\u001b[31mUsing callable method to show accounts in bank:\u001b[0m")
        for x in self.accounts:
            print(x)
        print('\u001b[32m--------------------\u001b[0m')


class Account:
    def __init__(self, customer, money):
        self.customer = customer
        self.number = randrange(10000001, 99999999)
        self.money = money

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'\u001b[32m------Customer------\n\u001b[0m{self.customer}\nAccount number: {self.number}\nAccount ' \
               f'amount: {self.money} $'

    def withdraw(self, amount):
        self.money -= amount
        print(f'{self.customer.name} has withdrawn {amount} $')

    def deposit(self, amount):
        self.money += amount
        print(f'{self.customer.name} has deposited {amount} $')

    def __call__(self, *args, **kwargs):
        print(self.__str__())


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age} years'


b = Bank('Nordea')
print(b)
b.accounts.append(Account(Customer('Hugo', 35), 758))
b.accounts.append(Account(Customer('Anders', 63), 95831))
print(b.accounts)

print(b.accounts[0].number)
print(b.accounts[0].customer.name)
c = Customer('Peter', 25)
b.accounts.append(Account(c, 12329))
print(b.accounts[1].number)
print(b.accounts[1].customer.name)
b()
b.accounts[0].withdraw(800)
b.accounts[0].deposit(1700)
b.accounts[1].deposit(2700)
b.accounts[2].withdraw(2100)
