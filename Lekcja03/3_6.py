y = input("Podaj wysokosc prostokata: ")
x = input("Podaj dlugosc prostokata: ")
y = int(y)
x = int(x)

i = 0
for i in range(y+1):
    print("+---"*x+"+")
    if i == y:
        break
    print("|   "*x+"|")
