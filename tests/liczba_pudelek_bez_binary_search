# czas działania algorytmu LIS w zależności od liczby pudełek, ale w przypadku pierwszej, wadliwej wersji (bez zaimplementowania
# binary search w algorytmie lis). Czas działania to O(n^2), i widać to po gorszym dopasowaniu krzywej O(nlogn).

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logic.lis import przetworz_pudelka
from src.logic.generate import generate_boxes_array


def lis_without_bs(pudelka):
    pudelka = przetworz_pudelka(pudelka)  # odpowiednio przetwórz wymiary pudełek
    n = len(pudelka)
    sub = []
    parent = np.full(n, -1)

    # Dodanie pierwszego elementu do sub:
    sub.append(0)
    j0 = 0

    for k in range(1, n):
        x = pudelka[k,1]  # długość k-tego pudełka
        for j in range(len(sub)):
            if pudelka[sub[j], 1] >= x:
                j0 = j
                sub[j0] = k
                break
            if j == len(sub) - 1:
                sub.append(k)
                j0 = j + 1
        if j0 > 0:
            parent[k] = sub[j0 - 1]
    
    lis = []
    k = sub[len(sub) - 1]
    while k != -1:
        lis.append(pudelka[k,:])
        k = parent[k]
    
    lis = np.array(lis)
    return lis[::-1]


def measure_time_for_lis_without_bs(n, a=1, b=10**9, seed=None):
    data = generate_boxes_array(n, a, b, seed)
    print("Tablica została wygenerowana.")
    start = time.perf_counter()
    _ = lis_without_bs(data)
    end = time.perf_counter()
    return end - start


def main():
    print("Testowanie wydajności LIS...")
    input_sizes = [1000, 5000] + list(range(10_000, 100_001, 10_000))
    times = []

    ziarno = 42

    for n in input_sizes:
        print(f"Test dla n = {n}...")
        try:
            t = measure_time_for_lis_without_bs(n, seed=ziarno)
            print(f"   czas: {t:.3f} s")
            times.append(t)
        except Exception as e:
            print(f"   Błąd przy n={n}: {e}")
            times.append(None)

      # ---- Dopasowanie do c * n log n ----
    nlogn = [n * np.log2(n) for n in input_sizes]
    coeff_nlogn = np.polyfit(nlogn, times, deg=1)  # times ≈ c * nlogn + d
    coeff_nsquared = np.polyfit(input_sizes, times, deg=2)
    fitted_times_nlogn = [coeff_nlogn[0] * x + coeff_nlogn[1] for x in nlogn]
    fitted_times_nsquared = [coeff_nsquared[0] * x**2 + coeff_nsquared[1] * x + coeff_nsquared[2] for x in input_sizes]

    print(f"\nDopasowano funkcję: t(n) ≈ {coeff_nlogn[0]:.6e} * n log n + {coeff_nlogn[1]:.6e}\n")

    # ---- Wykres ----
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times, 'o-', label='Zmierzony czas')
    plt.plot(input_sizes, fitted_times_nlogn, 'r--', label=f'Dopasowanie: c·n·log(n)')
    plt.plot(input_sizes, fitted_times_nsquared, 'b--', label=f'Dopasowanie: c·n^2')
    plt.xlabel("n (liczba pudełek)")
    plt.ylabel("Czas wykonania (s)")
    plt.title("Złożoność algorytmu LIS vs. dopasowanie c·n·log(n)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
