sek1 = [1, 2, 3, 4, 5]
sek2 = [4, 5, 6, 7, 8]

wspolne = list(set(sek1) & set(sek2))

wszystkie_elementy = list(set(sek1) | set(sek2))

print("Wspólne elementy:", wspolne)
print("Wszystkie elementy:", wszystkie_elementy)