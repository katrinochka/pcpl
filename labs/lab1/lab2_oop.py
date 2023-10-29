from math import sqrt

class Equa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solving(self):
        d = self.b * self.b - 4 * self.a * self.c
        if d < 0:
            return "Нет действительных корней!"
        elif d == 0:
            root = -self.b / (2 * self.a)
            return f"Один корень: {root}"
        else:
            root1 = (-self.b + sqrt(d)) / (2 * self.a)
            root2 = (-self.b - sqrt(d)) / (2 * self.a)
            return f"Два корня: {root1}, {root2}"

a, b, c = map(float, input("Введите коэффициенты a, b и c через пробел: ").split())
equation = Equa(a, b, c)
print(equation.solving())
