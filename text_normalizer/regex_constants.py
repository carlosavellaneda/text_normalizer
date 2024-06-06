HTML_REGEX = r"(?P<tag><[^<>]+>)|(?P<entity>&[a-z0-9]+|#[0-9]{1,10}|#x[0-9a-f]{1,6};)"
PUNCTUATION_REGEX = r"[!\"$&'()*+,-_./:;<=>@[\]^`{|}~?°ª#]"
ESCAPE_REGEX = r"\\n|\\t|\\r|\\a|\\\\n|\\\\t|\\\\r|\\\\a"
NUMBERS_REGEX = r"\d+(?:\s+\d+)*"
