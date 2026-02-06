N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [None] * Q
R = [None] * Q

for i in range(Q):
  L[i], R[i] = map(int, input().split())
  # print(L[i], R[i])
  
S = [0] * (N+1)
for i in range(1, N+1):
  S[i] = S[i-1] + A[i-1]
  # print(S[i])
  
for i in range(Q):
  sum = S[R[i]] - S[L[i]-1]
  print(sum)