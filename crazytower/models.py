class Tower(object):
    
    def __init__(self, x, y):
        
        if not x:
            raise ValueError(u'Tower x can not be null')
            
        if not isinstance(x, int):
            raise ValueError(u'Tower x will be a number')
            
        if not y:
            raise ValueError(u'Tower y can not be null')

        if not isinstance(y, int):
            raise ValueError(u'Tower y will be a number')
            
        self.x = x
        self.y = y

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
        
    def start(self):
        self.health = 1000
        self.gold = 200
