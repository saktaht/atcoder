N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = [None] * Q
R = [None] * Q

for i in range(Q):
  L[i], R[i] = map(int, input().split())
  
atari = [0] * (N + 1)
a_s = 0
hazure = [0] * (N + 1)
h_s = 0

for i in range(1, N+1):
  if A[i-1] == 1:
    atari[i] = a_s + 1
    a_s += 1
    # print("atari:", atari[i], i)
  if A[i-1] == 0:
    hazure[i] = h_s + 1
    h_s += 1
    # print("hazure:", hazure[i], i)
  atari[i] = a_s
  hazure[i] = h_s
  # atari[i] = a_s + 1
  # hazure[i] = h_s + 1
  
    
  # print(atari[i])
    
for i in range(Q):
  atari_sum = atari[R[i]] - atari[L[i]-1]
  # print(atari[7])
  hazure_sum = hazure[R[i]] - hazure[L[i]-1]
  # print(atari_sum)
  # print(hazure_sum)
  s = atari_sum - hazure_sum
  
  if s >0:
    print("win")
  elif s == 0:
    print("draw")
  else:
    print("lose")