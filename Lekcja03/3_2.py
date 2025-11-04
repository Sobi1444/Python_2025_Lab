L = [3, 5, 4] ; L = L.sort()
#L.sort() sortuje liste i nic nie zwraca, wiec L zmienia sie w pusta liste
############################################################################
x, y = 1, 2, 3 #python nie wie do czego przypisac wartosc 3

X = 1, 2, 3 ; X[1] = 4 #python stworzyl tutaj krotke, a ona jest niemodyfikowalna, wiec nie mozna przypisac nowej wartosci

############################################################################
X = [1, 2, 3] ; X[3] = 4 #ostatnim indeksem w tej tablicy jest 2

X = "abc" ; X.append("d") #dla zmiennej string nie ma funkcji append


L = list(map(pow, range(8))) #pow wymaga dwoch argumentow
print(L)