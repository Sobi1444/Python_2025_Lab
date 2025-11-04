roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def rzymska_na_arabska(liczba_rzymska):
    suma = 0
    poprzednia = 0

    for znak in reversed(liczba_rzymska):
        wartosc = roman[znak]
        if wartosc < poprzednia:
            suma -= wartosc
        else:
            suma += wartosc
        poprzednia = wartosc

    return suma


print(rzymska_na_arabska("III"))     # 3
print(rzymska_na_arabska("IV"))      # 4
print(rzymska_na_arabska("IX"))      # 9
print(rzymska_na_arabska("LVIII"))   # 58
print(rzymska_na_arabska("MCMXCIV")) #1994