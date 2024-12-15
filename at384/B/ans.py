N, R = map(int, input().split())

a = [list(map(int,input().split(" "))) for _ in range(N)]
total = R

for i in range(N):
  if a[i][0] == 1:
    if total >= 1600 and total <= 2799:
      total += a[i][1]
  else:
    if total >= 1200 and total <= 2399:
      total += a[i][1]
print(total)