use crate::transforms;
use rayon::prelude::*;

fn apply_transformations(input_text: &mut str) -> String {
    let mut input_text = transforms::to_lower(&input_text);
    input_text = transforms::remove_accents(&input_text);
    input_text = transforms::replace_escape_characters(&input_text, None, None);
    input_text = transforms::remove_html(&input_text);
    input_text = transforms::remove_punctuation(&input_text);
    input_text = transforms::replace_numbers(&input_text, None);
    input_text = transforms::remove_blank_spaces(&input_text);

    input_text.to_string()
}

pub fn normalize(vec_text: &mut Vec<String>) -> Vec<String> {
    vec_text
        .iter_mut()
        .map(|text| apply_transformations(text))
        .collect::<Vec<String>>()
}

pub fn parallel_normalize(vec_text: &mut Vec<String>) -> Vec<String> {
    vec_text
        .par_iter_mut()
        .map(|text| apply_transformations(text))
        .collect::<Vec<String>>()
}
