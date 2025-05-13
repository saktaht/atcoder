A, B = map(int, input().split())
yakusu = []

for i in range(A, B+1):
  if (100 % i == 0):
    yakusu.append(i)

if (yakusu):
  print('Yes')
else:
  print('No')