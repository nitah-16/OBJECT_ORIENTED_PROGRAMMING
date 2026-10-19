class Account:
    def __init__(self,name,age,balance):
        self.name = name
        self._age = age
        self.__balance = 1000

    def check(self):
        return self.__balance 

    def new_balance(self,amount):
        self.__balance = amount
        print(f"{self.__balance}")

    def deposit(self,k):
        self.__balance += k

B1 = Account("Tete",13,6)

B1.new_balance (3000)



B1.deposit(1000)

print(B1.check())



# print(Account1.check())