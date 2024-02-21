import transforms
from multiprocessing import Pool


def apply_transformations(input_text: str) -> str:
    input_text = transforms.to_lower(input_text)
    input_text = transforms.remove_accents(input_text)
    input_text = transforms.replace_escape_characters(input_text)
    input_text = transforms.remove_html(input_text)
    input_text = transforms.remove_punctuation(input_text)
    input_text = transforms.replace_numbers(input_text)
    input_text = transforms.remove_blank_spaces(input_text)
    return input_text


def normalize(vec_text: list[str]) -> list[str]:
    return [apply_transformations(text) for text in vec_text]


def parallel_normalize(vec_text: list[str]) -> list[str]:
    with Pool() as pool:
        normalized_texts = pool.map(apply_transformations, vec_text)

    return normalized_texts
