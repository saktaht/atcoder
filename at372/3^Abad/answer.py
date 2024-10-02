# 自分で考えたコード
# import math

# n = int(input())
# remainder = 0
# for i in range(int(math.sqrt(n)), 0, -1):
#   if n > 3**i:
#     remainder = n % (3**i)
#     print(remainder, end=' ')

m = int(input())
a = []
for i in range(11):
  # nを3で割ったあまり(0, 1, 2)のどれかの数、iのリストを作り、aに追加する
  a += [i] * (m%3)
  m //= 3
print(len(a))
# A の要素をスペース区切りで出力.
# *A という構文はリストのアンパックと呼ばれ、リストの要素を1つずつ出力するのに使います
print(*a)