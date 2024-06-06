mod regex_constants;
mod transforms;

use pyo3::prelude::*;
use rayon::prelude::*;

fn apply_transformations(input_text: &str) -> String {
    let mut input_text = transforms::to_lower(input_text);
    input_text = transforms::remove_accents(&input_text);
    input_text = transforms::replace_escape_characters(&input_text, None, None);
    input_text = transforms::remove_html(&input_text);
    input_text = transforms::remove_punctuation(&input_text);
    input_text = transforms::replace_numbers(&input_text, None);
    input_text = transforms::remove_blank_spaces(&input_text);

    input_text.to_string()
}

#[pyfunction]
pub fn normalize_rs(_py: Python, vec_text: Vec<String>) -> PyResult<Vec<String>> {
    let normalized_vec: Vec<String> = vec_text
        .iter()
        .map(|text| apply_transformations(text))
        .collect::<Vec<String>>();

    Ok(normalized_vec)
}

#[pyfunction]
pub fn parallel_normalize_rs(_py: Python, vec_text: Vec<String>) -> PyResult<Vec<String>> {
    let normalized_vec: Vec<String> = vec_text
        .par_iter()
        .map(|text| apply_transformations(text))
        .collect::<Vec<String>>();

    Ok(normalized_vec)
}

#[pymodule]
fn text_normalizer(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(normalize_rs, m)?)?;
    m.add_function(wrap_pyfunction!(parallel_normalize_rs, m)?)?;
    Ok(())
}
