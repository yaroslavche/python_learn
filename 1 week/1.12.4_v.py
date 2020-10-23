f = input()
s = 0
if f == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
elif f == 'круг':
    r = int(input())
    s = 3.14 * (r ** 2)
elif f == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = float(a * b)
print(s)
