import time
import normalizer


def main():
    input_text = [
        r"êstà és üna prùeba",
        r"\n\t\a prueba de saltos de línea    y espacios   ",
        r"prueba 3de numeros 33.32432 23",
        r"&lt; prueba de tags </h1> <p>jaja</p>",
    ]

    # copy the input text 500_000 times
    input_text = input_text * 500_000

    start = time.time()
    # input_text = normalizer.normalize(input_text)
    input_text = normalizer.parallel_normalize(input_text)
    end = time.time() - start
    print(f"Tiempo de ejecución: {end}")
    print(f"El texto final es: {input_text[:7]}")


if __name__ == "__main__":
    main()
