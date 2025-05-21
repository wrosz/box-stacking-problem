import numpy as np

def binary_search_left(arr, x):
    '''Zwraca najmniejszy indeks i, dla którego arr[i] >= x.
    Jeśli taki nie istnieje, zwraca len(arr) (miejsce do wstawienia na koniec).'''
    left, right = 0, len(arr) - 1
    pos = len(arr)  # domyślnie wstaw na koniec
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            pos = mid
            right = mid - 1
        else:
            left = mid + 1
    return pos


def przetworz_pudelka(pudelka):
    '''Przetwarza listę wymiarów pudełek, tak aby pierwsza współrzędna (szerokość) była nie mniejsza od drugiej (długość).
    Następnie sortuje wymiary pudełek według szerokości rosnąco, a w przypadku równej szerokości - według długości malejąco.
    Jeśli niektóre pary współrzędnych się powtarzają, to duplikaty usuwamy.
    
    Dane wejściowe:
    pudelka - tablica par liczb całkowitych o długości nieprzekraczającej 100 000'''

    # Zamień szerokość i długość, jeśli szerokość < długość
    maska = pudelka[:, 0] < pudelka[:, 1]
    pudelka[maska] = pudelka[maska][:, ::-1]  # zamiana kolumn

    # Usuń duplikaty
    pudelka = np.unique(pudelka, axis=0)

    # Posortuj według:
    # - szerokości rosnąco (kolumna 0)
    # - długości malejąco (kolumna 1) ⇒ dlatego używamy -kolumna 1
    indeksy_sortowania = np.lexsort((-pudelka[:, 1], pudelka[:, 0]))
    pudelka_posortowane = pudelka[indeksy_sortowania]

    return pudelka_posortowane

def lis(pudelka):
    '''Zwraca najdłuższy podciąg pudełek, które można zapakować jedno w drugie.
    Dane wejściowe:
    pudelka - tablica par liczb całkowitych o długości nieprzekraczającej 100 000'''

    pudelka = przetworz_pudelka(pudelka)
    n = len(pudelka)
    
    sub = []      # lista wartości długości pudełek
    sub_idx = []  # indeksy pudełek w pudelka (dla odtworzenia ścieżki)
    parent = np.full(n, -1)

    for i in range(n):
        x = pudelka[i, 1]
        pos = binary_search_left(sub, x)
        if pos == len(sub):
            sub.append(x)
            sub_idx.append(i)
        else:
            sub[pos] = x
            sub_idx[pos] = i
        if pos > 0:
            parent[i] = sub_idx[pos - 1]

    # Odtworzenie LIS
    lis_seq = []
    k = sub_idx[-1]
    while k != -1:
        lis_seq.append(pudelka[k])
        k = parent[k]
    lis_seq.reverse()
    return np.array(lis_seq)