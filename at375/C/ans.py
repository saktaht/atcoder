# N = int(input())
# B = [list(input()) for _ in range(N)]

# for i in range(1, N//2):
#   X = [x for x in range(i, N + 1 - i)]
#   Y = [y for y in range(i, N + 1 - i)]
#   for x in X:
#     for y in Y:
#       B[y][N-1-x] == B[x][y]
# for i in range(N):
#   print(*B[i])

import numpy as np

N = int(input())
B = np.array([list(input()) for _ in range(N)])

for i in range(1, N//2):
    mask = np.arange(i, N-i)
    x, y = np.meshgrid(mask, mask)
    B[y, N-1-x] = B[x, y]

for row in B:
    print(''.join(row))