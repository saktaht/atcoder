import math

N = int(input())
X, Y = map(int, input().split())
cnt = math.sqrt((0-X)**2 + (0-Y)**2)

if N > 1:
  for i in range(N-1):
    X1, Y1 = map(int, input().split())
    cnt += math.sqrt((X-X1)**2 + (Y-Y1)**2)
    X, Y = X1, Y1
    if i == N-2:
      cnt += math.sqrt((X-0)**2 + (Y-0)**2) 
else:
  cnt += math.sqrt((X-0)**2 + (Y-0)**2)

print(cnt)