N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(1, S + 1):
  dp[0][i] = False

for i in range(1, N + 1):
  for j in range(S + 1):
    # 合計値がA[i-1]より小さい場合（A[i-1]が使えない場合）
    if j < A[i-1]:
      # 合計値（S）がdp[2][1]でtureと出てたなら、dp[3][1]もtureだよねって言ってるだけ
      if dp[i-1][j] == True: 
        dp[i][j] = True
      else:
        dp[i][j] = False
        
    # 合計値がA[i-1]以上の場合（A[i-1]が使える場合）
    if j >= A[i-1]:
      # 上の条件分 or 今回使える数字(A[i-1])が一つ前の合計値でtureと出てたなら、dp[i][j]もtureだよねって言ってるだけ
      if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True: 
        dp[i][j] = True
      else:
        dp[i][j] = False
        
if dp[N][S] == True:
  print("Yes")
else:
  print("No")