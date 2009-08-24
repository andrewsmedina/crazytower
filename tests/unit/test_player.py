from crazytower.models import Player

def test_can_create_player():
    new_player = Player(name="andrews")
    assert new_player

def test_create_player_is_a_Player():
    new_player = Player(name="andrews")
    assert isinstance(new_player, Player)
    
def test_created_player_keeps_name():
    new_player = Player(name="andrews")
    assert new_player.name == "andrews"
    
def test_create_player_raises_on_null_name():
    try:
        new_player = Player(name=None)
    except ValueError, error:
        assert str(error) == u"Player name can not be null or empty"
        return 
    assert False
    
def test_create_player_raises_on_empty_name():
    try:
        new_player = Player(name="")
    except ValueError, error:
        assert str(error) == u"Player name can not be null or empty"
        return 
    assert False
    