import pytest
import bot_api.color as color

from bot_api import Color

@pytest.mark.parametrize("red,green,blue",[
    (0x00,0x00,0x00),
    (0xFF, 0xFF, 0xFF),
    (0x13, 0x9A, 0xF7)
])
def test_given_rgb_when_creating_color_then_created_color_matches_rgb(red: int, green:int, blue: int):
    c = Color( red, green, blue )

    assert c.red == red
    assert c.green == green
    assert c.blue == blue

@pytest.mark.parametrize("red,green,blue",[
    (-1, 70, 100),    # negative number (1st param)
    (50, -100, 100),  # negative number (2nd param)
    (50, 70, -1000),  # negative number (3rd param)
    (256, 255, 255),  # number too big  (1st param)
    (255, 1000, 0),   # number too big  (2nd param)
    (50, 100, 300),   # number too big  (3rd param)
])
def test_given_invalid_rgb_when_creating_color_then_throw_value_error(red: int, green:int, blue: int):
    with pytest.raises(ValueError):
        Color( red, green, blue )
