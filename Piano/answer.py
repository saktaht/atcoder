# 自分で解けなかった
# N = int(input())
# a, s = input().split()
# a = int(a)
# tired = 0

# for i in range(N-1):
#   a1, s1 = input().split()
#   a1 = int(a1)
#   if s1 == 'R':
#     tired = abs(a-a1)
#   if s1 == 'L':
#     tired = abs(a-a1)
# print(tired)

N = int(input())
pos = [-1, -1] # 0: left, 1: right
ans = 0

for i in range(N):
  a, s = input().split()
  a = int(a)
  # ここで手を0と1で分ける発想ができなかった
  hand = (0 if s == "L" else 1)
  # posの初期値を-1に設定することで最初の処理は飛ばせる
  if pos[hand] != -1:
    ans += abs(pos[hand] - a)
  pos[hand] = a
print(ans)