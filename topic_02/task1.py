import math
def find_descriminant(a, b, c):
    return b**2 - 4*a*c
def find_roots(a, b, c):
    d = find_descriminant(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return f"Дискрімінант: {d}. Два корені x1 = {x1}, x2 = {x2}"
    elif d == 0:
         x = -b / (2*a)
         return f"Дискрімінант: {d}. Один корінь x1 = {x}."
    else:
        return f"Коренів немає"

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

res = find_roots(a, b, c)

print("Результат:", res)