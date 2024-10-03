# 自分で考えたやつ
# n, m= map(int, input().split())
# list = []
# for i in range(m):
#     a,b=input().split()
#     list.append((int(a), b))

# for i in range(m):
#   if list[] == "M":
#     print('Yes')
#   else:
#     print('No')

n, m = map(int, input().split())
taro_exist = [False for i in range(n)]
for i in range(m):
  a, b = input().split()
  # 家の数は1から数えるから、aには1からしか入力されない。だから0からスタートするために-1する
  a = int(a) - 1
  if b == "F" or taro_exist[a]:
    print('No')
  else:
    taro_exist[a] = True
    print('Yes')