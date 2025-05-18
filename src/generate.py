import numpy as np
import warnings

def generate_boxes_array(n, a=1, b=10**9, seed=None):
    '''Generuje losową tablicę zawierającą n pudełek, o wymiarach w przedziale [a, b]'''
    if seed is not None:
        np.random.seed(seed)
    
    assert a > 0, "a musi być dodatnie"
    assert b > 0, "b musi być dodatnie"

    if a > 10 ** 9 or b > 10 ** 9:
        raise Warning("Maksymalne wymiary przekraczają rozmiar 10^9")
    if n > 10 ** 5:
        raise Warning("Liczba pudełek przekracza 100 000")

    return np.random.randint(a, b + 1, size=(n, 2), dtype=np.int64)


def generate_file(path, n, a, b, seed):
    arr = generate_boxes_array(n, a, b, seed)
    np.savetxt(path, arr, fmt='%d', delimiter=',', header=f'{len(arr)}\nw,l', comments='')
    return True

