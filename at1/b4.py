N = input()
status = 0
limit=8

for j in range(len(N)-1, -1, -1):
  N_num = len(N) - 1 - j
  status += int(N[N_num])*(2**j)
print(status)