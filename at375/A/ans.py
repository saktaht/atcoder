N = int(input())
S = input()
cnt = 0

for i, char in enumerate(S[:-2]):
  if char == '#' and S[i+1] == '.' and S[i+2] == '#':
    cnt += 1

print(cnt)