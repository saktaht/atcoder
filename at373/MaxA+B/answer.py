n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
# こんな簡単でいいみたい
print(max(a) + max(b))

# max_a = a[0]
# max_b = b[0]

# for i in range(n):
#   if a[i] > max_a:
#     max_a = a[i]
#   if b[i] > max_b:
#     max_b = b[i]
# print(max_a + max_b)