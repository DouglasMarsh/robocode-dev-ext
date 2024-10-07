class BotEvent:
    """
    Bot event occurring during a battle.
    """

    def __init__(self, turn_number:int) -> None:
        """
        Initializes a new instance of the Event class.

        Args:
            turn_number (int): is the turn number when the event occurred.
        """
        self.turn_number = turn_number

    def is_critical(self) -> bool:
        """
        Indicates if this event is critical, and hence should not be removed from event queue when it gets old.

        Returns:
            bool: true if this event is critical; false otherwise. Default is false.
        """
        return False