import numpy as np
from src.lis import lis
from src.wykres import wykres
from src.validate_input_file import validate_input_file
from src.print_solution import print_solution


def main():

    # walidacja pliku
    while True:
        sciezka_dane = input("Podaj ścieżkę do pliku .txt: ")
        try:
            validate_input_file(sciezka_dane)
            print("Plik został poprawnie odczytany.\n")
        except ValueError as e:
            print(f"Błąd w odczycie pliku: {e}\n")
            continue
        break

    # obliczanie LIS
    print("Trwa obliczanie wyniku...")
    try:
        dane = np.genfromtxt(sciezka_dane, delimiter=',', skip_header=1, dtype=int)
        wynik = lis(dane)
        print(f"Sukces! Długość odnalezionego podciągu wynosi {len(wynik)}.\n")
    except Exception as e:
        print(f"Błąd: {e}")
        input("Wciśnij dowolny klawisz, aby zamknąć program: ")
        quit("Trwa zamykanie programu...")

    # wyświetlanie wyniku w konsoli
    czy_wyswietlic_wynik = input("Czy chcesz wyświetlić elementy podciągu w konsoli? (t/n): ")
    while True:
        if czy_wyswietlic_wynik == "t":
            print("Oto odnaleziony podciąg:")
            print_solution(wynik)
            print("")
        elif czy_wyswietlic_wynik == "n":
            print("Wynik nie został wyświetlony.\n")
        else:
            czy_wyswietlic_wynik = input('Podaj odpowiedź "t" lub "n": ')
            continue
        break

    # zapis wyniku do pliku
    czy_zapisać = input("Czy chcesz zapisać wynik w pliku? (t/n): ")
    while True:
        if czy_zapisać == "t":
            sciezka_wynik = input("Podaj ścieżkę do pliku, w którym chcesz zapisać dane: ")
            while True:
                try:
                    np.savetxt(sciezka_wynik, wynik, fmt='%d', delimiter=',', header=f'{len(wynik)}\nw,l', comments='')
                    print("Plik został poprawnie zapisany.")
                    print("")
                    break
                except Exception as e:
                    print(f"Błąd w zapisie pliku: {e}")
                    sciezka_wynik = input("\nPodaj ścieżkę do pliku, w którym chcesz zapisać dane: ")
        elif czy_zapisać == "n":
            print("Plik nie został zapisany.\n")
        else:
            czy_zapisać = input('Podaj odpowiedź "t" lub "n": ')
            continue
        break

    # wyświetlanie wykresu
    czy_wyswietlic_wykres = input("Czy chcesz wyświetlić wykres? (t/n): ")
    while True:
        if czy_wyswietlic_wykres == "t":
            print("Wykres zostanie wyświetlony w nowym oknie.\n")
            wykres(dane, wynik)
        elif czy_wyswietlic_wykres == "n":
            print("Wynik nie został wyświetlony.\n")
        else:
            czy_wyswietlic_wykres = input('Podaj odpowiedź "t" lub "n": ')
            continue
        break

    input("Koniec programu. Wciśnij dowolny klawisz, aby zakończyć: ")
    quit("Trwa zamykanie programu...")

if __name__ == '__main__':
    main()