from dataclasses import dataclass
from typing import Optional, Self
import locale
import re

# Set the locale to the invariant culture
locale.setlocale(locale.LC_ALL, 'C')

@dataclass(frozen=True)
class InitialPosition:
    """
    InitialPosition class
    
    Initial starting position containing a start coordinate (x,y) and the shared direction of the body, gun, and radar.
    
    The initial position is only used when debugging to request the server to let a bot start at a specific position.
    Note that initial starting positions must be enabled at the server-side; otherwise the initial starting position
    is ignored.

    Args:
        x: is the x coordinate, where None means it is random. 
        y: is the y coordinate, where None means it is random.
        direction: is the shared direction of the body, gun, and radaar where None means it is random
    """

    x: Optional[float]
    y: Optional[float]
    direction: Optional[float]


    @staticmethod
    def from_string(initial_position: str) -> Self:
        """ 
        Constructs an InitialPosition object from a comma delimited string
        """
        if initial_position is None:
            return None

        initial_position = initial_position.strip()

        if initial_position:
            values = [n.strip() for n in re.split("\\s*,\\s*|\\s+", initial_position)]

            if not values:
                return None

            x = float(values[0]) if values[0] else None
            y = float(values[1]) if 1 < len(values) and values[1] else None
            direction = float(values[2]) if 2 < len(values) and values[2] else None
            
            if x is not None or y is not None or direction is not None :
                return InitialPosition(x, y, direction)
   
        return None

    def __hash__(self) -> int:
        args = [self.x, self.y, self.direction]
        hash_value = 0
        for arg in args:
            hash_value = hash_value * 31 + hash(arg)
        return hash_value

    def __str__(self) -> str:
        
        x = f"{self.x:n}" if self.x is not None else ""
        y = f"{self.y:n}" if self.y is not None else ""
        d = f"{self.direction:n}" if self.direction is not None else ""

        if x or y or d:
            return f"{x},{y},{d}"
        
        return ""

    def __eq__(self, value: object) -> bool:
        if isinstance(value, InitialPosition):
            return hash( self ) == hash( value )
        return False
