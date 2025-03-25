import matplotlib.pyplot as plt
import numpy as np


def main():
# na razie tylko przykładowy wykres

    data = [(3, 2), (4, 3), (5, 1), (6, 2), (7, 6)]
    data1 = [(5, 1), (6, 2), (7, 6)]

    # Rozpakowanie współrzędnych
    x, y = zip(*data)
    x1, y1 = zip(*data1)

    # Tworzenie scatterplota
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='black', s=30, label='Wszystkie punkty')  # Czarny, mniejsze
    plt.scatter(x1, y1, color='red', s=60, label='Punkty LIS')  # Czerwony, większe

    # Oznaczenia osi i tytuł
    plt.xlabel("szerokość pudełek")
    plt.ylabel("długość pudełek")
    plt.title("Posortowane wymiary pudełek z wyróżnionym ciągiem LIS")

    # Ustawienie zakresu osi oraz liczbowych oznaczeń tylko dla liczb całkowitych
    plt.xticks(np.arange(min(x) - 1, max(x) + 2, 1))
    plt.yticks(np.arange(min(y) - 1, max(y) + 2, 1))

    # Dodanie legendy
    plt.legend()
    plt.grid()

    # Wyświetlenie wykresu
    plt.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()