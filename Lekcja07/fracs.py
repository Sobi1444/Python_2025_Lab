from math import gcd

class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Mianownik rowny zero")
        if isinstance(x, float):
            x, y = x.as_integer_ratio()
        self.x = x
        self.y = y
        self._reduce()

    def _reduce(self):
        g = gcd(self.x, self.y)
        self.x //= g
        self.y //= g
        if self.y < 0:   # przenoszenie minusa
            self.x = -self.x
            self.y = -self.y

    def __str__(self):
        if self.y == 1:
            return str(self.x)
        return f"{self.x}/{self.y}"

    def __repr__(self):
        return f"Frac({self.x}, {self.y})"

    # OPERATORY PORÓWNAŃ
    def _to_frac(self, other):
        if isinstance(other, Frac):
            return other
        if isinstance(other, int):
            return Frac(other, 1)
        if isinstance(other, float):
            return Frac(*other.as_integer_ratio())
        raise ValueError("Nieobslugiwany typ")

    def __eq__(self, other):
        other = self._to_frac(other)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        other = self._to_frac(other)
        return self.x * other.y < other.x * self.y

    def __le__(self, other):
        other = self._to_frac(other)
        return self.x * other.y <= other.x * self.y

    # OPERATORY ARYTMETYCZNE
    def __add__(self, other):
        other = self._to_frac(other)
        return Frac(self.x * other.y + other.x * self.y, self.y * other.y)

    __radd__ = __add__

    def __sub__(self, other):
        other = self._to_frac(other)
        return Frac(self.x * other.y - other.x * self.y, self.y * other.y)

    def __rsub__(self, other):
        other = self._to_frac(other)
        return Frac(other.x * self.y - self.x * other.y, self.y * other.y)

    def __mul__(self, other):
        other = self._to_frac(other)
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self._to_frac(other)
        if other.x == 0:
            raise ValueError("Dzielenie przez zero")
        return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other):
        other = self._to_frac(other)
        if self.x == 0:
            raise ValueError("Dzielenie przez zero")
        return Frac(other.x * self.y, other.y * self.x)

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        if self.x == 0:
            raise ValueError("Odwrotnosc nie istnieje")
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y

    def __hash__(self):
        return hash((self.x, self.y))