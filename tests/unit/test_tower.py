from crazytower.models import Tower

def test_can_create_tower():
    new_tower = Tower(x=10, y=10)
    assert new_tower

def test_create_tower_is_a_Tower():
    new_tower = Tower(x=10, y=10)
    assert isinstance(new_tower, Tower)
    
def test_created_tower_keeps_x():
    new_tower = Tower(x=10, y=10)
    assert new_tower.x == 10
    
def test_create_tower_keeps_y():
    new_tower = Tower(x=10, y=10)
    assert new_tower.y == 10
    
def test_created_tower_raises_on_null_x():
    try:
        new_tower = Tower(x=None, y=10)
    except ValueError, error:
        assert str(error) == u'Tower x can not be null'
        return
    assert False

def test_created_twoer_raises_on_x_not_number():
    try:
        new_tower = Tower(x='foo', y=10)
    except ValueError, error:
        assert str(error) == u'Tower x will be a number'
        return
    assert False

def test_created_tower_raises_on_null_y():
    try:
        new_tower = Tower(x=10, y=None)
    except ValueError, error:
        assert str(error) == u'Tower y can not be null'
        return
    assert False

def test_created_twoer_raises_on_y_not_number():
    try:
        new_tower = Tower(x=10, y='foo')
    except ValueError, error:
        assert str(error) == u'Tower y will be a number'
        return
    assert False   