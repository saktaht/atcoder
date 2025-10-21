def check(m, N, K, A) -> bool:
  sum = 0
  # 各機械のプリンタの合計を求める
  for i in range(N):
    sum  += m // A[i] 
  
  if sum >= K:
    return True
  return False

N, K = map(int, input().split())
A = list(map(int, input().split()))

Left = 1
Right = 10 ** 9
while Left < Right:
  Mid = (Left + Right) // 2
  Answer = check(Mid, N, K, A)
  
  if Answer == False:
    Left = Mid + 1
  if Answer == True:
    Right = Mid

print(Left)