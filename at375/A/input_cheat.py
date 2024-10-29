# 入力編
# M Nの時
N, M = map(int, input().split())

#A1, A2, ... Anの時
A = [int(x) for x in input().split()]
# or
A = list(map(int, input().split()))

# 0 縦に入力したい時
# 1
# 2
# ...
# Nの時
a = [int(input()) for _ in range(N)]
# print(a) -> [0, 1, 2, 3, 4]

# Nの2次元配列
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
a = [ list(map(int,input().split(" "))) for _ in range(N)]
# print(a) -> [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

