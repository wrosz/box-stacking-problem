# czas działania algorytmu LIS w zależności od liczby pudełek

import time
import numpy as np
import matplotlib.pyplot as plt

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logic.lis import lis
from src.logic.generate import generate_boxes_array

def measure_time_for_lis(n, a=1, b=10**9, seed=None):
    data = generate_boxes_array(n, a, b, seed)
    start = time.perf_counter()
    _ = lis(data)
    end = time.perf_counter()
    return end - start

def main():
    print("Testowanie wydajności LIS...")

    input_sizes = [1000, 5000] + list(range(10_000, 100_001, 10_000))
    times = []

    for n in input_sizes:
        print(f"Test dla n = {n}...")
        try:
            t = measure_time_for_lis(n)
            print(f"   czas: {t:.3f} s")
            times.append(t)
        except Exception as e:
            print(f"   Błąd przy n={n}: {e}")
            times.append(None)


      # ---- Dopasowanie do c * n log n ----
    nlogn = [n * np.log2(n) for n in input_sizes]
    coeff = np.polyfit(nlogn, times, deg=1)  # times ≈ c * nlogn + d
    fitted_times = [coeff[0] * x + coeff[1] for x in nlogn]

    print(f"\nDopasowano funkcję: t(n) ≈ {coeff[0]:.6e} * n log n + {coeff[1]:.6e}\n")

    # ---- Wykres ----
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times, 'o-', label='Zmierzony czas')
    plt.plot(input_sizes, fitted_times, 'r--', label=f'Dopasowanie: c·n·log(n)')
    plt.xlabel("n (liczba pudełek)")
    plt.ylabel("Czas wykonania (s)")
    plt.title("Złożoność algorytmu LIS vs. dopasowanie c·n·log(n)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
