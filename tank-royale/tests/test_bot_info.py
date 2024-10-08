# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from platform import python_version
import pytest
from bot_api import InitialPosition, bot_info, BotInfo


NAME = "  TestBot  "
VERSION = "  1.0  "
AUTHORS = [" Author 1  ", " Author 2 "]
DESCRIPTION = "  short description "
HOME_PAGE = " https://testbot.robocode.dev "
COUNTRY_CODES = [" gb ", "  US "]
GAME_TYPES = [" classic ", " melee ", " 1v1 "]
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
    def test_authors_is_trimmed(self):
        trimmed = [a.strip() for a in AUTHORS]
        assert prefilled_bot.authors == trimmed

    @pytest.mark.parametrize("authors",[
        None, ["",None,""], ["", " ", "\t ", "\n"]
    ])
    def test_none_empty_blanks_raises_error(self, authors):
        with pytest.raises(ValueError):
            BotInfo(name=NAME, version=VERSION, authors=authors)


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
            initial_position=InitialPosition.from_string( initial_position ),
        )
        assert bot.initial_position is None

    