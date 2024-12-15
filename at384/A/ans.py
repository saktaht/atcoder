N = input()
n = int(N[0])
c1 = N[-3]
c2 = N[-1]

S = [x for x in input().split()]
S = str(S[0])
s = []

for i in S:
  if i != c1:
    i = c2
  s.append(i)

new = ''.join(s)
print(new)