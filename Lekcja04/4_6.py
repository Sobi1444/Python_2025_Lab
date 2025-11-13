seq = [(1,2), (3,6), [2,3,4], 2, 3, 5, 7]
print(seq)
def sum_seq(sequence):
    wynik = 0
    for k in sequence:
        if isinstance(k, (list, tuple)): # dzieki nawiasowi isinstance sprawdza czy obiekt k jest instancja danego typu tutaj obiekt listy lub krotki
            wynik += sum_seq(k)
        else:
            wynik += k
    return wynik
print(sum_seq(seq))
