import numpy as np
import matplotlib.pyplot as plt
from measure_time_for_lis import measure_time_for_lis


def main():
    print("Analiza wpływu zakresu b na czas działania i długość LIS")
    upper_bound = [10**i for i in range(3, 10)]
    n_repeats = 10

    avg_times = []
    std_times = []
    avg_lengths = []
    std_lengths = []

    all_times = {}     # b -> lista czasów
    all_lengths = {}   # b -> lista długości

    for b1 in upper_bound:
        print(f"Test dla b = 10^{np.log10(b1)}...")
        times_for_b = []
        lengths_for_b = []

        for i in range(n_repeats):
            try:
                t, wynik = measure_time_for_lis(100_000, b=b1)
                times_for_b.append(t)
                lengths_for_b.append(len(wynik))
                print(f"  pomiar {i+1}: czas={t:.3f}s, długość={len(wynik)}")
            except Exception as e:
                print(f"  Błąd w pomiarze {i+1}: {e}")

        all_times[b1] = times_for_b
        all_lengths[b1] = lengths_for_b

        avg_times.append(np.mean(times_for_b))
        std_times.append(np.std(times_for_b))
        avg_lengths.append(np.mean(lengths_for_b))
        std_lengths.append(np.std(lengths_for_b))

    # ---- Wykresy ----
    fig, axs = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

    # 1. Czas wykonania
    axs[0].errorbar(upper_bound, avg_times, yerr=std_times, fmt='o-', capsize=5, label='Średni czas', color='blue')
    for b, ts in all_times.items():
        axs[0].scatter([b]*len(ts), ts, color='blue', alpha=0.3, label='_pojedyncze czasy')
    axs[0].set_ylabel("Czas wykonania (s)")
    axs[0].set_title("Czas działania LIS vs zakres wymiarów (b)")
    axs[0].grid(True)

    # 2. Długość LIS
    axs[1].errorbar(upper_bound, avg_lengths, yerr=std_lengths, fmt='o-', capsize=5, label='Średnia długość', color='green')
    for b, ls in all_lengths.items():
        axs[1].scatter([b]*len(ls), ls, color='green', alpha=0.3, label='_pojedyncze długości')
    axs[1].set_ylabel("Długość LIS")
    axs[1].set_xlabel("b (górna granica wymiarów)")
    axs[1].set_title("Długość LIS vs zakres wymiarów (b)")
    axs[1].set_xscale("log")
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
