""" robocode.tankroyal.botapi.bot_state """

from dataclasses import dataclass
from .color import Color

@dataclass(frozen=True)
class BotState:
    """
    BotState class

    Args:
        is_droid: Flag specifying if the bot is a droid.
        energy: Energy level.
        x: X coordinate.
        y: Y coordinate.
        direction: Driving direction in degrees.
        gun_direction: Gun direction in degrees.
        radar_direction: Radar direction in degrees.
        radar_sweep: Radar sweep angle in degrees.
        speed: Speed measured in pixels per turn.
        turn_rate: Turn rate of the body in degrees per turn.
        gun_turn_rate: Turn rate of the gun in degrees per turn.
        radar_turn_rate: Turn rate of the radar in degrees per turn.
        gun_heat: Gun heat.
        body_color: Body color.
        turret_color: Gun turret color.
        radar_color: Radar color.
        bullet_color: Bullet color.
        scan_color: Scan arc color.
        tracks_color: Tracks color.
        gun_color: Gun color.
    """
    
    
    is_droid: bool    
    energy: float    
    x: float
    y: float
    direction: float
    gun_direction: float
    radar_direction: float
    radar_sweep: float
    speed: float
    turn_rate: float
    gun_turn_rate: float
    radar_turn_rate: float
    gun_heat: float
    body_color: Color
    turret_color: Color
    radar_color: Color
    bullet_color: Color
    scan_color: Color
    tracks_color: Color
    gun_color: Color
