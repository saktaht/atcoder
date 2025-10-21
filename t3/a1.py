def search(X, A):
  pointer_left = 0
  pointer_right = N - 1 #配列のインデックスぶん引いてる

  while pointer_left <= pointer_right:
    pointer_middle = (pointer_left + pointer_right) // 2
    
    if A[pointer_middle] == X:
      return pointer_middle
      break    
    elif A[pointer_middle] < X:
      pointer_left = pointer_middle + 1
    else:
      pointer_right = pointer_middle - 1
      
  return -1
      
N, X = map(int, input().split())
A = list(map(int, input().split()))
answer = search(X, A)
# プログラミングの配列は0から数え始めるため、そこに+1して出力する
print(answer + 1)

# -------------------モジュールを使うと-------------------
# import bisect

# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# answer = bisect.bisect_left(A, X)
# print(answer + 1)