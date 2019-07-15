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
        if  self.gold_coins > 0 and self.gold_coins % 10 == 0:
            self.gold_coins += 1      
            self.level_up() 
        else: 
            self.gold_coins += 1 

    def do_battle(self, damage): 
        # take damage from health 
        # if zero health lose one live 
        if damage >= 0 and damage <= 10: 
            self.health_points -= damage
            if self.health_points <= 0:
                self.lives -= 1 
                self.health_points = 10
            elif self.lives <= 0: 
                self.restart() 
        
    def restart(self): 
        self.gold_coins = 0 
        self.health_points = 10 
        self.lives = 5 


new_player1 = Player() 
new_player2 = Player() 
new_player1.collect_treasure()
print(new_player1)
new_player2.do_battle(10) 
print(new_player2)
# new_player1.restart()  


