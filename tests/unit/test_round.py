from crazytower.models import Round

def test_can_create_round():
    new_round = Round(number=1)
    assert new_round
    
def test_created_round_is_a_Round():
    new_round = Round(number=1)
    assert isinstance(new_round, Round)

def test_created_round_keeps_number():
    new_round = Round(number=1)
    assert new_round.number == 1

