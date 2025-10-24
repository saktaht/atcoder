N = int(input())
H = list(map(int, input().split()))

dp = [0] * N
dp[1] = abs(H[0] - H[1])

for i in range(2, N):
  dp[i] = min(dp[i-1] + abs(H[i] - H[i-1]), dp[i-2] + abs(H[i] - H[i-2]))
  
# print(dp[N-1])

Answer = []
place = N - 1
while True:
  Answer.append(place+1)
  # print(place)
  if place == 0:
    break
  # if place == 2:
  #   place = place - 1
  #   continue
  if dp[place] == dp[place-1] + abs(H[place-1] - H[place]):
    place = place - 1
    continue
  if dp[place] == dp[place-2] + abs(H[place] - H[place-2]):
  # else:
    place = place - 2
    continue
    

Answer.reverse()
print(len(Answer))
print(*Answer)