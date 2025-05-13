N = int(input())
A = [int(x) for x in input().split()]

status = False
for i in range(N):
  for j in range(i+1, N):
    for l in range(j+1, N):
      if A[i] + A[j] + A[l] == 1000:
        status = True

if status == True:
  print('Yes')
else:
  print('No')