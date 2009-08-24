class Player(object):
    
    def __init__(self, name):

        if not name:
            raise ValueError(u"Player name can not be null or empty")
            
        self.name = name

class Game(object):
    
    def __init__(self):
        self.players = []
        
    def add_player(self, player):
        self.players.append(player)

class Round(object):
    
    def __init__(self, number):
        
        if not number:
            raise ValueError(u"Round number can not be null")
            
        if not isinstance(number, int):
            raise ValueError(u"Round number will be a number")
            
        self.number = number
