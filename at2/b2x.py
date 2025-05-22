T = int(input())
N =int(input())
L = [None] * N
R = [None] * N

for i in range(N):
  L[i], R[i] = map(int, input().split())
  
count = [0] * (T+1)
for i in range(N):
  count[L[i]] += 1
  count[R[i]] -= 1

total = [None] * (T+1)
total[0] = count[0]
for i in range(1, T+1):
  total[i] = total[i-1] + count[i]

for i in range(T):
  print(total[i])