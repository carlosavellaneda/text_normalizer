import re
from regex_constants import (
    HTML_REGEX,
    NUMBERS_REGEX,
    ESCAPE_REGEX,
    PUNCTUATION_REGEX,
)
from unidecode import unidecode


def to_lower(text: str) -> str:
    return text.lower()


def remove_accents(text: str) -> str:
    return unidecode(text)


def remove_punctuation(text: str) -> str:
    return re.sub(PUNCTUATION_REGEX, " ", text)


def remove_blank_spaces(text: str) -> str:
    return " ".join(text.split())


def remove_html(text: str) -> str:
    return re.sub(HTML_REGEX, " ", text)


def replace_escape_characters(
    text: str,
    regex: str | None = ESCAPE_REGEX,
    replacement: str | None = " "
) -> str:
    return re.sub(regex, replacement, text)


def replace_numbers(text: str, replacement: str | None = " %number% ") -> str:
    return re.sub(NUMBERS_REGEX, replacement, text)
