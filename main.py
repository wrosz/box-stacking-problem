import numpy as np
from lis import lis
from wykres import wykres


def main():
    sciezka_dane = input("Podaj nazwę pliku .txt w katalogu ")
    dane = np.genfromtxt(sciezka_dane, delimiter=',', skip_header=1, dtype=int)
    wynik = lis(dane)
    sciezka_wynik = input("Podaj nazwę pliku, w którym chcesz zapisać dane: ")
    np.savetxt(sciezka_wynik, wynik, fmt='%d', delimiter=',', header=f'{len(wynik)}\nw,l', comments='')
    czy_wyswietlic_wykres = input(f"Wynik został zapisany w pliku {sciezka_wynik}.\nCzy chcesz wyświetlić wykres? (t/n):\n")
    if czy_wyswietlic_wykres == 't':
        wykres(dane, wynik)
    print("Koniec programu.")

if __name__ == '__main__':
    main()