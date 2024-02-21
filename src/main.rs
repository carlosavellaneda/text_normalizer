use std::time::Instant;

use text_normalizer::normalizer;

fn main() {
    let mut input_text = vec![
        r#"êstà és üná prùeba"#.to_string(),
        r#"\n\t\a prueba de saltos de línea    y espacios   "#.to_string(),
        r#"prueba 3de numeros 33.32432 23"#.to_string(),
        r#"&lt; prueba de tags </h1> <p>jaja</p>"#.to_string(),
    ];
    println!("El texto inicial es: {:?}", &input_text);

    // copy the input text 500_000 times
    input_text = input_text
        .iter()
        .cycle()
        .take(input_text.len() * 500_000)
        .cloned()
        .collect();

    let start = Instant::now();
    // input_text = normalizer::normalize(&mut input_text);
    input_text = normalizer::parallel_normalize(&mut input_text);
    println!("Tiempo de ejecución: {:?}", start.elapsed().as_secs_f32());
    println!("El texto final es: {:?}", &input_text[0..7]);
}
