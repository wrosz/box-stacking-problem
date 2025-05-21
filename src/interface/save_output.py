import numpy as np

def save_output(path, data):
    try:
        np.savetxt(path, data, fmt='%d', delimiter=',', header=f'{len(data)}\nw,l', comments='')
        print("Plik został poprawnie zapisany.\n")
    except Exception as e:
        raise RuntimeError(f"Błąd w zapisie pliku: {e}")
