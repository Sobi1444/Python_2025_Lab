n = input("Wpisz dlugosc miarki ")
n = int(n)
print("|...."*n+'|')
for i in range(n+1):
    if len(str(i)) == 1:
        print(i, end='    ')
    else:
        print(i, sep=' ', end='   ')