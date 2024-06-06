from time import time
import py_normalize
import text_normalizer

# TODO: think of the implementation of a tokenizer


def _create_data(n: int) -> list[str]:
    input_text = [
        r"êstà és üna prùeba",
        r"\n\t\a prueba de saltos de línea    y espacios   ",
        r"prueba 3de numeros 33.32432 23",
        r"&lt; prueba de tags </h1> <p>jaja</p>",
    ]

    # copy the input text n times
    input_text = input_text * n
    return input_text


def _exec_time(input_text: list[str], function: callable) -> float:
    print(input_text[:10])
    start = time()
    output_text = function(input_list)
    print(output_text[:10])
    return time() - start


def main(input_text: list[str]) -> None:
    py_exec_time = _exec_time(input_text=input_text, function=py_normalize.normalize)
    py_par_exec_time = _exec_time(input_text=input_text, function=py_normalize.parallel_normalize)

    ru_exec_time = _exec_time(input_text=input_text, function=text_normalizer.normalize_rs)
    ru_par_exec_time = _exec_time(input_text=input_text, function=text_normalizer.parallel_normalize_rs)

    print(f"List length: {len(input_text)}")
    print("=" * 50)
    print(f"Python execution time: {py_exec_time}")
    print(f"Python parallel execution time: {py_par_exec_time}")
    print("=" * 50)
    print(f"Rust execution time: {ru_exec_time}")
    print(f"Rust parallel execution time: {ru_par_exec_time}")
    print("=" * 50)
    print(f"Rust is {py_exec_time / ru_exec_time} faster than python")
    print(f"Parallelized rust is {py_par_exec_time / ru_par_exec_time} faster than parallelized python")


if __name__ == "__main__":
    # input_list = _create_data(5_000_000)
    with open("don_quijote.txt", "r") as f:
        input_list = f.read()

    input_list = input_list.splitlines()
    input_list = input_list * 100
    print(len(input_list))
    main(input_list)
