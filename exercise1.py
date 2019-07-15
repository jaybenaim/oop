class BankAccount: 
    ''' 
    A class representing a bank accounts balance and interest rate 
    ''' 

    def __init__(self, balance, interest_rate): 
        self.balance = balance 
        self.interest_rate = interest_rate 

    def __str__(self): 
        return f' Balance: {self.balance} , Interest Rate: {self.interest_rate} '

    def deposit(self, amount): 
        self.balance += amount 
        return self.balance 
    
    def withdraw(self, amount): 
        self.balance -= amount 
        return self.balance 
    
jays = BankAccount(433, 10) 
print(jays)
print(jays.balance) 

jays.deposit(222)
print(jays.balance)
jays.withdraw(600) 
print(jays.balance) 



