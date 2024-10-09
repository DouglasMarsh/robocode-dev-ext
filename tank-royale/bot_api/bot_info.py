""" bot_info module """

import json
from pathlib import Path
from platform import python_version
from dataclasses import dataclass
from typing import List, Self, Set, Optional
from bot_api import InitialPosition


import bot_api.util.country_code as CntryCodeUtil

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


@dataclass(frozen=True)
class BotInfo:
    """
    BotInfo class.<br>

    Properties:
        name            is the name of the bot (required).
        version         is the version of the bot (required).
        authors         is the author(s) of the bot (required).
        description     is a short description of the bot (optional).
        homepage        is the link to a homepage for the bot (optional).
        countryCodes    is the country code(s) for the bot (optional).
        gameTypes       is the game types that this bot can handle (optional).
        platform        is the platform used for running the bot (optional).
        programmingLang is the programming language used for developing the bot (optional).
        initialPosition is the initial position with starting coordinate and angle (optional).
    """

    name: str
    version: str
    authors: List[str]

    description: Optional[str] = None
    homepage: Optional[str] = None
    country_codes: Optional[List[str]] = None
    game_types: Optional[Set[str]] = None
    platform: Optional[str] = None
    programming_lang: Optional[str] = None

    initial_position: Optional[InitialPosition] = None

    @staticmethod
    def from_data_dict(data: dict) -> Self:
        """
        Creates a BotInfo object from a info dictionary

        Args:
            data (dict): dictionary object containing bot info

        Returns:
            BotInfo: bot info object constructed from the dict

        Raises:
            ValueError: If `name`, `version`, or `authors` are missing or blank.

        Example:
            {
              "name": "MyBot",
              "version": "1.0",
              "authors": "John Doe",
              "description": "Short description",
              "homepage": "https://somewhere.net/MyBot",
              "countryCodes": "us",
              "gameTypes": "classic, melee, 1v1",
              "platform": "PYTHON 3.11",
              "programmingLang": "Python 3.11",
              "initialPosition": "50,50, 90"
            }

        Notes:
            These fields are required as they are used to identify the bot:
            * name
            * version
            * authors

            These field can take comma seperated values:
            * authors, e.g. "John Doe, Jane Doe"
            * country_codes, e.g. "US, GB, CA"
            * game_types, e.g. "classic, melee, 1v1"

            The initial_position variable is optional and should ONLY be use for debugging.

            The game_types variable is optional, but can be used to limit which game types
            the bot is capable of participating in.
        """

        if not 'name' in data or not data["name"]:
            raise ValueError("The required field 'name' is missing or blank")
        if not 'version' in data or not data["version"]:
            raise ValueError("The required field 'version' is missing or blank")
        if not 'authors' in data or not data["authors"]:
            raise ValueError("The required field 'authors' is missing or blank")

        return BotInfo(
            name=data.get("name"),
            version=data.get("version"),
            authors=list(data.get("authors").split(",")),
            description=data.get("description", None),
            homepage=data.get("homepage", None),
            country_codes=list(data.get("countryCodes", "").split(",")),
            game_types=set(data.get("gameTypes", "").split(",")),
            platform=data.get("platform", None),
            programming_lang=data.get("programmingLang", None),
            initial_position=InitialPosition.from_string(
                data.get("initialPosition", "")
            ),
        )
    
    @staticmethod
    def from_json(json_str: str) -> Self:
        """
        Creates a BotInfo object from a json string
        The string is assumed to be in JSON format

        Args:
            json (str): json formatted BotInfo

        Returns:
            BotInfo: bot info object constructed from the JSON string

        Raises:
            ValueError: If `name`, `version`, or `authors` are missing or blank.

        Example:
            {
              "name": "MyBot",
              "version": "1.0",
              "authors": "John Doe",
              "description": "Short description",
              "homepage": "https://somewhere.net/MyBot",
              "countryCodes": "us",
              "gameTypes": "classic, melee, 1v1",
              "platform": "PYTHON 3.11",
              "programmingLang": "Python 3.11",
              "initialPosition": "50,50, 90"
            }

        Notes:
            These fields are required as they are used to identify the bot:
            * name
            * version
            * authors

            These field can take comma seperated values:
            * authors, e.g. "John Doe, Jane Doe"
            * country_codes, e.g. "US, GB, CA"
            * game_types, e.g. "classic, melee, 1v1"

            The initial_position variable is optional and should ONLY be use for debugging.

            The game_types variable is optional, but can be used to limit which game types
            the bot is capable of participating in.
        """

        data: dict = json.loads(json_str)
        return BotInfo.from_data_dict( data )
        
    @staticmethod
    def from_file(file_path: str) -> Self:
        """
        Creates a BotInfo object from a json file
        The file is assumed to be in JSON format

        Args:
            file_path (str): path to json formatted info file

        Returns:
            BotInfo: bot info object constructed from the JSON file

        Raises:
            FileNotFoundError: If json file is not found
            ValueError: If `name`, `version`, or `authors` are missing or blank.

        Example:
            {
              "name": "MyBot",
              "version": "1.0",
              "authors": "John Doe",
              "description": "Short description",
              "homepage": "https://somewhere.net/MyBot",
              "countryCodes": "us",
              "gameTypes": "classic, melee, 1v1",
              "platform": "PYTHON 3.11",
              "programmingLang": "Python 3.11",
              "initialPosition": "50,50, 90"
            }

        Notes:
            These fields are required as they are used to identify the bot:
            * name
            * version
            * authors

            These field can take comma seperated values:
            * authors, e.g. "John Doe, Jane Doe"
            * country_codes, e.g. "US, GB, CA"
            * game_types, e.g. "classic, melee, 1v1"

            The initial_position variable is optional and should ONLY be use for debugging.

            The game_types variable is optional, but can be used to limit which game types
            the bot is capable of participating in.
        """
        json_content = Path.cwd().joinpath( file_path ).read_text(encoding="utf-8")
        data = json.loads(json_content)
        return BotInfo.from_data_dict( data )

    
    def __post_init__(self):
        self.__process_name()
        self.__process_version()
        self.__process_authors()
        self.__process_description()
        self.__process_homepage()
        self.__process_country_codes()
        self.__process_game_types()
        self.__process_platform()
        self.__process_programming_lang()

    def __process_required_property(
        self, name: str, value: str, constraint: int
    ) -> str:
        if value is None or not value.strip():
            raise ValueError(f"'{name}' can not be None, empty, or blank")
        value = value.strip()
        if len(value) > constraint:
            raise ValueError(
                f"'{name}' length exceeds the maximum of {constraint} characters"
            )

        return value

    def __process_optional_property(
        self, name: str, value: str, constraint: int
    ) -> Optional[str]:
        value = value.strip() if value else ""

        if value and len(value.strip()) > constraint:
            raise ValueError(
                f"'{name}' length exceeds the maximum of {constraint} characters"
            )

        return value if value else None

    def __process_name(self):
        object.__setattr__(
            self,
            "name",
            self.__process_required_property("name", self.name, MAX_NAME_LENGTH),
        )

    def __process_version(self):
        object.__setattr__(
            self,
            "version",
            self.__process_required_property(
                "version", self.version, MAX_VERSION_LENGTH
            ),
        )

    def __process_authors(self):
        authors = self.authors
        authors = [] if not authors else [a.strip() for a in authors if a and a.strip()]
        if not authors:
            raise ValueError("'authors' cannot be null or empty or contain blanks")

        if len(self.authors) > MAX_NUMBER_OF_AUTHORS:
            raise ValueError(
                f"Size of 'authors' exceeds the maximum of {MAX_NUMBER_OF_AUTHORS}"
            )

        too_long = [a for a in authors if len(a) > MAX_AUTHOR_LENGTH]
        if too_long:
            raise ValueError(
                f"The following authors exceed the maximum of {MAX_AUTHOR_LENGTH} characters. {too_long}"
            )

        object.__setattr__(self, "authors", authors)

    def __process_description(self):
        object.__setattr__(
            self,
            "description",
            self.__process_optional_property(
                "description", self.description, MAX_DESCRIPTION_LENGTH
            ),
        )

    def __process_homepage(self):
        object.__setattr__(
            self,
            "homepage",
            self.__process_optional_property(
                "homepage", self.homepage, MAX_HOMEPAGE_LENGTH
            ),
        )

    def __process_country_codes(self):

        country_codes = [CntryCodeUtil.get_local_country_code()]
        if self.country_codes:
            if len(self.country_codes) > MAX_NUMBER_OF_COUNTRY_CODES:
                raise ValueError(
                    f"Size of 'country_codes' exceeds the maximum of {MAX_NUMBER_OF_COUNTRY_CODES}"
                )

            country_codes = [
                c.strip().upper()
                for c in self.country_codes
                if c
                and c.strip()
                and CntryCodeUtil.is_valid_country_code(c.strip().upper())
            ]
        if not country_codes:
            country_codes = [CntryCodeUtil.get_local_country_code()]
        object.__setattr__(self, "country_codes", country_codes)

    def __process_game_types(self):

        if self.game_types and len(self.game_types) > MAX_NUMBER_OF_GAME_TYPES:
            raise ValueError(
                f"Size of 'game_types' exceeds the maximum of {MAX_NUMBER_OF_GAME_TYPES}"
            )

        game_types = (
            set([gt.strip() for gt in self.game_types if gt and gt.strip()])
            if self.game_types
            else set()
        )

        too_long = [gt for gt in game_types if len(gt) > MAX_GAME_TYPE_LENGTH]
        if too_long:
            raise ValueError(
                f"The following 'game_types' exceed the maximum of {MAX_GAME_TYPE_LENGTH} characters. {too_long}"
            )

        object.__setattr__(self, "game_types", game_types)

    def __process_platform(self):
        object.__setattr__(
            self,
            "platform",
            (
                self.platform.strip()
                if self.platform and self.platform.strip()
                else f"PYTHON {python_version()}"
            ),
        )

        if len(self.platform) > MAX_PLATFORM_LENGTH:
            raise ValueError(
                f"'platform' length exceeds the maximum of {MAX_PLATFORM_LENGTH} characters"
            )

    def __process_programming_lang(self):
        object.__setattr__(
            self,
            "programming_lang",
            self.__process_optional_property(
                "programming_lang", self.programming_lang, MAX_PROGRAMMING_LANG_LENGTH
            ),
        )
