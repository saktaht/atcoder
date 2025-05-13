N, X = map(int, input().split())
A = [int(x) for x in input().split()]

status = True
for i in A:
  if (i == X):
    # print('Yes')
    status = True
    break
  else:
    status = False

if status:
  print('Yes')
else: 
  print('No')