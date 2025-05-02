import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def wykres(data, data1):
    '''Generuje wykres scatterplot z punktami znajdującymi się w tablicach data, data1.
    Punkty z tablicy data są zaznaczone na czarno i mają mniejszy rozmiar, natomiast punkty z tablicy data1
    są wyróżnione i mają kolor czerwony.'''

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
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True, prune='both'))
    plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True, prune='both'))

    # Dodanie legendy
    plt.legend()
    plt.grid()

    # Wyświetlenie wykresu
    plt.show()