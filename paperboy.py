class Paperboy: 
    '''
    This class will represent a paperboy and his amount of papers delivered and amount 
    of money made 
    ''' 

    def __init__(self, name, experience, earnings = 0): 
        self.name = name
        self.experience = experience 
        self.earnings = earnings
          
        

    def __str__(self): 
        return f'My name is {self.name}, I made {self.earnings}.'
    
    def quota(self): 
        new_quota = 50
        exp = self.experience / 2  
        new_quota += self.experience / 2
        return new_quota 

    def deliver(self, start_addr, end_addr): 
        total_houses = end_addr - start_addr 
        if total_houses >= self.quota():
            over_total = total_houses * .55
            earn = round(over_total, 2) 
            self.earnings += earn  
        elif total_houses <= self.quota():
            under_total = total_houses * .25 
            under_total -= 2 
            earn = round(under_total, 2) 
            self.earnings += earn
        else: 
            earn = round(self.earnings) 
            return self.earnings  

jack = Paperboy('Jack', 0)

jack.quota() 
jack.deliver(1, 51)
print(jack) 
