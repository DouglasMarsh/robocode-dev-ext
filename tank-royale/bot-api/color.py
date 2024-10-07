import re
from typing import Self


class Color:
    NUMERIC_RGB = re.compile('^#[0-9a-fA-F]{3,6}$')
    THREE_HEX_DIGITS = re.compile('^[0-9a-fA-F]{3}$')
    SIX_HEX_DIGITS = re.compile('^[0-9a-fA-F]{6}$')

    WHITE = Self.from_hex("FFFFFF")
    SILVER = Self.from_hex("C0C0C0")
    GRAY = Self.from_hex("808080")
    BLACK = Self.from_hex("000000")
    RED = Self.from_hex("FF0000")
    MAROON = Self.from_hex("800000")
    YELLOW = Self.from_hex("FFFF00")
    OLIVE = Self.from_hex("808000")
    LIME = Self.from_hex("00FF00")
    GREEN = Self.from_hex("008000")
    CYAN = Self.from_hex("00FFFF")
    TEAL = Self.from_hex("008080")
    BLUE = Self.from_hex("0000FF")
    NAVY = Self.from_hex("000080")
    FUCHSIA = Self.from_hex("FF00FF")
    PURPLE = Self.from_hex("800080")
    ORANGE = Self.from_hex("FF8000")
    
    @staticmethod
    def from_hex( hex_triplet: str) -> Self:
        """
        Creates a color from a hex triplet. A hex triplet is either three or six hexadecimal digits that represents an
        RGB Color.
        An example of a hex triplet is "09C" or "0099CC", which both represents the same color.

        Args:
            hex_triplet (str): is a string containing either a three or six hexadecimal numbers like "09C" or "0099CC".

        Returns:
            Color: the created Color object

        References:
            Colors RGB: https://www.w3schools.com/colors/colors_rgb.asp
            Web Colors: https://en.wikipedia.org/wiki/Web_colors
        """
        if bool(Color.THREE_HEX_DIGITS.search( hex_triplet)):
            return Color.__from_three_hex_digits( hex_triplet )
       
        if bool( Color.SIX_HEX_DIGITS.search( hex_triplet )):
            return Color.__from_six_hex_digits( hex_triplet )
       
        raise ValueError('You must supply 3 or 6 hex digits [0-9a-fA-F], e.g. "09C" or "0099CC"')

    @staticmethod
    def from_string(color: str) -> Self:
        if len(color) == 0: return None

        if not bool(Color.NUMERIC_RGB.search(color)):
            raise ValueError( 'You must supply the string in numeric RGB format #[0-9a-fA-F], e.g. "#09C" or "#0099CC"' )

        return Color.from_hex( color[1:] )
    
    
    @staticmethod
    def __to_hex(value: int) -> str:
        return f'{(value >> 4):x}{(value & 0xF):}'
    
    @staticmethod
    def __from_three_hex_digits(three_hex_digits: str) -> Self:
        r = int( three_hex_digits[0], 16)
        g = int( three_hex_digits[1], 16)
        b = int( three_hex_digits[2], 16)

        r = r << 4 | r
        g = g << 4 | g
        b = b << 4 | b
        return  Color(r, g, b)
    
    @staticmethod
    def __from_six_hex_digits(six_hex_digits: str) -> Self:
        r = int( six_hex_digits[0:2], 16)
        g = int( six_hex_digits[2:4], 16)
        b = int( six_hex_digits[4:6], 16)

        return  Color(r, g, b)


    def __init__(self, red:int, green:int, blue:int) -> None:
        """
        Creates a Color from RGB values.

        Args:
            red (int): is the red color component of the RGB color in the range [0 - 255]
            green (int): is the green color component of the RGB color in the range [0 - 255]
            blue (int): is the blue color component of the RGB color in the range [0 - 255]
        Ref:
            Colors RGB: https://www.w3schools.com/colors/colors_rgb.asp 
        """
        if red < 0 or red > 255:
            raise ValueError("The 'red' color component must be in the range 0 - 255")
        if green < 0 or green > 255:
            raise ValueError("The 'green' color component must be in the range 0 - 255")
        if blue < 0 or blue > 255:
            raise ValueError("The 'blue' color component must be in the range 0 - 255")

        self.__red = red
        self.__green = green
        self.__blue = blue 

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Color):
            return self.__red == value.__red \
               and self.__green == value.__green \
               and self.__blue == value.__blue
        
        return False

    def __hash__(self) -> int:
        return f"{self.__red},{self.__green},{self.__blue}".__hash__()
    
    def __str__(self) -> str:
        return self.to_hex()

    def to_hex(self) -> str:
        """
        Returns the color as a hex triplet of six hexadecimal digits representing an RGB color, e.g. "0099CC".

        Returns:
            str: the color as a hex triplet of six hexadecimal digits representing an RGB color, e.g. "0099CC".
        """
        return Color.__to_hex( self.__red ) + Color.__to_hex( self.__green ) + Color.__to_hex( self.__blue )

    @property
    def red(self):
        return self.__red
    @property
    def green(self):
        return self.__green
    @property
    def blue(self):
        return self.__blue