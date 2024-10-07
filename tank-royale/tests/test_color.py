import pytest

from bot_api import Color

class TestColorConstructor:
    @pytest.mark.parametrize("red,green,blue",[
        (0x00,0x00,0x00),
        (0xFF, 0xFF, 0xFF),
        (0x13, 0x9A, 0xF7)
    ])
    def test_given_rgb_when_creating_color_then_created_color_matches_rgb(self, red: int, green:int, blue: int):
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
    def test_given_invalid_rgb_when_creating_color_then_throw_value_error(self, red: int, green:int, blue: int):
        with pytest.raises(ValueError):
            Color( red, green, blue )

class TestColorFromString:
    @pytest.mark.parametrize("rgb,red,green,blue",[
        ("#000000",0x00,0x00,0x00),
        ("#000",0x00,0x00,0x00),
        ("#FfFfFf",0xFF,0xFF,0xFF),
        ("#fFF",0xFF,0xFF,0xFF),
        ("#1199cC",0x11,0x99,0xCC),
        ("#19C",0x11,0x99,0xCC),
        ("  #123456",0x12,0x34,0x56), # White spaces
        ("#789aBc\t",0x78,0x9A,0xBC), # White space
        ("  #123",0x11,0x22,0x33),    # White spaces
        ("#AbC\t",0xAA,0xBB,0xCC)     # White space
    ])
    def test_given_rgb_string_when_calling_from_string_then_created_color_matches_rgb(self, rgb: str, red: int, green:int, blue: int):
        c = Color.from_string( rgb )

        assert c.red == red
        assert c.green == green
        assert c.blue == blue
    
    
    @pytest.mark.parametrize("rgb",[
        "#00000",    # Too short
        "#0000000",  # Too long
        "#0000 00",  # White space
        "#xxxxxx",   # Wrong letters
        "#abcdeG",   # Wrong letter
        "000000",    # Missing hash (#)
    ])
    def test_given_invalid_rgb_string_when_calling_from_string_then_then_throw_value_error(self, rgb: str):
        with pytest.raises(ValueError):
            Color.from_string( rgb )

class TestColorFromHex:
    @pytest.mark.parametrize("hex_string,red,green,blue",[
        ("000000",0x00,0x00,0x00),
        ("000",0x00,0x00,0x00),
        ("FfFfFf",0xFF,0xFF,0xFF),
        ("fFF",0xFF,0xFF,0xFF),
        ("1199cC",0x11,0x99,0xCC),
        ("19C",0x11,0x99,0xCC),
        ("  123456",0x12,0x34,0x56), # White spaces
        ("789aBc\t",0x78,0x9A,0xBC), # White space
        ("  123",0x11,0x22,0x33),    # White spaces
        ("AbC\t",0xAA,0xBB,0xCC)     # White space
    ])
    def test_given_rgb_hex_string_when_calling_from_hex_then_created_color_matches_rgb(self, hex_string: str, red: int, green:int, blue: int):
        c = Color.from_hex( hex_string )

        assert c.red == red
        assert c.green == green
        assert c.blue == blue

    @pytest.mark.parametrize("hex_string",[
        "00000",    # Too short
        "0000000",  # Too long
        "0000 00",  # White space
        "xxxxxx",   # Wrong letters
        "abcdeG",   # Wrong letter
    ])
    def test_given_invalid_rgb_hex_string_when_calling_from_hex_then_then_throw_value_error(self, hex_string: str):
        with pytest.raises(ValueError):
            Color.from_hex( hex_string )

class TestColorToHex:
    @pytest.mark.parametrize("hex_string",[
        "000000",
        "FEDCBA",
        "123456"
    ])
    def test_given_rgb_hex_string_when_calling_to_hex_returns_matching_hex_string(self, hex_string: str):
        c = Color.from_hex( hex_string )
        assert c.to_hex().casefold() == hex_string.casefold()

