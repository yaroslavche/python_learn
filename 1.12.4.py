# Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и
# круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры
# комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
# Для числа π в стране Малевии используют значение 3.14.
# Формат ввода, который используют Малевийцы:
# треугольник
# a
# b
# c
# где a, b и c — длины сторон треугольника
# прямоугольник
# a
# b
# где a и b — длины сторон прямоугольника
# круг
# r
# где r — радиус окружности
# Sample Input 1:
# прямоугольник
# 4
# 10
# Sample Output 1:
# 40.0
# Sample Input 2:
# круг
# 5
# Sample Output 2:
# 78.5
# Sample Input 3:
# треугольник
# 3
# 4
# 5    eleven = int(n / 20) % 5 == 0

# Sample Output 3:
# 6.0

shape = input()
if shape == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif shape == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(float(a * b))
elif shape == 'круг':
    r = int(input())
    print(3.14 * (r ** 2))
