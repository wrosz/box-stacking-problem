import numpy as np
import matplotlib.pyplot as plt
from measure_time_for_lis import measure_time_for_lis

# Analiza wpływu długości przedziału możliwych wymiarów pudełek na czas wykonywania algorytmu oraz długość odnalezionego podciągu LIS

def main():
    print("Testowanie wydajności LIS w zależności od wymiarów pudełek...")
    upper_bound = [10**i for i in range(3, 13)]
    n_repeats = 60

    avg_times = []
    std_times = []
    all_times = []
    all_b_values = []

    for b1 in upper_bound:
        print(f"Test dla b = 10^{np.log10(b1)}...")
        times_for_b = []
        for i in range(n_repeats):
            try:
                t = measure_time_for_lis(100000, b=b1)[0]
                print(f"   pomiar {i+1}: {t:.3f} s")
                times_for_b.append(t)
                all_b_values.append(b1)
                all_times.append(t)
            except Exception as e:
                print(f"   Błąd przy b={b1}, pomiar {i+1}: {e}")

        if times_for_b:
            avg = np.mean(times_for_b)
            std = np.std(times_for_b)
            avg_times.append(avg)
            std_times.append(std)
        else:
            avg_times.append(None)
            std_times.append(0)

    # ---- Wykres ----
    plt.figure(figsize=(10, 6))

    # Pojedyncze pomiary
    plt.scatter(all_b_values, all_times, color='gray', alpha=0.5, label="Pojedyncze pomiary")

    # Średnie z błędami
    plt.errorbar(upper_bound, avg_times, yerr=std_times, fmt='o-', color='red',
                 ecolor='black', capsize=5, label='Średni czas ± std')

    plt.xscale("log")
    plt.xlabel("b (górne ograniczenie na wymiary pudełek)")
    plt.ylabel("Czas wykonania (s)")
    plt.title("Średni czas LIS i odchylenie standardowe vs zakres wymiarów")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
