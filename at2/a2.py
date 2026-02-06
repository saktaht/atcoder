D = int(input())
N = int(input())
L = [0] * N
R = [0] * N

for i in range(N):
  L[i], R[i] = map(int, input().split())
  
S = [0] * (D+2)
for i in range(N):
  S[L[i]] += 1
  S[R[i]+1] -= 1
  
sum = [0] * (D+2)
for i in range(1, D+1):
  sum[i] = sum[i-1] + S[i]

for i in range(1, D+1):
  print(sum[i])


# s_n = 0
# s_n = [0] * N
# 累積和を出す
# for i in range(1, D+1):
#   for j in range(L[i-1], R[i-1]+1):
#     S[j] =  s_n + 1
  
# # 日にちごとの人数を計算
# for i in range(N):
#   sum = S[R[i]] - S[L[i]-1]
  
# # 答えを出す
# for i in range(D):
#   print(S[i])