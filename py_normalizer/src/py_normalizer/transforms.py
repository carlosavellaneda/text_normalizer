import re
from unidecode import unidecode
import regex_constants


def to_lower(text: str) -> str:
    return text.lower()


def remove_accents(text: str) -> str:
    return unidecode(text)


def remove_punctuation(text: str) -> str:
    return re.sub(pattern=regex_constants.PUNCTUATION_REGEX, repl=" ", string=text)


def remove_blank_spaces(text: str) -> str:
    return " ".join(text.split())


def remove_html(text: str) -> str:
    return re.sub(pattern=regex_constants.HTML_REGEX, repl=" ", string=text)


def replace_escape_characters(
    text: str,
    regex: str | None = None,
    replacement: str | None = None
) -> str:
    if regex is None:
        regex = regex_constants.ESCAPE_REGEX

    if replacement is None:
        replacement = " "

    return re.sub(pattern=regex, repl=replacement, string=text)


def replace_numbers(text: str, replacement: str | None = None) -> str:
    if replacement is None:
        replacement = " %number% "

    return re.sub(pattern=regex_constants.NUMBER_REGEX, repl=replacement, string=text)
