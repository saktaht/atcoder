import sys

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S+1) for _ in range(N+1)]

dp[0][0] = True

for i in range(1, S+1):
  dp[0][i] = False
  
for i in range(1, N+1):
  for j in range(S+1):
    if j < A[i-1]:
      if dp[i-1][j] == True:
        dp[i][j] = True
      else:
        dp[i][j] = False
        
    if j >= A[i-1]:
      if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
        dp[i][j] = True
      else:
        dp[i][j] = False
        
if dp[N][S] == False: 
  print("-1")
  # sys.exitって何？ → 0は正常終了を意味する
  sys.exit(0)
  
# そもそもここにきている時点でSは満たせることが確定
Answer = []
place = S
# なんで1からループを始めてるのか → 0枚目の列はFalseで埋まってるから
for i in reversed(range(1, N+1)): 
  # この操作は何をやってるの？そもそも何でFalseのものをAnswerに追加してるの？
  # → dp[i-1][place]==TrueということはA[i-1]を使わなくてもSを満たしてるってこと 
  # → もう一つ下のdp[i-2][place]でも成り立つかもしれないからcontinue
  if dp[i-1][place] == True:
    continue
  else:
    place = place - A[i-1]
    Answer.append(i)
Answer.reverse()

# Answer2 = [str(i) for i in Answer]
print(len(Answer))
# print(" ".join(Answer2))
print(*Answer)