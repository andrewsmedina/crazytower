class Player(object):
    
    def __init__(self, name):

        if not name:
            raise ValueError(u"Player name can not be null or empty")
            
        self.name = name

class Game(object):
    pass