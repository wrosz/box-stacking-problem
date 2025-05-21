import numpy as np

def ask_choice(prompt, options):
    choice = input(prompt).lower()
    while choice not in options:
        choice = input(f'Podaj jedną z opcji {list(options)}: ').lower()
    return choice


def print_solution(arr):
    # Oblicz szerokość kolumn na podstawie maksymalnej długości liczby
    w_col = max(len(str(int(np.max(arr[:, 0])))), 1)
    l_col = max(len(str(int(np.max(arr[:, 1])))), 1)

    print(f"{'w':<{w_col}} {'l':<{l_col}}")
    print(f"{'-'*w_col} {'-'*l_col}")

    for row in arr:
        print(f"{int(row[0]):<{w_col}} {int(row[1]):<{l_col}}")
