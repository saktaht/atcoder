N, Q = map(int, input().split())
A = [int(x) for x in input().split()]
L = [None] * Q
R = [None] * Q

for j in range(Q):
  L[j], R[j] = map(int, input().split())

sum = [None] * (N+1)
sum[0] = 0
for i in range(N):
  sum[i+1] = sum[i] + A[i]

for i in range(Q):
  # print(R[i], L[i]-1)
  print(sum[R[i]]-sum[L[i]-1])