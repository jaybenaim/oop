class Cat: 
    ''' 
    A class to represent cats so we can populate our software with a menagerie of feline friends.
    '''
    def __init__(self, name, preferred_food, meal_time): 
        self.name = name 
        self.preferred_food = preferred_food 
        self.meal_time = meal_time 
    def __str__(self): 
        return f'Name: {self.name}, Preferred Food: {self.preferred_food}, Meal Time: {self.meal_time}'
    def eats_at(self): 
        if self.meal_time > 0 and self.meal_time < 12: 
            return f'{self.name} eats at {self.meal_time} AM'
        elif self.meal_time > 12 and self.meal_time < 24: 
            return f'{self.name} eats at {self.meal_time} PM'
        else: 
            return f'{self.name} eats anytime'
    def meow(self): 
        if self.meal_time < 12: 
            return f'My name is {self.name}, I like to eat at {self.meal_time} AM. '
        elif self.meal_time > 12 and self.meal_time < 24: 
            return f'My name is {self.name}, I like to eat at {self.meal_time} PM. '
        else: 
            return "Something went wrong" 

moo = Cat('Moo', 'Salmon-tuna', 7) 
# print(moo) 
# pete = Cat('Pete', 'Whitefish-tuna', 14)
# print(pete) 
# print(moo.eats_at())
# print(pete.eats_at())
# print(moo.meow())
# print(pete.meow())




