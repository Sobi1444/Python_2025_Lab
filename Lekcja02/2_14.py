line = "Abcddddd Efghhhhhhhhh Ijklmmm"
current = 0
for word in line.split():
    if current < len(word):
        current = len(word)
        slowo = word
print("Najdluzszy wyraz to " + slowo)
print("Dlugosc najdluzszego wyrazu to",current)


