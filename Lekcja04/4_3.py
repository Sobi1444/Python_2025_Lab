n = input("Wpisz liczbę której silnia ma być obliczona: ")
n = int(n)
wynik = 1
i = 1
while i <= n:
    wynik *= i
    i += 1
print(wynik)