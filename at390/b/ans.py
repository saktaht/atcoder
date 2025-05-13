from decimal import Decimal

N = int(input())
A = [int(x) for x in input().split()]

count = 1
div = Decimal(A[1])/Decimal(A[0])

for i in range(N-1):
  start = A[i]
  if Decimal(A[i+1])/Decimal(A[i]) != div:
    print('No')
    break
  count += 1
if count == N:
  print('Yes')
