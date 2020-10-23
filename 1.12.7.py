# Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство сумм и
# выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
# На вход программе подаётся строка из шести цифр.
# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
# Sample Input 1:
# 090234
# Sample Output 1:
# Счастливый
# Sample Input 2:
# 123456
# Sample Output 2:
# Обычный

ticket = input()
numbers = list(ticket)
first = int(numbers.__getitem__(0)) + int(numbers.__getitem__(1)) + int(numbers.__getitem__(2))
second = int(numbers.__getitem__(3)) + int(numbers.__getitem__(4)) + int(numbers.__getitem__(5))
lucky = first == second
if lucky:
    print('Счастливый')
else:
    print('Обычный')
