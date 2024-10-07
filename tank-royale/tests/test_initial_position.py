import pytest
from bot_api import InitialPosition

@pytest.mark.parametrize("_input", [
    None,
    ""
    " \t",
    " ,",
    ",,,",
    ", ,",
])
def test_from_string_given_none_or_empty_returns_none(_input):
    pos = InitialPosition.from_string( _input )
    assert pos is None

@pytest.mark.parametrize("_input, x,y,direction",[
    ("0,0,0", 0,0,0),
    ("50,50, 90", 50,50,90),
    ("12.23, -123.3, 45.5", 12.23, -123.3, 45.5),
    (" 50 ", 50,None,None),
    (" 50.1  70.2 ", 50.1,70.2,None),
    ("50.1 70.2, 678.3", 50.1,70.2,678.3),
    ("50.1  , 70.2, 678.3", 50.1,70.2,678.3),
    ("50.1 70.2, 678.3 789.1", 50.1,70.2,678.3),
    ("50.1  , , 678.3", 50.1,None,678.3),
    (", , 678.3", None,None,678.3)
])
def test_from_string_given_input_returns_expected(_input, x,y,direction):
    pos = InitialPosition.from_string( _input )
    assert pos is not None
    assert pos.x == x
    assert pos.y == y
    assert pos.direction == direction    

@pytest.mark.parametrize(["_input", "expected"],[
("0,0,0", "0,0,0"),
("50,50, 90", "50,50,90"),
("12.23, -123.3, 45.5", "12.23,-123.3,45.5"),
(" 50 ", "50,,"),
(" 50.1  70.2 ", "50.1,70.2,"),
("50.1 70.2, 678.3", "50.1,70.2,678.3"),
("50.1  , 70.2, 678.3", "50.1,70.2,678.3"),
("50.1 70.2, 678.3 789.1", "50.1,70.2,678.3"),
("50.1  , , 678.3", "50.1,,678.3"),
(", , 678.3", ",,678.3")
])
def test_from_string_given_input_returns_expected_string(_input, expected):
    pos = InitialPosition.from_string( _input )
    assert pos is not None
    assert str(pos) == expected


@pytest.mark.parametrize("_input, x,y,direction",[
    ("0,0,0", 0,0,0),
    ("50,50, 90", 50,50,90),
    ("12.23, -123.3, 45.5", 12.23, -123.3, 45.5),
    (" 50 ", 50,None,None),
    (" 50.1  70.2 ", 50.1,70.2,None),
    ("50.1 70.2, 678.3", 50.1,70.2,678.3),
    ("50.1  , 70.2, 678.3", 50.1,70.2,678.3),
    ("50.1 70.2, 678.3 789.1", 50.1,70.2,678.3),
    ("50.1  , , 678.3", 50.1,None,678.3),
    (", , 678.3", None,None,678.3)
])
def test_from_string_and_constructor_return_equality(_input, x,y,direction):
    actual_from_string = InitialPosition.from_string( _input )
    actual_from_const = InitialPosition(x, y, direction )
    
    assert actual_from_string == actual_from_const
    assert hash( actual_from_string) == hash( actual_from_const )

