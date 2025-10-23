N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * (N + 1)
dp[1] = 0
dp[2] = A[0]

for i in range(3, N+1):
  dp[i] = min(dp[i-1] + A[i-2], dp[i-2] + B[i-3])
  
Answer = []
place = N
while True:
  Answer.append(place)
  if place == 1:
    break

  # 上の"dp[i-1] + A[i-2]" この部分とやってることは一緒 Aだったら1つ前に移動、Bだったら2つ前に移動
  if dp[place-1] + A[place-2] == dp[place]:
    place = place - 1
  else:
    place = place - 2
      
Answer.reverse()

# Answer2 = [str(i) for i in Answer]
print(len(Answer))
# print(" ".join(Answer2))
print(*Answer)