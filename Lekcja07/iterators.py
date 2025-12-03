import random

# (a) 0, 1, 0, 1, ...
def iterator01():
    while True:
        yield 0
        yield 1

# (b) losowy kierunek
def random_dir():
    dirs = ("N", "E", "S", "W")
    while True:
        yield random.choice(dirs)

# (c) dni tygodnia 0–6 cyklicznie
def week_days():
    while True:
        for i in range(7):
            yield i