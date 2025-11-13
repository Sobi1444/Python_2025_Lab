n = input("Podaj ktory wyraz ciagu Fibonacciego ma byc obliczony ")
n = int(n)
i,a,b = 1,1,1
#f(0) = 0 f(1) = 1 f(2) = 1 f(3) = 2 f(4) = 3 f(5) = 5
if n == 0 or n == 1:
    print(n)
else:
    while i < n:
        fib = b
        b = a+b
        a = fib
        i += 1
    print(fib)
