""" Support Color represented in RGB format. """

import re
from typing import Self
from dataclasses import dataclass

NUMERIC_RGB = re.compile("^#[0-9a-fA-F]{3,6}$")
THREE_HEX_DIGITS = re.compile("^[0-9a-fA-F]{3}$")
SIX_HEX_DIGITS = re.compile("^[0-9a-fA-F]{6}$")

# Declaring namedtuple()


@dataclass(frozen=True)
class Color:
    """
    Color represented in RGB format.

    Args:
        red (int): is the red color component of the RGB color in the range [0 - 255]
        green (int): is the green color component of the RGB color in the range [0 - 255]
        blue (int): is the blue color component of the RGB color in the range [0 - 255]
    Ref:
        Colors RGB: https://www.w3schools.com/colors/colors_rgb.asp
    """

    red: int
    green: int
    blue: int

    def __post_init__(self):
        if self.red < 0 or self.red > 255:
            raise ValueError("The 'red' color component must be in the range 0 - 255")
        if self.green < 0 or self.green > 255:
            raise ValueError("The 'green' color component must be in the range 0 - 255")
        if self.blue < 0 or self.blue > 255:
            raise ValueError("The 'blue' color component must be in the range 0 - 255")

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Color):
            return (
                self.red == value.red
                and self.green == value.green
                and self.blue == value.blue
            )

        return False

    def __hash__(self) -> int:
        args = [self.red, self.green, self.blue]
        hash_value = 0
        for arg in args:
            hash_value = hash_value * 31 + hash(arg)
        return hash_value

    def __str__(self) -> str:
        return self.to_hex()

    def to_hex(self) -> str:
        """
        Returns the color as a hex triplet of six hexadecimal digits representing an RGB color
        e.g. "0099CC".

        Returns:
            str: the color as a hex triplet of six hexadecimal digits representing an RGB color
            e.g. "0099CC".
        """
        return (
            Color.__to_hex(self.red)
            + Color.__to_hex(self.green)
            + Color.__to_hex(self.blue)
        )

    @staticmethod
    def from_hex(hex_triplet: str) -> Self:
        """
        Creates a color from a hex triplet.
        A hex triplet is either three or six hexadecimal digits that represents an RGB Color.
        An example of a hex triplet is "09C" or "0099CC", which both represents the same color.

        Args:
            hex_triplet (str): is a string containing either a three or six hexadecimal numbers
            like "09C" or "0099CC".

        Returns:
            Color: the created Color object

        References:
            Colors RGB: https://www.w3schools.com/colors/colors_rgb.asp
            Web Colors: https://en.wikipedia.org/wiki/Web_colors
        """

        hex_triplet = hex_triplet.strip()

        if bool(THREE_HEX_DIGITS.search(hex_triplet)):
            return Color.__from_three_hex_digits(hex_triplet)

        if bool(SIX_HEX_DIGITS.search(hex_triplet)):
            return Color.__from_six_hex_digits(hex_triplet)

        raise ValueError(
            'You must supply 3 or 6 hex digits [0-9a-fA-F], e.g. "09C" or "0099CC"'
        )

    @staticmethod
    def from_string(color: str) -> Self:
        """
        Creates a color from a string.
        Currently, only numeric RGB values are supported.
        This method works the same was as from_hex
        except that is required as hash sign before the hex value.
        An example of a numeric RGB value is "#09C" or "#0099CC",
        which both represents the same color.

        Args:
            color is a string containing either a three or six hexadecimal RGB values
            like "#09C" or "#0099CC".

        Returns:
            Color: the created Color object; None if the input parameter is None

        References:
            Colors RGB: https://www.w3schools.com/colors/colors_rgb.asp
            Web Colors: https://en.wikipedia.org/wiki/Web_colors
        """

        color = color.strip()
        if color and bool(NUMERIC_RGB.search(color)):
            return Color.from_hex(color[1:])

        raise ValueError(
            "You must supply the string in numeric RGB format #[0-9a-fA-F],"
            + ' e.g. "#09C" or "#0099CC"'
        )

    @staticmethod
    def __to_hex(value: int) -> str:
        return f"{(value >> 4):x}{(value & 0xF):x}"

    @staticmethod
    def __from_three_hex_digits(three_hex_digits: str) -> Self:
        r = int(three_hex_digits[0], 16)
        g = int(three_hex_digits[1], 16)
        b = int(three_hex_digits[2], 16)

        r = r << 4 | r
        g = g << 4 | g
        b = b << 4 | b
        return Color(r, g, b)

    @staticmethod
    def __from_six_hex_digits(six_hex_digits: str) -> Self:
        r = int(six_hex_digits[0:2], 16)
        g = int(six_hex_digits[2:4], 16)
        b = int(six_hex_digits[4:6], 16)

        return Color(r, g, b)


WHITE = Color.from_hex("FFFFFF")
SILVER = Color.from_hex("C0C0C0")
GRAY = Color.from_hex("808080")
BLACK = Color.from_hex("000000")
RED = Color.from_hex("FF0000")
MAROON = Color.from_hex("800000")
YELLOW = Color.from_hex("FFFF00")
OLIVE = Color.from_hex("808000")
LIME = Color.from_hex("00FF00")
GREEN = Color.from_hex("008000")
CYAN = Color.from_hex("00FFFF")
TEAL = Color.from_hex("008080")
BLUE = Color.from_hex("0000FF")
NAVY = Color.from_hex("000080")
FUCHSIA = Color.from_hex("FF00FF")
PURPLE = Color.from_hex("800080")
ORANGE = Color.from_hex("FF8000")
