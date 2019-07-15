class Player: 
    def __init__(self, gold_coins = 0, health_points = 10, lives = 5): 
        self.gold_coins = gold_coins
        self.health_points = health_points 
        self.lives = lives
    def __str__(self): 
        return f'Coins: {self.gold_coins} Health: {self.health_points} Lives: {self.lives}'
    
    def level_up(self): 
        self.lives += 1 
        return self.lives 

    def collect_treasure(self): 
        gold_coins += 1 
        if gold_coins % 10 == 0: 
            self.level_up() 
        else: 


new_player1 = Player(100, 100) 
new_player1.level_up() 
print(new_player1) 
