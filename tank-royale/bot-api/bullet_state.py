from dataclasses import dataclass, field
from .color import Color

@dataclass(frozen=True)
class BulletState:
    bullet_id: int
    owner_id: int
    power: float
    x: float
    y: float
    direction: float    
    speed: float = field(init=False)
    color: Color

    def __post_init__(self):
        self.speed = 20 - 3 * self.power
