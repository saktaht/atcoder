D = int(input())
N = int(input())
L = [None] * N
R = [None] * N

for i in range(N):
  L[i], R[i] = map(int, input().split())
  
# 0日目から始まると面倒だからD+1で0を埋めといて、R[i]+1で一個先の値にアクセスする必要があるからD+1する必要がある→D+2になる
B = [ 0 ] * (D+2)
for i in range(N):
  B[L[i]] += 1
  B[R[i]+1] -= 1

# 累積和を求める
answer = [None] * (D+2)
answer[0] = 0
for i in range(1, D+1):
  answer[i] = answer[i-1] + B[i]

for i in range(1, D+1):
  print(answer[i])