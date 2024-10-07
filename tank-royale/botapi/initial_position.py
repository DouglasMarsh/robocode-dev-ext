from dataclasses import dataclass, field
from typing import Optional, Self
import locale

# Set the locale to the invariant culture
locale.setlocale(locale.LC_ALL, 'C')

@dataclass(frozen=True)
class InitialPostion:
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
    def fromString(initial_position: str) -> Self:
        initial_position = initial_position or initial_position.strip()

        if initial_position:
            values = [n.strip() for n in initial_position.split(',')]
            
            if len(values) < 1: return None

            x = float(values[0]) if values[0] else None
            y = float(values[1]) if len(values) >= 2 and values[1] else None
            dir = float(values[2]) if len(values) >= 3 and values[2] else None
            
            return InitialPostion(x, y, dir)
        
        return None
        
    def __hash__(self) -> int:
        args = [self.x, self.y, self.direction]
        hash_value = 0
        for arg in args:
            hash_value = hash_value * 31 + hash(arg)
        return hash_value

    def __str__(self) -> str:
        return f"{self.x:n},{self.y:n},{self.direction:n}"

    def __eq__(self, value: object) -> bool:
        if isinstance(value, InitialPostion):
            return hash( self ) == hash( value )        
        return False
