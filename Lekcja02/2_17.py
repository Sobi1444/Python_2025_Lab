line = "Klmnn Efghhhh Abcd"
x = sorted(line.split())
alfabetycznie = " ".join(x)
print(alfabetycznie)

y = sorted(line.split())
#print(y)
#print(len(y))
#print(range(len(y)-2))
for i in range(len(y) - 1):
    for w in range(len(y) - 1):
        if len(y[w]) > len(y[w + 1]):
            temp = y[w]
            y[w] = y[w + 1]
            y[w + 1] = temp
#print(y)
rosnaco = " ".join(y)
print(rosnaco)