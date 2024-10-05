S = input()
T = input()

# 1の処理
if S == T:
  print(0)
  
# 2, 3の処理
else:
  #3の前処理
  s_len, t_len = len(S), len(T)
  count = 0
  # 2の処理......
  for i in range(min(s_len, t_len)):
    if S[i] != T[i]:
      break
    count = i + 1
    # if S[i] == S[-1:]:
    #   break
  if count == min(s_len, t_len):  # すべての文字が一致しているが長さが違う場合
    print(count + 1)
  else:
    print(count + 1)