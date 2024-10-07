
MAX_NAME_LENGTH: int = 30    
"""Maximum number of characters accepted for the name."""
MAX_VERSION_LENGTH: int = 20
"""Maximum number of characters accepted for the version."""    
MAX_AUTHOR_LENGTH: int = 50
"""Maximum number of characters accepted for an author name."""    
MAX_DESCRIPTION_LENGTH: int = 250
"""Maximum number of characters accepted for the description."""    
MAX_HOMEPAGE_LENGTH: int = 150
"""Maximum number of characters accepted for the link to the homepage."""    
MAX_GAME_TYPE_LENGTH: int = 20
"""Maximum number of characters accepted for a game type."""    
MAX_PLATFORM_LENGTH: int = 30
"""Maximum number of characters accepted for the platform name."""    
MAX_PROGRAMMING_LANG_LENGTH: int = 30
"""Maximum number of characters accepted for the programming language name."""    
MAX_NUMBER_OF_AUTHORS: int = 5
"""Maximum number of authors accepted."""    
MAX_NUMBER_OF_COUNTRY_CODES: int = 5
"""Maximum number of country codes accepted."""    
MAX_NUMBER_OF_GAME_TYPES: int = 10
"""Maximum number of game types accepted."""

from dataclasses import dataclass
@dataclass(frozen=True)
class BotInfo:
    max_name_length = 30