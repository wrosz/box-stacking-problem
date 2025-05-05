# Problem Układania Pudełek

**Problem Układania Pudełek** to program, który znajduje najdłuższy możliwy ciąg pudełek, które można zapakować jedno w drugie. Każde kolejne pudełko w ciągu musi mieć **ściśle większą długość i szerokość** niż poprzednie. Dozwolone jest **obracanie pudełek o 90 stopni**, co oznacza, że program może traktować długość jako szerokość i odwrotnie, wybierając optymalną orientację.

## Wymagania

* System Windows (plik wykonywalny: `main.exe`)
* Python 3.9–3.11 do pracy z kodem źródłowym (jeśli nie korzystasz z `.exe`)
* Plik wejściowy `.txt` w odpowiednim formacie

## Jak uruchomić

1. Przejdź do folderu `dist`.
2. Uruchom plik `main.exe`.
3. Program poprosi o:

   * Ścieżkę do pliku wejściowego (`.txt`)
   * Ścieżkę do pliku wyjściowego (`.txt`)
   * Informację, czy chcesz wygenerować wykres ilustrujący rozwiązanie
4. Dla przetestowania działania programu możesz użyć gotowych danych z folderu `example_data/`:

   * `example.txt` – zawiera 5 pudełek
   * `example2.txt` – zawiera 1000 pudełek

## Format pliku wejściowego

Plik tekstowy musi mieć strukturę CSV z nagłówkiem `w,l`:

```
w,l
5,1
6,7
6,2
2,3
3,4
```

* Pierwszy wiersz to nagłówek: `w,l` (szerokość, długość)
* Kolejne wiersze to wymiary pudełek (liczby całkowite)
* Maksymalnie 100 000 pudełek
* Maksymalne wartości wymiarów: 10⁹
* Program automatycznie wybiera najlepszą orientację każdego pudełka (obrót o 90°)

## Format pliku wyjściowego

Wynikowy plik `.txt` ma następujący format:

```
3
w,l
5,1
6,2
7,6
```

* Pierwszy wiersz: długość najdłuższego ciągu pudełek
* Kolejne wiersze: wymiary wybranych pudełek w formacie `w,l`

## Wizualizacja

Po zakończeniu obliczeń program zapyta, czy chcesz wygenerować wykres punktowy:

* Wszystkie pudełka zostaną przedstawione jako punkty (`w`, `l`) na płaszczyźnie
* Znaleziony ciąg zostanie wyróżniony graficznie

## Algorytm

Program wykorzystuje zmodyfikowany algorytm najdłuższego rosnącego podciągu (LIS), po wcześniejszym posortowaniu pudełek. Dopuszczalność obrotu zwiększa przestrzeń możliwych rozwiązań i umożliwia znalezienie dłuższych ciągów.

## Struktura kodu

```
main.py                 # Obsługa interakcji z użytkownikiem (uruchamianie programu)
main.spec               # Konfiguracja PyInstaller
README.md               # Dokumentacja projektu
requirements.txt        # Lista zależności

dist/
└── main.exe            # Wersja wykonywalna programu

src/
├── lis.py              # Algorytm LIS (najdłuższy rosnący podciąg pudełek)
├── wykres.py           # Generowanie wykresu (matplotlib)
└── __init__.py         # Plik inicjalizujący moduł

example_data/
├── example.txt         # Przykładowy plik wejściowy (5 pudełek)
└── example2.txt        # Przykładowy plik testowy (1000 pudełek)

build/                  # Pliki techniczne tworzone przez PyInstaller
__pycache__/            # Pliki cache Pythona
.venv/                  # Środowisko wirtualne (lokalne)
```

## Plany rozwoju

Projekt znajduje się w fazie **beta**. W planach:

* Dodanie walidacji danych wejściowych i obsługi błędów
* Analiza wydajności algorytmu na dużych danych (benchmarki)
* Zautomatyzowane testy jednostkowe i integracyjne
* Generator losowych plików wejściowych
* Ulepszona, bardziej intuicyjna interakcja z użytkownikiem

## Licencja

Projekt edukacyjny. Brak formalnej licencji – używaj i modyfikuj na własną odpowiedzialność.