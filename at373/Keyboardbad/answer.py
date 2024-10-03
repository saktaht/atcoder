# str = input()
# x = [0]*26
# # 例えば、str = "BCADEF...Z"（仮に26文字）だとします。
# # 最初に x = [0]*26 で、x は26個の0からなるリストです。
# # ループの最初のステップでは、i = 0 のとき、str[0] は "B" です。
# # ord("B") - ord("A") は 66 - 65 = 1 となります。
# # これにより、x[1] = 0 となり、リスト x の2番目の位置に 0 が格納されます（"B" が0番目にあるため）。
# # 次に、i = 1 のとき、str[1] は "C" です。
# # ord("C") - ord("A") は 67 - 65 = 2 です。
# # x[2] = 1 となり、リスト x の3番目に 1 が格納されます（"C" が1番目にあるため）。
# for i in range(26):
#   x[ord(str[i]) - ord("A")] = i 
  
# ans = 0
# for i in range(25):
#   # アルファベットの順番で探索して行って、今のアルファベットともう一つ先のアルファベットの差の絶対値を足していく
#   ans += abs(x[i] - x[i+1])
# print(ans)

s = input()
x = [0] * 26

for i in range(26):
  x[ord(s[i]) - ord('A')] = i

total = 0
for i in range(25):
  total += abs(x[i+1] - x[i])
print(total)