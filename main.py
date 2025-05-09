import numpy as np
from src.lis import lis
from src.wykres import wykres


def main():
    sciezka_dane = input("Podaj ścieżkę do pliku .txt: ")
    dane = np.genfromtxt(sciezka_dane, delimiter=',', skip_header=1, dtype=int)
    wynik = lis(dane)
    sciezka_wynik = input("Podaj ścieżkę do pliku, w którym chcesz zapisać dane: ")
    np.savetxt(sciezka_wynik, wynik, fmt='%d', delimiter=',', header=f'{len(wynik)}\nw,l', comments='')
    czy_wyswietlic_wykres = input(f"Wynik został zapisany w pliku {sciezka_wynik}.\nCzy chcesz wyświetlić wykres? (t/n): ")
    if czy_wyswietlic_wykres == 't':
        wykres(dane, wynik)
    print("Koniec programu.")

if __name__ == '__main__':
    main()