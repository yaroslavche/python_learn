n = int(input())
if n >= 0:
    word = 'программист'
    mod20 = n % 20
    eleven = mod20 > 10 and int(n / 20) % 5 == 0
    if mod20 == 1 or (mod20 == 11 and not eleven):
        word = word
    elif mod20 == 0 or 5 <= mod20 <= 10 or 15 <= mod20 <= 19 or eleven:
        word += 'ов'
    else:
        word += 'а'
    print(n, word)
