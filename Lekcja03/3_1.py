x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

#ten kod jest poprawny, python pozwala na sredniki do oddzielania instrukcji w jednym wierszu

#################################################################################################

for i in "axby": if ord(i) < 100: print (i) #niepoprawne -
# po petli for, if, while, def moze byc maksymalnie jedna instrukcja w tym samym wierszu, tutaj sa dwie

#################################################################################################

for i in "axby": print (ord(i) if ord(i) < 100 else i)

#tutaj dziala, bo jest tylko jedna instrukcja print