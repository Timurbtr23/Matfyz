import numpy as np

n = int(input())
matrix = []
for i in range(n):
    matrix.append(input().split())
    matrix[i] = list(map(int, matrix[i]))

a = np.zeros((n, n + 1))
x = np.zeros(n)
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(matrix[i][j])

for i in range(n):
    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]
        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]

x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]
    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]
    x[i] = x[i] / a[i][i]

for i in range(n):
    if i != n-1:
        print(x[i])
    else:
        print(x[i], end="")
