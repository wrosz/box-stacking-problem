import time
import matplotlib.pyplot as plt

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logic.lis import lis
from src.logic.generate import generate_boxes_array


def measure_time_for_lis(n, a=1, b=10**9, seed=None):
    '''Pomiar czasu wykonywania algorytmu LIS na wygenerowanej losowo tablicy wymiarów o zadanych parametrach'''
    data = generate_boxes_array(n, a, b, seed)
    start = time.perf_counter()
    wynik = lis(data)
    end = time.perf_counter()
    return end - start, wynik