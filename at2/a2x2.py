D = int(input())
N = int(input())
L = [None] * N
R = [None] * N

for i in range(N):
  L[i], R[i] = map(int, input().split())

# その日初参加か行くのをやめる人の、出席する人数をカウント
count = [0] * (D+2)
for i in range(N):
  count[L[i]] += 1 
  count[R[i]+1] -= 1
# print(count)

# countで得たその日に出席する人の人数を数えていく → 1日ごとに初参加の数だけ増えて、やめる人の数だけ減る
total = [None] * (D+2)
total[0] = 0
for i in range(1, D+1):
  total[i] = total[i-1] + count[i]

for i in range(1, D+1):
  print(total[i])