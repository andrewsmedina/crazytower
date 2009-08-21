from crazytower.models import Game, Player

def test_can_create_game():
    new_game = Game()
    assert new_game
    
def test_created_game_is_a_Game():
    new_game = Game()
    assert isinstance(new_game, Game)
    
def test_created_game_has_no_players():
    new_game = Game()
    assert not new_game.players
    
def test_can_add_player_for_game():
    new_game = Game()
    new_game.add_player(Player(name="andrews"))
    
    assert len(new_game.players) == 1
    assert new_game.players[0].name == 'andrews'
