from src.logic.generate import generate_file

def get_valid_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                raise ValueError
            return val
        except ValueError:
            if min_val is not None and max_val is not None:
                print(f"Podaj liczbę całkowitą z zakresu [{min_val}, {max_val}]")
            elif min_val is not None:
                print(f"Podaj liczbę całkowitą większą lub równą {min_val}")
            elif max_val is not None:
                print(f"Podaj liczbę całkowitą mniejszą lub równą {max_val}")
            else:
                print("To nie jest poprawna liczba.")

def generate_random_input_interactive():
    print("\n--- Generowanie losowego pliku ---")

    n = get_valid_int("Podaj liczbę pudełek (2 <= n <= 100000): ", 2, 100000)
    a = get_valid_int("Podaj minimalny wymiar pudełka (1 <= a <= 10^9): ", 1, 10**9)
    b = get_valid_int(f"Podaj maksymalny wymiar pudełka (a <= b <= 10^9): ", a, 10**9)
    seed = get_valid_int("Podaj seed (liczba całkowita, np. 42): ")

    output_path = input("Podaj ścieżkę lub nazwę pliku .txt, który chcesz zapisać: ").strip()

    try:
        generate_file(output_path, n, a, b, seed)
        print(f"Plik został wygenerowany i zapisany jako: {output_path}\n")
        return output_path
    except Exception as e:
        print(f"Błąd przy generowaniu pliku: {e}")
        return None
