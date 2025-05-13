A = [int(x) for x in input().split()]
a = sorted(A)
sum = 1

for i in range(len(A)-1):
  if A[i] > A[i+1]:
    A[i], A[i+1] = A[i+1], A[i]
    break
  sum += 1

if sum == len(A):
  print('No')
elif A == a:
  print('Yes')
else:
  print('No')