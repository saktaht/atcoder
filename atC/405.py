N = int(input())
A = [int(x) for x in input().split()]

total = sum(A)
  
status = 0
for i in A:
  total -= i
  status += i * total
    
print(status)

# こんな感じの表を考えるといい
#     j→     1     2     3
# i↓
#   1         ×   1×2   1×3
#   2         -     ×   2×3
#   3         -     -     ×