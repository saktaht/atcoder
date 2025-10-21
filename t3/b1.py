def lower_bound(A, X):
  left = 0
  right = N
  while left < right:
    mid = (left + right) // 2
    if A[mid] < X:
      left = mid + 1
    else:
      right = mid # 2分探索みたいにmidを除外していないから、midも候補に入る だからright = mid
  return left


# import bisect

N = int(input()) 
A = list(map(int, input().split()))
sorted_A = sorted(A)
Q = int(input())
X = [0] * Q

for i in range(Q):
  X[i] = int(input())

for i in range(Q):
  answer = lower_bound(sorted_A, X[i])
  print(answer)

# for i in range(Q):
#   answer = bisect.bisect_left(sorted_A, X[i])
#   print(answer)