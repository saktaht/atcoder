N = int(input())
A = [int(x) for x in input().split()]
Q = int(input())
L = [None] * Q
R = [None] * Q

for i in range(Q):
  L[i], R[i] = map(int, input().split())
  
atari = [0] * (N+1)
hazure = [0] * (N+1)
for i in range(1, N+1):
  atari[i] = atari[i-1] # 前回のあたりの数を引き継ぐ
  hazure[i] = hazure[i-1]
  if A[i-1] == 1:
    atari[i] += 1
    # print("あたりは", atari)
  else:
    hazure[i] += 1
    # print("ハズレは", hazure)
    
for i in range(Q):
  numAtari = atari[R[i]] - atari[L[i]-1]
  numhazure =  hazure[R[i]] -  hazure[L[i]-1]
  if numAtari > numhazure:
    print("あたり")
  elif numAtari < numhazure:
    print("ハズレ")
  else:
    print("引き分け")