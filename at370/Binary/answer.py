n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#   temp = list(map(int, input().split()))
#   A.append(temp)
ans = 1
for i in range(n):
  ans = A[max(ans-1, i)][min(ans-1, i)]
print(ans)