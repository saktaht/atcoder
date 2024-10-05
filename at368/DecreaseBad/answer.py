# 自分で解けなかった
# N = int(input())
# A = list(map(int, input().split()))
# judge = [True for _ in range(N)]
# count = 0

# while True:
#   new_list = sorted(A)
#   new_list[0] -= 1
#   new_list[1] -= 1
#   count += 1
#   false_count = 0
#   A = new_list
#   for i in range(N):
#     if A[i] <= 0:
#       judge[i] = False
#       false_count += 1
      
#   if false_count >= N-1:
#     break

# print(count)

N = int(input())
A = list(map(int, input().split()))
count = 0

while A.count(0) < N-1:
  # reverse=Trueとすることで、降順ソートが簡単にできます
  A.sort(reverse=True)
  A[0] -= 1
  A[1] -= 1
  count += 1
print(count)