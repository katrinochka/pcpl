from math import sqrt

def solving(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return "Нет действительных корней!"
    elif d == 0:
        root = -b / (2 * a)
        return f"Один корень: {root}"
    else:
        root1 = (-b + sqrt(d)) / (2 * a)
        root2 = (-b - sqrt(d)) / (2 * a)
        return f"Два корня: {root1}, {root2}"

a, b, c = map(float, input("Введите коэффициенты a, b и c через пробел: ").split())
print(solving(a, b, c))
