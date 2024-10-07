from .bot_event import BotEvent


class BotDeathEvent(BotEvent):
    """Event occurring when another bot has died."""
    
    def __init__(self, turn_number:int, victim_id:int) -> None:
        """
        Initializes a new instance of the BotDeathEvent class.

        Args:
            turn_number (int): is the turn number when the bot died.
            victim_id (int): is the id of the bot that has died.
        """
        super().__init__(turn_number)
        self.victim_id = victim_id