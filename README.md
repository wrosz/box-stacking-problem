# Problem Układania Pudełek

**Problem Układania Pudełek** to aplikacja konsolowa, która znajduje najdłuższy możliwy ciąg pudełek, które można zapakować jedno w drugie. Każde pudełko opisane jest parą liczb całkowitych (szerokość, długość). Można je obracać o 90°, a program sam wybiera optymalną orientację.

Rozwiązanie oparte jest na algorytmie programowania dynamicznego o złożoności `O(n log n)`.

---

## Opis działania

Program realizuje następujące kroki:

1. **Standaryzacja pudełek** – wymiary są sortowane tak, aby szerokość ≥ długość.
2. **Usuwanie duplikatów** – identyczne pudełka są eliminowane.
3. **Sortowanie** – według szerokości rosnąco, a długości malejąco.
4. **Znajdowanie najdłuższego rosnącego podciągu (LIS)** – wyznaczany na długościach.

---

## Funkcje programu

- Wczytywanie danych z pliku lub generowanie ich losowo.
- Wyświetlenie wyniku w konsoli.
- Zapis rozwiązania do pliku.
- Wizualizacja danych wejściowych i rozwiązania (matplotlib).
- Obsługa danych do 100 000 pudełek.

---

## Jak uruchomić

### 1. Wersja źródłowa (Python)

Wymagania:
- Python 3.9–3.11
- Biblioteki: `numpy`, `matplotlib`

Instalacja zależności:
```bash
pip install -r requirements.txt
```

Uruchomienie:
```bash
python main.py
```

### 2. Wersja wykonywalna (Windows)

Pobierz plik `main.exe` i uruchom go dwuklikiem lub w terminalu:
```bash
./main.exe
```

Nie wymaga instalacji Pythona.

---

## Format danych

### Dane wejściowe (CSV)
```
w,l
5,1
6,7
6,2
2,3
3,4
```

- Pierwszy wiersz: nagłówek `w,l`
- Kolejne wiersze: wymiary pudełek
- Maksymalnie: 100 000 pudełek
- Maksymalny wymiar: 1 000 000 000

### Wynik (CSV)
```
3
w,l
2,3
3,4
6,7
```

- Wiersz 1: długość najdłuższego ciągu
- Kolejne: posortowane wymiary wybranych pudełek

---

## Wizualizacja

Po zakończeniu obliczeń program zapyta, czy chcesz wyświetlić wykres:

- Wszystkie pudełka jako punkty (w, l)
- Znaleziony ciąg LIS wyróżniony graficznie

---

## Struktura katalogów

```
.
├── main.py               # Główny plik aplikacji konsolowej
├── requirements.txt      # Lista zależności
├── README.md             # Dokumentacja projektu

├── src/                  # Logika aplikacji
│   ├── interface/        # Obsługa wejścia/wyjścia
│   │   ├── display.py
│   │   ├── generate_random_input.py
│   │   ├── load_input.py
│   │   ├── save_output.py
│   │   ├── validate_input_file.py
│   │   └── __init__.py
│   │
│   ├── logic/            # Algorytmy i przetwarzanie
│   │   ├── generate.py
│   │   ├── lis.py
│   │   └── __init__.py
│   │
│   └── plotting/         # Rysowanie wykresu
│       ├── wykres.py
│       └── __init__.py

├── tests/                # Skrypty testowe
│   ├── liczba_pudelek.py
│   ├── liczba_pudelek_bez_binary_search.py
│   ├── measure_time_for_lis.py
│   ├── wymiary_czas_i_dlugosc_LIS.py
│   ├── wymiary_pudelek.py
│   └── __init__.py
```

---

## Licencja

Projekt edukacyjny stworzony w ramach zajęć na studiach. Brak formalnej licencji — możesz używać i modyfikować na własną odpowiedzialność.

