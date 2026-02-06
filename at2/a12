N, Q = map(int, input().split())
A = [int(x) for x in input().split()]
L = [0] * Q
R = [0] * Q
S = [0] * (N + 1)

for _ in range(Q):
    l, r = map(int, input().split())
    L[_] = l
    R[_] = r
    
S[0] = 0

for i in range(N):
  S[i+1] = S[i] + A[i]
    
for i in range(Q):
    # print(sum(A[L[i]-1:R[i]]))
    print(S[R[i]] - S[L[i]-1])