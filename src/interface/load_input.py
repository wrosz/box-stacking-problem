import numpy as np

MAX_BOXES = 100_000
MAX_DIMENSION = 10**9

def validate_input_file(path):
    '''Sprawdza, czy ścieżka do pliku istnieje i czy ma format zgodny z wymaganiami zapisanymi w dokumentacj:
    - pierwszy wiersz to nagłówek w,l;
    - długość i szerokość pudełka nie większe niż 10^9;
    - maksymalnie 100 000 pudełek.'''

    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        raise ValueError(f"Nie znaleziono pliku: {path}")
    except Exception as e:
        raise ValueError(f"Nie można otworzyć pliku: {e}")

    if not lines:
        raise ValueError("Plik jest pusty.")

    if lines[0] != "w,l":
        raise ValueError("Nagłówek musi mieć postać dokładnie: w,l")

    data_lines = lines[1:]
    if len(data_lines) > MAX_BOXES:
        raise ValueError(f"Zbyt dużo pudełek: {len(data_lines)} (maksymalnie {MAX_BOXES})")

    for i, line in enumerate(data_lines, start=2):
        parts = line.split(',')
        if len(parts) != 2:
            raise ValueError(f"Błąd w linii {i}: oczekiwano dwóch wartości oddzielonych przecinkiem")
        try:
            w, l = map(int, parts)
        except ValueError:
            raise ValueError(f"Błąd w linii {i}: wartości muszą być liczbami całkowitymi")

        if not (1 <= w <= MAX_DIMENSION and 1 <= l <= MAX_DIMENSION):
            raise ValueError(f"Błąd w linii {i}: wymiary muszą być w zakresie 1..{MAX_DIMENSION}")

    return True


def load_input_from_file():
    while True:
        path = input("Podaj ścieżkę do pliku .txt: ")
        try:
            validate_input_file(path)
            print("Plik został poprawnie odczytany.\n")
            return path
        except ValueError as e:
            print(f"Błąd w odczycie pliku: {e}\n")

def load_data(path):
    return np.genfromtxt(path, delimiter=',', skip_header=1, dtype=int)
