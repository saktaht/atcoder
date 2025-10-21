N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = [0] * Q
R = [0] * Q

for _ in range(Q):
  L[_], R[_] = map(int, input().split())

atari = [0] * (N + 1)
hazure = [0] * (N + 1)

for i in range(1, N+1):
  atari[i] = atari[i-1]
  if A[i-1] == 1:
    atari[i] += 1
    
  hazure[i] = hazure[i-1]
  if A[i-1] == 0:
    hazure[i] += 1

for i in range(Q):
  atari_sum =atari[R[i]] - atari[L[i]-1]
  hazure_sum = hazure[R[i]] - hazure[L[i]-1]
  # print(sum)
  if atari_sum - hazure_sum > 0:
    print("win")
  elif atari_sum - hazure_sum < 0:
    print("lose")
  else:
    print("draw")