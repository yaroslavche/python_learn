# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные
# значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного
# списка, например:
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# Функция не должна осуществлять ввод/вывод информации.

def modify_list(l):
    new = []
    for n in l:
        if n % 2 == 0:
            new.append(n // 2)
    del l[:]
    for n in new:
        l.append(n)

# lst = [1, 2, 3, 4, 5, 6]
# modify_list(lst)
# print(lst)