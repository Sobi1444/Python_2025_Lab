def miarka(n):
    linia = "|...."*n+"|\n"
    liczby = ""
    for i in range(n+1):
        liczby += str(i)
        if len(str(i)) == 1:
            liczby += "    "
        else:
            liczby += '   '
    return linia+liczby
print(miarka(20))
print('\n')
def prostokat(y,x):
    wynik = ""
    y = int(y)
    x = int(x)
    for i in range(y+1):
        wynik += "+---"*x+"+\n"
        if i == y:
            break
        wynik += "|   "*x+"|\n"
    return wynik
print(prostokat(4,4))