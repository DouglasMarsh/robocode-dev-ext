# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import json
from platform import python_version
import pytest
from bot_api import InitialPosition, bot_info, BotInfo
import re

NAME = "  TestBot  "
VERSION = "  1.0  "
AUTHORS = [" Author 1  ", " Author 2 "]
DESCRIPTION = "  short description "
HOME_PAGE = " https://testbot.robocode.dev "
COUNTRY_CODES = [" gb ", "  US "]
GAME_TYPES = set([" classic ", " melee ", " 1v1 "])
PLATFORM = " PYTHON 3 "
PROGRAMMING_LANGUAGE = " PYTHON 3.11 "
INITIAL_POSITION = InitialPosition.from_string("  10, 20, 30  ")


prefilled_bot = BotInfo(
    name=NAME,
    version=VERSION,
    authors=AUTHORS,
    description=DESCRIPTION,
    homepage=HOME_PAGE,
    country_codes=COUNTRY_CODES,
    game_types=GAME_TYPES,
    platform=PLATFORM,
    programming_lang=PROGRAMMING_LANGUAGE,
    initial_position=INITIAL_POSITION,
)

BLANK_STRINGS = [None, "", " ", "\t ", "\n"]


class TestBotInfoName:
    def test_name_is_trimmed(self):
        assert prefilled_bot.name == NAME.strip()

    @pytest.mark.parametrize("name", BLANK_STRINGS)
    def test_none_empty_blank_raises_error(self, name):
        with pytest.raises(ValueError):
            BotInfo(name=name, version=VERSION, authors=AUTHORS)

    def test_with_maxlength_returns_name(self):
        max_name = NAME.strip().ljust(bot_info.MAX_NAME_LENGTH, "x")

        bot = BotInfo(name=max_name, version=VERSION, authors=AUTHORS)
        assert bot.name == max_name

    def test_exceeding_maxlength_raises_error(self):
        name_too_big = NAME.strip().ljust(bot_info.MAX_NAME_LENGTH + 1, "x")
        with pytest.raises(
            ValueError,
            match=f"'name' length exceeds the maximum of {bot_info.MAX_NAME_LENGTH} characters",
        ):
            BotInfo(name=name_too_big, version=VERSION, authors=AUTHORS)


class TestBotInfoVersion:
    def test_version_is_trimmed(self):
        assert prefilled_bot.version == VERSION.strip()

    @pytest.mark.parametrize("version", BLANK_STRINGS)
    def test_none_empty_blank_raises_error(self, version):
        with pytest.raises(ValueError):
            BotInfo(name=NAME, version=version, authors=AUTHORS)

    def test_with_maxlength_returns_version(self):
        max_version = VERSION.strip().ljust(bot_info.MAX_VERSION_LENGTH, "x")

        bot = BotInfo(name=NAME, version=max_version, authors=AUTHORS)
        assert bot.version == max_version

    def test_exceeding_maxlength_raises_error(self):
        version_too_big = VERSION.strip().ljust(bot_info.MAX_VERSION_LENGTH + 1, "x")
        with pytest.raises(
            ValueError,
            match=f"'version' length exceeds the maximum of {bot_info.MAX_VERSION_LENGTH} characters",
        ):
            BotInfo(name=NAME, version=version_too_big, authors=AUTHORS)


class TestBotInfoAuthors:
    AUTHOR_TOO_LONG = "Test Author".ljust(bot_info.MAX_AUTHOR_LENGTH + 1, "x")

    def test_authors_is_trimmed(self):
        trimmed = [a.strip() for a in AUTHORS]
        assert prefilled_bot.authors == trimmed

    @pytest.mark.parametrize("authors", [None, ["", None, ""], ["", " ", "\t ", "\n"]])
    def test_none_empty_blanks_raises_error(self, authors):
        with pytest.raises(
            ValueError, match="'authors' cannot be null or empty or contain blanks"
        ):
            BotInfo(name=NAME, version=VERSION, authors=authors)

    def test_single_author_of_maxlength_returns_that_author(self):
        authors = ["Test Author".ljust(bot_info.MAX_AUTHOR_LENGTH, "x")]
        b = BotInfo(name=NAME, version=VERSION, authors=authors)

        assert b.authors == authors

    @pytest.mark.parametrize(
        "authors, rejected",
        [
            pytest.param([AUTHOR_TOO_LONG], [AUTHOR_TOO_LONG], id="Single Author"),
            pytest.param(
                [AUTHOR_TOO_LONG + "1", AUTHOR_TOO_LONG + "2"],
                [AUTHOR_TOO_LONG + "1", AUTHOR_TOO_LONG + "2"],
                id="Multiple Authors",
            ),
            pytest.param(
                [*AUTHORS, AUTHOR_TOO_LONG],
                [AUTHOR_TOO_LONG],
                id="Multiple Authors; 1 Too Long",
            ),
        ],
    )
    def test_author_exceeds_maxlength_raises_error(self, authors, rejected):
        with pytest.raises(
            ValueError,
            match=re.escape(
                f"The following authors exceed the maximum of {bot_info.MAX_AUTHOR_LENGTH} characters. {rejected}"
            ),
        ):
            BotInfo(name=NAME, version=VERSION, authors=authors)

    def test_maximum_number_of_authors_returns_authors(self):
        authors = [f"Test Author {i}" for i in range(bot_info.MAX_NUMBER_OF_AUTHORS)]
        b = BotInfo(name=NAME, version=VERSION, authors=authors)

        assert b.authors == authors

    def test_exceed_maximum_number_of_authors_raises_error(self):
        with pytest.raises(
            ValueError,
            match=re.escape(
                f"Size of 'authors' exceeds the maximum of {bot_info.MAX_NUMBER_OF_AUTHORS}"
            ),
        ):
            BotInfo(
                name=NAME,
                version=VERSION,
                authors=[
                    f"Test Author {i}"
                    for i in range(bot_info.MAX_NUMBER_OF_AUTHORS + 1)
                ],
            )


class TestBotInfoDescription:
    def test_bot_info_description_is_trimmed(self):
        assert prefilled_bot.description == DESCRIPTION.strip()

    @pytest.mark.parametrize("description", BLANK_STRINGS)
    def test_none_empty_blank_description_return_none(self, description):
        bot = BotInfo(
            name=NAME, version=VERSION, authors=AUTHORS, description=description
        )
        assert bot.description is None

    def test_description_with_maxlength_returns_description(self):
        max_description = DESCRIPTION.strip().ljust(
            bot_info.MAX_DESCRIPTION_LENGTH, "x"
        )

        bot = BotInfo(
            name=NAME, version=VERSION, authors=AUTHORS, description=max_description
        )
        assert bot.description == max_description

    def test_description_exceeding_maxlength_raises_error(self):
        description_too_big = DESCRIPTION.strip().ljust(
            bot_info.MAX_DESCRIPTION_LENGTH + 1, "x"
        )
        with pytest.raises(
            ValueError,
            match=f"'description' length exceeds the maximum of {bot_info.MAX_DESCRIPTION_LENGTH} characters",
        ):
            BotInfo(
                name=NAME,
                version=VERSION,
                authors=AUTHORS,
                description=description_too_big,
            )


class TestBotInfoHomepage:
    def test_bot_info_homepage_is_trimmed(self):
        assert prefilled_bot.homepage == HOME_PAGE.strip()

    @pytest.mark.parametrize("homepage", BLANK_STRINGS)
    def test_none_empty_blank_homepage_return_none(self, homepage):
        bot = BotInfo(name=NAME, version=VERSION, authors=AUTHORS, homepage=homepage)
        assert bot.homepage is None

    def test_homepage_with_maxlength_returns_homepage(self):
        max_homepage = HOME_PAGE.strip().ljust(bot_info.MAX_HOMEPAGE_LENGTH, "x")

        bot = BotInfo(
            name=NAME, version=VERSION, authors=AUTHORS, homepage=max_homepage
        )
        assert bot.homepage == max_homepage

    def test_homepage_exceeding_maxlength_raises_error(self):
        homepage_too_big = HOME_PAGE.strip().ljust(
            bot_info.MAX_HOMEPAGE_LENGTH + 1, "x"
        )
        with pytest.raises(
            ValueError,
            match=f"'homepage' length exceeds the maximum of {bot_info.MAX_HOMEPAGE_LENGTH} characters",
        ):
            BotInfo(
                name=NAME, version=VERSION, authors=AUTHORS, homepage=homepage_too_big
            )


class TestBotInfoCountryCodes:
    DEFAULT_COUNTRY_CODES = [bot_info.CntryCodeUtil.get_local_country_code()]

    def test_country_codes_are_trimmed_and_ucased(self):
        trimmed = [a.strip().upper() for a in COUNTRY_CODES]
        assert prefilled_bot.country_codes == trimmed

    @pytest.mark.parametrize(
        "codes", [None, [], ["", None, ""], ["", " ", "\t ", "\n"]]
    )
    def test_none_empty_blanks_returns_default_country_code(self, codes):
        b = BotInfo(name=NAME, version=VERSION, authors=AUTHORS, country_codes=codes)
        assert b.country_codes == self.DEFAULT_COUNTRY_CODES

    def test_init_with_valid_list_of_codes_returns_codes(self):
        codes = ["US", "CA"]
        b = BotInfo(name=NAME, version=VERSION, authors=AUTHORS, country_codes=codes)
        assert b.country_codes == ["US", "CA"]

    @pytest.mark.parametrize("codes", [[" ", "U"], ["USA"], ["xx", "UNITED STATES"]])
    def test_init_with_invalid_list_of_codes_returns_default_country_code(self, codes):
        b = BotInfo(name=NAME, version=VERSION, authors=AUTHORS, country_codes=codes)
        assert b.country_codes == self.DEFAULT_COUNTRY_CODES

    def test_init_with_max_list_of_codes_returns_codes(self):
        codes = ["US" for i in range(bot_info.MAX_NUMBER_OF_COUNTRY_CODES)]
        b = BotInfo(name=NAME, version=VERSION, authors=AUTHORS, country_codes=codes)
        assert b.country_codes == codes

    def test_init_exceed_max_list_of_codes_raises_error(self):
        codes = ["US" for i in range(bot_info.MAX_NUMBER_OF_COUNTRY_CODES + 1)]
        with pytest.raises(
            ValueError,
            match=re.escape(
                f"Size of 'country_codes' exceeds the maximum of {bot_info.MAX_NUMBER_OF_COUNTRY_CODES}"
            ),
        ):
            BotInfo(name=NAME, version=VERSION, authors=AUTHORS, country_codes=codes)


class TestBotInfoGameTypes:
    def test_game_types_are_trimmed(self):
        trimmed = {a.strip() for a in GAME_TYPES}
        assert prefilled_bot.game_types == trimmed

    @pytest.mark.parametrize(
        "game_types", [None, set(), set(["", None, ""]), set(["", " ", "\t ", "\n"])]
    )
    def test_none_empty_blanks_returns_empty_set(self, game_types):
        b = BotInfo(name=NAME, version=VERSION, authors=AUTHORS, game_types=game_types)
        assert b.game_types == set()

    def test_game_types_contains_game_type_with_max_length(self):
        game_types = set(["1v1", "".ljust(bot_info.MAX_GAME_TYPE_LENGTH, "x")])
        b = BotInfo(name=NAME, version=VERSION, authors=AUTHORS, game_types=game_types)
        assert b.game_types == game_types

    def test_game_types_contains_game_type_exceeding_max_length_raises_error(self):
        game_types = set(["1v1", "".ljust(bot_info.MAX_GAME_TYPE_LENGTH + 1, "x")])
        too_long = ["".ljust(bot_info.MAX_GAME_TYPE_LENGTH + 1, "x")]
        with pytest.raises(
            ValueError,
            match=re.escape(
                f"The following 'game_types' exceed the maximum of {bot_info.MAX_GAME_TYPE_LENGTH} characters. {too_long}"
            ),
        ):
            BotInfo(name=NAME, version=VERSION, authors=AUTHORS, game_types=game_types)

    def test_max_number_of_game_types_returns_game_types(self):
        game_types = set([f"gt{i}" for i in range(bot_info.MAX_NUMBER_OF_GAME_TYPES)])
        b = BotInfo(name=NAME, version=VERSION, authors=AUTHORS, game_types=game_types)
        assert b.game_types == game_types

    def test_exceed_max_number_of_game_types_raises_error(self):
        game_types = set(
            [f"gt{i}" for i in range(bot_info.MAX_NUMBER_OF_GAME_TYPES + 1)]
        )
        with pytest.raises(
            ValueError,
            match=re.escape(
                f"Size of 'game_types' exceeds the maximum of {bot_info.MAX_NUMBER_OF_GAME_TYPES}"
            ),
        ):
            BotInfo(name=NAME, version=VERSION, authors=AUTHORS, game_types=game_types)


class TestBotInfoPlatform:
    def test_bot_info_platform_is_trimmed(self):
        assert prefilled_bot.platform == PLATFORM.strip()

    @pytest.mark.parametrize("platform", BLANK_STRINGS)
    def test_none_empty_blank_platform_return_system_platform(self, platform):
        bot = BotInfo(name=NAME, version=VERSION, authors=AUTHORS, platform=platform)
        assert bot.platform == f"PYTHON {python_version()}"

    def test_platform_with_maxlength_returns_platform(self):
        max_platform = PLATFORM.strip().ljust(bot_info.MAX_PLATFORM_LENGTH, "x")

        bot = BotInfo(
            name=NAME, version=VERSION, authors=AUTHORS, platform=max_platform
        )
        assert bot.platform == max_platform

    def test_platform_exceeding_maxlength_raises_error(self):
        platform_too_big = PLATFORM.strip().ljust(bot_info.MAX_PLATFORM_LENGTH + 1, "x")
        with pytest.raises(
            ValueError,
            match=f"'platform' length exceeds the maximum of {bot_info.MAX_PLATFORM_LENGTH} characters",
        ):
            BotInfo(
                name=NAME, version=VERSION, authors=AUTHORS, platform=platform_too_big
            )


class TestBotInfoProgrammingLang:
    def test_bot_info_programming_lang_is_trimmed(self):
        assert prefilled_bot.programming_lang == PROGRAMMING_LANGUAGE.strip()

    @pytest.mark.parametrize("programming_lang", BLANK_STRINGS)
    def test_none_empty_blank_homepage_return_none(self, programming_lang):
        bot = BotInfo(
            name=NAME,
            version=VERSION,
            authors=AUTHORS,
            programming_lang=programming_lang,
        )
        assert bot.programming_lang is None

    def test_programming_lang_with_maxlength_returns_programming_lang(self):
        max_programming_lang = PROGRAMMING_LANGUAGE.strip().ljust(
            bot_info.MAX_PROGRAMMING_LANG_LENGTH, "x"
        )

        bot = BotInfo(
            name=NAME,
            version=VERSION,
            authors=AUTHORS,
            programming_lang=max_programming_lang,
        )
        assert bot.programming_lang == max_programming_lang

    def test_programming_lang_exceeding_maxlength_raises_error(self):
        programming_lang_too_big = PROGRAMMING_LANGUAGE.strip().ljust(
            bot_info.MAX_PROGRAMMING_LANG_LENGTH + 1, "x"
        )
        with pytest.raises(
            ValueError,
            match=f"'programming_lang' length exceeds the maximum of {bot_info.MAX_PROGRAMMING_LANG_LENGTH} characters",
        ):
            BotInfo(
                name=NAME,
                version=VERSION,
                authors=AUTHORS,
                programming_lang=programming_lang_too_big,
            )


class TestBotInfoInitialPosition:
    def test_initial_position_matches(self):
        assert prefilled_bot.initial_position == INITIAL_POSITION

    @pytest.mark.parametrize("initial_position", BLANK_STRINGS)
    def test_none_empty_blank_initial_position_return_none(self, initial_position):
        bot = BotInfo(
            name=NAME,
            version=VERSION,
            authors=AUTHORS,
            initial_position=InitialPosition.from_string(initial_position),
        )
        assert bot.initial_position is None


class TestBotInfoConstructors:
    minimal_bot_dict = {}
    minimal_bot_dict["name"] = NAME.strip()
    minimal_bot_dict["version"] = VERSION.strip()
    minimal_bot_dict["authors"] = ",".join([c.strip() for c in AUTHORS])
    minimal_bot = BotInfo(NAME, VERSION, AUTHORS)
    minimal_bot_str = json.dumps(minimal_bot_dict)

    full_bot_dict = {**minimal_bot_dict}
    full_bot_dict["description"] = DESCRIPTION.strip()
    full_bot_dict["homepage"] = HOME_PAGE.strip()
    full_bot_dict["countryCodes"] = ",".join([c.strip() for c in COUNTRY_CODES])
    full_bot_dict["gameTypes"] = ",".join([c.strip() for c in GAME_TYPES])
    full_bot_dict["platform"] = PLATFORM.strip()
    full_bot_dict["programmingLang"] = PROGRAMMING_LANGUAGE.strip()
    full_bot_dict["initialPosition"] = str(INITIAL_POSITION)
    full_bot_str = json.dumps(full_bot_dict)

    @pytest.mark.parametrize(
        "data, expected",
        [
            pytest.param(minimal_bot_dict, minimal_bot, id="minimal params"),
            pytest.param(full_bot_dict, prefilled_bot, id="all params"),
        ],
    )
    def test_from_data_dict(self, data: dict, expected: BotInfo):
        bot = BotInfo.from_data_dict(data)
        assert bot == expected
 
    @pytest.mark.parametrize(
        "data",
        [
            pytest.param({}, id="empty dictionary"),
            pytest.param({"version":VERSION, "authors": AUTHORS}, id="missing name"),
            pytest.param({"name":NAME, "authors": AUTHORS}, id="missing version"),
            pytest.param({"name":NAME,"version":VERSION}, id="missing authors"),
        ],
    )
    def test_from_data_dict_with_missing_parameters_raises_error(self, data: dict):
        with pytest.raises(ValueError):
            BotInfo.from_data_dict(data)

    @pytest.mark.parametrize(
        "json_str, expected",
        [
            pytest.param(minimal_bot_str, minimal_bot, id="minimal params"),
            pytest.param(full_bot_str, prefilled_bot, id="all params"),
        ],
    )
    def test_from_json(self, json_str: str, expected: BotInfo):
        bot = BotInfo.from_json(json_str)
        assert bot == expected

    def test_from_file_with_valid_file_path(self):
        file_path = "tests/test_data/test_bot.json"
        bot = BotInfo.from_file(file_path)
        assert bot.name == NAME.strip()
        assert bot.version == VERSION.strip()

    def test_from_file_with_invalid_path_raises_error(self):
        file_path = "/tests/test_data/not_found.json"
        with pytest.raises(FileNotFoundError):
            BotInfo.from_file(file_path)

