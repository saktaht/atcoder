H, W = map(int, input().split())
X = [ None ] * H
for i in range(H):
  X[i] = list(map(int, input().split()))
Z = [[ 0 ] * (W+1) for i in range(H+1)]

Q = int(input())
A = [ None ] * Q
B = [ None ] * Q
C = [ None ] * Q
D = [ None ] * Q
for i in range(Q):
  A[i], B[i], C[i], D[i] = map(int, input().split())
  
# 横列の累積和
for h in range(1, H+1):
  for w in range(1, W+1):
    Z[h][w] = Z[h][w-1] + X[h-1][w-1]
    
# 盾の累積和
for h in range(1, H+1):
  for w in range(1, W+1):
    Z[h][w] = Z[h-1][w] + Z[h][w]
    
for i in range(Q):
  print(Z[C[i]][D[i]] + Z[A[i]-1][B[i]-1] - Z[A[i]-1][D[i]] -Z[C[i]][B[i]-1])