use text_normalizer::transforms;

fn main() {
    let mut input_text = r#"\nEsta es una prueba para ver si las transformaciones   quitan caracteres especiales como Angélica o você"#.to_string();

    input_text = transforms::to_lower(&input_text);
    input_text = transforms::remove_accents(&input_text);
    input_text = transforms::remove_punctuation(&input_text);
    input_text = transforms::remove_blank_spaces(&input_text);

    println!("El texto final es: {}", input_text);
}
