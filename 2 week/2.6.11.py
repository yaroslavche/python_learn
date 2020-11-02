# Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и
# закрученной по часовой стрелке, как показано в примере (здесь n=5):
# Sample Input:
# 5
# Sample Output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# 1 2 3
# 8 9 4
# 7 6 5

n = int(input())
i, j, di, dj = 0, 0, 1, 0
matrix = [[0 for _ in range(n)] for _ in range(n)]
for position in range(1, n ** 2 + 1):
    matrix[i][j] = position
    ni, nj = i + di, j + dj
    if 0 <= ni < n and 0 <= nj < n and not matrix[ni][nj]:
        i, j = ni, nj
    else:
        di, dj = -dj, di
        i, j = i + di, j + dj
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[j][i], end=' ')
    print()
