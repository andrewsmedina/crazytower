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

def test_created_round_raises_on_null_number():
    try:
        new_round = Round(number=None)
    except ValueError, error:
        assert str(error) == u"Round number can not be null"
        return 
    assert False

def test_created_round_raises_on_not_number():
    try:
        new_round = Round(number='foo')
    except ValueError, error:
        assert str(error) == u"Round number will be a number"
        return 
    assert False
    
def test_1000_health_point_when_start_a_round():
    new_round = Round(number=1)
    new_round.start()
    assert new_round.health == 1000

def test_200_gold_point_when_start_a_round():
    new_round = Round(number=1)
    new_round.start()
    assert new_round.gold == 200