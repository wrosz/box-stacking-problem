from io.load_input import load_input_from_file, load_data
from io.save_output import save_output
from io.display import ask_choice, print_solution
from io.generate_random_input import generate_random_input_interactive
from logic.lis import lis
from plotting.wykres import wykres

def main():
    print("Witaj! Co chcesz zrobić?")
    opcja = ask_choice("1. Wczytaj plik wejściowy\n2. Wygeneruj losowy plik wejściowy\nTwój wybór (1/2): ", ["1", "2"])

    if opcja == "1":
        sciezka_dane = load_input_from_file()
    elif opcja == "2":
        sciezka_dane = generate_random_input_interactive()
        if not sciezka_dane:
            input("Wystąpił błąd. Naciśnij dowolny klawisz, aby zakończyć.")
            return

    print("Trwa obliczanie wyniku...")
    try:
        dane = load_data(sciezka_dane)
        wynik = lis(dane)
        print(f"Sukces! Długość podciągu: {len(wynik)}\n")
    except Exception as e:
        print(f"Błąd: {e}")
        input("Wciśnij dowolny klawisz, aby zamknąć program: ")
        return

    if ask_choice("Wyświetlić podciąg w konsoli? (t/n): ", ["t", "n"]) == "t":
        print_solution(wynik)
        print("")

    if ask_choice("Zapisać wynik do pliku? (t/n): ", ["t", "n"]) == "t":
        while True:
            sciezka_wynik = input("Podaj ścieżkę do pliku: ")
            try:
                save_output(sciezka_wynik, wynik)
                break
            except Exception as e:
                print(e)

    if ask_choice("Wyświetlić wykres? (t/n): ", ["t", "n"]) == "t":
        wykres(dane, wynik)
        print("")

    input("Koniec programu. Wciśnij dowolny klawisz, aby zakończyć.")

if __name__ == '__main__':
    main()
