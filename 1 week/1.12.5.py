# Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три
# строки сначала максимальное, потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.
# Sample Input 1:
# 8
# 2
# 14
# Sample Output 1:
# 14
# 2
# 8
# Sample Input 2:
# 23
# 23
# 21
# Sample Output 2:
# 23
# 21
# 23

a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    max = a
    if b > c:
        min = c
        rest = b
    else:
        min = b
        rest = c
elif b >= a and b >= c:
    max = b
    if a > c:
        min = c
        rest = a
    else:
        min = a
        rest = c
elif c >= a and c >= b:
    max = c
    if a > b:
        min = b
        rest = a
    else:
        min = a
        rest = b
print(max)
print(min)
print(rest)