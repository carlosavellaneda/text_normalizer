# Text Normalizer

This repo aims to create a simple benchmark for text normalizing between Rust and Python. I implemented some simple functions to normalize a list of texts, covering the following functionalities:

- [X] Replace the strings to lowercase.
- [X] Replace accents and special characters into a 
- [X] Replace a unicode string and replaces it to represent it in ASCII characters. E.g. `á` will be transformed into `a`.
- [X] Remove punctuation.
- [X] Replace multiple white spaces with a single one.
- [X] Remove HTML tags.
- [X] Replace special escape characters into a white space.
- [X] Replace numbers into a specified replacement string. By default, all numbers will be replaced into the string `%number%`.
