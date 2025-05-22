H, W, N = map(int, input().split())
A = [None] * N
B = [None] * N
C = [None] * N
D = [None] * N
for i in range(N):
  A[i], B[i], C[i], D[i] = map(int, input().split())
  
#  累積和を求める下準備
X = [[0]*(W+2) for _ in range(H+2)]
for i in range(N):
  X[A[i]][B[i]] += 1
  X[A[i]][D[i]+1] -= 1
  X[C[i]+1][B[i]] -= 1
  X[C[i]+1][D[i]+1] += 1  

Z = [[0]*(W+2) for _ in range(H+2)]
for h in range(1, H+1):
  for w in range(1, W+1):
    Z[h][w] = Z[h][w-1] + X[h][w]
    
for w in range(1, W+1):
  for h in range(1, H+1):
    Z[h][w] = Z[h-1][w] + Z[h][w]
    
for i in range(1, H+1):
  for j in range(1, W+1):
    if j >= 2:
      print(" ", end="")
    print(Z[i][j], end="")
  print("")