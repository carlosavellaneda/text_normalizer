use crate::regex_constants;
use unidecode::unidecode;

pub fn to_lower(text: &str) -> String {
    text.to_lowercase()
}

pub fn remove_accents(text: &str) -> String {
    unidecode(text)
}

pub fn remove_punctuation(text: &str) -> String {
    regex_constants::PUNCTUATION_REGEX
        .replace_all(text, " ")
        .to_string()
}

pub fn remove_blank_spaces(text: &str) -> String {
    text.split_whitespace().collect::<Vec<&str>>().join(" ")
}

pub fn remove_html(text: &str) -> String {
    regex_constants::HTML_REGEX
        .replace_all(text, " ")
        .to_string()
}
