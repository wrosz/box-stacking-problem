# czas działania algorytmu LIS w zależności od liczby pudełek

import time
import numpy as np
import matplotlib.pyplot as plt

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logic.lis import lis
from src.logic.generate import generate_boxes_array


def measure_time_for_lis(data):
    start = time.perf_counter()
    _ = lis(data)
    end = time.perf_counter()
    return end - start

def main():
    print("Testowanie wydajności LIS...")

    input_sizes = [1000, 5000] + list(range(10_000, 100_001, 10_000)) + list(range(200_000, 1000_001, 100_000))
    times = []

    for n in input_sizes:
        print(f"Test dla n = {n}...")
        data = generate_boxes_array(n)
        print("Tablica została wygenerowana.")
        try:
            t = measure_time_for_lis(data)
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
