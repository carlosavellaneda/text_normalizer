PUNCTUATION_REGEX = r'[!\"$%\'()*+,_./:;<=>@\[\]^`{|}~?°ª#]'
ESCAPE_REGEX = r"\\n|\\t|\\a|\n|\t|\a"
HTML_REGEX = r"(?P<tag><[^<>]+>)|(?P<entity>&[a-z0-9]+|#[0-9]{1,10}|#x[0-9a-f]{1,6};)"
NUMBER_REGEX = r"\d+(?:\s+\d+)*"
