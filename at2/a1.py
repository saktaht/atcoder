N, Q = map(int, input().split())
A = [int(x) for x in input().split()]
paris= [list(map(int, input().split())) for _ in range(Q)]

cumulative_sum = 0
cumulative_list = []

for i in range(N):
  cumulative_sum += A[i]
  cumulative_list.append(cumulative_sum)
  
# print(cumulative_list)

answer = []
for par in paris:
  start = par[0]-1
  end = par[1]-1
  # print(start, end)
  if start == 0:
    answer.append(cumulative_list[end])
  else: 
    answer.append(cumulative_list[end]-cumulative_list[start-1])

for i in answer:
  print(i)