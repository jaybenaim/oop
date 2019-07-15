class BankAccount: 
    ''' 
    A class representing a bank accounts balance and interest rate 
    ''' 

    def __init__(self, balance, interest_rate): 
        self.balance = balance 
        self.interest_rate = interest_rate 

    def __str__(self): 
        return f' Balance: {self.balance} , Interest Rate: {self.interest_rate} '


jays = BankAccount(433, 10) 
print(jays)
print(jays.balance) 


