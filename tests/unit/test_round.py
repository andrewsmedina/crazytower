from crazytower.models import Round

def test_can_create_round():
    new_round = Round(number=1)
    assert new_round

