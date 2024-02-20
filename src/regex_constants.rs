use lazy_static::lazy_static;
use regex::escape;
use regex::Regex;

lazy_static! {
    pub static ref HTML_REGEX: Regex =
        Regex::new(r#"(?P<tag><[^<>]+>)|(?P<entity>&[a-z0-9]+|#[0-9]{1,10}|#x[0-9a-f]{1,6};)"#)
            .unwrap();
    pub static ref PUNCTUATION_REGEX: Regex =
        Regex::new(format!(r#"[{}]"#, escape(r#"!"$&'()*+,-_./:;<=>@[\]^`{|}~?°ª#"#),).as_str())
            .unwrap();
}
