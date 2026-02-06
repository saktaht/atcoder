D = int(input())
N = int(input())
L = [None] * N
R = [None] * N

for i in range(N):
  L[i], R[i] = map(int, input().split())
  
# 参加者数の日付ごとの人数
S = [0] * (D+2)
for i in range(N):
  S[L[i]] += 1
  S[R[i]+1] -= 1
  
# 合計値を求めるanswer
take_part_people = [0] * (D+2)
for i in range(1, D+1):
  take_part_people[i] = take_part_people[i-1] + S[i]
  print(take_part_people[i])