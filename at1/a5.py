N, K = map(int, input().split())

count = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    h = K - (i + j)
    if h >= 1 and h <= N:
      count += 1
        
print(count)