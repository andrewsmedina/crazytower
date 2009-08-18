from crazytower.models import Game

def test_can_create_game():
    new_game = Game()
    assert new_game
    
def test_created_game_is_a_Game():
    new_game = Game()
    assert isinstance(new_game, Game)