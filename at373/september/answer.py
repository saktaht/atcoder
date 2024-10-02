answer = 0

for i in range(12):
  num = input()
  if len(num) == i+1:
    answer += 1

print(answer)