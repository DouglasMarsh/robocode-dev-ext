import pytest
from botapi import InitialPostion

class TestInitialPosition:

    @pytest.mark.parametrize("input", [
        None, 
        ""
        " \t",
        " ,",
        ",,,",
        ", ,",
    ])
    def test_from_string_given_none_or_empty_returns_none(input):
        pos = InitialPostion.from_string( input )
        assert pos is None

    @pytest.mark.parametrize(["input", "expected"],[
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
    def test_from_string_given_input_returns_expected(input, x,y,direction):
        pos = InitialPostion.from_string( input )
        assert pos is not None
        assert pos.x == x
        assert pos.y == y
        assert pos.direction == direction    

    @pytest.mark.parametrize(["input", "expected"],[
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
    def test_from_string_given_input_returns_expected_string(input, expected):
        pos = InitialPostion.from_string( input )
        assert pos is not None
        assert str(pos) == expected