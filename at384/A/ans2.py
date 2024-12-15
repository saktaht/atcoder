# 3文字mapでよかった
n, x, y = map(str, input().split())
n = int(n)
# ただのinputで十分
s = input()
t = ""
for i in range(n):
    if s[i] == x:
        t += x
    else:
        t += y
print(t)
