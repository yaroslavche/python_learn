# Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать.
# Далее считывает n строк с числами Xi, по одному числу в каждой строке. Итого будет n+1 строк.
# При считывании числа Xi программа должна на отдельной строке вывести значение f(Xi). Функция f(x) уже реализована и
# доступна для вызова.
# Функция вычисляется достаточно долго и зависит только от переданного аргумента x. Для того, чтобы уложиться в
# ограничение по времени, нужно избежать повторного вычисления значений.
# Sample Input:
# 5
# 5
# 12
# 9
# 20
# 12
# Sample Output:
# 11
# 41
# 47
# 61
# 41

n = int(input())
s = {}
for i in range(n):
    x = int(input())
    if x not in s:
        s[x] = f(x)
    print(s[x])


