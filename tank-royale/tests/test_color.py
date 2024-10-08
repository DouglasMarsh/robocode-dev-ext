
import pytest
from dataclasses import dataclass
from bot_api import Color
from bot_api import color

@dataclass
class RGB:
    red: int
    green: int
    blue: int

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

class TestColorEquals:

    @pytest.mark.parametrize("rgb",[
        RGB(0x11,0x99,0xCC),
        RGB(0x12,0x34,0x56),
        RGB(0x78,0x9A,0xBC),
    ])
    def test_given_colors_with_same_rgb_are_equal(self, rgb: RGB):
        assert Color(rgb.red, rgb.green, rgb.blue) == Color(rgb.red, rgb.green, rgb.blue)
        
    @pytest.mark.parametrize("rgb1, rgb2",[
        (RGB(0x11,0x99,0xCC), RGB(0x12,0x34,0x56) ),
        (RGB(0x78,0x9A,0xBC), RGB(0x11,0x99,0xCC))
    ])
    def test_given_colors_with_different_rgb_are_notequal(self, rgb1, rgb2 ):
        assert Color(rgb1.red, rgb1.green, rgb1.blue) != Color(rgb2.red, rgb2.green, rgb2.blue)

    @pytest.mark.parametrize("rgb, rgb_str, hex_str",[
        ( RGB(0x00,0x00,0x00), "#000000", "000000", ),
        #( RGB(0x11,0x99,0xCC), "#1199cC","1199cC", ),
    ])
    def test_given_same_color_created_via_different_methods_are_equal(self, rgb: RGB, rgb_str:str, hex_str:str):
        color_from_init = Color(rgb.red, rgb.green, rgb.blue)
        color_from_string =  Color.from_string(rgb_str)
        color_from_hex = Color.from_hex(hex_str)

        assert color_from_init == color_from_string, "_init_ and from_string are not equal"
        assert color_from_init == color_from_hex, "_init_ and from_hex are not equal"
        assert color_from_string == color_from_hex, "from_string and from_hex are not equal"

class TestColorHashCode:
    @pytest.mark.parametrize("rgb, rgb_str, hex_str",[
        ( RGB(0x00,0x00,0x00), "#000000", "000000", ),
        ( RGB(0x11,0x99,0xCC), "#1199cC","1199cC", ),
    ])
    def test_given_same_color_created_via_different_methods_return_same_hash_code(self, rgb: RGB, rgb_str:str, hex_str:str):
        color_from_init = Color(rgb.red, rgb.green, rgb.blue)
        color_from_string =  Color.from_string(rgb_str)
        color_from_hex = Color.from_hex(hex_str)

        assert hash(color_from_init) == hash(color_from_string), "Hashes between _init_ and from_string don't match"
        assert hash(color_from_init) == hash(color_from_hex), "Hashes between _init_ and from_hex don't match"
        assert hash(color_from_string) == hash(color_from_hex), "Hashes between from_string and from_hex don't match"

    def test_given_different_colors_have_different_hash_codes(self):
        assert hash(Color(10,20,30)) != hash(Color.from_hex("1199CC"))
    
class TestColorToString:
    @pytest.mark.parametrize("rgb, rgb_str, hex_str",[
        ( RGB(0x00,0x00,0x00), "#000000", "000000", ),
        ( RGB(0x11,0x99,0xCC), "#1199cC","1199cC", ),
    ])
    def test_given_same_color_created_via_different_methods_calling_str_returns_same_hex_str(
        self, rgb: RGB, rgb_str:str, hex_str:str):

        color_from_init = Color(rgb.red, rgb.green, rgb.blue)
        color_from_string =  Color.from_string(rgb_str)
        color_from_hex = Color.from_hex(hex_str)

        assert str(color_from_init).casefold() == hex_str.casefold(), "str from _init_ don't match"
        assert str(color_from_string).casefold() == hex_str.casefold(), "str from_string don't match"
        assert str(color_from_hex).casefold() == hex_str.casefold(), "str from_hex don't match"

    
class TestColorConstants:
    @pytest.mark.parametrize("color, expected",[
        pytest.param(color.WHITE, "FFFFFF", id="WHITE"),
        pytest.param(color.SILVER, "C0C0C0", id="SILVER"),
        pytest.param(color.GRAY, "808080", id="GRAY"),
        pytest.param(color.BLACK, "000000", id="BLACK"),
        pytest.param(color.RED, "FF0000", id="RED"),
        pytest.param(color.MAROON, "800000", id="MAROON"),
        pytest.param(color.YELLOW, "FFFF00", id="YELLOW"),
        pytest.param(color.OLIVE, "808000", id="OLIVE"),
        pytest.param(color.LIME, "00FF00", id="LIME"),
        pytest.param(color.GREEN, "008000", id="GREEN"),
        pytest.param(color.CYAN, "00FFFF", id="CYAN"),
        pytest.param(color.TEAL, "008080", id="TEAL"),
        pytest.param(color.BLUE, "0000FF", id="BLUE"),
        pytest.param(color.NAVY, "000080", id="NAVY"),
        pytest.param(color.FUCHSIA, "FF00FF", id="FUCHSIA"),
        pytest.param(color.PURPLE, "800080", id="PURPLE"),
        pytest.param(color.ORANGE, "FF8000", id="ORANGE"),
    ])
    def test_given_color_const_when_getting_color_value_value_is_correct(self, color: Color, expected: str):
        assert str(color).casefold() == expected.casefold()
        