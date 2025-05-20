import numpy as np

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

    pudelka = przetworz_pudelka(pudelka)  # odpowiednio przetwórz wymiary pudełek
    n = len(pudelka)
    sub = []
    parent = np.full(n, -1)

    # Dodanie pierwszego elementu do sub:
    sub.append(0)
    j0 = 0

    for k in range(1, n):
        x = pudelka[k,1]  # długość k-tego pudełka
        for j in range(len(sub)):
            if pudelka[sub[j], 1] >= x:
                j0 = j
                sub[j0] = k
                break
            if j == len(sub) - 1:
                sub.append(k)
                j0 = j + 1
        if j0 > 0:
            parent[k] = sub[j0 - 1]
    
    lis = []
    k = sub[len(sub) - 1]
    while k != -1:
        lis.append(pudelka[k,:])
        k = parent[k]
    
    lis = np.array(lis)
    return lis[::-1]