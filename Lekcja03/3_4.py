while True:
    x = input("Wpisz liczbe lub 'stop' zeby zakonczyc dzialanie programu ")
    if x.lower() == "stop":
        break
    try:
        x = float(x)
    except ValueError:
        print("To nie jest liczba")
        continue
    print(x, x**3)