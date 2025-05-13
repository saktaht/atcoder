N = int(input())

status = []
limit = 10

for i in range(limit-1, -1, -1):
  if ((N // 2**i) >= 1):
    status.append(1)
    N -= 2**i
  else: 
    status.append(0)

for i in status:
  print(i, end='')